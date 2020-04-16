#!/usr/bin/env python
'''
        Author : Jay

        Technical Exercise - Oxford Nanopore

        Metrichor Challenge
        The purpose of this exercise is to create an utility that finds a total of seqlen values in all files matching
        *.data.json pattern that are found in a given folder
'''

import logging
import sys
import os
import json

from optparse import OptionParser

FilePattern = '.data.json'
TextPattern = "seqlen"


def find_files(path='.'):
    pattern = FilePattern
    for root, dirs, files in os.walk(path):
        for name in files:
            if pattern in name:
                yield os.path.join(root, name)


def processline(line):
    data = json.loads(line)
    val = 0
    try:
        val = int(data[TextPattern])
        return val
    except ValueError as err:
        logging.error(err)
        logging.info("Skiping line because of above error.")
        return 0


def process(file=None):
    total = 0
    # check if filename
    if file is None:
        return 0

    try:
        with open(file, mode="r") as fp:
            for line in fp.readlines():
                total += processline(line)
    except Exception as err:
        logging.error(err)
        logging.info("Skiping file because of above error.")
        return 0
    return total


def main():
    # Parse and get all options that we will need
    usage = "Usage: %prog [Options] path #If path not provided defaults to '.' "
    parser = OptionParser(usage)
    # Option for enabling log
    parser.add_option("-v", "--verbose",
                      action="store_true", dest="verbose", default=False,
                      help="Displays all logging.")
    # Option for disabling log
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose",
                      help="Dose not displays any logging.")
    # Option for log filename log
    parser.add_option("-f", "--filename",
                      help="write logs output to FILE.")

    # Parse options and arguments
    (options, args) = parser.parse_args()

    print(options, args, sys.argv)
    # Check if logging enabled or not
    if options.verbose:
        level = logging.INFO
    else:
        level = logging.WARNING
    # Configure logging
    logging.basicConfig(filename=options.filename,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        level=level)

    total = 0
    # Check if path is provided else default to '.'
    path = '.'
    if len(args) > 0:
        path = args[0]
    # Find and processes all the files in path one by one.
    for file in find_files(path):
        logging.info("Processing file {}".format(file))
        subTotal = process(file)
        total += subTotal
        logging.info("Total for file: {} is {}".format(file, subTotal))
        logging.info("Total : {}".format(total))

    if not options.verbose: print(total)


if __name__ == "__main__":
    main()
