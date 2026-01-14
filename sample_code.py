"""
Vulnerable Python Application - DO NOT USE IN PRODUCTION
This code contains intentional security vulnerabilities for testing Qwiet.AI scanner
All code is executable without external dependencies
"""

import os
import sys
import sqlite3
import subprocess
import pickle
import hashlib
import re

"""
Vulnerable Python Application - DO NOT USE IN PRODUCTION
This code contains intentional security vulnerabilities for testing Qwiet.AI scanner
All code is executable without external dependencies
"""

import os
import sys
import sqlite3
import subprocess
import pickle
import hashlib
import re


# VULNERABILITY 1: Hardcoded Secrets
DATABASE_PASSWORD = "MySecretPassword123!"
API_KEY = "sk-1234567890abcdef1234567890abcdef"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
STRIPE_SECRET = "sk_live_51HqT2pKqR3F4kE5L2n3M4p5Q6r7S8t9U0v1W2x3Y4z"
GITHUB_TOKEN = "ghp_1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnop"


# VULNERABILITY 2: SQL Injection with clear data flow
def get_user_by_name(username):
    """SQL Injection: user input directly in query"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Direct string concatenation - SQL Injection
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()


# VULNERABILITY 3: SQL Injection with format string
def authenticate_user(user, password):
    """SQL Injection via format string"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Format string injection
    sql = f"SELECT * FROM users WHERE username='{user}' AND password='{password}'"
    cursor.execute(sql)
    return cursor.fetchone()


