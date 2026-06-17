from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


# 1. Initialize our flask application
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning

# Create SQLAlchemy instance
db = SQLAlchemy(app)

# create user model
class User(db.Model):
        __tablename__ = "users"

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(255), nullable=False)

        def __str__(self):
          return f"<User:id={self.id}, name={self.name}>"      



    
    
       

# 2. Define route to home page
@app.route("/")
def home():
    return render_template("store/home.html")

@app.route('/products')
def products():
    products = [

        {
            "id":1,
            "name":"Wireless Headphones",
            "price":99,
            "category":"Electronics",
            "image":"https://picsum.photos/400/300?1",
            "description":"Premium sound quality"
        },

        {
            "id":2,
            "name":"Smart Watch",
            "price":149,
            "category":"Electronics",
            "image":"https://picsum.photos/400/300?2",
            "description":"Track fitness and health"
        },

        {
            "id":3,
            "name":"Running Shoes",
            "price":89,
            "category":"Sports",
            "image":"https://picsum.photos/400/300?3",
            "description":"Comfortable and durable"
        }

    ]

    return render_template(
        'store/products.html',
        products=products
    )


@app.route("/product_detail")
def product_detail():
    return render_template("store/product_detail.html")
# @app.route("/dashboard")
# def dashboard():
#     if session ==  True:
#         redirect(url_for("home"))
#     else:
#         redirect(url_for("login"))

# 6. Run application
if __name__ == "__main__":
    app.run(debug=True)