# FDtoRenpy
Convert dialogue from Final Draft screenplay to Renpy format.

## WHAT IS IT? 

The aim is to quickly convert dialogue written in Final Draft to a format suitable for importing to Renpy.

- Actions are converted to narrator dialogue, so `"[ACTION]"`
- Character dialogue is converted to the format `[CHARACTER NAME] "[DIALOGUE]"`
- Final Draft *General* type is converted to Renpy Label. Spaces are converted to underscores.  So a General of `This is a label` would become `label This_is_a_label:`
- Single and double curly quotes are changed to straight quotes in the dialogue and action text only.
- Everything else in the screenplay is ignored

Output is to a text file. Copy and paste the text file contents into your Renpy script, then press TAB to indent the text you just pasted.

## TO USE:

`python FDtoRenpy.py YourFinalDraftScript.fdx YourOutputFile.txt`

Ensure there are no spaces in filenames and that the FD script is **not** open in Final Draft.

## DISCLAIMERS
I am not a Python dev!  There are probably much better ways to do this, but this way was quick and it does the job :)

Also, please be aware that I have only done very limited testing on this and I am using Final Draft 10.
