# EPIC 1 — Khởi tạo dự án

## 1. Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Mục tiêu | Xây dựng nền tảng kỹ thuật thống nhất để nhóm có thể phát triển, kiểm thử và vận hành ứng dụng quản lý sản phẩm |
| Nền tảng | Odoo Community 19.0 |
| Cơ sở dữ liệu | PostgreSQL 15 |
| Mô hình repository | Monorepo |
| Công cụ chạy ứng dụng | Docker và Docker Compose v2 |
| Số công việc | 7 |
| Tổng ước tính | 18 giờ |
| Phạm vi MVP | SET-01 đến SET-05, ước tính 13 giờ |
| Trạng thái | Đang thực hiện |

## 2. Bối cảnh

Nhóm nội bộ hiện thiếu một nơi tập trung để lưu trữ, cập nhật và tìm kiếm
thông tin sản phẩm. Hệ thống được xây dựng nhằm hỗ trợ:

- Quản lý thông tin sản phẩm tập trung.
- Tra cứu thông tin phục vụ tư vấn khách hàng.
- Theo dõi cơ bản giá bán và số lượng tồn kho.
- Phân quyền người quản trị và người chỉ xem dữ liệu.

Epic này chưa triển khai đầy đủ các chức năng nghiệp vụ trên. Mục tiêu của Epic
là tạo môi trường và bộ khung kỹ thuật để các Epic sau có thể phát triển ổn
định.

## 3. Phạm vi

### Trong phạm vi

- Khởi tạo và chuẩn hóa monorepo.
- Chuẩn bị môi trường Odoo Community 19.0.
- Cấu hình PostgreSQL 15.
- Chuẩn hóa cách chạy hệ thống bằng Docker Compose.
- Tạo bộ khung module `product_management`.
- Chuẩn bị dữ liệu mẫu ban đầu phục vụ phát triển và demo.
- Thiết lập CI cơ bản để tự động kiểm tra pull request.

### Ngoài phạm vi

- Hoàn thiện model và giao diện quản lý danh mục.
- Hoàn thiện model và giao diện quản lý sản phẩm.
- Phân quyền nghiệp vụ đầy đủ.
- Tìm kiếm, bộ lọc, dashboard và báo cáo.
- Cấu hình Nginx, HTTPS, VPS và quy trình production hoàn chỉnh.

Các nội dung trên được thực hiện trong những Epic tương ứng.

## 4. Quyết định kỹ thuật

### 4.1. Phiên bản

- Odoo Community: `19.0`.
- PostgreSQL: `15`.
- Docker Compose: Compose v2, sử dụng lệnh `docker compose`.

Trong giai đoạn development, các image được khai báo bằng version tag cụ thể
như `odoo:19.0` và `postgres:15` để cấu hình đơn giản, dễ sử dụng. Không sử
dụng tag `latest`.

Khi hệ thống bước vào nghiệm thu hoặc triển khai production, image phải được
khóa thêm bằng digest để bảo đảm môi trường chạy đúng bản build đã kiểm thử.
Việc cập nhật digest phải được thực hiện chủ động, kiểm thử trước rồi mới triển
khai.

### 4.2. Mô hình repository

Dự án sử dụng monorepo để lưu mã nguồn module Odoo, cấu hình hạ tầng, kế
hoạch và tài liệu trong cùng một nơi.

Cấu trúc mục tiêu:

```text
product-management-pv/
├── .github/
│   └── workflows/
│       └── ci.yaml
├── addons/
│   └── product_management/
├── config/
│   └── odoo.conf
├── docs/
├── plans/
│   ├── README.md
│   ├── epic-1.md
│   ├── epic-2.md
│   ├── epic-3.md
│   ├── epic-4.md
│   ├── epic-5.md
│   ├── epic-6.md
│   ├── epic-7.md
│   ├── epic-8.md
│   └── epic-9.md
├── scripts/
│   └── ci.sh
├── .env.example
├── .gitignore
├── compose.yaml
├── compose.ci.yaml
├── compose.dev.yaml
├── compose.prod.yaml
└── README.md
```

