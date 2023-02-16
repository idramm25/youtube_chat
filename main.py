# import pytchat
# chat = pytchat.create(video_id="M5Su8Vl1egE")
# while chat.is_alive():
#     for c in chat.get().sync_items():
#         print(f"{c.datetime} [{c.author.name}[{c.channelId}]]- {c.message}")
#         # print(c)


# [{"author": {"badgeUrl": "", "type": "", "isVerified": false, "isChatOwner": false, "isChatSponsor": false, "isChatModerator": false, "channelId": "UCk6EFWbFGoanCIm7HGBK7GQ", "channelUrl": "http://www.youtube.com/channel/UCk6EFWbFGoanCIm7HGBK7GQ", "name": "M. Elich Qin", "imageUrl": "https://yt4.ggpht.com/d7RhFxNiiW_D5-sJyEXxE-yc3b4Q3zucr9XBG_1ADEd5b8RScfBIsqWCnMn90fxUPvJq2sSrXQ=s64-c-k-c0x00ffffff-no-rj"}, "type": "textMessage", "id": "CkUKGkNOYnhrcHJnLWZJQ0ZkVFJ3UW9kMDdnQmhREidDSTNabjViZy1mSUNGWkpPNEFvZEoyb0ZqQTE2MzE0NjA1NjA5OTA%3D", "timestamp": 1631460562090, "elapsedTime": "", "datetime": "2021-09-12 18:29:22", "message": "hi :hand_with_fingers_splayed:", "messageEx": ["hi ", {"id": "🖐", "txt": ":hand_with_fingers_splayed:", "url": "https://www.youtube.com/s/gaming/emoji/7ff574f2/emoji_u1f590.svg"}], "amountValue": 0.0, "amountString": "", "currency": "", "bgColor": 0}]


import sys
import time

import pytchat
from colorama import Fore

channel = input("Input channel ID: ")

try:
    chat = pytchat.create(video_id=channel)
except Exception as e:
    print("Something is wrong, check next:  ")
    print(str(e))
    sys.exit()


print("Ok")
print("Connecting to chat........")
print("**************************************************************************************************************")
print("Connect OK, messages:")

while chat.is_alive():
    chatdata = chat.get()
    items = chatdata.items
    for item in items:
        print(Fore.WHITE + f"{item.author.channelUrl} - " + Fore.CYAN + f"[{item.author.name}]: " + Fore.GREEN + f"{item.message}")
        time.sleep(5)

try:
    chat.raise_for_status()
except pytchat.ChatdataFinished:
    print("chat data finished")
except Exception as e:
    print(type(e), str(e))
