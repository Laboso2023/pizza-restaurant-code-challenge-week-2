# app.py
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request, abort
from models import db, Restaurant, Pizza, RestaurantPizza
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()

    restaurants_data = [{
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address
    } for restaurant in restaurants]

    return jsonify(restaurants_data)

@app.route('/restaurants/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)

    if not restaurant:
        abort(404, description="Restaurant not found")

    pizzas_data = [{
        'id': pizza.id,
        'name': pizza.name,
        'ingredients': pizza.ingredients
    } for pizza in restaurant.pizzas]

    restaurant_data = {
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': pizzas_data
    }

    return jsonify(restaurant_data)

@app.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
def delete_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)

    if not restaurant:
        abort(404, description="Restaurant not found")

    # Delete associated RestaurantPizza records
    RestaurantPizza.query.filter_by(restaurant_id=restaurant.id).delete()

    # Delete the Restaurant
    db.session.delete(restaurant)
    db.session.commit()

    return '', 204

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()

    pizzas_data = [{
        'id': pizza.id,
        'name': pizza.name,
        'ingredients': pizza.ingredients
    } for pizza in pizzas]

    return jsonify(pizzas_data)

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json

    required_fields = ['price', 'pizza_id', 'restaurant_id']
    if not all(field in data for field in required_fields):
        return jsonify(errors=["validation errors"]), 400

    pizza = Pizza.query.get(data['pizza_id'])
    restaurant = Restaurant.query.get(data['restaurant_id'])

    if not pizza or not restaurant:
        abort(400, description="Pizza or Restaurant not found")
    restaurant_pizza = RestaurantPizza(
        price=data['price'],
        pizza_id=pizza.id,
        restaurant_id=restaurant.id
    )

    db.session.add(restaurant_pizza)
    db.session.commit()

    pizza_data = {
        'id': pizza.id,
        'name': pizza.name,
        'ingredients': pizza.ingredients
    }

    return jsonify(pizza_data), 201


if __name__ == '__main__':
    app.run(debug=True, port=4000)
