from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getResource/', views.getResource, name='resource'),
    path('getMeeting/', views.getMeeting, name='meeting'),
    path('meetingdetail/<int:id>', views.meetingdetail, name='meetingdetail'),
    path('newResource/', views.newResource, name='newresource'), 
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]
 


