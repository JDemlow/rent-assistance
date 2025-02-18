import "@/app/globals.css";
import Navbar from "./components/Navbar";

export const metadata = {
  title: "Denver Rent & Housing Insights",
  description: "A platform to analyze rent trends and affordability in Denver.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-white text-gray-900">
        <Navbar />
        <div className="pt-16">{children}</div>{" "}
        {/* Add padding to prevent overlap */}
      </body>
    </html>
  );
}
