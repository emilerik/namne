import { Button } from "@/components/ui/button";
import type { Match as MatchType } from "@/feat/names/types";

export const Match = ({
  match,
  setMatch,
}: {
  match: MatchType;
  setMatch: (match: MatchType) => void;
}) => {
  if (!match) {
    return null;
  }
  return (
    <div className="grid grid-rows-3 max-w-screen max-h-screen overflow-hidden fixed z-2 inset-0 bg-black/85 items-center">
      <div className="row-2 flex flex-col items-center gap-3 w-full">
        <h1 className="font-kristi text-7xl text-white">It's a match!</h1>
        <h3 className="text-2xl text-white mt-2">
          You and {match.other} both like
        </h3>
        <h2 className="text-5xl text-white">{match.name.name}</h2>
      </div>
      <div className="row-3 w-full px-4">
        <Button
          variant="outline"
          className="mt-10 px-8 py-7 text-black text-2xl w-full"
          onClick={() => {
            setMatch(null);
          }}
        >
          Hihi okay!
        </Button>
      </div>
    </div>
  );
};
