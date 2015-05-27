def inBetweenAdv(var1):
        lst = []  
        for i in var1:  
            if isinstance(i, int) or isinstance(i, float):   
                lst.append(str(i) + "D")  
            else:  
                lst.append(str(i) + "X")  
        return lst