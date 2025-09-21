# Hướng dẫn sử dụng Kurumi 2.0

## Giới thiệu

Kurumi 2.0 là ngôn ngữ lập trình hiện đại được thiết kế để dễ sử dụng hơn Python, đồng thời tích hợp những ưu điểm từ nhiều ngôn ngữ như Rust, Go, TypeScript, Swift và Kotlin. Ngôn ngữ này tập trung vào tính đơn giản, hiệu suất cao, an toàn và khả năng mở rộng, đặc biệt phù hợp cho phát triển API web, ứng dụng di động và trí tuệ nhân tạo.

### Tại sao chọn Kurumi 2.0?

- **Dễ học hơn Python**: Cú pháp siêu đơn giản, loại bỏ các dấu ngoặc không cần thiết
- **Hiệu suất cao**: Tốc độ thực thi nhanh hơn Python 5-10 lần
- **Đa nền tảng**: Phát triển web, di động, desktop và AI trong cùng một ngôn ngữ
- **An toàn hơn**: Kiểu dữ liệu thông minh giúp phát hiện lỗi sớm
- **Tích hợp AI**: Hỗ trợ sẵn các thư viện và công cụ cho phát triển AI và ML

## Cài đặt

### Yêu cầu hệ thống
- Python 3.7+ (cho trình biên dịch)
- Node.js 14+ (cho môi trường runtime)

### Cài đặt Kurumi
```bash
# Cài đặt từ npm
npm install -g kurumi-lang

# Hoặc cài đặt từ pip
pip install kurumi-lang
```

## Bắt đầu nhanh

### Tạo dự án mới
```bash
kurumi init my-api-project
cd my-api-project
```

### Cấu trúc dự án
```
my-api-project/
├── src/
│   ├── app.kuru       # Điểm khởi đầu ứng dụng
│   ├── models/        # Thư mục chứa các model
│   ├── controllers/   # Thư mục chứa các controller
│   └── services/      # Thư mục chứa các service
├── tests/             # Thư mục chứa các test
├── kurumi.config.json # Cấu hình dự án
└── package.json       # Quản lý phụ thuộc
```

### Chạy ứng dụng
```bash
# Chạy ở chế độ phát triển
kurumi dev

# Hoặc build và chạy ở chế độ sản phẩm
kurumi build
kurumi start
```

## Cú pháp cơ bản

### Biến và hằng số

```kuru
# Khai báo biến với suy luận kiểu tự động
name = "Kurumi"
age = 25
is_active = true

# Khai báo biến với kiểu tĩnh tùy chọn
name: str = "Kurumi"
age: int = 25
is_active: bool = true

# Hằng số (không thể thay đổi)
PI: float = 3.14159
API_URL: str = "https://api.example.com"

# Kiểu dữ liệu phức tạp
user: User = User("Kurumi", "kurumi@example.com")
numbers: list[int] = [1, 2, 3, 4, 5]
config: dict[str, any] = {"debug": true, "port": 8080}

# Kiểu dữ liệu tùy chọn (nullable)
middle_name: str? = null  # Có thể là null
```

### Hàm

```kuru
# Hàm đơn giản - không cần dấu ngoặc nhọn
def greet(name)
    return f"Hello, {name}!"

# Hàm với kiểu dữ liệu
def greet(name: str) -> str
    return f"Hello, {name}!"

# Hàm một dòng - không cần từ khóa return
def multiply(a, b) => a * b

# Hàm với tham số mặc định và tham số từ khóa
def greet(name: str = "Guest", title: str = "") => f"Hello, {title} {name}!"

# Gọi hàm với tham số từ khóa
greeting = greet(name="Kurumi", title="Ms.")

# Hàm bất đồng bộ
async def fetch_data(url: str) -> dict
    response = await http.get(url)
    return response.json()

# Hàm với pattern matching
def process_value(value)
    match value
        case str()
            return f"String: {value}"
        case int() if value > 0
            return f"Positive number: {value}"
        case list()
            return f"List with {len(value)} items"
        case _
            return "Unknown type"
```

