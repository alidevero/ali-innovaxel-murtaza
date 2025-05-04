from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import *
from .serializers import ShortURLSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

class ShortURLViewSet(viewsets.ViewSet):

    def create(self, request):
        try:

            serializer = ShortURLSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        try:

            url_obj = get_object_or_404(ShortUrl, short_url=pk)
            url_obj.access_count += 1
            url_obj.save()
            return Response({"url": url_obj.url})
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:

            url_obj = get_object_or_404(ShortUrl, short_url=pk)
            serializer = ShortURLSerializer(url_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        try:    
            url_obj = get_object_or_404(ShortUrl, short_url=pk)
            url_obj.delete()
            return Response(status=204)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def stats(self, request, pk=None):
        try:

            url_obj = get_object_or_404(ShortUrl, short_url=pk)
            return Response({
                "id": url_obj.id,
                "url": url_obj.url,
                "shortCode": url_obj.short_url,
                "createdAt": url_obj.created_at,
                "updatedAt": url_obj.updated_at,
                "accessCount": url_obj.access_count
            })
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
