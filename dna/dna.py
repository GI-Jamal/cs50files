import csv
import sys


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py reference.csv sequences.txt")

    # TODO: Read database file into a variable
    dna = []
    with open(sys.argv[1], "r") as ref_file:
        reader = csv.DictReader(ref_file)
        for person in reader:
            dna.append(person)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as seq_file:
        sequence = seq_file.read()
    subseqs = list(dna[0].keys())[1:]

    # TODO: Find longest match of each STR in DNA sequence
    subseq_length = {}
    for subseq in subseqs:
        subseq_length[subseq] = longest_match(sequence, subseq)

    # TODO: Check database for matching profiles
    for person in dna:
        match = 0
        for subseq in subseqs:
            if int(person[subseq]) == subseq_length[subseq]:
                match += 1
        if match == len(subseqs):
            print(person["name"])
            return
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