### Lớp và đối tượng

```kuru
// Khai báo lớp
class User {
    // Thuộc tính tĩnh
    static count = 0;
    
    // Constructor
    func constructor(name, email) {
        this.name = name;
        this.email = email;
        User.count++;
    }
    
    // Phương thức
    func getName() {
        return this.name;
    }
    
    func setName(name) {
        this.name = name;
    }
    
    // Phương thức tĩnh
    static func getCount() {
        return User.count;
    }
}

// Tạo đối tượng
let user = new User("John", "john@example.com");
console.log(user.getName());  // "John"
console.log(User.getCount()); // 1
```

### Kế thừa

```kuru
class Admin extends User {
    func constructor(name, email, role) {
        super(name, email);
        this.role = role;
    }
    
    func getRole() {
        return this.role;
    }
    
    // Ghi đè phương thức
    func getName() {
        return `Admin: ${super.getName()}`;
    }
}

let admin = new Admin("Jane", "jane@example.com", "Super Admin");
console.log(admin.getName());  // "Admin: Jane"
console.log(admin.getRole());  // "Super Admin"
```

## Phát triển API Web

### Tạo API cơ bản

```kuru
// app.kuru
import { Server } from "kurumi/server";

let app = new Server();

// Định nghĩa route
app.get("/", (req, res) => {
    return res.send("Hello, World!");
});

app.get("/users", (req, res) => {
    return res.json([
        { id: 1, name: "User 1" },
        { id: 2, name: "User 2" }
    ]);
});

// Khởi động server
app.listen(3000, () => {
    console.log("Server running on port 3000");
});
```

### Sử dụng decorator để định nghĩa API

```kuru
// users.kuru
import { User } from "./models/user.kuru";

@api("/users")
class UserController {
    @get("/")
    async func getUsers(req, res) {
        let users = await User.findAll();
        return res.json(users);
    }
    
    @get("/:id")
    async func getUser(req, res) {
        let user = await User.findById(req.params.id);
        if (!user) {
            return res.status(404).json({ error: "User not found" });
        }
        return res.json(user);
    }
    
    @post("/")
    async func createUser(req, res) {
        let user = new User(req.body);
        await user.save();
        return res.status(201).json(user);
    }
    
    @put("/:id")
    async func updateUser(req, res) {
        let user = await User.findById(req.params.id);
        if (!user) {
            return res.status(404).json({ error: "User not found" });
        }
        
        user.update(req.body);
        await user.save();
        
        return res.json(user);
    }
    
    @delete("/:id")
    async func deleteUser(req, res) {
        let user = await User.findById(req.params.id);
        if (!user) {
            return res.status(404).json({ error: "User not found" });
        }
        
        await user.delete();
        return res.status(204).send();
    }
}

export default UserController;
```

### Middleware

```kuru
// auth.kuru
import { jwt } from "kurumi/jwt";

export func authMiddleware(req, res, next) {
    let token = req.headers.authorization;
    if (!token) {
        return res.status(401).json({ error: "Unauthorized" });
    }
    
    try {
        let decoded = jwt.verify(token, process.env.JWT_SECRET);
        req.user = decoded;
        next();
    } catch (error) {
        return res.status(401).json({ error: "Invalid token" });
    }
}

// Sử dụng middleware
@api("/admin")
class AdminController {
    @get("/dashboard")
    @middleware(authMiddleware)
    func getDashboard(req, res) {
        return res.json({ user: req.user, data: "Dashboard data" });
    }
}
```

## Làm việc với cơ sở dữ liệu

### Kết nối cơ sở dữ liệu

```kuru
// database.kuru
import { Database } from "kurumi/database";

let db = new Database({
    type: "mysql",  // hoặc "postgres", "sqlite", "mongodb"
    host: "localhost",
    port: 3306,
    user: "root",
    password: "password",
    database: "my_app"
});

export default db;
```

