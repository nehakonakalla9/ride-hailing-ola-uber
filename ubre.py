from rider import Rider
from driver import Driver
from rider_manager import RiderMgr
from driver_manager import DriverMgr
from trip_manager import TripMgr
from location import Location
from constants import RATING

keerti_rider = Rider("Keerti", RATING.FIVE_STARS)
gaurav_rider = Rider("Gaurav", RATING.FIVE_STARS)

rider_mgr = RiderMgr.get_instance()
rider_mgr.add_rider("keerti", keerti_rider)
rider_mgr.add_rider("gaurav", gaurav_rider)

yogita_driver = Driver("Yogita", RATING.THREE_STARS)
riddhi_driver = Driver("Riddhi", RATING.FOUR_STARS)

driver_mgr = DriverMgr.get_instance()
driver_mgr.add_driver("yogita", yogita_driver)
driver_mgr.add_driver("riddhi", riddhi_driver)

trip_mgr = TripMgr.get_instance()

print("\nCreating Trip for Keerti from location (10,10) to (30,30)")
trip_mgr.create_trip(keerti_rider, Location(10, 10), Location(30, 30))

print("\nCreating Trip for Gaurav from location (200,200) to (500,500)")
trip_mgr.create_trip(gaurav_rider, Location(200, 200), Location(500, 500))

trips_map = trip_mgr.get_trips_map()
for trip in trips_map.values():
    trip.display_trip_details()