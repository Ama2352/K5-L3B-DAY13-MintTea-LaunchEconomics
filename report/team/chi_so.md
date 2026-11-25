# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48/177; `sua` 41, `bo` 7) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm dùng trợ lý được mở bằng trợ lý | Số `agent_suggestion_shown` theo `staff_id` của nhóm dùng trợ lý, chia số `refund_request_created` giao cho nhóm đó | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm) | Số `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`, chia số đơn được kiểm tra | Không cần tính |

Chỉ số trong đợt chạy thử là 82,83% (chính), 27,12% (bỏ qua gợi ý) và 4,25% (mở lại trong 7 ngày). Không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

- **Trong phạm vi pilot** (`noi_dia` + `hang_nang`, 982 yêu cầu): chính 92,26% (906/982) · bỏ qua gợi ý 21,09% (27/128) · mở lại 3,97% (39/982). Đây là mức nền để đặt ngưỡng luật dừng trong `pilot_plan.yaml`.
- Cách tính: đếm trên `src/logix_requests.csv`, đọc bằng `pd.read_csv(..., keep_default_na=False)`. Ba chỉ số không dùng cột `_simulated` nên không mang nhãn simulated.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| refund_request_created | App khách | request_id, loai, so_tien, arm, trace_id | Khi khách gửi yêu cầu |
| agent_run_completed | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| agent_suggestion_shown | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra |
| staff_review_decision | Nhân viên | quyet_dinh (giu/sua/bo), phut_xem_lai đo thật, trace_id | Khi bấm gửi, sửa hoặc bỏ |
| handoff_to_staff | Agent | reason, tom_tat, trace_id | Khi chuyển cho nhân viên |
| ticket_closed | Hệ thống ticket | closed_at, trace_id | Khi đóng yêu cầu |
| ticket_reopened | Khách | reopened_at, reason, trace_id | Khi khách mở lại |
| audit_sample_checked | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chính: `refund_request_created` (mẫu số) + `ticket_closed` (đóng trong 24 giờ kể từ lúc tạo) + `ticket_reopened` (không có trong 7 ngày).
- Bỏ qua gợi ý: `staff_review_decision`, số có `quyet_dinh` là `sua` hoặc `bo`, chia tổng số event này.
- Lỗi lọt đến khách: `ticket_reopened` trong 7 ngày, chia `refund_request_created`.
- Dùng (tự đề xuất): `agent_suggestion_shown` chia `refund_request_created`, lọc theo `arm`.
- An toàn (tự đề xuất): `audit_sample_checked`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,77%, lên 6.787 đ/việc thành công (simulated, B1) | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 4,89% trong phạm vi, 48/982) | Thu hẹp về `noi_dia`, rà 20 trace làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ/việc = 0,98× với 9 phút làm lại; 12.415 đ = 1,03× với 15,3 phút (simulated, B4). Hòa vốn khi mỗi lần xem lại ≤ 5,12 hoặc ≤ 4,80 phút (simulated) | % yêu cầu được xem lại > 50% ở cuối bước rollout 0.25 | Giảm xem lại theo bậc khi tỉ lệ `sua` + `bo` < 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa (simulated, A4) | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
