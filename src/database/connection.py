import pymongo
from pymongo.server_api import ServerApi

client = pymongo.MongoClient("mongodb+srv://sys:teste123@cluster1.4zkfjz8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1", server_api=ServerApi('1'))
database = client.MercadoLivre
