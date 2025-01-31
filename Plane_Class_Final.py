"""
Maggie Friend
Plane Class Final
"""
class Plane():
    def __init__ (self, model, seats):
        self.__model= model
        self.__seats= seats
        
    def get_type(self):
        if 1<= self.__seats <11:
            self.__type = "puddle jumper"
        elif self.__seats < 21:
            self.__type = "small"
        elif self.__seats < 101:
            self.__type ="medium"
        elif self.__seats < 201:
            self.__type = "large"
        else:
            self.__type = "jumbo"
        return self.__type

#list of planes
lst = [Plane("X-wing", 2), Plane("Millenium Falcon", 20), Plane("Death Star", 5000)]

pj=0
s=0
m=0
l=0
j=0

#counts how many of each type of plane are in the list
for c in lst:
    t = c.get_type()
    if t == "puddle jumper":
        pj+=1
    elif t == "small":
        s+=1
    elif t == "medium":
        m+=1
    elif t == "large":
        l+=1
    else:
        j+=1
        
#prints total of each type of plane in the list
print("Puddle Jumper: " + str(pj) +", Small: " + str(s) + ", Medium: " +str(m)+ ", Large: " +str(l)+ ", Jumbo: " +str(j))
        