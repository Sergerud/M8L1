import os
from dotenv import load_dotenv

load_dotenv()

# Bot token
BOT_TOKEN = ''
#TELEGRAM_SUPPORT_CHAT_ID = "@SergerudBot"
#TELEGRAM_SUPPORT_CHAT_ID = int(TELEGRAM_SUPPORT_CHAT_ID)

SUPPORT_CHAT_ID = os.getenv("-1003426171537")

print(SUPPORT_CHAT_ID)
