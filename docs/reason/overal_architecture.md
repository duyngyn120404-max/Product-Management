# Overal Architecture Design

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Product Management PV |
| Ứng dụng | Quản lý sản phẩm nội bộ |
| Nguồn đầu vào | `overal_architecture.md` |
| Phiên bản tài liệu | Draft 1 |
| Ngày lập | 2026-08-06 |

## 1. Nội dung tài liệu

Tài liệu này nhằm diễn giải các techstack, kiến trúc được chọn ở phiên bản hiện tại

## 2. Lý do chọn các tech stack

1. *Vì sao chọn Odoo làm nền tảng phát triển?*

> Odoo được chọn vì phù hợp với bài toán quản lý nghiệp vụ nội bộ và có sẵn các thành phần nền tảng như quản lý người dùng, phân quyền, ORM, giao diện quản trị và tích hợp PostgreSQL. Điều này giúp rút ngắn thời gian phát triển MVP so với việc xây dựng toàn bộ hệ thống từ đầu, đồng thời vẫn cho phép mở rộng sang các nghiệp vụ như tồn kho, bán hàng hoặc báo cáo trong tương lai.

2. *Có những lựa chọn thay thế về nền tảng phát triển nào?*

> Hiện này có nhiều hướng để xây dựng hệ thống quản lý nguồn lực như custom web app (React, FastAPI, PostgreSQL, AdminUI,..), Low code (Retool), other ERP (Dolibarrr, Tryton,...). Lựa chọn Odoo vi Odoo là một nền tảng nghiệp vụ đầy đủ và khả năng mở rộng tốt hơn về lâu dài. 

3. *Vì sao chọn PostgreSQL mà k chọn DB khác?*

> PostgreSQL được chọn vì đây là hệ quản trị cơ sở dữ liệu chính thức và là 1 phần kiến trúc của Odoo. Odoo được thiết kế để hoạt động với PostgreSQL như ORM, model, access control,... Tương tác tốt, giảm rủi ro kỹ thuât và k cần tự tích hợp với DB khác

4. *Vì sao Nginx được sủ dụng thay vì forward thẳng vào cho Odoo?*

> Cần Nginx vì production k chỉ cần app chạy được, mà còn cần một lớp web server đứng trước để xử lý traffic an toàn và ổn định. Với quy mô hiện tại, Nginx k được dùng vì nhu cầu hiệu năng, mà vì yêu cầu triển khai production an toàn và chuẩn. Nó xư lý SSL, route request, log truy cập, k expose Odoo trực tiếp ra ngoài

## 3. Lý do chọn kiến trúc

1. *Vì sao chọn kiến trúc này?*

> Phù hợp với Odoo (PostgreSQL, Filestore), phù hợp quy mô nội bộ (k cần microservice hay cloud, only VPS), dễ triển khai với Docker Compose, dễ mở rộng sau (upgrade VPS, db,...)

2. *Các kiến trúc nào có thể thay thế?*

> Custom web app (react/vue + Backend + DB): linh hoạt nhưng phải tự dev nhiều
> Low-code/internal tool (retool, appsmith): nhanh với MVP, nhưng khó custom, mở rộng
> ERP khác (ERPNext, Dolibarr): nhẹ hơn nhưng mở rộng kém 
> Cloud: tốt hơn về vận hành nhưng tăng chi phí phức tạp
> Microservices: quá phức tạp cho hệ nội bộ

3. *Một vài rủi ro cho kién trúc này?*

> Singple point of failure: VPS chết -> app chết
> Hiệu năng: server VPS yếu