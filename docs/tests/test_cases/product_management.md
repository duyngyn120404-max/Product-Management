# Manual Test Cases - Product Management
| Thuộc tính | Giá trị |
|---|---|
| Dự án | Product Management PV |
| Ứng dụng | Quản lý sản phẩm nội bộ |
| Nguồn đầu vào | `docs/plans/implementation_plan.md` |
| Phiên bản tài liệu | Draft 1 |
| Ngày lập | 2026-08-22 |

## 1. Mục Đích
Kiểm tra các luồng chính của Product Management trong MVP: 
- tạo/cập nhật product
- gắn category/brand
- nhập specifications
- kiểm tra business rules cơ bản
- archive product 
- phân quyền Viewer/Admin.

## 2. Test Cases

### PRO-TC-01. Admin tạo và cập nhật product Draft

Status: Passed

Steps:
1. Login bằng Product Management Admin.
2. Vào `Product Management > Products`.
3. Tạo product `TEST - Product Create`.
4. Chọn category `TEST - Laptop`.
5. Chọn brand `TEST - Dell`.
6. Nhập `List Price = 1000`.
7. Nhập `Quantity = 10`.
8. Giữ `Product Status = Draft`.
9. Save.
10. Mở lại product vừa tạo.
11. Cập nhật name thành `TEST - Product Updated`.
12. Đổi brand, list price và quantity.
13. Save.

Expected Result:
- Product được tạo thành công.
- Product hiển thị trong danh sách Products.
- Category, brand, price, quantity và status được lưu đúng.
- Product được cập nhật thành công.
- `Stock Status` được tự tính theo quantity.

### PRO-TC-02. Không cho lưu product thiếu thông tin bắt buộc

Status: Passed

Steps:
1. Login bằng Product Management Admin.
2. Vào `Product Management > Products`.
3. Bấm New.
4. Để trống `Name`, thử Save.
5. Nhập Name nhưng để trống `Category`, thử Save.

Expected Result:
- Hệ thống không cho lưu khi thiếu `Name`.
- Hệ thống không cho lưu khi thiếu `Category`.

### PRO-TC-03. Product tự tạo và lưu specifications theo category

Status: Passed

Steps:
1. Login bằng Product Management Admin.
2. Tạo hoặc mở product Draft thuộc `TEST - Laptop`.
3. Mở tab Specifications.
4. Kiểm tra các fields của category `TEST - Laptop`.
5. Nhập specs:
   - CPU = Apple M3
   - RAM GB = 16
   - Warranty = 24 months
   - Touch Screen = False
   - Release Date = 2026-01-01
6. Save.
7. Mở lại product.

Expected Result:
- Specifications hiển thị active fields của category `TEST - Laptop`.
- Không hiển thị fields của category khác.
- Giá trị specifications được lưu đúng sau khi mở lại product.

Actual Result:
-

### PRO-TC-04. Required specifications kiểm soát trạng thái Available

Status: Passed

Steps:
1. Mở product Draft thuộc `TEST - Laptop` đang thiếu required spec, ví dụ thiếu CPU hoặc Warranty.
2. Đổi `Product Status = Available`.
3. Save.
4. Nhập đủ required specs.
5. Save lại với `Product Status = Available`.

Expected Result:
- Khi thiếu required specs, hệ thống không cho chuyển Available.
- Lỗi hiển thị tên required specs còn thiếu.
- Khi required specs đầy đủ, product chuyển Available thành công.

### PRO-TC-05. Đổi category đồng bộ specifications

Status: Passed

Steps:
1. Mở product thuộc `TEST - Laptop`.
2. Đổi category sang `TEST - Smartphone`.
3. Save.
4. Mở tab Specifications.

Expected Result:
- Specifications được đồng bộ theo category mới.
- Laptop fields không còn là active specifications.
- Smartphone fields hiển thị đúng.


## PRO-TC-06. Archive product theo rule trạng thái

Status: Passed

Steps:
1. Mở product có `Product Status = Available`.
2. Thử archive product.
3. Đổi `Product Status = Discontinued`.
4. Save.
5. Archive product.
6. Kiểm tra danh sách Products mặc định và filter Archived.

Expected Result:
- Hệ thống không cho archive product đang Available.
- Product Discontinued archive thành công.
- Product archived không hiển thị trong danh sách active mặc định.
- Product archived hiển thị khi dùng filter Archived.

### PRO-TC-07. Viewer chỉ được xem product

Status: Passed

Steps:
1. Login bằng Product Management Viewer.
2. Vào `Product Management > Products`.
3. Mở một product.
4. Thử tạo product mới.
5. Thử sửa product.
6. Thử xóa/archive product.

Expected Result:
- Viewer xem được Products.
- Viewer mở được product để xem thông tin.
- Viewer không tạo/sửa/xóa/archive được product.

## 3. Fixed Issues During Testing
| ID | Issue | Fix | Verified By |
|---|---|---|---|
| BUG-UI-01 | Product Specifications hiển thị nhiều cột kỹ thuật theo từng kiểu dữ liệu: Text, Long Text, Integer, Decimal, Boolean, Date, Datetime, Option. | Added `display_value` and simplified the specifications list to Field / Required / Value with a type-specific edit form. | PRO-TC-03 |
