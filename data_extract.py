import mysql.connector
import json
from datetime import datetime
import pandas as pd 
import pymysql 

with open('sample.json', 'r') as json_file:
    data = json.load(json_file)
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'article',
}

connection = mysql.connector.connect(**mysql_config)
cursor = connection.cursor()

create_table_query1 = """
CREATE TABLE IF NOT EXISTS publication (
    author_id VARCHAR(255),
    title VARCHAR(255),
    pub_year INT,
    citation VARCHAR(255),
    author VARCHAR(255),
    publication_id VARCHAR(255) PRIMARY KEY,
    num_citations INT,  
    citation_url VARCHAR(255),
    FOREIGN KEY(author_id) references author(gscholar_id)
)
"""

create_table_query2 = """
CREATE TABLE IF NOT EXISTS author (
    gscholar_id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    affiliation VARCHAR(255),
    email VARCHAR(255),
    interests JSON,
    department VARCHAR(25),
    citedby INT,
    h_index INT,
    i10_index INT,
    last_searched DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)
"""
cursor.execute(create_table_query2)
connection.commit()
cursor.execute(create_table_query1)
connection.commit()

    
json_data = json.dumps(data['interests'])
insert_query2 = """
INSERT INTO author 
(gscholar_id, name, affiliation, email, interests, department, citedby,h_index,i10_index) 
VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s)
ON DUPLICATE KEY UPDATE 
name=VALUES(name), 
affiliation=VALUES(affiliation), 
email=VALUES(email), 
interests=VALUES(interests), 
department=VALUES(department), 
citedby=VALUES(citedby), 
h_index=VALUES(h_index), 
i10_index=VALUES(i10_index) , 
last_searched = NOW()

"""
values = (
        data.get('scholar_id', 'NULL'),
        data['name'],
        data['affiliation'],
        data['email_domain'],
        json_data,
        'CE',
        int(data.get('cited_by', 0)),
        int(data['hindex']),
        int(data['i10index']),
    )
cursor.execute(insert_query2, values)
connection.commit()


for i in data["publications"]:
    insert_query1 = """
    INSERT INTO publication 
    (author_id , title, pub_year, citation, author, publication_id, num_citations,citation_url) 
    VALUES (%s, %s, %s, %s, %s, %s,%s,%s)
    ON DUPLICATE KEY UPDATE
    author_id = VALUES(author_id),
    title=VALUES(title), 
    pub_year=VALUES(pub_year), 
    citation=VALUES(citation), 
    author=VALUES(author), 
    publication_id=VALUES(publication_id), 
    num_citations=VALUES(num_citations), 
    citation_url=VALUES(citation_url)
    """
    values = (
            data.get('scholar_id', 'NULL'),
            i['bib']['title'],
            int(i['bib'].get('pub_year', 0)),
            i['bib']['citation'],
            data['name'],
            i['author_pub_id'],
            int(i['num_citations']),
            i.get('citedby_url', "NULL")
        )
    cursor.execute(insert_query1, values)
    connection.commit()
    
    
sql_query = "select * from author"

df = pd.read_sql(sql_query, connection)
    




cursor.close()

connection.close()

df.to_excel('author_data.xlsx', index=False)




 
