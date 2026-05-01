def count_implemented_problems(confidence_lines):
    count = 0
    for line in confidence_lines:
        if sum(line) >= 2:
            count += 1
    return count
 
n = int(input())
confidence_lines = [list(map(int, input().split())) for _ in range(n)]
print(count_implemented_problems(confidence_lines))