from src.config import config

class webhook_builder:


    def _parse_data(data: dict) -> str:
        string = ""
        for key, value in data.items():
            string += "> **%s**: %s \n" % (key, value)
        return string


    def _build(event_type: str, data: str) -> dict:
        username =  config.read()["webhook_settings"]["username"]
        avatar_url = config.read()["webhook_settings"]["avatar_url"]

        template = {
            "username": username,
            "avatar_url": avatar_url,
            "embeds": [
            {
                    "description": f"""
                    > **{event_type}**
                    {data}
                    """,
                    "color": 16777215,
                    "author": {
                        "name": f"{username} | Detections",
                        "url": "https://vaul.xyz",
                    }
            } ]
        }

        return template


    def form_webhook_data(event_type: str, data: dict) -> dict:
        data = webhook_builder._parse_data(data)
        template = webhook_builder._build(event_type, data)
        return template
            
            