# Manual Test Cases — Product Comparison

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Product Management PV |
| Ứng dụng | Quản lý sản phẩm nội bộ |
| Nguồn đầu vào | `docs/plans/implementation_plan.md` |
| Phiên bản tài liệu | Draft 1 |
| Ngày lập | 2026-08-19 |

## 1. Mục Đích

Tài liệu này mô tả các test case thủ công ở mức tổng quan để kiểm tra luồng
Product Comparison trong MVP.

## 2. Test Cases

### CMP-TC-01. Mở compare wizard từ Product List
Status: Passed

Preconditions:
- Có ít nhất 2 product cùng category.

Steps:
1. Mở Product List.
2. Chọn 2 product cùng category.
3. Bấm Compare Products.

Expected Result:
- Compare wizard mở thành công.
- Wizard hiển thị các product đã chọn và category tương ứng.

### CMP-TC-02. Chặn compare khi số lượng product không hợp lệ
Status: Passed

Preconditions:
- Có ít nhất 5 product.

Steps:
1. Chọn 1 product và bấm Compare Products.
2. Chọn 5 product và bấm Compare Products.

Expected Result:
- Hệ thống chặn khi chọn ít hơn 2 product.
- Hệ thống chặn khi chọn nhiều hơn 4 product.

### CMP-TC-03. Chặn compare product khác category
Status: Passed

Preconditions:
- Có ít nhất 2 product thuộc 2 category khác nhau.

Steps:
1. Chọn các product khác category.
2. Bấm Compare Products.

Expected Result:
- Hệ thống không mở bảng compare.
- Hệ thống hiển thị lỗi/cảnh báo rằng chỉ compare được product cùng category.

### CMP-TC-04. Hiển thị bảng compare readonly
Status: Passed

Preconditions:
- Có 2-4 product cùng category.
- Các product có thông tin chung và dynamic fields.

Steps:
1. Chọn 2-4 product cùng category.  
2. Bấm Compare Products.
3. Kiểm tra bảng compare.

Expected Result:
- Bảng compare hiển thị product theo cột và tiêu chí theo dòng.
- Bảng có thông tin chung và dynamic fields của category.
- Bảng chỉ đọc, không chỉnh sửa dữ liệu product.

### CMP-TC-05. Chọn/bỏ tiêu chí compare
Status: Passed

Preconditions:
- Compare wizard đã mở với 2-4 product cùng category.

Steps:
1. Bỏ chọn một tiêu chí chung hoặc dynamic field.
2. Chọn lại tiêu chí đó.

Expected Result:
- Bảng compare cập nhật theo tiêu chí được chọn.
- Tiêu chí bị bỏ chọn không còn hiển thị trong bảng.
- Tiêu chí được chọn lại hiển thị trong bảng.
