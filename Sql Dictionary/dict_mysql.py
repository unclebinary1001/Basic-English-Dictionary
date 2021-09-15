#Import mysql connector library
import mysql.connector
#from mysql.connector import errorcode

con = mysql.connector.connect(
  user= "ardit700_student", 
  password = "ardit700_student",
  host = "108.167.140.122",
  database = "ardit700_pm1database"
)
word = input("Enter a word you want to search: ")
cursor = con.cursor()
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}'".format(word))

results = cursor.fetchall()

if results:
  for result in results:
    print(result[1])
else:
  print("No word found")


#try:
#  cnx = mysql.connector.connect(user='scott',
#                                database='employ')
#except mysql.connector.Error as err:
#  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#    print("Something is wrong with your user name or password")
#  elif err.errno == errorcode.ER_BAD_DB_ERROR:
#    print("Database does not exist")
#  else:
#    print(err)
#else:
#  cnx.close()
