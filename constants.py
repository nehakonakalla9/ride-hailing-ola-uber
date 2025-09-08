from enum import Enum

class RATING(Enum):
    UNASSIGNED = 0
    ONE_STAR = 1
    TWO_STARS = 2
    THREE_STARS = 3
    FOUR_STARS = 4
    FIVE_STARS = 5

class TRIP_STATUS(Enum):
    UNASSIGNED = 0
    DRIVER_ON_THE_WAY = 1
    DRIVER_ARRIVED = 2
    STARTED = 3
    PAUSED = 4
    CANCELLED = 5
    ENDED = 6

class Util:
    rating_map = {
        RATING.ONE_STAR: "one star",
        RATING.TWO_STARS: "two stars",
        RATING.THREE_STARS: "three stars",
        RATING.FOUR_STARS: "four stars",
        RATING.FIVE_STARS: "five stars"
    }
    @staticmethod
    def rating_to_string(rating = RATING):
        return Util.rating_map.get(rating,"invalid rating")
    @staticmethod
    def is_high_rating(rating = RATING):
        return rating in {RATING.FOUR_STARS, RATING.FIVE_STARS}
    