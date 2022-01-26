import logging as lg
lg.basicConfig(filename='logger_file1.log' ,level = lg.INFO, format  = '%(asctime)s %(levelname)s %(message)s',filemode = 'a')


class Set_func:
    lg.info("Creating Class body")
    def __init__(self,l):
        self.l = l
        lg.info("Body of the Class created")
        
    def add_set_func(self,a):
        '''It will add an element to the set'''
        try:
            lg.info("Started adding element")
            self.l.add(a)
            lg.info("Successful")
            return self.l
        
        except Exception as e:
            lg.exception("Error occured: "+ str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
    def difference_set_func(self,a):
        '''It will subtract the elements which are presented in the both sets '''
        try:
            lg.info("Started subtracting")
            z = self.l.difference(a)
            lg.info("Successful")
            return z
        
        except Exception as e:
            lg.exception("Error occured: "+ str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
    def discard_set_func(self,a):
        '''It will discard the element which is passed as argument '''
        try:
            lg.info("Started discarding")
            self.l.discard(a)
            lg.info("Successful")
            return self.l
        
        except Exception as e:
            lg.exception("Error occured: "+ str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
    def intersection_set_func(self,a):
        '''It will select the element which is common in the both sets '''
        try:
            lg.info("Started selecting")
            z = self.l.intersection(a)
            lg.info("Successful")
            return z
        
        except Exception as e:
            lg.exception("Error occured: "+ str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
    def pop_set_func(self):
        '''It will remove the very first element from the set  '''
        try:
            lg.info("Started removing")
            self.l.pop()
            lg.info("Successful")
            return self.l
        
        except Exception as e:
            lg.exception("Error occured: "+ str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
    def isdisjoint_set_func(self,a):
        '''It will return true if no items of set 1 is matched with set 2 '''
        try:
            lg.info("Started matching")
            y = self.l.isdisjoint(a)
            lg.info("Successful")
            return y
        
        except Exception as e:
            lg.exception("Error occured: "+ str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
    def union_set_func(self,a):
        '''Return a set that contains all items from both sets, duplicates are excluded '''
        try:
            lg.info("Started adding the sets ")
            z = self.l.union(a)
            lg.info("Successful")
            return z
        
        except Exception as e:
            lg.exception("Error occured: "+ str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
    def update_set_func(self,a):
        '''It will insert set 2 into set 1 '''
        try:
            lg.info("Started inserting")
            self.l.update(a)
            lg.info("Successful")
            return self.l
        
        except Exception as e:
            lg.exception("Error occured: "+ str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
                            