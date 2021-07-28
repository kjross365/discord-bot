from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase

PREFIX = "+"
OWNER_ID = [511565586656919593]


class Bot(BotBase):
	def __init__(self):
		self.PREFIX = PREFIX
		self.ready = False
		self.guild = None
		self.scheduler = AsyncIOScheduler()

		super().__init__(command_prefix=PREFIX, owner_ids=OWNDER_IDS)

		def run(self, version):
			self.VERSION = version

			with open (".lib/bot/token", "r", encoding="utf-8") as tf:
				self.TOKEN = tf.read()

				print("running bot...")
				super().run(self.TOKEN, reconnect=true)

		async def on_connect(self):
			print("bot connected")

		async def on_disconnect(self):
			print("bot disconnected")

		async def on_ready(self):
			if not self.ready:
				self.ready = True
				self.guilt = self.get_guild(870050006323834880)
				print("bot ready")
				

		async def on_message(self, message):
			pass

bot = Bot()




		
