import base64
import requests
import time

SUB_URL = "https://zeus-panel-edqrba.zeus-ikyheb.workers.dev/feed/Deiii"

headers = {
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "User-Agent": "Mozilla/5.0"
}

url = f"{SUB_URL}?t={int(time.time())}"

r = requests.get(url, headers=headers)
r.raise_for_status()

decoded = base64.b64decode(r.text.strip()).decode("utf-8")

lines = decoded.splitlines()

filtered = [
    line for line in lines
    if "@0.0.0.0:1" not in line
]

encoded = base64.b64encode("\n".join(filtered).encode()).decode()

with open("sub.txt", "w") as f:
    f.write(encoded)
