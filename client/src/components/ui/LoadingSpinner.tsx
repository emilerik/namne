import { Loader2 } from "lucide-react";

export const LoadingSpinner = () => {
  return (
    <div className="w-full h-full flex items-center justify-center">
      <Loader2 className="animate-spin size-10" />;
    </div>
  );
};
