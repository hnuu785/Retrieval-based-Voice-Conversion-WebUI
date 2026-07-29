import json
import locale
import os
from tools.file_io import read_text


def load_language_list(language):
    return json.loads(read_text(f"./i18n/locale/{language}.json"))


class I18nAuto:
    def __init__(self, language=None):
        if language in ["Auto", None]:
            language = locale.getdefaultlocale()[
                0
            ]  # getlocale can't identify the system's language ((None, None))
        if language:
            language = language.split(".")[0]
        if not language or not os.path.exists(f"./i18n/locale/{language}.json"):
            language = "ko_KR"
        self.language = language
        self.language_map = load_language_list(language)

    def __call__(self, key):
        return self.language_map.get(key, key)

    def __repr__(self):
        return "Use Language: " + self.language
