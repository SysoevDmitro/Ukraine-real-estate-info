from django.urls import path
from .views import (
    index,
    HouseListView,
    HouseDetailView,
    HouseCreateView,
    HouseUpdateView,
    HouseDeleteView,
    RealtorListView,
    RealtorDetailView,
    RealtorCreateView,
    RealtorUpdateView,
    RealtorDeleteView,
    toggle_assign_to_house
)

urlpatterns = [
    path("", index, name="index"),
    path("houses/", HouseListView.as_view(), name="house-list"),
    path("houses/<int:pk>/", HouseDetailView.as_view(), name="house-detail"),
    path("houses/create/", HouseCreateView.as_view(), name="house-create"),
    path("houses/<int:pk>/update/", HouseUpdateView.as_view(), name="house-update"),
    path("houses/<int:pk>/delete/", HouseDeleteView.as_view(), name="house-delete"),
    path("realtors/", RealtorListView.as_view(), name="realtor-list"),
    path("realtors/<int:pk>/", RealtorDetailView.as_view(), name="realtor-detail"),
    path("realtors/create/", RealtorCreateView.as_view(), name="realtor-create"),
    path("realtors/<int:pk>/update", RealtorUpdateView.as_view(), name="realtor-update"),
    path("realtors/<int:pk>/delete/", RealtorDeleteView.as_view(), name="realtor-delete"),
    path(
        "houses/<int:pk>/toggle-assign/",
        toggle_assign_to_house,
        name="toggle-house-assign",
    ),
]

app_name = "estate"
