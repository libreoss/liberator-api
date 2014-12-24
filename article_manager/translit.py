# -*- coding: utf-8 -*- 
import sys 

from dokuwiki.parsers import Parser, LineParser
from dokuwiki.elements import LineElement


cir_lat_map = {
        u"љ": u"lj", 
        u"њ": u"nj", 
        u"е": u"e", 
        u"р": u"r", 
        u"т": u"t", 
        u"з": u"z",
        u"у": u"u", 
        u"и": u"i", 
        u"о": u"o", 
        u"п": u"p", 
        u"а": u"a",
        u"с": u"s", 
        u"д": u"d", 
        u"ф": u"f", 
        u"г": u"g", 
        u"х": u"h", 
        u"ј": u"j", 
        u"к": u"k", 
        u"л": u"l", 
        u"џ": u"dž", 
        u"ц": u"c", 
        u"в": u"v", 
        u"б": u"b", 
        u"н": u"n", 
        u"м": u"m", 
        u"ш": u"š", 
        u"ђ": u"đ",
        u"ж": u"ž", 
        u"ч": u"č", 
        u"ћ": u"ć", 
        u"Љ": u"Lj",
        u"Њ": u"Nj",
        u"Е": u"E", 
        u"Р": u"R",
        u"Т": u"T", 
        u"З": u"Z", 
        u"У": u"U",
        u"И": u"I", 
        u"О": u"O",
        u"П": u"P",
        u"А": u"A",
        u"С": u"S", 
        u"Д": u"D", 
        u"Ф": u"F", 
        u"Г": u"G", 
        u"Х": u"H", 
        u"Ј": u"J", 
        u"К": u"K", 
        u"Л": u"L", 
        u"Џ": u"Dž", 
        u"Ц": u"C", 
        u"В": u"V", 
        u"Б": u"B", 
        u"Н": u"N", 
        u"М": u"M", 
        u"Ш": u"Š", 
        u"Ђ": u"Đ", 
        u"Ж": u"Ž",
        u"Ч": u"Č",
        u"Ћ": u"Ć"
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
        if N == 0: return False
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
    #print "# Translate 2-letter letters first"
    # Translate 2-letter letters first 
    for cl in cir_lat_map.keys(): 
        if len(cir_lat_map[cl]) == 2: 
                #print cir_lat_map[cl] + " -> " + cl
                ntext = ntext.replace(cir_lat_map[cl], cl)
    
    
    #print "# Translate 1-letter letters"
    # Translate 1-letter letters
    for cl in cir_lat_map.keys(): 
        if len(cir_lat_map[cl]) == 1: 
                #print cir_lat_map[cl] + " -> " + cl
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
        self.frame = "" # frame is new translated text
    def onHeading(self, level, text):
        self.frame += "="*level + lat_to_cir(text) + "="*level + "\n"
    def onListStart(self, mode): pass
    def onListEnd(self): pass
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
        self.frame += l.getOutput() # huh, easy :)
        self.frame += "\n" # Don't forget to take newline
    def onDocumentEnd(self): pass
    def getOutput(self): 
        return self.frame

