/**
 * Script publish cho Kurumi Language
 */

const { execSync } = require('child_process');
const fs = require('fs-extra');
const path = require('path');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Đường dẫn thư mục gốc
const rootDir = path.resolve(__dirname, '..');

// Đọc phiên bản hiện tại từ package.json
const packageJson = require(path.join(rootDir, 'package.json'));
const currentVersion = packageJson.version;

console.log(`Phiên bản hiện tại: ${currentVersion}`);

// Hỏi người dùng về loại phiên bản cần tăng
rl.question('Loại phiên bản cần tăng (patch/minor/major): ', (versionType) => {
  if (!['patch', 'minor', 'major'].includes(versionType)) {
    console.error('Loại phiên bản không hợp lệ. Vui lòng chọn patch, minor hoặc major.');
    rl.close();
    process.exit(1);
  }

  try {
    // Chạy script build
    console.log('Đang build package...');
    execSync('node scripts/build.js', { stdio: 'inherit', cwd: rootDir });

    // Tăng phiên bản
    console.log(`Đang tăng phiên bản ${versionType}...`);
    execSync(`npm version ${versionType} --no-git-tag-version`, { stdio: 'inherit', cwd: rootDir });

    // Đọc phiên bản mới
    const updatedPackageJson = JSON.parse(fs.readFileSync(path.join(rootDir, 'package.json'), 'utf-8'));
    const newVersion = updatedPackageJson.version;
    console.log(`Phiên bản mới: ${newVersion}`);

    // Hỏi người dùng có muốn publish không
    rl.question('Bạn có muốn publish lên npm không? (y/n): ', (answer) => {
      if (answer.toLowerCase() === 'y') {
        console.log('Đang publish lên npm...');
        execSync('npm publish', { stdio: 'inherit', cwd: rootDir });
        console.log(`Đã publish kurumi-lang phiên bản ${newVersion} lên npm!`);
      } else {
        console.log('Đã hủy publish.');
      }
      rl.close();
    });
  } catch (error) {
    console.error('Lỗi trong quá trình publish:', error);
    rl.close();
    process.exit(1);
  }
});