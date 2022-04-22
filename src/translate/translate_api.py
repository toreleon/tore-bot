import os
from typing import Dict
import requests


class GoogleTranslateAPI:
    def __init__(self) -> None:
        self.url: str = os.getenv("GOOGLE_TRANSLATE_URL")
        self.key: str = os.getenv("GOOGLE_TRANSLATE_KEY")
        self.headers: Dict = {
            "content-type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "application/gzip",
            "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
            "X-RapidAPI-Key": self.key,
        }

    def translate(
        self, text: str, source_language: str = "en", target_language: str = "vi"
    ) -> str:
        data: Dict = {"q": text, "source": source_language, "target": target_language}
        response: requests.Response = requests.post(
            self.url, headers=self.headers, data=data
        )
        return response.json()["data"]["translations"][0]["translatedText"]
