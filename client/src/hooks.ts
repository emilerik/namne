import type { NameEntry } from "@/feat/names/types";
import { voteOnName } from "./feat/voting/api";
import { getNames } from "./feat/names/api";
import { useMutation, useQuery } from "@tanstack/react-query";
import { useAuth } from "@/feat/auth/useAuth";
import type { Vote } from "@/feat/voting/types";

export const useNames = () => {
  const { isAuthenticated } = useAuth();
  const { data: names, isPending } = useQuery<NameEntry[]>({
    queryKey: ["names"],
    queryFn: async () => {
      const { names } = await getNames();
      return names;
    },
    staleTime: 1000 * 60 * 5, // 5 minutes
    enabled: isAuthenticated,
  });

  return { names, isPending };
};

export const useVoteOnName = () => {
  const { mutateAsync } = useMutation({
    mutationFn: ({ nameId, vote }: { nameId: string; vote: Vote }) =>
      voteOnName({ nameId, vote }),
  });

  return { voteOnName: mutateAsync };
};
