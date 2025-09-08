from abc import ABC, abstractmethod
from trip_meta_data import TripMetaData
from driver_manager import Driver

class DriverMatchingStrategy(ABC):
    @abstractmethod
    def match_driver(self, trip_meta_data : TripMetaData):
        pass