import requests
import json

query = input("What would you like to search? ")

base_url = {
    'book': f"https://www.googleapis.com/books/v1/volumes?q={query}",
    'author': f"https://www.googleapis.com/books/v1/volumes?q=inauthor:{query}"}

print("Searching for: ", base_url['book'])

r = requests.get(base_url['book'])

output = r.json()
tidy_output = []
for index, item in enumerate(output['items']):
    # query_results = index, item['id'], item['volumeInfo']['title'],
    # item['volumeInfo']['authors']

    try:
        authors = ', '.join(item['volumeInfo']['authors'])
    except KeyError:
        authors = "Unknown author"

    tidy_output.append(
        {
            index: f"{item['volumeInfo']['title']} - {authors}",
        }
    )


def niceprint(dct):
    for person in dct:
        for k, v in person.items():
            print("{: >10} {: >10}".format(k, v))
            # print("{: >20} {: >20}".format(*row))


niceprint(tidy_output)

moreInfo = int(input(
    "Enter number of book to read more about, Z: Back, X: Forward "))

if(type(moreInfo) == int):
    print(
        f"Further details on {moreInfo}: {tidy_output[moreInfo]['title']}...")
    print(output['items'][moreInfo]['volumeInfo']['description'])
