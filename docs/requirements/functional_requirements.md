# Functional Requirements — Product Management

## 1. Thông tin tài liệu

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Product Management PV |
| Ứng dụng | Quản lý sản phẩm nội bộ |
| Nền tảng mục tiêu | Odoo Community 19.0 |
| Nguồn đầu vào | `docs/source/customer.pdf` |
| Phiên bản tài liệu | Draft 1 |
| Ngày lập | 2026-08-06 |

## 2. Mô tả tài liệu

Tài liệu `functional_requirements.md` mô tả các tính năng đáp ứng các nhu cầu nghiệp vụ và người dùng từ khỏa sát ban đầu về yêu cầu của người dùng `customer.pdf`.

Gồm các 9 yêu cầu chức năng chính:
- Xác thực người dùng
- Phân quyền
- Quản lý tài khoản
- Quản lý danh mục
- Quản lý sản phẩm
- Danh sách sản phẩm
- Chi tiết sản phẩm
- Tìm kiếm, lọc và sắp xếp
- So sánh sản phẩm
- Quản lý tồn kho 

## 3. Giả định và ràng buộc

- Số người dùng ban đầu dưới 10 người.
- Dữ liệu ban đầu khoảng 100 sản phẩm.
- Người dùng truy cập bằng trình duyệt web.
- MVP chỉ có hai vai trò chính: Quản trị viên và Người xem.
- Chỉ Quản trị viên được tạo, sửa hoặc ngừng sử dụng dữ liệu nghiệp vụ.
- Người xem chỉ được đăng nhập, tìm kiếm và xem thông tin.
- Sản phẩm không bị xóa cứng trong MVP; hệ thống chỉ chuyển sang trạng thái
  ngừng sử dụng để tránh mất dữ liệu.
- Mỗi danh mục có thể cần thông tin riêng, nhưng MVP ưu tiên trường văn bản
  bổ sung thay vì xây cấu trúc trường động.

## 3. Yêu cầu chức năng

### FR-01. Xác thực người dùng

| Mã | Yêu cầu |
|---|---|
| FR-01.01 | Hệ thống chỉ cho phép người dùng xác thực bằng tên đăng nhập và mật khẩu. |
| FR-01.02 | Hệ thống kiểm tra trạng thái tài khoảng trước khi cho phép truy cập. |
| FR-01.03 | Hệ thống từ chối truy cập khi thông tin đăng nhập không hợp lệ. |
| FR-01.04 | Hệ thống từ chối truy cập khi tài khoản bị khóa hoặc ngừng hoạt động. |
| FR-01.05 | Hệ thống duy trì phiên đăng nhập sau khi người dùng xác thực thành công. |
| FR-01.06 | Hệ thống cho phép người dùng kết thúc phiên đăng nhập. |

### FR-02. Phân quyền

| Mã | Yêu cầu |
|---|---|
| FR-02.01 | Hệ thống hỗ trợ hai vai trò nghiệp vụ: Quản trị viên và nhân viên. |
| FR-02.02 | Quản trị viên được tạo, sửa và ngừng sử dụng sản phẩm. |
| FR-02.03 | Quản trị viên được tạo, sửa và ngừng sử dụng danh mục. |
| FR-02.04 | Quản trị viên được quản lý tài khoản người dùng nội bộ. |
| FR-02.05 | Người xem chỉ được xem danh sách, xem chi tiết, tìm kiếm và lọc sản phẩm. |
| FR-02.06 | Người xem không được truy cập các chức năng thêm, sửa, khóa, mở khóa hoặc ngừng sử dụng dữ liệu. |

### FR-03. Quản lý tài khoản

| Mã | Yêu cầu |
|---|---|
| FR-03.01 | Quản trị viên xem danh sách tài khoản hiển thị họ tên, tên đăng nhập hoặc email, vai trò và trạng thái tài khoản. |
| FR-03.02 | Quản trị viên tạo được tài khoản mới |
| FR-03.03 | Quản trị viên khóa hoặc mở khóa tài khoản. |
| FR-03.04 | Quản trị viên thay đổi vai trò của tài khoản giữa Quản trị viên và Người xem. |
| FR-03.05 | Quản trị viên đặt lại mật khẩu cho người dùng. |
| FR-03.06 | Nhân viên xem được thông tin tài khoản cơ bản của chính mình. |
| FR-03.07 | Nhân viên đổi được mật khẩu của chính mình. |

### FR-04. Quản lý danh mục

