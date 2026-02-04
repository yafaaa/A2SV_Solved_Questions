if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l = [[i,j,q] for i in range(x+1) for j in range(y+1) for q in range(z+1) if i+j+q!=n]
    print(l)
                    
