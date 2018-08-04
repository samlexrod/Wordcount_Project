from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordList = fulltext.split()

    wordDict = {}

    for word in wordList:
        if word in wordDict:
            #Increase
            wordDict[word] += 1
        else:
            # Create list in dict
            wordDict[word] = 1

    df = pd.DataFrame.from_dict(wordDict, orient='index')

    sorted_words = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordList), 
                    'wordDict':sorted_words})

def about(request):
    return render(request, 'about.html')