Thư mục `scripts/` dành cho các thao tác kỹ thuật có nhiều bước hoặc cần thực
hiện lặp lại, ví dụ:

- Sao lưu và phục hồi PostgreSQL.
- Cập nhật module Odoo.
- Chạy kiểm tra tự động.
- Tạo dữ liệu demo khi cơ chế demo data tiêu chuẩn của Odoo không đáp ứng.

Không tạo script chỉ để thay thế một lệnh Docker Compose đơn giản.

### 4.3. Môi trường development và production

Hai môi trường được tách bằng cấu hình Docker Compose, không tách bằng một
Git branch `develop` ở giai đoạn hiện tại:

- `compose.yaml`: cấu hình chung.
- `compose.dev.yaml`: cấu hình dành cho phát triển.
- `compose.prod.yaml`: cấu hình dành cho chạy thực tế.

Môi trường development có thể mount trực tiếp mã nguồn addon, bật log chi tiết
và sử dụng demo data. Môi trường production không được nạp demo data, phải sử
dụng secret riêng và image đã được khóa bằng version tag kết hợp với digest.

Git tag phát hành sử dụng Semantic Versioning, ví dụ `v0.1.0`, `v1.0.0`.
Không sử dụng một tag `prod` có thể bị ghi đè làm định danh duy nhất cho bản
phát hành.

### 4.4. Quy trình branch và pull request

Các loại branch:

```text
main
feature/<task-id>-<short-name>
fix/<task-id>-<short-name>
docs/<short-name>
```

Ví dụ:

```text
feature/SET-02-odoo-environment
feature/PRO-01-product-model
fix/SEA-01-product-search
docs/epic-1-plan
```

Quy trình làm việc:

1. Cập nhật `main` và tạo branch mới từ `main`.
2. Mỗi branch chỉ xử lý một task hoặc một thay đổi có phạm vi rõ ràng.
3. Commit phải chứa mã task khi thay đổi gắn với backlog.
4. Push branch và tạo pull request vào `main`.
5. Pull request phải mô tả mục đích, thay đổi chính và cách kiểm tra.
6. Ít nhất một thành viên khác review.
7. Chỉ merge khi đạt tiêu chí hoàn thành và các kiểm tra liên quan đã đạt.
8. Ưu tiên squash merge để lịch sử `main` gọn.

Ví dụ commit:

```text
SET-01: initialize repository structure
PRO-01: add product model
SEA-01: fix case-insensitive product search
```

### 4.5. Quy ước tên database nghiệp vụ

Tên database phải sử dụng chữ thường, dấu gạch dưới, không có khoảng trắng
hoặc dấu tiếng Việt và phải thể hiện rõ môi trường:

| Môi trường | Tên database |
|---|---|
| Development | `product_management_dev` |
| Automated test | `product_management_test` |
| Demo/UAT | `product_management_uat` |
| Production | `product_management_prod` |

Trong Epic 1, database nghiệp vụ được triển khai trước là
`product_management_dev`. Các database còn lại chỉ được tạo khi có môi trường
tương ứng.

Phân biệt:

- `POSTGRES_DB=postgres` là database mặc định được PostgreSQL container tạo
  khi khởi động lần đầu.
- `ODOO_DATABASE` là database nghiệp vụ mà Odoo sử dụng trong từng môi trường.

Production phải giới hạn Odoo vào đúng database nghiệp vụ và không công khai
danh sách database:

```ini
db_name = product_management_prod
dbfilter = ^product_management_prod$
list_db = False
```

## 5. Luồng phụ thuộc

```text
SET-01
├── SET-02 ─┐
└── SET-03 ─┴── SET-04 ── SET-05 ─┬─ SET-06
                                  └─ SET-07
```

- SET-02 và SET-03 có thể thực hiện song song sau SET-01.
- SET-04 cần kết quả của SET-02 và SET-03.
- SET-05 cần môi trường Docker Compose hoạt động.
- SET-06 chỉ thực hiện sau khi module đã cài đặt thành công.
- SET-07 cần cấu hình Docker Compose và bộ khung module để kiểm tra việc cài
  đặt module trên CI.

