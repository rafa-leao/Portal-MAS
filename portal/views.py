from django.shortcuts import render

def portal_view(request):

    return render(request, "index.html")
