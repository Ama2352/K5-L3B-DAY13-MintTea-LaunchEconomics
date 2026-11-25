# Báo cáo nhóm · MintTea (L3B)

Thành viên và phân công được ghi trong [TEAM.md](../../TEAM.md).

## Mục tiêu và cách làm

Đánh giá chi phí của trợ lý hoàn phí LogiX-VN và thiết kế pilot có đối chứng. Nhóm dùng 1.624 lượt chạy liên kết với 1.200 yêu cầu giả lập. Chi phí token và công cụ bao gồm mọi lượt chạy. Công xem lại và làm lại tính từ phút simulated.

| Phần | Kết quả và bằng chứng |
| --- | --- |
| A · Chi phí | Ba phép thử A1 đạt. CPS là 4.472 đ trên toàn mẫu và 3.414 đ biến đổi trong phạm vi nội địa và hàng nặng (simulated). Quốc tế có CPS 22.515 đ, vượt mốc 12.000 đ nhân viên tự xử lý một yêu cầu (simulated). [Bảng chi phí](bang_chi_phi.md) |
| B · Độ nhạy | Đã tính 9 kịch bản riêng và 1 cặp. Làm lại chiếm 51,77% tổng chi phí (simulated). Giới hạn 2 lượt cho chi phí toàn hệ thống thấp nhất là 6.901.220 đ trên 1.200 yêu cầu (simulated). Xem lại 100% đầu ra đưa CPS lên 11.743–12.415 đ (simulated). [Bảng độ nhạy](bang_chi_phi.md#b1--đổi-từng-yếu-tố) |
| C · Lỗi | Hai người gắn nhãn độc lập đồng thuận 19/20 ca (95%). Đã thống nhất ca 3 và xây phương án phát hiện, khắc phục cho 5 ca thuộc 5 loại. [Bảng lỗi](bang_loi.md) |
| D · Pilot | Chia ngẫu nhiên theo nhân viên, phân tầng theo depot, 20 người mỗi nhóm, có đối chứng đồng thời và 3 luật dừng. MDE +6 điểm phần trăm cần 859 quan sát hiệu dụng, tương ứng 5.980 yêu cầu thực tế/nhóm nếu mỗi người nhận 299 yêu cầu. [Kế hoạch pilot](pilot_plan.yaml) · [Code tính mẫu](../../src/pilot_calc.py) |
| E · Chỉ số và Gate 2a | Toàn mẫu có 82,83% đóng trong 24 giờ và không mở lại trong 7 ngày, 27,12% sửa/bỏ trong các ca được xem lại, và 4,25% mở lại. Đã chọn thêm 2 chỉ số, mô tả 8 event có trace_id và 3 rủi ro kinh tế. [Đặc tả chỉ số](chi_so.md) · [Hồ sơ launch](ho_so_launch_v0.md) |

## Quyết định và việc còn lại

Nhóm đề xuất **Go có điều kiện** với pilot nội địa và hàng nặng. Kế hoạch cần đủ 40 nhân viên và 299 ca hợp lệ mỗi người. Dữ liệu quan sát có 20 mã nhân viên tại 6 depot, nên cần xác minh quân số và lưu lượng thực tế. Ngày quyết định phải chờ đủ cửa sổ mở lại 7 ngày cho ca cuối. Các tỷ lệ trong mẫu mô tả đợt chạy thử. Pilot có đối chứng sẽ dùng để ước lượng tác động.

Mức chênh mục tiêu của kế hoạch là +6 điểm phần trăm. Nếu tác động thật chỉ +5 điểm, power ước tính khoảng 64%. Do xem lại toàn bộ đầu ra có thể vượt chi phí xử lý thủ công, nhóm cần đo thời gian xem lại, thời gian làm lại và tỷ lệ mở lại trước khi tăng rollout.

MintTea đã hoàn tất duyệt chéo Gate 2a với 3boy. Phiếu của MintTea đề xuất 25/30 cho 3boy và cho chạy thử có điều kiện. Điểm MintTea nhận được chưa có trong hồ sơ lưu tại repo. [Phiếu chấm](phieu_cham.md)

## Tài liệu

[Công thức và giả định](../../docs/du_lieu_va_cong_thuc.md) · [Hướng dẫn chi tiết](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md)
