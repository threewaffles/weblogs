#import znc #cant import znc since i dont have it installed on my computer
from pathlib import Path
import glob


# znc module to view and search logs via the znc control panel.
class weblogs():#znc.Module):

	#module_types = [znc.CModInfo.GlobalModule]
	description = "Displays znc server logs via the web admin interface."

				##/home/arrow/.znc/moddata/log/arrow/snoonet/#channel/file.log
				##/home/arrow/.znc/moddata/log/arrow/ - would be the base dir, anything above that would be denied.
	accountname = "arrow"
	baselogdir = "moddata\\log\\%s" %(accountname)

	def GetWebMenuTitle(self):
		return "Web Logs"

	def derp(logdir): # lists all log files in the current directory.
		#/home/arrow/.znc.moddata/log/arrow/snoonet/#channel

		#gets list of networks
		networks = []

		#row = tmpl.AddRow("Networks")
		for filename in Path(logdir).glob("*"):
			if filename.is_dir():
				networks.append(str(filename).split("\\")[-1])
				#row["Network"] = filename


		#get the channels in the networks and puts them into a dict. key: network, data: channels (and PMs) on that network.
		networkchan = {}
		channels = set()
		for network in networks:
			for channel in Path(logdir+"\\"+network).glob("*"):
				if channel.is_dir():
					channels.add(str(channel).split("\\")[-1])
			networkchan[network] = channels.copy()
			channels.clear()

		#using baselogdir/networks/networkchan we can then display and find the logs on the admin page
		for n in networks:
			print(n)
			for c in networkchan[n]:
				print("--%s" % c)





	def OnWebRequest(self, sock, page, tmpl):
		pass
	#list all the files in the current channel/network selected.
	#allow users to click and view said logs
	#allow users to search this channel/network/global logs
	#deny users access to looking at other users logs
	#provide a way to change the log dir for non standard installations

	if __name__ == "__main__":
		derp(baselogdir)