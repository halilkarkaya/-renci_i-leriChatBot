from django import forms
from .models import Sikayet

class SikayetForm(forms.ModelForm):
    class Meta:
        model = Sikayet
        fields = ['ogrenci_no', 'ad_soyad', 'email', 'sikayet_konusu', 'sikayet_metni']
        widgets = {
            'sikayet_metni': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'ogrenci_no': 'Öğrenci Numarası',
            'ad_soyad': 'Ad Soyad',
            'email': 'E-posta',
            'sikayet_konusu': 'Şikayet Konusu',
            'sikayet_metni': 'Şikayet Detayı',
        } 