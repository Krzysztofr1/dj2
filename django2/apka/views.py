from django.shortcuts import render, HttpResponse

def test(request):
    return HttpResponse("<p>{{ item.name }}</p>{% endfor %}")
def index(request, id):
    return HttpResponse("<p>{{ item.name }}</p>{% endfor %}")