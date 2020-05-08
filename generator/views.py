from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
    return render(request, 'generator/index.html')

def about(request):
    return render(request, 'generator/about.html')


def password(request):
    # list constructor puts into indivdual strings into a list
    characters = list('abcdefghijklmnopqrstuvwxyz')  
    
    # check to see if uppercase is requested and if yes, then extend list
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    # check to see if special characters are requested and if yes, then extend list
    if request.GET.get('special'):
        characters.extend(list('!@#$%^()'))
    
    # check to see if numbers are requested and if yes, then extend list
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 9))

    randomizedPwd = ''
    for x in range(length):
        randomizedPwd += random.choice(characters)
    
    context = {'password': randomizedPwd}
    return render(request, 'generator/password.html', context)