# VULNERABILITY 4: SQL Injection with % operator
def find_user_by_email(email):
    """SQL Injection via % formatting"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE email = '%s'" % email
    cursor.execute(query)
    return cursor.fetchall()


# VULNERABILITY 5: Command Injection via os.system
def ping_host(host):
    """Command injection through os.system"""
    # Command injection - user input directly in system call
    result = os.system(f"ping -n 1 {host}")
    return result


# VULNERABILITY 6: Command Injection via subprocess with shell=True
def backup_file(filename):
    """Command injection via subprocess"""
    # Command injection with shell=True
    subprocess.call(f"copy {filename} backup.txt", shell=True)
    return "Backup created"


# VULNERABILITY 7: Command Injection with Popen
def list_directory(path):
    """Command injection via Popen"""
    # User input in shell command
    process = subprocess.Popen(f"dir {path}", shell=True, stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode()


# VULNERABILITY 8: Path Traversal - reading files
def read_log_file(filename):
    """Path traversal vulnerability"""
    # No validation on filename - allows ../../../etc/passwd
    log_path = f"C:\\logs\\{filename}"
    with open(log_path, 'r') as f:
        return f.read()


# VULNERABILITY 9: Path Traversal with open()
def get_file_contents(filepath):
    """Direct file access without validation"""
    # User-controlled path
    content = open(filepath).read()
    return content


# VULNERABILITY 10: Insecure Deserialization
def load_user_session(session_data):
    """Insecure pickle deserialization"""
    # Deserializing untrusted data with pickle
    user_obj = pickle.loads(session_data)
    return user_obj


# VULNERABILITY 11: Weak Cryptography - MD5 for passwords
def hash_password_md5(password):
    """Using MD5 for password hashing"""
    # MD5 is cryptographically broken
    return hashlib.md5(password.encode()).hexdigest()


# VULNERABILITY 12: Weak Cryptography - SHA1
def create_password_hash(password):
    """Using SHA1 for passwords"""
    # SHA1 is deprecated for security purposes
    return hashlib.sha1(password.encode()).hexdigest()


# VULNERABILITY 13: Use of eval() with user input
def calculate_expression(expr):
    """Code injection via eval"""
    # Arbitrary code execution
    result = eval(expr)
    return result


# VULNERABILITY 14: Use of exec()
def execute_user_code(code_string):
    """Code injection via exec"""
    # Executing arbitrary Python code
    exec(code_string)


# VULNERABILITY 15: Use of compile() and exec()
def run_dynamic_code(source):
    """Dynamic code execution"""
    code_obj = compile(source, '<string>', 'exec')
    exec(code_obj)


# VULNERABILITY 16: OS Command via os.popen
def execute_command(cmd):
    """Command execution via popen"""
    # User input directly in popen
    stream = os.popen(cmd)
    return stream.read()


# VULNERABILITY 17: Information Disclosure - printing stack trace
def process_data(data):
    """Exposing sensitive error information"""
    try:
        result = 1 / int(data)
        return result
    except Exception as e:
        # Exposing full exception details
        print(f"Error: {e}")
        print(f"Type: {type(e)}")
        print(f"Args: {e.args}")
        import traceback
        traceback.print_exc()
        return None


# VULNERABILITY 18: Insecure Random for security tokens
import random

def generate_session_token():
    """Using weak random for security token"""
    # Predictable random for security-critical operation
    return random.randint(10000000, 99999999)


def generate_password_reset_token():
    """Weak random for password reset"""
    return random.randrange(1000000)


# VULNERABILITY 19: Timing Attack in password comparison
def verify_password(stored_pass, provided_pass):
    """Timing attack vulnerability"""
    # Character-by-character comparison leaks information
    if len(stored_pass) != len(provided_pass):
        return False
    for i in range(len(stored_pass)):
        if stored_pass[i] != provided_pass[i]:
            return False
    return True


# VULNERABILITY 20: Regular Expression Denial of Service (ReDoS)
def validate_email(email):
    """ReDoS vulnerability"""
    # Catastrophic backtracking pattern
    pattern = r'^([a-zA-Z0-9]+)+@[a-zA-Z0-9]+\.[a-zA-Z]+$'
    return re.match(pattern, email) is not None


# VULNERABILITY 21: XML External Entity (XXE)
import xml.etree.ElementTree as ET

def parse_xml_data(xml_string):
    """XXE vulnerability"""
    # Parsing untrusted XML without disabling external entities
    root = ET.fromstring(xml_string)
    return ET.tostring(root)


# VULNERABILITY 22: YAML Deserialization
import yaml

def load_config_yaml(config_string):
    """Insecure YAML deserialization"""
    # Using unsafe yaml.load
    config = yaml.load(config_string, Loader=yaml.Loader)
    return config


# VULNERABILITY 23: Server-Side Template Injection simulation
def render_template(template_string, user_input):
    """Template injection via string formatting"""
    # User input in template
    rendered = template_string.format(user_data=user_input)
    return rendered


# VULNERABILITY 24: Race Condition
user_balance = 1000

def withdraw_money(amount):
    """Race condition in financial operation"""
    global user_balance
    # No locking mechanism
    if user_balance >= amount:
        # Vulnerability: Another thread could modify balance here
        user_balance -= amount
        return True
    return False


# VULNERABILITY 25: Hardcoded Credentials in Connection String
def connect_to_database():
    """Hardcoded database password"""
    connection_string = "Server=db.example.com;Database=prod;User=admin;Password=SuperSecret123!;"
    # Hardcoded credentials
    return connection_string


# VULNERABILITY 26: Integer Overflow
def allocate_buffer(size):
    """Potential integer overflow"""
    # No bounds checking
    buffer_size = size * 1024 * 1024
    buffer = bytearray(buffer_size)
    return buffer


# VULNERABILITY 27: NULL Byte Injection
def open_log_file(filename):
    """NULL byte injection"""
    # NULL byte can truncate filename
    full_path = f"/var/log/{filename}.log"
    return open(full_path, 'r')


# VULNERABILITY 28: Format String Vulnerability
def log_message(message):
    """Format string vulnerability"""
    # User input directly in format string
    sys.stderr.write(message % ())


# VULNERABILITY 29: Insecure File Permissions
def create_sensitive_file(filename, data):
    """Insecure file permissions"""
    # Creating file with overly permissive mode
    with open(filename, 'w') as f:
        f.write(data)
    os.chmod(filename, 0o777)  # World-writable


# VULNERABILITY 30: Unchecked Error Handling
def process_user_input(user_data):
    """Improper error handling"""
    try:
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        # SQL injection
        query = "INSERT INTO logs VALUES ('" + user_data + "')"
        cursor.execute(query)
        conn.commit()
    except:
        # Silently swallowing exceptions
        pass


# Main execution demonstrating vulnerabilities
if __name__ == "__main__":
    print("=" * 60)
    print("VULNERABLE APPLICATION - FOR TESTING ONLY")
    print("=" * 60)
    
    # Simulate user input for testing
    malicious_username = "admin' OR '1'='1"
    malicious_command = "127.0.0.1 & del /f /q important.txt"
    malicious_path = "../../../etc/passwd"
    malicious_code = "__import__('os').system('whoami')"
    
    # These would trigger vulnerabilities if executed
    print("\n[!] This application contains intentional vulnerabilities")
    print("[!] DO NOT run with untrusted input")
    print("[!] Qwiet.AI should detect multiple security issues")
    
    print("\nExpected vulnerabilities:")
    print("- SQL Injection (multiple instances)")
    print("- Command Injection (multiple methods)")
    print("- Path Traversal")
    print("- Insecure Deserialization")
    print("- Weak Cryptography")
    print("- Code Injection (eval/exec)")
    print("- Hardcoded Secrets")
    print("- Information Disclosure")
    print("- Insecure Random")
    print("- And more...")

