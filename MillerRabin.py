import random


#Primtal sannolikhets test, ju fler iteration ju större sannolikhet
def miller_rabin_test(n, iterations):

    # Kolla basfall då om talet n är 2 eller 3, då är det sannorligen ett primtal
    # Ett tal som är jämntdelbart eller är lika med 1 eller 0 är inte primtal
    if n in (2, 3):
        return True
    if n < 2 or n % 2 == 0:
        return False

    # n - 1 = 2^k * m
    m, k = find_m_and_k(n - 1, 0)

    for _ in range(iterations):
        a = random.randint(2, n - 2)  # Slump, välja: 2 <= a <= n-2
        x = pow(a, m, n)  # Modulär exponentiering där vi försöker ta reda på compositen/primtalet

        if x == 1 or x == n - 1:
            continue  # Fortsätt till nästa iteration

        composite = True
        for _ in range(k - 1):
            x = pow(x, 2, n)  # x = x^2 % n
            if x == n - 1:
                composite = False
                break

        if composite:
            return False  # Hittade en witness

    return True  # Ingen witness hittades, n är sannorliken primtal


def find_m_and_k(m, exp_also_known_as_k):

    if m % 2 == 1:
        return m, exp_also_known_as_k
    else:
        return find_m_and_k(m // 2, exp_also_known_as_k + 1)


# Testa vår primtals funktion

n = int(input("Vilket nummer vill du se är att ett primtal? "))
# n = 53
iterations = 10
print(f"{n}, är det ett primtal?: {miller_rabin_test(n, iterations)}")


    
