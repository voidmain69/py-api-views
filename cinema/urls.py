from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
)

actions_list = {
    "get": "list",
    "post": "create",
}

actions_detail = {
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
}

cinema_halls_list = CinemaHallViewSet.as_view(actions=actions_list)
cinema_halls_detail = CinemaHallViewSet.as_view(actions=actions_detail)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", cinema_halls_list, name="cinema-halls"),
    path(
        "cinema_halls/<int:pk>/",
        cinema_halls_detail,
        name="cinema-halls-detail",
    ),
]

app_name = "cinema"
