import csv
import os
import argparse
import sys

def getArgs():
    parser = argparse.ArgumentParser(description='Analyze text file.')

    parser.add_argument(
        '--infile', nargs='?', action='store',
        default=sys.stdin, help='specify input file')

    parser.add_argument(
        '--outfile', nargs='?', action='store',
        default=sys.stdout, help='specify output file')

    args = parser.parse_args()
    return str(args.infile), str(args.outfile)

def main():
    # Get command line arguments, make sure they are valid
    infile, outfile = getArgs()

    while not infile.endswith(".csv"):
        infile = str(input("Enter input file path: "))

    while not outfile.endswith(".txt"):
        outfile = str(input("Enter output file path: "))

    # Read in voter data
    with open(infile, 'r') as csv:
        # Skip first line
        csv.readline()
        csv = csv.read().split()
    
    # Get total number of votes
    totalVotes = len(csv)

    # Build dict of candidates
    candidates = {}

    # Loop through voter data
    for line in csv:
        line = line.split(',')
        cand = line[2]
        # Add candidate if not already in list, otherwise add to vote tally
        if cand not in candidates.keys():
            candidates[cand] = 1
        else:
            candidates[cand] += 1

    results = [
        "Election Results", 
        "-------------------------",
        "Total Votes: {}".format(totalVotes),
        "-------------------------"
    ]
    # Get candidate data and find winner
    mostVotes = 0
    winner = ""
    for c in candidates:
        name = c
        pcnt=(candidates[c]/totalVotes)*100
        numVotes=candidates[c]
        results.append("{}: {:.1f}% ({})".format(c, pcnt, numVotes))
        if numVotes > mostVotes:
            mostVotes = numVotes
            winner = name

    results.extend([
        "-------------------------",
        "Winner: {}".format(winner), 
        "-------------------------"])

    # Print results to stdout
    print("\n".join(results))

    # Write results to output file
    with open(outfile, 'w') as out:
        out.write("\n".join(results))
main()