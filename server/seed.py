from random import choice as rc
from faker import Faker

from app import app
from models import db, College, Gallery, Memories, Dates, Crazy

with app.app_context():
    fake=Faker()
    
    College.query.delete()
    Gallery.query.delete()

    for n in range(200):
        name=fake.name()
        description=fake.text(200)
        hashtag='#' + ''.join(fake.words(3))
        college=College(name=name, description=description, hashtag=hashtag )

        db.session.add( college)
        db.session.commit()

    for n in range(100):
        image=fake.image()
        gallery=Gallery(image=image)

        db.session.add( gallery)
        db.session.commit()

        

    for n in range(50):
        name=fake.name()
        description=fake.text(200)
        joke=fake.text(100)
        memory=fake.text(50)
        hashtag='#'+''.join(fake.words(4))
        memory=Memories(name=name, description=description, joke=joke, memory=memory, hashtag=hashtag)

        db.session.add(memory)
        db.session.commit()

    for n in range (100):
        
            name=fake.name()
            description=fake.text(200)
            hashtag='#'+''.join(fake.words(4))
            joke=fake.text(30)

            dates=Dates(name=name, description=description, hashtag=hashtag, joke=joke)

            db.session.add(dates)
            db.session.commit()

    for n in range(50):
         name=fake.name()
         caption=fake.text(5)

         crazy=Crazy(name=name, caption=caption)

         db.session.add(crazy)
         db.session.commit()

        
        