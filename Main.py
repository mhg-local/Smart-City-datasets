import glob
import os

from ReadContent import ReadContent
from RulesAndFilters import RulesAndFilters

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "input files/*")

for file in glob.glob(path):
    if ReadContent.getFileFormat(file) == "txt":
        readContent = ReadContent(file)

for file in glob.glob(path):
    if ReadContent.getFileFormat(file) == "csv":
        print("file is: ", file)

        rulesAndFilters = RulesAndFilters(file)

        # rulesAndFilters.removeDuplicateRowsFromCSV()  # To remove duplication
        # rulesAndFilters.setValueRange("vehicleCount", 0, condition="not equal")  # to check validity of the values
        rulesAndFilters.setValueRange("avgSpeed", 60, condition="smaller than")
        rulesAndFilters.checkTypeOfValue("avgSpeed", int)  # to check type of values
        rulesAndFilters.removeInvalidTimeStamps()  # check type and format
        rulesAndFilters.removeTimeStampsNotDividableBy5()   # to formalized th received timestamp

        readContent = ReadContent(file)
        # readContent.plotFromCSV()   # to draw a plot per each CSV


        # print("Avg is : ", readContent.getAvgValueOfColumn("avgMeasuredTime"))
        # print("min is : ", readContent.getMinValueOfColumn("avgSpeed"))
        # print("max is : ", readContent.getMaxValueOfColumn("avgSpeed"))
        print("first row is : ", readContent.getFirstRow())
        print("last row is : ", readContent.getLastRow())
        print("headers are : ", readContent.getHeaders())
        print("number of rows is : ", readContent.getSize(), "\n")

ReadContent.plotLineChart("pollutionData158324.csv", "trafficData158324.csv", "carbon_monoxide", "vehicleCount")