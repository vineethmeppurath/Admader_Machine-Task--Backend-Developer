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

    def put(self, request,id):
        data = TagModel.objects.filter(pk=id)
        tag = data.first()
        tag.__dict__.update(request.data)
        tag.save()
        return Response(data=data.values())
    def delete(self, request,id):
        data = TagModel.objects.filter(pk=id).first()
        data.delete()
        return Response(data=request.data)


class SnippetView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        if id and int(id) != 0:
            return Response(data=SnippetModel.objects.filter(pk=id).values())
        return Response(data=SnippetModel.objects.values())

    def post(self, request):
        title = request.data.pop("title")
        tag,_ = TagModel.objects.get_or_create(title=title)
        snippet = SnippetModel(text=request.data.get("text"), tag=tag, user=request.user)
        snippet.save()
        return Response(data = request.data)

    def put(self, request, id):
        title = request.data.pop("title")
        tag, _ = TagModel.objects.get_or_create(title=title)
        data = SnippetModel.objects.filter(pk=id)
        snippest = data.first()
        snippest.tag = tag
        snippest.text = request.data.get('text')
        snippest.save()
        return Response(data=data.values())

    def delete(self, request, id):
        data = SnippetModel.objects.filter(pk=id).first()
        data.delete()
        return Response(data=request.data)


class TagDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        if id and int(id) != 0:

            return Response(data=SnippetModel.objects.filter(tag_id=id).values())
        return Response(data=SnippetModel.objects.values())