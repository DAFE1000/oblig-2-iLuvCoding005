import numpy as np #henter bibloteket så kan bruke e opphøid i x-te og arctan funksjonene
import matplotlib.pyplot as plt #graf funkjsoner
from scipy.optimize import fsolve #funksjon for løse likningen g(x) = 0

#funksjonen f(x)
def f(x):
    return np.exp(-x/4) * np.arctan(x)

#funksjon g(x)av f(x) for å finne hvor den deriverte er 0 med likningen vi fant på papir som g(x). Dette er ikke selveste f'(x) men et utrykk for finne hvor den deriverte er 0, kaller denne g(x)
def g(x):
    return np.arctan(x) - 4/(x**2 + 1)

#løse likning og finne topppunkt kordinatene
x_topp = fsolve(g, 1)  #løse likning g(x) = 0 for finne x kordinatet til toppunktet i f(x), start leting rundt x = 1 fordi vi fant jo at er mellom x = {1, 2}
y_topp = f(x_topp[0])  #y verdien til toppunktet i f(x), finner med plotte inn x verdi for toppunktet som fant med løse g(x)=0, btw på fsolve så blir verdien lagret i en liste så derfor bare skrev [0] for å hente verdien i listen som den returnerer

print("x verdi ", x_topp[0], ", og y verdi ", y_topp)   #test

#lage grafen
x = np.linspace(-5, 5, 500) #legger til x verdier fra -5 til 5 også for at den ikke skal være hakkete så er det delt i 500 små punkter i det intervallet, med denne numpy metoden slipper legge til alle x veriene i en liste selv, men lager alle disse automatisk selv
y = f(x)    #dermed legger til y verdiene i liste i med plotte inn x verdiene vi lagde i f funksjonen. kjører på alle x veriedne, i med at bruker numpy funksjoner så kan vi også automatisk lage en liste med y for alle x verdiene uten loope gjennom, kjøre funksjon og legge til.

#plotter inn x verdien og tegn grafen f(x)
plt.plot(x, y, label="f(x)")

#lage punkt for topp punkt kordinat til f(x)
plt.scatter(x_topp, y_topp)

#pynt og kjør
plt.xlabel("x, akse")
plt.ylabel("y, akse for f(x)")
plt.title("Oblig 2 i Data1700, funksjon f(x) med toppunkt")
plt.show()