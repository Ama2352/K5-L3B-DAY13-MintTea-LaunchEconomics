# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm MintTea · Lớp L3B · Quyết định về kế hoạch pilot

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ trên toàn mẫu (simulated), 978/1.200 yêu cầu thành công. Trong phạm vi nội địa và hàng nặng, 3.414 đ biến đổi/việc (simulated). | Giả lập | Người viết code |
| 2 · Ba yếu tố nhạy nhất | Làm lại +51,77%, xem lại +40,70%, lương +23,12% theo B1 (simulated). | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Toàn hệ thống 5.865 đ/yêu cầu so với 12.000 đ, có tính phần nhân viên xử lý theo B3. Trong phạm vi nội địa và hàng nặng, CPS có cố định là 4.599 đ ở 45.000 yêu cầu toàn hệ thống/tháng và 5.784 đ ở nửa khối lượng (simulated). | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, dùng và an toàn | Cần 3 chỉ số tính thử và ít nhất 6 event có trace_id. [Đặc tả chỉ số](chi_so.md) đang chờ bằng chứng. | Chưa | Người phụ trách chỉ số |
| 5 · Bảng lỗi và khắc phục | Cần hai bộ nhãn độc lập cho 20 ca, đồng thuận từ 16/20 và 5 ca có phương án khắc phục. [Bảng lỗi](bang_loi.md) đang chờ kết quả. | Chưa | Người gắn nhãn 1 |
| 6 · Pilot plan | Baseline 70%, mục tiêu +5 điểm phần trăm, cần chốt cỡ mẫu, đơn vị chia, ngày quyết định và ít nhất 3 luật dừng trong [kế hoạch pilot](pilot_plan.yaml). | Chưa | Người phụ trách pilot |
| 7 · Rủi ro kinh tế | Xem lại 100% đầu ra có CPS trong khoảng 11.743–12.415 đ (simulated). Giới hạn 2 lần cho chi phí hệ thống thấp nhất trên mẫu toàn hệ thống. | Giả lập | Người phụ trách chỉ số |

Quay lại Gate 2a sau khi hoàn tất CP3–CP5, xác minh cách chia đủ mẫu và đối chứng đồng thời, chốt ngưỡng dừng, rồi kiểm tra liệu có thể giảm thời gian hoặc tỷ lệ xem lại mà vẫn đạt ngưỡng an toàn.

**Đề xuất hiện tại · No-go** cho pilot cho đến khi có đủ bằng chứng để xét lại tại Gate 2a.
