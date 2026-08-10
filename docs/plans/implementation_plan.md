# Implementation Plan

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Product Management PV |
| Ứng dụng | Quản lý sản phẩm nội bộ |
| Nguồn đầu vào | [Functional Requirement](../architecture/detailed_technical_design.md) |
| Phiên bản tài liệu | Draft 1 |
| Ngày lập | 2026-08-07 |

## Epic 1. Project Setup
Start from: 
To end: 
| Status | ID | Task |
|---|---|---|
| Done | SET-01 | Thiết lập cấu trúc repository. |
| Done | SET-02 | Cấu hình Docker Compose cho Odoo và PostgreSQL. |
| Done | SET-03 | Tạo custom addon `product_management`. |
| Done | SET-04 | Tạo menu gốc ứng dụng. |
| Done | SET-05 | Quy trình tạo branch, pull, xác định ranh giới của Prod, Dev, Test. |
| Done | SET-06 | Viết README. |

## Epic 2. Category Management
Start from: 10/08/2026
To end:

| Done | ID | Task |
|---|---|---|
| Done | CAT-01 | Tạo model category. |
| Done | CAT-02 | Cho phép Admin tạo, cập nhật, ngừng sử dụng và xóa danh mục. |
| Done | CAT-03 | Tạo model định nghĩa field theo danh mục và model cho field options. |
| In Progress | CAT-04 | Cho phép Admin cấu hình field, kiểu dữ liệu, trạng thái bắt buộc và thứ tự hiển thị. |
| Not Started | CAT-05 | Đảm bảo danh mục quyết định bộ field của sản phẩm. |

## Epic 4. Product Management 
| Done | ID | Task |
|---|---|---|
| [ ] | PRO-01 | Tạo model sản phẩm. |
| [ ] | PRO-02 | Cho phép Admin tạo, cập nhật và ngừng sử dụng sản phẩm. |
| [ ] | PRO-03 | Gắn sản phẩm với danh mục. |
| [ ] | PRO-04 | Lưu thông tin chung của sản phẩm. |
| [ ] | PRO-05 | Lưu giá trị field động theo danh mục bằng mô hình EAV. |
| [ ] | PRO-06 | Hiển thị trạng thái sản phẩm và tồn kho cơ bản. |

## Epic 5. Product Discovery

| Done | ID | Task |
|---|---|---|
| [ ] | DIS-01 | Xây dựng danh sách sản phẩm. |
| [ ] | DIS-02 | Xây dựng trang chi tiết sản phẩm. |
| [ ] | DIS-03 | Tìm kiếm theo tên hoặc mã sản phẩm. |
| [ ] | DIS-04 | Lọc theo danh mục, trạng thái và thương hiệu. |
| [ ] | DIS-05 | Sắp xếp danh sách theo giá. |
| [ ] | DIS-06 | Hiển thị thông tin chi tiết theo field của danh mục. |

## Epic 6. Product Comparison

| Done | ID | Task |
|---|---|---|
| [ ] | CMP-01 | Cho phép người dùng chọn nhiều sản phẩm cùng danh mục. |
| [ ] | CMP-02 | Cho phép người dùng chọn hoặc bỏ tiêu chí so sánh. |
| [ ] | CMP-03 | Hiển thị bảng so sánh theo field chung và field động của danh mục. |
| [ ] | CMP-04 | Chặn hoặc cảnh báo khi chọn sản phẩm khác danh mục. |

## Epic 7. Basic Inventory

| Done | ID | Task |
|---|---|---|
| [ ] | INV-01 | Lưu số lượng tồn hiện tại của sản phẩm. |
| [ ] | INV-02 | Cập nhật trạng thái còn hàng, hết hàng hoặc sắp hết nếu cần. |
| [ ] | INV-03 | Hiển thị tồn kho trong danh sách và chi tiết sản phẩm. |
| [ ] | INV-04 | Hỗ trợ lọc sản phẩm theo trạng thái tồn kho. |

## Epic 8. Testing & UAT

| Done | ID | Task |
|---|---|---|
| [ ] | TST-01 | Test quyền Admin và Viewer. |
| [ ] | TST-02 | Test tạo, cập nhật và ngừng sử dụng danh mục. |
| [ ] | TST-03 | Test field động theo danh mục. |
| [ ] | TST-04 | Test tạo, cập nhật và ngừng sử dụng sản phẩm. |
| [ ] | TST-05 | Test danh sách, chi tiết, tìm kiếm, lọc và sắp xếp. |
| [ ] | TST-06 | Test so sánh sản phẩm. |
| [ ] | TST-07 | Test performance theo NFR MVP. |
| [ ] | TST-08 | Chuẩn bị dữ liệu demo/UAT. |

## Epic 9. Deployment & Handover

| Done | ID | Task |
|---|---|---|
| [ ] | DEP-01 | Chuẩn bị cấu hình production. |
| [ ] | DEP-02 | Triển khai hệ thống trên VPS. |
| [ ] | DEP-03 | Cấu hình Nginx/HTTPS nếu có domain. |
| [ ] | DEP-04 | Thiết lập backup database và filestore. |
| [ ] | DEP-05 | Viết hướng dẫn vận hành cơ bản. |
| [ ] | DEP-06 | Bàn giao source code, tài liệu và hướng dẫn sử dụng. |