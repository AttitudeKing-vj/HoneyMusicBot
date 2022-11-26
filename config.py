from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "15229796"))
API_HASH = getenv("API_HASH", "4e3363ea7214ebab7a03b9300bba722c")
BOT_TOKEN = getenv("BOT_TOKEN","5759557752:AAEDDnyXQolV7RPVj4BYgPWPhhnaw53ZFMs")
BOT_NAME = getenv("BOT_NAME","Sofiya")
BOT_USERNAME = getenv("BOT_USERNAME","Sophia_X_Bot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "20"))
SESSION_NAME = getenv("SESSION_NAME", "BQCAs-flK6Aam2j2j-lJV1BMQQJFasntKtyDcMM2IbjzFTmL6VB47z6nTU8VW-XumkNRAV6O-mt2-QmEX8Od6136noKHWbgKuddL9Z6jXZOCFBG-eWSkG-Lbb6fafgFVm5hylrSVeAZZT9NJr1qDUciPh9LDiWv2dpwUZJafi-jSIWHra0FJdnmN0aIMcqXErbyQUdGnq4QdfnCsyGei4x1s1tfeW38BKnyQlLJKBMBqAvoelV2PEVFe_ismeFU0DIdZGAZvcw5z-BpKBNVd7wwf0yRF95DY11-gYPUjuwD9H0ItiRRszhT1yPO0eRdkkdSG0PB8x87dApcQpxBAwQs8bpDg3wA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2093345393").split()))
