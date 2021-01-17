from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.shortcuts import render
from .form import Fillform
from .models import Title

# Create your views here.
def index(request):
    if request.method=='POST':
        f=Fillform(request.POST)
        if f.is_valid():
            result=formdata(f.cleaned_data['title'])
            t=f.cleaned_data['title']
            data=Title(title=t,title1=result[0],title2=result[1],title3=result[2],title4=result[3],title5=result[4],title6=result[5],title7=result[6],title8=result[7],title9=result[8],title10=result[9])
            data.save()
    else:
        f=Fillform()
    return render(request,'index.html',{'form':f})

def formdata(title):
    PATH ="C:\Program Files (x86)\chromedriver.exe"
    driver =webdriver.Chrome(PATH)
    driver.get("https://medium.com/search?q="+title) 
    tags=driver.find_elements_by_class_name("graf--title")
    result=[]
    for tag in tags:
        result.append(tag.text)
        print(result)
    return result


