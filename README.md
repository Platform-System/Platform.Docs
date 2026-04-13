# 🚀 Platform System 

Bản đồ tri thức hệ thống Microservices Polyrepo.

---

## 🗺️ Master Map (12 Repositories)

### 1. APIs (Services nghiệp vụ)
- **Platform.Identity.API**: Quản lý Tài khoản & Xác thực người dùng.
- **Platform.Catalog.API**: Quản lý Sản phẩm & Danh mục.
- **Platform.Gateway**: Cổng tiếp nhận & Điều hướng yêu cầu (Gateway).

### 2. Core (Xương sống kiến trúc)
- **Platform.Domain**: Logic nghiệp vụ cốt lõi (Entities, Rules).
- **Platform.Application**: Quy trình xử lý hồ sơ (Use Cases, MediatR).
- **Platform.Infrastructure**: Hiện thực hóa công nghệ (RabbitMQ, Postgres).
- **Platform.Contracts**: Ngôn ngữ liên lạc chung (Integration Events).

### 3. Base (Tiện ích hỗ trợ)
- **Platform.BuildingBlocks**: Các công cụ lập trình cơ bản.
- **Platform.SystemContext**: Ngữ cảnh người dùng & Hệ thống.
- **Platform.Common**: Cấu hình và hằng số dùng chung.

### 4. Ops (Vận hành)
- **Platform.IaC**: Cấu hình hạ tầng Docker.
- **Platform.CI-CD**: Quy trình tự động hóa GitHub Actions.

---
## 🤖 AI Context & Instruction (Dành cho AI)
Nếu bạn là AI hỗ trợ dự án này, hãy tuân thủ:
- **Ngữ cảnh**: Hệ thống Microservices Polyrepo (12 repositories).
- **Kiến trúc**: Clean Architecture, DDD, Event-Driven.
- **Nghiệm vụ**: Review code, tối ưu hóa logic nghiệp vụ và đảm bảo tính đồng nhất giữa các repository.
- **Tiêu chuẩn**: Luôn kiểm tra các `Contracts` trước khi đề xuất thay đổi Integration Events.
