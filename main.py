#import znc #cant import znc since i dont have it installed on my computer
from pathlib import Path
import glob


# znc module to view and search logs via the znc control panel.
class weblogs():#znc.Module):

	#module_types = [znc.CModInfo.GlobalModule]
    description = "Displays znc server logs via the web admin interface."

				##/home/arrow/.znc.moddata/log/arrow/snoonet/#channel/file.log
				##/home/arrow/.znc.moddata/log/arrow/ - would be the base dir, anything above that would be denied.
	baselogdir = "C:\\Users\\mameman\\AppData\\Roaming\\HexChat\\logs"
	accountname = "Roaming"

	def GetWebMenuTitle(self):
		return "Web Logs"


	def derp(logdir): # lists all log files in the current directory.
		#/home/arrow/.znc.moddata/log/arrow/snoonet/#channel
		for filename in Path(logdir).glob("*.log"):
			print(filename)

	def OnWebRequest(self, sock, page, tmpl):
	#list all the files in the current channel/network selected.
	#allow users to click and view said logs
	#allow users to search this channel/network/global logs
	#deny users access to looking at other users logs
	#provide a way to change the log dir for non standard installations

	if __name__ == "__main__":
		derp(baselogdir)

