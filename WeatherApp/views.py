from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
import urllib.request
import json
from django.utils.timezone import localtime
import datetime




class Weather_1(TemplateView):
    template_name = 'weather2.html'
    
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+ city + 
                                        '&units=metric&appid=2efeaddddfd43f52f170e287fedad2fc')
        data_list = json.load(source)
        

        data = {
            "country_code": data_list['sys']['country'],
            "coordinate": str(data_list['coord']['lon']) +','+str(data_list['coord']['lat']),
            "temp": str(data_list['main']['temp']) +' °F',
            "pressure": str( data_list[ 'main']['pressure']),
            "humidity": str(data_list['main' ]['humidity' ]),
            "main": str(data_list[ 'weather' ][0]['main' ]),
            'description': str(data_list[ 'weather'][0]['description']),
            "icon": data_list[ 'weather' ][0]['icon'],
            "day" : datetime.date.today(),
            "city":city,   
            "today":localtime().time(),    
            }
        
        # print(data)
    else:
        data ={}

    return render(request,'weather1.html',data)
