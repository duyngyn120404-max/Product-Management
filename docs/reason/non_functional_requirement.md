# Non-Functional Requirements — Product Management

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Product Management PV |
| Ứng dụng | Quản lý sản phẩm nội bộ |
| Nguồn đầu vào | `non_functional_requirements.md` |
| Phiên bản tài liệu | Draft 1 |
| Ngày lập | 2026-08-06 |

Tài liệu này chứa các diễn giải về tính năng phi chức năng trong `non_functional_requirement.md`

## 1. Performance

1. *Các metrics thường được sử dụng trong performance nào khác?*

> Gồm concurrent users, response time, throughput, error rate, data volumne, page load time, search latency, import/export time, file/image upload time, resource usage, scalability, startup/restart time, background job time

2. *Làm sao biết yêu cầu hiện tại đã đáp ứng cho MVP?*

> Những yêu cầu này đủ vì nó bao phủ các luồng chính được sử dụng thường xuyên như tra cứu, tìm kiếm, quản lý,...

## 2. Security

1. *Ở phạm vi nội bộ, vấn đề bảo mật nên cover những khía canh nào, đã đủ cover chưa?*

> Với hệ thống nội bộ nhỏ, bộ security NFR được xem là đủ khi nó kiểm soát được các rủi ro chính như chỉ người hợp lệ được truy cập, người dùng k thao tác vượt quyền và một số khía cạnh phụ như thông tin nhạy cảm, dữ liệu qua prod được mã hóa, db k công khai. Các biện pháp công khai như 2FA, allowlist, audit log,... có thể triển khai nếu quy mô mở rộng

2. *Làm sao biết đã đủ?*

> Dựa vào các yếu tố như phạm vi người dùng (xx người nội bộ/khách hàng bên ngoài), độ nhạy cảm dữ liệu (dữ liệu y tế/tài chính,..), các rủi ro (lộ db, lộ secret, truy cập trái phép,) và chi phí 

3. *Thực tế thì security còn có những gì?*

> Auditability, deployment exposure,...

