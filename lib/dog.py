# lib/dog.py
from models import Dog

def create_table(engine):
    # Create the table in the database
    Dog.metadata.create_all(bind=engine)
from models import Dog

def create_table(base):
    # Create the table in the database
    base.metadata.create_all()

def save(session, dog):
    # Save the dog object to the database
    session.add(dog)
    session.commit()

def get_all(session):
    # Retrieve all dogs from the database
    return session.query(Dog).all()

def find_by_name(session, name):
    # Find a dog by name in the database
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    # Find a dog by id in the database
    return session.query(Dog).get(id)

def find_by_name_and_breed(session, name, breed):
    # Find a dog by name and breed in the database
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    # Update the breed of a specific dog in the database
    dog.breed = breed
    session.commit()
