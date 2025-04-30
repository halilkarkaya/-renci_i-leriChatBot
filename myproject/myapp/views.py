from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .rag_utils import get_rag_response
from .forms import SikayetForm

def home(request):
    if request.method == 'POST':
        form = SikayetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Şikayetiniz başarıyla kaydedildi.')
            return redirect('home')
    else:
        form = SikayetForm()
    
    return render(request, 'home.html', {'form': form})

def cevap_al(request):
    if request.method == 'POST':
        question = request.POST.get('question', '')
        if question:
            response = get_rag_response(question)
            return JsonResponse({'answer': response})
    return JsonResponse({'error': 'Geçersiz istek'}, status=400)