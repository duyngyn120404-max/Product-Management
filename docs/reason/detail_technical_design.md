# Detailed Technical Design

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Product Management PV |
| Ứng dụng | Quản lý sản phẩm nội bộ |
| Nguồn đầu vào | `detail_technical_design.md` |
| Phiên bản tài liệu | Draft 1 |
| Ngày lập | 2026-08-06 |

## Nội dung

Diễn giải về các thiết kế trong `detailed_technical_design`

## 1. Data Model

1. *Kiểu thiết kê data model trong dự án hiện tại là gì?*

> Kiểu thiết kế này gọi là EAV Model (Entity - Attribute - Value) cho các trường thông tin động theo danh mục sản phẩm. Với `product` đóng vai trò entity, `category field definition` đóng vai trò attribute và `product field value` đóng vai trò value của từng attribute.

2. *Vì sao k dùng jsonb để biễu diễn trường động?*

> Không chọn `jsonb` làm hướng chỉnh vì các trường động trong hệ thống dược xem là metadata phụ, mà là các thông tin chính thức của sản phẩm. Jsonb phù hợp khi cần lưu dữ liệu bán cấu trúc hoặc metadata linh hoạt. 

3. *Vì sao k lưu các field động chung trong `Product` mà phải tách ra `category field definition` và `product field value`

> Vì mỗi danh mục sản phẩm có bộ field khác nhau, lưu hết có thể làm bảng phình to hoặc phải đổi schema.

## 2. Access Control

## 3. UI/View Design

## 4. Flows

