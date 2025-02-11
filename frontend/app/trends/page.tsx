export default function TrendsPage() {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-6">
      <h1 className="text-4xl font-bold text-blue-600">Rent Trends</h1>
      <p className="mt-4 text-lg text-gray-700 text-center max-w-2xl">
        This page will display historical rent trends and future predictions for
        Denver neighborhoods.
      </p>

      {/* Placeholder for trend charts */}
      <div className="mt-8 w-full max-w-3xl p-6 bg-white rounded-lg shadow-md text-center">
        <p className="text-gray-500">📊 Trend charts coming soon...</p>
      </div>
    </main>
  );
}
