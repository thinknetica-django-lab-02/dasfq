from django.shortcuts import render
from django.contrib.flatpages.models import FlatPage


def IndexView(request):
    queryset = FlatPage.objects.all()
    print(queryset)
    context = {
        'pages': queryset,
    }
    return render(request, 'index.html', context)