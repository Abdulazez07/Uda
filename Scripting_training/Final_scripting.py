def flower_dict(filen):
    my_dict = {}
    with open(filen) as f:
        for line in f:
            letter = line.split(': ')[0].lower()
            namai = line.split(': ')[1].strip()
            my_dict[letter] = namai
    return my_dict

def main():
    fulln = input("enter you first and last name: ")
    firstn = fulln.split()[0].lower()
    lastn = fulln.split()[1]
    letr = firstn[0]
    flowerdict = flower_dict('flowers.txt')
    print(flowerdict[letr])
    
main()