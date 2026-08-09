# Functional Requirements — Product Management

## 1. Thông tin tài liệu

| Thuộc tsnh | Giá trị |
|---|---|
| Dự án | Product Management PV |
| Ứng dụng | Quản lý sản phẩm nội bộ |
| Nền tảng mục tiêu | Odoo Community 19.0 |
| Nguồn đầu vào | `docs/requirements/function_requirements` |
| Ngày lập | 2026-08-06 |

Tài liệu này nhằm mục đích bảo vệ các yêu cầu chức năng dược đua ra trong `functional_requirements`

## 2. Xác thực
1. *Xác thực là gì?*

>Là quá trình hệ thống xác minh thông tin đăng nhập người dùng, nếu đúng thì cho phép, sai thì từ chối truy cập

2. *Vì sao ở xác thực chỉ có 6 yêu cầu, vì sao k chọn 6 yêu cầu khác?*

>Chọn các yêu cầu Authentication này vì đây là các chức năng xác thực cơ bản cần có cho MVP nội bộ: đăng nhập, kiểm tra thông tin đăng nhập, kiểm tra trạng thái tài khoản, duy trì phiên làm việc và đăng xuất. Các chức năng nâng cao như xác thực hai lớp, khóa tạm sau nhiều lần đăng nhập sai, tự động hết phiên sau một thời gian, hoặc chính sách mật khẩu phức tạp chưa cần thiết trong phạm vi MVP hiện tại. Những chức năng liên quan đến quản trị người dùng như tạo tài khoản, khóa/mở tài khoản, đặt lại mật khẩu và gán vai trò sẽ được mô tả riêng trong phần User Management hoặc Access Control.

## 3. Phân quyền

1. *Phân quyền là gì*

>Là cơ chế cho phép hệ thống xác định người dùng được thực hiện những nhóm thao tác nào

2. *Vì sao chọn các yêu cầu ở phân quyền?*

>Vì MVP hiện tại chỉ có hai nhóm người dùng nội bộ: quản trị viên và người xem. Vì vậy phân quyền cần tập trung vào việc rách rõ người quản lý và người sử dụng hệ thống để tra cứu dữ liệu. Các phân quyền nâng cao như phân quyền theo từng danh mục, từng tường dữ liệu, chi nhánh, lịch sử thay đổi, role riêng cho khách hàng, hay nhiều role phức tạp khác chưa đề cập vì làm hệ thống phức tạp

## 4. Quản lý tài khoản

1. *Quản lý tài khoản là gì*

>Là chức năng giúp admin quản lý các tài khoản trong hệ thống, gồm tạo, cập nhật, khóa,.. tài khoản

2. *Vì sao cần quản lý tài khoản?*

>Quản lý tài khoản là cần thiết để ai được truy cập hệ thống. Vì đây là ứng dụng nội bộ, chỉ những người thuộc team mới được đăng nhập và sử dụng dữ liệu sản phẩm. Admin cần có khả năng tạo tài khoản, khóa/mở tài khoản, gán vai trò và đặt lại mật khẩu để quản lý vòng đời tài khoản trong hệ thống`

## 5. Quản lý danh mục

1. *Quản lý danh mục là gì?*

>Danh mục là nhóm chức năng để sắp xếp các sản phẩm có cùng đặc điểm hoặc cùng mục đích sử dụng

2. *Vì sao cần quản lý danh mục, thay vì để chung trong sản phẩm và filter danh mục?*

>Vì danh mục không chỉ để lọc sản phẩm, mà còn đại diện cho từng nhóm sản phẩm có cấu trúc thông tin khác nhau. Ví dụ thực phẩm có thể cần hạn dùng, thành phần trong khi thời gian cần size, màu sắc, chất liệu. Vì vậy hệ thống cần quản lý danh mục như một nghiệp vụ riêng để dễ mở rộng các trường thông tin theo từng nhóm khi cần.

## 6. Quản lý sản phẩm

1. *Quản lý sản phẩm là gì*

>Là nhóm các chức năng cho phép Admin quản lý vòng đời dữ liệu của sản phẩm, như tạo mới, cập nhât,.. đến đánh dấu ngừng sử dụng sản phẩm

2. *Những tính năng nào cần cân nhắc ở tính năng quản lý sản phẩm?*

>Import/Export dữ liệu với format file xlxs, lịch sử thay đổi sản phẩm, quản lý nhiều ảnh/tập đính kèm, kiểm tra tính hợp lệ theo từng danh mục

## 7. Danh sách sản phẩm

1. *Danh sách sản phẩm là gì?*

>Là chức năng cho phép nhân viên xem tập hợp sản phẩm trong hệ thống dưới dạng danh sách nhằm hỗ trợ tra cứu nhanh chóng thông tin sản phẩm để phục vụ tư vấn khách hàng

2. *Những tính năng nào có thể có thêm trong danh sách sản phẩm ngoài CRUD?*

>Các tính năng trong danh sachs sản phẩm phục vụ 4 tiêu chí chính tìm ra nhóm sản phẩm đúng, đủ, nhanh và trực quan thông qua bộ lọc, tìm kiếm, sắp xếp và cách trình bày (sẽ được trình bày sau). 

## 8. Chi tiết sản phẩm

1. *Chi tiết sản phẩm là gì?*

>Là tính năng cho phép người dùng xem đúng, nhanh, đủ các thông tin của 1 sản phẩm cụ thể

2. *Những tính năng nào có thể thêm trong danh sahcs sản phẩm?*

>Xuất dữ liệu nhanh để tư vấn

## 9. Tìm kiếm, lọc và sắp xếp

1. *Tìm kiếm và bộ lọc khác nhau như nào?*

> Tìm kiếm dựa trên từ khóa tự do do người dùng dùng, còn bộ lọc dựa trên các điều kiện có cấu trúc

2. *Vì sao chọn danh mục, mã, tên,.. làm tiêu chí lọc?*
> Tại nó phổ biến 

## 10. Quản lý tồn kho 

1. *Quản lý tồn kho là gì?*

> là nhóm chức năng giúp hệ thống theo dõi và kiểm soát số lường hàng còn lại của từng sản phẩm, ở phạm vi hiện tại thì gồm  số lượng hiện tại, trạng thái còn/hết/sắp hết của 1 sản phẩm.

2. *Các tính năng nào có thể có trong tương lai?*

> Gồm phiếu nhập kho, phiếu xuất kho, lichj sử nhập, xuất hàng, kiểm kê, tồn khoo,...