import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import HeroSection from "./components/Hero";
import Restaurants from "./pages/Restaurants";
import RestaurantDetails from "./pages/RestaurantDetails";
import PizzaList from "./pages/PizzaList";
import MenuManagement from "./pages/Management";
import Footer from "./components/Footer";


const App = () => {
  return (
    <Router>
      <div className="mx-auto max-w-screen-lg p-4">
        <Navbar />
        <Routes>
          <Route
            path="/restaurants/*"
            element={
              <div>
                <HeroSection />
                <Restaurants />
              </div>
            }
          />
          <Route
            path="/restaurants/:id/*"
            element={
              <div>
                <RestaurantDetails />
                <PizzaList />
              </div>
            }
          />
          <Route
            path="/pizzaList"
            element={<PizzaList />}
          />
          <Route
            path="/pizzas"
            element={<PizzaList />}
          />
                  <Route path="/menuManagement" element={<MenuManagement />} />

        </Routes>
        {/* <PizzaList /> */}
      <Footer />
      </div>
    </Router>
  );
};

export default App;
