from django.shortcuts import render_to_response
import re
import urllib.request
from .models import Thehindu

def thehindu(request):
    page=urllib.request.urlopen('https://newsapi.org/v1/articles?source=the-hindu&sortBy=top&apiKey=0ca6ea2df18e4d128f1490601cfa5785')
    extracted_data=page.read()
    string_data=str(extracted_data,'utf-8')
    filtrd=string_data.replace("\"", "")

    pattern = r'(author:)|(description:)|(title:)|(url:)|(urlToImage:)|(publishedAt:)'
    for match in re.finditer(pattern, lists):
        s = match.start()
        e = match.end()

    ult={"title":lists}

    return render_to_response('TheHindu.html',ult)
