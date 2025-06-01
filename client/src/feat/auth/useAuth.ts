import { AuthContext } from "@/feat/auth/AuthContext";
import type { AuthContextType } from "@/feat/auth/types";
import { useContext } from "react";

export const useAuth = (): AuthContextType => {
  const context = useContext(AuthContext);

  return context;
};
