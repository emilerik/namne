export enum Vote {
  "DISLIKE" = 0,
  "LIKE" = 1,
  "SUPERLIKE" = 2,
}

export type VoteOnNameRequest = {
  nameId: string;
  vote: Vote;
};

export type VoteOnNameResponse = {
  matchedWith: { username: string; name: string } | null;
};
