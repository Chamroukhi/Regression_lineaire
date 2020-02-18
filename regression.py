import numpy as np
import matplotlib.pyplot as plt

"""

================= Author: 'CHAMROUKHI Naoufel' =====================

=============  Un exemple de la régression linéaire simple =========
""" 
"""
1) calculer Xbar et Ybar => Xbar = 
======================= 18 Février 2020 ============================



"""


#dataset
x = np.array([[28],[50],[196],[55],[190],[110],[60],[48],[90],[35],[86],[65],[32],[52],[40],[70],[28],[30],[105],[52],[80],[60],[20],[100]])
y= np.array([[130],[280],[800],[268],[790],[500],[320],[250],[378],[250],[350],[300],[155],[245],[200],[325],[85],[78],[375],[200],[270],[295],[85],[495]])

"""
selection des données a partir d'un fichier '
A=open("test.csv", 'r')
A.readline()
X=array([])
Y=array([])
for i in A:
    var=i.split(",")
    x=float(var[0])
    y=float(var[1])
    X=append(X,x)
    Y=append(Y,y)
    
    """
    
    
#calculer Xbar et Ybar
xbar=sum(x)/len(x)
ybar=sum(y)/len(y)

#calculer la variance Var(x)
Var=sum(pow(x-xbar,2))/len(x)

#calculer la Cov(x,y)
Cov=sum((x-xbar)*(y-ybar))/len(x)

#calculer la valeur de a et de b
a=Cov/Var
b=ybar-a*xbar




#présenter les nuages de point x,y
plt.scatter(x,y)

#tracer la droite y= a*x + b 
plt.plot(x,a*x+b,'g',label='Régression linéaire')
plt.show()


#afficher la variance, covariance,a,b  
print('Variance(x) :' , Var)
print('Covariance(x) :',Cov)
print('Le valeur de a:',a)
print('le valeur de b:',b)


#Prédiction
#la droite linéaire et de la forme suivante y= a*x + b
#pour prédire un exemple juste modifier la surface y ou le prix x 
def predsurface(Px):
    
    return a*Px+b

def predprix(Py):
   
    return (Py-b)/a


print('pour prédire de surface taper 1 et pour prédire le prix taper 2 :')
choix=int(input())

if choix == 1 :
    print('inserer le prix')
    prix=int(input())
    
    print('la surface y=' ,predsurface(prix))
elif choix == 2:
    print('inserer la surface')
    surface=float(input())
    
    print('le prix x=' ,predprix(surface))
else:
    print('choisit un valeur correcte')    

    

