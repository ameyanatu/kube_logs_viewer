import wx


class Viewer(wx.Frame):

    def __init__(self, parent, title):
        super(Viewer, self).__init__(parent, title=title, size=(1000, 1000))

        self.Centre()


def main():

    app = wx.App()
    ex = Viewer(None, title='Kube Logs Viewer')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()