import math

# define class similarity
class similarity:
    
    #class instantiation
    def __init__ (self, ratingP, ratingQ):
        self.ratings1 = ratingP
        self.ratings2 = ratingQ
        
    def minkowski(self, r):
        
        # (1) MY CODE HERE
        # calculate Minkowski distance
       distance = 0
       for k in self.ratings1.keys():
           if k in self.ratings2.keys():
               x = self.ratings1[k]
               y = self.ratings2[k]
               distance += pow(abs(x - y), r)
        # return value of minkowski distance
       return pow(distance,1/r)
    
    def pearson(self):

        # (2) MY CODE HERE
        sumpq = 0 
        sump = 0 
        sumq = 0
        sump2 = 0
        sumq2 = 0
        n = 0
        # Iterating over userratings1 keys
        for k in self.ratings1.keys():   
        # Determining if the value of item is in the userratings2 keys
            if k in self.ratings2.keys():
                p = self.ratings1[k]
                q = self.ratings2[k]
                sumpq += p * q
                sump += p
                sumq += q
                sump2 += pow(p, 2)
                sumq2 += pow(q, 2)
                n +=1
        nr = (sumpq - (sump * sumq) / n)
        dr = (math.sqrt(sump2 - pow(sump, 2)/ n) * math.sqrt(sumq2 - pow(sumq, 2) /n ))
        r = nr/dr
        # returning pearson value
        return round(r,4)
    

UserPRatings = {'Motorola':8, 'LG':5, 'Sony':1, 'Apple':1, 'Samsung':5, 'Nokia':7}
UserQRatings = {'Apple':7, 'Samsung':1, 'Nokia':4, 'LG':4, 'Sony':6, 'Blackberry':3}


# instantiating the class with the dictionaries provided - UserP and UserQ
sim = similarity(UserPRatings, UserQRatings)

# calling minkowski to calculate manhattan distance
manhattan = similarity.minkowski(sim, 1)
print('The Manhattan Distance is', round(manhattan,4))

# calling minkowski to calculate euclidean distance
euclidean = similarity.minkowski(sim, 2)
print('The Euclidean Distance is', round(euclidean, 4))

# calling minkowski to calculate minkowski distance
mink = similarity.minkowski(sim, 3)
print('The Minkowski Distance is', round(mink, 4))

# calling pearson
pear = similarity.pearson(sim)
print('The Pearson Correlation is', round(pear,4))

  



