import sys
 
def solve():
    line = sys.stdin.readline().split()
    M = int(line[0])
    N = int(line[1])
    print((M * N) // 2)
 
if __name__ == '__main__':
    solve()