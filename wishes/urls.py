from django.urls import path
from .views import (homeView,
                    createWishView,
                    editWishView,
                    deleteWish,
                    grantWish,
                    likeWish,
                    statsView
                    )

app_name = 'wishes'
urlpatterns = [
    path("", homeView, name="home"),
    path("new/", createWishView, name="create-wish"),
    path("edit/<str:pk>/", editWishView, name="edit-wish"),
    path('delete/<str:pk>/', deleteWish, name="delete-wish"),
    path('grant/<str:pk>/', grantWish, name="grant-wish"),
    path('like/<str:pk>/', likeWish, name="like-wish"),
    path("stats/", statsView, name="stats"),
]