## 6. Danh sách công việc

| ID | Công việc | Ưu tiên | Ước tính | Trạng thái |
|---|---|---:|---:|---|
| SET-01 | Khởi tạo repository Git | Must | 1 giờ | Hoàn thành |
| SET-02 | Tạo môi trường Odoo Community | Must | 3 giờ | Hoàn thành |
| SET-03 | Cấu hình PostgreSQL | Must | 2 giờ | Hoàn thành |
| SET-04 | Tạo Docker Compose | Must | 4 giờ | Hoàn thành |
| SET-05 | Tạo module quản lý sản phẩm | Must | 3 giờ | Chưa thực hiện |
| SET-06 | Tạo dữ liệu mẫu ban đầu | Should | 2 giờ | Chưa thực hiện |
| SET-07 | Thiết lập CI cơ bản | Should | 3 giờ | Chưa thực hiện |

## 7. Chi tiết công việc

### SET-01 — Khởi tạo repository Git

**Trạng thái:** Hoàn thành.

**Mục tiêu**

Tạo một repository thống nhất để nhóm quản lý mã nguồn, tài liệu, kế hoạch và
quy trình cộng tác.

**Công việc**

- Khởi tạo Git repository với branch mặc định là `main`.
- Tạo cấu trúc thư mục ban đầu của monorepo.
- Tạo `.gitignore` phù hợp với Python, Odoo, PostgreSQL, Docker, IDE và hệ điều
  hành.
- Tạo `.env.example` không chứa thông tin bí mật thật.
- Tạo README ban đầu.
- Tạo thư mục `plans/` và mục lục kế hoạch.
- Ghi lại quy ước branch, commit và pull request.

**README ban đầu phải mô tả**

- Vấn đề sản phẩm cần giải quyết.
- Phiên bản Odoo và PostgreSQL.
- Yêu cầu cài đặt trên máy phát triển.
- Cách tạo `.env` từ `.env.example`.
- Cách khởi động, dừng và xem log hệ thống.
- URL truy cập.
- Cách cài đặt và cập nhật module.
- Cấu trúc thư mục.
- Quy trình branch và pull request.
- Các lỗi thiết lập thường gặp.

**Không được commit**

- File `.env`.
- Mật khẩu hoặc secret thật.
- PostgreSQL data directory.
- Odoo filestore và session.
- File log, cache Python và cấu hình IDE cá nhân.

**Tiêu chí hoàn thành**

- Repository có cấu trúc dự án, `.gitignore`, `.env.example`, README và thư
  mục kế hoạch.
- Quy ước branch, commit và pull request đã được ghi lại.
- Không có secret hoặc dữ liệu runtime trong Git.
- Một thành viên mới có thể clone repository, hiểu cấu trúc và biết bước tiếp
  theo để bắt đầu phát triển mà không cần nhận thông tin riêng.

### SET-02 — Tạo môi trường Odoo Community

**Trạng thái:** Hoàn thành.

**Mục tiêu**

Chuẩn bị Odoo Community 19.0 làm nền tảng chạy ứng dụng.

**Công việc**

- Sử dụng Docker image chính thức `odoo:19.0`.
- Chuẩn bị `config/odoo.conf`.
- Khai báo đường dẫn custom addons là `/mnt/extra-addons`.
- Cấu hình thư mục dữ liệu Odoo có persistent volume.
- Thiết lập log phù hợp với môi trường development.
- Xác nhận phiên bản Odoo đang chạy.

**Phiên bản đã xác nhận**

```text
Docker Engine:  29.1.3
Docker Compose: 2.40.3
Odoo Server:    19.0-20260723
Image digest:   sha256:e415f9924395e7521245813135112f264b9222bcde3b1d3c2ee9ff073081540a
```

**Tiêu chí hoàn thành**

