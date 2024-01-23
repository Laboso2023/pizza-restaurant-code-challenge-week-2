# seed.py
from app import app, db
from models import Restaurant, Pizza, RestaurantPizza

with app.app_context():
    # Drop all existing tables and recreate them
    db.drop_all()
    db.create_all()

    # Seed data for restaurants
    restaurant1 = Restaurant(name="Sottocasa NYC", address="298 Atlantic Ave, Brooklyn, NY 11201")
    restaurant2 = Restaurant(name="PizzArte", address="69 W 55th St, New York, NY 10019")
    restaurant3 = Restaurant(name="Slice Palace", address="123 Main St, Cityville, NY 12345")
    restaurant4 = Restaurant(name="Mama Mia", address="456 Broadway, Little Italy, NY 67890")
    restaurant5 = Restaurant(name="Pizza Haven", address="789 Elm St, Downtown, NY 45678")

    db.session.add_all([restaurant1, restaurant2, restaurant3, restaurant4, restaurant5])
    db.session.commit()

    # Seed data for pizzas
    pizza1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    pizza3 = Pizza(name="Vegetarian", ingredients="Dough, Tomato Sauce, Cheese, Vegetables")
    pizza4 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese, Basil")
    pizza5 = Pizza(name="Hawaiian", ingredients="Dough, Tomato Sauce, Cheese, Ham, Pineapple")

    db.session.add_all([pizza1, pizza2, pizza3, pizza4, pizza5])
    db.session.commit()

    # Seed data for RestaurantPizza
    restaurant_pizza1 = RestaurantPizza(price=15.99, restaurant_id=restaurant1.id, pizza_id=pizza1.id)
    restaurant_pizza2 = RestaurantPizza(price=18.99, restaurant_id=restaurant1.id, pizza_id=pizza2.id)
    restaurant_pizza3 = RestaurantPizza(price=16.99, restaurant_id=restaurant2.id, pizza_id=pizza1.id)
    restaurant_pizza4 = RestaurantPizza(price=14.99, restaurant_id=restaurant3.id, pizza_id=pizza3.id)
    restaurant_pizza5 = RestaurantPizza(price=17.99, restaurant_id=restaurant2.id, pizza_id=pizza4.id)
    restaurant_pizza6 = RestaurantPizza(price=19.99, restaurant_id=restaurant3.id, pizza_id=pizza5.id)

    db.session.add_all([restaurant_pizza1, restaurant_pizza2, restaurant_pizza3, restaurant_pizza4, restaurant_pizza5, restaurant_pizza6])
    db.session.commit()

print("Seed data added successfully!")
