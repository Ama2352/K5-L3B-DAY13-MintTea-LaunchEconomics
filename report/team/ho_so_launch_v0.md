# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm MintTea · Lớp L3B · Phạm vi đề xuất: nội địa và hàng nặng tại 6 depot.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ toàn mẫu, 978/1.200 ca; 3.414 đ biến đổi/việc trong phạm vi (simulated). [A2–A4](bang_chi_phi.md) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Làm lại gấp đôi +51,77%, xem lại gấp đôi +40,70%, lương tăng 25% làm CPS tăng 23,12% (simulated). [B1–B2](bang_chi_phi.md) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống 5.865 đ/yêu cầu so với 12.000 đ ở cấu hình gốc. Trong phạm vi, CPS có cố định là 4.599 đ ở 45.000 yêu cầu toàn hệ thống/tháng và 5.784 đ ở nửa khối lượng (simulated). [A2–A4](bang_chi_phi.md) | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, dùng và an toàn | Toàn mẫu có 82,83% đóng trong 24 giờ và không mở lại, 27,12% sửa hoặc bỏ gợi ý trong số được xem lại, 4,25% mở lại trong 7 ngày. Đặc tả 8 event có trace_id. [Bộ chỉ số](chi_so.md) | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và khắc phục | Hai bộ nhãn độc lập đồng thuận 19/20 ca (95%); đã thống nhất ca 3 và lập 5 phương án khắc phục. [Bảng lỗi](bang_loi.md) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia ngẫu nhiên theo nhân viên, 20/nhóm, có đối chứng đồng thời và 3 luật dừng. MDE +6 điểm cần 859 quan sát hiệu dụng mỗi nhóm = 299 yêu cầu/nhân viên = 5.980 yêu cầu thực tế/nhóm, thu trong 14 ngày ở bước 0.50 (15–28/12/2026). Bất lợi: nếu tác động thật chỉ +5 điểm thì power còn khoảng 0,64. Quyết định ngày 05/01/2027. [Kế hoạch pilot](pilot_plan.yaml) | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Xem lại 100% đầu ra đưa CPS lên 11.743–12.415 đ (0,98–1,03× của 12.000 đ). Làm lại gấp đôi đưa CPS lên 6.787 đ. Giới hạn 2 lượt có chi phí toàn hệ thống thấp nhất trên mẫu (simulated). [Rủi ro kinh tế](chi_so.md#e2--rủi-ro-kinh-tế) | Giả lập | PM trợ lý hoàn phí |

Điều kiện, mỗi điều kiện có người phụ trách và ngày kiểm tra (lịch bắt đầu dự kiến 01/12/2026):

- **Kỹ sư trưởng agent** · kiểm tra 30/11/2026: có khoá chống trùng (idempotency) khi ghi sổ cái và chỉ báo "đã hoàn" khi sổ cái trả ok (ca 7, 20 trong bảng lỗi). Ngưỡng: 0 ca hoàn trùng trên dữ liệu thử.
- **Giám đốc vận hành** · kiểm tra 30/11/2026: xác nhận đủ 40 nhân viên và lưu lượng khoảng 31 yêu cầu trong phạm vi/người/ngày (1.500 ÷ 40 × 81,83%). Mẫu chạy thử chỉ có 20 mã nhân viên ở 6 depot. Ký chấp nhận MDE +6 điểm, biết power chỉ còn khoảng 0,64 nếu tác động thật là +5 điểm. Nếu thiếu quân số hoặc lưu lượng thì tính lại cỡ mẫu trước khi bắt đầu.
- **PM trợ lý hoàn phí** · kiểm tra 07/12/2026 (cuối bước 0.10): đủ 8 event có trace_id ghi cho ≥ 95% yêu cầu; thay phút xem lại và làm lại simulated bằng phút đo thật từ `staff_review_decision`.
- **Trưởng nhóm CSKH** · kiểm tra 14/12/2026 (cuối bước 0.25): có kế hoạch giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%, vì xem lại 100% tốn 11.743–12.415 đ/việc (simulated). Hòa vốn khi mỗi lần xem lại ≤ 5,12 phút (≤ 4,80 phút nếu làm lại 15,3 phút/ca) (simulated).
- **Giám đốc vận hành** · kiểm tra 28/12/2026: mỗi nhóm đã thu đủ 5.980 yêu cầu; nếu thiếu thì kéo dài bước 0.50 tối đa 7 ngày và lùi ngày quyết định. Ca cuối phải đủ 7 ngày theo dõi mở lại (đến 04/01/2027) trước ngày quyết định 05/01/2027.

**Đề xuất · Go có điều kiện** cho pilot nội địa và hàng nặng, chỉ bắt đầu khi đạt các điều kiện kiểm tra ngày 30/11/2026 ở trên.
