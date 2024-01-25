import mysql.connector
import json
with open('test1.json', 'r') as json_file:
    data = json.load(json_file)
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'MySQL@2023',
    'database': 'article',
}




connection = mysql.connector.connect(**mysql_config)
cursor = connection.cursor()




create_table_query = """
CREATE TABLE IF NOT EXISTS publications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    pub_year VARCHAR(4),
    citation VARCHAR(255),
    author VARCHAR(255),
    journal VARCHAR(255),
    volume VARCHAR(10),
    number VARCHAR(10),
    pages VARCHAR(20),
    abstract TEXT,
    num_citations INT,
    pub_url VARCHAR(255)
)
"""
cursor.execute(create_table_query)
connection.commit()



for i in list(data['Publication_1']):
    insert_query = """
    INSERT INTO publications 
    (title, pub_year, citation, author, journal, volume, number, pages, abstract, num_citations, pub_url) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
            i['title'],
            i['pub_year'],
            i['citation'],
            i['author'],
            i['journal'],
            i['volume'],
            i['number'],
            i['pages'],
            i['abstract'],
            int(i['num_citations']),
            i['pub_url']
        )
    cursor.execute(insert_query, values)
    connection.commit()
cursor.close()



connection.close()
