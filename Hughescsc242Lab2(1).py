# Lab 2
#
# Kristofer Hughes
#
# Your collaborators (if any)
#

class Worker(object):
    
    def __init__(self, wrkname='Jane Doe', payrate=8.25):
        self.wrkname = wrkname
        self.payrate = payrate
    

    def changeRate(self,n):
        self.payrate = n
        "changes payrate to n"
        

    def weeklyPay(self,n):
        return "Not Implemented"


    def __repr__(self):
        return 'Worker({}, { :2f})'.format(self.wrkname, self.payrate)

    
    

class HourlyWorker(Worker):

    def __init__(self, wrkname='Jane Doe', payrate=8.25):
        self.wrkname = wrkname
        self.payrate = payrate

    
    def weeklyPay(self,n):
        overtime=0
        if n > 40:
            overtime = n-40
            normal=40
            wkPay=normal*self.payrate+(overtime*(2*self.payrate)
            else:
                wkPay = self.payrate*n
        "multiplies payrate by n"
        return wkPay
    
    

class SalariedWorker(Worker):

    def __init__(self, wrkname='Jane Doe', payrate=8.25):
        self.wrkname = wrkname
        self.payrate = payrate
        
    
    def weeklyPay(self,n):
        wkPay = self.payrate*40
        "multiples payrate by 40, regardless of what n is"
        return wkPay
        
    

