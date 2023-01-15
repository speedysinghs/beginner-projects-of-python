import os

dirs = os.listdir()
j = 0            # count how many files have binod
counter = 0       #count how many times binod detected in all files
list1 = []         #write down the files which have binod
for i in dirs:
    if i.endswith("txt"):
        print(f"Detecting in file {i}")
        with open(i, "r") as f:
            content = f.read()
            if "binod" in content:
                list1.append(i)
                count = content.count("binod")
                print(f"Binod detected in file {i} and detected {count} times\n")
                counter = count + counter
                j = j + 1
            else:
                print(f"The file {i} does not have binod\n")
print("****************************************")
print(f"The binod is detected in {j} files and counted as {counter} times")
print(list1)

        
