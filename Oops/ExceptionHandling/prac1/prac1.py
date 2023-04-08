def readFile(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")

readFile('/home/ram/Python/Oops/ExceptionHandling/prac1/1.txt')
readFile('/home/ram/Python/Oops/ExceptionHandling/prac1/2.txt')
readFile('/home/ram/Python/Oops/ExceptionHandling/prac1/3.txt')