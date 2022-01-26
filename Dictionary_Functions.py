import logging as lg
lg.basicConfig(filename='logger_file2.log' ,level = lg.INFO, format  = '%(asctime)s %(levelname)s %(message)s',filemode = 'a')

class Dictionary_func:
    lg.info("Creating Class body")
    def __init__(self,l):
        self.l = l
        lg.info("Body of the Class created")
        
    def items_dict_func(self):
        '''It will give all the items of the dictionary'''
        try:
            lg.info("Started fetching the elements..")
            x = self.l.items()
            lg.info("Successful")
            return x
        
        except Exception as e:
            lg.exception("Error occured: "+ str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
    def keys_dict_func(self):
        '''It will give all the keys of the dictionary'''
        try:
            lg.info("Started fetching the keys..")
            x = self.l.keys()
            lg.info("Successful")
            return x
        
        except Exception as e:
            lg.exception("Error occured: "+ str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
             
    def values_dict_func(self):
        '''It will give all the values of the dictionary'''
        try:
            lg.info("Started fetching the values..")
            x = self.l.values()
            lg.info("Successful")
            return x
        
        except Exception as e:
            lg.exception("Error occured: "+ str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
    def get_dict_func(self,a):
        '''It will give the value of the given key'''
        try:
            lg.info("Started fetching the keys..")
            x = self.l.get(a)
            lg.info("Successful")
            return x
        
        except Exception as e:
            lg.exception("Error occured: "+ str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
    def fromkeys_dict_func(self,a,b):
        '''It will take 2 arguments a as key and b as value'''
        try:
            lg.info("Started mapping the key-value pair..")
            x = dict.fromkeys(a,b)
            lg.info("Successful")
            return x
        
        except Exception as e:
            lg.exception("Error occured: "+ str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
    def pop_dict_func(self,a):
        '''It will remove the key-value pair from the dictionary '''
        try:
            lg.info("Started f the keys..")
            self.l.pop(a)
            lg.info("Successful")
            return self.l
        
        except Exception as e:
            lg.exception("Error occured: "+ str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
    def update_dict_func(self,**kwargs):
        '''It will update the key-value pair of the dictionary'''
        try:
            lg.info("Started adding the key-value pair..")
            self.l.update(eval(kwargs))
            lg.info("Successful")
            return self.l
        
        except Exception as e:
            lg.exception("Error occured: "+ str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
                     
                     
        