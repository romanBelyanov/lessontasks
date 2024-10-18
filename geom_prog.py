def geom_prog(d, a=1):
    if a < 1000:
        print(a*d)
        geom_prog(d, a*d)

geom_prog(4)