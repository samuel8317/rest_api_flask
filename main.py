from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)
    
# TODO: PEP-484 - Appropriate type-hinting

# Users Endpoint

class Users(Resource):

#    def __init(self, *args, **kwargs):
        
#        self.var = self.kwargs.get('var')

    def get(self):
        
        data = pd.read_csv('users.csv')
        data = data.to_dict()
        
        return {'data': data}, 200

    def post(self):

        parser = reqparse.RequestParser()
        
        parser.add_argument('userId', required=True, type=str)
        parser.add_argument('name', required=True, type=str)
        parser.add_argument('city', required=True, type=str)

        args = parser.parse_args()

        data = pd.read_csv('users.csv')

        if args['userId'] in data['userId']:
            
            return {
                    'message': f"'{args['userId']}' already exists"
                    }, 409
            
        else:
            
            data = data.append({
                'userId':   args['userId'],
                'name':     args['name'],
                'city':     args['city'],
                'locations': []
                }, ignore_index=True)

            data.to_csv('users.csv', index=False)
                
            return {'data': data.to_dict()}, 200

# Locations Endpoint

class Locations(Resource):
    pass

api.add_resource(Users,'/users')
api.add_resource(Locations, '/locations')

if __name__ == '__main__':
    app.run(debug=True)
