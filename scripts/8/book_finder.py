"""
This script takes a subject as an input and return upto 5 book regarding that subject
"""
import requests # requests allows me to do HTTP requests to a HTTP server

title = input("What title are you looking for: ")

response = requests.get(f"http://openlibrary.org/search.json?title={title}") #curl -X GET url
print(response.status_code)
data = response.json()
top5 = data['docs'][:5]
print(f"{data['numFound']} books are available")

for book in top5:
    print(f"title: {book['title']}, Authors: {book['author_name']} ,publish year: {book['publish_year']}")





