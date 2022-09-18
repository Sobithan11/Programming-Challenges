
def metres(rods):
    metres=rods*5.0292
    return metres

def furlongs(rods):
    furlongs=rods/40
    return furlongs

def feet(rods):
    feet=rods*(5.0292/0.3048)
    return feet

def miles(rods):
    miles=rods*(5.0292/1609.34)
    return miles

def time(rods):
    time=(miles(rods)/3.1)*60
    return time

def output(rods):
    print (f'Metres: {metres(rods)}')
    print(f'Feet: {feet(rods)}')
    print(f'Miles: {miles(rods)}')
    print(f'furlongs: {furlongs(rods)}')
    print(f'Minutes to walk in {(rods)} rods is {time(rods)}')
    return output

def run():
    rods=float(input("Input rods: "))
    print("You input", rods, "rods")
    print("Conversions")
    x=output(rods)
    print(x)
    
if __name__=="__main__":
    run()
    
    








