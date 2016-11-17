import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,
            pos = DefaultPosition, size=wx.Size(450,100),
            style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
            wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title = "VA")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label = "Hello I am VA. How can i help you?")
