from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RealtorCreationForm, RealtorUpdateForm, RealtorUsernameSearchForm, HouseSearchForm

from .models import (
    House,
    Realtor,
)


def index(request):
    num_houses = House.objects.count()
    num_realtors = Realtor.objects.count()

    context = {
        "num_houses": num_houses,
        "num_realtors": num_realtors,
    }

    return render(request, "estate/index.html", context=context)


class RealtorListView(generic.ListView):
    model = Realtor
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RealtorListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username", "")

        context["search_form"] = RealtorUsernameSearchForm(
            initial={"username": username})
        return context

    def get_queryset(self):
        queryset = Realtor.objects.all()
        form = RealtorUsernameSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"])

        return super().get_queryset()


class RealtorDetailView(generic.DetailView):
    model = Realtor


class RealtorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Realtor
    fields = "__all__"
    form = RealtorCreationForm
    success_url = reverse_lazy("estate:realtor-list")


class RealtorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Realtor
    fields = "__all__"
    form = RealtorUpdateForm
    success_url = reverse_lazy("estate:realtor-list")


class RealtorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Realtor
    success_url = reverse_lazy("estate:realtor-list")
    queryset = Realtor.objects.all().prefetch_related("house")


class HouseListView(generic.ListView):
    model = House
    paginate_by = 3
    queryset = House.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HouseListView, self).get_context_data(**kwargs)

        price = self.request.GET.get("price", "")

        context["search_price_form"] = HouseSearchForm(
            initial={"price": price})
        return context

    def get_queryset(self):
        queryset = House.objects.all()
        form = HouseSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                price__icontains=form.cleaned_data["price"])

        return super().get_queryset()


class HouseDetailView(generic.DetailView):
    model = House

    def get_queryset(self):
        houses = House.objects.all()
        for house in houses:
            if house.area != 0:
                house.price_per_area = round(house.price / house.area)
            else:
                house.price_per_area = None
        return houses


class HouseCreateView(LoginRequiredMixin, generic.CreateView):
    model = House
    fields = "__all__"
    success_url = reverse_lazy("estate:house-list")


class HouseUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = House
    fields = "__all__"
    success_url = reverse_lazy("estate:house-list")


class HouseDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = House
    success_url = reverse_lazy("estate:house-list")


@login_required
def toggle_assign_to_house(request, pk):
    realtor = Realtor.objects.get(id=request.user.id)
    if (
        House.objects.get(id=pk) in realtor.house.all()
    ):
        realtor.house.remove(pk)
    else:
        realtor.house.add(pk)
    return HttpResponseRedirect(reverse_lazy("estate:house-detail", args=[pk]))
