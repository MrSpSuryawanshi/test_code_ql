# SQL Injection Vulnerability
user_input = "john' OR '1'='1"
query = "SELECT * FROM users WHERE username='" + user_input + "'"

# Cross-Site Scripting (XSS) Vulnerability
user_input = "<script>alert('XSS')</script>"
html = f"<div>{user_input}</div>"

# Insecure File Upload
from werkzeug.utils import secure_filename

user_input = "evil_payload.exe"
uploaded_file = user_input  # Insecure file upload, no validation

# Inadequate Authentication and Authorization
def admin_page():
    if not is_admin():
        return "Unauthorized"
    return "Welcome, Admin"

# Hardcoded Secrets
db_password = "supersecret"
api_key = "myapikey"

# Deprecated or Insecure Libraries
import urllib2  # urllib2 is deprecated

# Inadequate Input Validation
user_input = "file:///etc/passwd"
if "http://" not in user_input:
    user_input = "http://" + user_input

print("CodeQL example file")
