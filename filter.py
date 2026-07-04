import base64
import requests

SUB_URL = "https://super-violet-255f.momehdi010.workers.dev"

r = requests.get(SUB_URL)
r.raise_for_status()

decoded = base64.b64decode(r.text.strip()).decode("utf-8")

lines = decoded.splitlines()

filtered = [
    line for line in lines
    if "@0.0.0.0:1" not in line
]

encoded = base64.b64encode(
    "\n".join(filtered).encode()
).decode()

with open("sub.txt", "w") as f:
    f.write(encoded)
