import uglimodules.kmhook as km
import json

class Shortcut:
    def __init__(self, symbol: str, code: str):
        self.symbol = symbol
        self.code = code

    def trigger(self):
        km.press('lalt')
        for digit in self.code:
            km.sleep(0.05)
            km.press('num_' + digit)
            km.sleep(0.05)
            km.release('num_' + digit)
        km.sleep(0.05)
        km.release('lalt')


with open("codes.json","rt",encoding="utf8") as rf:
    data = json.load(rf)

shortcut_list = []
for element in data:
    shortcut_list.append(Shortcut(element['symbol'],element['code']))
