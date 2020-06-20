# Auto-pastebin
Desktop application for instant code snippet sharing

# Screenshot
![Screenshot_2](https://user-images.githubusercontent.com/24731446/85190497-dedf1d00-b2da-11ea-8e40-4b18e831496d.png)


# Requirements 
  
  python 3
  PyQt5
  
  pyperclip ( pyperclip is required for copying the returned url to clipboard )
  more info https://pypi.org/project/pyperclip/
 
 
# Usage

## GUI     
      You can open a file and edit it in the codebox before pasting it.
      or 
      You can paste something in the codebox without even opening any file .
      
 
## CLI

  python3 auto_pastebin.py "path to your file" "an optional username"
  
  
  ex:
  
    $ python3 auto_pastebin.py uva900.cpp shakil
    > https://pastebin.ubuntu.com/XXXX
    
    or 
    
    $ python3 auto_pastebin.py uva900.cpp 
    > https://pastebin.ubuntu.com/XXXX (this will take the username of your pc account)
    
    
 
