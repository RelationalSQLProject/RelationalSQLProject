from django.shortcuts import render

# Create your views here.

def store_view(request):
    context = {}
    return render(request, 'listings/store.html', context=context)