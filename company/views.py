from django.http import HttpResponse
from django.shortcuts import render

from .forms import *
from .models import *


def detail(request, company_name):
    form = SearchForm()

    esg_object = ESG.objects.filter(ticker__contains=company_name).first()
    sustainable_object = Sustainable.objects.filter(ticker__contains=company_name).first()
    sp_gloabl_object = SPGlobal.objects.filter(ticker__contains=company_name).first()

    return render(request, 'detail.html', {
        'form': form, 
        'company': {
            'name': esg_object.name,
            'ticker': esg_object.ticker,
            'country': esg_object.country,
            'industry': esg_object.industry,
            'esg_score': sp_gloabl_object.esg_score,
            'environmental_score': sp_gloabl_object.environmental_score,
            'social_score': sp_gloabl_object.social_score,
            'governance_score': sp_gloabl_object.governance_score,
            'rating': esg_object.rating,
            'comparison': esg_object.comparison,
        }
    })

def index(request):
    return render(request, 'index.html')


def sp_data_analytics(request):
    return render(request, 'sp_data_analytics.html')


def msci_data_analytics(request):
    return render(request, 'msci_data_analytics.html')


def esg_score(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EstimateForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            score = (0.371559 * form.cleaned_data['social_score']) + (0.198854 * form.cleaned_data['environmental_score']) + (0.408538 * form.cleaned_data['governance_score'])

            # redirect to a new URL:
            return render(request, 'esg_score.html', {
                'form': form, 
                'score': round(score, 2)
            })
    else:
        form = EstimateForm()
    return render(request, 'esg_score.html', {'form': form, 'score': 0})


def search(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # redirect to a new URL:
            return detail(request=request, company_name=form.cleaned_data['name'])
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()
    return render(request, 'index.html', {'form': form})
