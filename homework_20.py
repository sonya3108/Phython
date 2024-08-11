from pymongo import MongoClient


USER_NAME = 'vershynasofiya2011'
PASSWORD = 'scX12WvqbQCNx4eT'
uri = f"mongodb+srv://{USER_NAME}:{PASSWORD}@cluster130524.skzc5id.mongodb.net/?retryWrites=true&w=majority&appName=cluster130524"


client = MongoClient(uri)


db = client['book_database']


fantasy_collection = db['fantasy_books']

school_literature_collection = db['school_literature_books']


game_of_thrones = {
    "title": "Гра престолів",
    "price": 300,
    "year": 1996,
    "pages": 694
}
fantasy_collection.insert_one(game_of_thrones)


school_books = [
    {"title": "Історія України", "class": 10, "pages": 350},
    {"title": "Математика", "class": 9, "pages": 200},
    {"title": "Українська мова", "class": 8, "pages": 180},
    {"title": "Біологія", "class": 7, "pages": 220},
    {"title": "Фізика", "class": 9, "pages": 210}
]
school_literature_collection.insert_many(school_books)


history_books = school_literature_collection.find({"title": {"$regex": "Історія"}})
for book in history_books:
    print(book)

