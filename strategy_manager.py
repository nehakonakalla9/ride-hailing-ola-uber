import trip_meta_data
from defaultPricingStrategy import DefaultPricingStrategy
from leasttimebasedMatchingStrategy import LeastTimeBasedMatchingStrategy

class StrategyMgr:
    __instance = None
    def __init__(self):
        if StrategyMgr.__instance is not None:
            raise Exception("This class is a singleton!")
    
    @staticmethod
    def get_instance():
        if StrategyMgr.__instance is None:
            StrategyMgr.__instance = StrategyMgr()
        return StrategyMgr.__instance
    
    def determine_pricing_strategy(self, trip_meta_data):
        print("Based on location and other factors, setting pricing strategy")
        return DefaultPricingStrategy()

    def determine_matching_strategy(self, trip_meta_data):
        print("Based on location and other factors, setting matching strategy")
        return LeastTimeBasedMatchingStrategy()
