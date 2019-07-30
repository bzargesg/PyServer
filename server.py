############################################
#           Simple Http server             #
# ##########################################
# import http.server
# import socketserver

# PORT = 8080
# Handler = http.server.SimpleHTTPRequestHandler

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print(f"serving at port", PORT)
#     httpd.serve_forever()
############################################
#     Flask Restful Server w/ Decorators   #
# ##########################################
# from flask import Flask
# from flask_restful import Api, Resource, reqparse

# app = Flask(__name__)
# api = Api(app)

# data = {'1': ['init']}


# class My_api(Resource):

#     @app.route('/dostuff', methods=['GET'])
#     def do_stuff_get():
#         print('get route dostuff')
#         return data, 200

#     @app.route('/dostuff', methods=['POST'])
#     def do_stuff_post():
#         parser = reqparse.RequestParser()
#         parser.add_argument("id")
#         args = parser.parse_args()
#         data["1"].append(args["id"])
#         print('args: ', args)
#         print('post route dostuff')
#         return data, 201

#     @app.route('/dostuff/<index>', methods=['DELETE'])
#     def do_stuff_delete(index):
#         print(f"delete index: {index}")
#         removedValue = data["1"].pop(int(index))
#         return f"{removedValue} is deleted.", 200


# api.add_resource(My_api, '/')
# app.run(debug=True)
############################################
#                Flask Restful             #
# ##########################################
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

beer_names = [{"name": 'init'}]


class Some_server(Resource):
    def get(self, name):
        if(name == "all"):
            return beer_names, 200
        for beer in beer_names:
            if(name == beer["name"]):
                return beer, 200
            return "beer not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        args = parser.parse_args()
        for beer in beer_names:
            if(name == beer["name"]):
                return f"Beer with name: {name} already exists", 400

        newbeer = {
            "name": args["name"],
        }
        beer_names.append(newbeer)
        return newbeer, 201

    def put(self, name):
        return "put doesnt really make sense here", 400

    def delete(self, name):
        beer_names_new = [beer for beer in beer_names if beer["name"] != name]
        return f"{name} is deleted.", 200


api.add_resource(Some_server, "/beer/<string:name>")
app.run(debug=True)
