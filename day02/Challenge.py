i=1
found=False
while not found:
    ok=True
    d = 1
    while d<=20000:
        if i%d != 0:
            ok=False
            break
        d+=1
    if ok:
        print(i)
        found = True
    i+=1
