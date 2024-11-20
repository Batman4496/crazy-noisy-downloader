import discord
from discord.ui import Modal, InputText, View

class TimestampModal(Modal):

  def __init__(self, view: View, *children, title, custom_id = None, timeout = None):
    super().__init__(*children, title=title, custom_id=custom_id, timeout=timeout)
    self.view = view

    s = InputText(label="Start Time", placeholder="HH:MM:SS", value=view.start)
    e = InputText(label="End Time", placeholder="HH:MM:SS", value=view.end)
    
    self.add_item(s)
    self.add_item(e)

  async def callback(self, interaction: discord.Interaction):
    await interaction.response.defer()
    s = self.children[0].value
    e = self.children[1].value

    self.view.start = s
    self.view.end = e

    await interaction.message.edit(embed=self.view.generate_embed())