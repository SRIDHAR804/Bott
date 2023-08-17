import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv("API_ID", "13399054"))
    API_HASH = os.getenv("API_HASH", "585801d590dac4c79aeaa7bcda495e62")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5753462185:AAGfUMEZKVA3fH_EHGttXroE1MM9eXy5Pao")
    sudo = os.getenv("SUDO", "1697462260")
    SUDO = []
    if sudo:
        SUDO = make_int(sudo)
