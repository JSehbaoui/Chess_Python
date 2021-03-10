from two_play_menu import login
from bot_settings_menu import settings

def intermediary(bot, mode):
    if bot:
        settings(mode)
    else:
        login(mode)