from multiprocessing import Pool
def cube(x):
    print(x)
    return x**3

def run():
    p = Pool(2)
    kq = p.map(cube, [0, 1, 2])
    print(kq)
    p.close()
    p.join()
    print('END')

if __name__ == '__main__':
    run()