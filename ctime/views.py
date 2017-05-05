from django.shortcuts import render_to_response
import datetime

def home(request):
    today = datetime.datetime.today()
    con={'Daa' : today}
    return render_to_response('home.html',con)
