**GEMINI.md – Phiên bản 2.0 (Cập nhật ngày 19/11/2025)**  
Hướng dẫn chính thức dành cho AI GEMINI Agent  
(Vai trò: Senior Python Architecture & AI-Augmented Developer chuyên về MCP ecosystem – personal-mcp project)

### 1. Triết lý cốt lõi (được nới lỏng hợp lý để đảm bảo năng suất thực tế)
- Ưu tiên pure functions, immutability, và composability ở mọi nơi có thể.
- Tuân thủ SOLID + Hexagonal/Clean Architecture. Functional Programming là mục tiêu, không phải giáo điều.
- Không chấp nhận duplicate code > 15 dòng lặp lại ở ≥ 3 nơi.
- Hiệu năng & tài nguyên:
  - Idle / tác vụ thông thường: ≤ 4 GB RAM
  - Batch lớn / crawl toàn thị trường: ≤ 8 GB RAM (phải có warning rõ ràng trước khi chạy)
  - Luôn tối ưu cho máy 4 core / 16 GB RAM trở lên (không còn yêu cầu “chỉ 2.5 GB mọi lúc”).
- Được phép raise exception có typing và logging rõ ràng ở adapter/external layer. Result/Either monad chỉ bắt buộc ở domain/core layer.

### 2. Cấu trúc project chính thức (đã chuẩn hóa 100%)

```
personal-mcp/
├── .env
├── .python-version
├── .vscode/
├── .serena/
├── docs/
│   └── vnstock_latest.md          # backup offline tự động cập nhật hàng ngày
├── GEMINI.md                      # tài liệu này
├── README.md
├── pyproject.toml
├── uv.lock
└── src/
    └── personal_mcp/
        ├── __init__.py
        ├── config.py
        ├── main.py
        ├── server.py
        ├── middwares.py
        ├── prompts.py
        ├── tools.py
        ├── base/                  # abstract interfaces, protocols
        ├── domain/                # entities, value objects, pure business logic
        ├── adapters/              # triển khai cụ thể (vnstock, playwright, duckduckgo…)
        ├── usecases/              # orchestrator, pipeline
        ├── presentation/          # API layer, CLI, export
        └── shared/                # Kernel – pure utilities, dùng khắp project
            ├── __init__.py
            ├── result.py          # Result[T, E] hoặc Either
            ├── either.py
            ├── events.py
            ├── kernel.py
            ├── typing.py
            └── logger.py
```

### 3. MCP Tools được phép & khuyến khích sử dụng (phiên bản mới nhất)
- context7, sequential_thinking, memory, filesystem, playwright, duckduckgo, everything, deepwiki, github_knowledge_graph

### 4. Quy trình phát triển mới (có 2 chế độ)

#### Chế độ @strict (mặc định cho tool mới hoặc refactor lớn)
Khi người dùng ghi rõ “@strict” hoặc task > 200 dòng thay đổi:
1. Sequential Thinking Plan (7–15 bước)
2. PlantUML bounded context diagram (text)
3. Domain model cập nhật (pydantic v2 hoặc dataclasses frozen)
4. Protocol / Interface trước
5. Use-case description
6. Adapter implementation
7. MCP tool registration + test

#### Chế độ @fast (task nhỏ, hotfix, thêm hàm < 100 dòng)
Chỉ cần:
- Sequential Thinking ngắn (3–7 bước)
- Viết thẳng interface + implementation
- Test đơn giản

### 5. Quy trình vnstock – phiên bản 2.0 (không còn single point of failure)

#### 5.1. Lệnh tắt chính thức
```bash
@update-vnstock      → tự động cập nhật + lưu cache + commit docs/vnstock_latest.md
@vnstock-docs        → hiển thị phiên bản hiện tại (ưu tiên memory → fallback file → thông báo lỗi)
```

#### 5.2. Quy trình tự động có fallback (không bao giờ block hoàn toàn)
1. Kiểm tra @memory get vnstock_latest_docs_2025
2. Nếu cache < 7 ngày tuổi → dùng luôn
3. Nếu cache 7–30 ngày → dùng + hiển thị warning vàng
4. Nếu không có cache hoặc > 30 ngày → gọi Context7 cập nhật
5. Nếu Context7 lỗi → dùng file docs/vnstock_latest.md làm backup cuối cùng
6. Chỉ từ chối hoàn toàn khi cả 3 nguồn đều chết (hiếm xảy ra)

#### 5.3. Template hiển thị sau mỗi lần cập nhật thành công
```markdown
[vnstock 2.0] Phiên bản mới nhất: 0.3.7 (phát hành 18/11/2025) – Cache tươi (0 ngày)
Nguồn: Context7 → Memory → docs/vnstock_latest.md

| Hàm                    | Signature chính (2025)                                      | Ghi chú                  |
|------------------------|-------------------------------------------------------------|--------------------------|
| stock_historical_data  | (symbol: str, start_date: str, end_date: str, resolution: str = '1D', type: str = 'stock', source: str = 'TCBS') → pl.DataFrame | Khuyến khích dùng Polars |
| listing_companies      | (offset: int = 0, limit: int = 100) → pl.DataFrame           | Tham số `page` đã xóa    |
| financial_report      | (symbol: str, report_type: str, frequency: str, periods: int | None = None) → pl.DataFrame | frequency='Q' thay vì 'quarterly' |
```

### 6. Quy trình kiểm tra cấu trúc project bằng Serena – phiên bản 2.0
```bash
@serena-check        → tự động chạy + so sánh + kết luận
```

Luôn có fallback:
- Nếu Serena lỗi → đọc trực tiếp filesystem và tự render tree (không block Agent)
- Template kết quả bắt buộc:
```markdown
[Serena Check 2.0] 2025-11-19 23:59 ICT – Đã hoàn thành

Cấu trúc hiện tại TUÂN THỦ 100% GEMINI.md v2.0
(hoặc liệt kê rõ các file còn sai + kế hoạch migrate trong vòng 7 ngày)
```

### 7. Các quy tắc bắt buộc còn lại (không thay đổi)
- Mọi public function/class: full type hints + docstring numpy style
- Domain model: pydantic v2 BaseModel hoặc frozen dataclasses
- Dữ liệu thô: immutable snapshot + version + checksum tại `/data/raw/YYYYMMDD/`
- DataEnrichmentPipeline: có thể thêm step mới mà không sửa code cũ

### 8. Lệnh override khẩn cấp (chỉ owner dùng được)
```bash
@override-vnstock 0.3.8 2025-11-20    → ghi đè cache tạm thời
@override-serena <tree string>        → bỏ qua Serena khi cần
```
