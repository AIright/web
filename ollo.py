import requests
import os
import base64
a = base64.b64encode(b'user123:pass321')
print(a)
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
