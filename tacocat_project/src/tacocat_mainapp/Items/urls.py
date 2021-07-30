from django.urls import path
from . import views


urlpatterns = [
    path('', views.topics, name="topics"),
    # i need to know two things:
    # does leaving it blank mean that it already sees the path join/ and
    # will every path be an extension of join/
    # path('createuser/', views.createUser, name="createuser"),
    # path('createuser/confirmed/', views.confirmation, name="confirm"),
]

