#Fibonacci

amount = int(input("How many numbers from the Fibonacci sequence you want ?\n"))

iterations_done = 1
base_num = 1

golden_seq = [1]

while iterations_done < amount:
    golden_seq.append(base_num + golden_seq[len(golden_seq) - 1])
    base_num += golden_seq[len(golden_seq) -1]
    iterations_done += 1

print(f"The first {amount} numbers of the Fibonacci sequence are: {golden_seq}")