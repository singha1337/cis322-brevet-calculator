# Laptop Service

from flask import Flask
from flask_restful import Resource, Api

# Instantiate the app
app = Flask(__name__)
api = Api(app)


class listAll(Resource):
    def get(self):
        top = int(request.args.get("top"))
        if top == 0:
            db_items = db.tododb.find().sort("Open", pymongo.ASCENDING)
        else:
            db_items = db.tododb.find().sort("Open", pymongo.ASCENDING).limit(top)
        return {
            'Open': [times['open_times'] for times in db_items],
            'Close': [item['close_times'] for times in db_items]
        }


class listOpenOnly(Resource):
    def get(self):
        top = int(request.args.get("top"))
        if top == 0:
            db_items = db.tododb.find().sort("Open", pymongo.ASCENDING)
        else:
            db_items = db.tododb.find().sort("Open", pymongo.ASCENDING).limit(top)
        return {
            'Open': [times['open_times'] for times in db_items]
        }


class listCloseOnly(Resource):
    def get(self):
        top = int(request.args.get("top"))
        if top == 0:
            db_items = db.tododb.find().sort("Open", pymongo.ASCENDING)
        else:
            db_items = db.tododb.find().sort("Open", pymongo.ASCENDING).limit(top)
        return {
            'Close': [item['close_times'] for times in db_items]
        }


class listAllCSV(Resource):
    def get(self):
        top = int(request.args.get("top"))
        if top == 0:
            db_items = db.tododb.find().sort("Open", pymongo.ASCENDING)
        else:
            db_items = db.tododb.find().sort("Open", pymongo.ASCENDING).limit(top)

        #CSV is just a string of comma separated values
        csv_string = ""
        for times in db_items:
            csv_string += times['open_times'] + ", "
            csv_string += times['close_times'] + ", "

        return csv_string


class listOpenOnlyCSV(Resource):
    def get(self):
        top = int(request.args.get("top"))
        if top == 0:
            db_items = db.tododb.find().sort("Open", pymongo.ASCENDING)
        else:
            db_items = db.tododb.find().sort("Open", pymongo.ASCENDING).limit(top)

        #CSV is just a string of comma separated values
        csv_string = ""
        for times in db_items:
            csv_string += times['open_times'] + ", "

        return csv_string


class listCloseOnlyCSV(Resource):
    def get(self):
        top = int(request.args.get("top"))
        if top == 0:
            db_items = db.tododb.find().sort("Open", pymongo.ASCENDING)
        else:
            db_items = db.tododb.find().sort("Open", pymongo.ASCENDING).limit(top)

        #CSV is just a string of comma separated values
        csv_string = ""
        for times in db_items:
            csv_string += times['close_times'] + ", "

        return csv_string


class listAllJSON(Resource):
    def get(self):
        top = int(request.args.get("top"))
        if top == 0:
            db_items = db.tododb.find().sort("Open", pymongo.ASCENDING)
        else:
            db_items = db.tododb.find().sort("Open", pymongo.ASCENDING).limit(top)
        return {
            'Open': [times['open_times'] for times in db_items],
            'Close': [item['close_times'] for times in db_items]
        }


class listOpenOnlyJSON(Resource):
    def get(self):
        top = int(request.args.get("top"))
        if top == 0:
            db_items = db.tododb.find().sort("Open", pymongo.ASCENDING)
        else:
            db_items = db.tododb.find().sort("Open", pymongo.ASCENDING).limit(top)
        return {
            'Open': [times['open_times'] for times in db_items],
        }


class listCloseOnlyJSON(Resource):
    def get(self):
        top = int(request.args.get("top"))
        if top == 0:
            db_items = db.tododb.find().sort("Open", pymongo.ASCENDING)
        else:
            db_items = db.tododb.find().sort("Open", pymongo.ASCENDING).limit(top)
        return {
            'Close': [times['close_times'] for times in db_items],
        }


# Create routes
# Another way, without decorators
api.add_resource(listAll, '/listAll')
api.add_resource(listOpenOnly, '/listOpenOnly')
api.add_resource(listCloseOnly, '/listCloseOnly')
api.add_resource(listAllCSV, '/listAll/csv')
api.add_resource(listOpenOnlyCSV, '/listOpenOnly/csv')
api.add_resource(listCloseOnlyCSV, '/listCloseOnly/csv')
api.add_resource(listAllJSON, '/listAll/json')
api.add_resource(listOpenOnlyJSON, '/listOpenOnly/json')
api.add_resource(listCloseOnlyJSON, '/listCloseOnly/json')


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
