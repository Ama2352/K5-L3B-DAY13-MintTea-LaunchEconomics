# Báo cáo nhóm · MintTea (L3B)

Thành viên và phân công được ghi trong [TEAM.md](../../TEAM.md).

## Mục tiêu và cách làm

Đánh giá tính khả thi về chi phí của trợ lý hoàn phí LogiX-VN và chuẩn bị kế hoạch pilot có đối chứng. Nhóm dùng 1.624 trace liên kết với 1.200 yêu cầu giả lập. Chi phí token và công cụ cộng trên mọi lượt chạy. Chi phí xem lại và làm lại dùng phút simulated.

| Phần | Cách làm và bằng chứng |
| --- | --- |
| A · Chi phí | Kiểm tra ba công thức chạy lại, tính chi phí theo trace, chia bốn loại yêu cầu và cộng chi phí cố định cho phạm vi pilot. [Bảng chi phí](bang_chi_phi.md) |
| B · Độ nhạy | Chạy chín thay đổi riêng và một cặp. So sánh giới hạn 1–3 lần theo chi phí toàn hệ thống và giả lập xem lại 100% đầu ra. [Bảng độ nhạy](bang_chi_phi.md#b1--đổi-từng-yếu-tố) |
| C · Lỗi | Chờ hai bộ nhãn độc lập, đồng thuận và bảng khắc phục năm ca. [Bảng lỗi](bang_loi.md) |
| D · Pilot | Chờ cỡ mẫu, phương án chia có đối chứng, luật dừng và lịch quyết định. [Kế hoạch pilot](pilot_plan.yaml) |
| E · Gate 2a | Hồ sơ v0 đã tổng hợp kinh tế. Chờ đặc tả chỉ số, event và kết quả duyệt chéo. [Chỉ số](chi_so.md) · [Hồ sơ launch](ho_so_launch_v0.md) |

## Kết quả và giới hạn

CPS toàn mẫu là **4.472 đ** (simulated), gấp **16,28 lần** hóa đơn token và công cụ mỗi yêu cầu. Làm lại chiếm **51,77%** tổng chi phí (simulated). Chi phí toàn hệ thống theo quy ước B3 thấp nhất khi giới hạn **2 lần**, ở **6.901.220 đ** cho 1.200 yêu cầu (simulated). Nội địa và hàng nặng là phạm vi đề xuất xem xét. Xem lại toàn bộ đầu ra có thể đẩy CPS lên **12.415 đ** (simulated), vượt baseline 12.000 đ.

Giờ nhân viên và chi phí tháng là đầu vào giả lập. Mẫu quan sát phục vụ mô hình chi phí. Pilot có đối chứng cần kiểm tra hiệu quả thực tế, mức sử dụng và tỷ lệ mở lại sau 7 ngày. Đề xuất hiện tại là **No-go** tại Gate 2a, chờ hoàn tất bằng chứng trong [hồ sơ launch](ho_so_launch_v0.md). Kết quả hội đồng chờ duyệt chéo.

## Tài liệu

[Công thức và giả định](../../docs/du_lieu_va_cong_thuc.md) · [Hướng dẫn chi tiết](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md)
