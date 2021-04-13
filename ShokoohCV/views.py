from django.shortcuts import render

from cvsetting.models import SiteSetting


def home_page(request):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting,

    }

    return render(request, 'home.html', context)
