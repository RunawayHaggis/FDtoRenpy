#FDtoRenpy is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License. https://github.com/RunawayHaggis/FDtoRenpy

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

            if hasattr(stuff.find('Text'), 'text'):
                theAction = stuff.find('Text').text
            else:
                theAction=""
                
            if theAction != "":
                file.write("\t")
                file.write('"')
                theAction = theAction.replace('“','"')
                theAction = theAction.replace('”','"')
                theAction = theAction.replace("’","'")
                file.write(theAction)
                file.write('"')
                file.write('\n')
                
        elif stuff.attrib['Type'] == "General":

            if hasattr(stuff.find('Text'), 'text'):
                theLabel = stuff.find('Text').text
            else:
                theLabel=""
            
            if theLabel != "":
                file.write('\n')
                file.write("label ")
                theLabel = theLabel.replace(" ","_")
                theLabel = theLabel.replace("“","")
                theLabel = theLabel.replace("”","")
                theLabel = theLabel.replace("’","")
                file.write(theLabel)
                file.write(":\n\n")

        elif stuff.attrib['Type'] == "Transition":

            if hasattr(stuff.find('Text'), 'text'):
                theScene = stuff.find('Text').text
            else:
                theScene=""
            
            if theScene != "":
                file.write("\t")
                file.write("scene ")
                theScene = theScene.replace('“','"')
                theScene = theScene.replace('”','"')
                theScene = theScene.replace("’","'")
                file.write(theScene.lower())
                file.write("\n\n")
                
        elif stuff.attrib['Type'] == "Character":
            if hasattr(stuff.find('Text'), 'text'):
                theCharacter = stuff.find('Text').text
            else:
                theCharacter=""

            if theCharacter != "":
                file.write("\t")
                file.write(theCharacter)
                file.write(" ")

        elif stuff.attrib['Type'] == "Parenthetical":
            if hasattr(stuff.find('Text'), 'text'):
                theComment = stuff.find('Text').text
            else:
                theComment=""

            if theComment != "":
                file.write("\n")
                file.write("# ")
                theComment = theComment.replace('(','')
                theComment = theComment.replace(')','')
                file.write(theComment)
                file.write("\n")
            
        elif stuff.attrib['Type'] == "Dialogue":
            if hasattr(stuff.find('Text'), 'text'):
                theDialogue = stuff.find('Text').text
            else:
                theDialogue=""
           
            if theDialogue!= "":
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
