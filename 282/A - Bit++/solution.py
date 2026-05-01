def execute_bit_plus_plus_program(program):
    x = 0
    for statement in program:
        if '+' in statement:
            x += 1
        elif '-' in statement:
            x -= 1
    return x
 
def main():
    input_data = []
    while True:
        try:
            line = input().strip()
            input_data.append(line)
        except EOFError:
            break
 
    n = int(input_data[0])
    program = input_data[1:n+1]
    final_value = execute_bit_plus_plus_program(program)
    print(final_value)
 
if __name__ == "__main__":
    main()