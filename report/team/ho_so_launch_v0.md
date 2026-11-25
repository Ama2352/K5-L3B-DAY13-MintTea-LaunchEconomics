# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm MintTea · Lớp L3B · Phạm vi đề xuất: nội địa và hàng nặng tại 6 depot.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ toàn mẫu, 978/1.200 ca; 3.414 đ biến đổi/việc trong phạm vi (simulated). [A2–A4](bang_chi_phi.md) | Giả lập | Người viết code |
| 2 · Ba yếu tố nhạy nhất | Làm lại gấp đôi +51,77%, xem lại gấp đôi +40,70%, lương tăng 25% làm CPS tăng 23,12% (simulated). [B1–B2](bang_chi_phi.md) | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Cả hệ thống 5.865 đ/yêu cầu so với 12.000 đ ở cấu hình gốc. Trong phạm vi, CPS có cố định là 4.599 đ ở 45.000 yêu cầu toàn hệ thống/tháng và 5.784 đ ở nửa khối lượng (simulated). [A2–A4](bang_chi_phi.md) | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, dùng và an toàn | Toàn mẫu có 82,83% đóng trong 24 giờ và không mở lại, 27,12% sửa hoặc bỏ gợi ý trong số được xem lại, 4,25% mở lại trong 7 ngày. Đặc tả 8 event có trace_id. [Bộ chỉ số](chi_so.md) | Xong, có bằng chứng | Người phụ trách chỉ số |
| 5 · Bảng lỗi và khắc phục | Hai bộ nhãn độc lập đồng thuận 19/20 ca (95%); đã thống nhất ca 3 và lập 5 phương án khắc phục. [Bảng lỗi](bang_loi.md) | Xong, có bằng chứng | Người gắn nhãn 1 |
| 6 · Pilot plan | Chia theo nhân viên, 20/nhóm, có đối chứng đồng thời và 3 luật dừng. Với MDE +6 điểm phần trăm, cần 859 quan sát hiệu dụng mỗi nhóm, tương ứng 299 yêu cầu đủ điều kiện/nhân viên, tức 5.980 yêu cầu thực tế/nhóm. Quân số và lịch thu mẫu chờ xác nhận. [Kế hoạch pilot](pilot_plan.yaml) | Chưa | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Xem lại 100% đầu ra đưa CPS lên 11.743–12.415 đ. Làm lại gấp đôi đưa CPS lên 6.787 đ. Giới hạn 2 lượt có chi phí toàn hệ thống thấp nhất trên mẫu (simulated). [Rủi ro kinh tế](chi_so.md#e2--rủi-ro-kinh-tế) | Giả lập | PM trợ lý hoàn phí |

Điều kiện cần kiểm tra trước lịch bắt đầu dự kiến 01/12/2026:

- **Giám đốc vận hành** xác nhận danh sách đủ 40 nhân viên tại các depot đã chọn và lưu lượng đủ cho 299 ca hợp lệ mỗi người. Mẫu có 20 mã nhân viên ở 6 depot. Nếu thiếu quân số hoặc lưu lượng, cập nhật thiết kế và tính lại cỡ mẫu.
- **Người phụ trách pilot** làm rõ 859 là cỡ mẫu hiệu dụng, chốt chỉ tiêu thu 5.980 ca thực tế/nhóm theo giả định cụm cân bằng và đặt ngày quyết định sau khi ca cuối có đủ 7 ngày theo dõi. Nếu ca cuối vào 21/12/2026 thì có thể đọc kết quả sớm nhất ngày 28/12/2026.
- **Người phụ trách chỉ số và Trưởng nhóm CSKH** kiểm tra luồng đo, rollback trong 4 giờ, quãng thời gian xem lại và luật an toàn khi tỷ lệ mở lại vượt 6% hoặc cao hơn đối chứng quá 2 điểm phần trăm. Kế hoạch cần quy định rõ điều kiện chuyển bước khi các luật dừng chưa kích hoạt.

**Đề xuất · Go có điều kiện** cho pilot nội địa và hàng nặng sau khi xác nhận đủ quân số, lưu lượng, lịch theo dõi và điều kiện an toàn ở trên.
