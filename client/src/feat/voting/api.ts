import { API_URL } from "@/config";
import type {
  VoteOnNameRequest,
  VoteOnNameResponse,
} from "@/feat/voting/types";
import { toast } from "react-toastify";

export const voteOnName = async ({
  nameId,
  vote,
}: VoteOnNameRequest): Promise<VoteOnNameResponse> => {
  const authHeader = sessionStorage.getItem("basicAuth");
  const response = await fetch(`${API_URL}/name/${nameId}`, {
    method: "POST",
    body: JSON.stringify({ vote }),
    headers: {
      "Content-Type": "application/json",
      Authorization: authHeader ?? "",
    },
  });
  if (!response.ok) {
    toast.error("Failed to post name");
    throw new Error("Failed to post name");
  }
  return response.json();
};
