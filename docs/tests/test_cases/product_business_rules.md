# Manual Test Cases — Product Business Rules

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Product Management PV |
| Ứng dụng | Quản lý sản phẩm nội bộ |
| Nguồn đầu vào | `docs/business_rules.md` |
| Phiên bản tài liệu | Draft 1 |
| Ngày lập | 2026-08-19 |

## 1. Mục Đích

Tài liệu này mô tả các test case thủ công để kiểm tra business rules của
Product trước khi nghiệm thu Product Discovery và Product Comparison.

## 2. Tiền Điều Kiện Chung

- Module `product_management` đã được cài đặt hoặc cập nhật thành công.
- Người test đăng nhập bằng tài khoản Product Management Admin.
- Có ít nhất một category dùng để tạo product test.
- Nếu test dynamic fields, category test cần có field được đánh dấu `required`.

## 3. Test Data Gợi Ý

| Dữ liệu | Giá trị gợi ý |
|---|---|
| Category | Laptop |
| Brand | Apple |
| Product | MacBook Air M3 Test |
| Required text field | CPU |
| Required selection field | Warranty |
| Low stock threshold MVP | 5 |

## 4. Active and Product Status

### BR-STATUS-TC-01. Không cho archive available product

Preconditions:
- Có product đang có `active = True`.
- Product có `product_status = available`.

Steps:
1. Mở product.
2. Archive product hoặc đặt `active = False`.
3. Lưu product.

Expected Result:
- Hệ thống không cho lưu.
- Product không được ở trạng thái `active = False` và `product_status = available`.

### BR-STATUS-TC-02. Discontinued product vẫn có thể active

Preconditions:
- Có product đang có `active = True`.

Steps:
1. Mở product.
2. Đặt `product_status = discontinued`.
3. Giữ `active = True`.
4. Lưu product.

Expected Result:
- Product được lưu thành công.
- Product vẫn là active record.
- Product hiển thị trạng thái nghiệp vụ `discontinued`.

### BR-STATUS-TC-03. Product draft dùng để nhập liệu

Preconditions:
- Có category hợp lệ để tạo product.

Steps:
1. Tạo product mới.
2. Đặt `product_status = draft`.
3. Chưa nhập đủ thông tin tư vấn.
4. Lưu product.

Expected Result:
- Product được lưu thành công.
- Product vẫn ở trạng thái `draft`.

## 5. Price Rules

### BR-PRICE-TC-01. Không cho giá bán âm khi tạo product

Preconditions:
- Có category hợp lệ để tạo product.

Steps:
1. Tạo product mới.
2. Nhập `list_price = -1`.
3. Lưu product.

Expected Result:
- Hệ thống không cho lưu.
- Hệ thống hiển thị lỗi giá bán không được âm.

### BR-PRICE-TC-02. Không cho giá bán âm khi cập nhật product

Preconditions:
- Có product đã tồn tại.

Steps:
1. Mở product.
2. Đổi `list_price = -100`.
3. Lưu product.

Expected Result:
- Hệ thống không cho lưu.
- Giá bán không bị cập nhật thành số âm.

### BR-PRICE-TC-03. Cho phép giá bán bằng 0

Preconditions:
- Có product đang ở `product_status = draft`.

Steps:
1. Mở product.
2. Đặt `list_price = 0`.
3. Lưu product.

Expected Result:
- Product được lưu thành công.
- `list_price = 0` được chấp nhận theo rule MVP.

### BR-PRICE-TC-04. Cho phép giá bán dương

Preconditions:
- Có product đã tồn tại.

Steps:
1. Mở product.
2. Đặt `list_price = 100000`.
3. Lưu product.

Expected Result:
- Product được lưu thành công.
- `list_price` được cập nhật đúng.

## 6. Stock Rules

### BR-STOCK-TC-01. Không cho số lượng tồn âm khi tạo product

Preconditions:
- Có category hợp lệ để tạo product.

Steps:
1. Tạo product mới.
2. Nhập `qty_available = -1`.
3. Lưu product.

Expected Result:
- Hệ thống không cho lưu.
- Hệ thống hiển thị lỗi số lượng tồn không được âm.

### BR-STOCK-TC-02. Không cho số lượng tồn âm khi cập nhật product

Preconditions:
- Có product đã tồn tại.

Steps:
1. Mở product.
2. Đổi `qty_available = -10`.
3. Lưu product.

Expected Result:
- Hệ thống không cho lưu.
- Số lượng tồn không bị cập nhật thành số âm.

### BR-STOCK-TC-03. Tự tính out_of_stock

Preconditions:
- Có product đã tồn tại.

Steps:
1. Mở product.
2. Đặt `qty_available = 0`.
3. Lưu product.

Expected Result:
- Product được lưu thành công.
- `stock_status = out_of_stock`.

### BR-STOCK-TC-04. Tự tính low_stock

Preconditions:
- Low stock threshold MVP là `5`.
- Có product đã tồn tại.

