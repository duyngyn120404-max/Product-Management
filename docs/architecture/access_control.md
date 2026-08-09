# Access Control

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Product Management PV |
| Ứng dụng | Quản lý sản phẩm nội bộ |
| Nguồn đầu vào | [Detailed Technical Design](./detailed_technical_design.md) |
| Phiên bản tài liệu | Draft 1 |
| Ngày lập | 2026-08-06 |

Mục tiêu của tài liệu là quy định các thao tác của người dùng trong ứng dụng phù hợp với phân quyền

## 1. Access Right
Access Rights được cấu hình theo model bằng `ir.model.access.csv`


| Model | Admin | Viewer |
|---|---|---|
| Product | Read, Create, Update, Unlink | Read |
| Category | Read, Create, Update, Unlink | Read |
| Category Field Definition | Read, Create, Update, Unlink | Read |
| Product Field Value | Read, Create, Update, Unlink | Read |
| Product Image / Attachment | Read, Create, Update, Unlink | Read |
| User Account | Read, Create, Update, Unlink | Không có quyền quản lý |

## 2. Menu and UI Access

| Menu / Action | Admin | Viewer |
|---|---|---|
| Xem danh sách sản phẩm | Có | Có |
| Xem chi tiết sản phẩm | Có | Có |
| Tìm kiếm, lọc, sắp xếp sản phẩm | Có | Có |
| So sánh sản phẩm | Có | Có |
| Quản lý sản phẩm | Có | Không |
| Quản lý danh mục | Có | Không |
| Quản lý tài khoản | Có | Không |

## 3. Notes
- Secret và thông tin cấu hình không thuộc Access Control của ứng dụng, sẽ được xử lý trong Deployment.