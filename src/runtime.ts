/**
 * Kurumi Language - Runtime Module
 * 
 * Module này chịu trách nhiệm chạy mã Kurumi đã được biên dịch
 */

import * as fs from 'fs-extra';
import * as path from 'path';
import { compile, compileFile } from './compiler';

/**
 * Chạy mã Kurumi từ chuỗi
 */
export async function run(source: string): Promise<any> {
  try {
    // Biên dịch mã Kurumi thành JavaScript
    const jsCode = compile(source);
    
    // Thực thi mã JavaScript
    const result = eval(jsCode);
    return result;
  } catch (error) {
    throw new Error(`Lỗi chạy mã: ${error.message}`);
  }
}

/**
 * Chạy file Kurumi
 */
export async function runFile(filePath: string): Promise<any> {
  try {
    // Kiểm tra file tồn tại
    if (!fs.existsSync(filePath)) {
      throw new Error(`File không tồn tại: ${filePath}`);
    }
    
    // Biên dịch file Kurumi thành JavaScript
    const jsCode = compileFile(filePath);
    
    // Thực thi mã JavaScript
    const result = eval(jsCode);
    return result;
  } catch (error) {
    throw new Error(`Lỗi chạy file ${filePath}: ${error.message}`);
  }
}