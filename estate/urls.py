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
    AssignToHouseView
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
    path("houses/<int:pk>/assign/", AssignToHouseView.as_view(), name="house-assign"),
    path("houses/<int:pk>/remove/", AssignToHouseView.as_view(), name="house-remove"),
]

app_name = "estate"
