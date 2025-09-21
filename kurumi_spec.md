# Ngôn Ngữ Lập Trình Kurumi 2.0 (.kuru)

## Giới thiệu

Kurumi là một ngôn ngữ lập trình hiện đại được thiết kế để dễ sử dụng hơn Python, đồng thời tích hợp những ưu điểm từ nhiều ngôn ngữ như Rust, Go, TypeScript, Swift và Kotlin. Ngôn ngữ này tập trung vào tính đơn giản, hiệu suất cao, an toàn và khả năng mở rộng, đặc biệt phù hợp cho phát triển API web, ứng dụng di động và trí tuệ nhân tạo.

## Đặc điểm chính

- **Cú pháp siêu đơn giản**: Còn đơn giản hơn Python, loại bỏ các dấu ngoặc không cần thiết
- **Kiểu dữ liệu thông minh**: Hỗ trợ kiểu tĩnh tùy chọn với suy luận kiểu tự động
- **Hướng đối tượng hiện đại**: Kết hợp OOP với lập trình hàm và trait từ Rust
- **Tích hợp đa nền tảng**: Phát triển web, di động, desktop và AI trong cùng một ngôn ngữ
- **Quản lý bộ nhớ thông minh**: Kết hợp thu gom rác với mô hình sở hữu từ Rust
- **Xử lý bất đồng bộ nâng cao**: Hỗ trợ async/await, coroutines và xử lý đồng thời
- **Tích hợp AI**: Hỗ trợ sẵn các thư viện và công cụ cho phát triển AI và ML
- **Tự động tối ưu hóa**: Trình biên dịch thông minh tự động tối ưu code

## Cú pháp cơ bản

### Khai báo biến

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
```

### Hàm

```kuru
# Hàm đơn giản - không cần dấu ngoặc nhọn
def add(a, b)
    return a + b

# Hàm với kiểu dữ liệu
def add(a: int, b: int) -> int
    return a + b

# Hàm một dòng - không cần từ khóa return
def multiply(a, b) => a * b

# Hàm bất đồng bộ
async def fetch_data(url: str) -> dict
    response = await http.get(url)
    return response.json()

# Hàm với tham số mặc định và tham số từ khóa
def greet(name: str = "Guest", title: str = "") => f"Hello, {title} {name}!"

# Gọi hàm với tham số từ khóa
greeting = greet(name="Kurumi", title="Ms.")
```

### Lớp và đối tượng

```kuru
# Định nghĩa lớp - không cần dấu ngoặc nhọn
class User
    # Thuộc tính với kiểu dữ liệu
    name: str
    email: str
    active: bool = true  # Thuộc tính với giá trị mặc định
    
    # Constructor đơn giản
    def __init__(name, email)
        self.name = name
        self.email = email
    
    # Phương thức
    def get_name() -> str
        return self.name
    
    # Phương thức với decorator
    @property
    def email_domain() -> str
        return self.email.split("@")[1]
    
    # Phương thức tĩnh
    @static
    def create(data: dict) -> User
        return User(data.name, data.email)
    
    # Phương thức lớp
    @classmethod
    def from_dict(cls, data: dict) -> User
        return cls(data.name, data.email)

# Tạo đối tượng
user = User("Kurumi", "kurumi@example.com")
print(user.get_name())  # "Kurumi"
print(user.email_domain)  # "example.com"

# Trait (interface) từ Rust
trait Serializable
    def to_json() -> str
    def from_json(data: str) -> Self

# Lớp với trait
class User(Serializable)
    # ... thuộc tính và phương thức
    
    def to_json() -> str
        return json.dumps({"name": self.name, "email": self.email})
    
    def from_json(data: str) -> User
        data_dict = json.loads(data)
        return User(data_dict.name, data_dict.email)
```

### Cấu trúc điều khiển

```kuru
# If-else - không cần dấu ngoặc tròn và ngoặc nhọn
if condition
    # code
elif another_condition
    # code
else
    # code

# If một dòng
if condition => do_something()

# Toán tử điều kiện
result = value_if_true if condition else value_if_false

# Vòng lặp for với range
for i in range(10)
    # code

# Vòng lặp for với step
for i in range(0, 10, 2)  # 0, 2, 4, 6, 8
    # code

# Vòng lặp for-in với dictionary
for key, value in object.items()
    # code

# Vòng lặp for với array
for item in array
    # code

# Vòng lặp for với index
for i, item in enumerate(array)
    # code

# While
while condition
    # code

# Do-while (từ C/C++)
do
    # code
while condition

# Match (từ Rust/Swift) - thay thế switch
match value
    case 1
        # code
    case 2
        # code
    case _  # mặc định
        # code

# Pattern matching (từ Rust/Scala)
match user
    case User(name="Admin", _)
        # code cho admin
    case User(name, email) if email.endswith("@company.com")
        # code cho nhân viên công ty
    case _
        # code cho người dùng khác
