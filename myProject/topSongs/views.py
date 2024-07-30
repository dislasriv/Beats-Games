from django.shortcuts import render
from .models import Song
# Create your views here.
def topSongsRoot(request):
    return render(request, 'topSongs/topSongsRoot.html', {"songs": Song.objects.all()})
