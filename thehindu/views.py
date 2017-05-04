from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context, loader
import re
import urllib.request
from .models import Thehindu
import ast

def thehindu(request):
    page=urllib.request.urlopen('https://newsapi.org/v1/articles?source=the-hindu&sortBy=top&apiKey=0ca6ea2df18e4d128f1490601cfa5785')
    extracted_data=page.read()
    string_data=str(extracted_data,'utf-8')
    regex = r"\[.*\]"
    lists=re.findall(regex,string_data)
    li=''.join(lists)
    regex2 = r"\{.*\}"
    list2=re.findall(regex2,li)
    strng=''.join(list2)
    mydict=ast.literal_eval(strng)

    for tup in mydict:
        if not Thehindu.objects.filter(title=tup['title']):
            Thehindu.objects.create(author=tup['author'],title=tup['title'],description=tup['description'],url=tup['url'],imgurl=tup['urlToImage'],pubat=tup['publishedAt'])

    rec=Thehindu.objects.all()
    tmpl = loader.get_template("TheHindu.html")
    cont = Context({'Thehindu': rec})
    return HttpResponse(tmpl.render(cont))

    #return render_to_response('TheHindu.html')
