import pandas as pd
import xlwt
import wx

def excel2dict(str1):
        df=pd.read_excel("C:\\Users\\eix\\Desktop\\"+str1+".xls")
        r=len(df)
        c=df.columns.size
        d1={}
        for x in range(r):
                for y in range(c):
                        s1=df.iloc[x][y]
                        if  type(s1)!=str:
                                continue
                        if not s1.startswith('A7'):
                                continue
                        if s1 in d1:
                                d1[s1]+=1
                        else:
                                d1[s1]=0
                                d1[s1]+=1
        return d1
        #a7=pd.DataFrame([d1])#another way
        #a7.to_excel(r"tongji.xls",sheet_name='Sheet1')
def dict2excel(d1):
        wb=xlwt.Workbook()
        sht=wb.add_sheet('sheet 1')
        i=0
        for x in d1:
                sht.write(i,0,x)
                sht.write(i,1,d1[x])
                i+=1
        wb.save(r'C:\\Users\\eix\\Desktop\\tongji.xls')

class ExamplePanel(wx.Panel):
        def __init__(self, parent):
                wx.Panel.__init__(self, parent)
                self.quote = wx.StaticText(self, label="put excel files on desktop:", pos=(10, 10))
         
                self.xlsName = wx.TextCtrl(self, pos=(15,30), size=(300,20))
                self.logger = wx.TextCtrl(self, pos=(15,55), size=(320,320), style=wx.TE_MULTILINE | wx.TE_READONLY)
         
                # A button
                self.button =wx.Button(self, label="Count", pos=(360, 105))
                self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)

        def OnClick(self,event):
                str1=self.xlsName.GetValue()
                if str1=="":return 
                dict1=excel2dict(str1)
                dict2excel(dict1)
                for x in dict1:
                        self.logger.AppendText(x+","+str(dict1[x])+"\n")
                self.logger.AppendText("Count result on desktop:tongji.xls")

app = wx.App(False)
frame = wx.Frame(None,title = "My tool", size = (480,420))
panel = ExamplePanel(frame)
frame.Show()
app.MainLoop()
        
