from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response


def index(request):
    var="abc"
    print("hell")
    return render_to_response('login.html')
