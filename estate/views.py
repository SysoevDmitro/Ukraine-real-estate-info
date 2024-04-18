from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import HouseSearchForm

from .models import (
    House,
    Realtor,
)


def index(request):
    num_houses = House.objects.count()
    num_realtors = Realtor.objects.count()

    # num_visits = request.session.get("num_visits", 0)
    # request.session["num_visits"] = num_visits + 1

    context = {
        "num_houses": num_houses,
        "num_realtors": num_realtors,
        # "num_visits": num_visits + 1,
    }

    return render(request, "estate/index.html", context=context)


class RealtorListView(generic.ListView):
    model = Realtor
    paginate_by = 5


class HouseListView(generic.ListView):
    model = House
    paginate_by = 5
    queryset = House.objects.all()


class HouseDetailView(generic.DetailView):
    model = House
