from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Realtor, House, Owner, Address


@admin.register(Realtor)
class RealtorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("rating",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("rating",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "rating",
                    )
                },
            ),
        )
    )


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    search_fields = ("price", "owner", "address")
    list_filter = ("owner",)
    list_display = ["address", "price", "owner"]


admin.site.register(Address)
admin.site.register(Owner)

