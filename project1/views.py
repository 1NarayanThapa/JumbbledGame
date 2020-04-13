from django.http import HttpResponse



def home(request):
    return HttpResponse("<h2>i am success</h2>")