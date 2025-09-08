from rider_manager import RiderMgr
from driver_manager import DriverMgr
from trip_meta_data import TripMetaData
from trip import Trip
from strategy_manager import StrategyMgr


class TripMgr:
    __instance = None
    def __init__(self):
        if TripMgr.__instance is not None:
            raise Exception("This class is a Singleton!")
        self.rider_mgr = RiderMgr.get_instance()
        self.driver_mgr = DriverMgr.get_instance()
        self.trips_meta_data_info = {}
        self.trips_info = {}

    @staticmethod
    def get_instance():
        if TripMgr.__instance is None:
            TripMgr.__instance = TripMgr()
        return TripMgr.__instance
    
    def create_trip(self, rider, src_loc, dst_loc):
        meta_data = TripMetaData(src_loc, dst_loc, rider.get_rider_rating())

        strategy_mgr = StrategyMgr.get_instance()
        pricing_strategy = strategy_mgr.determine_pricing_strategy(meta_data)
        driver_matching_strategy = strategy_mgr.determine_matching_strategy(meta_data)

        driver = driver_matching_strategy.match_driver(meta_data)
        trip_price = pricing_strategy.calculate_price(meta_data)

        trip = Trip(rider, driver, trip_price, src_loc, dst_loc, pricing_strategy, driver_matching_strategy)
        trip_id = trip.trip_id

        self.trips_meta_data_info[trip_id] = meta_data
        self.trips_info[trip_id] = trip

    def get_trips_map(self):
        return self.trips_info
