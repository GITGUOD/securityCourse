
import random
import time

#bits
bits = 512
#bits = 2048
iterations = 1000

def generateRandomLargeBit(bits):
    return random.getrandbits(bits)

n = generateRandomLargeBit(bits)


def first_Algorithm(n, iterations):

    x = random.randint(2, n - 2)  # Slump, välja ett tal 2 <= a <= n - 2 där a är nu x


    start_time = time.time()
    # Första algoritmen där vi använder x = x^2 % n
    for i in range(iterations):

        x = pow(x, 2, n)  # x = x^2 % n, dubblar exponenten varje gång vi testar
    end_time = time.time()

    calculating_Time_Complexity = end_time - start_time
    return calculating_Time_Complexity


def second_Algorithm(n, iterations):
    start_time = time.time()
    # Andra algoritmen där vi använder x = a^(2^j) * s % n

    a = random.randint(2, n - 2)  # Slump, välja ett tal 2 <= a <= n - 2
    m = random.randint(1, n - 1)  # Slump, välja ett tal 1 <= s <= n - 1, Olika slumpiga tal

    j = random.randint(0, 100)
    
    for i in range(iterations):

        x = pow(a, (2**j) * m, n) # a^(2^j * m) mod n

    end_time = time.time()

    calculating_Time_Complexity = end_time - start_time
    return calculating_Time_Complexity

#Jämföra de två algoritmerna och printa ut det
def compareAlgorithm():
    timeForFirstAlgoritm = first_Algorithm(n, iterations)
    timeForSecondAlgoritm = second_Algorithm(n, iterations)

    if timeForFirstAlgoritm > timeForSecondAlgoritm:

        print("First algoritm is faster:")
        print(timeForFirstAlgoritm - timeForSecondAlgoritm)
        return timeForFirstAlgoritm
    else:
        print("Second algoritm is faster:")
        print(timeForSecondAlgoritm - timeForFirstAlgoritm)
        return timeForSecondAlgoritm

def getAverageTime():

    average = 0 
    for _ in range(100):
        average += compareAlgorithm()

    print("medelvärde: ")
    print(average/100)

#getAverageTime()
compareAlgorithm()