# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 10:59:14 2022

@author: demoulin
"""
import sys
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from bioObject import colony


def deriv_popBacteria(POP, t, B, D):
  dPOPdt = B * POP - D * POP
  return dPOPdt






# =============================================================================
# function on colony
def update_p(p,mod,probEvent=0.1,itMax=1):
    # update p=prob for an  event (death, birth, ...) to  happen
    # each it, p is compare to a rnd in [0,1[ 
    # if rnd < p ==> the event happens
    if mod==1 :
        # mod 1 : set p to negative value ==> event will never happen
        p=-1*np.ones(np.size(p))
    if mod==2 :
        # mod 2 : set p to constant value  in ]0,1[ proba for the event to happen each time step
        p=probEvent*np.ones(np.size(p))
    return p

# =============================================================================

if __name__ == "__main__":
    
    # bio 1 : bacteria "bs"
    n0_bs   = 50 #population initial
    vMag_bs = 0.1 #displament, this feature s for graph only it has not yet any effect
    bs      = colony(n0_bs) # initialize the colony
    
    
    plotBact   = False
    
    nit        = 50
    it         = [0]
    population = [n0_bs]
    #create petri box    
    petri      = []
    
#   to store the position of dead bacteria  
    xDead      = np.empty((0, 2))

#   A colony to store the new born bacteria during the time step    
    cbb=colony(0)
    
    # iteration over cycle    
    for i in range(1,nit) :
        # new time
        bs.age   += 1
        #
        # ZONE INTERVENTION DE L'ETUDE
        #
        bs.pDeath = update_p(bs.pDeath,mod=2,probEvent=0.07)
        bs.pBirth = update_p(bs.pBirth,mod=2,probEvent=0.1)             
        #
        # FIN ZONE INTERVENTION DE L'ETUDE
        #
        # move to see bacteria in space, no effect at this stage
        v         = np.random.uniform(-vMag_bs,vMag_bs,[bs.nPop,2])
        bs.move(v)

        # Death : Evaluate Death event 
        posDead   = bs.testDeath()
        xDead     = np.concatenate((xDead,posDead),axis=0)
        
        
        #reproduction : Evaluate Birth event 
        bb        = bs.testBirth()
        bs.add(bb)

    
        #To store populatio at it i
        it.append(i)
        population.append(bs.nPop)
        
        # print status
        print(i,"bs:","Pop=",bs.nPop,"Mean age=",np.mean(bs.age),
              "Mean prob Death=",np.mean(bs.pDeath),
              "Mean prob Birth=",np.mean(bs.pBirth))
        
        # graph
        if plotBact :
            plt.figure(0)
            
            plt.clf()
            
            plt.plot(xDead[:,0],xDead[:,1],'+k')
            
            xAlive=bs.pos[bs.alive]
            plt.plot(xAlive[:,0],xAlive[:,1],'.g')
            
            plt.xlim(-1,1)
            plt.ylim(-1,1)
            plt.show()
            
        
        
    #Final Analysis
    # Plot population
    # Conditins de calculs
    POP_0 = n0_bs
    B     = 0.1
    D     = 0.07
    
    POP  = odeint(deriv_popBacteria, POP_0, it, args = (B,D,) )
    
    
    plt.figure(1)
    plt.plot(it,population,label='stat')
    it=np.array(it)
    popModel= n0_bs*np.exp(0.1*it)
    plt.plot(it,POP,label='equ. diff')
    plt.xlabel('Time',fontsize=14)
    plt.ylabel('Pop',fontsize=14)
    plt.legend(loc='best')
    plt.show()
    
    """
    plt.figure(2)
    plt.hist(bs.age)
    plt.title('Histo age')
    plt.show()
    
    
    plt.figure(3)
    plt.hist(bs.pDeath)
    plt.title('Histo pDeath')
    plt.show()
    
    plt.figure(4)
    plt.hist(bs.pBirth,ec="yellow", fc="green")
    plt.title('Histo pBirth')
    plt.show()
    """
