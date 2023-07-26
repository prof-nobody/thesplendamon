from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetails.as_view(), name='post_detail'),
    path('create_post', views.PostCreation.as_view(), name='post_creation')
]
