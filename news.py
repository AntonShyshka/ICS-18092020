from sqlalchemy.ext.declarative import declarative_base 
Base = declarative_base() 
from sqlalchemy import Column, String, Integer 
class News(Base):     
    __tablename__ = "news"     
    id = Column(Integer, primary_key = True)     
    title = Column(String)     
    author = Column(String)     
    url = Column(String)     
    comments = Column(Integer) 
    points = Column(Integer)     
    label = Column(String) 
    from sqlalchemy import create_engine 
    engine = create_engine("https://news.rbc.ua/rus/politics/konstitutsionnyy-krizis-reshitsya-techenie-1605186400.html") 
    Base.metadata.create_all(bind=engine) 
    from sqlalchemy.orm import sessionmaker 
    session = sessionmaker(bind=engine) 
    s = session() 