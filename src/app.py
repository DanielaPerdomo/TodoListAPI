from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
   {"label": "My first task", "done": False}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods = ['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    json_body = jsonify(todos)
    return json_body

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
   todos.pop( position - 1 )
   json_todos = jsonify(todos)
   return  json_todos



# Estas dos líneas siempre seben estar al final de tu archivo app.py.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)