"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py (cần pandas; statsmodels dùng để đối chiếu D1).
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

from pilot_calc import d1, doc_yeu_cau, doi_chieu_statsmodels, du_lieu_nen

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p if p else math.inf
    return ti_le_thanh_cong(p, k) / p if p else k


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k == 0 or p == 0:
        return 0.0
    if k is None or p == 1:
        return 1.0
    return -math.expm1(k * math.log1p(-p))


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    thanh_cong = ti_le_thanh_cong(p, k)
    return so_lan_chay_ky_vong(p, k) / thanh_cong if thanh_cong else math.inf


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        reqs = reqs[reqs['so_lan_chay'] <= max_lan_chay]

    token = (runs['tokens_in'] * gia_vao + runs['tokens_out'] * gia_ra) / 1000
    tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token.sum() + tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(token=token.sum(), tool=tool.sum(),
                chay_lai=(token + tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong if thanh_cong else math.inf)


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    hoa_don = (ket_qua['token'] + ket_qua['tool']) / len(reqs)
    print(f'Hóa đơn token và tool/yêu cầu: {hoa_don:,.2f} đ')
    print(f'Hệ số CPS/hóa đơn: {ket_qua["cps"] / hoa_don:.2f}')
    print(f'Tỷ trọng làm lại: {ket_qua["lam_lai"] / ket_qua["tong"]:.2%}')

    print('\nA3 · Loại | yêu cầu | thành công | lần chạy/yêu cầu | CPS simulated')
    for loai, nhom in reqs.groupby('loai'):
        model = mo_hinh(runs, nhom)
        print(f'{loai}: {len(nhom)} | {model["thanh_cong"] / len(nhom):.2%} | '
              f'{nhom["so_lan_chay"].mean():.2f} | {model["cps"]:,.2f}')
    quoc_te = runs[runs['request_id'].isin(reqs.loc[reqs['loai'] == 'quoc_te', 'request_id'])]
    print('Tỷ lệ ok quốc tế theo lần:', quoc_te['status'].eq('ok').groupby(quoc_te['attempt']).mean().to_dict())

    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    model_pham_vi = mo_hinh(runs, pham_vi)
    print('\nA4 · Khối lượng toàn hệ thống | thành công trong phạm vi | cố định/việc | CPS simulated')
    for khoi_luong in (45000, 22500):
        thanh_cong_thang = khoi_luong * model_pham_vi['thanh_cong'] / len(reqs)
        co_dinh = 40_000_000 / thanh_cong_thang
        print(f'{khoi_luong:,} | {thanh_cong_thang:,.0f} | {co_dinh:,.2f} | '
              f'{model_pham_vi["cps"] + co_dinh:,.2f}')

    kich_ban = {
        'Token ×2': dict(gia_vao=52, gia_ra=260),
        'Token ×0.5': dict(gia_vao=13, gia_ra=65),
        'Xem lại ×2': dict(he_so_xem_lai=2),
        'Xem lại ×0.5': dict(he_so_xem_lai=0.5),
        'Làm lại ×2': dict(he_so_lam_lai=2),
        'Làm lại ×0.5': dict(he_so_lam_lai=0.5),
        'Lương +25%': dict(luong_phut=2500),
        'Tối đa 2 lần': dict(max_lan_chay=2),
        'Tối đa 1 lần': dict(max_lan_chay=1),
    }
    print('\nB1–B2 · Kịch bản | CPS simulated | thay đổi')
    for ten, tham_so in kich_ban.items():
        cps = mo_hinh(runs, reqs, **tham_so)['cps']
        print(f'{ten}: {cps:,.2f} | {cps / ket_qua["cps"] - 1:+.2%}')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'Token và xem lại ×2: {cps_cap:,.2f} | {cps_cap / ket_qua["cps"] - 1:+.2%}')

    print('\nB3 · Giới hạn | tổng trợ lý | không thành công | cả hệ thống | CPS simulated')
    for gioi_han in (1, 2, 3):
        model = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        that_bai = len(reqs) - model['thanh_cong']
        ca_he_thong = model['tong'] + BASELINE * that_bai
        print(f'{gioi_han} | {model["tong"]:,.2f} | {that_bai} | {ca_he_thong:,.2f} | {model["cps"]:,.2f}')

    print('\nB4 · Phút làm lại/ca | CPS simulated | phút xem lại hòa vốn')
    ok = runs['status'].eq('ok') & runs['request_id'].isin(pham_vi['request_id'])
    so_ca_xem = runs.loc[ok, 'request_id'].nunique()
    lam_lai = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated']
    so_ca_lam_lai = pham_vi['ket_qua'].eq('lam_lai').sum()
    for phut_lam_lai in (9, round(lam_lai.mean(), 1)):
        chi_phi_khac = model_pham_vi['token'] + model_pham_vi['tool'] + so_ca_lam_lai * phut_lam_lai * LUONG_PHUT
        cps = (chi_phi_khac + so_ca_xem * 5 * LUONG_PHUT) / model_pham_vi['thanh_cong']
        hoa_von = (BASELINE * model_pham_vi['thanh_cong'] - chi_phi_khac) / (so_ca_xem * LUONG_PHUT)
        print(f'{phut_lam_lai:g} | {cps:,.2f} | {hoa_von:.2f}')
    print()
    co_mau_pilot = d1()
    doi_chieu_statsmodels(co_mau_pilot['n_a'])
    du_lieu_nen(doc_yeu_cau())
