'''
IDLE ist zur Zeilenweise Ausführung von Python Code geeignet


'''
a=5
b=7

print(a,"geteilt durch",b,"ergibt",str(a/b)+"!")
print("%d geteilt durch %d ergibt %-12.3f=" % (a,b,a/b))

print("{0:d} geteilt durch {1:d} (nochmals {1:d}) ergibt{2:0.3f}".format(a,b,a/b))
print("{0:.0f} geteilt durch {1:d} (nochmals {1:d}) ergibt{2:0.3f}".format(a,b,a/b))
print("{:f} geteilt durch {:d} ergibt{:0.3f}".format(a,b,a/b))
