import json
import time
import os
from pypresence import Presence

# Config file load karo
with open('config.json', 'r') as f:
    config = json.load(f)

client_id = config['APPLICATION_ID']
RPC = Presence(client_id)
RPC.connect()

print("🚀 Real RPC Start! 24/7 chalega aur sabko dikhega!")

while True:
    try:
        RPC.update(
            state=config['state'],
            details=config['details'],
            large_image=config['assets']['large_image'],
            large_text=config['assets']['large_text'],
            small_image=config['assets']['small_image'],
            small_text=config['assets']['small_text'],
            buttons=config.get('buttons', []),
            start=int(time.time())
        )
        print(f"✅ Status update hua - {time.strftime('%H:%M:%S')}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    time.sleep(config['refreshInterval'])
