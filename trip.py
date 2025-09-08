from constants import TRIP_STATUS
from rider import Rider
from driver import Driver
from location import Location
from pricing_strategy import PricingStrategy
from driverMatching_strategy import DriverMatchingStrategy

class Trip:
    next_trip_id = 1
    def __init__(self, rider : Rider, driver : Driver, price : float, src_loc : Location, dst_loc : Location, pricing_strategy : PricingStrategy, driver_matching_strategy : DriverMatchingStrategy):
        self.rider = rider
        self.driver = driver
        self.src_loc = src_loc
        self.dst_loc = dst_loc
        self.price = price
        self.pricing_strategy = pricing_strategy
        self.driver_matching_strategy = driver_matching_strategy
        self.status = TRIP_STATUS.DRIVER_ON_THE_WAY
        self.trip_id = Trip.next_trip_id
        Trip.next_trip_id += 1

    def display_trip_details(self):
        print(f"\nTrip id - {self.trip_id}")
        print(f"Rider - {self.rider.get_rider_name()}")
        print(f"Driver - {self.driver.get_driver_name()}")
        print(f"Price - {self.price}")
        print(f"Location - ({self.src_loc.latitude}, {self.src_loc.longitude}) -> ({self.dst_loc.latitude}, {self.dst_loc.longitude})")

