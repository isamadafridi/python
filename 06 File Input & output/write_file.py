# This program writes three lines of data
# to a file.
def main():
    # Open a file named philosophers.txt.
    outfile = open('append.txt', 'a')

    # Write the names of three philosphers
    # to the file.
    outfile.write('\nJohn Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    # Close the file.
    outfile.close()

    infile = open('append.txt', 'r')

    read_file = infile.read()

    infile.close()

    print(read_file)

# Call the main function.
main()