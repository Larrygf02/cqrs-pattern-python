from pymongo import MongoClient

def upsert_data(payload):
    products = get_collection('products')
    products.replace_one({'id_sync': payload.get('id_sync')}, payload, upsert=True)

def get_collection(collection):
    client = MongoClient('localhost', 27017)
    db = client['sync-demo']
    return db[collection]