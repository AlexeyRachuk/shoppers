from django.shortcuts import render

from index.models import Index


# Представление главной страницы
def index(request):
    return render(request, 'index/index.html', {'index_items': Index.objects.all()})
