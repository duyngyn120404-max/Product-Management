# Detailed Technical Design

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Product Management PV |
| Ứng dụng | Quản lý sản phẩm nội bộ |
| Nguồn đầu vào | [Detail Technical Design](./detailed_technical_design.md) |
| Phiên bản tài liệu | Draft 1 |
| Ngày lập | 2026-08-06 |

Tài liệu này mô tả cách thiết kế giao diện cho hệ thống quản lý sản phẩm nôi bộ

## 1. Main Menus:

| Menu | Người dùng | Mục đích |
|---|---|---|
| Dashboard | Admin, Viewer | Xem tổng quan số lượng sản phẩm, danh mục và các sản phẩm cần chú ý. |
| Products | Admin, Viewer | Xem danh sách, tra cứu và mở chi tiết sản phẩm. |
| Categories | Admin, Viewer | Admin quản lý danh mục và field theo danh mục; Viewer chỉ xem để hiểu cấu trúc thông tin sản phẩm. |
| Users | Admin | Quản lý tài khoản và vai trò người dùng. |

## 2. Dashboard Views:

| View | Mục đích |
|---|---|
| Product Dashboard Form View | Hiển thị tổng số product, product available, low stock, out of stock, số category, product mới cập nhật và product cần chú ý về tồn kho. |

## 3. Product Views:

| View | Mục đích |
|---|---|
| Product List View | Hiển thị danh sách sản phẩm với các thông tin chính như mã, tên, danh mục, thương hiệu, giá, tồn kho và trạng thái. |
| Product Form View | Cho phép Admin tạo/cập nhật sản phẩm và nhập các thông tin theo danh mục. |
| Product Detail View | Hiển thị đầy đủ thông tin sản phẩm để người dùng tra cứu và tư vấn khách hàng. |
| Product Compare View | Hiển thị nhiều sản phẩm cùng danh mục cạnh nhau theo các tiêu chí được chọn. |

## 4. Category Views:

| View | Mục đích |
|---|---|
| Category List View | Hiển thị danh sách danh mục. |
| Category Form View | Cho phép Admin tạo/cập nhật danh mục và cấu hình các field thuộc danh mục đó. |

### 5. User Views

| View | Mục đích |
|---|---|
| User List View | Hiển thị danh sách tài khoản nội bộ. |
| User Form View | Cho phép Admin cập nhật thông tin tài khoản và gán vai trò. |

### 6. UI Access

| View / Action | Admin | Viewer |
|---|---|---|
| Dashboard View | Có | Có |
| Product List View | Có | Có |
| Product Detail View | Có | Có |
| Product Compare View | Có | Có |
| Product Form Create/Edit | Có | Không |
| Category Views | Có, tạo/sửa/archive | Có, chỉ xem |
| User Views | Có | Không |
