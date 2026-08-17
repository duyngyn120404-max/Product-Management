# Implementation Plan

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Product Management PV |
| Ứng dụng | Quản lý sản phẩm nội bộ |
| Nguồn đầu vào | [Functional Requirement](../architecture/detailed_technical_design.md) |
| Phiên bản tài liệu | Draft 1 |
| Ngày lập | 2026-08-07 |

## Epic 1. Project Setup
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
To end:: 11/08/2026

| Done | ID | Task |
|---|---|---|
| Done | CAT-01 | Tạo model category. |
| Done | CAT-02 | Cho phép Admin tạo, cập nhật, ngừng sử dụng và xóa danh mục. |
| Done | CAT-03 | Tạo model định nghĩa field theo danh mục và model cho field options. |
| Done | CAT-04 | Cho phép Admin cấu hình field, kiểu dữ liệu, trạng thái bắt buộc và thứ tự hiển thị. |

## Epic 4. Product Management 
| Done | ID | Task |
|---|---|---|
| Done | PRO-01 | Tạo model sản phẩm. |
| Done | PRO-02 | Cho phép Admin tạo, cập nhật ngừng sử dụng và xóa sản phẩm. |
| Done | PRO-03 | Gắn sản phẩm với danh mục. |
| Done | PRO-04 | Đồng bộ khi category field thay đổi. |

Future works:
- thêm một case thông báo (hoặc raise error/hướng dẫn archieve) cho category field.
- sync khi option của selector field thay đổi 
- Ẩn bớt cột kỹ thuật (Text, Decimal,...)
- Compute stock status

## Epic 4. Product Business Rules (Additional for more constraints)
| Done | ID | Task |
| --- | --- | --- |
| Done | BR-01 | Đảm bảo active và product_status không mâu thuẫn nhau.
| Done | BR-02 | Prevent negative list_price.
| Done | BR-03 | Prevent negative qty_available.
| Done | BR-04 | Compute stock_status from qty_available.
| Done | BR-05 | Validate required dynamic fields when product becomes available.
| Done | BR-06 | Validate selection option belongs to its category field.

Future works:
- Ẩn sản phẩm `draft` khỏi màn tra cứu chính của Consultant/Viewer; Discovery mặc định chỉ hiển thị `active=True` và `product_status` thuộc `available` hoặc `discontinued`.
- Làm rõ rule giá cho sản phẩm `available`: xử lý trường hợp giá chưa chốt hoặc giá liên hệ trước khi enforce `list_price > 0`.
- Hoàn thiện Product Discovery default domain/filter theo business rules, đặc biệt với `draft`, `discontinued` và archived product.
- Chốt cách xử lý dữ liệu cũ khi category field bị inactive: giữ lại Product Field Value cũ, ẩn khỏi form chính, và dùng lại nếu field được active lại.

## Epic 5. Product Discovery

Mục tiêu: cung cấp các công cụ tra cứu để Consultant/Viewer tìm, lọc, sắp xếp
và mở đúng sản phẩm nhanh hơn dựa trên dữ liệu product đã được kiểm soát bởi
business rules.

| Done | ID | Task |
| --- | --- | --- |
| Not Started | DIS-01 | Đặt Product List làm điểm bắt đầu mặc định cho luồng tra cứu sản phẩm.
| Not Started | DIS-02 | Thiết lập domain mặc định cho màn tra cứu: active product và trạng thái phù hợp cho Consultant/Viewer.
| Not Started | DIS-03 | Tối ưu tìm kiếm nhanh theo tên sản phẩm và mã sản phẩm.
| Not Started | DIS-04 | Bổ sung filter theo danh mục, thương hiệu, product_status và stock_status.
| Not Started | DIS-05 | Bổ sung filter tư vấn thường dùng: đang bán, ngừng bán, còn hàng, sắp hết hàng, hết hàng.
| Not Started | DIS-06 | Bổ sung group by theo danh mục, thương hiệu, trạng thái sản phẩm và trạng thái tồn kho.
| Not Started | DIS-07 | Bổ sung khả năng sắp xếp theo giá, tên và tồn kho nếu Odoo view/action hỗ trợ phù hợp.
| Not Started | DIS-08 | Kiểm tra bằng user Viewer để đảm bảo luồng tra cứu chỉ đọc nhưng vẫn đủ thông tin tư vấn.

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
