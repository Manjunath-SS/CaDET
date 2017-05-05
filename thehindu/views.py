from django.http import HttpResponse
from django.template import Context, loader
import urllib.request
from .models import Thehindu
import ast, re, datetime, requests

def thehindu(request):
    try:
        #page=urllib.request.urlopen('https://newsapi.org/v1/articles?source=the-hindu&sortBy=top&apiKey=0ca6ea2df18e4d128f1490601cfa5785')
        #extracted_data=page.read()
        #string_data=str(extracted_data,'utf-8')
        '''response=requests.get('https://newsapi.org/v1/articles?source=the-hindu&sortBy=top&apiKey=0ca6ea2df18e4d128f1490601cfa5785', verify=False)
        extracted_data=response.content
        string_data=str(extracted_data,'utf-8')
        regex = r"\[.*\]"
        lists=re.findall(regex,string_data)
        li=''.join(lists)
        regex2 = r"\{.*\}"
        list2=re.findall(regex2,li)
        strng=''.join(list2)'''
        strng='{\"author\":\"Suhasini Haidar\",\"title\":\"South Asian leaders pat Modi for gifting satellite to the region\",\"description\":\"PM hosts ‘Mini-SAARC summit’ via video-conferencing after GSLV launch.\",\"url\":\"http://www.thehindu.com/news/national/south-asian-leaders-pat-modi-for-gifting-satellite-to-the-region/article18393669.ece\",\"urlToImage\":\"http://www.thehindu.com/news/national/article18393668.ece/ALTERNATES/LANDSCAPE_615/06THSATELLITE-PG10\",\"publishedAt\":\"2017-05-05T16:04:48Z\"},{\"author\":\"K. Venkateshwarlu, S.Murali\",\"title\":\"Forced out of the forest\",\"description\":\"For the Chenchus, the Nallamala forest is their home. Not any longer after a National Tiger Conservation Authority order stripped them of their rights in a bid to fortify India’s largest tiger reserve. K. Venkateshwarlu and S. Murali report\",\"url\":\"http://www.thehindu.com/news/national/andhra-pradesh/chenchus-of-nallamala-forest-forced-out-of-the-forest/article18394340.ece\",\"urlToImage\":\"http://www.thehindu.com/news/national/andhra-pradesh/article18394336.ece/ALTERNATES/LANDSCAPE_615/06THCHENCHUTRIBE2\",\"publishedAt\":\"2017-05-05T19:08:09Z\"},{\"author\":\"Krishnadas Rajagopal\",\"title\":\"Is gender justice only on paper, asks woman judge\",\"description\":\"Member of Nirbhaya case Bench Justice R. Banumathi rues how crimes against women go on despite legislation meant to deter them\",\"url\":\"http://www.thehindu.com/news/national/nirbhaya-case-is-gender-justice-only-on-paper-asks-woman-judge/article18394193.ece\",\"urlToImage\":\"http://www.thehindu.com/news/national/article18211099.ece/ALTERNATES/LANDSCAPE_615/25THPRIYASC\",\"publishedAt\":\"2017-05-05T19:26:38Z\"},{\"author\":\"Smita Gupta\",\"title\":\"Presidential polls: ‘Neutral parties’ in demand\",\"description\":\"CPI(M) general secretary Sitaram Yechury meets Naveen Patnaik; he will soon be talking to YSR Congress and DMK.\",\"url\":\"http://www.thehindu.com/news/national/in-presidential-polls-opposition-parties-target-support-of-neutral-parties/article18393921.ece\",\"urlToImage\":\"http://www.thehindu.com/news/national/article18393920.ece/ALTERNATES/LANDSCAPE_615/05THPRIYANAVEEN11\",\"publishedAt\":\"2017-05-05T17:02:36Z\"},{\"author\":\"Suhasini Haidar\",\"title\":\"India’s stance on forum irks China\",\"description\":\"Beijing likens Dalai Lama visit to Arunachal to a ‘sting’ for bilateral relations\",\"url\":\"http://www.thehindu.com/news/national/indias-stance-on-forum-irks-china/article18393829.ece\",\"urlToImage\":\"http://www.thehindu.com/news/national/article18393828.ece/ALTERNATES/LANDSCAPE_615/TH-6-CHINASILKROAD\",\"publishedAt\":\"2017-05-05T17:54:13Z\"},{\"author\":\"Special Correspondent\",\"title\":\"‘Good chance of normal monsoon in south India’\",\"description\":\"Monsoon arrival could be on time in June first week in Kerala and gradually spread across the country in the next few days.\",\"url\":\"http://www.thehindu.com/news/national/good-chance-of-normal-monsoon-in-south-india/article18393817.ece\",\"urlToImage\":\"http://www.thehindu.com/news/national/article12229089.ece/ALTERNATES/LANDSCAPE_615/IMD2\",\"publishedAt\":\"2017-05-05T16:20:12Z\"},{\"author\":\"Smita Gupta\",\"title\":\"DMK plans unifying birthday for Karunanidhi\",\"description\":\"Personal invitations to key leaders.\",\"url\":\"http://www.thehindu.com/news/national/stalin-plans-unifying-birthday-for-patriarch/article18393583.ece\",\"urlToImage\":\"http://www.thehindu.com/news/national/article18393582.ece/ALTERNATES/LANDSCAPE_615/05THPRIYAKARUNANIDHI\",\"publishedAt\":\"2017-05-05T16:51:02Z\"},{\"author\":\"VARGHESE K. GEORGE\",\"title\":\"America stares at a health scare\",\"description\":\"New health care bill could exclude 24 mn people from insurance coverage\",\"url\":\"http://www.thehindu.com/news/international/america-stares-at-a-health-scare/article18393808.ece\",\"urlToImage\":\"http://www.thehindu.com/news/international/article18392657.ece/ALTERNATES/LANDSCAPE_615/USA-HEALTHCARE\",\"publishedAt\":\"2017-05-05T19:27:18Z\"},{\"author\":\"\",\"title\":\"All for one? : On Congress\' strategy to contest in presidential poll\",\"description\":\"Congress will need to reach out to friends and foes to make a contest of the presidential poll\",\"url\":\"http://www.thehindu.com/opinion/editorial/on-congresss-strategy-for-presidential-elections/article18394225.ece\",\"urlToImage\":\"http://www.thehindu.com/static/theme/default/base/img/og-image.jpg\",\"publishedAt\":\"2017-05-05T18:36:25Z\"},{\"author\":\"\",\"title\":\"Put cricket first: On BCCI being forced to name team for Champions Trophy\",\"description\":\"It reflects poorly on the BCCI that it has to be forced to name a team for Champions Trophy\",\"url\":\"http://www.thehindu.com/opinion/editorial/on-bcci-being-forced-to-name-a-team-for-champions-trophy/article18394238.ece\",\"urlToImage\":\"http://www.thehindu.com/static/theme/default/base/img/og-image.jpg\",\"publishedAt\":\"2017-05-05T19:10:11Z\"}'
        mydict=ast.literal_eval(strng)

        for tup in mydict:
            if not Thehindu.objects.filter(title=tup['title']):
                if not tup['author']:
                    tup['author']="Anonymous"
                Thehindu.objects.create(author=tup['author'],title=tup['title'],description=tup['description'],url=tup['url'],imgurl=tup['urlToImage'],pubat=tup['publishedAt'])

    finally:
        today = datetime.datetime.today()
        rec=Thehindu.objects.all().order_by('-pubat')
        tmpl = loader.get_template("TheHindu.html")
        cont = Context({'Thehindu': rec, 'Daa': today})
        return HttpResponse(tmpl.render(cont))