- Docker image chính thức `odoo:19.0` được tải thành công.
- Lệnh `odoo --version` xác nhận Odoo Server 19.0.
- `config/odoo.conf` hợp lệ và không chứa secret.
- Custom addons được mount tại `/mnt/extra-addons`; việc Odoo nhận diện module
  trong đường dẫn này được xác nhận ở SET-05 sau khi module được tạo.
- Thư mục dữ liệu Odoo được xác định là `/var/lib/odoo`.

Việc truy cập giao diện, kết nối PostgreSQL và kiểm tra persistent volume được
xác nhận trong SET-04 sau khi hai service được tích hợp bằng Docker Compose.

### SET-03 — Cấu hình PostgreSQL

**Trạng thái:** Hoàn thành.

**Mục tiêu**

Cung cấp cơ sở dữ liệu ổn định và lưu bền cho Odoo.

**Công việc**

- Sử dụng Docker image `postgres:15`.
- Khai báo `POSTGRES_DB`, `POSTGRES_USER` và `POSTGRES_PASSWORD` qua biến môi
  trường.
- Không sử dụng role `postgres` làm tài khoản kết nối của Odoo.
- Cấu hình persistent volume cho PostgreSQL.
- Kiểm tra kết nối từ Odoo đến service database.
- Không công khai port PostgreSQL ra máy host nếu chưa có nhu cầu.

**Phiên bản đã xác nhận**

```text
PostgreSQL Server: 15.18 (Debian 15.18-1.pgdg13+1)
Image tag:         postgres:15
Image digest:      sha256:74e110c41804365e3915fcc09d5e7a1eff50161aaa94d5da0e58e0cd75ae509c
Role kết nối:      odoo
```

**Kết quả kiểm tra**

- PostgreSQL khởi động và `pg_isready` xác nhận sẵn sàng.
- Service không publish port `5432` ra host.
- Odoo 19 kết nối qua Docker network và tạo
  `product_management_test` thành công.
- Một marker được ghi vào database, container PostgreSQL được xóa và tạo lại
  với cùng named volume; marker vẫn đọc lại được.
- Container, network và volume kiểm thử tạm đã được xóa sau khi kiểm tra.
- Hai volume HCDC không bị thay đổi.

**Tiêu chí hoàn thành**

- PostgreSQL khởi động thành công.
- Odoo kết nối và tạo database thành công.
- Dữ liệu vẫn còn sau khi restart hoặc tạo lại container.
- Thông tin đăng nhập thật không xuất hiện trong repository.

### SET-04 — Tạo Docker Compose

**Trạng thái:** Hoàn thành.

**Mục tiêu**

Chuẩn hóa cách khởi động Odoo và PostgreSQL bằng một lệnh.

**Công việc**

- Tạo service `odoo`.
- Tạo service `db`.
- Khai báo network nội bộ, environment variables và persistent volumes.
- Mount `addons/` và `config/` đúng đường dẫn trong container.
- Tạo cấu hình chung, development và production.
- Bổ sung health check hoặc cơ chế chờ PostgreSQL sẵn sàng nếu cần.
- Ghi lệnh vận hành trong README.

**Kết quả triển khai**

- `compose.yaml` định nghĩa service `odoo`, service `db`, network và hai named
  volumes.
- `compose.dev.yaml` publish port Odoo và mount source addon cho development.
- `compose.prod.yaml` thiết lập restart policy, loopback port và cấu hình Odoo
  production làm nền cho Epic 9.
- PostgreSQL healthcheck chặn Odoo khởi động trước khi database sẵn sàng.
- PostgreSQL không publish port `5432` ra host.
- `scripts/odoo-entrypoint.sh` tạo cấu hình runtime chứa master password từ
  biến môi trường; secret không được ghi vào Git.

**Kết quả kiểm tra**

- `docker compose config` hợp lệ cho development và production.
- PostgreSQL đạt trạng thái healthy.
- Odoo 19 kết nối PostgreSQL 15 thành công.
- Giao diện Odoo trả HTTP 200 tại port `8069`.
- Odoo tạo thành công database `product_management_dev`.
- Database marker và Odoo data marker vẫn tồn tại sau khi `docker compose
  down` và `docker compose up -d` tạo lại container.
