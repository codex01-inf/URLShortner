from pymongo.mongo_client import MongoClient
from Utilities.globals import Constants


class DBManager:
    def __init__(self):
        self.uri = f"mongodb://{Constants.DB_USERNAME}:{Constants.DB_PASSWORD}@{Constants.DB_HOST}:{Constants.DB_PORT}"
        print(self.uri)
        self.uri = "mongodb+srv://codex01inf:VYuhtXyqvfc28EyU@cluster0.8ct2i.mongodb.net/?retryWrites=true&w=majority" \
                   "&appName=Cluster0"
        self.client = MongoClient(self.uri)
        self.db = "sample_data"
        self.collection = "urls"

    # @classmethod
    def ping_db(self):
        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def check_existence(self, val, query=None) -> bool:
        mydb = self.client[self.db]
        myurls = mydb[self.collection]
        cursor = myurls.find({"client_url": {"$exists": "true", "$in": [val]}})
        if len(cursor.to_list(1)) == 0:
            return False
        return True

    def insert(self, vals):
        mydb = self.client[self.db]
        myurls = mydb[self.collection]

        try:
            x = myurls.insert_one({'client_url': vals[0], 'redirect_url': vals[1], 'length': vals[2]})
            print(f"Inserted new row with object id = {x}")
        except Exception as e:
            print(e)
            return e

    def get_value(self, val):
        mydb = self.client[self.db]
        myurls = mydb[self.collection]
        cursor = myurls.find({"redirect_url": {"$exists": "true", "$in": [val]}}).to_list(1)

        if len(cursor) == 0:
            return {"message": "The entry dies not exists. Wrong URL or got deleted."}
        else:
            return cursor[0]['client_url']


if __name__ == "__main__":
    obj = DBManager()
    obj.ping_db()
    # obj.insert(payload={'url': "https://chatgpt.com/c/6700fbf3-e6c4-800c-a8d5-e8d4536d2729", 'custom': ''})
    # print(hash_url_encode("2&,;fgfgnSf_=d+Fgdfgd 3dgdfgd 4298342349284967867867867867865654653542342432342342"))
    # r = requests.get('https://www.instagram.com/accounts/login/')
    # print(r.status_code)
