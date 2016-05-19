
from rest_framework import viewsets
from limbo import serializers

from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from limbo.serializers import LimboSerializer

from limbo.lib import Dictionary

class LimboViewSet(viewsets.ViewSet):
    
    def list(self, request):
        """
        Lists all dictionaries currently available
        """

    def create(self, request):
        """
        Adds words to global dictionary
        """
        dictionary = Dictionary.get_global_dictionary()
        wordlist = LimboSerializer(data=request.data)
        if wordlist.is_valid():
            for w in wordlist.data["words"]:
                dictionary.add_word(w["word"])
        return Response(wordlist.data)


    def retrieve(self, request, pk=None):
        """
        List of words for specified dictionary
        """
        dictionary = Dictionary(pk)
        return Response(LimboSerializer(data={"words": dictionary.get_words()}).data)

    def destroy(self, request, pk=None):
        """
        Removes word from specified dictionary (specify 'global' for global dictionary)
        """
        dictionary = None
        if pk == "global":
            dictionary = Dictionary.get_global_dictionary()
        else:
            dictionary = Dictionary(pk)
        wordlist = LimboSerializer(data=request.data)
        if wordlist.is_valid():
            for w in wordlist.data["words"]:
                dictionary.ignore_word(w["word"])
            return Response(data=wordlist.data)
    
    @detail_route(methods=['post'])
    def check(self, request, pk=None):
        wordlist = LimboSerializer(data=request.data)
        dictionary = Dictionary(pk)
        res = []
        for w in wordlist.data["words"]:
            if dictionary.check(w["word"]):
                res.append({"word": w["word"], "ok": True, "suggestions": []})
            else:
                res.append({"word": w["word"], "ok": False, "suggestions": dictionary.get_suggestions(w)})
        return Response(data=res)
