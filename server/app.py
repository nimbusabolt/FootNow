from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from flask_bcrypt import Bcrypt
from models import db, User, Product, CartItem, Reviews

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config["JWT_SECRET_KEY"] = "jehadruhan"

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)


with app.app_context():
    db.create_all()


@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    # Check if user already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "User already exists"}), 400

    if email and password:
        print(password)
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        print(hashed_password)
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        access_token = create_access_token(identity=email)
        print(access_token)
        return (
            jsonify(
                {
                    "message": "You are successfully signed up.",
                    "access_token": access_token,
                }
            ),
            201,
        )

    return jsonify({"message": "Failed to sign up."})


@app.route("/signin", methods=["POST"])
def signin():
    post_data = request.get_json()
    email = post_data.get("email")
    password = post_data.get("password")
    user = User.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=email)
        return jsonify(
            {"message": "You are successfully signed in.", "access_token": access_token}
        )
    return jsonify({"message": "Invalid email or password."}), 401


@app.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    products_data = [
        {
            "id": product.id,
            "name": product.name,
            "image": product.image,
            "price": product.price,
            "stock": product.stock,
            "description": product.description,
        }
        for product in products
    ]

    return jsonify(products_data)


@app.route("/additem", methods=["POST"])
@jwt_required()
def add_item():
    print(request.get_json())
    current_user = get_jwt_identity()
    data = request.get_json()
    product_id = data.get("productId")

    if not product_id:
        return jsonify({"message": "Product ID is required"}), 400

    product = db.session.get(Product, product_id)

    if not product:
        return jsonify({"message": "Product not found"}), 404

    user = User.query.filter_by(email=current_user).first()
    if not user:
        return jsonify({"message": "User not found"}), 404

    cart_item = CartItem.query.filter_by(user_id=user.id, product_id=product_id).first()
    if cart_item:
        cart_item.quantity += 1
    else:
        cart_item = CartItem(user_id=user.id, product_id=product_id, quantity=1)
        db.session.add(cart_item)

    db.session.commit()
    return jsonify({"message": "Product added to cart"}), 200


@app.route("/cartitems", methods=["GET"])
@jwt_required()
def get_cart_items():
    user_email = get_jwt_identity()
    print(user_email)
    user = User.query.filter_by(email=user_email).first()
    cart_items = CartItem.query.filter_by(user_id=user.id).all()
    result = []
    for item in cart_items:
        product = db.session.get(Product, item.product_id)

        result.append(
            {
                "name": product.name,
                "image": product.image,
                "quantity": item.quantity,
                "price": product.price,
            }
        )
    return jsonify(result)


@app.route("/deleteitem", methods=["DELETE"])
def delete_item():
    try:
        item_name = request.json.get("item_name")
        product = Product.query.filter_by(name=item_name).first()
        if product:
            delete_item = CartItem.query.filter_by(product_id=product.id).first()
            if delete_item:
                db.session.delete(delete_item)
                db.session.commit()
                return jsonify({"message": "Item deleted successfully"}), 200
            else:
                return jsonify({"error": "Item not found in cart"}), 404
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        # Handle exceptions
        return jsonify({"error": str(e)}), 500


@app.route("/submit_review", methods=["POST"])
@jwt_required()
def submit_review():
    try:
        user_email = get_jwt_identity()
        data = request.get_json()
        writer = User.query.filter_by(email=user_email).first().id
        title = data.get("title")
        content = data.get("content")
        rating = data.get("rating")

        if not writer or not title or not content or rating is None:
            return jsonify({"error": "Missing data"}), 400

        review = Reviews(writer=writer, title=title, content=content, rating=rating)
        db.session.add(review)
        db.session.commit()

        return jsonify({"message": "Review submitted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/get_reviews", methods=["GET"])
def get_reviews():
    try:
        reviews = Reviews.query.all()
        for review in reviews:
            user = User.query.filter_by(id=review.writer).first()
            review.writer = user.email
        review_data = [
            {
                "id": review.id,
                "writer": review.writer,
                "title": review.title,
                "content": review.content,
                "rating": review.rating,
            }
            for review in reviews
        ]  # Assuming this function returns a list of reviews

        return jsonify(review_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run()
