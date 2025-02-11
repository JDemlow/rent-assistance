export default function AssistancePage() {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-6">
      <h1 className="text-4xl font-bold text-blue-600">
        Rental Assistance Programs
      </h1>
      <p className="mt-4 text-lg text-gray-700 text-center max-w-2xl">
        This page will provide information on rental assistance programs
        available in Denver.
      </p>

      {/* Placeholder for assistance resources */}
      <div className="mt-8 w-full max-w-3xl p-6 bg-white rounded-lg shadow-md text-center">
        <p className="text-gray-500">
          🏡 Assistance program details coming soon...
        </p>
      </div>
    </main>
  );
}
