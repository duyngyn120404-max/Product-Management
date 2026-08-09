# Non-Functional Requirements — Product Management

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Product Management PV |
| Ứng dụng | Quản lý sản phẩm nội bộ |
| Nguồn đầu vào | `docs/source/customer.pdf` |
| Phiên bản tài liệu | Draft 1 |
| Ngày lập | 2026-08-06 |

## 1. Mục tiêu

Tài liệu này mô tả các yêu cầu phi chức năng của hệ thống Product Management, mô tả hệ thống cần hoạt động như thế nào về hiệu năng, bảo mật, khả năng sử dụng, độ ổn định, sao lưu và vận hành. Ngoài ra tài liệu đóng vai trò là tiêu chi thiết kế, tiêu chí nghiệm thu và cơ sở để viết test.

## 2. Performance Requirements

| Mã | Yêu cầu |
|---|---|
| NFR-PER-01 | Hệ thống hỗ trợ tối thiểu 10 người dùng nội bộ đăng nhập và sử dụng đồng thời trong phạm vi MVP. |
| NFR-PER-02 | Với dữ liệu tối thiểu 100 sản phẩm, trang danh sách sản phẩm phản hồi trong tối đa 1.5 giây. |
| NFR-PER-03 | Với dữ liệu tối thiểu 100 sản phẩm, thao tác tìm kiếm, lọc hoặc sắp xếp sản phẩm phản hồi trong tối đa 1.5 giây. |
| NFR-PER-04 | Với dữ liệu tối thiểu 100 sản phẩm, trang chi tiết sản phẩm phản hồi trong tối đa 1 giây. |
| NFR-PER-05 | Hệ thống xử lý tối thiểu 30 yêu cầu tra cứu sản phẩm mỗi phút mà vẫn đáp ứng các yêu cầu thời gian phản hồi trong phạm vi MVP. |
| NFR-PER-06 | Thao tác tạo hoặc cập nhật sản phẩm phản hồi trong tối đa 1 giây với dữ liệu MVP, không bao gồm thời gian upload ảnh. |
| NFR-PER-07 | Thao tác tạo hoặc cập nhật danh mục phản hồi trong tối đa 1 giây với dữ liệu MVP. |
| NFR-PER-08 | Thao tác tạo hoặc cập nhật tài khoản người dùng phản hồi trong tối đa 1 giây với tối thiểu 10 tài khoản nội bộ. |

## 3. Security Requirements

| Mã | Yêu cầu |
|---|---|
| NFR-02.01 | Hệ thống chỉ cho phép người dùng đã đăng nhập truy cập dữ liệu sản phẩm nội bộ. |
| NFR-02.02 | Hệ thống phải kiểm soát quyền truy cập theo vai trò người dùng. |
| NFR-02.03 | Người dùng không được truy cập các chức năng hoặc dữ liệu vượt quá quyền được cấp. |
| NFR-02.04 | Mật khẩu người dùng phải được lưu trữ theo cơ chế bảo mật của nền tảng Odoo. |
| NFR-02.05 | Hệ thống production phải sử dụng HTTPS khi triển khai thực tế. |
| NFR-02.06 | Các thông tin nhạy cảm như mật khẩu database, master password và secret cấu hình không được lưu trực tiếp trong mã nguồn. |

## 4. Usability Requirements

| Mã | Yêu cầu |
|---|---|
| NFR-03.01 | Giao diện hệ thống phải dễ sử dụng với người dùng nội bộ không có nền tảng kỹ thuật. |
| NFR-03.02 | Các chức năng tra cứu sản phẩm phải dễ tiếp cận vì đây là luồng sử dụng chính của nhân viên. |
| NFR-03.03 | Thông tin sản phẩm cần được trình bày rõ ràng, dễ đọc và phù hợp cho mục đích tư vấn khách hàng. |
| NFR-03.04 | Các thao tác quản trị như tạo, cập nhật và ngừng sử dụng sản phẩm cần có nhãn rõ ràng để tránh thao tác nhầm. |
| NFR-03.05 | Hệ thống nên hạn chế số bước thao tác đối với các luồng sử dụng thường xuyên như tìm kiếm và xem chi tiết sản phẩm. |

## 5. Reliability Requirements

