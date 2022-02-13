from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def index():
    first_name = "Ridvan"
    stuff = "this is <strong>bold</strong> text"
    stuff1 = "first word capitaliz"
    mytrim = "remove the last space from this         hello"
    favorit_pizza =['pepperoni','cheese','mushrooms',41]
    return render_template("index.html",first_name=first_name,stuff=stuff,stuff1=stuff1,mytrim=mytrim,favorit_pizza=favorit_pizza)


@app.route("/user/<name>")
def user(name):
    #return "hello user{}".format(name)
    return render_template("user.html",username=name)

#create custom error page
#invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404
#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500  

if __name__ == '__main__':
    app.run(debug=True)