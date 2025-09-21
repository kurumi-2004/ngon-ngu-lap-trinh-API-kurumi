# Hướng dẫn cài đặt Kurumi

Kurumi có thể được cài đặt thông qua npm (Node.js) hoặc pip (Python), tùy theo môi trường bạn đang sử dụng.

## Cài đặt thông qua npm (Node.js)

### Cài đặt toàn cục

```bash
npm install -g kurumi-lang
```

### Sử dụng với npx

```bash
npx kurumi init my-project
npx kurumi run app.kuru
```

## Cài đặt thông qua pip (Python)

### Cài đặt toàn cục

```bash
pip install kurumi-lang
```

### Sử dụng

```bash
kurumi init my-project
kurumi run app.kuru
```

## Lệnh cơ bản

Kurumi cung cấp các lệnh sau:

- `kurumi init <tên-dự-án>`: Tạo dự án Kurumi mới
- `kurumi run <file>`: Chạy file Kurumi
- `kurumi dev`: Chạy ứng dụng ở chế độ phát triển
- `kurumi build`: Biên dịch ứng dụng

## Yêu cầu hệ thống

### Cho phiên bản npm:
- Node.js >= 14.0.0
- npm >= 6.0.0

### Cho phiên bản pip:
- Python >= 3.6
- pip >= 20.0.0