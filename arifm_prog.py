def arifm_prog(d, a=0):
    if a < 1000:
        print(a+d)
        arifm_prog(d, a+d)

arifm_prog(4)