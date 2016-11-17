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
        my_sizer.Add(lbl,0,wx.All,5)
        self.txt = wx.TextCtrl(panel,style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt,0,wx.ALL,5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self,event):
        input = self.txt.GetValue()
        input = input.lower()
        try:
            #wolframalpha
            app_id = ""
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            answer = next(res.results).text
            print answer
        except:
            #wikipedia
            print wikipedia.summary(input)
