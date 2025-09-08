from driver import Driver
class DriverMgr:
    __instance = None
    def __init__(self):
        if DriverMgr.__instance is not None:
            raise Exception("This class is a singleton!")
        self.__drivers_mpp = {}
    @staticmethod
    def get_instance():
        if DriverMgr.__instance is None:
            DriverMgr.__instance = DriverMgr()
        return DriverMgr.__instance
    
    def add_driver(self, driver_name, driver : Driver):
        self.__drivers_mpp[driver_name] = driver
    
    def get_driver(self, driver_name):
        return self.__drivers_mpp.get(driver_name)
    
    def get_drivers_mpp(self):
        return self.__drivers_mpp

