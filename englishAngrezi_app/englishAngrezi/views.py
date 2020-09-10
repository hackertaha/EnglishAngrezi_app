from django.shortcuts import render, redirect
from englishAngrezi import models
# from django.contrib.auth.forms import UserCreationForm


def index(request):
    header_data = models.Header.objects.all()
    testimonal_data = models.Testimonals.objects.all()
    social_link_data = models.Social_Links.objects.all()
    arthur_data = models.Arthur_Details.objects.all()
    pricing_data = models.Pricing.objects.all()
    pricing_plan_data = models.Pricing_Plan.objects.all()
    data_list = {
        'header_detail' : header_data,
        'testimonal' : testimonal_data,
        'sociallink' : social_link_data,
        'arthurdetail' : arthur_data,
        'pricingdetail' : pricing_data,
        'pricingplandetail' : pricing_plan_data,
    }
    return render(request, 'website/html/index.html', data_list)


def free_download(request):

    data_list = {

    }
    return render(request, 'website/html/free_download.html', data_list)


# Create your views here.
