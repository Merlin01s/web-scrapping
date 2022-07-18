from bs4 import BeautifulSoup
import requests
import json

url="https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/"
sample=requests.get(url)
# print(sample)

soup=BeautifulSoup(sample.text,"html.parser")
# print(soup)

def scrape_top_list():
    list=[]
    main_div=soup.find('div', class_='body_main container')
    # print(main_div)

    td_body= main_div.find('table', class_='table')
    # print(td_body)

    trs=td_body.find_all('tr')
    # print(trs)

    for i in trs:
        dict1={}
        td=i.find_all("td")
        for j in td:
            rank=i.find("td", class_="bold").get_text()[:-1]
            dict1["Rank"]=int(rank)
            
            # print(dict1)    
            rating=i.find("span",class_="tMeterScore").get_text()[1:3]
            dict1["Rating"]=float(rating)
            # print(dict1) 
            reviews=i.find("td",class_="right hidden-xs").get_text()
            dict1["Reviews"]=int(reviews)   
            # print(dict1)
            M_name=i.find("a",class_="unstyled articleLink")["href"][3:]
            dict1["movie_name"]=M_name
            # print(dict1)
            movieurl=i.find("a",class_="unstyled articleLink")["href"]
            url="https://www.rottentomatoes.com" + movieurl
            dict1["URL"]=url
            # print(dict1)
            year=i.find("a",class_="unstyled articleLink").get_text()
            year=year.strip()
            dict1["Year"]=int(year[-5:-1])
        list.append(dict1.copy())
        if {} in list:
            list.remove({})
    with open("mytask1.json","w") as f:
        json.dump(list,f,indent=4)
    return list            
scrape_top_list() 