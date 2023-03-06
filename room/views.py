from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Room, Message


@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})


@login_required
def add_room(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        room = Room(name=name)
        room.save()

        return redirect('rooms')

    return render(request, 'room/add_room.html')
