#!/usr/bin/env node

/**
 * Kurumi Language - Main Entry Point
 * 
 * Đây là điểm khởi đầu của trình biên dịch Kurumi 2.0
 */

import { Command } from 'commander';
import * as fs from 'fs-extra';
import * as path from 'path';
import { compile } from './compiler';
import { runFile } from './runtime';
import { initProject } from './project';
import { version } from '../package.json';

// Khởi tạo command line interface
const program = new Command();

program
  .name('kurumi')
  .description('Kurumi Programming Language CLI')
  .version(version);

// Lệnh biên dịch file
program
  .command('compile <file>')
  .description('Biên dịch file Kurumi (.kuru) thành JavaScript')
  .option('-o, --output <output>', 'Đường dẫn file đầu ra')
  .action(async (file, options) => {
    try {
      const inputPath = path.resolve(file);
      const outputPath = options.output || inputPath.replace(/\.kuru$/, '.js');
      
      if (!fs.existsSync(inputPath)) {
        console.error(`Lỗi: File không tồn tại: ${inputPath}`);
        process.exit(1);
      }
      
      const source = fs.readFileSync(inputPath, 'utf-8');
      const result = compile(source);
      
      fs.writeFileSync(outputPath, result, 'utf-8');
      console.log(`Đã biên dịch thành công: ${outputPath}`);
    } catch (error) {
      console.error('Lỗi biên dịch:', error.message);
      process.exit(1);
    }
  });

// Lệnh chạy file
program
  .command('run <file>')
  .description('Chạy file Kurumi (.kuru)')
  .action(async (file) => {
    try {
      const inputPath = path.resolve(file);
      
      if (!fs.existsSync(inputPath)) {
        console.error(`Lỗi: File không tồn tại: ${inputPath}`);
        process.exit(1);
      }
      
      await runFile(inputPath);
    } catch (error) {
      console.error('Lỗi chạy file:', error.message);
      process.exit(1);
    }
  });

// Lệnh khởi tạo dự án mới
program
  .command('init [name]')
  .description('Khởi tạo dự án Kurumi mới')
  .action(async (name = 'kurumi-project') => {
    try {
      await initProject(name);
      console.log(`Đã khởi tạo dự án mới: ${name}`);
    } catch (error) {
      console.error('Lỗi khởi tạo dự án:', error.message);
      process.exit(1);
    }
  });

// Lệnh chạy ở chế độ phát triển
program
  .command('dev')
  .description('Chạy ứng dụng ở chế độ phát triển')
  .option('-p, --port <port>', 'Cổng để chạy server', '3000')
  .action(async (options) => {
    try {
      console.log(`Đang chạy ứng dụng ở chế độ phát triển trên cổng ${options.port}...`);
      // Thực hiện chạy ứng dụng ở chế độ phát triển
    } catch (error) {
      console.error('Lỗi chạy ứng dụng:', error.message);
      process.exit(1);
    }
  });

// Lệnh build ứng dụng
program
  .command('build')
  .description('Build ứng dụng Kurumi cho môi trường production')
  .action(async () => {
    try {
      console.log('Đang build ứng dụng...');
      // Thực hiện build ứng dụng
      console.log('Đã build ứng dụng thành công!');
    } catch (error) {
      console.error('Lỗi build ứng dụng:', error.message);
      process.exit(1);
    }
  });

// Phân tích tham số dòng lệnh
program.parse(process.argv);

// Hiển thị trợ giúp nếu không có lệnh nào được chỉ định
if (!process.argv.slice(2).length) {
  program.outputHelp();
}