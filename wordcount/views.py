from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordList = fulltext.split()

    wordDict = {}

    for word in wordList:
        if word in wordDict:
            #Increase
            wordDict[word][0] = wordDict[word][0] + 1
        else:
            # Create list in dict
            wordDict[word] = [1]

    df = pd.DataFrame.from_dict(wordDict, orient='index')

    print(df)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordList), 'wordDict':df})