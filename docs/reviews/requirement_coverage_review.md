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
  - Lưu công dụng/purpose phục vụ tư vấn.
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
  - Search theo tên, mã, category, brand, purpose.
  - Filter theo product status và stock status.
  - Group by category, brand, product status, stock status.
  - Default list ưu tiên active/available products.

- Dashboard:
  - Dashboard menu là màn đầu của Product Management.
  - Hiển thị tổng số product, product available, low stock, out of stock và số category.
  - Hiển thị product mới cập nhật và product cần chú ý về tồn kho.

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
| Done | Product Consultation UX | Product detail/specifications đã được làm gọn hơn | Product form có purpose và specifications dùng `display_value` để list đọc dễ hơn; dynamic fields vẫn dùng cho thông tin riêng theo category. | Retest trong UAT nếu customer cần layout tư vấn riêng hơn. |
| Done | Product Discovery | Search theo công dụng/purpose | Purpose được xử lý bằng field cố định trên Product để search thống nhất, thay vì search dynamic field values. | Dynamic field value search/filter vẫn deferred nếu customer yêu cầu sau UAT. |
| Done | Product Data Rules | Unique product code | `default_code` đã có unique constraint khi có nhập giá trị; placeholder form hướng dẫn format mã sản phẩm. | Category product count deferred; required numeric `0` accepted by current implementation. |
| Need Confirm | Archive/Delete Policy | Stop using product/category chưa thống nhất hoàn toàn | Đã có active/archive và product status; current implementation vẫn giữ unlink trong internal testing. Category inactive không tự ảnh hưởng product, và delete parent category bị chặn bằng message kỹ thuật. | Giữ current behavior hiện tại; bàn lại với customer trước UAT/prod. |
| Partial | Production Readiness & NFR | Production/deployment/testing chưa hoàn chỉnh | Đã có compose/config nền; còn thiếu Nginx, HTTPS, backup/restore, deployment checklist, performance/responsive/backup verification. | Làm trong Deployment epic; không block feature testing nhưng block production go-live. |
| Done | Documentation Consistency | Docs chính đã được đồng bộ với code hiện tại | Đã cập nhật Viewer category access, hard delete policy note, addon README, dynamic field approach, purpose field và testing status. | Tiếp tục rà khi có thay đổi mới. |
| Deferred | Test Data Isolation | Test seed XML đang nằm trong manifest `data` | Có nguy cơ load dữ liệu `TEST - ...` vào UAT/prod nếu không tách. Team quyết định giữ hiện tại trong internal testing. | Revisit trước clean UAT/prod. |
| Deferred | Non-MVP / Later Scope | Reports, custom profile page, full ACL testing, advanced inventory, mobile app, customer portal, sales/payment/accounting, AI suggestion | Các mục này hoặc nằm ngoài MVP, hoặc customer nói chưa cần, hoặc chỉ hữu ích khi hệ thống có nhiều app/user group hơn. | Skip hiện tại; revisit sau UAT hoặc khi customer yêu cầu. |
## 6. Deferred / Skipped

| Item | Reason | Revisit When |
|---|---|---|
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
| Custom dashboard/report architecture | Dashboard MVP dùng form/list chuẩn của Odoo để hiển thị số liệu và danh sách cần chú ý. Dashboard dạng chart/KPI cards hoặc report chuyên sâu chưa cần trong MVP. | Sau UAT, nếu customer muốn xem KPI/tổng quan riêng hơn. |
