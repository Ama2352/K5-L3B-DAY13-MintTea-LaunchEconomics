# Báo cáo cá nhân — NguyenThaoQuyen-2A202603895

## 1. Thông tin thành viên

- Họ tên: Nguyễn Thảo Quyên
- MSSV: 2A202603895
- Email:
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 1; phụ trách CP3 (bảng lỗi) và CP4 (kế hoạch pilot)

## 2. Phần việc phụ trách

- **CP3 · Nhiệm vụ C:** gắn nhãn độc lập 20 ca lỗi, so nhãn với Quỳnh Anh, tổng hợp đồng thuận, viết quy tắc cho ca không trùng và lập bảng khắc phục 5 ca.
- **CP4 · Nhiệm vụ D:** tính cỡ mẫu D1, trả lời 5 câu D2 và điền `pilot_plan.yaml` (phạm vi, cách chia, cỡ mẫu, ba luật dừng, rollback, ngày quyết định).

## 3. Đóng góp cụ thể

- Gắn nhãn 20 ca lỗi độc lập với Quỳnh Anh. Hai bộ nhãn trùng 19/20 ca (95%). Ca lệch duy nhất là ca 3, nhãn của tôi là Ngầm, của Quỳnh Anh là Ngữ cảnh. Hai bạn thống nhất **Ngữ cảnh** vì khách đã báo "chưa được hoàn" nên lỗi đã lộ ra, trợ lý chỉ làm đúng thiết kế nhưng không khớp kỳ vọng của khách.
- Bảng khắc phục 5 ca, mỗi loại một ca: ca 14 (Do người dùng), ca 2 (Hệ thống), ca 16 (Ngữ cảnh), ca 19 (Giới hạn hệ thống), ca 12 (Ngầm). Mỗi dòng có cách phát hiện đo được và một vai trò phụ trách.
- Tính cỡ mẫu D1 bằng `src/pilot_calc.py`: 1.251 yêu cầu mỗi nhóm khi chia theo yêu cầu; chia theo nhân viên với m = 75 cần 42 người mỗi nhóm, vượt 40 nhân viên; 20 nhân viên mỗi nhóm chỉ đạt tối đa 1.000 cỡ mẫu hiệu dụng; mức chênh 6 điểm cần mỗi nhân viên ít nhất 299 yêu cầu.
- Chọn cách chia theo nhân viên, 20 + 20, phân tầng theo depot, chấp nhận chỉ phát hiện được mức chênh 6 điểm. Ghi rõ rằng nếu tác động thật chỉ là 5 điểm thì power còn khoảng 0,64.
- Chọn phạm vi pilot là `noi_dia` và `hang_nang`, đưa `quoc_te` và `doi_tac` ra ngoài, dựa trên bảng A3 của Sang (số simulated).
- Viết ba luật dừng (an toàn, chi phí, mức độ sử dụng) theo mẫu NẾU – TRONG – THÌ – KHÔNG THÌ. Tỉ lệ mở lại trong 7 ngày hiện tại là 4,25% (3,97% trong phạm vi pilot), nên ngưỡng an toàn đặt theo mức chênh +2 điểm so với đối chứng kèm trần 6%.

## 4. Bằng chứng

- `report/team/bang_loi.md`: hai bộ nhãn, tỉ lệ đồng thuận 19/20, quy tắc cho ca 3, bảng khắc phục 5 ca.
- `report/team/pilot_plan.yaml`: không còn dấu `?` ngoài dòng chú thích, đọc được bằng `yaml.safe_load`, ba luật dừng.
- `src/pilot_calc.py`: chạy bằng `python3 pilot_calc.py` trong thư mục `src/`, in kết quả D1 và tỉ lệ mở lại.
- Commit trên nhánh `quyen/cp3-cp4`, PR #3 đã merge vào `main` (phần CP3 đầu tiên).
- Các con số tính từ cột `_simulated` (chi phí mỗi việc thành công theo loại yêu cầu trong phần phạm vi) đều ghi nhãn simulated.

## 5. Công cụ AI đã dùng

- **Claude Code.** Dùng để: đọc và giải thích đề bài và phân chia công việc; viết `src/pilot_calc.py`; soạn nháp bảng khắc phục 5 ca và nháp `pilot_plan.yaml`; điền các cột so nhãn và tỉ lệ đồng thuận trong `bang_loi.md` từ hai file nhãn đã có; kiểm tra cú pháp yaml.

## 6. Tự đánh giá

- Làm tốt: hai bộ nhãn độc lập đạt đồng thuận cao; số cỡ mẫu tính lại khớp đáp án; bảng khắc phục đo được.
- Bài học: với 40 nhân viên, chia theo cụm không đủ mẫu cho mức chênh 5 điểm, nên phải nói rõ đánh đổi thay vì giả vờ đủ mẫu.
