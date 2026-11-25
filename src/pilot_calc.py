"""Nhiệm vụ D (CP4) · Cỡ mẫu và dữ liệu nền cho pilot_plan.yaml.
Chạy trong thư mục src/:  python3 pilot_calc.py
Chỉ cần thư viện chuẩn của Python. Nếu có statsmodels thì in thêm số đối chiếu.
Tham số cho sẵn: baseline 0,70; mục tiêu +5 điểm; alpha 0,05; power 0,8; ICC 0,02.
"""
import csv
import math
from collections import Counter, defaultdict
from statistics import NormalDist

BASELINE = 0.70
MDE = 0.05
ALPHA = 0.05
POWER = 0.80
ICC = 0.02
N_NHAN_VIEN = 40
N_DEPOT = 12

_N = NormalDist()


def co_mau(p1, p2, alpha=ALPHA, power=POWER):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (công thức của đề)."""
    za, zb = _N.inv_cdf(1 - alpha / 2), _N.inv_cdf(power)
    pb = (p1 + p2) / 2
    tu = za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return math.ceil(tu ** 2 / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc=ICC):
    return 1 + (m - 1) * icc


def mau_hieu_dung(c, m, icc=ICC):
    """Cỡ mẫu hiệu dụng mỗi nhóm khi chia theo cụm: c cụm, m yêu cầu mỗi cụm."""
    return c * m / he_so_thiet_ke(m, icc)


def m_toi_thieu(c, n_can, icc=ICC):
    """Số yêu cầu tối thiểu mỗi cụm để c cụm đạt cỡ mẫu hiệu dụng n_can.
    Giải c·m / (1 + (m-1)·icc) >= n_can  ->  m >= n_can·(1-icc) / (c - n_can·icc)."""
    mau = c - n_can * icc
    if mau <= 0:
        return None  # c / icc <= n_can: không bao giờ đạt
    return math.ceil(n_can * (1 - icc) / mau)


def power_voi_n(p1, p2, n, alpha=ALPHA):
    """Power xấp xỉ khi mỗi nhóm có n quan sát hiệu dụng."""
    za = _N.inv_cdf(1 - alpha / 2)
    pb = (p1 + p2) / 2
    se0 = math.sqrt(2 * pb * (1 - pb) / n)
    se1 = math.sqrt((p1 * (1 - p1) + p2 * (1 - p2)) / n)
    return _N.cdf((abs(p2 - p1) - za * se0) / se1)


def d1():
    print('=== D1 · Cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02) ===')
    n_a = co_mau(BASELINE, BASELINE + MDE)
    print(f'a) Chia theo yêu cầu: {n_a:,} yêu cầu mỗi nhóm (hệ số thiết kế 1)')

    de_b = he_so_thiet_ke(75)
    n_b = math.ceil(n_a * de_b)
    nv_nhom = math.ceil(n_b / 75)
    print(f'b) Theo nhân viên, m = 75: DE = {de_b:.2f}; {n_b:,} yêu cầu mỗi nhóm '
          f'-> {nv_nhom} nhân viên mỗi nhóm, tổng {2 * nv_nhom} '
          f'({"đủ" if 2 * nv_nhom <= N_NHAN_VIEN else "KHÔNG đủ"} so với {N_NHAN_VIEN} nhân viên)')

    gh_c = 20 / ICC
    print(f'c) 20 nhân viên mỗi nhóm: cỡ mẫu hiệu dụng tối đa = 20 / 0,02 = {gh_c:,.0f} '
          f'({"đạt" if gh_c >= n_a else "KHÔNG đạt"} so với {n_a:,})')

    gh_d = 6 / ICC
    print(f'd) 6 depot mỗi nhóm: cỡ mẫu hiệu dụng tối đa = 6 / 0,02 = {gh_d:,.0f}')

    n_6 = co_mau(BASELINE, BASELINE + 0.06)
    m_e = m_toi_thieu(20, 859)
    print(f'e) Mức chênh 6 điểm (tính lại: {n_6:,}/nhóm; đề cho 859), 20 nhân viên mỗi nhóm: '
          f'm >= {m_e} yêu cầu mỗi nhân viên (DE = {he_so_thiet_ke(m_e):.2f}, '
          f'hiệu dụng = {mau_hieu_dung(20, m_e):,.0f})')
    m_chk = m_toi_thieu(20, n_6)
    print(f'   (nếu dùng {n_6:,} thay vì 859 thì m >= {m_chk})')

    pw = power_voi_n(BASELINE, BASELINE + MDE, 859)
    print(f'   Nếu thiết kế cho 6 điểm (859/nhóm) mà tác động thật chỉ 5 điểm: power ~ {pw:.2f}')
    return {'n_a': n_a, 'de_e': he_so_thiet_ke(m_e), 'm_e': m_e}


def doi_chieu_statsmodels(n_a):
    try:
        from statsmodels.stats.power import NormalIndPower
        from statsmodels.stats.proportion import proportion_effectsize
    except ImportError:
        print('(chưa cài statsmodels, bỏ qua bước đối chiếu)')
        return
    es = proportion_effectsize(BASELINE + MDE, BASELINE)
    n = NormalIndPower().solve_power(effect_size=es, alpha=ALPHA, power=POWER, ratio=1.0)
    print(f'Đối chiếu statsmodels: {math.ceil(n):,} mỗi nhóm (công thức tay: {n_a:,})')


def doc_yeu_cau(path='logix_requests.csv'):
    with open(path, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def du_lieu_nen(reqs):
    print('\n=== Dữ liệu nền cho luật an toàn (không dùng cột _simulated) ===')
    tong = len(reqs)
    mo_lai = sum(int(r['mo_lai_trong_7_ngay']) for r in reqs)
    dong = sum(int(r['dong_trong_24h']) for r in reqs)
    print(f'Tổng yêu cầu: {tong:,}; nhân viên: {len({r["staff_id"] for r in reqs})}; '
          f'depot: {len({r["depot"] for r in reqs})}')
    print(f'mo_lai_trong_7_ngay: {mo_lai}/{tong} = {mo_lai / tong:.2%}')
    print(f'dong_trong_24h: {dong}/{tong} = {dong / tong:.2%}')

    pham_vi = [r for r in reqs if r['loai'] in ('noi_dia', 'hang_nang')]
    mo_pv = sum(int(r['mo_lai_trong_7_ngay']) for r in pham_vi)
    print(f'Phạm vi noi_dia + hang_nang: mo_lai {mo_pv}/{len(pham_vi)} = {mo_pv / len(pham_vi):.2%}')

    print('Theo loại:')
    theo_loai = defaultdict(lambda: [0, 0])
    for r in reqs:
        theo_loai[r['loai']][0] += 1
        theo_loai[r['loai']][1] += int(r['mo_lai_trong_7_ngay'])
    for loai, (n, m) in sorted(theo_loai.items()):
        print(f'  {loai:10s} n={n:4d}  mo_lai={m / n:.2%}')

    dem = Counter(r['staff_id'] for r in reqs)
    print(f'Số yêu cầu mỗi nhân viên trong mẫu: min {min(dem.values())}, '
          f'max {max(dem.values())}, TB {tong / len(dem):.1f}')


if __name__ == '__main__':
    ket_qua = d1()
    doi_chieu_statsmodels(ket_qua['n_a'])
    du_lieu_nen(doc_yeu_cau())
