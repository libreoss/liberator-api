
import logging
import enchant
import json

import os 

class Dictionary(object):
    
    def __init__(self, dictname, search_path="/var/db/liberator/dictionaries/", tag="sh"):
        self.filepath = search_path + "/" + dictname + ".txt"
        self.search_path = search_path
        self.dict = enchant.DictWithPWL(
            tag=tag,
            pwl=self.filepath,
            pel="%s/%s.ignore.txt" % (search_path, dictname)
        )
        self.dictname = dictname
    
    def dictionary_list(search_path="/var/db/liberator/dictionaries/"):
        files = os.listdir(search_path)
        res = [] 
        for f in files:
            name = ""
            for w in f:
                if w == ".":
                    break
                name += w
            if not name in res:
                res.append(name)
        return res

    def add_word(self, word):
        if not self.dict.check(word) and not Dictionary.get_global_dictionary(search_path=self.search_path).check(word):
            self.dict.add(word)

    def ignore_word(self, word):
        self.dict.remove(word)

    def check(self, word):
        return self.dict.check(word) or Dictionary.get_global_dictionary(search_path=self.search_path).dict.check(word)

    def get_words(self):
        res = []
        f = open(self.filepath, "r")
        for w in f:
            if self.dict.check(w):
                res.append(w)
        return res

    def get_suggestions(self, word):
        return self.dict.suggest(word)

    def get_global_dictionary(search_path="/var/db/liberator/dictionaries/"):
        return Dictionary("GLOBAL", search_path, "sh")

    def is_owner(self, email):
        return self.dictname == email.replace(".", "_")
