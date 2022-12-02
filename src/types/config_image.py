class config_image:
    """Contains the default config image and some restricted values that are used to check and validate the config file."""

    default = {

        "user": {
            "token": "token-here",
            "password" : "password"         
        },

        "commands": {
            "prefix": "v!",
            "command_mode": "ansi",
            "delete_after": 25,
            "delete_invoking": True
        },

        "rich_presence": {
            "enabled": True,
            "client_id": "892043411102769153",
            "details": "drippin as always",
            "state": "logged in as uhh",
            "large_image": "sdf",
            "large_text": "cici",
            "small_image": "",
            "small_text": ""       
        },

        "console": {
            "primary_color": "#748cdb",
            "secondary_color": "#323e63"   
        },

        "embeds": {
            "host": "vaul.xyz",
            "title": "Vissarion",
            "image_url": "https://vaul.xyz/vissarion_logo.png",
            "color": "#ffffff",
            "footer": "Vissarion",
            "large": False
        },

        "ansi": {
            "title": "Vissarion",
            "footer": "Vissarion"
        },

        "useOwnXProperties": {
            "enabled": False,
            "x-property": "property-here"
        },

        "session_manager": {
            "enabled": False,
            "operating_systems": [],
            "platforms": [],
            "locations": []
        },
        
        "startup_state": {
            "enabled": False,
            "status": "online",
            "custom_status": "drippin as always",
            "activity": "playing",
            "activity_name": "ur mom",
            "stream_url": "https://www.twitch.tv/uhh"
        },
        "event_logger": {
            "enabled": False,
            "message_delete": False,
            "message_edit": False,
            "ghostpings": False,
            "member_join": False,
            "member_leave": False,
            "member_ban": False,
            "dm_typing": False
        },
        
        "webhook_settings": {
            "username": "Vissarion",
            "avatar_url": "https://cdn.discordapp.com/avatars/818606240371310622/64308969717d2fa9c235d96880a253aa.webp?size=1024"
        },
        
        "webhook_urls": {
            "message_delete_url": "",
            "message_edit_url": "",
            "ghostpings_url": "",
            "member_join_url": "",
            "member_leave_url": "",
            "member_ban_url": ""
        }
    }

    restricted_values = {
        
        "rich_presence": {
            "enabled": [True, False]
        },

        "commands": {
            "command_mode": ["embed", "ansi"],
            "delete_invoking": [True, False]
        },

        "embeds": {
            "host": ["vaul.xyz"],
            "large": [True, False]
        },

        "startup_state": {
            "enabled": [True, False],
            "status": ["online", "idle", "dnd", "invisible", "null"],
            "activity": ["playing", "streaming", "listening", "watching", "null"]
        },

        "event_logger": {
            "enabled": [True, False],
            "message_delete": [True, False],
            "message_edit": [True, False],
            "ghostpings": [True, False],
            "member_join": [True, False],
            "member_leave": [True, False],
            "member_ban": [True, False],
            "dm_typing": [True, False]
        }

    }
    
