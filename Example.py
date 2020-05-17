import mysql.connector
import Recommender

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="restaurants"
)

mycursor = mydb.cursor()
print(Recommender.get_recommendations(1, mycursor, 4))

print(Recommender.get_recommendations(1, mycursor))