# -*- coding: utf-8 -*-
import wx
import numpy as np
import matplotlib
import xlrd     #EXCEL文件读取模块
# matplotlib采用WXAgg为后台,将matplotlib嵌入wxPython中
matplotlib.use("WXAgg")
import random
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
from matplotlib.ticker import MultipleLocator, FuncFormatter
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as ticker
import pylab
from matplotlib import pyplot
 
 
######################################################################################
class MPL_Panel_base(wx.Panel):
    ''''' #MPL_Panel_base面板,可以继承或者创建实例'''
 
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=-1)
 
        self.Figure = matplotlib.figure.Figure(figsize=(6, 6.5))
        self.axes = self.Figure.add_axes([0.1, 0.1, 0.8, 0.8])
        self.FigureCanvas = FigureCanvas(self, -1, self.Figure)
 
        self.NavigationToolbar = NavigationToolbar(self.FigureCanvas)
 
        #self.StaticText = wx.StaticText(self, -1, label='Show Help String')
 
        self.SubBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SubBoxSizer.Add(self.NavigationToolbar, proportion=0, border=2, flag=wx.ALL | wx.EXPAND)
        #self.SubBoxSizer.Add(self.StaticText, proportion=-1, border=2, flag=wx.ALL | wx.EXPAND)
 
        self.TopBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.TopBoxSizer.Add(self.SubBoxSizer, proportion=-1, border=2, flag=wx.ALL | wx.EXPAND)
        self.TopBoxSizer.Add(self.FigureCanvas, proportion=-10, border=2, flag=wx.ALL | wx.EXPAND)
 
        self.SetSizer(self.TopBoxSizer)
 
        ###方便调用
        self.pylab = pylab
        self.pl = pylab
        self.pyplot = pyplot
        self.numpy = np
        self.np = np
        self.plt = pyplot
        self.x = np.random.rand(10)
        self.y = np.random.rand(10)
    def UpdatePlot(self):
        '''''#修改图形的任何属性后都必须使用self.UpdatePlot()更新GUI界面 '''
        self.FigureCanvas.draw()
 
    def pyplotPoint(self, *args, **kwargs):
        '''''#最常用的绘图命令plot '''
        #N = 10
        #x = self.np.random.rand(N)
        #y = self.np.random.rand(N)
        #x2 = self.np.random.rand(N)
        #y2 = self.np.random.rand(N)
        #x3 = self.np.random.rand(N)
        #y3 = self.np.random.rand(N)
        #area = self.np.random.rand(N) * 100
        #fig = self.plt.figure()
        #ax = self.plt.subplot()
        #x = np.arange(0.1, 2,0.1)
        x = args[0]

        y = args[1]

        #y = np.sin(x)
        area = self.np.random.rand(len(y)) * 100
        
        self.axes.set_xscale("symlog")
        self.axes.set_yscale("symlog")
        self.xlabel('Pr/nC18')
        self.ylabel('Pr/nC17')
        self.axes.scatter(x, y, marker=args[2],s=area,cmap='green', alpha=0.5)
       
        self.axes.set_xlim(0.1, 100)
        self.axes.set_ylim(0.1, 100)
        #设置坐标轴刻度
        my_x_ticks = np.arange(0.1, 100, 10)
        #对比范围和名称的区别
        #my_x_ticks = np.arange(-5, 2, 0.5)
        my_y_ticks = np.arange(0.1, 100, 3)
        #self.axes.set_xticks(my_x_ticks)
        #self.axes.set_yticks(my_y_ticks)


        #self.axes.get_xaxis().set_major_formatter(MaxNLocator(prune='lower'))
        #self.axes.tick_params(axis='both', which='major', labelsize=8,length=9,direction='in')    # 设置x轴标签大小
        
        #self.axes.yaxis.set_tick_params(right='on',which='both')
        #self.axes.xaxis.set_tick_params(top='on',which='both')
      

        #xt = np.arange(0.1, 100,10)
        #yt = np.arange(0.1, 100,10)
        #self.axes.set_yticks([0.1,1, 10,100], minor=False)
        #self.axes.set_yticklabels([0.1,1, 10,100],minor=True) # turn minor label off
        #self.axes.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
      
        #self.axes.set_xticks([0.1,1, 10], minor=False)
        #self.axes.set_xticklabels([0.1,1, 10],minor=True) # turn minor label off
        #self.axes.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

        #self.axes.get_yaxis(1).set_visible(False)
        #self.axes.get_xaxis(1).set_visible(False)
        #self.axes.set_aspect(1)

        #self.axes.get_yaxis().set_visible(False)
        #self.axes.get_xaxis().set_visible(False)
        #self.axes.set_aspect(1)
           # 设置刻度
        #self.axes.set_yticks(x)
        #self.axes.set_xticks(y.min()*2)
        #xmajorFormatter = FormatStrFormatter('%d') #设置x轴标签文本的格式
        #ymajorFormatter = FormatStrFormatter('%d') #设置y轴标签文本的格式

        self.axes.xaxis.set_major_locator(ticker.MultipleLocator(5))
        #self.axes.xaxis.set_major_formatter(xmajorFormatter)
        self.axes.xaxis.set_minor_locator(ticker.MultipleLocator(1))
        self.axes.yaxis.set_major_locator(ticker.MultipleLocator(5))
        #self.axes.xaxis.set_major_formatter(ymajorFormatter)
        self.axes.yaxis.set_minor_locator(ticker.MultipleLocator(1))

         # 设置网格
        #self.axes.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
        #self.axes.yaxis.grid(True, which='minor')  # y坐标轴的网格使用次刻度
        #self.axes.yaxis.grid(True, which='major')


        #self.axes.get_xaxis().set_major_formatter(
        #    FuncFormatter(lambda x, p: 
        #        '$\mathdefault{10^{%i}}$' % np.log10(1**20)))


        #self.axes.xaxis.set_major_formatter(ticker.ScalarFormatter())
        #self.axes.xaxis.set_minor_formatter(ticker.ScalarFormatter())
        #self.axes.ticklabel_format(style='plain',axis='x',useOffset=False)
        
        #self.axes.scatter(x2, y2, marker='D', s=area, c='green', alpha=0.6)
        #self.axes.scatter(x3, y3,  s=area, c=area, marker='v', cmap='Reds', alpha=0.7)  # 更换标记样式，另一种颜色的样式
        #self.plt.show()
        self.axes.grid(color='g', linestyle='--', linewidth=1,alpha=0.3)
        #self.axes.arrow(0.25, 1.5, 0.3, -0.5, head_width=0.02, head_length=0.1, shape="full",fc='red',ec='red',alpha=0.9, overhang=0.5)
        #self.axes.loglog(x,Roxy,label='Roxy',color='r',linewidth=1) #绘制双对数曲线
        self.axes.plot([0.1,100],[0.1,100])
        self.axes.plot([0.4,100],[0.1,22])
        self.axes.plot([0.1,55],[0.2,100])
        self.axes.plot([0.1,17],[0.8,100])

        #self.plt.tight_layout()
        #self.axes.text(0.5, 66, 'put some text',ha='right',va='baseline')
        #设置lable
        #self.axes.set_xticklabels(x)
        #self.axes.set_yticklabels(y)
        #xticks = self.axes.xaxis.get_major_ticks()
        #xticks[0].label1.set_visible(False)
        #xticks[-1].label1.set_visible(False)
        #self.axes.xaxis.set_major_locator(self.plt.MaxNLocator(10))
        #self.axes.yaxis.set_major_locator(self.plt.MaxNLocator(10))
        self.UpdatePlot()


    def plot(self, *args, **kwargs):
        '''''#最常用的绘图命令plot '''
        self.axes.plot(*args, **kwargs)
        self.UpdatePlot()
 
    def semilogx(self, *args, **kwargs):
        ''''' #对数坐标绘图命令 '''
        self.axes.semilogx(*args, **kwargs)
        self.UpdatePlot()
 
    def semilogy(self, *args, **kwargs):
        ''''' #对数坐标绘图命令 '''
        self.axes.semilogy(*args, **kwargs)
        self.UpdatePlot()
 
    def loglog(self, *args, **kwargs):
        ''''' #对数坐标绘图命令 '''
        self.axes.loglog(*args, **kwargs)
        self.UpdatePlot()
 
    def grid(self, flag=True):
        ''''' ##显示网格  '''
        if flag:
            self.axes.grid()
        else:
            self.axes.grid(False)
 
    def title_MPL(self, TitleString="wxMatPlotLib Example In wxPython"):
        ''''' # 给图像添加一个标题   '''
        self.axes.set_title(TitleString)
 
    def xlabel(self, XabelString="X"):
        ''''' # Add xlabel to the plotting    '''
        self.axes.set_xlabel(XabelString)
 
    def ylabel(self, YabelString="Y"):
        ''''' # Add ylabel to the plotting '''
        self.axes.set_ylabel(YabelString)
 
    def xticker(self, major_ticker=1.0, minor_ticker=0.1):
        ''''' # 设置X轴的刻度大小 '''
        self.axes.xaxis.set_major_locator(MultipleLocator(major_ticker))
        self.axes.xaxis.set_minor_locator(MultipleLocator(minor_ticker))
 
    def yticker(self, major_ticker=1.0, minor_ticker=0.1):
        ''''' # 设置Y轴的刻度大小 '''
        self.axes.yaxis.set_major_locator(MultipleLocator(major_ticker))
        self.axes.yaxis.set_minor_locator(MultipleLocator(minor_ticker))
 
    def legend(self, *args, **kwargs):
        ''''' #图例legend for the plotting  '''
        self.axes.legend(*args, **kwargs)
 
    def xlim(self, x_min, x_max):
        ''' # 设置x轴的显示范围  '''
        self.axes.set_xlim(x_min, x_max)
 
    def ylim(self, y_min, y_max):
        ''' # 设置y轴的显示范围   '''
        self.axes.set_ylim(y_min, y_max)
 
    def savefig(self, *args, **kwargs):
        ''' #保存图形到文件 '''
        self.Figure.savefig(*args, **kwargs)
 
    def cla(self):
        ''' # 再次画图前,必须调用该命令清空原来的图形  '''
        self.axes.clear()
        self.Figure.set_canvas(self.FigureCanvas)
        self.UpdatePlot()
 
    def ShowHelpString(self, HelpString="Show Help String"):
        ''''' #可以用它来显示一些帮助信息,如鼠标位置等 '''
        self.StaticText.SetLabel(HelpString)
 
        ################################################################

 
 
