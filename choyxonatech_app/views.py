from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
# from .models import Chat, Room, User
from django.contrib.auth.decorators import login_required


# @login_required
def home(request):
    # user_chat = Chat.objects.filter(participants=request.user)
    # context = {'user_chat': user_chat}
    return render(request, 'home.html')


# def room(request):
# return render(request, 'room.html')
# def user(request):
# return render(request, 'user.html')
# def room(request):
# return render(request, 'room.html')
def messages(request):
    return render(request, 'messages.html')


def chat(request):
    return render(request, 'chat.html')


def LoginPage(request):
    return render(request, 'registration.html')
