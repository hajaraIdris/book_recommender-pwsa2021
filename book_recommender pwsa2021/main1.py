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


def demo_similartiy(user1, user2_name):
    # this is a demo function, does not returns real similarity.
    return sum([ord(x) for x in user2_name])


def most_similar(user):
    global users
    global ratings

    _users = users[:]
    _users.remove(user)
    score = demo_similartiy("civan", "civan")
    return


if __name__ == "__main__":
    global books
    global ratings
    setup()
    print(likedBooks("Ben"))
    print(unreadBooks("Ben"))
    # print(books)
    # print("demo:", demo_similartiy("civan","uche"))
