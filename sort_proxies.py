import threading
import queue
import requests

q = queue.Queue()
valid_proxies = []

# Read in raw list
with open("raw_proxy_list.txt", "r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)

# Check each proxy
def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get(
                "http://ipinfo.io/json",
                proxies={
                    "http": proxy, "https": proxy
                }
            )
        except:
            continue

        if res.status_code == 200:
            valid_proxies.append(proxy)
            print(proxy)

for _ in range(30):
    threading.Thread(target=check_proxies).start()

# Write out to new "clean" file
with open("proxies.txt", "w") as f:
    [f.write(ip + "\n") for ip in valid_proxies]