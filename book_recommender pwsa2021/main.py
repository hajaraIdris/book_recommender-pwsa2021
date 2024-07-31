import random

global books
global ratings


def read_books_file():
    with open("data/books.txt") as bookFile:
        # line = bookFile.readline()
        list_names = []
        for line in bookFile:
            listed = listed = line.strip().split(",")
            list_names.append(tuple(listed))
        return list_names


def read_ratings_file():
    with open("data/ratings.txt") as F:
        diction = {}

        bookrating = F.readlines()
        length = len(bookrating)

        for index in range(0, length, 2):
            # print("User:",bookrating[index],"Ratings",bookrating[index+1])
            key = bookrating[index].strip()
            val = bookrating[index + 1]
            int_list = []
            for x in val:
                if x.isdigit():
                    int_list.append(int(x))
                else:
                    continue
            diction[key] = int_list

    return diction
    # val = [5,5,0,0,....]

    # convert ratings to list
    # add them to dict as name --> list of ratings


def likedBooks(name):
    #returns indexes of liked books for user.
    global ratings
    list_books = []
    user_ratings = ratings[name]
    length = len(user_ratings)
    for index in range(length):
        if user_ratings[index] >= 3:
            list_books.append(index)

    return list_books

def unreadBooks(name):
    # returns indexes of unliked books for user.
    global ratings
    list_books=[]
    user_ratings = ratings[name]
    length = len(user_ratings)
    for index in range(length):
        if user_ratings[index] == 0:
            list_books.append(index)

    return list_books



def setup():
    global books
    global ratings
    print("Importing books\n")
    books = read_books_file()

    print("Importing ratings\n")
    ratings = read_ratings_file()
    print(ratings)

import numpy as np
def similarityBetween(user_a,user_b):
    global ratings
    user1rating = ratings[user_a]
    user2rating = ratings[user_b]
    recommend = np.dot(user1rating, user2rating)
    return recommend


def most_similar(user):
    global ratings

    users = list(ratings.keys())
    users.remove(user)
    print(users)

    userslist = [(user_b, similarityBetween(user,user_b)) for user_b in users]
    return sorted(userslist,
                  key=lambda x: (x[1], x[0].lower().title()),
                  reverse=True)

def printAndSave(recom):
    output = ""
    for user,recommandations in recom.items():
        output += f"\nBooks Recommended By: {user}"
        print(f"\nBooks Recommended By: {user} \n")

        for author_name, book_title in [books[x] for x in recommandations]:
            output += f" {book_title} Written by  {author_name}"
            print (f" {book_title} Written by  {author_name}")



    with open("output.txt","a") as f:
        f.write(output)
        print("Writing Done")

def recommendationsFor(user, number=10):  # time complexity = o(nm)
    r = {}  # dictionary(key = user , value = books recommended by that user)


    l = [x[0] for x in most_similar(user)]
    i = 0  # i counter for used user
    k = 0  # k counter for books
    matchings = []

    while (number > k and i < len(l)):

        if len(matchings) == 0:
            recommender = l[i]  # takes new most common user from l (sorted mostSimilarUsers for given user)
            i = i + 1  # increses the user index
            matchings = list(set(unreadBooks(user)).intersection(
                likedBooks(recommender)))  # finds the books both unread for given user and liked books for similaruser
            continue

        book = matchings.pop(random.randint(0, len(matchings) - 1))  # picks random book in matching books

        if not any(book in values for values in list(r.values())):  # checks if the choosen book is appered before
            if recommender not in r:  # if recommender not recommended before adds key to the dictionary
                r[recommender] = []

            r[recommender].append(book)  # add book to the dictinoary
            k = k + 1  # increases the book counter

    return r  # returns dictionary

if __name__ == "__main__":
    global books
    global ratings
    setup()

    re = recommendationsFor("Ben",10)
    print(re)
    printAndSave(re)
    # print(books)
    # print("demo:", demo_similartiy("civan","uche"))
