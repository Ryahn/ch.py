import ch
import random

class Test(ch.RoomConnection):
	def onConnect(self):
		print("Connected")
		self.enableBg()
		self.enableRecording()
		self.setNameColor("F9F")
		self.setFontColor("F33")
		self.setFontFace("1")
		self.setFontSize(10)
	
	def onReconnect(self):
		print("Reconnected")
	
	def onDisconnect(self):
		print("Disconnected")
	
	def onMessage(self, user, message):
		if self.getLevel(self.user) > 0:
			print(user.name, message.ip, message.body)
		else:
			print(user.name, message.body)
		if self.user == user: return
		if message.body[0] == "!":
			data = message.body[1:].split(" ", 1)
			if len(data) > 1:
				cmd, args = data[0], data[1]
			else:
				cmd, args = data[0], ""
			if   cmd == "delay":
				self.setTimeout(int(args), self.message, ":D")
			elif cmd == "randomuser":
				self.message(random.choice(self.usernames))
			elif cmd == "ival":
				self.setInterval(int(args), self.message, ":D")
			elif cmd == "mylvl":
				self.message("Your mod level: %i" %(self.getLevel(user)))
			elif cmd == "mods":
				self.message(", ".join(self.modnames + [self.ownername]))
			elif cmd == "ismod":
				user = ch.User(args)
				if self.getLevel(user) > 0:
					self.message("yes")
				else:
					self.message("no")
	
	def onFloodWarning(self):
		self.reconnect()
	
	def onJoin(self, user):
		self.message("hello, " + user.name + "!")
	
	def onLeave(self, user):
		self.message("bye, " + user.name + "!")
	
	def onUserCountChange(self):
		print("users: " + str(self.usercount))
	
	def onMessageDelete(self, user, msg):
		self.message("a message got deleted! " + user.name + ": " + msg.body)

if __name__ == "__main__": Test.easy_start()
