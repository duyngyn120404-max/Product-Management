# Product Management PV

Ứng dụng quản lý sản phẩm nội bộ được xây dựng trên Odoo Community. Hệ thống
cung cấp một nơi tập trung để lưu trữ, cập nhật và tìm kiếm thông tin sản phẩm,
hỗ trợ tư vấn khách hàng và theo dõi cơ bản giá bán, số lượng tồn kho.

## Trạng thái

Dự án đang ở giai đoạn khởi tạo. SET-01 thiết lập repository và quy ước làm
việc; môi trường Odoo/PostgreSQL sẽ được bổ sung trong SET-02 đến SET-04.

## Công nghệ

- Odoo Community 19.0.
- PostgreSQL 15.
- Docker Engine hoặc Docker Desktop.
- Docker Compose v2.

Development dùng version tag `odoo:19.0` và `postgres:15`. Khi nghiệm thu
hoặc triển khai production, image sẽ được khóa thêm bằng digest.

## Yêu cầu máy phát triển

- Git.
- Docker Engine hoặc Docker Desktop đang hoạt động.
- Docker Compose v2, kiểm tra bằng `docker compose version`.
- Port mặc định `8069` chưa được ứng dụng khác sử dụng.

Không cần cài trực tiếp Odoo, Python hoặc PostgreSQL trên máy phát triển.

Các phiên bản đã kiểm tra trong SET-02:

```text
Docker Engine:  29.1.3
Docker Compose: 2.40.3
Odoo:           19.0-20260723
```

Image development hiện tại:

```text
Tag:    odoo:19.0
Digest: sha256:e415f9924395e7521245813135112f264b9222bcde3b1d3c2ee9ff073081540a
```

## Odoo development

Tải image chính thức và xác nhận phiên bản:

```bash
docker pull odoo:19.0
docker run --rm odoo:19.0 odoo --version
```

Cấu hình development nằm tại `config/odoo.conf`. Khi container được tích hợp
ở SET-04:

- `config/` được mount vào `/etc/odoo`.
- `addons/` được mount vào `/mnt/extra-addons`.
- Dữ liệu Odoo nằm tại `/var/lib/odoo` và được giữ bằng named volume.

`odoo.conf` không chứa database password hoặc master password. Các giá trị bí
mật được cung cấp từ `.env` khi Docker Compose được tạo ở SET-04.

## Bắt đầu

```bash
git clone <repository-url>
cd product-management-pv
cp .env.example .env
```

Mở `.env` và thay các giá trị có tiền tố `replace_with_`. Không commit `.env`.

Các file Compose được tạo trong SET-04. Sau khi SET-04 hoàn thành, chạy
development bằng:

```bash
docker compose -f compose.yaml -f compose.dev.yaml up -d
```

Các lệnh vận hành:

```bash
docker compose ps
docker compose logs -f odoo
docker compose stop
docker compose down
```

Không dùng `docker compose down -v` cho development hoặc production vì tùy
chọn `-v` xóa volume dữ liệu.

## URL truy cập

```text
Development: http://localhost:8069
Trong mạng:  http://<server-ip>:<ODOO_PORT>
```

Production sẽ sử dụng tên miền và HTTPS sau khi Epic 9 được thực hiện.

## Cấu trúc repository

```text
product-management-pv/
├── .github/workflows/       GitHub Actions
├── addons/                  Custom Odoo addons
│   └── product_management/  Module nghiệp vụ chính, tạo ở SET-05
├── config/                  Cấu hình Odoo
├── docs/                    Tài liệu dự án
├── plans/                   Kế hoạch chi tiết theo Epic
├── scripts/                 Quy trình kỹ thuật chạy lặp lại
├── .env.example             Mẫu biến môi trường
├── .gitignore
├── compose.yaml             Cấu hình chung, tạo ở SET-04
├── compose.ci.yaml          Cấu hình CI, tạo ở SET-07
├── compose.dev.yaml         Cấu hình development, tạo ở SET-04
└── compose.prod.yaml        Cấu hình production, tạo ở SET-04
```

`scripts/` chỉ chứa thao tác có nhiều bước hoặc cần thực hiện nhất quán, ví dụ
CI, cập nhật module, backup và restore. Không tạo script chỉ để thay thế một
lệnh Compose đơn giản.

## Database

| Môi trường | Database |
|---|---|
| Development | `product_management_dev` |
| Automated test | `product_management_test` |
| Demo/UAT | `product_management_uat` |
| Production | `product_management_prod` |

## Module Odoo

Tên kỹ thuật của module là `product_management`. Sau SET-05, có thể cài từ
giao diện Apps. Lệnh cập nhật dự kiến:

```bash
docker compose exec odoo odoo \
  -d product_management_dev \
  -u product_management \
  --stop-after-init
```

Lệnh sẽ được xác nhận khi cấu hình Odoo thực tế hoàn thành.

## Quy trình Git

Branch `main` phải luôn ở trạng thái có thể triển khai. Các loại branch:

```text
feature/<task-id>-<short-name>
fix/<task-id>-<short-name>
docs/<short-name>
```

Ví dụ:

```text
feature/SET-02-odoo-environment
fix/SEA-01-product-search
docs/setup-guide
```

Commit gắn với backlog phải bắt đầu bằng mã task:

```text
SET-01: initialize repository structure
PRO-01: add product model
```

Quy trình pull request:

1. Tạo branch từ phiên bản mới nhất của `main`.
2. Mỗi branch xử lý một task hoặc thay đổi có phạm vi rõ ràng.
3. Push branch và mở pull request vào `main`.
4. Mô tả mục đích, thay đổi chính và cách kiểm tra.
5. Ít nhất một thành viên khác review.
6. Chỉ merge khi tiêu chí hoàn thành và CI đều đạt.
7. Ưu tiên squash merge.

Git tag phát hành sử dụng Semantic Versioning, ví dụ `v0.1.0`, `v1.0.0-rc.1`
và `v1.0.0`. Không dùng tag `dev` hoặc `prod` có thể bị di chuyển làm định danh
duy nhất.

## Xử lý lỗi thiết lập

### Container không chạy

```bash
docker compose ps
docker compose logs odoo
docker compose logs db
```

### Port 8069 đã được sử dụng

Đổi `ODOO_PORT` trong `.env`, ví dụ thành `8070`, rồi tạo lại container.

### Odoo không kết nối PostgreSQL

- Kiểm tra service `db` đang chạy.
- Kiểm tra user và password giữa Odoo và PostgreSQL khớp nhau.
- Database host phải là tên service `db`, không phải `localhost`.
- Kiểm tra PostgreSQL đã hoàn tất khởi tạo.

### Không thấy module

- Kiểm tra module nằm tại `addons/product_management`.
- Kiểm tra `addons/` được mount tới `/mnt/extra-addons`.
- Kiểm tra `addons_path`, manifest và các file `__init__.py`.
- Cập nhật Apps List và xem log Odoo.

### Thay mật khẩu PostgreSQL nhưng không có tác dụng

Biến khởi tạo của image PostgreSQL chỉ có tác dụng khi data directory còn
trống. Không xóa volume tùy tiện; hãy đổi mật khẩu trong PostgreSQL hoặc tạo
lại môi trường development có kiểm soát.

### Dữ liệu mất sau khi tạo lại container

Kiểm tra persistent volume cho cả PostgreSQL database và Odoo filestore.

## Kế hoạch

Xem [mục lục kế hoạch](plans/README.md) và
[Epic 1 — Khởi tạo dự án](plans/epic-1.md).
