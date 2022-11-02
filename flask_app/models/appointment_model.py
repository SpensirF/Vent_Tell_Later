from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 
from flask_app import DATABASE 
from flask_app.models.user_model import User 
import re 

class Appointment: 
    def __init__(self, data): 
        self.id = data['id']
        self.topic = data['topic']
        self.context = data['context']
        self.event = data['event']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create(cls, data):
        query = "INSERT INTO appointments(topic, context, event, user_id) VALUE( %(topic)s, %(context)s, %(event)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)