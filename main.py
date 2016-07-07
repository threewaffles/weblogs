#import znc #cant import znc since i dont have it installed on my computer
from pathlib import Path
import glob


## znc module to view and search logs via the znc control panel.



logdir = "C:\\Users\\mameman\\AppData\\Roaming\\HexChat"
accountname = "Roaming"

def derp(logdir): # lists all log files in the current directory.
	for filename in Path(logdir).rglob("*.log"):
		print(filename)

if __name__ == "__main__":
	derp(logdir)

