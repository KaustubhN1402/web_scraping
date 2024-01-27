
class Publication:
    id: int
    title : str
    year: int
    citation:str
    author:str
    publication_id:str
    num_citations:int
    citation_url:str


class Author :
    id : int 
    name : str
    affliation : str
    email : str
    citations : str
    hindex : int
    iindex : str
    publications: list[Publication]
    
    