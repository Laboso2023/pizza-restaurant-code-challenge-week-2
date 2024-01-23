import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import AddRestaurantPizza from "../components/Add";

const PizzaList = () => {
  const [pizzas, setPizzas] = useState([]);

  useEffect(() => {
    // Fetch all pizzas from your API endpoint
    fetch("/pizzas")
      .then((response) => response.json())
      .then((data) => setPizzas(data))
      .catch((error) => console.error("Error fetching pizzas:", error));
  }, []);

  return (
    <div>
      <h2 className="text-4xl text-red-500 font-extralight pb-2">All Pizzas</h2>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 p-4">
        {pizzas.map((pizza) => (
          <div
            key={pizza.id}
            className="bg-white rounded-lg overflow-hidden shadow-lg transition-transform transform hover:scale-105"
          >
            {/* You can replace the pizza image URL with your actual image URLs */}
            <img
              className="w-full h-32 object-cover object-center"
              src={`https://source.unsplash.com/800x600/?pizza,${pizza.name}`}
              alt={`Pizza ${pizza.name}`}
            />

            <div className="p-4 flex flex-col ">
              <h2 className="text-xl font-semibold mb-2">{pizza.name}</h2>
              <p className="text-gray-600 font-thin mb-2">{pizza.ingredients}</p>

              {/* Use Link to navigate to the pizza details page */}
              <Link to={`/pizzas/${pizza.id}`} className="show-btn cursor-pointer flex ">
                <h3 className='text-blue-500 cursor-not-allowed'>Place an order</h3>
              </Link>
            </div>
          </div>
        ))}
      </div>
      <AddRestaurantPizza />
    </div>
  );
};

export default PizzaList;
