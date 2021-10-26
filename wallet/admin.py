from django.contrib import admin

from .models import Wallet, AppTransaction


admin.site.register(Wallet)
admin.site.register(AppTransaction)