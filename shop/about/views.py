from django.shortcuts import render

from about.models import About


# Представление страницы «О нас»
def about(request):
    return render(request, 'about/about.html', {'about_items': About.objects.all()})
