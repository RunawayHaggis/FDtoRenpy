# FDtoRenpy
Convert dialogue from Final Draft screenplay to Renpy format.

The aim is to quickly convert dialogue written in Final Draft to a format suitable for importing to Renpy.

- Actions are converted to narrator dialogue, so "[ACTION]"
- Character dialogue is converted to the format [CHARACTER NAME] "[DIALOGUE]"
- Nothing else is changed, so watch out for 'smart' apostrophes etc.
- Everything else in the screenplay is ignored

Output is to a text file. Copy and paste the text file contents into your Renpy script, then press TAB to indent the text you just pasted.

## TO USE:

`python FDtoRenpy.py YourFinalDraftScript.fdx YourOutputFile.txt`

Ensure there are no spaces in filenames and that the FD script is **not** open in Final Draft.

**Disclaimer: I am not a Python dev!  There are probably much better ways to do this, but this way was quick and it does the job :)**

**Other disclaimer: I have only done very limited testing on this, so be aware.**
