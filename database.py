import mysql.connector 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="scraping"
)

mycursor = mydb.cursor()


def insert_author(author):
    mycursor.execute( "insert into author_info( name , hindex ) values( '{}','{}' )".format( author.name , author.hindex))
    mydb.commit()
    