import time
def generateRandom(max,highPrcnt):
    upper_array = list(range(max//2,max+1))
    lower_array = list(range(max//2))
    if int(str(time.time())[-2:]) < highPrcnt :
        return upper_array[int(time.time()*10000000)%len(upper_array)]
    else:
        return lower_array[int(time.time()*10000000) % len(lower_array)]

if __name__ == "__main__":
    for i in range(0,10):
        a = generateRandom(10,73)
        print("random number generated is:" + str(a))