Steps:
1. Mở product.
2. Đặt `qty_available = 1`.
3. Lưu product.
4. Đổi `qty_available = 5`.
5. Lưu product.

Expected Result:
- Khi `qty_available = 1`, `stock_status = low_stock`.
- Khi `qty_available = 5`, `stock_status = low_stock`.

### BR-STOCK-TC-05. Tự tính in_stock

Preconditions:
- Low stock threshold MVP là `5`.
- Có product đã tồn tại.

Steps:
1. Mở product.
2. Đặt `qty_available = 6`.
3. Lưu product.

Expected Result:
- Product được lưu thành công.
- `stock_status = in_stock`.

### BR-STOCK-TC-06. Stock status không nhập tay

Preconditions:
- Có product đã tồn tại.

Steps:
1. Mở product form.
2. Kiểm tra field `stock_status`.
3. Thử chỉnh trực tiếp `stock_status` nếu UI cho phép.

Expected Result:
- `stock_status` là readonly hoặc không nhập tay được.
- Giá trị `stock_status` được xác định từ `qty_available`.

### BR-STOCK-TC-07. Product hết hàng vẫn có thể available

Preconditions:
- Có product đủ dữ liệu bắt buộc để chuyển sang `available`.

Steps:
1. Mở product.
2. Đặt `qty_available = 0`.
3. Đặt `product_status = available`.
4. Lưu product.

Expected Result:
- Product được lưu thành công.
- `stock_status = out_of_stock`.
- `product_status = available`.

## 7. Required Dynamic Fields

### BR-FIELD-TC-01. Draft được phép thiếu required dynamic field

Preconditions:
- Category `Laptop` có field `CPU` được đánh dấu `required`.

Steps:
1. Tạo product thuộc category `Laptop`.
2. Đặt `product_status = draft`.
3. Để trống field `CPU`.
4. Lưu product.

Expected Result:
- Product được lưu thành công.
- Product vẫn ở trạng thái `draft`.

### BR-FIELD-TC-02. Available bị chặn khi thiếu required dynamic field

Preconditions:
- Category `Laptop` có field `CPU` được đánh dấu `required`.
- Có product thuộc category `Laptop`.

Steps:
1. Mở product.
2. Để trống field `CPU`.
3. Đặt `product_status = available`.
4. Lưu product.

Expected Result:
- Hệ thống không cho lưu.
- Product không được chuyển sang `available`.
- Hệ thống hiển thị lỗi nêu field bắt buộc đang thiếu.

### BR-FIELD-TC-03. Available được lưu khi đủ required dynamic fields

Preconditions:
- Category `Laptop` có field `CPU` được đánh dấu `required`.
- Có product thuộc category `Laptop`.

Steps:
1. Mở product.
2. Nhập giá trị cho field `CPU`.
3. Đặt `product_status = available`.
4. Lưu product.

Expected Result:
- Product được lưu thành công.
- Product có `product_status = available`.

### BR-FIELD-TC-04. Không cho xóa required field khi product đang available

Preconditions:
- Product đang có `product_status = available`.
- Product có field `CPU` required và đã có giá trị.

Steps:
1. Mở product.
2. Xóa giá trị field `CPU`.
3. Lưu product.

Expected Result:
- Hệ thống không cho lưu.
- Product không bị lưu trong trạng thái available thiếu required field.

### BR-FIELD-TC-05. Required selection field phải chọn option

Preconditions:
- Category `Laptop` có selection field `Warranty` được đánh dấu `required`.
- Field `Warranty` có ít nhất một option active.

Steps:
1. Mở product thuộc category `Laptop`.
2. Để trống field `Warranty`.
3. Đặt `product_status = available`.
4. Lưu product.

Expected Result:
- Hệ thống không cho lưu.
- Product không được chuyển sang `available`.

### BR-FIELD-TC-06. Selection option phải thuộc đúng field

Preconditions:
- Category có hai selection field khác nhau.
- Mỗi selection field có danh sách option riêng.

Steps:
1. Mở product thuộc category đó.
2. Ở một selection field, thử chọn hoặc ghi một option thuộc field khác.
3. Lưu product.

Expected Result:
- Hệ thống không chấp nhận option không thuộc đúng field.
- Product Field Value không lưu dữ liệu selection sai field.

### BR-FIELD-TC-07. Inactive category field không xuất hiện trong form nhập liệu chính

Preconditions:
- Category `Laptop` có field `CPU`.
- Có product thuộc category `Laptop`.

Steps:
1. Mở category `Laptop`.
2. Đặt field `CPU` thành inactive.
3. Mở lại product thuộc category `Laptop`.

Expected Result:
- Field `CPU` không còn xuất hiện trong form nhập liệu chính của product.
- Dữ liệu cũ của field inactive không làm lỗi luồng mở product.

## 8. Ghi Chú

- Test case về quyền Admin/Viewer chi tiết nên đặt ở tài liệu access control
  hoặc security riêng.
- Với required numeric dynamic fields, MVP cần chốt thêm việc `0` có được xem là
  giá trị hợp lệ hay không.
