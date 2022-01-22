import glob
import os

from ReadContent import ReadContent
from RulesAndFilters import RulesAndFilters

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "Files/*")


for file in glob.glob(path):
    if ReadContent.getFileFormat(file) == "txt":
        readContent = ReadContent(file)

for file in glob.glob(path):
    if ReadContent.getFileFormat(file) == "csv":
        print("file is: ", file)

        rulesAndFilters = RulesAndFilters(file)
        rulesAndFilters.removeRowsThatViolateAllConditions([{"header": "vehicleCount", "value": 0, "condition": "not equal"},
                                   {"header": "avgSpeed", "value": 1, "condition": "smaller than"}])

        # rulesAndFilters.removeDuplicateRowsFromCSV()
        # rulesAndFilters.setValueRange("vehicleCount", 0, condition="not equal")
        # rulesAndFilters.setValueRange("avgSpeed", 60, condition="smaller than")
        # rulesAndFilters.checkTypeOfValue("avgSpeed", int)
        # rulesAndFilters.removeInvalidTimeStamps()
        # rulesAndFilters.removeTimeStampsNotDividableBy5()

        readContent = ReadContent(file)

        readContent.createFormattedAddressColumn()

        # readContent.plotFromCSV()
        # print("Avg is : ", readContent.getAvgValueOfColumn("avgMeasuredTime"))
        # print("min is : ", readContent.getMinValueOfColumn("avgSpeed"))
        # print("max is : ", readContent.getMaxValueOfColumn("avgSpeed"))
        # print("first row is : ", readContent.getFirstRow())
        # print("last row is : ", readContent.getLastRow())
        # print("headers are : ", readContent.getHeaders())
        print("number of rows is : ", readContent.getSize(), "\n")

    # ReadContent.plotLineChart("pollutionData158324.csv", "trafficData158324.csv", "carbon_monoxide", "vehicleCount")
