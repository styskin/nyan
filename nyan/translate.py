import requests
import json

URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"
LANG = "fa-ru"


class Translator:
    def __init__(self, config_path):
        with open(config_path) as r:
            config = json.load(r)
        self.key = config["cloud_translate"]
        self.folder_id = config["cloud_folder"]
        self.lang = config["translate_lang"]

    def __call__(self, text):
        body = {
#            "sourceLanguageCode": "uz",
            "targetLanguageCode": "ru",
            "texts": [text],
            "folderId": self.folder_id,
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {0}".format(self.key)
        }
        response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
            json = body,
            headers = headers
        )
        return json.loads(response.text)["translations"][0]["text"]
