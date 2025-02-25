"use client"; // ✅ Add this at the top

import { useEffect, useState } from "react";

// Define the TypeScript type for rent data
type RentData = {
  id: number;
  neighborhood: string;
  rent_price: number;
};

const Page = () => {
  const [rentData, setRentData] = useState<RentData[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/rent_data/")
      .then((res) => res.json())
      .then((data) => setRentData(data))
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  return (
    <div>
      <h1>Denver Rent Data</h1>
      <ul>
        {rentData.map((item) => (
          <li key={item.id}>
            {item.neighborhood}: ${item.rent_price}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Page;
