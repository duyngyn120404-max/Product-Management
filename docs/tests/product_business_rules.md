# Manual Test Cases — Product Business Rules

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Product Management PV |
| Ứng dụng | Quản lý sản phẩm nội bộ |
| Nguồn đầu vào | `docs/business_rules.md` |
| Phiên bản tài liệu | Draft 1 |
| Ngày lập | 2026-08-17 |

## 1. Mục đích

Tài liệu này mô tả các test case thủ công dùng để kiểm tra business rules của
Product trước khi triển khai hoặc nghiệm thu Product Discovery.

Các test case tập trung vào:
- Ràng buộc giữa `active` và `product_status`
- Giá bán
- Tồn kho và `stock_status`
- Required dynamic fields theo category
- Một số rule liên quan đến dữ liệu hiển thị trong Product Discovery

## 2. Tiền điều kiện chung

- Module `product_management` đã được cài đặt hoặc cập nhật.
- Người test đăng nhập bằng tài khoản Admin.
- Đã có ít nhất một category dùng để tạo product test.
- Nếu test dynamic fields, category test cần có field được đánh dấu `required`.

## 3. Test Data Gợi Ý

| Dữ liệu | Giá trị gợi ý |
|---|---|
| Category | Laptop |
| Brand | Apple |
| Product | MacBook Air M3 Test |
| Required dynamic field dạng text | CPU |
| Required dynamic field dạng selection | Warranty |
| Low stock threshold MVP | 5 |

## 4. Active and Product Status

### BR-STATUS-TC-01. Available product phải active

Preconditions:
- Có product đang ở `product_status = available`.

Steps:
1. Mở product.
2. Thử archive product hoặc đặt `active = False`.
3. Lưu product.

Expected Result:
- Hệ thống không cho lưu.
- Product không được ở trạng thái `active = False` khi `product_status = available`.
- Hệ thống hiển thị lỗi validation rõ ràng.

### BR-STATUS-TC-02. Archived product phải discontinued

Preconditions:
- Có product đang ở `active = True`.

Steps:
1. Mở product.
2. Đặt `product_status = discontinued`.
3. Archive product hoặc đặt `active = False`.
4. Lưu product.

Expected Result:
- Product được lưu thành công.
- Product có `active = False`.
- Product có `product_status = discontinued`.

### BR-STATUS-TC-03. Discontinued product vẫn có thể active

Preconditions:
- Có product đang ở `active = True`.

Steps:
1. Mở product.
2. Đặt `product_status = discontinued`.
3. Giữ `active = True`.
4. Lưu product.

Expected Result:
- Product được lưu thành công.
- Product vẫn xuất hiện trong dữ liệu active.
- Product thể hiện đúng trạng thái nghiệp vụ là `discontinued`.

### BR-STATUS-TC-04. Draft product dùng để nhập liệu

Preconditions:
- Có category hợp lệ để tạo product.

Steps:
1. Tạo product mới.
2. Đặt `product_status = draft`.
3. Chưa nhập đủ toàn bộ thông tin tư vấn.
4. Lưu product.

Expected Result:
- Product được lưu thành công ở trạng thái `draft`.
- Product chưa được xem là sẵn sàng tư vấn/bán.

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
- Hệ thống hiển thị lỗi validation rằng giá bán không được âm.

### BR-PRICE-TC-02. Không cho giá bán âm khi cập nhật product

Preconditions:
- Có product đã tồn tại.

Steps:
1. Mở product.
2. Đổi `list_price = -100`.
3. Lưu product.

Expected Result:
- Hệ thống không cho lưu.
- Giá bán cũ của product không bị cập nhật thành giá âm.

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
- `list_price` được cập nhật đúng giá trị.

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
- Hệ thống hiển thị lỗi validation rằng số lượng tồn không được âm.

### BR-STOCK-TC-02. Không cho số lượng tồn âm khi cập nhật product

Preconditions:
- Có product đã tồn tại.

Steps:
1. Mở product.
2. Đổi `qty_available = -10`.
3. Lưu product.

Expected Result:
- Hệ thống không cho lưu.
- Số lượng tồn cũ không bị cập nhật thành số âm.

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
- Cả hai lần lưu đều thành công.
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
- `stock_status` là field chỉ đọc hoặc không cho người dùng nhập tay.
- Giá trị `stock_status` luôn được xác định từ `qty_available`.

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

### BR-FIELD-TC-04. Không cho xóa giá trị required field khi product đang available

Preconditions:
- Product đang ở `product_status = available`.
- Product có field `CPU` required và đã có giá trị.

Steps:
1. Mở product.
2. Xóa giá trị field `CPU`.
3. Lưu product.

Expected Result:
- Hệ thống không cho lưu.
- Product vẫn giữ trạng thái dữ liệu hợp lệ trước đó.

### BR-FIELD-TC-05. Required selection field phải chọn option hợp lệ

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
- Product không được chuyển sang `available` khi thiếu option cho required selection field.

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

## 8. Product Discovery Data Rules

### BR-DIS-TC-01. Màn tra cứu mặc định chỉ hiển thị active product phù hợp

Preconditions:
- Có các product với trạng thái sau:
  - `active = True`, `product_status = available`
  - `active = True`, `product_status = discontinued`
  - `active = True`, `product_status = draft`
  - `active = False`, `product_status = discontinued`

Steps:
1. Mở màn tra cứu Product của Consultant/Viewer.
2. Kiểm tra danh sách product mặc định.

Expected Result:
- Danh sách mặc định hiển thị product `active = True`.
- Danh sách mặc định hiển thị product có `product_status = available` hoặc `discontinued`.
- Product `draft` không xuất hiện trong màn tra cứu chính.
- Product `active = False` không xuất hiện trong màn tra cứu chính.

### BR-DIS-TC-02. Viewer/Consultant thấy các trạng thái cần cho tư vấn

Preconditions:
- Có product đang được hiển thị trong màn tra cứu.

Steps:
1. Mở product list hoặc product detail.
2. Kiểm tra các thông tin trạng thái và dữ liệu tư vấn.

Expected Result:
- Người dùng thấy `list_price`.
- Người dùng thấy `qty_available`.
- Người dùng thấy `stock_status`.
- Người dùng thấy `product_status`.

### BR-DIS-TC-03. Discontinued product vẫn tra cứu được

Preconditions:
- Có product `active = True`, `product_status = discontinued`.

Steps:
1. Mở màn tra cứu Product.
2. Tìm product discontinued theo tên hoặc mã.

Expected Result:
- Product discontinued vẫn có thể được tìm thấy.
- Trạng thái `discontinued` được hiển thị rõ để tránh tư vấn nhầm là sản phẩm đang bán.

## 9. Ghi Chú

- Các test case về quyền Admin/Viewer chi tiết nên đặt ở tài liệu test access
  control hoặc security riêng.
- Các test case này ưu tiên xác nhận business behavior trước khi tối ưu Product
  Discovery.
- Với required numeric dynamic fields, MVP cần chốt thêm việc `0` có được xem là
  giá trị hợp lệ hay không.
