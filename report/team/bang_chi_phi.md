# Bảng chi phí · Nhiệm vụ A và B

Nguồn tính là `src/lab13.py` và hai CSV của lab. Các giá trị có dùng phút giả lập mang nhãn **simulated**.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả |
| --- | ---: |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Giá trị | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 đ | logix_runs.csv | đo từ trace |
| Tool | 84.000 đ | logix_runs.csv | đo từ trace |
| Token và tool của lần 2 và 3 | 93.804 đ | attempt > 1 | đo từ trace |
| Xem lại | 1.780.000 đ | phut_xem_lai_simulated | simulated |
| Làm lại | 2.264.000 đ | phut_lam_lai_simulated | simulated |
| Tổng chi phí | 4.373.585 đ | token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 | ket_qua | đếm từ dữ liệu |
| Chi phí mỗi việc thành công | 4.472 đ | tổng / 978 | simulated |
| Hóa đơn token và tool mỗi yêu cầu | 274,65 đ | (token + tool) / 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,28 lần** hóa đơn token và tool mỗi yêu cầu (simulated).
- Làm lại lớn nhất, chiếm **51,77%** tổng chi phí (simulated).
- Theo quy ước B3, cộng 12.000 đ cho mỗi yêu cầu trong 222 ca chưa thành công cho **5.865 đ/yêu cầu**, bằng **0,49×** baseline (simulated).

## A3 · Tách theo loại yêu cầu

| Loại | Yêu cầu | Thành công | Lần chạy/yêu cầu | Chi phí/việc thành công (simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,02% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,05% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,33% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,41% | 1,88 | 10.215 đ | 0,85× |

- Loại `quoc_te` khỏi pilot. Với tối đa 3 lần, giá vẫn là 22.515 đ/việc thành công (simulated), tỷ lệ `ok` theo lần giảm từ 30,0% xuống 11,4% rồi 2,2%.
- Hoãn `doi_tac` vì có điều khoản riêng và chi phí đã bằng 0,85× baseline (simulated).

## A4 · Chi phí cố định trong phạm vi noi_dia + hang_nang

Giữ cơ cấu của mẫu, cứ 1.200 yêu cầu toàn hệ thống có 900 việc thành công trong phạm vi. Chi phí biến đổi trong phạm vi là 3.414 đ/việc thành công (simulated).

| Yêu cầu toàn hệ thống/tháng | Việc thành công trong phạm vi | Cố định/việc | Chi phí/việc thành công có cố định (simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 45.000 | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| 22.500 | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Cả hai mức vẫn dưới 12.000 đ theo phép so CPS của A4 (simulated). Khối lượng giảm nửa làm chi phí cố định mỗi việc tăng thêm 1.185 đ.

## B1 · Đổi từng yếu tố

| Kịch bản | Chi phí/việc thành công (simulated) | Thay đổi (simulated) |
| --- | ---: | ---: |
| Giá token gấp đôi | 4.723,08 đ | +5,62% |
| Giá token giảm một nửa | 4.346,41 đ | −2,81% |
| Chi phí xem lại gấp đôi | 6.292,01 đ | +40,70% |
| Chi phí xem lại giảm một nửa | 3.561,95 đ | −20,35% |
| Chi phí làm lại gấp đôi | 6.786,90 đ | +51,77% |
| Chi phí làm lại giảm một nửa | 3.314,50 đ | −25,88% |
| Lương nhân viên tăng 25% | 5.505,71 đ | +23,12% |
| Tối đa 2 lần chạy | 4.237,29 đ | −5,25% |
| Tối đa 1 lần chạy | 4.110,99 đ | −8,07% |

Khi giới hạn số lần chạy, yêu cầu vượt ngưỡng chuyển sang nhân viên, bỏ các trace vượt ngưỡng và đặt phút xem lại, làm lại của trợ lý về 0.

## B2 · Đổi một cặp và xếp hạng

- Giá token và chi phí xem lại đồng thời gấp đôi cho **6.543,12 đ (+46,31%)** (simulated). Tác động bằng tổng hai mức tăng riêng trước làm tròn.
- Ba yếu tố tác động mạnh nhất là làm lại (+51,77%), xem lại (+40,70%) và lương (+23,12%) (simulated).

## B3 · Giới hạn chạy lại

Chi phí cả hệ thống cộng 12.000 đ cho mỗi yêu cầu chưa thành công theo quy ước của B3.

| Giới hạn | Tổng trợ lý (simulated) | Yêu cầu chưa thành công | Cả hệ thống (simulated) | Chi phí/việc thành công (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.110,99 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237,29 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.471,97 đ |

- Hai lần rẻ nhất cho cả hệ thống. Một lần có CPS thấp nhất và đẩy thêm 85 ca sang nhân viên so với hai lần (simulated).

## B4 · Xem lại 100% đầu ra trong phạm vi

- Xem lại 948 yêu cầu có đầu ra `ok`, mỗi ca 5 phút. Với 48 ca làm lại ở mức 9 phút/ca, chi phí là **11.743 đ/việc** (0,98×). Ở mức 15,3 phút/ca từ dữ liệu toàn mẫu, chi phí là **12.415 đ/việc** (1,03×) (simulated).
- Pilot cần đo phút làm lại, thời gian xem lại và tỷ lệ xem lại tối thiểu vẫn đạt ngưỡng an toàn. Điểm hòa vốn ở hai kịch bản tương ứng là **5,12** và **4,80 phút** xem lại mỗi ca (simulated).
