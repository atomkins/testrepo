# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:16:25 2018

@author: atomki200
"""

from django.http import HttpResponse # allows us return information as http response
from django.shortcuts import render # allows us to send to an html template
import operator

def home(request):
    return render(request, 'home.html')

def stats(request):
    return HttpResponse('Stats page')

def about(request):
    return render(request, 'about.html')

def count(request):
    textval = request.GET['fulltext']
    wordlist = textval.split()
    
    word_dict = {}
    for word in wordlist:
        if word in word_dict:
            word_dict[word] += 1
        else:
            # add word
            word_dict[word] = 1
    # Turn the dictionary into a list and sort it.
    sortedWords = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
        
    return render(request, 'count.html', {'mytext': textval, 'countwords': len(wordlist), 'word_dict': word_dict, 'word_list': word_dict.items(), 'sort_list': sortedWords })




