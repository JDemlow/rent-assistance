const FeatureCard = ({
  title,
  description,
}: {
  title: string;
  description: string;
}) => {
  return (
    <div className="bg-white p-6 rounded-lg shadow-md text-center">
      <h3 className="text-xl font-semibold text-blue-600">{title}</h3>
      <p className="mt-2 text-gray-600">{description}</p>
    </div>
  );
};

export default FeatureCard;
