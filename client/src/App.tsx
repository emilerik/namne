import { Heart, Star, X } from "lucide-react";
import { useRef, useState } from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import type { Swiper as SwiperType } from "swiper";
import { useNames, useVoteOnName } from "./hooks";
import { useAuth } from "@/feat/auth/useAuth";
import { Vote } from "@/feat/voting/types";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Match } from "@/feat/voting/Match";
import { type Match as MatchType } from "@/feat/names/types";

const App = () => {
  console.log("Hello world");
  const [activeIndex, setActiveIndex] = useState(0);
  const [match, setMatch] = useState<MatchType | null>(null);
  const authContext = useAuth();
  const isAuthenticated = authContext?.isAuthenticated;
  const swiperRef = useRef<SwiperType | null>(null);

  const { names, isPending } = useNames();

  const { voteOnName } = useVoteOnName();

  const handleLike = async () => {
    if (!names) {
      return;
    }
    try {
      const { matchedWith } = await voteOnName({
        nameId: names[activeIndex].id,
        vote: Vote.LIKE,
      });
      if (matchedWith) {
        setMatch({ name: names[activeIndex], other: matchedWith.name });
      }
    } catch {
      console.log("Already voted");
    }
    if (swiperRef.current && activeIndex < names.length - 1) {
      swiperRef.current.slideNext();
    }
  };

  const handleReject = () => {
    if (!names) {
      return;
    }
    voteOnName({ nameId: names[activeIndex].id, vote: Vote.DISLIKE });
    if (swiperRef.current && activeIndex < names.length - 1) {
      swiperRef.current.slideNext();
    }
  };

  const handleSuperLike = () => {
    if (!names) {
      return;
    }
    voteOnName({ nameId: names[activeIndex].id, vote: Vote.SUPERLIKE });
    if (swiperRef.current && activeIndex < names.length - 1) {
      swiperRef.current.slideNext();
    }
  };

  const handleSlideChange = (swiper: SwiperType) => {
    setActiveIndex(swiper.activeIndex);
  };

  if (isPending || !names || !isAuthenticated) {
    return (
      <div className="h-screen w-screen bg-gradient-to-b from-[#F27121] via-[#E94057] to-[#8A2387]" />
    );
  }

  return (
    <div className="h-screen w-screen bg-gradient-to-b from-[#F27121] via-[#E94057] to-[#8A2387]">
      <div className="grid grid-rows-3 h-screen">
        {/* Cards Container */}
        <div className="flex items-center justify-center row-span-2 px-8">
          <div className="w-80 h-96">
            <Swiper
              onSwiper={(swiper) => (swiperRef.current = swiper)}
              onSlideChange={handleSlideChange}
              effect={"slide"}
              grabCursor={true}
              // modules={[Effect]}
              className="w-full h-full"
            >
              {names.map((name, index) => (
                <SwiperSlide
                  key={index}
                  className="rounded-3xl overflow-hidden"
                >
                  <Card className="w-full h-full bg-gradient-to-br from-white/20 via-white/10 to-transparent backdrop-blur-lg border-2 border-white/30 shadow-2xl rounded-3xl">
                    <CardContent className="flex items-center justify-center h-full p-2">
                      <h1 className="text-4xl font-bold text-white text-center drop-shadow-lg break-all">
                        {name.name}
                      </h1>
                    </CardContent>
                  </Card>
                </SwiperSlide>
              ))}
            </Swiper>
          </div>
        </div>

        {/* Buttons */}
        <div className="flex flex-row items-center justify-around row-span-1 mx-4 pb-8">
          <div className="flex flex-col items-center justify-center">
            <Button
              onClick={handleReject}
              disabled={activeIndex >= names.length - 1}
              className="p-5 bg-white/90 hover:bg-white active:scale-90 active:bg-white/70 rounded-full size-18 border-2 border-red-500 shadow-lg transition-all duration-200 hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:scale-100 disabled:active:scale-100"
            >
              <X className="size-10 text-red-500" strokeWidth={3} />
            </Button>
          </div>
          <div className="flex flex-col items-center justify-center">
            <Button
              onClick={handleSuperLike}
              disabled={activeIndex >= names.length - 1}
              className="p-5 bg-white/90 hover:bg-white active:scale-90 active:bg-white/70 rounded-full size-18 border-2 border-indigo-500 shadow-lg transition-all duration-200 hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:scale-100 disabled:active:scale-100"
            >
              <Star
                className="size-10 text-indigo-500"
                fill="currentColor"
                strokeWidth={0}
              />
            </Button>
          </div>
          <div className="flex flex-col items-center justify-center">
            <Button
              onClick={handleLike}
              disabled={activeIndex >= names.length - 1}
              className="p-5 bg-white/90 hover:bg-white active:scale-90 active:bg-white/70 rounded-full size-18 border-2 border-green-600 shadow-lg transition-all duration-200 hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:scale-100 disabled:active:scale-100"
            >
              <Heart
                className="size-10 text-green-600"
                fill="currentColor"
                strokeWidth={0}
              />
            </Button>
          </div>
          <Match setMatch={setMatch} match={match} />
        </div>
      </div>
    </div>
  );
};

export default App;
