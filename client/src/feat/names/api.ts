import { BASE_URL } from "@/api";
import type { GetNamesResponse } from "@/feat/names/types";
import { toast } from "react-toastify";

export const getNames = async (): Promise<GetNamesResponse> => {
  const authHeader = sessionStorage.getItem("basicAuth");
  const response = await fetch(`${BASE_URL}/names`, {
    headers: { Authorization: authHeader ?? "" },
  });
  if (!response.ok) {
    toast.error("Failed to get names");
    throw new Error("Failed to get names");
  }
  return response.json();
};
