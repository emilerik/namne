import type { AuthContextType } from "@/feat/auth/types";
import { createContext } from "react";

const defaultContext = {
  isAuthenticated: false,
  login: () => Promise.resolve(false),
  logout: () => {},
  loading: true,
};

export const AuthContext = createContext<AuthContextType>(defaultContext);
