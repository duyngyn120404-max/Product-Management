# Manual Test Cases — Product Discovery

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Product Management PV |
| Ứng dụng | Quản lý sản phẩm nội bộ |
| Nguồn đầu vào | `docs/plans/implementation_plan.md` |
| Phiên bản tài liệu | Draft 1 |
| Ngày lập | 2026-08-22 |

## 1. Scope
Kiểm tra khả năng tra cứu sản phẩm trong MVP:
- Product List là màn mặc định của app
- Danh sách mặc định ưu tiên product active và available
- Search theo tên, mã, category, brand
- Filter theo product status và stock status
- Group by theo category, brand, product status, và stock status
- Viewer có thể dùng discovery flow để tra cứu sản phẩm

## 2. Test Cases

### DIS-TC-01. Product List là màn mặc định khi mở app Product Management

Status: Passed

Steps:
1. Login bằng Product Management Viewer hoặc Admin.
2. Mở app `Product Management`.

Expected Result:
- App mở vào màn `Products`.
- Product List hiển thị.
- Các cột chính hiển thị đủ để scan sản phẩm: image, internal reference, name, category, brand, price, quantity, stock status, product status.

### DIS-TC-02. Danh sách mặc định hiển thị product active và available

Status: Passed

Steps:
1. Login bằng Product Management Viewer hoặc Admin.
2. Mở `Product Management > Products`.
3. Kiểm tra filter mặc định trên search bar.
4. Quan sát danh sách product.

Expected Result:
- Danh sách mặc định ưu tiên product active.
- Filter `Product: Available` được bật mặc định nếu cấu hình hiện tại áp dụng.
- Product không active không hiển thị trong danh sách mặc định.
- Product không Available không hiển thị nếu default available filter đang bật.

### DIS-TC-03. Search product theo thông tin chính

Status: Passed

Steps:
1. Login bằng Product Management Viewer hoặc Admin.
2. Vào `Product Management > Products`.
3. Search theo tên product, ví dụ `Laptop Full`.
4. Search theo internal reference, ví dụ `TEST-LAP-FULL`.
5. Search theo category `TEST - Laptop`.
6. Search theo brand `TEST - Apple`.

Expected Result:
- Search theo tên trả về product phù hợp.
- Search theo internal reference trả về product phù hợp.
- Search theo category trả về products thuộc category đó.
- Search theo brand trả về products thuộc brand đó.
- Search không trả về product không liên quan.

### DIS-TC-04. Filter theo product status và stock status

Status: Passed

Steps:
1. Login bằng Product Management Viewer hoặc Admin.
2. Vào `Product Management > Products`.
3. Dùng filter `Product: Available`.
4. Dùng filter `Product: Discontinued` nếu có dữ liệu phù hợp.
5. Dùng filter `Stock: In Stock`.
6. Dùng filter `Stock: Low Stock`.
7. Dùng filter `Stock: Out of Stock`.

Expected Result:
- Filter product status chỉ hiển thị product có status tương ứng.
- Filter stock status chỉ hiển thị product có stock status tương ứng.
- `TEST - Laptop Low Stock` hiển thị khi filter Low Stock.
- `TEST - Laptop Out Of Stock` hiển thị khi filter Out of Stock.
- Các filter có thể bật/tắt lại để quay về danh sách mong muốn.

### DIS-TC-05. Group by các tiêu chí chính

Status: Passed

Steps:
1. Login bằng Product Management Viewer hoặc Admin.
2. Vào `Product Management > Products`.
3. Group by Category.
4. Group by Brand.
5. Group by Product Status.
6. Group by Stock Status.

Expected Result:
- Group by Category gom products theo category.
- Group by Brand gom products theo brand.
- Group by Product Status gom products theo Draft/Available/Discontinued.
- Group by Stock Status gom products theo In Stock/Low Stock/Out of Stock.
- Người dùng có thể mở/thu group để scan danh sách.

## 4. Open Questions

| ID | Open Questions | Impact | Decision |
|---|---|---|---|
