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

        elif line.startswith("say '") and line[-1] == "'":
            message = line[5:-1] # need to exclude the last '
            print(message)
        
        elif line.startswith("say '") and line[-1] == "x":
            closing_quote_index = line[5:].find("'")
            message = line[5:5+closing_quote_index] # need to exclude the last '
            times_to_print = int(line[5+closing_quote_index+1:-1])
            for i in range(times_to_print):
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

    elif instr.lower() == "reverse":
        if line == instr:
            original_text = brain.pop()
            reversed_text = original_text[::-1]
            print(reversed_text)

        elif line.startswith("reverse '") and line[-1] == "'":
            message = line[9:-1] 
            reversed_message = message[::-1]  
            print(reversed_message)
