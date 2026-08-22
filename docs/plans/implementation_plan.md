# Implementation Plan

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Product Management PV |
| Ứng dụng | Quản lý sản phẩm nội bộ |
| Nguồn đầu vào | [Functional Requirement](../architecture/detailed_technical_design.md) |
| Phiên bản tài liệu | Draft 1 |
| Ngày lập | 2026-08-07 |

![Project Lifecycle](../assets/Project%20Lifecycle.png)
**Project LifeCycle**
1. Requiremnt Intake: Thu thập input ban đầu từ customer, và tài liệu nguồn
2. Requirement Analysis: Làm rõ yêu cầu chức năng, phi chức năng, role, scope. Các output gồm non/functional requirements
3. Architecture and Technical Design: Thiết kế kiến trúc, data model, flow, access control, UI View ở mức kỹ thuật. Output gồm: architecture docs, data model, access controll design, detail technical design (flow)
4. Feature Planning: Chia yêu cầu thành các epic/task với thứ tự thực hiện, tiêu chí hoàn thành. Output là Implementation plan
4. Feature Implemenentation: Implement từng feature theo task, kiểm thử cơ bản, Output: working code.
5. Internal Testing: tự kiểm tra các luồng MVP chính, business rules, access control.
6. UAT Preparation & UAT: Chuẩn bị scenario, dữ liệu và hướng dẫn để custom xác nhận hệ thống đáp ứng nhu cầu sử dụng thực tế. Output gồm UAT Plan, UAT Scenarios, feedback log,
7. Maintainance và Future Improvements: theo dõi issule sau go-live và fix

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
Deferred to Testing 
UI improvements will be identified and fixed during manual testing and UAT based on actual usability issues.

## Epic 10. Testing 

| Done | ID | Task |
|---|---|---|
| Done | TST-01 | Viết Testing Guide để thống nhất môi trường test, database, user roles, test data stragy, format test case, bug handling, UI enhancement |
| Done | TST-02 | Tạo database `product_management_test` để chạy manual testing độc lập với db dev|
| Done | TST-03 | Cài đặt module `product_management` trên db `product_management_test` |
| Done | TST-04 | Thiết kế common test data dùng cho các features: categories, brands, category fields/options, và products |
| Done | TST-05 | Tạo test seed XML theo nhóm dữ liệu: categories, brands, category fields, product và product field values |
| Done | TST-06 | Load test seed data cho `product_management_test` và kiểm tra dữ liệu hiển thị đúng UI |
| Done | TST-07 | Viết test cases và manual test cho Category Management. |
| Done | TST-08 | Viết test cases và manual test cho Product Management và Product Business Rules. |
| Done | TST-09 | Viết test cases và manual test cho Product Discovery và Product Comparison. |
| Done | TST-10 | Viết test cases và manual test Account Management và Access Control. |
| Done | TST-11 | Xác định các feature còn thiếu/đã cover so với customer requirement |
| Not Started | TST-12 | Phân loại issue và giải quyết. |

### TST-12 Subtasks - Requirement Coverage Cleanup

| Status | ID | Task |
|---|---|---|
| Done | TST-12.01 | Cải thiện Product detail/specifications UI để người dùng đọc thông tin tư vấn dễ hơn, ưu tiên hướng `display_value` và giảm các cột kỹ thuật theo field type. |
| Done | TST-12.02 | Chốt và xử lý nhu cầu search/filter theo công dụng/purpose: dùng field cố định hay hỗ trợ search/filter trên dynamic field values. |
| Done | TST-12.03 | Bổ sung các data rule nhỏ còn thiếu: unique product code, category product count |
| Need Confirm | TST-12.04 | Rà soát archive/delete policy cho Product, Category, Brand và dynamic fields để MVP ưu tiên archive/ngừng sử dụng thay vì xóa cứng nếu không thật sự cần. |
| Deferred | TST-12.05 | Tách test seed XML khỏi production manifest để tránh load dữ liệu `TEST - ...` vào UAT/prod clean environment. |
| Done | TST-12.06 | Cập nhật lại tài liệu bị lệch với code hiện tại: Viewer category access, hard delete policy, addon README, dynamic field approach và testing status. |

#### TST-12 Subtasks - Dashboard

| Status | ID | Task |
|---|---|---|
| Done | DASH-01 | Tạo Dashboard MVP hiển thị tổng số product, available, low stock, out of stock và số category. |
| Done | DASH-02 | Hiển thị danh sách product mới cập nhật và product cần chú ý về tồn kho. |
| Done | DASH-03 | Thêm Dashboard menu và đặt làm màn đầu của Product Management. |
| Deferred | DASH-04 | Dashboard dạng biểu đồ hoặc KPI cards tùy biến. |
## Epic 11. UAT
## UAT Phases

UAT sẽ được thực hiện sau khi Testing phase hoàn tất các luồng MVP chính và không còn blocker/high severity issue.

| Phase | Mục đích | Kết quả đầu ra |
|---|---|---|
| UAT-01. UAT Preparation | Chuẩn bị môi trường, dữ liệu, tài khoản, danh sách scenario và phạm vi nghiệm thu. | UAT checklist, UAT database/data, user accounts, known issues list. |
| UAT-02. Internal Dry Run | Team nội bộ chạy thử các scenario UAT trước khi đưa cho customer/business user. | Danh sách lỗi còn lại, điều chỉnh scenario hoặc data nếu cần. |
| UAT-03. Customer/Business User Walkthrough | Hướng dẫn customer/business user luồng chính và phạm vi test. Chi tiết giao tiếp sẽ bổ sung sau. | Người dùng hiểu cách test, phạm vi UAT và cách ghi nhận feedback. |
| UAT-04. Customer/Business User Testing | Customer/business user chạy scenario theo checklist. Chi tiết lịch, người tham gia và kênh feedback sẽ bổ sung sau. | Kết quả Pass/Fail theo scenario, feedback nghiệp vụ, issue list. |
| UAT-05. Feedback Triage | Phân loại feedback thành blocker, bug, usability issue, change request hoặc nice-to-have. | Danh sách issue đã phân loại và quyết định xử lý. |
| UAT-06. Fix & Retest | Sửa lỗi thuộc phạm vi UAT MVP và retest các scenario liên quan. | Scenario đã retest, trạng thái issue cập nhật. |
| UAT-07. UAT Sign-off | Xác nhận phạm vi MVP đã đạt yêu cầu nghiệm thu hoặc ghi nhận known issues được chấp nhận. | UAT sign-off note, danh sách known issues, quyết định go/no-go. |
## Epic 11. Deployment & Handover

| Done | ID | Task |
|---|---|---|
| [ ] | DEP-01 | Chuẩn bị cấu hình production. |
| [ ] | DEP-02 | Triển khai hệ thống trên VPS. |
| [ ] | DEP-03 | Cấu hình Nginx/HTTPS nếu có domain. |
| [ ] | DEP-04 | Thiết lập backup database và filestore. |
| [ ] | DEP-05 | Viết hướng dẫn vận hành cơ bản. |
| [ ] | DEP-06 | Bàn giao source code, tài liệu và hướng dẫn sử dụng. |
