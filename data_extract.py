import mysql.connector
import json
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
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    pub_year INT,
    citation VARCHAR(255),
    author VARCHAR(255),
    publication_id VARCHAR(255),
    num_citations INT,
    citation_url VARCHAR(255)
)
"""

create_table_query2 = """
CREATE TABLE IF NOT EXISTS author (
    id INT AUTO_INCREMENT PRIMARY KEY,
    gscholar_id VARCHAR(255),
    name VARCHAR(255),
    affiliation VARCHAR(255),
    email VARCHAR(255),
    interests JSON,
    department VARCHAR(25),
    citedby INT,
    h_index INT,
    i10_index INT
)
"""
cursor.execute(create_table_query1)
connection.commit()
cursor.execute(create_table_query2)
connection.commit()

for i in data["publications"]:
    insert_query1 = """
    INSERT INTO publication 
    (title, pub_year, citation, author, publication_id, num_citations,citation_url) 
    VALUES (%s, %s, %s, %s, %s, %s,%s)
    """
    values = (
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

json_data = json.dumps(data['interests'])
insert_query2 = """
INSERT INTO author 
(gscholar_id, name, affiliation, email, interests, department, citedby,h_index,i10_index) 
VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s)
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


cursor.close()



connection.close()




 
