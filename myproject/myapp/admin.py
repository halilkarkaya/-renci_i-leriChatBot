from django.contrib import admin
from .models import Sikayet

@admin.register(Sikayet)
class SikayetAdmin(admin.ModelAdmin):
    list_display = ('ogrenci_no', 'ad_soyad', 'sikayet_konusu', 'tarih', 'durum')
    list_filter = ('durum', 'tarih')
    search_fields = ('ogrenci_no', 'ad_soyad', 'sikayet_konusu')
    readonly_fields = ('tarih',)
