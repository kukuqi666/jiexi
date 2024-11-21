import tkinter as tk
from tkinter.messagebox import showerror
import webbrowser
import re
from urllib import parse

class APP:
    # 初始化应用程序窗口
    def __init__(self, width=1200, height=600):
        self.w = width
        self.h = height
        self.title = 'VIP视频解析'
        self.root = tk.Tk(className=self.title)
        self.url = tk.StringVar()
        self.v = tk.IntVar()
        
        self.v.set(1)
        
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)
        frame_3 = tk.Frame(self.root)
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        moviemenu = tk.Menu(menu, tearoff=0)
        
        menu.add_cascade(label='点我选择视频播放网站', menu=moviemenu)
        moviemenu.add_command(label='腾讯视频', command=lambda: webbrowser.open('http://v.qq.com/'))
        moviemenu.add_command(label='搜狐视频', command=lambda: webbrowser.open('http://tv.sohu.com/'))
        moviemenu.add_command(label='芒果TV', command=lambda: webbrowser.open('http://www.mgtv.com/'))
        moviemenu.add_command(label='爱奇艺', command=lambda: webbrowser.open('http://www.iqiyi.com/'))
        moviemenu.add_command(label='PPTV', command=lambda: webbrowser.open('http://www.bilibili.com/'))
        moviemenu.add_command(label='优酷', command=lambda: webbrowser.open('http://www.youku.com/'))
        moviemenu.add_command(label='乐视', command=lambda: webbrowser.open('http://www.le.com/'))
        moviemenu.add_command(label='土豆', command=lambda: webbrowser.open('http://www.tudou.com/'))
        moviemenu.add_command(label='A站', command=lambda: webbrowser.open('http://www.acfun.tv/'))
        moviemenu.add_command(label='B站', command=lambda: webbrowser.open('http://www.bilibili.com/'))
        
        
        group = tk.Label(frame_1, text='请选择一个视频播放通道：', padx=20, pady=20, font=('楷体', 20))
        tb1 = tk.Radiobutton(frame_1, text='通道一', variable=self.v, value=1, width=15, height=3, font=('楷体', 18))
        tb2 = tk.Radiobutton(frame_1, text='通道二', variable=self.v, value=2, width=15, height=3, font=('楷体', 18))
        tb3 = tk.Radiobutton(frame_1, text='通道三', variable=self.v, value=3, width=15, height=3, font=('楷体', 18))
        tb4 = tk.Radiobutton(frame_1, text='通道四', variable=self.v, value=4, width=15, height=3, font=('楷体', 18))
        
        label1 = tk.Label(frame_2, text='请输入视频链接：', font=('楷体', 20))
        entry = tk.Entry(frame_2, textvariable=self.url, highlightcolor='Fuchsia', highlightthickness=1, width=50, font=('楷体', 20))
        label2 = tk.Label(frame_2, text=' ')
        play = tk.Button(frame_2, text='播放', font=('楷体', 16), fg='Purple', width=3, height=1, command=self.video_play)
        label3 = tk.Label(frame_2, text=' ')
        label_explain = tk.Label(frame_3, fg='red', font=('楷体', 20), text='\n注意：支持大部分主流视频网站的视频播放！\n此解析脚本仅供由琪大大提供，请勿用于任何商业用途！')
        label_warning = tk.Label(frame_3, fg='blue', font=('楷体', 20), text='\n建议：将Chrome内核浏览器设置为默认浏览器')
        lable_social = tk.Label(frame_3, fg='orange', font=('楷体', 20), text='\n联系方式：QID：wnfng66\nWeChat:kukuqi6666')
        
        
        frame_1.pack()
        frame_2.pack()
        frame_3.pack()
        group.grid(row=0, column=0)
        tb1.grid(row=0, column=1)
        tb2.grid(row=0, column=2)
        tb3.grid(row=0, column=3)
        tb4.grid(row=0, column=4)
        label1.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        label2.grid(row=0, column=2)
        play.grid(row=0, column=3, ipadx=20, ipady=20)
        label3.grid(row=0, column=4)
        label_explain.grid(row=1, column=0)
        label_warning.grid(row=2, column=0)
        lable_social.grid(row=3, column=0)

    # 播放视频的方法
    def video_play(self):
        port_1 = 'https://jx.m3u8.tv/jiexi/?url='
        port_2 = 'https://www.ckplayer.vip/jiexi/?url='
        port_3 = 'https://jx.playerjy.com/?url='
        port_4 = 'https://jx.xmflv.com/?url='
        if re.match('^https?:/{2}\\w.+$', self.url.get()):
            if self.v.get() == 1:
                ip = self.url.get()
                ip = parse.quote_plus(ip)
                webbrowser.open(port_1 + ip)
                return None
            elif self.v.get() == 2:
                ip = self.url.get()
                ip = parse.quote_plus(ip)
                webbrowser.open(port_2 + ip)
                return None
            
            elif self.v.get() == 3:
                ip = self.url.get()
                ip = parse.quote_plus(ip)
                webbrowser.open(port_3 + ip)
                return None
                
            elif self.v.get() == 4:
                ip = self.url.get()
                ip = parse.quote_plus(ip)
                get_url = 'https://jx.xmflv.com/?url=%s' % ip
                webbrowser.open(get_url)
            else:
               showerror(title='错误', message='视频链接地址无效，请重新输入！')

    # 将窗口居中的方法
    def center(self):
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = int(ws / 2 - self.w / 2)
        y = int(hs / 2 - self.h / 2)
        self.root.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))

    # 启动应用程序主循环的方法
    def loop(self):
        self.root.resizable(False, False)
        self.center()
        self.root.mainloop()

if __name__ == '__main__':
    app = APP()
    app.loop()