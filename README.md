# 🚀 Platform System 

Bản đồ tri thức hệ thống Microservices Polyrepo.

---

## 🗺️ Master Map (12 Repositories)

### 1. UI (Giao diện người dùng)
- **Platform.UI**: Giao diện cổng thông tin Nexus hiện đại.

### 2. APIs (Services nghiệp vụ)
- **Platform.Identity.API**: Quản lý Tài khoản & Xác thực người dùng.
- **Platform.Catalog.API**: Quản lý Sản phẩm & Danh mục.
- **Platform.Gateway**: Cổng tiếp nhận & Điều hướng yêu cầu (Gateway).

### 3. Core (Xương sống kiến trúc)
- **Platform.Domain**: Logic nghiệp vụ cốt lõi (Entities, Rules).
- **Platform.Application**: Quy trình xử lý hồ sơ (Use Cases, MediatR).
- **Platform.Infrastructure**: Hiện thực hóa công nghệ (RabbitMQ, Postgres).
- **Platform.Contracts**: Ngôn ngữ liên lạc chung (Integration Events).

### 4. Base (Tiện ích hỗ trợ)
- **Platform.BuildingBlocks**: Các công cụ lập trình cơ bản.
- **Platform.SystemContext**: Ngữ cảnh người dùng & Hệ thống.

### 5. Ops (Vận hành)
- **Platform.IaC**: Cấu hình hạ tầng Docker.
- **Platform.CI-CD**: Quy trình tự động hóa GitHub Actions.

---
## 🤖 AI Context & Instruction (Dành cho AI)
Nếu bạn là AI hỗ trợ dự án này, hãy tuân thủ:
- **Ngữ cảnh**: Hệ thống Microservices Polyrepo (12 repositories).
- **Kiến trúc**: Clean Architecture, DDD, Event-Driven.
- **Nghiệm vụ**: Review code, tối ưu hóa logic nghiệp vụ và đảm bảo tính đồng nhất giữa các repository.
- **Tiêu chuẩn**: Luôn kiểm tra các `Contracts` trước khi đề xuất thay đổi Integration Events.
- **GIỚI HẠN QUYỀN (QUAN TRỌNG)**: User đang học Microservices, nên AI tuyệt đối KHÔNG ĐƯỢC dùng tool can thiệp sửa code trực tiếp. AI chỉ được đưa ra code mẫu trong khung chat để user tự gõ lại và rèn luyện. BẮT BUỘC phải có lệnh cho phép trước khi thao tác push/commit đối với toàn bộ các dự án Code. **(☀️ NGOẠI LỆ: AI ĐƯỢC PHÉP ĐẶC CÁCH tự động chỉnh sửa và push thẳng lên riêng Repo `Platform.Docs` này mà không cần xin phép)**.
- **Quy chuẩn Commit**: Mọi mã commit đẩy lên đều phải tuân theo chuẩn Conventional format (feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert) và BẮT BUỘC viết bằng Tiếng Anh (English ONLY).
- **Cleanup Code**: Trước khi tiến hành Commit/Push (nếu được phép), AI BẮT BUỘC phải soi lại toàn bộ C# class và dọn dẹp xóa sạch các đoạn khai báo namespace (`using`) bị thừa thãi. Đảm bảo source code luôn Clean trước khi lên Remote.
- **CI/CD Tập trung**: Mọi quy trình CI/CD BẮT BUỘC phải sử dụng template chuẩn tại repo `Platform.CI-CD`. KHÔNG ĐƯỢC tự tạo quy trình CI/CD rời rạc trong từng project. Nếu template thiếu tính năng, phải cập nhật trực tiếp vào file template trong `Platform.CI-CD`.
- **Tái sử dụng Code**: Chủ động tìm kiếm và đọc các repository xung quanh (ví dụ: `BuildingBlocks`, `Common`, v.v.) để tái sử dụng code, pattern hoặc thư viện đã có. KHÔNG tự code lại từ đầu nếu thành phần đó đã tồn tại trong hệ sinh thái.
- **Chiến lược Xác thực (JWT)**: Toàn bộ downstream HTTP APIs có user context phải đi theo hướng `every service validates JWT`. `Platform.Gateway` có thể xác thực trước ở edge, nhưng KHÔNG phải trust boundary duy nhất.
- **Nguồn danh tính chuẩn**: Các downstream service BẮT BUỘC phải lấy user identity từ `HttpContext.User.Claims` sau khi JWT đã được xác thực trong chính service đó. KHÔNG được dùng `X-User-*` headers làm nguồn danh tính chính cho business logic hoặc authorization.
- **Claims chuẩn toàn hệ**: Khi cần đọc user context, ưu tiên thống nhất theo các claim `sub`, `email`, `preferred_username`.
- **Chuẩn triển khai cho HTTP APIs**: Với các APIs nhận request từ client hoặc có user context, AI phải ưu tiên mẫu triển khai gồm `AddKeycloakAuthentication(builder.Configuration)`, `AddAuthorization()`, `UseAuthentication()`, `UseAuthorization()`, và gắn `[Authorize]` cho controller/action cần bảo vệ.
