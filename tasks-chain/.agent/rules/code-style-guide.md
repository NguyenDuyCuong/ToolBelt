---
trigger: always_on
---

## 1. Sử dụng Model Context Protocol (MCP) Tools
- **Sequential Thinking - sequentialthinking - cho mọi yêu cầu ban đầu**  
  Luôn phân rã yêu cầu gốc thành chuỗi các bước tư duy tuần tự (sequential steps). Mỗi bước phải được diễn đạt rõ ràng, độc lập và có thứ tự thực thi logic. Không được bỏ qua hoặc gộp bước để đảm bảo khả năng theo dõi và tái hiện.

- **Sử dụng Tool Memory để lưu trữ và quản lý context**  
  Bắt buộc sử dụng cơ chế memory của MCP tools để lưu lại toàn bộ các step đã thực hiện. Việc này cho phép:
  - Quay lại (rollback) về bất kỳ step nào trước đó mà không mất trạng thái.
  - Tiếp tục (resume) quy trình phức tạp sau khi bị gián đoạn.
  - Theo dõi lịch sử thay đổi và lý do của từng bước.
  Mọi step đều phải được ghi vào memory kèm theo metadata phù hợp (timestamp, input, output, intent).

## 2. Nguyên tắc thiết kế hệ thống và giải pháp

- **Hoàn toàn không có server**  
  Hệ thống chỉ được gồm các client giao tiếp trực tiếp với nhau (peer-to-peer). Máy chủ server chỉ đóng vai trò chứa mã nguồn.

- **Dữ liệu chỉ lưu trữ tại client**  
  Toàn bộ dữ liệu (bao gồm trạng thái ứng dụng, lịch sử giao dịch, private key, v.v.) phải được lưu trữ phân tán trên thiết bị của người dùng. Không được truyền hoặc đồng bộ lên bất kỳ server nào.

- **Đảm bảo an toàn và tính bất biến theo nguyên tắc blockchain**  
  Áp dụng các kỹ thuật cryptographic và thiết kế blockchain-inspired (merkle tree, cryptographic commitment, chain of hashes, decentralized consensus khi cần) để đảm bảo tính toàn vẹn, chống sửa đổi và khả năng xác minh độc lập mà không cần server.

## 3. Tiêu chuẩn lập trình
Code phải đáp ứng các yêu cầu nghiêm ngặt sau:

- Luôn Comment code đủ và đúng chuẩn. Đánh giá và update lại comment khi có sự thay đổi.

- **Pure Functions là bắt buộc**  
  Tất cả hàm logic cốt lõi phải là pure function: cùng input luôn cho cùng output, không có side effect, không phụ thuộc hoặc thay đổi trạng thái bên ngoài.

- **Ưu tiên tối đa Functional Programming**  
  Sử dụng paradigm lập trình hàm làm nền tảng chính: immutability, higher-order functions, function composition, referential transparency, algebraic data types khi có thể.

- **Tuân thủ nghiêm ngặt nguyên tắc SOLID** (khi vẫn phải sử dụng OOP hoặc hybrid approach)

Mọi vi phạm đối với các quy định trên đều phải được trình bày lý do rõ ràng trong code review và chỉ được chấp nhận trong trường hợp ngoại lệ cực kỳ hiếm hoi với sự đồng thuận của toàn bộ đội ngũ kiến trúc.