import os
os.chdir("C:\\Users\Rana\Desktop\Hello")
print(f"{os.getcwd()}")
# os.rename("Viv.png","1.png")
get_files = os.listdir()
print(f"{get_files}")

def Names(file):
    count = 0
    ignore = file.readlines()
    ignore = [i.replace("\n","") for i in ignore]
    print(ignore)
    for i,j in enumerate(get_files):
        print("H",j[:-4])
        for k in ignore:
            if not (k == j[:-4]):
                pass
            else:
                break
        else:
            os.rename(f"{j}", f"{j.capitalize()}")


def fomat(fmt):
    l = []
    n = 5
    for i, j in enumerate(get_files):
        print(f"{j[-4:]}")
        if j[-4:] == fmt:
            print(j)
            os.rename(f"{j}", f"{n}.png")
            n += 1


def Pretify(p,f,fm):
    os.chdir(f"{p}")
    fomat(fm)
    Names(f)




path = os.getcwd()
f = open(f"E:\\na.txt",'r')
Format = ".png"

Pretify(path,f,Format)
get_files = os.listdir()
print(f"{get_files}")
