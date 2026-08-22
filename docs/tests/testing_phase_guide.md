# Implementation Plan

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Product Management PV |
| Ứng dụng | Quản lý sản phẩm nội bộ |
| Nguồn đầu vào | [Implementation Plan](../plans/implementation_plan.md) |
| Phiên bản tài liệu | Draft 1 |
| Ngày lập | 2026-08-21 |

Tài liệu này quy định cách chuẩn bị môi trường, dữ liệu, user test, format test case, cách xử lý lỗi trong Testing Phase của Product Management PV

## 1. Test Enviroment
- Development DB: `product_management_dev`
- Testing DB: `product_management_test`
- Testing dùng DB riêng
- K dùng `docker compose down -v`

## 2. Test User Accounts
Cần các user:
| User | Role | Purpose |
|---|---|---|
|`system_amin` | Odoo System Admin | Setup, khôi phục lỗi, kiểm tra quyền hệ thống |
|`pm_admin` | Product Management Admin | Test thao tác quản lý category, product, account |
|`pm_viewer`| Product Management Viewer | Test quyền chỉ xem, search, filter, compare|
|`non_pm_user`| Không thuộc module Product Management | Test user ngoài scope không truy cập được app |

## 3. Test Data Setup
Bộ data tối thiểu gồm:
- 2 categories
- 2 brands
- Dynamic fields gồm required/optional và các type chính
- Product ở nhiều trạng thái:
    - Draft
    - Available
    - Discontinued
    - In Stock
    - Low stock
    - Out of stock
    - Mising required specifications
    - Product thuộc category khác nhau

## 4. Test Case format 
```md
### Test ID. Test case name

Purpose:
- ...

Precondition (optional):
- ... 

Steps:
1. ...
2. ...

Actual:
- ...

Status:
- Not Run / Pass / Fail / Blocked / Skipped

Notes:
```

## 5. Bug Handling:
Khi test fail:
1. Ghi test case ID
2. Ghi expected result và actual result
3. Đính kèm screenshot/log
4. Ghi env/db đang test
5. Tạo task fix hoặc note trong implemenation plan
6. Rêtst sau khi fix

## 6. UI Enhance:
UI issue được xử lý trong Testing nếu:
- Gây hiểu lầm khi thao tác
- Làm chậm hoặc cản trở luồng chính
- Hiển thị sai/khó đọc
- Làm test case fail

## 6. Feature Test Document:
- `category_management.md`
- `product_management.md`
- `product_discovery.md`
- `product_business_rules.md`
- `product_comparison.md`
- `account_management.md`
- `access_control.md`