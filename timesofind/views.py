from django.http import HttpResponse
from django.template import Context, loader
import re
import urllib.request
from .models import Toi
import ast

def timesofind(request):
    try:
        page2=urllib.request.urlopen('https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=0ca6ea2df18e4d128f1490601cfa5785')
        extracted_data2=page2.read()
        string_data2=str(extracted_data2,'utf-8')
        regex2 = r"\[.*\]"
        lists2=re.findall(regex2,string_data2)
        li2=''.join(lists2)
        regex3 = r"\{.*\}"
        list3=re.findall(regex3,li2)
        strng2=''.join(list3)

        for tup2 in mydict2:
            if not Toi.objects.filter(title=tup2['title']):
                if not tup2['author']:
                    tup2['author']="Anonymous"
                Toi.objects.create(author=tup2['author'],title=tup2['title'],description=tup2['description'],url=tup2['url'],imgurl=tup2['urlToImage'],pubat=tup2['publishedAt'])

    finally:
        rec2=Toi.objects.all().order_by('-pubat')
        tmpl2 = loader.get_template("TimesOfIndia.html")
        cont2 = Context({'Toi': rec2})
        return HttpResponse(tmpl2.render(cont2))
