from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings 
import csv
from searchString.models import Searchword
from django.core import serializers


# Create your views here.

def index(request):
    return HttpResponse("hello, world") 

def checkdata(request):
    if Searchword.objects.all().count() == 0:
        # read the provided dataset file and store in database
        superfile = open(os.path.join(settings.PROJECT_ROOT, 'word_search.tsv'))
        s = superfile.readlines()
        for lines in s:
            #elimination spaces between words and counts
            wordArray = lines.split('\t')
            secondWord = wordArray[1].split('\n')
            word = wordArray[0]
            occurance = int(secondWord[0])
            q = Searchword(word = word, occurance = occurance)
            q.save()
    return HttpResponse("check")

def getFormdata(request):
    if request.method == 'GET':
        inputstring = request.GET.get('q', '')
        # creating two empty array to store objects using filters
        array1 = []
        array2 = []
        # loop through all objects to find the string required
        for record in Searchword.objects.all():
            # if there is subtring in the objects word then index will be greater then -1
            # and we get the desired result
            if record.word.find(inputstring) > -1:
                if record.word.find(inputstring) == 0:
                    array1.append(record)
                else:
                    array2.append(record)
        # now sorting the array according to the occurance and length of the word
        #firstly writing the logic to sort the array when the words having the same occurance but different length
        #sortLengthwise = sorted(array1,key = lambda x:len(x.word))

        # sorted according to occurance of the word as well as length of the word for array1
        supernewarr1 = sorted(sorted(array1, key=lambda x: len(x.word)), key = lambda x: x.occurance, reverse = True)
        supernewarr2 = sorted(sorted(array2, key = lambda y:len(y.word)), key = lambda y:y.occurance, reverse = True)

        #Merging array1 and array2 to get total possibility of the all the possible word
        for elements in supernewarr2:
            supernewarr1.append(elements)
        
        # cutting the result to 25 words
        finalCutarray = supernewarr1[:25]
        print(len(finalCutarray))
        #serializing the data in json format

        data = serializers.serialize("json", finalCutarray)

    return HttpResponse(data)