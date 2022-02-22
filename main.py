"""
This telegram bot checks for links from members and deletes the messages and also restricting them from sending any message for 10 minutes
"""

from os import environ
from keep_alive import keep_alive
from pyrogram import Client, filters
from pyrogram.types import ChatPermissions

# Authorize bot
PHONE_NUMBER = environ["PHONE_NUMBER"]
PASSWORD = environ["PASSWORD"]
USERNAME = environ["USERNAME"]
API_ID = environ["API_ID"]
API_HASH = environ["API_HASH"]
me = Client(USERNAME, api_id=API_ID, api_hash=API_HASH, phone_number=PHONE_NUMBER, password=PASSWORD)

# Set Target chat to CeloDoge channel
TARGET_CHAT = environ["TARGET_CHAT"]
target_chat = TARGET_CHAT

# Set warn message
WARN_MESSAGE = ""

# Check for links and delete
url_regex = "https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)|[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)"


@me.on_message(filters.chat(target_chat) & filters.regex(url_regex))
def delete(me, message):
    user = message.from_user
    chat = me.get_chat(target_chat)
    chatMember = chat.get_member(user.id)
    if chatMember.status == "member" & "explorer.celo.org" in message.text:
        restrict_date = message.date + 700
        message.delete()

        # Restrict Violator from sending message for 10mins

        chat.restrict_member(user.id,
                             ChatPermissions(can_send_messages=False),
                             until_date=restrict_date)


print("I'm alive")

# Start Server
keep_alive()

# Run Bot
me.run()
