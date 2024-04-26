from flask import Flask,request, make_response
from flask_restful import Api, Resource
from models import db, College, Gallery, Memories, Dates, Crazy
from flask_migrate import Migrate


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.json.compact=False

migrate=Migrate(app, db)

db.init_app(app)
api=Api(app)

class Index(Resource):
    def get(self):

        welcome_message={"message":"welcome to smart gallery"}
        response=make_response(welcome_message, 200)
        return response
    
api.add_resource(Index, '/')
#getting a college

class CollegeResource(Resource):
    def get(self):
        college_dict=[college.to_dict() for college in College.query.all()]
        response=make_response(college_dict, 200)
        return response
    #creating a new college
    
    def post(self):
        newCollege=College(
            name=request.form['name'],
            description=request.form['description'],
            hashtag=request.form['hashtag']
        )
        db.session.add(newCollege)
        db.session.commit()

        response_dict=newCollege.to_dict()

        response=make_response(response_dict, 201)
        return response

api.add_resource(CollegeResource, '/college')

    
    #Getting a college resource by id
class CollegeDyId(Resource):
    def get(self, id):
        college_by_id=College.query.filter_by(id=id).first()
        if college_by_id:
            college_dict=college_by_id.to_dict()
            response=make_response(college_dict, 200)
            return response

        else:
            response_dict={"message":"failed to fetch college"}
            response=make_response(response_dict, 404)
            return response
        
    
    #updating a resource by id
    def patch(self, id):
        college=College.query.filter_by(id=id).first()
        if college:
            for attr in request.form:
                setattr(college, attr, request.form[attr])

                db.session.add(college)
                db.session.commit()

                response_dict=college.to_dict()
                response_message={"message":"successfully updated!"}
                response=make_response(response_message,response_dict, 203)
                return response
        else:
            return {"message" : "failed to update!"}
        
    def delete(self, id):
        college=College.query.filter_by(id=id).first()
        if college:
            db.session.delete(college)
            db.session.commit()

            response_dict={"message":"College successfully deleted!"}
            response=make_response(response_dict, 204)
            return response
        else:
            response_dict= {"message":"failed to delete"}
            response=make_response(response_dict, 400)
            return response
api.add_resource(CollegeDyId, '/college/<int:id>')
    

  #getting all images in a gallery  

class GalleryResource(Resource):
    def get(self):
        gallery_dict=[gallery.to_dict() for gallery in Gallery.query.all()]
        response=make_response(gallery_dict, 200)
        return response
    
    #adding an image to the gallery
    
    def post(self):

        new_gallery=Gallery(
            image=request.form['image']
        )
        db.session.add(new_gallery)
        db.session.commit()
        response_dict=new_gallery.to_dict()
        response=make_response(response_dict, 201)
        return response
    
api.add_resource(GalleryResource, '/gallery')

#getting a gallery resource by id

class GalleryDyId(Resource):
    def get(self, id):
        gallery_dict=Gallery.query.filter_by(id=id).first().to_dict()
        response=make_response(gallery_dict, 200)
        return response
    #updating a gallery item by id

    def patch(self, id):
        update_gallery=Gallery.query.filter_by(id=id).first()
        for attr in request.form:
            setattr(update_gallery, attr, request.form[attr])
            db.session.add(update_gallery)
            db.session.commit()

            response_dict=update_gallery.to_dict()
            response=make_response(response_dict)
            return response
        
    def delete(self, id):
        delete_gallery=Gallery.query.filter_by(id=id).first()

        db.session.delete(delete_gallery)
        db.session.commit()

        response_dict={"message":"Gallery successfully deleted!"}
        response=make_response(response_dict, 203)
        return response
api.add_resource(GalleryDyId, '/gallery/<int:id>')


    # getting Memories
class MemoriesResource(Resource):
    def get(self):
        memories_dict=[memory.to_dict() for memory in Memories.query.all()]
        response=make_response(memories_dict, 200)
        return response
    
    def post(self):
        new_memory=Memories(
           name=request.form['name'],
           description=request.form['description'],
           joke=request.form['joke'],
           memory=request.form['memory'],
           hashtag=request.form['hashtag'] 
        )
        db.session.add(new_memory)
        db.session.commit()

        response_dict=new_memory.to_dict()
        response=make_response(response_dict, 201)
        return response
    
api.add_resource(MemoriesResource, '/memories')
#get memories by id

class MemoryById(Resource):
    def get(self, id):
        memory_by_id=Memories.query.filter_by(id=id).first().to_dict()
        if memory_by_id:
            response=make_response(memory_by_id, 200)
            return response
        else:
            return {"message":"failed to locate memory!"}
        #update memory by id
    
    def patch(self, id):
        update_memory=Memories.query.filter_by(id=id).first()
        if update_memory:
            for attr in request.form:
                setattr(update_memory, attr, request.form[attr])
                db.session.add(update_memory)
                db.session.commit()

                response_dict=update_memory.to_dict()
                response=make_response(response_dict, 201)
                return response
        else:
            return {"message": "failed to update resource!"}, 400
        #delete a memory
        
    def delete(delf, id):
        delete_memory=Memories.query.filter_by(id=id).first()
        if delete_memory:
            db.session.delete(delete_memory)
            db.session.commit()
        else:
            return {"message":"failed to delete resource"}, 401
        
api.add_resource(MemoryById, '/memories/<int:id>')



class DatesResource(Resource):
    def get(self):
        dates=[date.to_dict() for date in Dates.query.all()]
        response=make_response(dates, 200)
        return response
    
    def post(self):
        new_date=Dates(
            name=request.form['name'],
            description=request.form['description'],
            hashtag=request.form['hashtag'],
            joke=request.form['joke']
        )

        db.session.add(new_date)
        db.session.commit()

        date_dict=new_date.to_dict()
        response=make_response(date_dict)
        return response
    
api.add_resource(DatesResource, '/dates')


class CrazyResource(Resource):
    def get(self):
        crazy_dict=[crazy.to_dict() for crazy in Crazy.query.all()]
        response=make_response(crazy_dict, 200)
        return response
    
    def post(self):
        new_crazy_dict=Crazy(
            name=request.form['name'],
            caption=request.form['caption']
        )

        db.session.add(new_crazy_dict)
        db.session.commit()

        response_dict=new_crazy_dict.to_dict()
        response=make_response(response_dict)
        return response

api.add_resource(CrazyResource, '/crazy')

class CrazyResourceById(Resource):
    def get(self, id):
        crazy_items=Crazy.query.filter_by(id=id).first().to_dict()
        if crazy_items:
            response=make_response(crazy_items, 200)
            return response
        else:
            return{"message":"failed to fetch items"}, 402
        
    def patch(self, id):
        updated_crazy=Crazy.query.filter_by(id=id).first()
        if updated_crazy:
            for attr in request.form:
                setattr(updated_crazy, attr, request.form[attr])
                db.session.add(updated_crazy)
                db.session.commit()

                response_dict=updated_crazy.to_dict()
                response=make_response(response_dict, 201)
                return response
        else:
            return {"message" : "failed to update resource"}
        
    def delete(self, id):
        delete_response=Crazy.query.filter_by(id=id).first()
        if delete_response:
            db.session.delete(delete_response)
            db.session.commit()

            response_dict={"message":"successfully deleted!"}
            response=make_response(response_dict, 204)
            return response
        else:
            return {"message":"failed to delete resource!"}
        
api.add_resource(CrazyResourceById, '/crazy/<int:id>')
            





if __name__=='__main__':
    app.run(port=5555, debug=True)
