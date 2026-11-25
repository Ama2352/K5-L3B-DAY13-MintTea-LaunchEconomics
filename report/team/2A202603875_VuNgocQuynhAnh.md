# Báo cáo cá nhân — VuNgocQuynhAnh-2A202603875

## 1. Thông tin thành viên

- Họ tên: Vũ Ngọc Quỳnh Anh
- MSSV: 2A202603875
- Email: 26ai.anhvnq@vinuni.edu.vn
- Vai trong nhóm: Người gắn nhãn 2 (gắn nhãn độc lập CP3), phụ trách chỉ số và rủi ro kinh tế

## 2. Phần việc phụ trách

- CP3: gắn nhãn độc lập 20 ca lỗi theo năm loại của Google PAIR, làm người gắn nhãn thứ hai.
- CP5: đặc tả chỉ số, danh sách event và rủi ro kinh tế (`chi_so.md`).

## 3. Đóng góp cụ thể

- Gắn nhãn 20 ca từ 14:55 đến 15:04, có lý do theo nguyên nhân gốc. Không xem nhãn của người gắn nhãn 1. Commit trước khi so nhãn để làm bằng chứng gắn độc lập. Đồng thuận với người gắn nhãn 1: 19/20.
- Tính thử ba chỉ số trên 1.200 yêu cầu: chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại trong 7 ngày 4,25% (51/1.200). Tính thêm trong phạm vi pilot noi_dia + hang_nang: 92,26% · 21,09% · 3,97%.
- Đề xuất thêm một chỉ số dùng (% yêu cầu được mở bằng trợ lý) và một chỉ số an toàn (% đơn hoàn sai qua kiểm tra mẫu hằng tuần).
- Liệt kê 8 event có `trace_id` và kiểm tra chéo để chỉ số nào cũng tính được từ event.
- Viết 3 dòng rủi ro kinh tế lấy số từ bảng độ nhạy của nhóm: làm lại gấp đôi (+51,77%, simulated), xem lại 100% (0,98× đến 1,03×, simulated), khối lượng thấp (+1.185 đến +2.370 đ/việc, simulated).
- Gửi mức nền 3,97% và 21,09% cho người lập `pilot_plan.yaml` để đặt ngưỡng luật dừng.

## 4. Bằng chứng

- `report/team/nhan_quynhanh.md`: commit `624df55`, PR #2
- `report/team/chi_so.md`: commit `afd3c24`, PR #4

## 5. Công cụ AI đã dùng

- Claude Code (Claude Opus): tóm tắt đề, lập checklist công việc theo phân công, tạo khung bảng trống cho file nhãn, đếm ba chỉ số từ `logix_requests.csv` bằng pandas, soạn nháp `chi_so.md`, chạy lệnh git push và tạo PR.
- Không dùng AI để gắn nhãn 20 ca. AI không đề xuất nhãn, theo RULES.
- Tự kiểm tra: đối chiếu ba chỉ số với số mẫu trong hướng dẫn chi tiết (khớp 994/1.200, 48/177, 51/1.200); kiểm tra mẫu số chỉ số dùng là số yêu cầu được xem lại (177), không phải 1.200; đối chiếu số rủi ro với `bang_chi_phi.md` của nhóm (lệch dưới 2%); lệnh tìm từ bị cấm trong `report/team` không in gì.

## 6. Tự đánh giá

- Làm tốt: giữ được tính độc lập khi gắn nhãn; mọi con số trong `chi_so.md` có tử, mẫu và nhãn simulated khi cần.
- Chưa tốt: gắn nhãn mất 9 phút, quá giới hạn 8 phút 1 phút.
- Học được: chỉ số nào không tính được từ danh sách event thì chưa đo được; mức nền trong phạm vi pilot khác toàn mẫu, nên ngưỡng luật dừng phải đặt theo phạm vi.
