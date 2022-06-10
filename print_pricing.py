import emoji
import re


class Personalize:

    def __init__(self, text, item):
        self.string = text
        self.item = item
        self.pricing = {'mug': 10, 't-shirt': 20, 'notebook': 5, 'waterbottle': 45, 'drinking glass': 10, 'pencil': 3,
                        'backpack': 80, 'cap': 15, 'flag': 30, 'ferrari': 400000}
        self.current = -1

    def __iter__(self):
        for char in self.string:
            yield char

    def calculate_price(self):
        return self.__len__() + self.pricing[self.item]

    def isascii(self):
        return self.string.isascii()

    def emoji_count(self):
        return emoji.emoji_count(self.string)

    def __len__(self):
        empty = self.string.count(' ')
        ascii_chars = 0
        emoji_num = int(self.emoji_count())
        emojis = emoji.distinct_emoji_list(self.string)
        non_latin = 0
        for char in self.string:
            if char.isascii():
                ascii_chars += 1
        string = self.string
        for i in emojis:
            string = re.sub(i, '', string)
        for char in string:
            try:
                if char.encode('latin-1'):
                    continue
            except UnicodeEncodeError:
                if char not in emojis:
                    non_latin += 3
        return ascii_chars + emoji_num * 2 + non_latin - empty
