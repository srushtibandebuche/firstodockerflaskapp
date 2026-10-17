from flask import Flask ,render_template,redirect
#Need to create a instance a for Flask
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


print("========>",__name__)#__main__ current module execution


if __name__ == '__main__':
    app.run(debug=True,port=8000)
