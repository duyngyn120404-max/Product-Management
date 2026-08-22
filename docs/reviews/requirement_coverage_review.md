# Requirement Coverage Review

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Product Management PV |
| Ứng dụng | Quản lý sản phẩm nội bộ |
| Nguồn đầu vào | |
| Phiên bản tài liệu | Draft 1 |
| Ngày lập | 2026-08-22 |

## 1. Purpose
Đối chiếu customer requirement, functional requirement, non-functional requirement, architecture docs và codebase hiện tại để xác định:
- Feature đã cover
- Feature cover một phần
- Feature còn thiếu
- Feature có thể skip/defer khỏi MVP
- Task cần làm tiếp trước UAT/production

## 2. Sources
- `docs/source/customer.pdf`
- `docs/source/4936998a-334e-4be0-82e6-b2de405c7df1_Backlog.pdf`
- `docs/source/15_cau_hoi_khao_sat_ung_dung_quan_ly_san_pham.docx`
- `docs/requirements/functional_requirements.md`
- `docs/requirements/non_functional_requirements.md`
- `docs/architecture/*`
- `docs/plans/implementation_plan.md`
- `addons/product_management/*`

## 3. Coverage Summary
- Functional MVP core: khoảng 75-80%
- Full project scope including NFR/deployment: khoảng 60-65%

## 4. Covered
- Authentication bằng cơ chế chuẩn của Odoo: login, logout, session và kiểm tra user active.

- Role cơ bản cho Product Management:
  - Product Management Admin
  - Product Management Viewer

- Phân quyền trong phạm vi Product Management:
  - Admin quản lý dữ liệu.
  - Viewer chỉ xem/tra cứu.
  - Viewer không thấy Account Management.

- Account Management:
  - Xem danh sách account thuộc Product Management.
  - Tạo Viewer account.
  - Cập nhật tên, email/login và trạng thái active.
  - Đổi role Viewer/Admin theo guard rules.
  - Set temporary password.
  - Xem activity info cơ bản.

- Category Management:
  - Tạo/cập nhật category.
  - Archive/restore category.
  - Parent category.
  - Cấu hình dynamic fields theo category.
  - Cấu hình selection options.

- Product Management:
  - Tạo/cập nhật product.
  - Gắn category và brand.
  - Upload/xem ảnh chính.
  - Quản lý giá bán.
  - Quản lý quantity.
  - Product status: Draft, Available, Discontinued.
  - Archive product theo rule trạng thái.

- Product Specifications:
  - Tự đồng bộ specifications theo category.
  - Lưu giá trị dynamic fields theo product.
  - Required specifications kiểm soát trạng thái Available.

- Product Discovery:
  - Product List là màn chính.
  - Search theo tên, mã, category, brand.
  - Filter theo product status và stock status.
  - Group by category, brand, product status, stock status.
  - Default list ưu tiên active/available products.

- Product Comparison:
  - Compare 2-4 product cùng category.
  - Chặn compare khác category.
  - Chọn/bỏ tiêu chí compare.
  - So sánh thông tin chung và dynamic fields.
  - Bảng compare readonly.

- Basic Inventory:
  - Lưu quantity hiện tại.
  - Không cho quantity âm.
  - Tự tính stock status: In Stock, Low Stock, Out of Stock.
  - Hiển thị stock status trên list/form/search/compare.

- Testing Foundation:
  - Testing guide.
  - Test database.
  - Test seed data.
  - Manual test cases cho các feature chính.

## 5. Gaps / Need More Work

## 5. Gaps, Open Questions, and Deferred Items

