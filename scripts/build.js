/**
 * Script build cho Kurumi Language
 */

const { execSync } = require('child_process');
const fs = require('fs-extra');
const path = require('path');

// Đường dẫn thư mục gốc
const rootDir = path.resolve(__dirname, '..');
const distDir = path.join(rootDir, 'dist');

// Xóa thư mục dist nếu tồn tại
if (fs.existsSync(distDir)) {
  console.log('Đang xóa thư mục dist...');
  fs.removeSync(distDir);
}

// Tạo thư mục dist
fs.mkdirSync(distDir, { recursive: true });

try {
  // Biên dịch TypeScript
  console.log('Đang biên dịch TypeScript...');
  execSync('npx tsc', { stdio: 'inherit', cwd: rootDir });

  // Sao chép các file Python
  console.log('Đang sao chép kurumi_parser.py...');
  fs.copyFileSync(
    path.join(rootDir, 'kurumi_parser.py'),
    path.join(distDir, 'kurumi_parser.py')
  );

  // Sao chép các file tài liệu
  console.log('Đang sao chép tài liệu...');
  fs.copyFileSync(
    path.join(rootDir, 'kurumi_spec.md'),
    path.join(distDir, 'kurumi_spec.md')
  );
  fs.copyFileSync(
    path.join(rootDir, 'kurumi_guide.md'),
    path.join(distDir, 'kurumi_guide.md')
  );

  // Sao chép ví dụ
  console.log('Đang sao chép ví dụ...');
  fs.copyFileSync(
    path.join(rootDir, 'example_api.kuru'),
    path.join(distDir, 'example_api.kuru')
  );

  console.log('Build hoàn tất!');
} catch (error) {
  console.error('Lỗi trong quá trình build:', error);
  process.exit(1);
}