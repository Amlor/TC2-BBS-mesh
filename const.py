import configparser, enum

# Read the configuration for menu options
config = configparser.ConfigParser()
config.read('config.ini')

config_main_menu_items = config['menu']['main_menu_items'].split(',')
config_bbs_menu_items = config['menu']['bbs_menu_items'].split(',')
config_utilities_menu_items = config['menu']['utilities_menu_items'].split(',')

main_menu_items = ()


class CONFIG_MENU_ITEM(enum, str):
    MAIN = "main_menu_items"
    BBS = "bbs_menu_items"
    UTILITIES = "utilities_menu_items"


class MENU_ITEM(enum, str):
    QUICK = "Q"
    BBS = "B"
    UTILITIES = "U"
    EXIT = "X"
    MAIL = "M"
    CHANNEL_DIR = "C"
    JS8CALL = "J"
    STATS = "S"
    FORTUNE = "F"
    WALL = "W"


class MENU_TYPE(enum, str):
    MAIN = "main"
    QUICK = "quick"
    BBS = "bbs"
    UTILITIES = "utilities"
    EXIT = "exit"
    MAIL = "mail"
    CHANNEL_DIR = "channel"
    JS8CALL = "js8call"
    STATS = "stats"
    FORTUNE = "fortune"
    WALL = "wall"


MENU_LINES = {
    MENU_ITEM.QUICK: "[Q]uick Commands\n",
    MENU_ITEM.BBS: "[B]BS\n",
    MENU_ITEM.UTILITIES: "[U]tilities\n",
    MENU_ITEM.EXIT: "E[X]IT\n",
    MENU_ITEM.MAIL: "[M]ail\n",
    MENU_ITEM.CHANNEL_DIR: "[C]hannel Dir\n",
    MENU_ITEM.JS8CALL: "[J]S8CALL\n",
    MENU_ITEM.STATS: "[S]tats\n",
    MENU_ITEM.FORTUNE: "[F]ortune\n",
    MENU_ITEM.WALL: "[W]all of Shame\n",
}

MENU_HEADERS = {
    MENU_TYPE.MAIN: "💾TC² BBS💾",
    MENU_TYPE.BBS: "📰BBS Menu📰",
    MENU_TYPE.UTILITIES: "🛠️Utilities Menu🛠️",
}

def get_config_menu_items(config_menu_item: CONFIG_MENU_ITEM) -> list[str]:
    

def convert_config_items_to_enum(config_items: list[str]) -> tuple[MENU_ITEM]:
    return (MENU_ITEM(item) for item in config_items)

MENU_ITEMS = {
    MENU_ITEM.MAIN: convert_config_items_to_enum()
}
