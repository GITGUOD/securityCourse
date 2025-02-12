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

def generatePrime(bits, nbrPrimes):
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

#generateTestPrime()
#Generera 100 primtal

generatePrime(4096, 100)
# Testa vår primtals funktion, vilken som

# n = int(input("Vilket nummer vill du se är att ett primtal? "))

# iterations = 20

# result = miller_rabin_test(n, iterations)

#if result == True:
    #print(f"{n} är sannorligen ett primtal")
#else:
    #print(f"{n} är nog inte ett primtal.")




