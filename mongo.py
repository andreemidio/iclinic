from pymongo import MongoClient

class MongoConnect:
    def __init__(self):
        self.db_name = "exchange",
        self.host = "localhost",
        self.port = 27017,
        self.username = None,
        self.password = None

    def get_db_handle(self):
        print(self.port)

        client = MongoClient(host=self.host,
                             port=int(27017),
                             # username=self.username,
                             # password=self.password
                             )
        db_handle = client['exchange']

        return db_handle, client


if __name__ == "__main__":
    mongo = MongoConnect()

    db_handle, client = mongo.get_db_handle()

    import datetime

    print(db_handle)
    print(client)
    post = {"author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}

    posts = db_handle.exchange
    post_id = posts.insert_one(post).inserted_id
    print(post_id)
