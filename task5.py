import json
from task1 import scrape_top_list
from task4 import  movie_details

with open("mytask1.json","r") as file:
    data = json.load(file)

movies=scrape_top_list()
def get_movie_list_details():
    list=[]
    for i in data:
        a=i["URL"]
        # print(a)
        b= movie_details(a)
        list.append(b)
        # print(list)
    with open ("task5.json", "w+") as f:
        json.dump(list,f, indent=4)
    return list
get_movie_list_details()  
