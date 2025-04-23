class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7019600964"
    sudo_users = "6239769036", "1514849521"
    GROUP_ID = -1002304401488
    TOKEN = "7851576039:AAFv6o74rF5Ej0DP_aa7AAHgDYXKorkbbj8"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://files.catbox.moe/olhyw5.jpg"]
    SUPPORT_CHAT = "Collect_em_support"
    UPDATE_CHAT = "Collect_em_support"
    BOT_USERNAME = "Collect_Em_AllBot"
    CHARA_CHANNEL_ID = "-1002515671821"
    api_id = 25698862
    api_hash = "7d7739b44f5f8c825d48cc6787889dbc"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
