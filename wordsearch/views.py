from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import search_here, constraints
from django.contrib import messages
import json


# Create your views here.
# Total three functions are created as mentioned in urls file
# search_word function is to render html page where frontend page is set up
# auto_search for getting data from user and convert it to lower if it id capital word by initial
# get_results function is to verify conditions to return final output


def search_word(request):
    return render(request, 'page3.html', {})  # home page is designed through page4.html


def auto_search(request):
    if request.is_ajax():
        text = request.GET.get('term', '')
        results = constraints(search_here(text.lower()), text.lower())
        data = json.dumps(results)  # results after conversion
    else:
        data = 'fail'
    type = 'application/json'
    return HttpResponse(data, type)


def get_results(request):
    if request.method == 'GET':
        text = request.GET.get('term') # for example: query = 'hello'
        if text:
            search_result = constraints(search_here(text.lower()), text.lower())
            if len(search_result) == 0:
                messages.info(request, f"No word as:  {text}")   # Dynamic presentation of unknown word
                return redirect('/')  # redirect to homepage if no word found
            else:
                return JsonResponse({'Search_Result': search_result})  # Json format of final list of words as values
        else:
            messages.info(request, "Please enter atleast one letter")
            return redirect('/')  # if text box is searched empty then this will execute



