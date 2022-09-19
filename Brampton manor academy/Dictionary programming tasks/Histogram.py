hist={}
def histogram(string):
    for i in range(len(string)):
        inp_str=string
        str_cnt=inp_str.count(string[i])
        hist[string[i]]=str_cnt
    return hist
string=input("Enter a string")

def output():
    for x in range(len(histogram(string))):
        key=list(hist.items())[x][0]
        value=list(hist.items())[x][1]
        print(f'The letter {key} appears {value} time(s)')

print(output())
