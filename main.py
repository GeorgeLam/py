import requests
import json

r = {}
start_index = 0
query = input("What would you like to search for? ")


def niceprint(dct):
    print("\n")
    for book in dct:
        for k, v in book.items():
            print("{: >10} {: >10}".format(k, v))
    print("\n")


def search(start_index, query=query):
    base_url = {
        'book': f"https://www.googleapis.com/books/v1/volumes?q={query}&startIndex={start_index}",
        'author': f"https://www.googleapis.com/books/v1/volumes?q=inauthor:{query}"}

    print("Searching for: ", base_url['book'])

    r.update(requests.get(base_url['book']).json())
    tidy_output = []
    for index, item in enumerate(r['items']):
        try:
            authors = ', '.join(item['volumeInfo']['authors'])
        except KeyError:
            authors = "Unknown author"

        tidy_output.append(
            {
                index: f"{item['volumeInfo']['title']} - {authors}",
            }
        )
    niceprint(tidy_output)
    return tidy_output


search(start_index, query)

while(1):
    moreInfo = input(
        "Enter number of book to read about, Z: Back, X: Forward, N: Search ")

    try:
        if(int(moreInfo) >= 0 and int(moreInfo) < 10):
            moreInfo = int(moreInfo)
            print(f"Further details on: {moreInfo}...\n")
            print(
                f"{r['items'][moreInfo]['volumeInfo']['description'][: 400]}...\n\n")

    except KeyError:
        print("No description found!")

    except ValueError:
        if(moreInfo.lower() == "z" and start_index > 0):
            print("Going back a page...")
            start_index -= 10
            search(start_index)
        elif(moreInfo.lower() == "x"):
            print("Going forward a page...")
            start_index += 10
            search(start_index)
        elif(moreInfo.lower() == "n"):
            query = input("What would you like to search for? ")
            search(0, query)
