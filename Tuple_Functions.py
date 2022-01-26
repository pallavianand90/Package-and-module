import logging as lg
lg.basicConfig(filename='logger_file3.log' ,level = lg.INFO, format  = '%(asctime)s %(levelname)s %(message)s',filemode = 'a')


class Tuple_func:
    lg.info("Creating Class body")
    def __init__(self,l):
        self.l = l
        lg.info("Body of the Class created")
        
    def count_tuple_func(self,a):
        '''It will count the frequency of element'''
        try:
            lg.info("Started counting the elements..")
            x = self.l.count(a)
            lg.info("Successful")
            return x
        
        except Exception as e:
            lg.exception("Error occured: "+ str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
    def index_tuple_func(self,a):
        '''It will give index of the element'''
        try:
            lg.info("Started counting the indexes..")
            x = self.l.index(a)
            lg.info("Successful")
            return x
        
        except Exception as e:
            lg.exception("Error occured: "+ str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
                    
                 
        