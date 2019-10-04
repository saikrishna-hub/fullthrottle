from django.contrib import admin
from django.urls import path
from . import views
from .views import search_word, auto_search, get_results

# all urls of wordsearch app is mentioned here after creating this file which by default doesn't exists
# Finally include this url pge in main project url page

urlpatterns = [
    path('', views.search_word, name='search_word'),
    path('search/', auto_search, name = 'search_results'),
    path('search_results/', get_results, name='getSearchResults'),

]