class MPL_Panel(MPL_Panel_base):
    ''''' #MPL_Panel重要面板,可以继承或者创建实例 '''
 
    def __init__(self, parent):
        MPL_Panel_base.__init__(self, parent=parent)
 
        # 测试一下
        self.FirstPlot()
 
 
        # 仅仅用于测试和初始化,意义不大
 
    def FirstPlot(self):
        # self.rc('lines',lw=5,c='r')
        self.cla()
        x = np.arange(-5, 5, 0.25)
        y = np.sin(x)
        self.yticker(0.5, 0.1)
        self.xticker(1.0, 0.2)
        self.xlabel('X')
        self.ylabel('Y')
        self.title_MPL("图像")
        self.grid()
        self.plot(x, y, '--^g')
 
 
        ###############################################################################
 
 
# MPL_Frame添加了MPL_Panel的1个实例
###############################################################################
class MPL_Frame(wx.Frame):
    """MPL_Frame可以继承,并可修改,或者直接使用"""
 
    def __init__(self, title="图形计算器", size=(900, 750)):
        wx.Frame.__init__(self, parent=None, title=title, size=size)
 
        self.MPL = MPL_Panel_base(self)
 
        # 创建FlexGridSizer
        self.FlexGridSizer = wx.FlexGridSizer(rows=9, cols=1, vgap=5, hgap=5)
        self.FlexGridSizer.SetFlexibleDirection(wx.BOTH)
 
        self.RightPanel = wx.Panel(self, -1)
 
        # 测试按钮1
        self.Button1 = wx.Button(self.RightPanel, -1, "刷新", size=(100, 40), pos=(10, 10))
        self.Button1.Bind(wx.EVT_BUTTON, self.Button1Event)
 
        # 测试按钮2
        self.Button2 = wx.Button(self.RightPanel, -1, "Pr/nC17_Ph/nC18图", size=(100, 40), pos=(10, 10))
        self.Button2.Bind(wx.EVT_BUTTON, self.Button2Event)
 

        #  # 测试按钮2
        #self.Button3 = wx.Button(self.RightPanel, -1, "文件", size=(100, 40), pos=(10, 10))
        #self.Button3.Bind(wx.EVT_BUTTON, self.Button3Event)

        # 加入Sizer中
        self.FlexGridSizer.Add(self.Button1, proportion=0, border=5, flag=wx.ALL | wx.EXPAND)
        self.FlexGridSizer.Add(self.Button2, proportion=0, border=5, flag=wx.ALL | wx.EXPAND)
        #self.FlexGridSizer.Add(self.Button3, proportion=0, border=5, flag=wx.ALL | wx.EXPAND)
 
        self.RightPanel.SetSizer(self.FlexGridSizer)
 
        self.BoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.BoxSizer.Add(self.MPL, proportion=-10, border=2, flag=wx.ALL | wx.EXPAND)
        self.BoxSizer.Add(self.RightPanel, proportion=0, border=2, flag=wx.ALL | wx.EXPAND)
 
        self.SetSizer(self.BoxSizer)
 
        # 状态栏
        self.StatusBar()
 
        # MPL_Frame界面居中显示
        self.Centre(wx.BOTH)
 
 
 
        # 按钮事件,用于测试
 
    def Button1Event(self, event):
        self.MPL.cla()  # 必须清理图形,才能显示下一幅图
        type = random.choice ( ['o', '8', 's', 'p', '*'] )
        self.MPL.pyplotPoint(self.x, self.y, type)
        #self.MPL.xticker(2.0, 0.5)
        #self.MPL.yticker(0.5, 0.1)
        #self.MPL.title_MPL("MPL1")
        #self.MPL.ShowHelpString("You Can Show MPL Helpful String Here !")
        #self.MPL.grid()
        #self.MPL.UpdatePlot()  # 必须刷新才能显示


   
    # 打开文件,用于测试
    def Button3Event(self, event):
        def DoOpenFile(self, event):
            wildcard = r"Data files (*.dat)|*.dat|Text files (*.txt)|*.txt|ALL Files (*.*)|*.*"
            open_dlg = wx.FileDialog(self, message='Choose a file', wildcard=wildcard, style=wx.OPEN)
            if open_dlg.ShowModal() == wx.ID_OK:
                path = open_dlg.GetPath()
                try:
                    file = open(path, 'r')
                    text = file.read()
                    file.close()
                except:
                    dlg = wx.MessageDialog(self, 'Error opening file\n')
                    dlg.ShowModal()
 
            open_dlg.Destroy()

        DoOpenFile(self,event)
 
    def Button2Event(self, event):
        with wx.FileDialog(self, "Open XYZ file", wildcard="EXCEL files (*.xls;*.xlsx)|*.xls;*.xlsx",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()

            #self.path_text.SetValue(pathname)
            
            x = []
            y = []

            bk = xlrd.open_workbook(pathname)
            shxrange = range(bk.nsheets)
            for sheetIndex in shxrange:

                try:
                    if sheetIndex>2:
                        sh = bk.sheet_by_index(sheetIndex)
                        ph17 = sh.cell_value(11, 11)
                        ph18 = sh.cell_value(12, 11)
                        x.append(ph17)
                        y.append(ph18)
                except:
                    print("no sheet in %s named Sheet1" % fname)
            ## 获取行数
            #nrows = sh.nrows
            ## 获取列数
            #ncols = sh.ncols
            #print("nrows %d, ncols %d" % (nrows, ncols))
            ## 获取第一行第一列数据
            ## cell_value = sh.cell_value(0, 2)
            ## print(cell_value)

            #part_name = ""
            #part_value = ""

            #part_title = sh.row_values(0)



          

            #for i in part_title:
            #    n = "".join([str(i)," char(20),"]) 
            #    part_name += n

            #part_value = ' values '
            #for i in range(0, nrows):
            #    row_data = sh.row_values(i)
            #    x.append(tuple(row_data)[0])
            #    y.append(tuple(row_data)[1])

            #    #part_value = "".join([part_value, str(tuple(row_data)), ','])
            self.x = x;
            self.y = y;
            self.MPL.cla()  # 必须清理图形,才能显示下一幅图
            self.MPL.pyplotPoint(x, y, 'v')
 
        # 打开文件,用于测试
 
       
 
 
 
        # 自动创建状态栏
 
    def StatusBar(self):
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-2, -2, -1])
 
 
        # About对话框
 
    def AboutDialog(self):
        dlg = wx.MessageDialog(self,
                               '\twxMatPlotLib\t\nMPL_Panel_base,MPL_Panel,MPL_Frame and MPL2_Frame \n Created by Wu Xuping\n Version 1.0.0 \n 2012-02-01',
                               'About MPL_Frame and MPL_Panel', wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
 
        ###############################################################################
 
 
###  MPL2_Frame添加了MPL_Panel的两个实例
###############################################################################
class MPL2_Frame(wx.Frame):
    """MPL2_Frame可以继承,并可修改,或者直接使用"""
 
    def __init__(self, title="MPL2_Frame Example In wxPython", size=(850, 500)):
        wx.Frame.__init__(self, parent=None, title=title, size=size)
 
        self.BoxSizer = wx.BoxSizer(wx.HORIZONTAL)
 
        self.MPL1 = MPL_Panel_base(self)
        self.BoxSizer.Add(self.MPL1, proportion=-1, border=2, flag=wx.ALL | wx.EXPAND)
 
        self.MPL2 = MPL_Panel_base(self)
        self.BoxSizer.Add(self.MPL2, proportion=-1, border=2, flag=wx.ALL | wx.EXPAND)
 
        self.RightPanel = wx.Panel(self, -1)
        self.BoxSizer.Add(self.RightPanel, proportion=0, border=2, flag=wx.ALL | wx.EXPAND)
 
        self.SetSizer(self.BoxSizer)
 
        # 创建FlexGridSizer
        self.FlexGridSizer = wx.FlexGridSizer(rows=9, cols=1, vgap=5, hgap=5)
        self.FlexGridSizer.SetFlexibleDirection(wx.BOTH)
 
        # 测试按钮1
        self.Button1 = wx.Button(self.RightPanel, -1, "TestButton", size=(100, 40), pos=(10, 10))
        self.Button1.Bind(wx.EVT_BUTTON, self.Button1Event)
 
        # 测试按钮2
        self.Button2 = wx.Button(self.RightPanel, -1, "AboutButton", size=(100, 40), pos=(10, 10))
        self.Button2.Bind(wx.EVT_BUTTON, self.Button2Event)
 
        # 加入Sizer中
        self.FlexGridSizer.Add(self.Button1, proportion=0, border=5, flag=wx.ALL | wx.EXPAND)
        self.FlexGridSizer.Add(self.Button2, proportion=0, border=5, flag=wx.ALL | wx.EXPAND)
 
        self.RightPanel.SetSizer(self.FlexGridSizer)
 
        # 状态栏
        self.StatusBar()
 
        # MPL2_Frame界面居中显示
        self.Centre(wx.BOTH)
 
 
 
        # 按钮事件,用于测试
 
    def Button1Event(self, event):
        self.MPL1.cla()  # 必须清理图形,才能显示下一幅图
        x = np.arange(-5, 5, 0.2)
        y = np.cos(x)
        self.MPL1.plot(x, y, '--*g')
        self.MPL1.xticker(2.0, 1.0)
        self.MPL1.yticker(0.5, 0.1)
        self.MPL1.title_MPL("MPL1")
        self.MPL1.ShowHelpString("You Can Show MPL1 Helpful String Here !")
        self.MPL1.grid()
        self.MPL1.UpdatePlot()  # 必须刷新才能显示
 
        self.MPL2.cla()
        self.MPL2.plot(x, np.sin(x), ':^b')
        self.MPL2.xticker(1.0, 0.5)
        self.MPL2.yticker(0.2, 0.1)
        self.MPL2.title_MPL("MPL2")
        self.MPL2.grid()
        self.MPL2.UpdatePlot()
 
    def Button2Event(self, event):
        self.AboutDialog()
 
 
 
        # 自动创建状态栏
 
    def StatusBar(self):
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-2, -2, -1])
 
 
        # About对话框
 
    def AboutDialog(self):
        dlg = wx.MessageDialog(self,
                               '\twxMatPlotLib\t\nMPL_Panel_base,MPL_Panel,MPL_Frame and MPL2_Frame \n Created by Wu Xuping\n Version 1.0.0 \n 2012-02-01',
                               'About MPL_Frame and MPL_Panel', wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
 
 
 
 
        ########################################################################
def main():
    app = wx.App()
    #frame = MPL2_Frame()
    frame = MPL_Frame()
    frame.Center()
    frame.Show()
    app.MainLoop()



main()
# 主程序测试
#if __name__ == '__main__':
#    app = wx.App()
#    #frame = MPL2_Frame()
#    frame = MPL_Frame()
#    frame.Center()
#    frame.Show()
#    app.MainLoop()