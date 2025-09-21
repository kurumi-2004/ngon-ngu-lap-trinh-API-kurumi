

import re
import sys
import json
from enum import Enum

class TokenType(Enum):
    KEYWORD = 'KEYWORD'
    IDENTIFIER = 'IDENTIFIER'
    STRING = 'STRING'
    NUMBER = 'NUMBER'
    OPERATOR = 'OPERATOR'
    PUNCTUATION = 'PUNCTUATION'
    DECORATOR = 'DECORATOR'
    COMMENT = 'COMMENT'
    WHITESPACE = 'WHITESPACE'
    EOF = 'EOF'

class Token:
    def __init__(self, type, value, line, column):
        self.type = type
        self.value = value
        self.line = line
        self.column = column
    
    def __repr__(self):
        return f"Token({self.type}, '{self.value}', {self.line}, {self.column})"

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.line = 1
        self.column = 1
        self.current_char = self.source_code[0] if self.source_code else None
        
        # Định nghĩa từ khóa
        self.keywords = {
            'func', 'class', 'let', 'const', 'var', 'if', 'else', 'for', 'while', 
            'return', 'import', 'export', 'from', 'new', 'this', 'static', 'async', 
            'await', 'try', 'catch', 'finally', 'switch', 'case', 'default', 'break',
            'continue', 'in', 'of'
        }
        
        # Định nghĩa toán tử
        self.operators = {
            '+', '-', '*', '/', '%', '=', '==', '!=', '>', '<', '>=', '<=', 
            '&&', '||', '!', '++', '--', '+=', '-=', '*=', '/=', '%=', '=>'
        }
        
        # Định nghĩa dấu câu
        self.punctuation = {
            '(', ')', '{', '}', '[', ']', ';', ',', '.', ':', '?'
        }
    
    def advance(self):
        self.position += 1
        if self.position >= len(self.source_code):
            self.current_char = None
        else:
            self.current_char = self.source_code[self.position]
            if self.current_char == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
    
    def peek(self, n=1):
        peek_pos = self.position + n
        if peek_pos >= len(self.source_code):
            return None
        return self.source_code[peek_pos]
    
    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()
    
    def skip_comment(self):
        # Bỏ qua comment dạng //
        if self.current_char == '/' and self.peek() == '/':
            while self.current_char and self.current_char != '\n':
                self.advance()
            return True
        
        # Bỏ qua comment dạng /* */
        if self.current_char == '/' and self.peek() == '*':
            self.advance()  # Bỏ qua /
            self.advance()  # Bỏ qua *
            
            while self.current_char:
                if self.current_char == '*' and self.peek() == '/':
                    self.advance()  # Bỏ qua *
                    self.advance()  # Bỏ qua /
                    return True
                self.advance()
            
            # Lỗi nếu comment không được đóng
            raise Exception("Unclosed comment")
        
        return False
    
    def get_identifier(self):
        start_column = self.column
        result = ''
        
        while self.current_char and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        
        if result in self.keywords:
            return Token(TokenType.KEYWORD, result, self.line, start_column)
        else:
            return Token(TokenType.IDENTIFIER, result, self.line, start_column)
    
    def get_number(self):
        start_column = self.column
        result = ''
        has_dot = False
        
        while self.current_char and (self.current_char.isdigit() or self.current_char == '.'):
            if self.current_char == '.':
                if has_dot:
                    break
                has_dot = True
            
            result += self.current_char
            self.advance()
        
        if has_dot:
            return Token(TokenType.NUMBER, float(result), self.line, start_column)
        else:
            return Token(TokenType.NUMBER, int(result), self.line, start_column)
    
    def get_string(self):
        start_column = self.column
        quote_char = self.current_char  # ' or "
        self.advance()  # Bỏ qua dấu nháy đầu tiên
        
        result = ''
        while self.current_char and self.current_char != quote_char:
            if self.current_char == '\\':
                self.advance()
                if self.current_char == 'n':
                    result += '\n'
                elif self.current_char == 't':
                    result += '\t'
                elif self.current_char == 'r':
                    result += '\r'
                elif self.current_char == '\\':
                    result += '\\'
                elif self.current_char == quote_char:
                    result += quote_char
                else:
                    result += '\\' + self.current_char
            else:
                result += self.current_char
            
            self.advance()
        
        if not self.current_char:
            raise Exception(f"Unclosed string literal at line {self.line}")
        
        self.advance()  # Bỏ qua dấu nháy cuối cùng
        return Token(TokenType.STRING, result, self.line, start_column)
    
    def get_operator(self):
        start_column = self.column
        result = self.current_char
        self.advance()
        
        # Kiểm tra toán tử 2 ký tự
        if result + self.current_char in self.operators:
            result += self.current_char
            self.advance()
        
        return Token(TokenType.OPERATOR, result, self.line, start_column)
    
    def get_decorator(self):
        start_column = self.column
        self.advance()  # Bỏ qua @
        
        result = '@'
        while self.current_char and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        
        return Token(TokenType.DECORATOR, result, self.line, start_column)
    
    def get_next_token(self):
        while self.current_char:
            # Bỏ qua khoảng trắng
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            
            # Bỏ qua comment
            if self.current_char == '/' and (self.peek() == '/' or self.peek() == '*'):
                if self.skip_comment():
                    continue
            
            # Xử lý decorator
            if self.current_char == '@':
                return self.get_decorator()
            
            # Xử lý identifier
            if self.current_char.isalpha() or self.current_char == '_':
                return self.get_identifier()
            
            # Xử lý số
            if self.current_char.isdigit():
                return self.get_number()
            
            # Xử lý chuỗi
            if self.current_char in ('"', "'"):
                return self.get_string()
            
            # Xử lý toán tử
            if self.current_char in '+-*/%=!><&|':
                return self.get_operator()
            
            # Xử lý dấu câu
            if self.current_char in self.punctuation:
                token = Token(TokenType.PUNCTUATION, self.current_char, self.line, self.column)
                self.advance()
                return token
            
            # Ký tự không hợp lệ
            raise Exception(f"Invalid character '{self.current_char}' at line {self.line}, column {self.column}")
        
        # Kết thúc file
        return Token(TokenType.EOF, None, self.line, self.column)
    
    def tokenize(self):
        tokens = []
        while True:
            token = self.get_next_token()
            tokens.append(token)
            if token.type == TokenType.EOF:
                break
        return tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
        self.current_token = self.tokens[0] if self.tokens else None
    
    def advance(self):
        self.position += 1
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
        else:
            self.current_token = None
    
    def parse(self):
        """
        Phân tích cú pháp toàn bộ chương trình
        """
        program = {
            'type': 'Program',
            'body': []
        }
        
        while self.current_token and self.current_token.type != TokenType.EOF:
            statement = self.parse_statement()
            if statement:
                program['body'].append(statement)
        
        return program
    
    def parse_statement(self):
        """
        Phân tích một câu lệnh
        """
        if not self.current_token:
            return None
        
        # Import statement
        if self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'import':
            return self.parse_import_statement()
        
        # Export statement
        if self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'export':
            return self.parse_export_statement()
        
        # Class declaration
        if self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'class':
            return self.parse_class_declaration()
        
        # Function declaration
        if self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'func':
            return self.parse_function_declaration()
        
        # Variable declaration
        if self.current_token.type == TokenType.KEYWORD and self.current_token.value in ('let', 'const', 'var'):
            return self.parse_variable_declaration()
        
        # Decorator
        if self.current_token.type == TokenType.DECORATOR:
            return self.parse_decorated_statement()
        
        # Expression statement
        return self.parse_expression_statement()
    
    def parse_import_statement(self):
        # Đơn giản hóa: chỉ xử lý cú pháp cơ bản
        token = self.current_token
        self.advance()  # Bỏ qua 'import'
        
        # Lấy tên module
        if self.current_token.type != TokenType.IDENTIFIER and self.current_token.type != TokenType.PUNCTUATION:
            raise Exception(f"Expected identifier or {{ after import at line {token.line}")
        
        # Đơn giản hóa: bỏ qua chi tiết import
        while self.current_token and self.current_token.value != ';':
            self.advance()
        
        if self.current_token and self.current_token.value == ';':
            self.advance()  # Bỏ qua ';'
        
        return {
            'type': 'ImportStatement',
            'line': token.line
        }
    
    def parse_export_statement(self):
        # Đơn giản hóa: chỉ xử lý cú pháp cơ bản
        token = self.current_token
        self.advance()  # Bỏ qua 'export'
        
        # Phân tích statement sau export
        statement = self.parse_statement()
        
        return {
            'type': 'ExportStatement',
            'declaration': statement,
            'line': token.line
        }
    
    def parse_class_declaration(self):
        token = self.current_token
        self.advance()  # Bỏ qua 'class'
        
        # Lấy tên lớp
        if self.current_token.type != TokenType.IDENTIFIER:
            raise Exception(f"Expected class name at line {token.line}")
        
        class_name = self.current_token.value
        self.advance()  # Bỏ qua tên lớp
        
        # Kiểm tra kế thừa
        parent = None
        if self.current_token and self.current_token.value == 'extends':
            self.advance()  # Bỏ qua 'extends'
            
            if self.current_token.type != TokenType.IDENTIFIER:
                raise Exception(f"Expected parent class name at line {token.line}")
            
            parent = self.current_token.value
            self.advance()  # Bỏ qua tên lớp cha
        
        # Kiểm tra dấu {
        if not self.current_token or self.current_token.value != '{':
            raise Exception(f"Expected {{ after class declaration at line {token.line}")
        
        self.advance()  # Bỏ qua '{'
        
        # Phân tích thân lớp
        body = []
        while self.current_token and self.current_token.value != '}':
            method = self.parse_class_member()
            if method:
                body.append(method)
        
        # Kiểm tra dấu }
        if not self.current_token or self.current_token.value != '}':
            raise Exception(f"Expected }} after class body at line {token.line}")
        
        self.advance()  # Bỏ qua '}'
        
        return {
            'type': 'ClassDeclaration',
            'name': class_name,
            'parent': parent,
            'body': body,
            'line': token.line
        }
    
    def parse_class_member(self):
        # Kiểm tra static
        is_static = False
        if self.current_token and self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'static':
            is_static = True
            self.advance()  # Bỏ qua 'static'
        
        # Kiểm tra func
        if self.current_token and self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'func':
            method = self.parse_function_declaration()
            method['static'] = is_static
            return method
        
        # Thuộc tính
        if self.current_token and self.current_token.type == TokenType.IDENTIFIER:
            property_name = self.current_token.value
            line = self.current_token.line
            self.advance()  # Bỏ qua tên thuộc tính
            
            # Kiểm tra dấu =
            if not self.current_token or self.current_token.value != '=':
                raise Exception(f"Expected = after property name at line {line}")
            
            self.advance()  # Bỏ qua '='
            
            # Phân tích giá trị
            value = self.parse_expression()
            
            # Kiểm tra dấu ;
            if self.current_token and self.current_token.value == ';':
                self.advance()  # Bỏ qua ';'
            
            return {
                'type': 'PropertyDefinition',
                'name': property_name,
                'value': value,
                'static': is_static,
                'line': line
            }
        
        # Bỏ qua thành phần không xác định
        self.advance()
        return None
    
    def parse_function_declaration(self):
        token = self.current_token
        self.advance()  # Bỏ qua 'func'
        
        # Lấy tên hàm
        if self.current_token.type != TokenType.IDENTIFIER:
            raise Exception(f"Expected function name at line {token.line}")
        
        func_name = self.current_token.value
        self.advance()  # Bỏ qua tên hàm
        
        # Kiểm tra dấu (
        if not self.current_token or self.current_token.value != '(':
            raise Exception(f"Expected ( after function name at line {token.line}")
        
        self.advance()  # Bỏ qua '('
        
        # Phân tích tham số
        params = []
        while self.current_token and self.current_token.value != ')':
            if self.current_token.type == TokenType.IDENTIFIER:
                params.append(self.current_token.value)
                self.advance()  # Bỏ qua tên tham số
                
                # Kiểm tra dấu ,
                if self.current_token and self.current_token.value == ',':
                    self.advance()  # Bỏ qua ','
            else:
                self.advance()  # Bỏ qua token không xác định
        
        # Kiểm tra dấu )
        if not self.current_token or self.current_token.value != ')':
            raise Exception(f"Expected ) after function parameters at line {token.line}")
        
        self.advance()  # Bỏ qua ')'
        
        # Kiểm tra dấu {
        if not self.current_token or self.current_token.value != '{':
            raise Exception(f"Expected {{ after function declaration at line {token.line}")
        
        self.advance()  # Bỏ qua '{'
        
        # Phân tích thân hàm (đơn giản hóa)
        body = []
        while self.current_token and self.current_token.value != '}':
            statement = self.parse_statement()
            if statement:
                body.append(statement)
        
        # Kiểm tra dấu }
        if not self.current_token or self.current_token.value != '}':
            raise Exception(f"Expected }} after function body at line {token.line}")
        
        self.advance()  # Bỏ qua '}'
        
        return {
            'type': 'FunctionDeclaration',
            'name': func_name,
            'params': params,
            'body': body,
            'line': token.line
        }
    
    def parse_variable_declaration(self):
        token = self.current_token
        kind = self.current_token.value  # let, const, var
        self.advance()  # Bỏ qua từ khóa
        
        # Lấy tên biến
        if self.current_token.type != TokenType.IDENTIFIER:
            raise Exception(f"Expected variable name at line {token.line}")
        
        var_name = self.current_token.value
        self.advance()  # Bỏ qua tên biến
        
        # Kiểm tra dấu =
        if not self.current_token or self.current_token.value != '=':
            raise Exception(f"Expected = after variable name at line {token.line}")
        
        self.advance()  # Bỏ qua '='
        
        # Phân tích giá trị
        value = self.parse_expression()
        
        # Kiểm tra dấu ;
        if self.current_token and self.current_token.value == ';':
            self.advance()  # Bỏ qua ';'
        
        return {
            'type': 'VariableDeclaration',
            'kind': kind,
            'name': var_name,
            'value': value,
            'line': token.line
        }
    
    def parse_decorated_statement(self):
        decorators = []
        
        # Thu thập tất cả decorator
        while self.current_token and self.current_token.type == TokenType.DECORATOR:
            decorators.append(self.current_token.value)
            self.advance()  # Bỏ qua decorator
        
        # Phân tích statement được trang trí
        statement = self.parse_statement()
        
        if statement:
            statement['decorators'] = decorators
        
        return statement
    
    def parse_expression_statement(self):
        expression = self.parse_expression()
        
        # Kiểm tra dấu ;
        if self.current_token and self.current_token.value == ';':
            self.advance()  # Bỏ qua ';'
        
        return {
            'type': 'ExpressionStatement',
            'expression': expression
        }
    
    def parse_expression(self):
        # Đơn giản hóa: chỉ xử lý các biểu thức cơ bản
        if not self.current_token:
            return None
        
        # Literal
        if self.current_token.type in (TokenType.STRING, TokenType.NUMBER):
            value = self.current_token.value
            line = self.current_token.line
            self.advance()
            
            return {
                'type': 'Literal',
                'value': value,
                'line': line
            }
        
        # Identifier
        if self.current_token.type == TokenType.IDENTIFIER:
            name = self.current_token.value
            line = self.current_token.line
            self.advance()
            
            return {
                'type': 'Identifier',
                'name': name,
                'line': line
            }
        
        # Đơn giản hóa: bỏ qua các biểu thức phức tạp
        self.advance()
        return {
            'type': 'Expression',
            'value': 'simplified'
        }

def parse_kurumi_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            source_code = file.read()
        
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        
        parser = Parser(tokens)
        ast = parser.parse()
        
        return ast
    except Exception as e:
        print(f"Error parsing {file_path}: {str(e)}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python kurumi_parser.py <file.kuru>")
        return
    
    file_path = sys.argv[1]
    ast = parse_kurumi_file(file_path)
    
    if ast:
        print(json.dumps(ast, indent=2))

if __name__ == "__main__":
    main()