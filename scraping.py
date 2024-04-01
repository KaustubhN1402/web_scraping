from scholarly import scholarly
from author import Author
from database import insert_author
import json
import os
author_name = input("enter name of the author to be searched ")
r = scholarly.search_author( author_name)
r = next( r )
author = scholarly.fill( r )

with open( "sample.json" , "w" ) as file:
    json.dump( author , file )
    
os.system( "python data_extract.py" )
   
'''
#scholarly.pprint( author )

# Print the titles of the author's publications
publication_titles = [pub['bib']['title'] for pub in author['publications']]
#print(publication_titles)

first_publication = author['publications'][0]
first_publication_filled = scholarly.fill(first_publication)
scholarly.pprint(first_publication_filled)







"""
with open("myfile.txt", "w", encoding="utf-8") as file:
    file.write(str(author))
    
    """
    
with open("extraction_of_profile.txt", "w", encoding="utf-8") as file:
    file.write(f"Author Name: {author['name']}\n")
    file.write(f"Affiliation: {author['affiliation']}\n")
    file.write(f"Email: {author['email_domain']}\n")
    file.write(f"Citations: {author['citedby']}\n")
    file.write(f"h-index: {author['hindex']}\n")
    file.write(f"i10-index: {author['i10index']}\n")
    file.write(f"Cites per year: {author['cites_per_year']}\n")
    
    author_obj = Author()
    author_obj.name = author[ "name" ]
    author_obj.hindex = author["hindex"]
    
    
    insert_author( author_obj )
    
    
with open("extraction_of_publication.txt" , "w" , encoding="utf-8") as file : 
    file.write(f"Publication_1 : {author['publications']}\n ")
    
#with open("extraction_of_publication_1.txt" , "w" , encoding="utf-8") as file : 
#  file.write(f"Publication_2.txt :{author[]}  ")
    
    
filename = 'extraction_of_publication.txt'
 
# dictionary where the lines from
# text will be stored
dict1 = {}
 
# creating dictionary
with open(filename) as fh:
 
    for line in fh:
        
        if line.strip():
            
            parts = line.strip().split(None,1)
            
            if len(parts)==2 : 
                
                command , description = parts
 
        # reads each line and trims of extra the spaces 
        # and gives only the valid words
        
 
                dict1[command] = description.strip()
            else:
                print("unable to split lines")
                
                
 
# creating json file
# the JSON file is named as test1
out_file = open("test1.json", "w")
json.dump(dict1, out_file, indent = 4, sort_keys = False)
out_file.close()
'''