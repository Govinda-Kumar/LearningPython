try:
    # using open() function to open a file
    file1 = open('sample.txt', 'r')
    content = file1.read()
    print("Reading file content:")
    # print(content)
    l = 1
    for line in content.splitlines():
        print(f"Line {l}: {line.strip()}")
        l += 1
    file1.close()

    # using with open() as to open a file
    # with open('sample.txt', 'r') as file2:
    #     print("Reading file content:")
    #     for line_number, line in enumerate(file2, start=1):
    #         print(f"Line {line_number}: {line.strip()}")

except FileNotFoundError:
        print("Error: The file 'sample.txt' does not exist.")