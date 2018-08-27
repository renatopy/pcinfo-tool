import wx
import uuid
import socket
import wmi
import json
import os
import platform

def get_mac_address(): 
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
    rstr="-".join([mac[e:e+2] for e in range(0,11,2)])
    return rstr.upper()

class PCHardwork(object):
    global s
    s=wmi.WMI()
    def get_disk_info(self):
        disk = []
        for pd in s.Win32_DiskDrive():#much diskdrive information
            disk.append(
                {
                "SerialNumber": s.Win32_PhysicalMedia()[0].SerialNumber.lstrip().rstrip(),
                "Caption": pd.Caption,
                "Size": str(int(float(pd.Size)/1024/1024/1024))+"G"
                }
                       )
  
        return disk
    def get_sys_info(self):
        pstr=''
        for ps in s.Win32_OperatingSystem():#much system information
            pstr=ps.InstallDate #only get installdate
            #print("InstallDate:"+pstr[0:8])
            return(pstr[0:8])

class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.quote = wx.StaticText(self, label="Computer Information:", pos=(10, 10))
 
        self.logger = wx.TextCtrl(self, pos=(15,30), size=(330,320), style=wx.TE_MULTILINE | wx.TE_READONLY)
 
        # A button
        self.button =wx.Button(self, label="Read", pos=(360, 105))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        
    def OnClick(self,event):
        myname=socket.getfqdn(socket.gethostname())
        myaddr=socket.gethostbyname(myname)
        PCinfo = PCHardwork()
        num=0
        for info in PCinfo.get_disk_info():
            num=num+1
            self.logger.AppendText("Disk"+str(num)+":"+str(info)+"\n")
        self.logger.AppendText("InstallDate:"+PCinfo.get_sys_info())
        self.logger.AppendText("\nOS:"+platform.platform())
        self.logger.AppendText("\nMachine:"+platform.machine())
        self.logger.AppendText("\nUser:"+myname)
        self.logger.AppendText("\nLAN IP:"+myaddr)
        self.logger.AppendText("\nMAC:"+get_mac_address())

app = wx.App(False)
frame = wx.Frame(None,title = "My tool", size = (480,400))
panel = ExamplePanel(frame)
frame.Show()
app.MainLoop()
