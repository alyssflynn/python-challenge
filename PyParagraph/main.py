import os
import csv
import sys
import argparse

p1 = os.path.join("raw_data", "paragraph_1.txt")
p2 = os.path.join("raw_data", "paragraph_2.txt")

parser = argparse.ArgumentParser(description='Analyze text file.')

parser.add_argument(
    '--infile', nargs='?', action='store',
    default=sys.stdin, help='specify input file')

parser.add_argument(
    '--outfile', nargs='?', action='store',
    default=sys.stdout, help='specify output file')

def clean(paragraph):
    cleantxt = ""
    for char in paragraph:
        if char.isalpha() or (char==" ") or (char=="."):
            cleantxt = cleantxt + char
    return cleantxt

def main():
    # Parse args from command line
    args = parser.parse_args()
    # print(args)
    # print(args.infile, type(args.infile)) 
    # print(args.outfile, type(args.outfile))
    
    infile = str(args.infile)
    outfile = str(args.outfile)

    # Ask for filename as input/output if file not specified
    if not infile.endswith('.txt'):
        infile = str(input("Enter input file path: "))
    if not outfile.endswith('.txt'):
        outfile = str(input("Enter output file path"))


    # Read in files
    with open(infile, 'r') as paragraph:
        # print(paragraph)
        paragraph = paragraph.read()

        # Remove extraneous punctuation before analysis
        txt = clean(paragraph)

        # Get sentence count
        sentList = txt.split(".")
        numSentences = len(sentList) - 1

        #  Get word count
        txt = txt.replace(".", " ")
        wordList = txt.split()
        numWords = len(wordList)

        # Get average sentence length (in words)
        # re.split("(?&lt;=[.!?]) +", paragraph)
        avgSentLen = numWords / numSentences

        # Get average letter count (per word)
        txt = txt.replace(" ", "")
        numLetters = len(txt)
        avgLetters = numLetters / numWords


    results = (
        "Paragraph Analysis",
        "-----------------",
        "Approximate Word Count: {}".format(numWords),
        "Approximate Sentence Count: {}".format(numSentences),
        "Average Letter Count: {}".format(avgLetters),
        "Average Sentence Length: {}".format(avgSentLen)
    )

    # Print results to stdout
    print("\n".join(results))

    # Write results to output file
    with open(outfile, 'w') as out:
        out.write("\n".join(results))


main()