class RiderMgr:
    __instance = None
    def __init__(self):
        if RiderMgr.__instance is not None:
            raise Exception("This class is a singleton!")
        self.__riders_mpp = {}

    @staticmethod
    def get_instance():
        if RiderMgr.__instance is None:
            RiderMgr.__instance = RiderMgr()
        return RiderMgr.__instance
    
    def add_rider(self, rider_name, rider):
        self.__riders_mpp[rider_name] = rider
        
    def get_rider(self, rider_name):
        return self.__riders_mpp.get(rider_name)
        

