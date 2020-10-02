def find_fraction(num):
    changesing=False
    num=round(float(num), 8)
    if num<0:
        changesing=True
        num=abs(num)
    i=0
    while True:
        i+=1
        for j in range(abs(round(i/num)-1), round(i/num)+1):
            if j!=0:
                if str(round((i/j), 8))==str(float(num)):
                    if j==1:
                        return str(i)
                    else:
                        if changesing:
                            return '-'+str(i)+'/'+str(j)
                        if not(changesing):
                            return str(i)+'/'+str(j)