def swapDataFile();
    file1 = input("Enter files name :-")
    file2 = input("Enter files name :-")

with open(file1, 'r') as a:
    data_a = a.read()

with open(file2, 'r') as a:
        data_b = b.read()

with open(file1, 'w') as a:
            a.write(data_b)

with open(file1, 'w') as a: 
    b.write(data.a)

swapDataFile()