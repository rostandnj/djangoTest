from django.urls import path

from . import views
app_name = 'users'
urlpatterns = [
    path('', views.index, name='user_index'),
    path('create_user', views.createUser, name='user_add'),
]