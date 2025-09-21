# Kurumi 2.0 - Ngôn ngữ lập trình API hiện đại

![Kurumi Logo](https://via.placeholder.com/200x200.png?text=Kurumi+2.0)

## Giới thiệu

Kurumi là ngôn ngữ lập trình API hiện đại, dễ sử dụng và mạnh mẽ, được thiết kế để tạo API và ứng dụng web một cách nhanh chóng. Kurumi kết hợp những ưu điểm từ nhiều ngôn ngữ lập trình phổ biến như Python, Rust, Go, TypeScript, Swift và Kotlin, tạo ra một ngôn ngữ dễ học, dễ sử dụng nhưng vẫn đảm bảo hiệu suất cao.

## Tính năng chính

- **Cú pháp đơn giản**: Dễ học, dễ đọc, ít dấu ngoặc và dấu chấm phẩy
- **Kiểu dữ liệu mạnh**: Hỗ trợ kiểu dữ liệu tĩnh và động
- **Hướng đối tượng**: Hỗ trợ lập trình hướng đối tượng với class, interface
- **Decorator**: Hỗ trợ decorator để định nghĩa API, middleware, validation
- **Tích hợp cơ sở dữ liệu**: Hỗ trợ nhiều loại cơ sở dữ liệu như MySQL, PostgreSQL, MongoDB
- **Tích hợp API**: Dễ dàng tạo và quản lý API RESTful
- **Hiệu suất cao**: Biên dịch thành JavaScript/TypeScript để chạy trên Node.js
- **Đa nền tảng**: Chạy trên Windows, macOS, Linux

## Cài đặt

Kurumi có thể được cài đặt thông qua npm (Node.js) hoặc pip (Python):

### Cài đặt qua npm

```bash
# Cài đặt toàn cục
npm install -g kurumi-lang

# Hoặc sử dụng npx
npx kurumi-lang init my-project
```

### Cài đặt qua pip

```bash
# Cài đặt toàn cục
pip install kurumi-lang

# Sử dụng
kurumi init my-project
```

## Ví dụ mã nguồn

### Hello World

```
# Hello World in Kurumi
print("Hello, World!")
```

### API đơn giản

```
# Simple API in Kurumi
import { Server } from "kurumi/server"

# Khởi tạo server
server = Server()

@api("/api")
class HelloAPI
    @get("/hello/:name")
    def hello(req, res) => f"Hello, {req.params.name}!"

# Đăng ký API
server.add_api(HelloAPI)

# Khởi động server
server.listen(3000)
print("Server đang chạy tại http://localhost:3000")
```

### Kết nối cơ sở dữ liệu

```
# Database connection in Kurumi
import { Database } from "kurumi/database"

# Khởi tạo kết nối cơ sở dữ liệu
db = Database.connect("mysql://user:password@localhost:3306/blog")

@table("posts")
class Post
    constructor(title, content, author_id) =>
        this.title = title
        this.content = content
        this.author_id = author_id
    
    @static
    def findAll() => db.query("SELECT * FROM posts")
    
    @static
    def findById(id) => db.query("SELECT * FROM posts WHERE id = ?", [id])
    
    def save() =>
        if this.id
            # Cập nhật bài viết
            db.query(
                "UPDATE posts SET title = ?, content = ? WHERE id = ?",
                [this.title, this.content, this.id]
            )
        else
            # Tạo bài viết mới
            result = db.query(
                "INSERT INTO posts (title, content, author_id) VALUES (?, ?, ?)",
                [this.title, this.content, this.author_id]
            )
            this.id = result.insertId
```

## Lệnh cơ bản

- `kurumi init <tên-dự-án>`: Tạo dự án Kurumi mới
- `kurumi run <file>`: Chạy file Kurumi
- `kurumi dev`: Chạy ứng dụng ở chế độ phát triển
- `kurumi build`: Biên dịch ứng dụng

## Tài liệu

- [Hướng dẫn sử dụng](./kurumi_guide.md)
- [Đặc tả ngôn ngữ](./kurumi_spec.md)
- [Hướng dẫn cài đặt](./INSTALL.md)
- [Ví dụ API](./example_api.kuru)

## Đóng góp

Chúng tôi rất hoan nghênh mọi đóng góp từ cộng đồng. Nếu bạn muốn đóng góp, vui lòng:

1. Fork repository
2. Tạo branch mới (`git checkout -b feature/amazing-feature`)
3. Commit thay đổi của bạn (`git commit -m 'Add some amazing feature'`)
4. Push lên branch (`git push origin feature/amazing-feature`)
5. Tạo Pull Request

## Giấy phép

Kurumi được phát hành dưới giấy phép MIT. Xem file [LICENSE](./LICENSE) để biết thêm chi tiết.

## Liên hệ

- Website: [kurumi-lang.org](https://kurumi-lang.org)
- GitHub: [github.com/kurumi-2004/ngon-ngu-lap-trinh-API-kurumi](https://github.com/kurumi-2004/ngon-ngu-lap-trinh-API-kurumi)
- Email: kurumi@example.com