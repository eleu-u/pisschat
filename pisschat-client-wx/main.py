import wx
import back_end

# connect to server
def ask_and_connect_to_server():
	# ip address dialog
    ask_address = wx.TextEntryDialog(None, "enter IP address to connect to (leave blank for localhost:6166)", caption="connect")
    if ask_address.ShowModal() != wx.ID_OK:
        wx.MessageBox("please enter an IP address")
        exit(1)
	
    address = ask_address.GetValue()
    if address == "":
        address = "localhost:6166"
    split_address = address.split(":")
    if len(split_address) < 2:
        wx.MessageBox("invalid IP address")
        exit(1)
    
    # connect to server through IP and port provided
    back_end.connect_server(split_address[0], split_address[1], messages_box)

    # ask for nickname
    ask_name = wx.TextEntryDialog(None, "enter name", caption="set nickname")
    ask_name.ShowModal()
    if ask_name.GetValue() != "":
        back_end.send_message("!set-name " + ask_name.GetValue())
    ask_name.Destroy() # destroying this makes the app close properly

    # destroy the dialog so that the app closes properly
    ask_address.Destroy()

# initialize wx
app = wx.App()
window = wx.Frame(None, title="pisschat-client-wx", size=(600, 400))

# set up widgets globals
input_box = wx.TextCtrl(window, pos=(5,330), size=(400,25), style=wx.TE_PROCESS_ENTER)
character_count_label = wx.StaticText(window, label="1023", pos=(415,330), size=(80,25))
messages_box = wx.TextCtrl(window, pos=(5,5), size=(450,315), style=(wx.TE_MULTILINE|wx.HSCROLL|wx.TE_READONLY))

member_list = wx.TextCtrl(window, pos=(460,5), size=(135,150), style=(wx.TE_MULTILINE|wx.HSCROLL|wx.TE_READONLY))
member_list.AppendText("ele\n")

change_nickname_label = wx.StaticText(window, label="change nickname", pos=(460, 160))
change_nickname_box = wx.TextCtrl(window, pos=(460, 185), size=(125, 25), style=wx.TE_PROCESS_ENTER)

reconnect_button = wx.Button(window, label="reconnect", pos=(460, 220), size=(90, 25))

# bind events
change_nickname_box.Bind(wx.EVT_TEXT_ENTER, lambda x:
    back_end.send_message("!set-name " + change_nickname_box.GetValue())
)

input_box.Bind(wx.EVT_TEXT_ENTER, lambda x:( 
    back_end.send_message(input_box.GetValue()),
    input_box.Clear(),
    character_count_label.SetLabel("1023")
))

input_box.Bind(wx.EVT_TEXT, lambda x:(
    character_count_label.SetLabel(str(1023 - len(input_box.GetValue())))
))

reconnect_button.Bind(wx.EVT_BUTTON, lambda x:(
    back_end.send_message("!q"),
    ask_and_connect_to_server(),
))

# connect
ask_and_connect_to_server()

# start wx loop
window.Show(True)
app.MainLoop()
