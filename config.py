import os
from dotenv import load_dotenv

load_dotenv()

# Bot token
BOT_TOKEN = '8019756028:AAHlbthAV1qP_ky0Qw2Ut8MObKfxly4xrbI'
#TELEGRAM_SUPPORT_CHAT_ID = "@SergerudBot"
#TELEGRAM_SUPPORT_CHAT_ID = int(TELEGRAM_SUPPORT_CHAT_ID)

SUPPORT_CHAT_ID = os.getenv("-1003426171537")
print(SUPPORT_CHAT_ID)