FILE_SRC = "file.txt"

def WriteAppend():
    file = open(FILE_SRC, "a") # a option is append
    file.write("hello world\n")
    file.close()

def main():
    WriteAppend()
    WriteAppend()
    WriteAppend()

if __name__ == "__main__":
    main()