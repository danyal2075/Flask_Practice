from flask import Flask, jsonify
# Creating object 
app = Flask(__name__)

#This is the calling of method. this defines the route after slash
@app.route("/")
def helloworld():
    return "HelloWorld from pakistan morning"

# if i write get after the slash it will direct me to the down function  
@app.route("/get")
def get():
    data = {
        "name" : "Sohail Danyal",
        "father name" : "Qamar zaman",
        'course' : 'MT'
    }
    return jsonify(data)
app.run(debug=True , port=80)
