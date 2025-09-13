#!/usr/bin/env python3
# server/seed.py

from random import choice as rc
from faker import Faker
from app import app
from models import db, Pet

with app.app_context():

    # Delete all existing rows
    Pet.query.delete()

    # Initialize Faker
    fake = Faker()

    # Species list
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    # Create 10 random pets
    pets = []
    for _ in range(10):
        pets.append(Pet(name=fake.first_name(), species=rc(species)))

    # Insert into database
    db.session.add_all(pets)
    db.session.commit()
