import sys
from xml.etree import ElementTree as ET

#New_variable.py <0:XML File> <1:variable_name> <2:Code 1> <3:Code 2> <4:Code 1 Val> <5:Code 2 Val> <6:Code 1 stats> <7:Code 2 stats>

#example:
#New_variable.py "Dummy_CodeBook.xml" Var_Z ON OFF 1 2 234 321

XML_FILE=str(sys.argv[1])

NEW_VAR_NAME=str(sys.argv[2])
NEW_VAR_CODE_1=str(sys.argv[3])
NEW_VAR_CODE_2=str(sys.argv[4])

NEW_VAR_CODE_VALUE_1=str(sys.argv[5])
NEW_VAR_CODE_VALUE_2=str(sys.argv[6])

NEW_VAR_STATISTICS_1_VALUE=str(sys.argv[7])
NEW_VAR_STATISTICS_2_VALUE=str(sys.argv[8])

tree = ET.parse(XML_FILE)
root = tree.getroot()

#new variable to add
New_Variable = ET.Element(NEW_VAR_NAME)
#append the new variable
root.append(New_Variable)

#Variable name contaienr
New_Variable_Name = ET.Element("Name")
New_Variable_Name.text = NEW_VAR_NAME
#append the name container
New_Variable.append(New_Variable_Name)

#Variable Code contaienr
New_Variable_Code = ET.Element("Code")
#append the Code container
New_Variable.append(New_Variable_Code)
#create the statistics containers with the values

#To Do:
#This elements need to be determided dinamically since we dont know how many codes
#a given variable has.
ET.SubElement(New_Variable_Code, NEW_VAR_CODE_1).text=NEW_VAR_CODE_VALUE_1
ET.SubElement(New_Variable_Code, NEW_VAR_CODE_2).text=NEW_VAR_CODE_VALUE_2

#Variable Statistics contaienr
New_Variable_Statistics = ET.Element("Statistics")
#append the statistics container
New_Variable.append(New_Variable_Statistics)
#create the statistics containers with the values

#To Do:
#This elements need to be determided dinamically since we dont know how many statistics
#a given variable has.
ET.SubElement(New_Variable_Statistics, NEW_VAR_CODE_1).text=NEW_VAR_STATISTICS_1_VALUE
ET.SubElement(New_Variable_Statistics, NEW_VAR_CODE_2).text=NEW_VAR_STATISTICS_2_VALUE

#write to the xml
tree.write(XML_FILE)