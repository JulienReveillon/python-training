import numpy as np
import copy


class Bio:
    def __init__(self,age=0):
        self.age=age
        self.energ=1
        self.alive= True
        self.birth= False
    def __str__(self):
        return f"Alive: {self.alive}, since age= {self.age} Energy level={self.energ}"
    

    # Instance method
    def kill(self):
        self.alive=False
    
class Bactery(Bio):
    
    def __init__(self, age=0):
        # Appele au Constructeur de la classe mère (Bio)
        # pour attribuer la valeur des  attribut de la classe mère.
        super().__init__(age)
        self.pos=[0,0]
        self.pBirth=0
        self.pDeath=0
                
    def cons(self,dEnerg):
        self.energ-=dEnerg
        if self.energ<=0 :
            self.energ=0
            self.alive=False
    def setPos(self,vect):
        self.pos=copy.deepcopy(vect)
    def move(self,vect):
        self.pos[0]+=vect[0]
        self.pos[1]+=vect[1]
        
        
        
class colony:    
    def __init__(self,nPop=1):
        self.nPop=nPop
        self.age=np.zeros(nPop)
        self.alive= np.ones(nPop, dtype=bool)
        self.birth= np.zeros(nPop, dtype=bool)
        self.pos=np.zeros([nPop,2])
        
        self.pBirth=np.zeros(nPop)
        self.pDeath=np.zeros(nPop)
    def __str__(self):
        return f"Alive: {self.alive}, since age= {self.age} at {self.pos} "

    # Instance method
    def kill(self):
        self.alive=False 
    def append(self,b):
        self.nPop+=1 
        self.age=np.append(self.age,b.age) 
        self.alive=np.append(self.alive,b.alive) 
        self.birth=np.append(self.birth,b.birth) 
        self.pos=np.append(self.pos,[b.pos],axis=0) 
        self.pBirth=np.append(self.pBirth,b.pBirth) 
        self.pDeath=np.append(self.pDeath,b.pDeath) 
        
    def move(self,nPopVect):
        self.pos+=nPopVect
    def testDeath(self):
        rdDeath=np.random.uniform(0,1,self.nPop)
        self.alive= self.pDeath < rdDeath
        
        # clean deads keeping only position to be returned
        xDead=self.pos[np.logical_not(self.alive)]
        #reduce all thanks to alive
        self.pos=self.pos[self.alive]
        self.age=self.age[self.alive] 
        self.pBirth=self.pBirth[self.alive] 
        self.pDeath=self.pDeath[self.alive]  
        # and reduce alive
        self.alive=self.alive[self.alive] 
        self.nPop=len(self.alive)
        return xDead
    
    def testBirth(self):
        rdBirth=np.random.uniform(0,1,self.nPop)
        self.birth= self.pBirth > rdBirth
        #new born
        born=colony(0)
        born.alive=self.alive[self.birth] 
        born.nPop=len(born.alive)
        born.pos=copy.deepcopy(self.pos[self.birth])
        born.age=np.zeros(born.nPop) 
        born.pBirth=np.zeros(born.nPop)
        born.pDeath=np.zeros(born.nPop)
        
        
        # and rinitialize birth
        self.pBirth[self.birth]=0
        self.birth[self.birth]=False 
        return born
    def add(self,bAdd):
        self.nPop+=len(bAdd.alive)
        self.age=np.append(self.age,bAdd.age) 
        self.alive=np.append(self.alive,bAdd.alive) 
        self.birth=np.append(self.birth,bAdd.birth) 
        self.pos=np.append(self.pos,bAdd.pos,axis=0) 
        self.pBirth=np.append(self.pBirth,bAdd.pBirth) 
        self.pDeath=np.append(self.pDeath,bAdd.pDeath) 
        
        
      
 
    
class milieu:
    def __init__(self,age=0,lx=1,ly=2):
        self.age=age
        self.name="myEnv"
        self.lx=lx
        self.ly=ly
    def __str__(self):
        return f"Environement {self.name} "
    

    # Instance method