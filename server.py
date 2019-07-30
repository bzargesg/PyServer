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
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

data = {'1': ['init']}


class My_api(Resource):

    @app.route('/dostuff', methods=['GET'])
    def do_stuff_get():
        print('get route dostuff')
        return data, 200

    @app.route('/dostuff', methods=['POST'])
    def do_stuff_post():
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        args = parser.parse_args()
        data["1"].append(args["id"])
        print('args: ', args)
        print('post route dostuff')
        return data, 201

    @app.route('/dostuff/<index>', methods=['DELETE'])
    def do_stuff_delete(index):
        print(f"delete index: {index}")
        removedValue = data["1"].pop(int(index))
        return f"{removedValue} is deleted.", 200


api.add_resource(My_api, '/')
app.run(debug=True)
