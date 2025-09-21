#!/usr/bin/env python
"""
Kurumi Language - Command Line Interface
"""

import os
import sys
import click
import shutil
import subprocess

@click.group()
def main():
    """Kurumi - Ngôn ngữ lập trình API hiện đại"""
    pass

@main.command()
@click.argument('file', type=click.Path(exists=True))
def run(file):
    """Chạy file Kurumi"""
    click.echo(f"Đang chạy file {file}...")
    # Sử dụng kurumi_parser.py để chạy file
    kurumi_parser = os.path.join(os.path.dirname(__file__), 'kurumi_parser.py')
    subprocess.run([sys.executable, kurumi_parser, file])

@main.command()
@click.argument('name')
def init(name):
    """Khởi tạo dự án Kurumi mới"""
    click.echo(f"Đang khởi tạo dự án Kurumi mới: {name}...")
    
    # Tạo cấu trúc thư mục
    os.makedirs(os.path.join(name, 'src'), exist_ok=True)
    os.makedirs(os.path.join(name, 'tests'), exist_ok=True)
    
    # Tạo file mẫu
    with open(os.path.join(name, 'src', 'app.kuru'), 'w', encoding='utf-8') as f:
        f.write("""# Ứng dụng Kurumi
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
""")
    
    # Tạo file README.md
    with open(os.path.join(name, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(f"""# {name}

Dự án được tạo bằng ngôn ngữ lập trình Kurumi.

## Cài đặt

```bash
pip install -r requirements.txt
```

## Chạy ứng dụng

```bash
kurumi run src/app.kuru
```
""")
    
    # Tạo file requirements.txt
    with open(os.path.join(name, 'requirements.txt'), 'w', encoding='utf-8') as f:
        f.write("kurumi-lang>=2.0.0\n")
    
    click.echo(f"Đã khởi tạo dự án Kurumi tại {name}")

@main.command()
def dev():
    """Chạy ứng dụng ở chế độ phát triển"""
    click.echo("Đang chạy ứng dụng ở chế độ phát triển...")
    # Tìm file app.kuru
    if os.path.exists('src/app.kuru'):
        run('src/app.kuru')
    else:
        click.echo("Không tìm thấy file src/app.kuru")

@main.command()
@click.argument('file', type=click.Path(exists=True))
def build(file):
    """Biên dịch file Kurumi thành JavaScript"""
    click.echo(f"Đang biên dịch file {file}...")
    # Sử dụng kurumi_parser.py để biên dịch file
    kurumi_parser = os.path.join(os.path.dirname(__file__), 'kurumi_parser.py')
    subprocess.run([sys.executable, kurumi_parser, file, '--build'])

if __name__ == '__main__':
    main()