### Định nghĩa model

```kuru
// models/user.kuru
import db from "../database.kuru";

class User {
    static table = "users";
    
    func constructor(data) {
        this.id = data.id;
        this.name = data.name;
        this.email = data.email;
        this.created_at = data.created_at || new Date();
    }
    
    static async func findAll() {
        return await db.query(`SELECT * FROM ${this.table}`);
    }
    
    static async func findById(id) {
        let [user] = await db.query(`SELECT * FROM ${this.table} WHERE id = ?`, [id]);
        return user ? new User(user) : null;
    }
    
    async func save() {
        if (this.id) {
            // Cập nhật
            await db.query(
                `UPDATE ${User.table} SET name = ?, email = ? WHERE id = ?`,
                [this.name, this.email, this.id]
            );
        } else {
            // Tạo mới
            let result = await db.query(
                `INSERT INTO ${User.table} (name, email, created_at) VALUES (?, ?, ?)`,
                [this.name, this.email, this.created_at]
            );
            this.id = result.insertId;
        }
        return this;
    }
    
    async func delete() {
        if (!this.id) return false;
        await db.query(`DELETE FROM ${User.table} WHERE id = ?`, [this.id]);
        return true;
    }
    
    func update(data) {
        if (data.name) this.name = data.name;
        if (data.email) this.email = data.email;
    }
}

export default User;
```

## Xử lý lỗi

```kuru
// Xử lý lỗi cơ bản
try {
    // Code có thể gây lỗi
    let result = dangerousOperation();
} catch (error) {
    console.error("Error:", error.message);
} finally {
    // Luôn thực thi
    cleanup();
}

// Xử lý lỗi trong API
@api("/api")
class ErrorHandlingExample {
    @get("/safe")
    func safeEndpoint(req, res) {
        try {
            // Code có thể gây lỗi
            let data = processData(req.query);
            return res.json(data);
        } catch (error) {
            return res.status(500).json({
                error: "Internal Server Error",
                message: error.message
            });
        }
    }
}
```

## Mẹo và thủ thuật

### Destructuring

```kuru
// Destructuring đối tượng
let user = { name: "John", age: 30, email: "john@example.com" };
let { name, age } = user;
console.log(name);  // "John"
console.log(age);   // 30

// Destructuring mảng
let numbers = [1, 2, 3, 4, 5];
let [first, second, ...rest] = numbers;
console.log(first);  // 1
console.log(second); // 2
console.log(rest);   // [3, 4, 5]
```

### Template strings

```kuru
let name = "Kurumi";
let greeting = `Hello, ${name}!`;
console.log(greeting);  // "Hello, Kurumi!"

// Template strings nhiều dòng
let html = `
<div>
    <h1>${name}</h1>
    <p>Welcome to Kurumi!</p>
</div>
`;
```

### Spread operator

```kuru
// Spread với mảng
let arr1 = [1, 2, 3];
let arr2 = [4, 5, 6];
let combined = [...arr1, ...arr2];  // [1, 2, 3, 4, 5, 6]

// Spread với đối tượng
let defaults = { theme: "light", fontSize: 14 };
let userPrefs = { fontSize: 16, showSidebar: true };
let merged = { ...defaults, ...userPrefs };
// { theme: "light", fontSize: 16, showSidebar: true }
```

## Tài liệu tham khảo

- [Trang chủ Kurumi](https://kurumi-lang.org)
- [API Reference](https://kurumi-lang.org/api)
- [Thư viện chuẩn](https://kurumi-lang.org/stdlib)
- [Cộng đồng và hỗ trợ](https://kurumi-lang.org/community)

## Đóng góp

Kurumi là dự án mã nguồn mở. Bạn có thể đóng góp tại [GitHub repository](https://github.com/kurumi-lang/kurumi).

## Giấy phép

Kurumi được phát hành dưới giấy phép MIT.