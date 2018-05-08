# FDtoRenpy
Convert dialogue from Final Draft screenplay to Renpy format.

## What is it? 

The aim is to quickly convert dialogue written in Final Draft to a format suitable for importing to Renpy.

- Actions are converted to narrator dialogue, so `"[ACTION]"`
- Character and Dialogue are converted to the format `[CHARACTER] "[DIALOGUE]"`
- Final Draft *General* type is converted to Renpy Label. Spaces are converted to underscores.  So a General of `This is a label` would become `label This_is_a_label:`
- Transition type is converted to scene.  So a transition that reads `bg office` would become `scene bg office` (automatically converted to lower case)
- Single and double curly quotes are changed to straight quotes in the dialogue and action text only.
- Everything else in the screenplay is ignored

Output is to a text file with indents.

## To use:

`python FDtoRenpy.py YourFinalDraftScript.fdx YourOutputFile.txt`

Ensure there are no spaces in filenames and that the FD script is **not** open in Final Draft.

## Potential gotchas:

Final Draft sometimes adds a wiggly line underneath a word it doesn't know.  That formatting appears in the XML too and will affect the conversion, so it's best to get rid of it first. You can usually do that by either confirming the spelling of the word, or just highlighting the whole block and reapplying the style (e.g. transition, dialogue).

## Disclaimers:

I am not a Python dev!  There are probably much better ways to do this, but this way was quick and it does the job :)

Also, please be aware that I have only done very limited testing on this and I am using Final Draft 10.
