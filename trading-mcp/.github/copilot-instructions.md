# Project 
Là MCP server về thị trường chứng khoán Việt Nam.

# Coding
Code theo định hướng SOLID

### Modular Design
- Chia code thành các module nhỏ, chuyên biệt
- Mỗi module giải quyết một nhiệm vụ cụ thể
- Sử dụng package để nhóm module liên quan
- Ưu tiên composition over inheritance

### Pure Function
- Không thay đổi input arguments
- Không có side effects (IO, global state)
- Luôn trả về output nhất quán với cùng input
- Dễ test và debug

### Giới hạn
- Tối đa 300 dòng/file
- Mỗi file chứa 1 class chính hoặc 1 nhóm function liên quan
- Function không quá 20-30 dòng
- Chia nhỏ function phức tạp
- Tách class lớn thành multiple classes
- Sử dụng module để phân tách responsibility

### QUY TẮC COMMENT
- Docstring (Bắt buộc)
- Comment inline, Giải thích "tại sao" thay vì "cái gì"
- Comment cho logic phức tạp, thuật toán
- Đánh dấu TODO, FIXME khi cần

### Code Style
- Tuân thủ PEP 8
- Đặt tên có ý nghĩa (variables, functions, classes)
- Consistent formatting

### Error Handling
- Sử dụng exception thay vì return codes
- Specific exceptions thay vì generic
- Proper error messages và logging

### Performance
- Ưu tiên readability trước optimization
- Tránh premature optimization
- Sử dụng profiling để xác định bottlenecks

