# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): MintTea (L3B)
- Nhóm được chấm: 3boy (L3B)
- Căn cứ: hồ sơ launch v0, bảng chi phí A–B và kế hoạch pilot trong repo 3boy.

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất cho chạy thử có điều kiện. Nhóm nêu kịch bản bất lợi: xem lại 100% có thể đưa chi phí lên khoảng 12.415 đ/ca thành công (simulated). Nhóm đề xuất đo thời gian thật và giảm xem lại theo bậc khi tỷ lệ sửa hoặc bỏ gợi ý dưới 15%, có người phụ trách và ngày kiểm tra. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Bảng A–B gắn nhãn simulated, hồ sơ launch đánh dấu Giả lập. Phạm vi chỉ gồm nội địa và hàng nặng, lần lượt 2.696 đ và 8.221 đ/ca thành công, so với 22.515 đ của quốc tế (simulated). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 5 | Có đối chứng đồng thời, phân nhóm ngẫu nhiên 20 nhân viên mỗi bên và ba luật dừng có ngưỡng. Phép tính D1 yêu cầu 299 ca/người, tức 5.980 ca thực tế mỗi bên để đạt 859 quan sát hiệu dụng. YAML ghi 859 ở trường cỡ mẫu nhưng chưa ghi chỉ tiêu thu thực tế và lịch thu đủ mẫu. Kế hoạch chỉ đo chỉ số chính từ bước 0,50, mỗi bước một tuần, và chưa gắn mốc kết thúc thu mẫu với cửa sổ theo dõi 7 ngày trước ngày quyết định 05/01/2027. |
| **Tổng** | | | | **25 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Go có điều kiện cho pilot nội địa và hàng nặng. Trước khi chạy, Giám đốc vận hành cần xác nhận đủ 20 nhân viên và khả năng thu 5.980 ca hợp lệ mỗi bên, ghi riêng số ca thực tế và số quan sát hiệu dụng, rồi chốt lịch thu mẫu sao cho ca cuối được theo dõi đủ 7 ngày. Nhóm cũng cần làm rõ điều kiện chuyển bước rollout khi các ngưỡng dừng chưa bị chạm.

**Một câu hỏi cho đội trình:** Kế hoạch chỉ đo chỉ số chính từ bước 0,50. Hai nhóm sẽ thu đủ 5.980 ca mỗi bên trong bao lâu, và ca cuối cần vào hệ thống chậm nhất ngày nào để đến 05/01/2027 đã theo dõi đủ 7 ngày?

**Câu trả lời của đội trình (ghi lại tại buổi):** Ở bước rollout 0,50, mỗi bên có 20 nhân viên và cần thu ít nhất 299 ca hợp lệ mỗi người, tức 5.980 ca thực tế mỗi bên để đạt khoảng 859 quan sát hiệu dụng. Kế hoạch ghi mỗi bước rollout kéo dài một tuần. Để đạt chỉ tiêu trong tuần đo ở bước 0,50, mỗi bên cần trung bình khoảng 855 ca hợp lệ mỗi ngày. Với ngày quyết định 05/01/2027, ca cuối cần vào hệ thống chậm nhất ngày 29/12/2026 để có đủ 7 ngày theo dõi. Lưu lượng 855 ca/ngày là mức cần đạt tính từ kế hoạch. Khả năng thu đủ với lưu lượng thực tế là điều kiện hội đồng yêu cầu xác nhận.

_Ghi chú: câu trả lời trên được đối chiếu lại theo kế hoạch pilot của 3boy sau buổi trình._
