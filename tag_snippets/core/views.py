from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder


from core.models import TagModel, SnippetModel
from core.serializers import TagSerializer, SnippetSerializer


class TagView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request,id):
        if id and int(id) != 0:
           return Response(data = TagModel.objects.filter(pk=id).values())
        return Response(data =  TagModel.objects.values())

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        print(request.user.__module__)
        return Response(serializer.data)

    def put(self):
        pass


class SnippetView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        if id and int(id) != 0:
            return Response(data=SnippetModel.objects.filter(pk=id).values())
        return Response(data=SnippetModel.objects.values())

    def post(self, request):
        title = request.data.pop("title")
        tag,_ = TagModel.objects.get_or_create(title=title)
        print(tag.id)
        snippet = SnippetModel(text=request.data.get("text"), tag=tag, user=request.user)
        snippet.save()
        serializer = SnippetSerializer(instance=snippet)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)
        return Response(request.data)