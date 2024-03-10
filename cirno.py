import sys

lines = []
try:
    fileName = sys.argv[1]
    file = open(fileName)
    lines = file.read().split("\n")
    file.close()

except Exception as e:
    print(f"Error while opening file:\n{e}")
    sys.exit(0)

brain = []

print("Cirno is starting")
for line in lines:
    parts = line.split(" ")
    instr = parts[0].lower()

    if instr == "say":
    
        if line == instr:
            print(brain.pop())

        elif line.startswith("say '") and line[-1]:
            message = line[5:-1] # need to exclude the last '
            print(message)
            
        else:
            raise SyntaxError

        
    elif instr == "hear":

        if line == instr:
            value = input()
            try:
                int_value = int(value)
                brain.append(int_value)
            except ValueError:
                # If input is not an integer, store it as a string
                brain.append(value)

        else:
            raise SyntaxError

    elif instr.lower() == "multiply":
        try:
            times_to_multiply = int(parts[1])
        except Exception as e:
            print(e)
            break
        result = 1
        for i in range(times_to_multiply):
            result *= brain.pop()
        brain.append(result)