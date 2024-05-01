from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Album, Artist, Tracks
from .serializers import ArtistSerializer, AlbumSerializer, TracksSerializer
import json

class LandingPageApiView(APIView):
    def get(self, request):
        return Response(data={"get api": 'Landing Page'})

    def post(self, request):
        return Response(data={"post api": ' This is post request'})


class ArtistPageApiView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(data=serializer.data)


class AlbumPageApiView(APIView):
    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(data=serializer.data)


class TracksPageApiView(APIView):
    def get(self, request):
        tracks = Tracks.objects.all()
        serializer = TracksSerializer(tracks, many=True)
        return Response(data=serializer.data)
