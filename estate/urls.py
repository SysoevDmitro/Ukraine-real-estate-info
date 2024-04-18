from django.urls import path
from .views import (
    index,
    HouseListView,
    HouseDetailView,
    RealtorListView
)

urlpatterns = [
    path("", index, name="index"),
    path("houses/", HouseListView.as_view(), name="house-list"),
    path("houses/<int:pk>", HouseDetailView.as_view(), name="house-detail"),
    path("realtors/", RealtorListView.as_view(), name="realtor-list"),
]

app_name = "estate"
