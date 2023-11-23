import views
from django.urls import path

import choyxonatech_app
from . import views
from .views import *

app_name = 'choyxonatech_app'

urlpatterns = [
    path('login/', choyxonatech_app.views.LoginPage, name='login'),
    path('', home, name='home'),
    # path('update_user/<int:id>', update_user, name='update-user'),
    path('messages/', messages, name='messages'),
    path('chat/', chat,  name='chat'),

]