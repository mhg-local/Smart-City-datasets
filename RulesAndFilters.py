from ReadContent import ReadContent


class RulesAndFilters(ReadContent):
    def __init__(self, fileAddress):
        super().__init__(fileAddress)

    def setValueRange(self, columnName, value, **kwargs):

        if kwargs.get('condition') == 'not equal':
            self.removeInvalids(columnName, value, 'not equal')
            while self.removeInvalids(columnName, value, 'not equal') != 0 and \
                    self.removeInvalids(columnName, value, 'not equal') is not None:
                self.removeInvalids(columnName, value, 'not equal')
            ReadContent.writeNewCSVFile(self, self.header, self.rows)

        elif kwargs.get('condition') == 'greater than':
            self.removeInvalids(columnName, value, 'greater than')
            while self.removeInvalids(columnName, value, 'greater than') != 0 and \
                    self.removeInvalids(columnName, value, 'greater than') is not None:
                self.removeInvalids(columnName, value, 'greater than')
            ReadContent.writeNewCSVFile(self, self.header, self.rows)

        elif kwargs.get('condition') == 'smaller than':
            self.removeInvalids(columnName, value, 'smaller than')
            while self.removeInvalids(columnName, value, 'smaller than') != 0 and \
                    self.removeInvalids(columnName, value, 'smaller than') is not None:
                self.removeInvalids(columnName, value, 'smaller than')
            ReadContent.writeNewCSVFile(self, self.header, self.rows)

    def removeInvalids(self, columnName, value, condition):
        rowsToBeDeleted = 0
        if columnName in self.header:
            index = self.header.index(columnName)
            for row in self.rows:
                try:
                    int(row[index])
                    if condition == 'smaller than':
                        if int(row[index]) > value:
                            print("Invalid value : ", row)
                            rowsToBeDeleted += 1
                            self.rows.remove(row)
                    elif condition == 'greater than':
                        if int(row[index]) < value:
                            print("Invalid value : ", row)
                            rowsToBeDeleted += 1
                            self.rows.remove(row)
                    elif condition == 'not equal':
                        if int(row[index]) == value:
                            print("Invalid value : ", row)
                            rowsToBeDeleted += 1
                            self.rows.remove(row)
                except:
                    continue
            return rowsToBeDeleted

    def removeDuplicateRowsFromCSV(self):
        newRows = []
        for row in self.rows:
            if row not in newRows:
                newRows.append(row)
            elif row in newRows:
                print("Duplicate Row : ", row)
        self.rows = newRows

        self.writeNewCSVFile(self.header, self.rows)

    def removeInvalidTimeStamps(self):
        for item in self.header:
            if 'timestamp' in item.lower():
                index = self.header.index(item)

                for row in self.rows:
                    if not ReadContent.isValidDate(row[index]):
                        print("Invalid TimeStamp : ", row)
                        self.rows.remove(row)

        ReadContent.writeNewCSVFile(self, self.header, self.rows)

    def checkTypeOfValue(self, columnName, typeOfValue):
        for item in self.header:
            if columnName in item.lower():
                index = self.header.index(item)

                for row in self.rows:
                    if not self.checkTypeOfVariable(row[index], typeOfValue):
                        print("Invalid value type : ", row)
                        self.rows.remove(row)

        ReadContent.writeNewCSVFile(self, self.header, self.rows)

    def removeTimeStampsNotDividableBy5(self):
        for item in self.header:
            if 'timestamp' in item.lower():
                index = self.header.index(item)

                for row in self.rows:
                    if ReadContent.isValidDate(row[index]) and ':' in row[index]:
                        tempList = row[index].split(':')
                        if len(tempList) == 3:
                            if int(tempList[1]) % 5 == 0 and int(tempList[2] == 0):
                                continue
                        elif len(tempList) == 2 and int(tempList[1]) % 5 == 0:
                            continue
                        else:
                            print("Invalid TimeStamp (not dividable by 5): ", row)
                            self.rows.remove(row)

        ReadContent.writeNewCSVFile(self, self.header, self.rows)

    def cleaning(self):
        self.setValueRange("vehicleCount", 0, condition="not equal")
        self.setValueRange("avgSpeed", 60, condition="smaller than")
        self.checkTypeOfValue("avgSpeed", int)
        self.removeInvalidTimeStamps()
        self.removeTimeStampsNotDividableBy5()

    def removeRowsThatViolateAllConditions(self, listOfDesiredFilters):
        conditions = []
        for item in listOfDesiredFilters:
            if item["header"] in self.header:
                conditions.append({"header": item["header"], 'value': item["value"], 'condition': item["condition"]})
        if len(conditions) == 0:
            return

        def removeRows():
            flag = False
            rowsToBeDeleted = 0
            for row in self.rows:
                for condition in conditions:
                    if self.checkRowValidity(row, condition):
                        flag = False
                        break
                    elif not self.checkRowValidity(row, condition):
                        flag = True
                if flag:
                    print("invalid row: ", row)
                    rowsToBeDeleted += 1
                    self.rows.remove(row)
            return rowsToBeDeleted
        while removeRows() != 0 and removeRows() is not None:
            removeRows()
        ReadContent.writeNewCSVFile(self, self.header, self.rows)


    def checkRowValidity(self, row, condition):
        header = condition["header"]
        value = condition["value"]
        conditionStr = condition["condition"]
        index = self.header.index(header)

        if conditionStr == 'smaller than':
            if int(row[index]) > value:
                return False
        elif conditionStr == 'greater than':
            if int(row[index]) < value:
                return False
        elif conditionStr == 'not equal':
            if int(row[index]) == value:
                return False
        return True
