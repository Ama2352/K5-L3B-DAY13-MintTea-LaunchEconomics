# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Thảo Quyên · Người gắn nhãn 2: Quỳnh Anh (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngầm | Ngữ cảnh | Không | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 19 / 20 = 95%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 3 (Ngầm vs Ngữ cảnh) → Ngữ cảnh:** khách đã báo "chưa được hoàn" nên lỗi đã lộ ra, không phải lỗi ngầm; trợ lý hoàn đúng thiết kế (ví LogiX trong 5 phút), chỉ giả định "tiền về ngân hàng" không khớp kỳ vọng của khách. Ngầm chỉ dùng khi cả khách lẫn hệ thống đều không nhận ra cho tới khi kiểm tra.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 14 | Do người dùng | Event `confirm_received_clicked` mà 24 giờ sau có `reopen_request` hoặc khiếu nại cùng `trace_id`; cảnh báo khi quá 1% yêu cầu đóng trong ngày | Thêm bước xác nhận hai lần kèm số tiền và tài khoản nhận; cho phép mở lại trong 7 ngày không cần tạo yêu cầu mới | PM trợ lý hoàn phí |
| 2 | Hệ thống | Kiểm tra mẫu mỗi ngày: so tham số tool `tra_bang_gia` (loại hàng, cân nặng) với dữ liệu đơn; ngưỡng 0 ca sai loại hàng; theo dõi tỉ lệ `mo_lai_trong_7_ngay` của `hang_nang` theo tuần | Bắt buộc suy ra loại hàng từ cân nặng (từ 20 kg là hàng nặng) trước khi gọi tool; thêm kiểm tra đầu ra tool so với khoảng giá hợp lệ | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | Event `notification_sent` có giờ gửi ngoài 07:00–21:00; tỉ lệ khiếu nại về thông báo theo tuần, ngưỡng 0,5% | Hẹn giờ gửi: tin nhắn tạo ngoài khung 07:00–21:00 được giữ lại tới 07:00 sáng hôm sau; tin gấp vẫn gửi qua kênh không rung | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason` = `ngoai_thoi_han_luu_tru`; theo dõi số ca mỗi tuần và thời gian nhân viên xử lý | Giữ cách chuyển nhân viên kèm tóm tắt; báo ngay thời hạn tra cứu 12 tháng khi khách bắt đầu; nếu tỉ lệ vượt 3% thì cân nhắc mở rộng kho dữ liệu | PM trợ lý hoàn phí |
| 12 | Ngầm | Cảnh báo chi phí token trung bình mỗi yêu cầu theo depot mỗi ngày: depot vượt 1,5 lần trung vị 12 depot hai ngày liên tiếp; kèm kiểm tra tool trả đủ trường (schema) | Thêm kiểm tra schema đầu ra của tool tra đơn và báo lỗi khi thiếu trường; giới hạn số lần gọi lại tối đa 3 mỗi yêu cầu | Kỹ sư trưởng agent |
