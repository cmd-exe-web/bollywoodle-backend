from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HomeResource(Resource):
    def get(self):
        return "home resource"


api.add_resource(HomeResource, '/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
