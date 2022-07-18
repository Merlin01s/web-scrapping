from bs4 import BeautifulSoup
from task1 import scrape_top_list
import requests
import json
url="https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse"
# print(url)

def movie_details(movie_url):
    res=requests.get(movie_url)
    soup = BeautifulSoup(res.text,"html.parser") 
    h1=soup.find("h1", class_="scoreboard__title").get_text()
    li=soup.find_all("li",class_="meta-row clearfix")
    dic={}
    for k in li:
        f=k.text
        b=f.split()
        for j in b:
            if "Rating" in j:
                dic["Name"]=h1
                dic["Rating"]=b[1:2]
            if "Genre:" in j:
                k=b[1:]
                g=" "
                for i in k:
                    g+=i
                g=g.split(",")
                # print(g)
                
                dic["Genre"]=g
                # print(dic)
            if "Language" in j:
                dic['Language']=b[2:]
              
            if "Director" in j:
                k=b[1:]
                h = ""
                # print(w)

                for c in k:
                    h += c
                # print(h)
                h = h.split(",")
                # print(h)

                dic["Director"]= h
                # print(dic)
            if "Producer" in b:
                k=b[1:]
                v=" "
                for c in k:
                    v+=c
                v=v.split(",")
                dic["Producer"]=v
            if "Runtime" in j:
                s=b[1:]
                i=0
                while i<len(s):
                    hour=s[0][0]
                    mint=s[1]
                    min=mint[:-1]
                    i+=1
                tom=int(hour)*60+int(min)
                dic["Runtime"]=tom
            
        
    with open("mytask4.json","w+") as file:
        json.dump(dic,file,indent = 4)
        b=json.dumps(dic)
    return dic
movie_details(url)