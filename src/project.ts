/**
 * Kurumi Language - Project Module
 * 
 * Module này chịu trách nhiệm khởi tạo và quản lý dự án Kurumi
 */

import * as fs from 'fs-extra';
import * as path from 'path';

// Cấu trúc thư mục dự án mặc định
const PROJECT_STRUCTURE = {
  'src': {
    'app.kuru': `# Ứng dụng Kurumi
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
`,
    'models': {
      '.gitkeep': ''
    },
    'controllers': {
      '.gitkeep': ''
    },
    'services': {
      '.gitkeep': ''
    }
  },
  'tests': {
    '.gitkeep': ''
  },
  'kurumi.config.json': JSON.stringify({
    "name": "kurumi-project",
    "version": "1.0.0",
    "port": 3000,
    "database": {
      "type": "sqlite",
      "file": "database.sqlite"
    }
  }, null, 2),
  'package.json': JSON.stringify({
    "name": "kurumi-project",
    "version": "1.0.0",
    "description": "Dự án Kurumi mới",
    "main": "src/app.kuru",
    "scripts": {
      "start": "kurumi run src/app.kuru",
      "dev": "kurumi dev",
      "build": "kurumi build"
    },
    "dependencies": {
      "kurumi-lang": "^2.0.0"
    }
  }, null, 2),
  'README.md': `# Dự án Kurumi

Dự án này được tạo bằng ngôn ngữ lập trình Kurumi 2.0.

## Cài đặt

\`\`\`bash
npm install
\`\`\`

## Chạy ứng dụng

\`\`\`bash
# Chế độ phát triển
npm run dev

# Chế độ sản phẩm
npm run build
npm start
\`\`\`
`
};

/**
 * Tạo cấu trúc thư mục và file
 */
function createDirectoryStructure(basePath: string, structure: any) {
  for (const [name, content] of Object.entries(structure)) {
    const itemPath = path.join(basePath, name);
    
    if (typeof content === 'object') {
      // Tạo thư mục
      fs.mkdirSync(itemPath, { recursive: true });
      // Tạo cấu trúc bên trong thư mục
      createDirectoryStructure(itemPath, content);
    } else {
      // Tạo file với nội dung
      fs.writeFileSync(itemPath, content);
    }
  }
}

/**
 * Khởi tạo dự án Kurumi mới
 */
export async function initProject(projectName: string): Promise<void> {
  try {
    const projectPath = path.resolve(projectName);
    
    // Kiểm tra thư mục đã tồn tại chưa
    if (fs.existsSync(projectPath)) {
      const stats = fs.statSync(projectPath);
      
      if (stats.isDirectory()) {
        const files = fs.readdirSync(projectPath);
        
        if (files.length > 0) {
          throw new Error(`Thư mục ${projectPath} đã tồn tại và không trống.`);
        }
      } else {
        throw new Error(`${projectPath} đã tồn tại nhưng không phải là thư mục.`);
      }
    } else {
      // Tạo thư mục dự án
      fs.mkdirSync(projectPath, { recursive: true });
    }
    
    // Tạo cấu trúc dự án
    createDirectoryStructure(projectPath, PROJECT_STRUCTURE);
    
    // Cập nhật tên dự án trong package.json
    const packageJsonPath = path.join(projectPath, 'package.json');
    const packageJson = JSON.parse(fs.readFileSync(packageJsonPath, 'utf-8'));
    packageJson.name = path.basename(projectName);
    fs.writeFileSync(packageJsonPath, JSON.stringify(packageJson, null, 2));
    
    // Cập nhật tên dự án trong kurumi.config.json
    const configPath = path.join(projectPath, 'kurumi.config.json');
    const config = JSON.parse(fs.readFileSync(configPath, 'utf-8'));
    config.name = path.basename(projectName);
    fs.writeFileSync(configPath, JSON.stringify(config, null, 2));
    
    console.log(`Đã khởi tạo dự án Kurumi tại ${projectPath}`);
  } catch (error) {
    throw new Error(`Lỗi khởi tạo dự án: ${error.message}`);
  }
}