# import pytchat
# chat = pytchat.create(video_id="M5Su8Vl1egE")
# while chat.is_alive():
#     for c in chat.get().sync_items():
#         print(f"{c.datetime} [{c.author.name}[{c.channelId}]]- {c.message}")
#         # print(c)


# [{"author": {"badgeUrl": "", "type": "", "isVerified": false, "isChatOwner": false, "isChatS>


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
