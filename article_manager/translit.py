# -*- coding: utf-8 -*-
from dokuwiki.parsers import Parser, LineParser


cir_lat_map = {
    "љ": "lj",
    "њ": "nj",
    "е": "e",
    "р": "r",
    "т": "t",
    "з": "z",
    "у": "u",
    "и": "i",
    "о": "o",
    "п": "p",
    "а": "a",
    "с": "s",
    "д": "d",
    "ф": "f",
    "г": "g",
    "х": "h",
    "ј": "j",
    "к": "k",
    "л": "l",
    "џ": "dž",
    "ц": "c",
    "в": "v",
    "б": "b",
    "н": "n",
    "м": "m",
    "ш": "š",
    "ђ": "đ",
    "ж": "ž",
    "ч": "č",
    "ћ": "ć",
    "Љ": "Lj",
    "Њ": "Nj",
    "Е": "E",
    "Р": "R",
    "Т": "T",
    "З": "Z",
    "У": "U",
    "И": "I",
    "О": "O",
    "П": "P",
    "А": "A",
    "С": "S",
    "Д": "D",
    "Ф": "F",
    "Г": "G",
    "Х": "H",
    "Ј": "J",
    "К": "K",
    "Л": "L",
    "Џ": "Dž",
    "Ц": "C",
    "В": "V",
    "Б": "B",
    "Н": "N",
    "М": "M",
    "Ш": "Š",
    "Ђ": "Đ",
    "Ж": "Ž",
    "Ч": "Č",
    "Ћ": "Ć"
}


def check_cyr(text):
        """
        Returns True if more then 40% letters of text is in cyrilic script
        """
        counter = 0
        N = 0
        cyr = list(cir_lat_map.keys())
        lat = list(cir_lat_map.values())
        serbian_letters = cyr + lat
        for c in text:
                if c in serbian_letters:
                        N += 1
                        if c in cyr:
                                counter += 1
        if N == 0:
            return False
        return counter / float(N) > 0.4


def cir_to_lat(txt):
    ntxt = ""
    for c in txt:
        if c in cir_lat_map:
            ntxt += cir_lat_map[c]
        else:
            ntxt += c
    return ntxt


def lat_to_cir(text):
    ntext = ""
    ntext = text
    # Translate 2-letter letters first
    for cl in cir_lat_map.keys():
        if len(cir_lat_map[cl]) == 2:
            ntext = ntext.replace(cir_lat_map[cl], cl)

    # Translate 1-letter letters
    for cl in cir_lat_map.keys():
        if len(cir_lat_map[cl]) == 1:
            ntext = ntext.replace(cir_lat_map[cl], cl)
    return ntext


class TranslatorLineParser(LineParser):
        def onStart(self):
            self.output = ""
            self.translate = True

        def onNormal(self, text):
            if self.translate:
                self.output += lat_to_cir(text)
            else:
                self.output += text

        def onItalicStart(self):
            self.translate = False
            self.output += "//"

        def onItalicEnd(self):
            self.translate = True
            self.output += "//"

        def onBoldStart(self):
            self.output += "**"

        def onBoldEnd(self):
            self.output += "**"

        def onUnderlineStart(self):
            self.output += "__"

        def onUnderlineEnd(self):
            self.output += "__"

        def onLink(self, url, title):
            self.output += "[[" + title + "|" + url + "]]"

        def onImage(self, params):
            self.output += "{{" + params + "}}"

        def getOutput(self):
            return self.output


class TranslatorParser(Parser):
    def onDocumentStart(self):
        self.frame = ""

    def onHeading(self, level, text):
        self.frame += "="*level + lat_to_cir(text) + "="*level + "\n"

    def onListStart(self, mode):
        pass

    def onListEnd(self):
        pass

    def onListItem(self, level, text):
        l = TranslatorLineParser(text)
        new_text = l.getOutput()
        self.frame += "  * " + new_text + "\n"

    def onCodeStart(self, language, filename):
        self.frame += "<code>" + "\n"

    def onCode(self, text):
        self.frame += text + "\n"

    def onCodeEnd(self):
        self.frame += "</code>" + "\n"

    def onParagraphStart(self):
        self.frame += "\n"

    def onParagraphEnd(self):
        self.frame += "\n"

    def onText(self, text):
        l = TranslatorLineParser(text)
        self.frame += l.getOutput()
        self.frame += "\n"

    def onDocumentEnd(self):
        pass

    def getOutput(self):
        return self.frame
