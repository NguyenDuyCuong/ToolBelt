Dễ thôi Cường — mình sẽ **sửa lại toàn bộ tài liệu SRS** theo đúng hướng mới:  
**Automerge (CRDT) + WebRTC**,  
và **giữ đầy đủ các nội dung đã trao đổi từ đầu**:  
- Ứng dụng quản lý Tasks  
- Distributed + Decentralized  
- Không server  
- P2P sync  
- Offline-first  
- Không dùng Gun.js nữa  
- Có thể dùng IPFS/Helia nếu cần lưu file (tùy chọn)

Dưới đây là **bản SRS đã được viết lại hoàn chỉnh**, rõ ràng, mạch lạc và đúng chuẩn.

---

# 📘 **Software Requirements Specification (SRS)**  
## **Decentralized Task Management System (DTM)**  
### *(Version: Automerge + WebRTC Edition)*

---

# **1. Introduction**

## **1.1 Purpose**
Tài liệu này mô tả yêu cầu của hệ thống **Decentralized Task Manager (DTM)** — một ứng dụng quản lý công việc hoạt động hoàn toàn theo mô hình **P2P**, không sử dụng máy chủ trung tâm.  
Hệ thống sử dụng:

- **Automerge (CRDT)** để lưu trữ và đồng bộ dữ liệu không xung đột  
- **WebRTC** để kết nối P2P giữa các client  
- **(Tùy chọn)** Helia/IPFS để lưu trữ file phi tập trung  

DTM hướng tới khả năng hoạt động **offline-first**, **không phụ thuộc server**, và **đồng bộ mượt mà giữa nhiều thiết bị**.

---

## **1.2 Scope**
Hệ thống cho phép:

- Tạo, cập nhật, phân công và theo dõi nhiệm vụ  
- Quản lý người dùng theo phân cấp (Admin → Manager → Executor)  
- Đồng bộ dữ liệu P2P giữa các client  
- Lưu trữ dữ liệu bằng Automerge (CRDT)  
- Kết nối trực tiếp qua WebRTC  
- Hoạt động trong LAN hoặc mạng nội bộ  
- Không sử dụng server  

---

## **1.3 Definitions**
- **DTM** – Decentralized Task Manager  
- **CRDT** – Conflict-free Replicated Data Type  
- **Automerge** – Thư viện CRDT dùng để lưu trữ và hợp nhất dữ liệu  
- **WebRTC** – Giao thức kết nối P2P giữa các client  
- **Peer** – Một client tham gia mạng  
- **Offline-first** – Ứng dụng hoạt động không cần mạng, đồng bộ khi có kết nối  

---

## **1.4 References**
- Automerge Documentation  
- WebRTC Specification  
- IEEE SRS 830-1998  

---

## **1.5 Overview**
Tài liệu mô tả tổng quan hệ thống, yêu cầu chức năng, yêu cầu phi chức năng và các thông tin hỗ trợ triển khai.

---

# **2. Overall Description**

## **2.1 Product Perspective**
DTM là ứng dụng quản lý công việc **phi tập trung**, không có backend.  
Mỗi client giữ một bản sao đầy đủ của dữ liệu (Automerge document).  
Khi các peer kết nối qua WebRTC, dữ liệu được đồng bộ tự động bằng CRDT.

Hệ thống phù hợp với:

- Nhóm làm việc nội bộ  
- Môi trường không có server  
- Mạng LAN hoặc mesh network  
- Ứng dụng cần tính riêng tư cao  

---

## **2.2 Product Functions**
- Quản lý nhiệm vụ (CRUD)  
- Quản lý người dùng và phân quyền  
- Đồng bộ dữ liệu P2P  
- Hoạt động offline-first  
- Lưu trữ file phi tập trung (tùy chọn)  

---

## **2.3 User Classes**
- **Admin** – tạo người dùng, phân quyền  
- **Manager** – giao nhiệm vụ, theo dõi tiến độ  
- **Executor** – thực hiện nhiệm vụ  

---

