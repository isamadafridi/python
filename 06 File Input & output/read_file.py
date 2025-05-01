# This program reads and displays the contents
# of the philosophers.txt file.
def main():
    # Open a file named philosophers.txt.
    infile = open('philosophers.txt', 'r')
    # print(infile.read)
    # Read the file's contents.
    file_contents1 = infile.readline()
    file_contents2 = infile.readline()
    file_contents3 = infile.readline()


    # Close the file.
    infile.close()

    # Print the data that was read into memory.
    print(file_contents1)
    print(file_contents2)
    print(file_contents3)
# Call the main function.

main()
