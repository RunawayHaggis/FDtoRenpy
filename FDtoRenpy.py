import xml.etree.ElementTree as ET

def main():
    import sys
    try:
        output_file_name = sys.argv[2]
        input_file_name = sys.argv[1]
        file = open(output_file_name,"w")
        tree = ET.parse(input_file_name)
    except:
        print("\n\n***************************************\n\nHOW TO USE: python FDtoRenpy.py YourFinalDraftScript.fdx YourOutputFile.txt\n\nEnsure filenames are all one word (no spaces) and that the FDX file is NOT open in Final Draft.\n\n***************************************\n\n")
        sys.exit(0)

    
    root = tree.getroot()
    for stuff in root.iterfind('Content/Paragraph'):
        
        if stuff.attrib['Type'] == "Action":
            theAction = stuff.find('Text').text
            
            if theAction != None:
                file.write("\t")
                file.write('"')
                theAction = theAction.replace('“','"')
                theAction = theAction.replace('”','"')
                theAction = theAction.replace("’","'")
                file.write(theAction)
                file.write('"')
                file.write('\n')
                
        elif stuff.attrib['Type'] == "General":
            theLabel = stuff.find('Text').text
            if theLabel != None:
                file.write('\n')
                file.write("label ")
                theLabel = theLabel.replace(" ","_")
                theLabel = theLabel.replace("“","")
                theLabel = theLabel.replace("”","")
                theLabel = theLabel.replace("’","")
                file.write(theLabel)
                file.write(":\n")

        elif stuff.attrib['Type'] == "Transition":
            theScene = stuff.find('Text').text
            if theScene != None:
                file.write('\n')
                file.write("\t")
                file.write("scene ")
                theScene = theScene.replace('“','"')
                theScene = theScene.replace('”','"')
                theScene = theScene.replace("’","'")
                file.write(theScene.lower())
                file.write("\n\n")
                
        elif stuff.attrib['Type'] == "Character":
            file.write("\t")
            file.write(stuff.find('Text').text)
            file.write(" ")
            
        elif stuff.attrib['Type'] == "Dialogue": 
            theDialogue = stuff.find('Text').text
            if theDialogue!= None:
                file.write('"')
                theDialogue = theDialogue.replace('“','"')
                theDialogue = theDialogue.replace('”','"')
                theDialogue = theDialogue.replace("’","'")
                file.write(theDialogue)
                file.write('"')
            file.write('\n')
        
    file.close()

if __name__ == "__main__":
    main();
