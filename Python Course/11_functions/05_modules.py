# Two types of modules in Python:
# - Built in modules
# - External modules

import math
import os
import mymodule
import requests

print(math.sqrt(16))  # Output: 4.0
mymodule.hello()  
r = requests.get("https://www.google.com")
print(r.url)  