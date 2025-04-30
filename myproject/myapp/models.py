from django.db import models

# Create your models here.

class Sikayet(models.Model):
    ogrenci_no = models.CharField(max_length=20, verbose_name="Öğrenci Numarası")
    ad_soyad = models.CharField(max_length=100, verbose_name="Ad Soyad")
    email = models.EmailField(verbose_name="E-posta")
    sikayet_konusu = models.CharField(max_length=200, verbose_name="Şikayet Konusu")
    sikayet_metni = models.TextField(verbose_name="Şikayet Detayı")
    tarih = models.DateTimeField(auto_now_add=True, verbose_name="Şikayet Tarihi")
    durum = models.BooleanField(default=False, verbose_name="Çözüldü mü?")

    class Meta:
        verbose_name = "Şikayet"
        verbose_name_plural = "Şikayetler"
        ordering = ['-tarih']

    def __str__(self):
        return f"{self.ogrenci_no} - {self.sikayet_konusu}"
