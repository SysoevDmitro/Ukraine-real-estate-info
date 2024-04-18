from django.shortcuts import render
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
