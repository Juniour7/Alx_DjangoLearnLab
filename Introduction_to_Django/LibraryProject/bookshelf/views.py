from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import datetime

# Create your views here.
def say_hello(request):
    """This returns the words Hello World"""
    return HttpResponse("Hello There")

def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html lang="en"><body>It is now %s.</body></html>' % now
    return HttpResponse(html)

def template_view(request):
    """Renders a Html document"""
    return render(request, 'hello.html')

class HelloView(TemplateView):
    """This is a class based view"""
    template_name = 'hello.html'
