from django.http import JsonResponse
from django.shortcuts import render, redirect
import requests

from .models import Dict

def home(request):
    if request.method=='POST':
        text = request.POST['text']

        try:
            response = requests.get('https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=ru&dt=t&q=' + text)
            trans_text = response.json()[0][0][0]
            dicts= Dict(eng=text, rus=trans_text)
            dicts.save()
            return redirect('home')


        except Exception as e:
            print('Ошибка при переводе:', e)

    dicts = Dict.objects.all()[::-1]

    contex={
        'dicts': dicts,
        'len':len(dicts)
    }
    return render(request, 'app/home.html',contex)


def delete(request, pk):
    try:
        d = Dict.objects.get(pk=pk)
        d.delete()
    except:
        pass
    return redirect('home')