from array import array
import csv
import numpy as np
import os


def readFromCSV() -> dict:
    """
    Read input from file and pass to the parser function
    """
    try:
        dataSet = []
        # Need to update relative path
        currentWorkingPath = os.path.dirname(__file__)
        relativePath = os.path.join(currentWorkingPath, '../data/input.csv')
        with open(relativePath, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                dataSet.append(row)
        return parseInputCsv(dataSet)
    except:
        print('Something went wrong while pulling data from file. Please try again')
        exit()

def parseInputCsv(dataSet:array) -> dict:
    """
    Parses input 2-D array into 1-D arrays corresponding to each column
    @dataSet: 2-D array input data set
    """
    try:
        parsedDataSet = {}
        for i in range(len(dataSet[0])):
            # Create a list for each header
            parsedDataSet[dataSet[0][i]] = []
            for j in range(1, len(dataSet)):
                # Check for '?' in the data as that cannot be parsed into float
                if dataSet[j][i] != '?':
                    parsedDataSet[dataSet[0][i]].append(float(dataSet[j][i]))
                else:
                    parsedDataSet[dataSet[0][i]].append('?')
        return parsedDataSet
    except:
        print('Something went wrong while parsing data for each column. Please try again')
        exit()

def main():
    """
    Main function
    """
    try:
        dataSet = readFromCSV()
    except:
        print('Something went wrong in the main function. Please try again')
        exit()
    
if __name__ == "__main__":
    main()
