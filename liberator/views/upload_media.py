

from rest_framework import viewsets
from liberator import serializers

from rest_framework.response import Response
from rest_framework.decorators import list_route

from liberator.models import Media, Article

from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from project import settings

from time import time

class UploadMediaView(APIView):

    parser_classes = [MultiPartParser,]

    def post(self, request, articleId):
        file_obj = request.data['file']
        article = Article.objects.get(pk=articleId)
        name = "%d-%d" % (article.pk, int(time() * 100) )
        f = open(settings.MEDIA_ROOT + "/" + name, "wb")
        f.write(file_obj.read())
        f.close()
        media = Media.objects.create(article=article, url="media/%s" % name)
        media.save()
        return Response(status=201)
