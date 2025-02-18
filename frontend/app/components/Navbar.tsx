"use client";

import { useState } from "react";
import Link from "next/link";

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="fixed top-0 left-0 w-full bg-white shadow-md p-2 flex justify-between items-center md:px-8 z-50">
      <h1 className="text-xl font-bold text-blue-600">Rent Insights</h1>
      <button
        className="md:hidden px-3 py-2 bg-blue-500 text-white rounded"
        onClick={() => setIsOpen(!isOpen)}
      >
        Menu
      </button>

      <ul
        className={`absolute top-14 left-0 w-full bg-white shadow-md md:static md:flex md:space-x-6 transition-all duration-300 ${
          isOpen ? "block z-50" : "hidden"
        }`}
      >
        <li className="p-3 text-gray-600 hover:text-blue-600 cursor-pointer">
          <Link href="/">Home</Link>
        </li>
        <li className="p-3 text-gray-600 hover:text-blue-600 cursor-pointer">
          <Link href="/trends">Trends</Link>
        </li>
        <li className="p-3 text-gray-600 hover:text-blue-600 cursor-pointer">
          <Link href="/assistance">Assistance</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
