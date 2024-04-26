from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

convention={
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata=MetaData(naming_convention=convention)

db=SQLAlchemy(metadata=metadata)

#College model

class College(db.Model, SerializerMixin):
    __tablename__='college'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    description=db.Column(db.String)
    date=db.Column(db.DateTime, default=datetime.now)
    hashtag=db.Column(db.String)
    
    def __repr__(self):
        return f'<College {self.id}, {self.name}, {self.description}, {self.date}, {self.hashtag}>'
    
    #Gallery model
    
class Gallery(db.Model, SerializerMixin):
    __tablename__='gallery'

    id=db.Column(db.Integer, primary_key=True)
    image=db.Column(db.String(200))
    created_at=db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f'<Gallery {self.id}, {self.image}, {self.created_at}>'
    
    #memories model
class Memories(db.Model, SerializerMixin):
    __tablename__='memories'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    description=db.Column(db.String(200))
    joke=db.Column(db.String(100))
    memory=db.Column(db.String(50))
    hashtag=db.Column(db.String)

    def __repr__(self):
        return f'<Memories {self.id},{self.name},{self.description},{self.joke},{self.memory},{self.hashtag}>'
    
#Dates model
class Dates(db.Model, SerializerMixin):
    __tablename__='dates'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    description=db.Column(db.String)
    hashtag=db.Column(db.String)
    joke=db.Column(db.String)

    def __repr__(self):
        return f'<Dates {self.id}, {self.name}, {self.description}, {self.hashtag}, {self.joke}>'
    
#crazy model

class Crazy(db.Model, SerializerMixin):
    __tablename__='crazy'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    caption=db.Column(db.String (5))

    def __repr__(self):
        return f'<Crazy {self.id}, {self.name}, {self.caption}>'

    

