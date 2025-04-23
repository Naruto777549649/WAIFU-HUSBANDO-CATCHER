class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7019600964"
    sudo_users = "6239769036", "7019600964"
    GROUP_ID = -1002304401488
    TOKEN = "7851576039:AAFv6o74rF5Ej0DP_aa7AAHgDYXKorkbbj8"
    mongo_url = "mongodb+srv://sufyan532011:2010@dbz.28ftn.mongodb.net/?retryWrites=true&w=majority&appName=DBZ"
    PHOTO_URL = ["https://files.catbox.moe/olhyw5.jpg"]
    SUPPORT_CHAT = "animaction_world_in_2025"
    UPDATE_CHAT = "harmonyheaven03"
    BOT_USERNAME = "Collect_Em_AllBot"
    CHARA_CHANNEL_ID = "-1002515671821"
    api_id = 25698862
    api_hash = "7d7739b44f5f8c825d48cc6787889dbc"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