- Stack và volume chứa mật khẩu kiểm thử đã được xóa sau nghiệm thu.
- Hai container HCDC vẫn dừng và hai volume HCDC không bị thay đổi.

**Các lệnh chuẩn**

Khởi động development:

```bash
docker compose -f compose.yaml -f compose.dev.yaml up -d
```

Xem trạng thái:

```bash
docker compose ps
```

Xem log:

```bash
docker compose logs -f odoo
```

Dừng container nhưng giữ nguyên trạng thái:

```bash
docker compose stop
```

Dừng và xóa container/network nhưng giữ named volume:

```bash
docker compose down
```

Không sử dụng `docker compose down -v` trong quy trình thông thường vì tùy
chọn `-v` xóa volume dữ liệu.

**URL development**

```text
http://localhost:<ODOO_PORT>
http://<IP-máy-chạy-Odoo>:<ODOO_PORT>
```

Port mặc định đề xuất là `8069`.

**Tiêu chí hoàn thành**

- Thành viên có thể khởi động Odoo và PostgreSQL bằng một lệnh Compose.
- Cả hai service ở trạng thái hoạt động và Odoo kết nối được database.
- Giao diện Odoo truy cập được bằng IP máy chạy hệ thống và port đã cấu hình.
- Restart hoặc tạo lại container không làm mất database và filestore.

### SET-05 — Tạo module quản lý sản phẩm

**Mục tiêu**

Tạo bộ khung module nghiệp vụ để các Epic tiếp theo triển khai chức năng.

**Tên kỹ thuật**

```text
product_management
```

**Cấu trúc tối thiểu**

```text
addons/product_management/
├── data/
├── demo/
├── models/
│   └── __init__.py
├── security/
├── views/
├── __init__.py
└── __manifest__.py
```

**Công việc**

- Tạo manifest với tên, phiên bản, license và dependency rõ ràng.
- Tạo các file khởi tạo Python.
- Tạo cấu trúc `models`, `views`, `security`, `data` và `demo`.
- Tạo menu hoặc thành phần tối thiểu cần thiết để xác nhận module được nạp.
- Ghi hướng dẫn cài đặt và cập nhật module.

**Cập nhật module**

```bash
docker compose exec odoo odoo \
  -d <database_name> \
  -u product_management \
  --stop-after-init
```

Lệnh phải được điều chỉnh nếu cách chạy service Odoo thực tế yêu cầu tham số
khác. Sau khi cập nhật, khởi động lại service Odoo nếu cần.

**Tiêu chí hoàn thành**

- Module xuất hiện trong danh sách Apps.
- Module cài đặt và cập nhật không phát sinh lỗi.
- Odoo nạp đúng cấu trúc module từ custom addons path.
- Module chưa triển khai vượt phạm vi nghiệp vụ của các Epic sau.

### SET-06 — Tạo dữ liệu mẫu ban đầu

**Mục tiêu**

Cung cấp dữ liệu nhất quán để phát triển, kiểm thử và trình diễn hệ thống.

**Dữ liệu đề xuất**

- Tài khoản hoặc vai trò mẫu phù hợp với khả năng đã triển khai.
- Một số danh mục sản phẩm.
- Từ 10 đến 20 sản phẩm.
- Các trường hợp còn hàng, sắp hết và hết hàng.
- Giá, mô tả, công dụng, ưu điểm, nhược điểm và hình ảnh mẫu nếu model đã hỗ
  trợ.

**Cách triển khai ưu tiên**

Sử dụng cơ chế dữ liệu chuẩn của Odoo:

```text
addons/product_management/data/initial_data.xml
addons/product_management/demo/product_demo.xml
```

