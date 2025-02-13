import random
import time


#Primtal sannolikhets test, ju fler iteration ju större sannolikhet
def miller_rabin_test(n, iterations):

    probablyPrime = True
    composite = False
    

    # Kolla basfall då om talet n är 2 eller 3, då är det sannorligen ett primtal
    # Ett tal som är jämntdelbart eller är lika med 1 eller 0 är inte primtal
    if n == 2 or n == 3:
        return probablyPrime
    elif n < 2 or n % 2 == 0:
        return composite

    # n - 1 = 2^k * m, vi vill hitta m och k vilket är ekvivalent med s och r där s = m och k = r
    m, k = find_m_and_k(n - 1, 0)

    #Loopa i iterationer flera gånger för att bekräfta sannolikheten att talet n är ett primtal
    for i in range(iterations):
        a = random.randint(2, n - 2)  # Slump, välja ett tal mellan som det står i pseudo koden: 2 <= a <= n - 2

        x = pow(a, m, n)  # compositen/primtalet <-> x = a^s mod n

        #Om compositen eller primtalet bli detta, fortsätter vi till nästa steg för att vara säkra eftersom vi kan bara ha haft otur med a
        if x == 1 or x == n - 1:
            continue

        #Gör extra koll
        composite = True
        for _ in range(k - 1):
            x = pow(x, 2, n)  # x = x^2 % n, dubblar exponenten varje gång vi testar
            if x == n - 1:
                composite = False
                break

        if composite:
            return False  # Hittade en witness

    return probablyPrime 

# Rekursivt metod för att hitta m och k
def find_m_and_k(m, exp_also_known_as_k):

    if m % 2 == 1:
        return m, exp_also_known_as_k
    else:
        return find_m_and_k(m // 2, exp_also_known_as_k + 1) # // är heltals division

# Generera 100 primtal med olika bitar, 512, 1024, 2048, 4096
def generatePrime(bits, nbrPrimes):
    print("Starting generating")

    listOfPrimes = []
    start_time = time.time()
    while len(listOfPrimes) < (nbrPrimes):
        potentialCandidates = random.getrandbits(bits)
        if(miller_rabin_test(potentialCandidates, 100) == True):
            listOfPrimes.append(potentialCandidates)
    
    end_time = time.time()
    print("Lista av genererade primtal", listOfPrimes)
    timeToExecute = end_time - start_time
    print(timeToExecute)

    print(len(listOfPrimes))
    return listOfPrimes

#Hitta p och Q
def generate_Prime_For_RSA_Exponents(bits, nbrPrimes):
    listOfPrimes = []

    while len(listOfPrimes) < (nbrPrimes):
        potentialCandidates = random.getrandbits(bits)
        if(miller_rabin_test(potentialCandidates, 20) == True):
            listOfPrimes.append(potentialCandidates)
    q = listOfPrimes[0]
    p = listOfPrimes[1]
    print("Lista av genererade primtal", listOfPrimes)

    return p,q

# Testa primtalslistan angiven i uppgiften
def generateTestPrime(nbrOfTests = 7920):
    listOfPrimes = []
    i = 0
    for i in range(nbrOfTests):
        if(miller_rabin_test(i, 100) == True):
            listOfPrimes.append(i)
            
        i+=1
    print("Lista av genererade primtal", listOfPrimes)

    print(len(listOfPrimes))
    return listOfPrimes

#Vad vi vet
#Vi vet att e är ett fast tal
# e =  3,5,7, or 2^16 + 1
# e = a
# d = e−1 (mod (p − 1)(q − 1))
# m = (p-1)(q-1)
# x such that a × x ≡ 1 (mod m)
# //Find numbers u,v,d such that d=gcd(a,m)=m x u + a x v


def findExponents(bits):

    primes = 2
    # p,q = generate_Prime_For_RSA_Exponents(bits, primes) # Om vi vill generera random p, q primtal
    p = 2179718491501612441833817328375883435620635924535759732650338455028674600279328551254564909638324061112032844686907803823364483045640627651074588155126323
    q = 1019888133180980018385639226956307469544252836639624261650619145840709943531335271857402182539188539679686942934422011898972632483366922612626187985182557
    m = (p-1) * (q-1)
    # Om vi vill ha random värde på e av dessa tal
    # randomValue = [3,5,7, 2**16+1]
    # e = random.choice(randomValue)
    #Bestämt E
    e = 2**16+1

    d = extended_euclidean_with_inverse_mod(m, e)
    print("e value")
    print(e)
    print("m value")
    print(m)
    print("d value")
    print(d)
    return e, m, d

def extended_euclidean_with_inverse_mod(m, a):
    #Find numbers u,v,d such that d=gcd(a,m)=m x u + a x v

    d1 = m
    d2 = a
    v1 = 0
    v2 = 1

    while (d2 != 0):
        q = d1 // d2
        t2 = v1 - q*v2
        t3 = d1 - q*d2
        v1 = v2; d1 = d2
        v2 = t2; d2 = t3

    v=v1
    d=d1

    if d != 1:
        return None
    else:
        return v % m    # Göra v positivt enligt a × v ≡ a × (v + m) ≡ a × v + 0 (mod m) ≡ 1 (mod m)
                        # Thus we can always find a positive solution in the range 0 < v < m, to our problem
     

findExponents(64)
# e × d ≡ 1 mod m för att bekräfta det.
# 3 x 222435085542683005284630252518380267 = 1 mod 333652628314024507926945378777570400
# -> 6.6730526e+35 = 1 mod
 


#generateTestPrime()
#Generera 100 primtal

#generatePrime(256, 100)
#generate_Prime_For_RSA_Exponents(512, 2)
# Testa vår primtals funktion, vilken som

# n = int(input("Vilket nummer vill du se är att ett primtal? "))

# iterations = 20

# result = miller_rabin_test(n, iterations)

#if result == True:
    #print(f"{n} är sannorligen ett primtal")
#else:
    #print(f"{n} är nog inte ett primtal.")