## **2.4 Operating Environment**
- Desktop/mobile app (Electron, React Native…)  
- Automerge (CRDT)  
- WebRTC (P2P)  
- (Tùy chọn) Helia/IPFS  
- Mạng LAN hoặc Internet có NAT traversal  

---

## **2.5 Constraints**
- Không sử dụng server   
- Tất cả logic chạy client-side  
- Dữ liệu phải đồng bộ được khi mạng chập chờn  
- Mỗi peer phải giữ khóa riêng (nếu dùng mã hóa)  

---

## **2.6 Assumptions**
- Các peer có thể tìm thấy nhau qua WebRTC signaling thủ công (QR code, link mời, nhập IP)  
- Người dùng có thể chia sẻ link mời P2P  
- Mạng LAN ổn định giúp sync nhanh hơn  

---

# **3. Specific Requirements**

## **3.1 External Interfaces**
- **UI**: giao diện quản lý nhiệm vụ  
- **Network**: WebRTC DataChannel  
- **Data**: Automerge document  

---

# **3.2 Functional Requirements**

## **3.2.1 Peer Discovery & Connection**
- **FR1.1** – Hệ thống tạo link mời chứa thông tin kết nối WebRTC  
- **FR1.2** – Peer khác nhập link để kết nối trực tiếp  
- **FR1.3** – Không sử dụng server signaling; có thể dùng QR code hoặc copy-paste SDP  

---

## **3.2.2 User Management**
- **FR2.1** – Admin tạo người dùng mới  
- **FR2.2** – Gán vai trò: Admin, Manager, Executor  
- **FR2.3** – Thay đổi vai trò được ghi vào Automerge document  

---

## **3.2.3 Task Management**
- **FR3.1** – Tạo nhiệm vụ (title, description, assignee, priority, deadline)  
- **FR3.2** – Cập nhật trạng thái nhiệm vụ  
- **FR3.3** – CRDT đảm bảo không xung đột khi nhiều peer chỉnh sửa  
- **FR3.4** – Tìm kiếm nhiệm vụ theo trạng thái, người thực hiện  

---

## **3.2.4 Data Synchronization**
- **FR4.1** – Mỗi peer giữ bản sao đầy đủ của Automerge document  
- **FR4.2** – Khi kết nối WebRTC, các peer trao đổi changesets  
- **FR4.3** – Automerge tự hợp nhất dữ liệu không xung đột  
- **FR4.4** – Hệ thống phải hoạt động offline-first  

---

## **3.2.5 File Storage (Optional)**
- **FR5.1** – Lưu file đính kèm bằng Helia/IPFS  
- **FR5.2** – Lưu hash vào Automerge document  

---

# **3.3 Non‑Functional Requirements**

## **3.3.1 Performance**
- Đồng bộ giữa các peer trong ≤ 3 giây khi cùng LAN  
- Hỗ trợ tối thiểu 200 peer  

---

## **3.3.2 Security**
- Mã hóa WebRTC DTLS  
- (Tùy chọn) Mã hóa nội dung Automerge bằng key chung  
- Không có server nên không có điểm tấn công trung tâm  

---

## **3.3.3 Reliability**
- Dữ liệu được nhân bản trên tất cả peer  
- Không có single point of failure  
- CRDT đảm bảo không mất dữ liệu  

---

## **3.3.4 Usability**
- UI đơn giản, dễ dùng  
- Hỗ trợ đa ngôn ngữ  

---

## **3.3.5 Maintainability**
- Kiến trúc module  
- Dễ mở rộng thêm loại dữ liệu khác  

---

## **3.3.6 Scalability**
- CRDT hỗ trợ mở rộng số lượng peer  
- WebRTC mesh phù hợp nhóm nhỏ–trung bình  

---

# **4. Supporting Information**
- Use case diagram  
- Data model (Automerge schema)  
- WebRTC connection flow  
- Peer invitation flow  

---

# 🎉 **SRS đã được sửa xong theo đúng yêu cầu**

Phiên bản này:

- Dùng **Automerge (CRDT)**  
- Dùng **WebRTC**  
- Không server  
- Giữ toàn bộ nội dung đã trao đổi từ đầu  
- Rõ ràng, mạch lạc, chuẩn SRS  