- `data/` chỉ chứa dữ liệu khởi tạo bắt buộc.
- `demo/` chứa dữ liệu phục vụ phát triển, kiểm thử và trình diễn.
- Demo data không được nạp vào production.
- Chỉ tạo `scripts/seed-demo.sh` nếu quy trình nạp dữ liệu có nhiều bước và cơ
  chế demo data của Odoo không đáp ứng.

**Tiêu chí hoàn thành**

- Dữ liệu mẫu được nạp thành công trong môi trường development.
- Dữ liệu phản ánh đủ các tình huống chính mà model hiện tại hỗ trợ.
- Có thể phân biệt rõ dữ liệu bắt buộc và dữ liệu demo.
- Production không tự động nạp demo data.

### SET-07 — Thiết lập CI cơ bản

**Mục tiêu**

Tự động kiểm tra mã nguồn và khả năng cài đặt module khi có pull request vào
`main`, giúp phát hiện lỗi trước khi merge.

**Nền tảng**

Sử dụng GitHub Actions. Workflow được đặt tại:

```text
.github/workflows/ci.yaml
```

**Điều kiện chạy**

- Khi tạo hoặc cập nhật pull request vào `main`.
- Khi có commit được merge hoặc push trực tiếp vào `main`.

**Công việc**

- Tạo `compose.ci.yaml` cho môi trường kiểm tra tự động.
- Tạo `scripts/ci.sh` để cùng một bộ lệnh có thể chạy trên máy phát triển và
  GitHub Actions.
- Kiểm tra cú pháp Python trong module.
- Kiểm tra cấu trúc các file XML.
- Khởi động PostgreSQL với database tạm `product_management_test`.
- Cài module `product_management` trên Odoo.
- Chạy các Odoo test hiện có với `--test-enable`.
- Dừng và xóa container, network và volume tạm sau khi kiểm tra.
- Hiển thị kết quả thành công hoặc thất bại trên pull request.

**Luồng CI**

```text
Pull request vào main
        ↓
Checkout mã nguồn
        ↓
Kiểm tra Python và XML
        ↓
Khởi động PostgreSQL
        ↓
Cài module trên Odoo và chạy test
        ↓
Trả kết quả lên pull request
```

Lệnh kiểm tra cài đặt module dự kiến:

```bash
docker compose \
  -f compose.yaml \
  -f compose.ci.yaml \
  run --rm odoo \
  odoo \
  -d product_management_test \
  -i product_management \
  --test-enable \
  --stop-after-init
```

CI được phép dùng `docker compose down -v` vì chỉ xóa volume tạm của lần kiểm
tra, không tác động đến dữ liệu development hoặc production.

**Phạm vi của Epic 1**

- Tạo đường ống CI hoạt động.
- Kiểm tra cú pháp và cấu trúc cơ bản.
- Xác nhận module cài đặt được.
- Chạy các test đã tồn tại.

Việc viết đầy đủ test nghiệp vụ, test phân quyền, tìm kiếm, bộ lọc và dữ liệu
không hợp lệ thuộc Epic 8.

**Tiêu chí hoàn thành**

- CI tự động chạy khi có pull request vào `main`.
- Lỗi Python, XML hoặc lỗi cài module làm CI thất bại.
- Module cài đặt thành công làm CI trả kết quả đạt.
- Log đủ rõ để xác định bước kiểm tra bị lỗi.
- Môi trường và dữ liệu tạm được dọn sau khi CI kết thúc.
- Thành viên có thể chạy cùng kiểm tra bằng `scripts/ci.sh` trên máy phát triển.

## 8. Cấu hình môi trường đề xuất

`.env.example` dự kiến:

```dotenv
ODOO_PORT=8069
POSTGRES_DB=postgres
POSTGRES_USER=odoo
POSTGRES_PASSWORD=replace_with_a_strong_password
ODOO_ADMIN_PASSWORD=replace_with_a_strong_master_password
ODOO_DATABASE=product_management_dev
```

Tạo file môi trường cục bộ:

```bash
cp .env.example .env
```

Sau đó thay các giá trị minh họa bằng mật khẩu thực tế. File `.env` không được
commit.

## 9. Xử lý lỗi thiết lập thường gặp

