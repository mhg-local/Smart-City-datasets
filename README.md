# CSV-Modificator
### A brief explanation about each method and its arguments <br/> <br/>

------------------------------------------------------
**createFormattedAddressColumn method :<br/>**
<img src="README_Docs/method call_createFormattedAddressColumn.png" width="250">
<br/>
Calling this classmethod on CSV files which include data referring to a physical location (E.g. "latitude" and "longitude" as the initial data of a location) will add a new column called: "Formatted Address" containing the formatted address of the initial location. An example of this method's function is given below:
<br/> <br/>
initial .CSV file :
<br/>
<img src="README_Docs/geolocation_initialCSV.png" width="400">

final .CSV file :
<br/>
<img src="README_Docs/geolocation_finalCSV.png" width="450">
<br/> 

A SQL database containing initial and formatted addresses of location is created for higher effiency:
<br/>
<img src="README_Docs/SQLAddress.png" width="450">
<br/> 

------------------------------------------------------

**removeRowsThatViolateAllConditions method :<br/>**
<img src="README_Docs/removeRowsThatViolateAllConditions_declaration.png" width="600">
<br/>
Calling this classmethod on CSV files, will filter rows based on the conditions that are given (E.g. "vehicleCount" msut not be 0), for instance in case method depicted in image above is called, rows that their "vehicleCount" value is equal to 0 **and** their "avgSpeed" value is larger than 60 **and** their "sulfure_dioxide" value is larger than 60 will be removed. If rows lack the given headers, related filter will be ignored and other filters will be applied.
<br/> <br/>
initial .CSV file :
<br/>
<img src="README_Docs/removeRowsThatViolateAllConditions_initial_csv.png" width="450">

final .CSV file :
<br/>
<img src="README_Docs/removeRowsThatViolateAllConditions_final_csv.png" width="450">
<br/> 
