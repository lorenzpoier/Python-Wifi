'''
Funktionen werden mit def eingeleitet und haben einen Namen  und Übergabeparameter

'''

def addiere(c, d):
    summe = c + d
    return summe
def sum_list(l):
        sum = 0
        for s in l:
            sum += s
        return sum 
    
if __name__ == "__main__":    
        
        
    
        
    a=2
    b=3

    sum = a + b

    print(sum)
    print(addiere(a,b))

    k=[1,4,5,7,]
    print(sum_list(k))