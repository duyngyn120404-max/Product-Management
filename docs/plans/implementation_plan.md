# Implementation Plan

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Product Management PV |
| Ứng dụng | Quản lý sản phẩm nội bộ |
| Nguồn đầu vào | [Functional Requirement](../architecture/detailed_technical_design.md) |
| Phiên bản tài liệu | Draft 1 |
| Ngày lập | 2026-08-07 |

## Epic 0. Technical Debt
| Status | ID | Task |
|---|---|---|
| Not Started | SEC-01 | Rà soát quyền unlink cho Product, Category, Brand và dynamic field để ưu tiên archive thay vì delete nhằm giữ lịch sử nghiệp vụ. |

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
## Epic 5. Product Discovery

| Done | ID | Task |
| --- | --- | --- |
| Done | DIS-01 | Đặt Product List làm điểm bắt đầu mặc định cho luồng tra cứu sản phẩm.
| Done | DIS-02 | Thiết lập domain mặc định chỉ hiển thị active product và bật default filter cho product_status = available.
| Done | DIS-03 |  Rà soát search fields hiện có và giữ các tiêu chỉ tra cứu chính: tên, mã, danh mục, và thương hiệu. | 
| Done | DIS-04 | Rà soát filter hiện có theo product status và stock status, bổ sung filter còn thiếu nếu cần|
| Done | DIS-05 | Rà soát group by hiện có theo danh mục, thương hiệu, product_status, và stock_status |
| Done | DIS-06 | Kiểm tra thao tác tìm kiếm, lọc, group by trên dữ liệu mẫu để phù hợp với luồng tư vấn |
| Done | DIS-07 | Kiểm tra thao tác sắp xếp trên Product List. |
| Done | DIS-08 | Kiểm tra Favourites để người dùng lưu các bộ lọc tra cứu nhanh |

## Epic 6. Product Comparison

| Status | ID | Task |
|---|---|---|
| Done | CMP-01 | Tạo compare wizard bằng TransientModel để lưu tạm danh sách product, category, tiêu chí và kết quả so sánh. |
| Done | CMP-02 | Thêm button Compare Products trên Product List để mở compare wizard cho các product được chọn mà không yêu cầu quyền write trên Product. |
| Done | CMP-03 | Validate số lượng product được chọn: tối thiểu 2 và tối đa 4 product trong một lần so sánh. |
| Done | CMP-04 | Validate các product được chọn phải thuộc cùng một category trước khi hiển thị bảng so sánh. |
| Done | CMP-05 | Hiển thị các tiêu chí thông tin chung để người dùng chọn/bỏ: mã sản phẩm, thương hiệu, giá, tồn kho, trạng thái tồn kho và trạng thái sản phẩm. |
| Done | CMP-06 | Hiển thị dynamic fields của category dưới dạng tiêu chí so sánh và cho phép người dùng chọn/bỏ từng field. |
| Done | CMP-07 | Tạo bảng so sánh readonly, hiển thị product theo cột và tiêu chí theo dòng. |
| Done | CMP-08 | Cập nhật bảng so sánh khi người dùng thay đổi tiêu chí trong wizard. |
| Done | CMP-09 | Hiển thị dấu gạch ngang cho tiêu chí không có giá trị ở một product. |
| Done | CMP-10 | Kiểm tra compare wizard bằng user Viewer để đảm bảo chỉ đọc Product nhưng vẫn mở và dùng compare được. |

## Epic 7. Basic Inventory

Scope:
- Basic Inventory trong MVP chỉ quản lý tồn kho đơn giản ở cấp product.
- Admin nhập `qty_available`, hệ thống tự tính `stock_status`.
- Chưa xử lý nhập kho/xuất kho, lịch sử biến động tồn kho, nhiều kho, giữ hàng hoặc tích hợp đơn bán.

| Status | ID | Task |
|---|---|---|
| Done | INV-01 | Xác nhận `qty_available` là số lượng tồn hiện tại của product trong phạm vi MVP. |
| Done | INV-02 | Không cho `qty_available` nhận giá trị âm khi tạo hoặc cập nhật product. |
| Done | INV-03 | Tự tính `stock_status` từ `qty_available` theo rule: hết hàng, sắp hết hàng, còn hàng. |
| Done | INV-04 | Không cho người dùng chỉnh tay `stock_status`; giá trị này do hệ thống kiểm soát. |
| Done | INV-05 | Hiển thị `qty_available` và `stock_status` trên Product List và Product Form. |
| Done | INV-06 | Hỗ trợ tra cứu sản phẩm theo `stock_status` thông qua filter và group by. |
| Done | INV-07 | Đưa thông tin tồn kho vào Product Comparison để người dùng so sánh nhanh giữa các sản phẩm. |
| [ ] | INV-08 | Chạy manual test cho các rule tồn kho trước khi nghiệm thu. |

## Epic 8. Account Managemnt
| Status | ID | Task |
|---|---|---|
| Done | ACC-01 | Xác định model nền tảng dùng cho account management, ưu tiên kế thừa `res.users` thay vì tạo model user riêng. |
| Done | ACC-02 | Tạo menu Account Management chỉ hiển thị cho Product Admin. |
| Done | ACC-03 | Tạo list/form view đơn giản để Product Admin xem danh sách user thuộc phạm vi Product Management. |
| Done | ACC-05 | Cho phép Product Admin tạo account Viewer mới với các thông tin tối thiểu: tên, email/login, trạng thái hoạt động. |
| Done | ACC-06 | Khi tạo account từ Account Management, tự gán quyền Product Management Viewer mặc định. |
| Done | ACC-07 | Cho phép Product Admin cập nhật thông tin cơ bản của Viewer như tên, email/login và trạng thái hoạt động. |
| Done | ACC-08 | Cho phép Product Admin gán đổi role trong phạm vi Product Management giữa Viewer và Admin theo rule được xác nhận. |
| Done | ACC-10 | Cho phép Product Admin reset password tạm thời. |
| Done | ACC-11 | Hiển thị lịch sử hoạt động cơ bản của account, ưu tiên các thông tin có sẵn như người tạo, ngày tạo, người cập nhật, ngày cập nhật và lần đăng nhập gần nhất nếu Odoo hỗ trợ. |
| Done | ACC-12 | Đảm bảo Viewer không thể truy cập menu Account Management. |
| Done | ACC-13 | Đảm bảo Product Admin không thể quản lý user ngoài phạm vi Product Management qua màn hình này. |
## Epic 9. Product UI Enhancement

## Epic 10. Testing & UAT

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

## Epic 11. Deployment & Handover

| Done | ID | Task |
|---|---|---|
| [ ] | DEP-01 | Chuẩn bị cấu hình production. |
| [ ] | DEP-02 | Triển khai hệ thống trên VPS. |
| [ ] | DEP-03 | Cấu hình Nginx/HTTPS nếu có domain. |
| [ ] | DEP-04 | Thiết lập backup database và filestore. |
| [ ] | DEP-05 | Viết hướng dẫn vận hành cơ bản. |
| [ ] | DEP-06 | Bàn giao source code, tài liệu và hướng dẫn sử dụng. |

