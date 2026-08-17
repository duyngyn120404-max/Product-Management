# Business Rules

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Product Management PV |
| Ứng dụng | Quản lý sản phẩm nội bộ |
| Nguồn đầu vào | |
| Phiên bản tài liệu | Draft 1 |
| Ngày lập | 2026-08-17 |

Tài liệu này nhầm thiết lập các quy tắc nghiệp vụ cho dữ liệu sản phẩm: Trong phiên bản này, business rules nhằm thống nhất cách hệ thống xử lý trạng thái sản phẩm, giá bán, tồn kho và trải nghiệm tra cứu của Consultant/Viewer. 
## 1. Phạm vi
Áp dụng cho các nhóm dữ liệu chính:
- Product
- Category
- Brand
- Product Field Value
- Product status
- Product price
- Product stock

Không bao gồm:

## 2. Product Status and Active
### BR-STATUS-01. Ý nghĩa của `product_status`
product_status là trạng thái nghiệp vụ của sản phẩm

|Giá trị | Ý nghĩa |
|---|---|
|draft| chưa sẵn sàng tư vấn/bán|
|available| đang được phép tư vấn/bán|
|discontinued| ngừng bán/ngừng tư vấn|

### BR-STATUS-02. Ý nghĩa `active`
`active` là trạng thái kỹ thuật dùng cho cơ chế archieve của Odoo

|Giá trị|Ý nghĩa|
|---|---|
|True| record còn được sử dụng trong hệ thống|
|False| đã bị archieved, sản phẩm bị ẩn khỏi luồng tra cứu mặc định|

### BR-STATUS-03. Ràng buộc giữa `activte` và `product_status`
Sản phẩm có `product_status=available` bắt buộc phải có `active=True` và `active=False` thì `product_status=discontinued`

### BR-STATUS-04. Không đòng nhất `discontinued` với archieve
`product_status=discontinued` k đồng nghĩa với `active=False`
Sản phẩm ngừng bán vẫn có thể `active = True` để Consultant/Viewer biết rằng sản phẩm từng tồn tại nhưng hiện k còn được tư vấn/bán

### BR-STATUS-05. Sản phẩm `draft`
Sản phẩm `draft` dùng cho Admin chuẩn bị dữ liệu
Mặc định, sản phẩm `draft` không nên xuất hiện trong màn tra cứu chính của Consultant/Viewer

## 3. Price Rules

### BR-PRICE-01. Giá bán k âm
`list_price` k được nhỏ hơn `0`

### BR-PRICE-02. Giá của sản phẩm available
Sản phẩm có `product_status=available` nên có `list_price>0` (trừ trường hợp cho phép sản phẩm ở trạng thái chưa chốt giá/giá liên hệ)

### BR-PRICE-03. Giá bằng 0
`list_price=0` được phép trong các trường hợp
- `product_status=draft`
- Sản phẩm chưa chốt giá
- Sản phẩm cần tư vấn báo giá riêng

## 4. Stock Rules
### BR-STOCK-01. Số lượng tồn k âm
`qty_availabel` k được nhỏ hơn `0`

### BR-STOCK-02. Ý nghĩa `stock_status`
`stock_status` thể hiện trạng thái tồn kho dùng cho tra cứu và tư vấn

|Giá trị| Ý nghĩa|
|---|---|
|`in_stock` | Còn hàng |
|`low_stock` | Sắp hết hàng |
|`out_of_stock` | Hết hàng |

### BR-STOCK-03. Tính `stock_status` từ `qty_available`
|Điều kiện | `stock_status` |
|---|---|
|`qty_availabel=0` | `out_of_stock` |
|`qty_available>0` và `qty_available <= low_stock_threshold`| `low_stock` |
|`qty_available > low_stock_threshold` | `in_stock` |

### BR-STOCK-04. Sản phẩm hết hàng vẫn có thể available
Ý nghĩa sản phẩm vẫn cần được tư vấn, nhưng hiện tại hết hàng

## 5. Product Discovery Rules
### BR-DIS-01. Màn tra cứu mặc định
Màn tra cứu chính của Consultant/Viewer mặc định chỉ hiển thị sản phẩm `active=True` và `product_status` thuộc `available` hoặc `discontinued`

### BR-DIS-02. Trạng thái cần hiển thị cho Viewer
Consultant ngoài các thông tin về speicied về sản phẩm, cần thấy các trạng thái khác như:
- `list_price`: giá niêm yết
- `qty_available`: số lượng tồn
- `stock_status`: trạng thái tồn (dựa vào qty)
- `product_status`: trạng thái sản phẩm 

### BR-DIS-03: Sản phẩm discontinued trong tra cứu
- Sản phẩm discontinued vẫn được hiển thị cho consultat

## 6. Category Field 
### BR-FIE-01. Field động theo category
Mỗi cateogyr có thể định nghĩa bộ Field riêng. Khi product được gắn với category, hệ thống tạo hoặc đồng bộ Product Field Value tương ứng

### BR-FIELD-02. Required dynamic Field
Nếu category field được đánh dấu required, product phải có giá trị hợp lệ cho field. Với draft cho phép thiếu để admin nhập liệu

### BR-FIELD-03. Inactive category field
Khi category field bị inactive, field đó k nên xuất hiện trong form nhập liệu của product. (Dữ liệu cũ cần có cách xử lỷ)

### BR-FIELD-04. Selection Option
Nếu field type là selection, giá trị được chọn phải thuộc danh sách option

