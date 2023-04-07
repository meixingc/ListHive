from django.urls import path
from . import views

urlpatterns = [
    path('users', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('followers', views.FollowerList.as_view()),
    path('followers/<int:pk>/', views.FollowerDetail.as_view()),
    path('favorites', views.FavoriteList.as_view()),
    path('favorites/<int:pk>/', views.FavoriteDetail.as_view()),
    path('likes', views.LikeList.as_view()),
    path('likes/<int:pk>/', views.LikeDetail.as_view()),
    path('lists', views.ListList.as_view()),
    path('lists/<int:pk>/', views.ListDetail.as_view()),
    path('listitems', views.ListItemList.as_view()),
    path('listitems/<int:pk>/', views.ListItemDetail.as_view()),
    path('trackers', views.TrackerList.as_view()),
    path('trackers/<int:pk>/', views.TrackerDetail.as_view()),
    path('tracker/items', views.TrackerItemList.as_view()),
    path('tracker/items/<int:pk>/', views.TrackerItemDetail.as_view()),
    path('tracker/fields', views.TrackerFieldList.as_view()),
    path('tracker/fields/<int:pk>/', views.TrackerFieldDetail.as_view()),
    path('tracker/items', views.TrackerItemList.as_view()),
    path('tracker/items/<int:pk>/', views.TrackerItemDetail.as_view()),
    path('tracker/item/values', views.TrackerItemValueList.as_view()),
    path('tracker/item/values/<int:pk>/', views.TrackerItemValueDetail.as_view()),
    path('folders', views.FolderList.as_view()),
    path('folders/<int:pk>/', views.FolderDetail.as_view()),
    path('folder/lists', views.ListInFolderList().as_view()),
    path('folder/lists/<int:pk>/', views.ListInFolderDetail().as_view()),
    path('folder/trackers', views.TrackerInFolderList().as_view()),
    path('folder/trackers/<int:pk>/', views.TrackerInFolderDetail().as_view()),
]