### Container không chạy

```bash
docker compose ps
docker compose logs odoo
docker compose logs db
```

Đọc lỗi đầu tiên xuất hiện trong log thay vì chỉ dựa vào trạng thái container.

### Port Odoo đã được sử dụng

Đổi `ODOO_PORT` trong `.env`, ví dụ từ `8069` sang `8070`, sau đó tạo lại
container.

### Odoo không kết nối PostgreSQL

Kiểm tra:

- Service `db` đang hoạt động.
- User và password của Odoo khớp với PostgreSQL.
- Host database là tên service `db`, không phải `localhost`.
- PostgreSQL đã khởi tạo xong trước khi Odoo kết nối.

### Không thấy module

Kiểm tra:

- Module nằm trong `addons/product_management`.
- `addons/` được mount đến `/mnt/extra-addons`.
- `addons_path` trong cấu hình Odoo chứa `/mnt/extra-addons`.
- Manifest và các file `__init__.py` hợp lệ.
- Danh sách Apps đã được cập nhật.

### Thay mật khẩu trong `.env` nhưng PostgreSQL vẫn dùng mật khẩu cũ

Các biến khởi tạo của image PostgreSQL chỉ có tác dụng khi data directory còn
trống. Không xóa volume tùy tiện. Cần đổi mật khẩu trong PostgreSQL hoặc thực
hiện quy trình tạo lại môi trường development có kiểm soát.

### Dữ liệu mất sau khi tạo lại container

Kiểm tra persistent volume cho cả:

- PostgreSQL database.
- Odoo filestore.

## 10. Rủi ro và biện pháp

| Rủi ro | Ảnh hưởng | Biện pháp |
|---|---|---|
| Dùng image `latest` | Môi trường thay đổi ngoài dự kiến | Development dùng version tag; nghiệm thu và production khóa thêm digest |
| Commit `.env` hoặc secret | Lộ thông tin truy cập | `.gitignore`, `.env.example` và review pull request |
| Không cấu hình volume | Mất database hoặc hình ảnh | Persistent volume cho PostgreSQL và Odoo |
| Development và production dùng chung cấu hình | Bật nhầm demo/debug trên production | Tách Compose override cho từng môi trường |
| Odoo chạy trước khi PostgreSQL sẵn sàng | Khởi động không ổn định | Health check hoặc cơ chế chờ database |
| Dữ liệu demo vào production | Sai lệch dữ liệu thực tế | Chỉ khai báo demo data trong manifest và quy trình development |
| README không được cập nhật | Thành viên mới dựng môi trường thất bại | Cập nhật README trong cùng pull request khi lệnh vận hành thay đổi |
| CI chỉ chạy trên GitHub nhưng không chạy được cục bộ | Khó tái hiện và sửa lỗi | Dùng chung `scripts/ci.sh` cho máy phát triển và GitHub Actions |

## 11. Definition of Done của Epic

Epic 1 hoàn thành khi:

1. Thành viên mới có thể clone repository và làm theo README.
2. Odoo 19.0 và PostgreSQL 15 khởi động bằng một lệnh Docker Compose.
3. Odoo truy cập được trên trình duyệt và kết nối database thành công.
4. Database và Odoo filestore không mất khi container được tạo lại.
5. Module `product_management` cài đặt và cập nhật không có lỗi.
6. Dữ liệu demo được nạp đúng trong development và không được nạp vào
   production.
7. Repository không chứa secret hoặc dữ liệu runtime.
8. Cấu hình development và production được tách biệt.
9. Từng SET đạt tiêu chí hoàn thành riêng và trạng thái được cập nhật trong tài
   liệu này.
10. Pull request vào `main` được CI kiểm tra tự động và module cài đặt thành
    công trên database test sạch.

## 12. Câu hỏi còn mở

Không còn câu hỏi mở trong phạm vi Epic 1. Quy tắc xác định sản phẩm “sắp
hết” được chuyển sang Epic 4 để thảo luận trước khi thực hiện PRO-10.
