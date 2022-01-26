import logging as lg
lg.basicConfig(filename='logger_file.log' ,level = lg.INFO, format  = '%(asctime)s %(levelname)s %(message)s',filemode = 'a')

class List_func:
    lg.info("Creating Class body")
    def __init__(self,l):
        self.l = l
        lg.info("Body of the Class created")
        
    def append_list_func(self,*args):
        '''It will append one or more lists'''
        l1 = []
        try:
            lg.info("Started appending list")
            l1.append(self.l)
            for i in args:
                l1.append(i)
                lg.info("Successful")
            return l1
        
        except Exception as e:
            lg.exception("Error occured: "+ str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
    def get_length_func(self):
        '''It will give the complete length of list elements'''
        try:
            lg.info("Started counting the length of list")
            Len = len(self.l)
            lg.info("Successful")
            return Len
            
            
        except Exception as e:
            lg.exception("Error occured: "+ str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
            
    def clear_list_fun(self):
        '''It will clear the complete list'''
        try:
            lg.info("Started clearing the list")
            self.l.clear()
            lg.info("Successful")
            return self.l
           
            
        except Exception as e:
            lg.exception("Error occured: " + str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
                   
    def copy_list_func(self):
        '''It will copy the existing list elements'''
        try:
            lg.info("Started copying the list")
            x = self.l.copy()
            lg.info("Successful")
            return x
            
            
        except Exception as e:
            lg.exception("Error occured: " + str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
            
    def extend_list_func(self,*args):
        '''It will append the multiple list as single list'''
        l1 = []
        try:
            lg.info("Started extending the list")
            l1.extend(self.l)
            for i in args:
                l1.extend(i)
                lg.info("Successful")
            return l1
            
            
        except Exception as e:
            lg.exception("Error occured: " + str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
            
    def count_list_func(self,a):
        '''It will count the number of each elements which you pass as argument '''
        try:
            lg.info("Started counting the list elements...")
            x = self.l.count(a)
            lg.info("Successful")
            return x
            
            
        except Exception as e:
            lg.exception("Error occured: " + str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
            
    def index_list_func(self):
        '''It will give the index number even list contains duplicates'''
        try:
            lg.info("Started counting the index of the list elements even duplicates present...")
            for i in range(len(self.l)):
                if self.l[i] == self.l[i-1]:
                    lg.info("Successful")
                    #return '[{a},{b}]'.format(b=self.l[i],a=i)
                    print([i,self.l[i]])
                    
                else:
                    lg.info("Successful")
                    #return '[{a},{b}]'.format(b=self.l[i],a=i)
                    print([i,self.l[i]])
            
        except Exception as e:
            lg.exception("Error occured: " + str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
                    
    def insert_list_func(self,integer,l3):
        '''Integer value should be 1 positional argument and 2 argument can be any datatype '''
        try:
            lg.info("Started inserting the list elements...")
            self.l.insert(integer,l3)
            lg.info("Successful")
            return self.l
           
            
        except Exception as e:
            lg.exception("Error occured: ",e)
                         
    def pop_list_func(self,a):
        ''' a--> should be integer'''
        try:
            lg.info("Started poping the list elements according to index...")
            self.l.pop(a)
            lg.info("Successful")
            return self.l
           
            
        except Exception as e:
            lg.exception("Error occured: " + str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
                  
    def remove_list_func(self,a):
        '''User can select any element which they want to remove'''
        try:
            lg.info("Started removing the list elements...")
            self.l.remove(a)
            lg.info("Successful")
            return self.l
          
            
        except Exception as e:
            lg.exception("Error occured: " + str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
            
    def reverse_list_func(self):
        '''It will reverse all the elements in the list'''
        try:
            lg.info("Started reversing the list elements...")
            self.l.reverse()
            lg.info("Successful")
            return self.l
          
            
        except Exception as e:
            lg.exception("Error occured: " + str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
            
            
    def sort_list_func(self):
        '''It will sort the elements in the list'''
        try:
            lg.info("Started counting the list elements...")
            self.l.sort()
            lg.info("Successful")
            return self.l
            
            
        except Exception as e:
            lg.exception("Error occured: " + str(e))
            lg.error("Something went Wrong")
            lg.warning("Fix the bug otherwise code will not work!!!!")
            
                
                    
                    
            