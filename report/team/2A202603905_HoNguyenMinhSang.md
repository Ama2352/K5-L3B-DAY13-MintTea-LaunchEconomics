# Báo cáo cá nhân · Hồ Nguyễn Minh Sang

## 1. Thông tin thành viên

- Họ tên: Hồ Nguyễn Minh Sang
- MSSV: 2A202603905
- Vai trò: Nhóm trưởng, viết code và kiểm số CP1–CP2, tích hợp hồ sơ Gate 2a.

## 2. Phần việc phụ trách

- Viết mô hình chi phí A1–A4, phân tích độ nhạy B1–B4 và điền bảng chi phí.
- Tích hợp các phần C–E sau khi các PR của nhóm đã vào main, điền hồ sơ launch và tổng hợp báo cáo nhóm.

## 3. Đóng góp cụ thể

- Tính chi phí từ mọi lượt chạy, gồm token, tool, giờ xem lại và làm lại. Mẫu có 978/1.200 việc thành công, chi phí 4.472 đ/việc (simulated).
- Tách bốn loại yêu cầu, dùng kết quả để đề xuất nội địa và hàng nặng, rồi cộng 40 triệu đồng chi phí cố định mỗi tháng ở hai mức khối lượng.
- Tính chín kịch bản riêng, một kịch bản cặp, chi phí khi giới hạn lượt chạy và chi phí khi xem lại toàn bộ đầu ra. Hai lượt có chi phí toàn hệ thống thấp nhất theo B3, khoảng 6,90 triệu đồng cho 1.200 yêu cầu (simulated).
- Ghép kết quả đồng thuận 19/20 ca, bộ chỉ số và thiết kế pilot vào hồ sơ. Ghi điều kiện xác nhận 40 nhân viên, 5.980 yêu cầu thực tế/nhóm và cửa sổ theo dõi 7 ngày trước khi ra quyết định.
- Đối chiếu hồ sơ 3boy với thang điểm Gate 2a và lập phiếu chấm đề xuất 25/30, cho chạy thử có điều kiện. Câu hỏi duyệt chéo tập trung vào lịch thu 5.980 ca thực tế mỗi nhóm và thời gian theo dõi ca cuối đủ 7 ngày. Câu trả lời của 3boy chờ ghi nhận tại buổi duyệt.

## 4. Bằng chứng

- Commit `692e55d`, PR #1 đã merge. [Code A–B](../../src/lab13.py) · [Bảng A–B](bang_chi_phi.md)
- [Hồ sơ launch v0](ho_so_launch_v0.md) · [Báo cáo nhóm](group_report.md)
- [Phiếu duyệt chéo 3boy](phieu_cham.md)

## 5. Công cụ AI đã dùng

Codex hỗ trợ đọc đề, viết và chạy mô hình, đối chiếu kết quả với hướng dẫn, và tổng hợp hồ sơ từ các PR đã merge. Kiểm chứng bằng ba phép thử A1, chạy lại bảng A–B trên hai CSV, và tính lại cỡ mẫu bằng `pilot_calc.py`.

## 6. Tự đánh giá

Kết quả nhạy nhất với thời gian nhân viên làm lại và xem lại. Khi chọn giới hạn chạy, cần tính cả chi phí của các ca chuyển sang nhân viên. Pilot cần đo thời gian xử lý thực tế và xác nhận đủ nhân viên trước khi dùng kết quả để quyết định mở rộng.
