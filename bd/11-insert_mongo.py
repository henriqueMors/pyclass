from pymongo import MongoClient

client = MongoClient()
mydb = client.dbposts
mycol = mydb.posts

post1 = {
    "title": "Pandas",
    "category": "Data Analysis",
    "level": "Intermediário",
    "author": {
        "name": "Fulano",
        "email": "fulano@email.com"
    }
}

result = mycol.insert_one(post1)
print("Documento incluído com sucesso")