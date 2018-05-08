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
            file.write('"')
            file.write(stuff.find('Text').text)
            file.write('"')
            file.write('\n')
        elif stuff.attrib['Type'] == "Character":
            file.write(stuff.find('Text').text)
            file.write(" ")
        elif stuff.attrib['Type'] == "Dialogue":
            file.write('"')
            theDialogue = stuff.find('Text').text
            theDialogue = theDialogue.replace('“','"')
            theDialogue = theDialogue.replace('”','"')
            theDialogue = theDialogue.replace("’","'")
            file.write(theDialogue)
            file.write('"')
            file.write('\n')
        
    file.close()

if __name__ == "__main__":
    main();
