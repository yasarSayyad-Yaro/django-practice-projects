from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('login/',views.loginpage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerpage,name="register"),
    path('user-profile/<str:pk>',views.user_profile,name="user-profile"),


    path('',views.home,name="home"),
    path('room/<int:pk>/',views.room,name="room"),
    path('create_room/',views.create_room,name="create_room"),
    path('update_room/<int:pk>',views.update_room,name="update_room"),
    path('delete_room/<int:pk>',views.delete_room,name="delete_room"),
    path('my-rooms/', views.my_rooms, name='my_rooms'),  

    path('update_message/<int:pk>',views.update_message,name="update_message"),
    path('delete_message/<int:pk>',views.delete_message,name="delete_message"),



    path("__reload__",include("django_browser_reload.urls")),
]