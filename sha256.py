from hashlib import sha256
import time

start = time.time()
for input in range(100000):   #You can write any number you want in the range 

    hash = sha256(str(input).encode('utf-8')).hexdigest()
    print(hash,input)
    stop =time.time()
    print("Result Time ",stop-start )
quit()


