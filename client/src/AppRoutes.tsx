import App from "@/App";
import { LoadingSpinner } from "@/components/ui/LoadingSpinner";
import { LoginPage } from "@/feat/auth/LoginPage";
import { useAuth } from "@/feat/auth/useAuth";
import type { PropsWithChildren } from "react";
import { BrowserRouter, Navigate, Route, Routes } from "react-router";

const ProtectedRoutes = ({ children }: PropsWithChildren) => {
  const { isAuthenticated, loading } = useAuth();
  if (loading) {
    return <LoadingSpinner />;
  }
  if (!isAuthenticated) {
    return <Navigate to={"/login"} />;
  }
  return children;
};

export const AppRoutes = () => {
  return (
    <div className="h-screen w-screen bg-gradient-to-b from-[#F27121] via-[#E94057] to-[#8A2387]">
      <BrowserRouter>
        <Routes>
          <Route
            index
            element={
              <ProtectedRoutes>
                <App />
              </ProtectedRoutes>
            }
          />
          <Route path="/login" element={<LoginPage />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
};
