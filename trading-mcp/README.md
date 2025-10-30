Bạn có thể tự xây dựng MCP lấy dữ liệu cổ phiếu
Đây là cách bạn có thể triển khai:
- Tích hợp API tài chính như:
- Vietstock – dữ liệu cổ phiếu Việt Nam
- Investing.com – biểu đồ, phân tích kỹ thuật
- Simplize.vn – giá cổ phiếu và lịch trả cổ tức
- Xây dựng MCP Server:
- Sử dụng Node.js hoặc Python để tạo máy chủ MCP.
- Thiết kế các endpoint như /get-stock-info, /get-chart, /get-dividend-schedule.
- Lưu trữ ngữ cảnh người dùng: mã cổ phiếu, thời gian, loại dữ liệu cần truy vấn.
- Tích hợp với mô hình AI:
- Kết nối với GPT hoặc Claude để xử lý ngôn ngữ tự nhiên và truy vấn dữ liệu cổ phiếu theo ngữ cảnh.

🔍 Ví dụ ứng dụng MCP trong chứng khoán
- Người dùng hỏi: “Giá cổ phiếu FPT hôm nay là bao nhiêu?”
- MCP lưu ngữ cảnh “FPT” là mã cổ phiếu, “hôm nay” là ngày hiện tại.
- Máy chủ MCP gọi API Vietstock để lấy giá và trả về kết quả.

🚀 Gợi ý mở rộng
- Tích hợp thêm dữ liệu ETF, chỉ số VN-Index, khối lượng giao dịch, phân tích kỹ thuật.
- Cho phép người dùng đặt câu hỏi phức tạp như: “So sánh P/E của FPT và VNM trong 6 tháng qua.”


# Dev
> uv run uvicorn stock_mcp.main:app --host 0.0.0.0 --port 8000 --reload