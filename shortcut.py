import uglimodules.kmhook as km


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

shortcut_list = [
    Shortcut("æ", "145"),
    Shortcut("É", "144"),
    Shortcut("Ç", "128"),
    Shortcut("Œ", "0140"),
    Shortcut("œ", "0156"),
    Shortcut("«", "174"),
    Shortcut("»", "175"),

]

# Will import shortcuts via a .json file later
