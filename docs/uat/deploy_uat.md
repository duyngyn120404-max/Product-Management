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
### 1. SSH vào VPS

```bash
ssh <user>@<vps-ip>
```

### 2. Clone source code / chuyển vào branch UAT

```bash
git clone <repo-url>
cd Product-Management
git checkout <uat-branch>
```

Nếu source đã có sẵn:

```bash
cd Product-Management
git fetch
git checkout <uat-branch>
git pull
```

### 3. Chuẩn bị file cấu hình

Nếu project dùng `.env`:

```bash
cp .env.example .env
nano .env
```

Nếu chưa rõ cấu hình đang nằm ở đâu:

```bash
rg -n "admin_passwd|POSTGRES|ODOO|env_file|\\$\\{" compose.yaml compose.dev.yaml .
```

### 4. Start services

```bash
docker compose -f compose.yaml -f compose.dev.yaml up -d
```

Kiểm tra container:

```bash
docker compose -f compose.yaml -f compose.dev.yaml ps
```

Xem log Odoo:

```bash
docker compose -f compose.yaml -f compose.dev.yaml logs -f odoo
```

### 5. Tạo DB UAT

Mở trên browser:

```text
http://<vps-ip>:8069/web/database/manager
```

Điền:

```text
Database Name: product_management_uat
Demo Data: bỏ tick
```

### 6. Install hoặc update module `product_management`

Nếu DB mới chưa cài module:

```bash
docker compose -f compose.yaml -f compose.dev.yaml run --rm odoo \
  -d product_management_uat \
  -i product_management \
  --stop-after-init \
  --no-http
```

Nếu DB đã cài module rồi:

```bash
docker compose -f compose.yaml -f compose.dev.yaml run --rm odoo \
  -d product_management_uat \
  -u product_management \
  --stop-after-init \
  --no-http
```

### 7. Restart Odoo

```bash
docker compose -f compose.yaml -f compose.dev.yaml restart odoo
```

### 8. Tạo UAT accounts

Vào Odoo UI:

```text
Product Management > Accounts
```

Tạo:

- Product Admin
- Product Viewer

### 9. Backup DB trước khi gửi user test

```bash
docker compose -f compose.yaml -f compose.dev.yaml exec db \
  pg_dump -U odoo product_management_uat > product_management_uat_before_uat.sql
```

Nếu PostgreSQL user không phải `odoo`, kiểm tra trong compose/config rồi thay lại:

```bash
rg -n "POSTGRES_USER|POSTGRES_PASSWORD" compose.yaml compose.dev.yaml .
```

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
