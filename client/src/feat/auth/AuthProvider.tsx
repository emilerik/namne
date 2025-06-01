import {
  useCallback,
  useEffect,
  useState,
  type PropsWithChildren,
} from "react";
import { AuthContext } from "./AuthContext";
import { API_URL } from "@/config";

export const AuthProvider = ({ children }: PropsWithChildren) => {
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(true);

  const login = async ({
    username,
    password,
  }: {
    username: string;
    password: string;
  }) => {
    const token = btoa(`${username}:${password}`);
    const authHeader = `Basic ${token}`;
    return authenticate(authHeader);
  };

  const authenticate = useCallback(async (authHeader: string) => {
    const res = await fetch(`${API_URL}/authenticate`, {
      headers: { Authorization: authHeader },
    });
    if (!res.ok) {
      logout();
      return false;
    } else {
      sessionStorage.setItem("basicAuth", authHeader);
      setIsAuthenticated(true);
      return true;
    }
  }, []);

  useEffect(() => {
    if (isAuthenticated) {
      return;
    }
    const authHeader = sessionStorage.getItem("basicAuth");
    if (!authHeader) {
      setLoading(false);
    } else {
      authenticate(authHeader).finally(() => {
        setLoading(false);
      });
    }
  }, [authenticate, isAuthenticated]);

  const logout = () => {
    sessionStorage.removeItem("basicAuth");
    setIsAuthenticated(false);
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
};
