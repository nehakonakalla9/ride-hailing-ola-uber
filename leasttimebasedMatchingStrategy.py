from driverMatching_strategy import DriverMatchingStrategy
from driver_manager import DriverMgr
from trip_meta_data import TripMetaData
from driver import Driver


class LeastTimeBasedMatchingStrategy(DriverMatchingStrategy):
    def match_driver(self, meta_data : TripMetaData):
        driver_mgr = DriverMgr.get_instance()
        
        if len(driver_mgr.get_drivers_mpp()) == 0:
            print("No drivers")
            return None
        print("Using Quadtrees to see nearest cabs, " \
        "using driver manager to get driver details and send notifications")

        driver = next(iter(driver_mgr.get_drivers_mpp().values()))

        print(f"Setting{driver.get_driver_name()} as driver")
        meta_data.set_driver_rating(driver.get_rating())
        return driver