```

### API Web và Microservices

```kuru
# Định nghĩa API với decorator đơn giản
@api("/users")
class UserAPI
    # Endpoint GET với validation tự động
    @get("/")
    def get_users(req, res) -> list[User]
        return users  # Tự động chuyển đổi thành JSON
    
    # Endpoint POST với validation tự động
    @post("/")
    @validate  # Tự động kiểm tra dữ liệu đầu vào
    def create_user(req, res) -> User
        user = User(req.body.name, req.body.email)
        users.append(user)
        return user  # Tự động trả về status 201 và JSON
    
    # Endpoint GET với tham số đường dẫn
    @get("/:id")
    def get_user(req, res) -> User?
        user = users.find(u => u.id == req.params.id)
        if not user
            raise NotFoundError("User not found")  # Tự động trả về 404
        return user

# Khởi động server đơn giản
server = Server()
server.add_api(UserAPI)
server.listen(3000)

# GraphQL tích hợp
@graphql
class UserSchema
    @query
    def user(id: str) -> User?
        return users.find(u => u.id == id)
    
    @query
    def users() -> list[User]
        return users
    
    @mutation
    def create_user(name: str, email: str) -> User
        user = User(name, email)
        users.append(user)
        return user

# Microservices với gRPC tích hợp
@service
class UserService
    @rpc
    def get_user(id: str) -> User?
        return users.find(u => u.id == id)
    
    @rpc
    def create_user(name: str, email: str) -> User
        user = User(name, email)
        users.append(user)
        return user

# Serverless Functions
@serverless
def process_payment(payment: Payment) -> PaymentResult
    # Xử lý thanh toán
    return PaymentResult(success=true)
```

### Xử lý lỗi và Ngoại lệ

```kuru
# Try-except đơn giản
try
    # code có thể gây lỗi
except Error as e
    # xử lý lỗi
finally
    # luôn thực thi

# Xử lý nhiều loại lỗi
try
    # code có thể gây lỗi
except DatabaseError as e
    # xử lý lỗi database
except NetworkError as e
    # xử lý lỗi mạng
except
    # xử lý các lỗi khác

# Result type (từ Rust) - xử lý lỗi không dùng ngoại lệ
def divide(a: int, b: int) -> Result[int, DivisionError]
    if b == 0
        return Err(DivisionError("Division by zero"))
    return Ok(a / b)

# Sử dụng Result
result = divide(10, 2)
match result
    case Ok(value)
        print(f"Result: {value}")
    case Err(error)
        print(f"Error: {error.message}")

# Unwrap Result (với xử lý lỗi tự động)
value = divide(10, 2).unwrap_or(0)  # Trả về 0 nếu có lỗi
```

### Module và Import

```kuru
# Xuất module
export def helper()
    # code

export class Helper
    # code

# Import module
from "./helpers.kuru" import helper, Helper
import utils from "./utils.kuru"

# Import có điều kiện (lazy loading)
if condition
    from "./heavy_module.kuru" import HeavyClass
```

### Xử lý đồng thời và Bất đồng bộ

```kuru
# Coroutines và async/await
async def fetch_data(url: str) -> dict
    response = await http.get(url)
    return response.json()

# Parallel processing với Promise.all
async def fetch_all_data(urls: list[str]) -> list[dict]
    promises = [fetch_data(url) for url in urls]
    return await Promise.all(promises)

# Channels (từ Go)
chan = Channel[int](capacity=10)
async def producer()
    for i in range(10)
        await chan.send(i)
    chan.close()

async def consumer()
    async for value in chan
        print(value)

# Worker pools
@worker_pool(size=5)
def process_image(image: Image) -> ProcessedImage
    # xử lý hình ảnh nặng
    return processed_image
```

## Thư viện chuẩn và Tích hợp

Kurumi 2.0 cung cấp các thư viện chuẩn và tích hợp cho:

- **Web và API**: HTTP client/server, GraphQL, WebSockets, gRPC
- **Dữ liệu**: JSON, XML, CSV, Protobuf, YAML
- **Cơ sở dữ liệu**: SQL, NoSQL, ORM, Migrations
- **Bảo mật**: Xác thực, JWT, OAuth, Mã hóa, CSRF
- **AI và ML**: Tích hợp với TensorFlow, PyTorch, Scikit-learn
- **Mobile**: React Native, Flutter bindings
- **DevOps**: Docker, Kubernetes, CI/CD
- **Testing**: Unit, Integration, E2E, Mocking

## Ví dụ hoàn chỉnh

```kuru
// app.kuru
import { Database } from "./database.kuru";
import { User } from "./models/user.kuru";

// Kết nối database
let db = new Database({
    host: "localhost",
    user: "root",
    password: "password",
    database: "kurumi_app"
});

// Định nghĩa API
@api
class App {
    @get("/")
    func home(req, res) {
        return res.send("Welcome to Kurumi API");
    }
    
    @get("/users")
    async func getUsers(req, res) {
        let users = await User.findAll();
        return res.json(users);
    }
    
    @post("/users")
    async func createUser(req, res) {
        try {
            let user = new User(req.body);
            await user.save();
            return res.status(201).json(user);
        } catch (error) {
            return res.status(400).json({error: error.message});
        }
    }
}

// Khởi động server
let app = new App();
app.listen(3000, () => {
    console.log("Server running on port 3000");
});
```