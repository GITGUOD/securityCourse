import random

# e × d ≡ 1 mod m för att bekräfta det.
# 3 x 222435085542683005284630252518380267 = 1 mod 333652628314024507926945378777570400
# -> 6.6730526e+35 = 1 mod

def verify_rsa_parameters(e, d, m):
    # Kontrollera om e * d ≡ 1 (mod m)
    return (e * d) % m == 1

# Givna värden
# e = 65537
# m = 2223069023157641372458942672097486367226421675176895810123567446504051008870279889359540694490231672109842500076816434183892000730732485561511817135275752279254094900703199824674656963980110603716338692413613425683463504500007204585108226883427622404822379758892276777248266468062387121226055508888410839032
# d = 1578200243700999778675019710423236503373308129137437698732152814685558955074212156985244828903558581817637855845918510411519587805332249313134546958753675794506553845157957719193937621589920593687632543498112184618594427733453395799727564032200948471958833035723668604578373219602218948108144385714057749009

# Gamla
#e = 3
# d = 222435085542683005284630252518380267
# m = 333652628314024507926945378777570400

#Kryptering

s = 100276256409632925171776883962
e = 65537
n = 2223069023157641372458942672097486367226421675176895810123567446504051008870279889359540694490231672109842500076816434183892000730732485561511817135275755478860719583295660044131212296171015768605099867797607726641064373884551015248931338850519799917423171478679898107063988805177916128776319209664551147911 # p*q
#def C(s, e, n):
    # Kontrollera om s^e mod n
    #return (s ** e) % n

def C(s, e, n):
    # Kontrollera om s^e mod n
    return pow(s, e, n)


d = 1578200243700999778675019710423236503373308129137437698732152814685558955074212156985244828903558581817637855845918510411519587805332249313134546958753675794506553845157957719193937621589920593687632543498112184618594427733453395799727564032200948471958833035723668604578373219602218948108144385714057749009

#def Z(c, d, n):
    #Kontrollera om c^d (mod n)
    #return (c ** d) % n

def Z(c, d, n):
    return pow(c, d, n)

# c = question_D_2(s, e, n)
# vi fick det från den
c = C(s, e, n)

print("answer to D2, encrypting")
print(C(s, e, n))

print("Answer to D3, decrypting")
print(Z(c, d, n))


# Verifiera
# result = verify_rsa_parameters(e, d, m)
# print("Verification result:", result)



# r = random.getrandbits(100)
#print(2179718491501612441833817328375883435620635924535759732650338455028674600279328551254564909638324061112032844686907803823364483045640627651074588155126323*1019888133180980018385639226956307469544252836639624261650619145840709943531335271857402182539188539679686942934422011898972632483366922612626187985182557)

# print(r)