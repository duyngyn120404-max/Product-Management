# UAT Guide
| Thuộc tính | Giá trị |
|---|---|
| Dự án | Product Management PV |
| Ứng dụng | Quản lý sản phẩm nội bộ |
| Nguồn đầu vào |  |
| Phiên bản tài liệu | Draft 1 |
| Ngày lập | 2026-08-22 |

## 1. Objective

Xác nhận Product Management MVP đáp ứng đủ các luồng nghiệp vụ chính để user dùng thử, góp ý và quyết định có thể chuyển sang bước tiếp theo hay không.

## 2. Scope

### In Scope

- Dashboard
- Category Management
- Product Management
- Product Detail / Specifications
- Product Discovery / Search / Filter / Group By
- Product Comparison
- Basic Inventory status
- Account Management
- Access Control cơ bản

### Out of Scope

- Sales / payment / accounting
- Advanced inventory
- AI product suggestion
- Customer portal / external users
- Mobile app riêng
- Production deployment hardening
- CI/CD
- Performance/load testing sâu

## 3. UAT Environment

- URL: http:/160.250.187.247:8069
- Database: product_management_uat
- Branch/build: uat/
- Module version: 1.0.0
- Deploy date: 22-08-2026

Note:

- Đây là môi trường UAT/staging tạm thời.
- Dữ liệu có thể được reset nếu cần.
- Không dùng cho production thật.

## 4. UAT Accounts

| Role | Login | Password | Purpose |
|---|---|---|---|
| System Admin | | | Setup, support kỹ thuật, xử lý lỗi cấu hình. |
| Product Admin | | | Test luồng quản trị category, product, account. |
| Product Viewer | | | Test luồng xem, tìm kiếm, so sánh sản phẩm. |

## 5. UAT Data

Chuẩn bị dữ liệu đủ cho:

- Categories: Laptop, Smartphone, Accessory
- Brands: Dell, Apple, Samsung, Logitech
- Category fields/options: CPU, RAM, Storage, Screen Size, Warranty, Color...
- Products:
  - Available product
  - Draft product
  - Discontinued product
  - Low stock product
  - Out of stock product
  - Product thiếu required specification
  - 2-4 products cùng category để compare

## 6. Feature Checklist

| Status | Area | Checklist |
|---|---|---|
| Not Run | Dashboard | User xem được số liệu tổng quan và danh sách product cần chú ý. |
| Not Run | Category Management | Admin tạo/sửa/archive/xóa category và cấu hình fields/options. |
| Not Run | Product Management | Admin tạo/sửa/archive/xóa product, nhập thông tin chung và specifications. |
| Not Run | Product Detail | User xem được thông tin tư vấn sản phẩm rõ ràng. |
| Not Run | Product Discovery | User search/filter/group sản phẩm theo các tiêu chí chính. |
| Not Run | Product Comparison | User so sánh 2-4 sản phẩm cùng category. |
| Not Run | Basic Inventory | User thấy đúng stock status theo quantity. |
| Not Run | Account Management | Admin tạo/sửa/khóa/mở khóa/reset password account Viewer. |
| Not Run | Access Control | Viewer không thấy/không thao tác được chức năng admin. |

## 7. Issue Reporting

Khi gặp lỗi, ghi theo format:

```text
Feature:
Account used:
Steps:
Expected:
Actual:
Screenshot:
Severity:
Notes: