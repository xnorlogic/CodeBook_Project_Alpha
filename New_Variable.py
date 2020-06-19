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
New_Variable = ET.Element("Variable")
#append the new variable
root.append(New_Variable)

#Variable name contaienr
New_Variable_Name = ET.Element("Name")
New_Variable_Name.text = NEW_VAR_NAME
#append the name container
New_Variable.append(New_Variable_Name)

#Variable name contaienr
New_Variable_Note = ET.Element("Note")
New_Variable_Note.text = "This is some Note"
#append the name container
New_Variable.append(New_Variable_Note)

#Variable Code contaienr
New_Variable_Code = ET.Element("Coding")
New_Variable.append(New_Variable_Code)

New_Code = ET.SubElement(New_Variable_Code, "Code")
ET.SubElement(New_Code, "Name").text="ON"
ET.SubElement(New_Code, "Value").text="1"

New_Code = ET.SubElement(New_Variable_Code, "Code")
ET.SubElement(New_Code, "Name").text="OFF"
ET.SubElement(New_Code, "Value").text="2"

#Variable Statistics contaienr
New_Variable_Statistics = ET.Element("Statistics")
#append the statistics container
New_Variable.append(New_Variable_Statistics)

New_Statistic = ET.SubElement(New_Variable_Statistics, "Statistic")
ET.SubElement(New_Statistic, "Name").text="ON"
ET.SubElement(New_Statistic, "Value").text="134"

New_Statistic = ET.SubElement(New_Variable_Statistics, "Statistic")
ET.SubElement(New_Statistic, "Name").text="OFF"
ET.SubElement(New_Statistic, "Value").text="2664"

tree.write(XML_FILE,xml_declaration=True) 
