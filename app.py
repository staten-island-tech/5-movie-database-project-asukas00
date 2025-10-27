import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

""" for i in data:
    print(i["title"]) """


""" user_input = int(input("Are there any movies you’d like to watch that were released after a certain year?"))
 """
""" for i in data:
    if i["year"] >= user_input:
        print(i["title"]) """

user_input = int(input("Are there any movies you’d like to watch that were released during a certain year?"))

for i in data:
    if i["year"] == user_input:
        print(i["title"])
""" 
user_input = int(input("Are there any movies you’d like to watch that were released before and after a certain year?"))

for i in data:
    if i["year"] >= user_input and i["year"] <= user_input:
        print(i["title"] ) """