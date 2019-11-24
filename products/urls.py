from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add, name='add'),
    path('<slug:title>',views.info, name='info'),
    path('<slug:title>/upvote',views.upvote, name='upvote'),
]
