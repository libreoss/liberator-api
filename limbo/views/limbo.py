
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
        l = Dictionary.dictionary_list()
        return Response(data={"words": l}, status=200)

    def partial_update(self, request, pk=None):
        pass

    def create(self, request):
        """
        Adds words to global dictionary
        """
        dictionary = Dictionary.get_global_dictionary()
        wordlist = LimboSerializer(data=request.data)
        if wordlist.is_valid():
            for w in wordlist.data["words"]:
                dictionary.add_word(w["word"])
            return Response(wordlist.data, status=201)
        else:
            return Response(status=400)

    def retrieve(self, request, pk=None):
        """
        List of words for specified dictionary
        """
        dictionary = Dictionary(pk)
        return Response(
            status=200,
            data={"words": dictionary.get_words()}
        )

    def destroy(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        """
        Add word to local dictionary
        """
        dictionary = Dictionary(pk)
        if dictionary.is_owner(request.user.email):
            wordlist = LimboSerializer(data=request.data)
            if wordlist.is_valid():
                words = wordlist.validated_data["words"]
                for w in words:
                    dictionary.add_word(w["word"])
                return Response(status=201)
            else:
                return Response(status=400)
        else:
            return Response(status=403)

    @detail_route(methods=['post'])
    def check(self, request, pk=None):
        wordlist = LimboSerializer(data=request.data)
        dictionary = Dictionary(pk)
        res = []
        if wordlist.is_valid():
            ww = wordlist.data["words"]
            for w in ww:
                if dictionary.check(w["word"]):
                    res.append({
                        "word": w["word"],
                        "ok": True,
                        "suggestions": []
                    })
                else:
                    res.append({
                        "word": w["word"],
                        "ok": False,
                        "suggestions": dictionary.get_suggestions(w["word"])
                    })
            return Response(data={"words": res})
        else:
            return Response(status=400)

    @detail_route(methods=['post'])
    def ignore(self, request, pk=None):
        """
        Removes word from specified dictionary
        (specify 'global' for global dictionary)
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
            return Response(status=202)
        else:
            return Response(status=400)
