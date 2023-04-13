from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegisterView.as_view()),
    path('login', views.LoginView.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('users', views.UserView.as_view()),
    path('users/update/<int:user_id>', views.UserUpdateView().as_view()),
    # path('users', views.UserList.as_view(), name='user-list'),
    # path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('followers', views.FollowerList.as_view(), name='follower-list'),
    path('followers/<int:pk>', views.FollowerDetail.as_view(), name='follower-detail'),
    path('favorites', views.FavoriteList.as_view(), name='favorite-list'),
    path('favorites/<int:pk>', views.FavoriteDetail.as_view(), name='favorite-detail'),
    path('likes', views.LikeList.as_view(), name='like-list'),
    path('likes/<int:pk>', views.LikeDetail.as_view(), name='like-detail'),
    path('lists', views.ListList.as_view(), name='list-list'),
    path('lists/<int:pk>', views.ListDetail.as_view(), name='list-detail'),
    path('listitems', views.ListItemList.as_view(), name='listitem-list'),
    path('listitems/<int:pk>', views.ListItemDetail.as_view(), name='listitem-detail'),
    path('trackers', views.TrackerList.as_view(), name='tracker-list'),
    path('trackers/<int:pk>', views.TrackerDetail.as_view(), name='tracker-detail'),
    path('tracker/items', views.TrackerItemList.as_view(), name='trackeritem-list'),
    path('tracker/items/<int:pk>', views.TrackerItemDetail.as_view(), name='trackeritem-detail'),
    path('tracker/fields', views.TrackerFieldList.as_view(), name='trackerfield-list'),
    path('tracker/fields/<int:pk>', views.TrackerFieldDetail.as_view(), name='trackerfield-detail'),
    path('tracker/items', views.TrackerItemList.as_view(), name='trackeritem-list'),
    path('tracker/items/<int:pk>', views.TrackerItemDetail.as_view(), name='trackeritem-detail'),
    path('tracker/item/values', views.TrackerItemValueList.as_view(), name='trackeritemvalue-list'),
    path('tracker/item/values/<int:pk>', views.TrackerItemValueDetail.as_view(), name='trackeritemvalue-detail'),
    path('folders', views.FolderList.as_view(), name='folder-list'),
    path('folders/<int:pk>', views.FolderDetail.as_view(), name='folder-detail'),
    path('folder/lists', views.ListInFolderList().as_view(), name='listinfolder-list'),
    path('folder/lists/<int:pk>', views.ListInFolderDetail().as_view(), name='listinfolder-detail'),
    path('folder/trackers', views.TrackerInFolderList().as_view(), name='trackerinfolder-list'),
    path('folder/trackers/<int:pk>', views.TrackerInFolderDetail().as_view(), name='trackerinfolder-detail'),
]