import Image from "next/image";

export default function Home() {
  return (
    <main className="relative flex flex-col items-center justify-center min-h-screen bg-gray-100">
      {/* Background Image */}
      <div className="absolute inset-0 w-full h-full z-0">
        <Image
          src="/images/hero-bg.jpg"
          alt="Denver city skyline"
          layout="fill"
          objectFit="cover"
          priority // Improves image loading for performance
          quality={85} // Slightly reduces quality to optimize load time
          className="opacity-60"
        />
      </div>

      {/* Hero Content */}
      <section className="relative z-10 max-w-3xl p-8 bg-white bg-opacity-85 rounded-xl shadow-xl text-center mt-28">
        <h1 className="text-4xl font-extrabold text-blue-700 sm:text-5xl">
          Denver Rent & Housing Insights
        </h1>
        <p className="mt-4 text-lg text-gray-800">
          Explore rent affordability, housing trends, and rental assistance in
          Denver.
        </p>
        <button className="mt-6 px-8 py-3 bg-blue-600 text-white text-lg font-semibold rounded-lg shadow-lg hover:bg-blue-700 transition">
          Get Started
        </button>
      </section>
    </main>
  );
}
