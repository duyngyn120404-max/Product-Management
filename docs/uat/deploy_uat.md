# Deploy UAT lên VPS 
| Thuộc tính | Giá trị |
|---|---|
| Dự án | Product Management PV |
| Ứng dụng | Quản lý sản phẩm nội bộ |
| Nguồn đầu vào |  |
| Phiên bản tài liệu | Draft 1 |
| Ngày lập | 2026-08-22 |

Tài liệu này hướng dẫn cách chuẩn bị môi trường UAT để user/customer có thể truy cập trực tiếp, test, và gửi feed back trước khi go-live

## 1. Prequisites
- VPS Ubuntu có IP Public hoặc domain tạm
- Docker và Docker Compose
- Source code đúng branch cho UAT (uat*)
- File cấu hình môi trường: .env, docker compose, Odoo config
- Db riêng cho UAT: product_management_uat
- UAT data và UAT account
- Backup DB trước khi bắt đầu UAT

## 2. Port/URL
Tối thiểu cần: 
- 22: SSH
- 8069: Odoo

Khuyến nghị:
- Dùng Nginx Reverse Proxy
- Mở 80/443
- Không export trực tiếp 8069

URL UAT nên là: http://<vps-ip>:8069 hoặc https://uat.example.com

## 3. Các bước deploy
1. SSH vào VPS
2. Clone Source code / chuyển vào branch uat/
3. Chuẩn bị file cấu hình (.env)
4. Start services
5. Install hoặc update module
6. Restart Odoo
7. Tạo UAT accounts
8. Backup DB trước khi gửi user test

## 4. UAT Data:
Cần có dữ liệu mẫu để test các luồng chính
#### Các nhóm dữ liệu
- Categories:
  - Laptop
  - Smartphone
  - Accessory

- Brands:
  - Dell
  - Apple
  - Samsung
  - Logitech

- Category fields/options:
  - CPU
  - RAM
  - Storage
  - Screen Size
  - Warranty
  - Color
  - Purpose
  - Connection Type

- Products:
  - Product Available
  - Product Draft
  - Product Discontinued
  - Product Low Stock
  - Product Out Of Stock
  - Product thiếu required specification
  - 2-4 products cùng category để test comparison

- Accounts:
  - System Admin
  - Product Admin
  - Product Viewer

Khuyến nghị dùng seed XML cho module
