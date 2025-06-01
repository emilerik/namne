export type Match = {
  name: NameEntry;
  other: string;
} | null;

export type NameEntry = {
  id: string;
  name: string;
  gender: string;
};

export type GetNamesResponse = {
  names: NameEntry[];
};
