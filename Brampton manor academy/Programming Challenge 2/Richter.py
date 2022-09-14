y=[1.0,5.0,9.1,9.2,9.5]
def measurements(richter):
    print("Richter      Joules     Tnt")
    for i in range(0,5):
        print(y[i],    energy(y[i]),      tons_of_tnt(y[i]))
    return measurements

def energy(richter):
    energy=10**(1.5*richter+4.8)
    return energy

def tons_of_tnt(richter):
    tons_of_tnt=energy(richter)/(4.184*10**9)
    return tons_of_tnt

def output(richter):
    print("Equivalence in joules: ", energy(richter))
    print("Equivalence in tons of tnt: ", tons_of_tnt(richter))
    return output

richter=float(input("Please eneter a Richter scale value"))
print("Richter value: ", richter)

x=output(richter)
print(x)


y=measurements(richter)
print(y)





