# Kurumi 2.0

Kurumi là ngôn ngữ lập trình API hiện đại, dễ sử dụng và mạnh mẽ, được thiết kế để tạo API và ứng dụng web một cách nhanh chóng.

## Tính năng chính

- **Cú pháp đơn giản**: Dễ học, dễ đọc, ít dấu ngoặc và dấu chấm phẩy
- **Kiểu dữ liệu mạnh**: Hỗ trợ kiểu dữ liệu tĩnh và động
- **Hướng đối tượng**: Hỗ trợ lập trình hướng đối tượng với class, interface
- **Decorator**: Hỗ trợ decorator để định nghĩa API, middleware, validation
- **Tích hợp cơ sở dữ liệu**: Hỗ trợ nhiều loại cơ sở dữ liệu
- **Đa nền tảng**: Chạy trên Windows, macOS, Linux

## Cài đặt

### Cài đặt qua npm

```bash
# Cài đặt toàn cục
npm install -g kurumi-lang

# Hoặc cài đặt trong dự án
npm install kurumi-lang
```

### Cài đặt qua pip

```bash
# Cài đặt toàn cục
pip install kurumi-lang
```

## Sử dụng

### Tạo dự án mới

```bash
kurumi init my-project
cd my-project
```

### Chạy ứng dụng

```bash
# Chế độ phát triển
kurumi dev

# Hoặc chạy file cụ thể
kurumi run src/app.kuru
```

### Biên dịch ứng dụng

```bash
kurumi build
```

## Ví dụ

```
# Ứng dụng Kurumi đơn giản
import { Server } from "kurumi/server"
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

# Khởi tạo server
server = Server()

@api("/api")
class BlogAPI
    @get("/posts")
    def getPosts(req, res) => Post.findAll()

# Đăng ký API
server.add_api(BlogAPI)

# Khởi động server
server.listen(3000)
print("Server đang chạy tại http://localhost:3000")
```

## Tài liệu

Để biết thêm chi tiết, vui lòng xem:

- [Giới thiệu toàn bộ](./KURUMI_INTRODUCTION.md)
- [Hướng dẫn sử dụng](./kurumi_guide.md)
- [Đặc tả ngôn ngữ](./kurumi_spec.md)
- [Hướng dẫn cài đặt](./INSTALL.md)

## Giấy phép

Kurumi được phát hành dưới giấy phép độc quyền.