| Mã | Yêu cầu |
|---|---|
| FR-04.01 | Quản trị viên xem danh sách danh mục hiển thị tên danh mục, mô tả, số lượng sản phẩm và trạng thái sử dụng. |
| FR-04.02 | Quản trị viên tạo được danh mục mới. |
| FR-04.03 | Quản trị viên sửa/thêm/cập nhật được tên và các trường trong danh mục. |
| FR-04.04 | Quản trị viên ngừng sử dụng danh mục. |
| FR-04.05 | Hệ thống không cho Người xem tạo, sửa hoặc ngừng sử dụng danh mục. |
| FR-04.06 | Danh mục hỗ trợ bộ cấu hình riêng cho từng danh mục. |

### FR-05. Quản lý sản phẩm

| Mã | Yêu cầu |
|---|---|
| FR-05.01 | Quản trị viên tạo được sản phẩm mới. |
| FR-05.02 | Quản trị viên cập nhật được thông tin sản phẩm đã có. |
| FR-05.03 | Quản trị viên ngừng sử dụng sản phẩm thay vì xóa sản phẩm khỏi hệ thống. |
| FR-05.04 | Quản trị viên gắn sản phẩm với danh mục. |
| FR-05.05 | Quản trị viên xóa cứng sản phẩm. |

### FR-06. Danh sách sản phẩm

| Mã | Yêu cầu |
|---|---|
| FR-06.01 | Trang danh sách sản phẩm là màn hình sử dụng chính sau khi đăng nhập. |
| FR-06.03 | Với Quản trị viên, danh sách sản phẩm hiển thị thêm thao tác thêm sản phẩm, sửa sản phẩm, ngừng sử dụng và xóa cứng sản phẩm. |
| FR-06.04 | Với nhân viên, hệ thống ẩn và vô hiệu hóa các thao tác quản trị dữ liệu. |

### FR-07. Chi tiết sản phẩm

| Mã | Yêu cầu |
|---|---|
| FR-07.01 | Hệ thống hiển thị thông tin của sản phẩm để tư vấn |
| FR-07.02 | Thông tin chi tiết sản phẩm được tổ chức theo các nhóm thông tin phù hợp với dữ liệu sản phẩm và danh mục sản phẩm. |

### FR-08. Tìm kiếm, lọc và sắp xếp

| Mã | Yêu cầu |
|---|---|
| FR-08.01 | Hệ thống cho phép tìm/lọc sản phẩm theo tên. |
| FR-08.02 | Hệ thống cho phép tìm/lọc sản phẩm theo mã sản phẩm. |
| FR-08.03 | Hệ thống cho phép tìm/lọc sản phẩm theo danh mục. |
| FR-08.04 | Hệ thống cho phép tìm/lọc sản phẩm theo trạng thái |
| FR-08.05 | Hệ thống cho phép tìm/lọc sản phẩm theo thương hiệu |
| FR-08.06 | Hệ thống cho phép sắp xếp theo giá |

### FR-09. So sánh sản phẩm
| Mã | Yêu cầu |
|---|---|
| FR-09.01 | Hệ thống cho phép người dùng chọn nhiều sản phẩm thuọc cùng 1 danh mục để so sánh. |
| FR-09.02 | Hệ thống cho phép người dùng chọn/bỏ nhiều tiêu chí để so sánh. |

### FR-10. Quản lý tồn kho cơ bản

| Mã | Yêu cầu |
|---|---|
| FR-10.01 | Hệ thống lưu số lượng tồn hiện tại của từng sản phẩm. |
| FR-10.02 | Hệ thống xác định và hiển thị trạng thái còn hàng hoặc hết hàng dựa trên dữ liệu sản phẩm. |
| FR-10.03 | MVP không quản lý phiếu nhập kho, phiếu xuất kho, nhà cung cấp, kiểm kê kho hoặc lịch sử giao dịch kho. |


## 4. Rủi ro và một số giải pháp thay thế

- Cấu trúc thông tin của từng loại sản phẩm có thể khác nhau, dễ phát sinh nhu
  cầu trường dữ liệu riêng theo danh mục.
- Yêu cầu danh mục và thông tin tư vấn có thể thay đổi sau khi người dùng nhập
  dữ liệu thật.
- Dữ liệu sản phẩm và tồn kho trong MVP phụ thuộc vào việc Quản trị viên cập
  nhật thủ công.
- Ngưỡng xác định sản phẩm sắp hết hàng chưa được chốt; có thể dùng ngưỡng
  chung hoặc ngưỡng riêng theo từng sản phẩm ở giai đoạn sau.
