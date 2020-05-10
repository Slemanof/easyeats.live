import mysql.connector
import Reccomender

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="restaurants"
)

mycursor = mydb.cursor()
print(Reccomender.get_recommendations(1, mycursor, 4))

print(Reccomender.get_recommendations(1, mycursor))