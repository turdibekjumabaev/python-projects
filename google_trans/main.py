import requests
from google_trans.const import DEFAULT_USER_AGENT

class Translator:
    def __init__(self):
        self.url = 'https://translate.google.com/'
        self.headers = {
            'User-Agent' : DEFAULT_USER_AGENT
        }

    def translate(self, text: str, source_lang='auto', target_lang='uz'):
        params = {
            'hl': 'en',
            'ie': 'UTF-8',
            'text': text,
            'langpair': f'{source_lang}|{target_lang}'
        }

        if source_lang == 'auto':
            del params['langpair']
            return requests.get(
                url=self.url + f"translate_a/single?client=gtx&sl=auto&tl={target_lang}&dt=t&q={text}", params=params, headers=self.headers
            ).json()[0][0][0]
        else:
            return requests.get(
                url=self.url + f"translate_a/single?client=gtx&sl={source_lang}&tl={target_lang}&dt=t&q={text}", params=params, headers=self.headers
            ).json()[0][0][0]