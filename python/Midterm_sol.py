class TwoDArray(list):
    
    #part A
    def __init__(self, array):
        
        if not isinstance(array, list):
            raise TypeError("You must supply a list of lists")
        
        for x in array:
            if not isinstance(x, list):
                raise TypeError("You must supply a list of lists")
        
        for i in range(1, len(array)):
            if len(array[i]) != len(array[0]):
                raise ValueError("All rows must have the same length")
                
        self.array = array
        
    #I am giving you this one for free to save you time
    def __str__(self):
        return '[' + "\n ".join([str(arr) for arr in self.array]) + ']'
    
    def shape(self):
        return (len(self.array), len(self.array[0]))

    
    #part B
    def __rmul__(self, c): 
        m, n = self.shape()
                
        newarray = [[c*self.array[i][j] for j in range(n)] for i in range(m)]
        
        return TwoDArray(newarray)
        
    
    #Part C
    def __add__(self, other):

        if not isinstance(other, TwoDArray):
            raise TypeError("Cannot add " + str(type(other))+" to TwoDArray")

        #dummy variables for shorter lines
        sa, oa = self.array, other.array
        
        #array dimesnions
        m, n = self.shape()
        m1, n1 = other.shape()

        if m==m1 and n==n1:
            # element-wise addition, no broadcasting
            return TwoDArray([[sa[i][j]+oa[i][j] for j in range(n)] for i in range(m)])        
        elif m==m1 and n==1:
            newsa = [[sa[j][0]]*n1 for j in range(m)]
            return TwoDArray(newsa) + other
            # or TwoDArray([[sa[i][0]+oa[i][j] for j in range(n1)] for i in range(m)]) 
        elif m==1 and n==n1:
            newsa = [sa[0]]*m1
            return TwoDArray(newsa) + other
            # or TwoDArray([[sa[0][j]+oa[i][j] for j in range(n)] for i in range(m1)]) 
        elif (m==m1 and n1==1) or (m1==1 and n==n1):
            return other + self
        else:
            raise ValueError("Shapes are incompatible")   
    
    #part D
    def __sub__(self, other):
        return self + (-1*other)
    
    #Part E
    def __iter__(self):
        return TwoDArrayIterator(self)
    
#more part E
class TwoDArrayIterator:

    def __init__(self, TDA):
        self.array = TDA.array
        self.i, self.j = 0, 0
        self.m, self.n = TDA.shape()
    
    def __next__(self):
        if self.i == self.m:
            raise StopIteration
            
        if self.j == self.n-1:
            item = self.array[self.i][-1]
            self.i += 1
            self.j = 0
            return item
        else:
            item = self.array[self.i][self.j]
            self.j += 1
            return item
              