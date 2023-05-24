from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def app2_string(request):
    return HttpResponse('<h2>this is app2_string page</h2>')
def app2_htmlpage(request):
    return render(request,'app2_htmlpage.html')