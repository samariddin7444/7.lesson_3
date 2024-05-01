from django.urls import path
from .views import LandingPageApiView,ArtistPageApiView,AlbumPageApiView,TracksPageApiView
urlpatterns = [
    path('landing/', LandingPageApiView.as_view(), name='landing'),
    path('artists/', ArtistPageApiView.as_view(), name='artist'),
    path('albums/', AlbumPageApiView.as_view(), name='album'),
    path('tracks/', TracksPageApiView.as_view(), name='tracks'),
]