| Status | Area | Item | Notes | Suggested Decision |
|---|---|---|---|---|
| Partial | Product Consultation UX | Product detail/specifications còn khó đọc cho mục đích tư vấn | Đã có product form, ảnh, giá, tồn kho, category, brand và dynamic specifications; nhưng specs UI còn kỹ thuật, nhiều cột theo type. Nội dung tư vấn như công dụng, ưu/nhược điểm, đối tượng phù hợp có thể cover bằng dynamic fields nhưng chưa có layout cố định. | Ưu tiên cải thiện bằng `display_value`; chấp nhận dynamic fields cho MVP nếu customer không yêu cầu layout riêng. |
| Missing | Product Discovery | Chưa search/filter rõ theo công dụng/purpose | Customer/backlog có yêu cầu lọc theo công dụng. Nếu công dụng là dynamic field thì hiện cũng chưa có search/filter dynamic field values rõ ràng. | Cần chốt trước UAT: thêm field cố định hay hỗ trợ search/filter dynamic fields. |
| Missing | Product & Category Data Rules | Thiếu một số data rule nhỏ: unique product code, category product count, required numeric value `0` | `default_code` chưa unique; category list chưa có product count; cần chốt `0` có hợp lệ cho required integer/decimal không. | Nên làm unique code + product count; chốt rule numeric `0` là hợp lệ nếu không có lý do nghiệp vụ khác. |
| Partial | Archive/Delete Policy | Stop using product/category chưa thống nhất hoàn toàn | Đã có active/archive và product status; nhưng ACL vẫn cho unlink. Category inactive không tự ảnh hưởng product, và delete parent category bị chặn bằng message kỹ thuật. | Chốt MVP ưu tiên archive, hạn chế unlink; custom message nếu còn thời gian; không cascade trạng thái category sang product nếu chưa có yêu cầu. |
| Partial | Production Readiness & NFR | Production/deployment/testing chưa hoàn chỉnh | Đã có compose/config nền; còn thiếu Nginx, HTTPS, backup/restore, deployment checklist, performance/responsive/backup verification. | Làm trong Deployment epic; không block feature testing nhưng block production go-live. |
| Partial | Documentation Consistency | Docs lệch với code hiện tại | Một số docs còn lệch: Viewer category access, hard delete product, addon README, dynamic field approach, testing status. | Update trước UAT/sign-off. |
| Missing | Test Data Isolation | Test seed XML đang nằm trong manifest `data` | Có nguy cơ load dữ liệu `TEST - ...` vào UAT/prod nếu không tách. | Must fix trước clean UAT/prod. |
| Deferred | Non-MVP / Later Scope | Dashboard, reports, custom profile page, full ACL testing, advanced inventory, mobile app, customer portal, sales/payment/accounting, AI suggestion | Các mục này hoặc nằm ngoài MVP, hoặc customer nói chưa cần, hoặc chỉ hữu ích khi hệ thống có nhiều app/user group hơn. | Skip hiện tại; revisit sau UAT hoặc khi customer yêu cầu. |
## 6. Deferred / Skipped

| Item | Reason | Revisit When |
|---|---|---|
| Dashboard / overview | Customer PDF có nhắc, nhưng backlog xếp phần lớn là Should/Could. Product List hiện đang là màn chính và đủ dùng cho tra cứu MVP. | Customer yêu cầu trong UAT hoặc cần quick overview cho vận hành. |
| Custom user profile page | Customer nói không cần làm thành trang riêng. Odoo đã có built-in profile/preferences/change password/logout. | Người dùng thấy Odoo built-in khó dùng hoặc cần profile riêng trong Product Management. |
| Full Access Control testing | Hiện chỉ có một internal app, hai role đơn giản. Smoke test đủ cho MVP hiện tại. | Hệ thống có nhiều app, nhiều phòng ban, nhiều nhóm quyền hoặc dữ liệu chia theo scope. |
| Advanced inventory | Customer đã ghi ngoài phạm vi MVP: phiếu nhập, phiếu xuất, nhà cung cấp, lịch sử kho, kiểm kê. | Cửa hàng cần quản lý vận hành kho thật. |
| Reports | Customer PDF nói báo cáo chưa cần trong MVP. Backlog report chủ yếu Should/Could. | Cần xem danh sách hàng hết, tổng giá trị tồn kho, báo cáo theo danh mục hoặc export Excel. |
| AI product suggestion | Customer PDF ghi ngoài phạm vi MVP. | Có đủ dữ liệu sản phẩm và cần tư vấn/gợi ý tự động. |
| Customer portal / external users | Customer PDF ghi ngoài phạm vi MVP, hệ thống hiện chỉ dùng nội bộ. | Muốn khách hàng hoặc partner tự truy cập. |
| Sales/payment/accounting | Customer PDF ghi ngoài phạm vi MVP. | Cần quản lý bán hàng, đơn hàng, thanh toán hoặc kế toán. |
| Mobile app riêng | Customer PDF ghi ngoài phạm vi MVP. | Người dùng cần app native hoặc workflow mobile chuyên biệt. |
| Deep performance/load testing | MVP dưới 10 user và khoảng 100 sản phẩm, manual verification là đủ ở giai đoạn này. | Trước production hoặc khi dữ liệu/user tăng. |
| Responsive/mobile UI testing sâu | Người dùng chủ yếu dùng trình duyệt web; chưa phải blocker cho internal MVP. | Trước UAT chính thức hoặc khi người dùng test nhiều trên mobile/tablet. |
| Cross-app permission conflict testing | Hiện Product Management gần như là app độc lập. | Khi triển khai thêm app khác hoặc chia quyền giữa nhiều module. |
| Custom dashboard/report architecture | Chưa có nhu cầu vận hành dashboard/report rõ ràng trong MVP. | Sau UAT, nếu customer muốn xem KPI/tổng quan. |
