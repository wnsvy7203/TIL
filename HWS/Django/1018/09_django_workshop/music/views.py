from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Artist, Music
from .serializers import (ArtistListSerializer, ArtistSerializer,
                          MusicListSerializer, MusicSerializer)


@api_view(['GET', 'POST'])
def artist_list(request):
    if request.method == 'GET':
        # artists = Artist.objects.all()
        artists = get_list_or_404(Artist)
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtistListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def artist_detail(request, artist_pk):
    # artist = Artist.objects.get(pk=artist_pk)
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)


@api_view(['POST'])
def music_create(request, artist_pk):
    # artist = Artist.objects.get(pk=artist_pk)
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = MusicListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(artist=artist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def music_list(request):
    # musics = Music.objects.all()
    musics = get_list_or_404(Music)
    serializer = MusicListSerializer(musics, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def music_detail(request, music_pk):
    # music = Music.objects.get(pk=music_pk)
    music = get_object_or_404(Music, pk=music_pk)

    if request.method == 'GET':
        serializer = MusicListSerializer(music)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        music.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