| Mã | Yêu cầu |
|---|---|
| NFR-04.01 | Hệ thống phải duy trì dữ liệu sản phẩm ổn định trong quá trình sử dụng nội bộ. |
| NFR-04.02 | Hệ thống không được làm mất dữ liệu sản phẩm khi sản phẩm bị ngừng sử dụng. |
| NFR-04.03 | Hệ thống cần hạn chế lỗi gây gián đoạn các luồng chính như đăng nhập, tìm kiếm và xem chi tiết sản phẩm. |
| NFR-04.04 | Khi xảy ra lỗi, hệ thống cần hiển thị thông báo phù hợp để người dùng biết thao tác không thành công. |

## 6. Availability Requirements

| Mã | Yêu cầu |
|---|---|
| NFR-05.01 | Hệ thống cần sẵn sàng trong thời gian làm việc chính của nhóm nội bộ. |
| NFR-05.02 | Các hoạt động bảo trì hoặc cập nhật hệ thống nên được thực hiện ngoài thời gian sử dụng chính nếu có thể. |
| NFR-05.03 | Khi triển khai production, hệ thống cần có cơ chế khởi động lại dịch vụ khi gặp lỗi ở mức container hoặc server. |

## 7. Backup and Recovery Requirements

| Mã | Yêu cầu |
|---|---|
| NFR-06.01 | Dữ liệu database cần được sao lưu định kỳ. |
| NFR-06.02 | File đính kèm và hình ảnh sản phẩm cần được sao lưu cùng với database. |
| NFR-06.03 | Hệ thống cần có quy trình phục hồi dữ liệu từ bản sao lưu khi xảy ra sự cố. |
| NFR-06.04 | Bản sao lưu production không nên lưu chung duy nhất trên server đang chạy ứng dụng. |

## 8. Maintainability Requirements

| Mã | Yêu cầu |
|---|---|
| NFR-07.01 | Mã nguồn module cần được tổ chức rõ ràng theo cấu trúc chuẩn của Odoo. |
| NFR-07.02 | Các thay đổi chức năng cần được quản lý bằng Git và lưu trên GitHub. |
| NFR-07.03 | Cấu hình development và production cần được tách riêng. |
| NFR-07.04 | Các logic nghiệp vụ quan trọng cần được đặt tên rõ ràng để dễ bảo trì và mở rộng. |
| NFR-07.05 | Tài liệu triển khai và vận hành cần được cập nhật khi có thay đổi quan trọng. |

## 9. Compatibility Requirements

| Mã | Yêu cầu |
|---|---|
| NFR-08.01 | Hệ thống được xây dựng trên Odoo Community 19.0. |
| NFR-08.02 | Hệ thống sử dụng PostgreSQL làm cơ sở dữ liệu. |
| NFR-08.03 | Hệ thống cần chạy được bằng Docker Compose trong môi trường development. |
| NFR-08.04 | Người dùng truy cập hệ thống qua trình duyệt web phổ biến. |

## 10. Deployment and Operation Requirements

| Mã | Yêu cầu |
|---|---|
| NFR-09.01 | Hệ thống production được triển khai trên VPS. |
| NFR-09.02 | Hệ thống production cần đặt sau web server như Nginx khi sử dụng domain và HTTPS. |
| NFR-09.03 | Cấu hình production không được bật demo data. |
| NFR-09.04 | Database production cần được giới hạn đúng database nghiệp vụ của hệ thống. |
| NFR-09.05 | Quy trình triển khai cần có bước kiểm tra sau khi cập nhật hệ thống. |

## 11. Data Requirements

| Mã | Yêu cầu |
|---|---|
| NFR-10.01 | Dữ liệu sản phẩm cần được lưu trữ nhất quán và tránh trùng lặp không cần thiết. |
| NFR-10.02 | Các dữ liệu phân loại như danh mục cần được quản lý tập trung. |
| NFR-10.03 | Hệ thống cần bảo toàn dữ liệu sản phẩm cũ khi sản phẩm không còn sử dụng. |
| NFR-10.04 | Dữ liệu cần có khả năng mở rộng để hỗ trợ thông tin khác nhau theo từng danh mục sản phẩm. |

## 12. Scope Notes

Các yêu cầu phi chức năng nâng cao như high availability, autoscaling, xác thực hai lớp, monitoring chuyên sâu, audit log chi tiết và disaster recovery đầy đủ chưa bắt buộc trong MVP. Những nội dung này có thể được xem xét ở giai đoạn sau khi hệ thống mở rộng hoặc có yêu cầu vận hành cao hơn.