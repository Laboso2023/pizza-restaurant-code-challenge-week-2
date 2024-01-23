import React from "react";
import { FaChevronUp } from "react-icons/fa";

const Footer = () => {
  // Function to scroll to the top of the page
  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  return (
    <footer className=" text-black py-6 px-3">
        <hr />
      <div className="container mx-auto text-center mt-2">
        <div className="flex justify-center mb-4">
          <button
            onClick={scrollToTop}
            className="text-red-600 focus:outline-none hover:text-gray-300 transition duration-300"
          >
            <FaChevronUp size={24} />
          </button>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="mb-4 md:mb-0">
            <h3 className="text-lg font-bold mb-2">About Us</h3>
            <p className="text-black">
          Deluxe  is where passion meets flavor. We're dedicated to creating delicious, high-quality meals that bring people together. Sustainability and community are at our core.            </p>
          </div>
          <div className="mb-4 md:mb-0">
            <h3 className="text-lg font-bold mb-2">Contact</h3>
            <p className="text-green-600">
              Email: contact@example.com
              <br />
              Phone: +1 (123) 456-7890
            </p>
          </div>
          <div className="mb-4 md:mb-0">
            <h3 className="text-lg font-bold mb-2">Social Media</h3>
            <p className="text-white">Follow us on:</p>
            {/* Add your social media icons/links here */}
          </div>
          <div className="mb-4 md:mb-0">
            <h3 className="text-lg font-bold mb-2">Privacy Policy</h3>
            <a href="http://" target="blank">
              {" "}
              <p className="text-slate-600">Read our privacy policy here.</p>
            </a>
          </div>
        </div>
      </div>
      <div className="text-center mt-4 bg-black w-full">
        <p className="text-gray-500">
          © 2024 Your Company Name. All rights reserved.
        </p>
      </div>
    </footer>
  );
};

export default Footer;
