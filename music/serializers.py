from rest_framework import serializers
from music.models import Artist, Album, Tracks


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    class Meta:
        model = Album
        fields = '__all__'

class TracksSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()
    class Meta:
        model = Tracks
        fields = '__all__'
