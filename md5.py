from hashlib import md5



for i in range(10000):

    a = md5(str(i).encode('Utf-8')).hexdigest()

    print(a,i)
