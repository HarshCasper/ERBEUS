#Python Coding of the ERBEUS Computer Assistant.
#This GUI Application utilizes various modules, packages and APIs to perform various tasks by utilizing various keywords in your input.
#These keywords help it perceive the general intent of the message and perform various tasks accordingly.

from tkinter import *
from tkinter import messagebox as mb
import pyttsx3
import random
from datetime import datetime
import wikipedia
import winshell
from oneliners import get_random
import webbrowser
import os
import pyautogui
import pyperclip
import requests
import ctypes
import time
#*****************************************************************************************************************************

class Widget():
            
    def __init__(self):
        self.win = Tk()
        self.win.geometry('400x350')
        self.win.resizable(0,0)
        self.win.title('PYTHON ASSISTANT')
        self.win.configure(bg='black')
        
        Label(self.win, text='ASSISTANT',font=('times new roman',24),fg='white',width=30,bg='black',bd=5).pack()
        
        Label(self.win, text='YOU' , font=('times new roman',20),fg='white',bg='black').place(x=60,y=50)
        Label(self.win, text='ERBEUS' , font=('times new roman',20),fg='white',bg='black').place(x=260,y=60)

        self.text_box1 = Text(self.win, font=('times new roman',13),width=16,height=5,fg='black', wrap=WORD )
        self.text_box1.place(x=10,y=100)

        self.text_box2 = Text(self.win, font=('times new roman',13),width=15,height=5,fg='black', wrap=WORD)
        self.text_box2.place(x=200,y=100)

        self.search_var = StringVar()

        Entry(self.win, font=('arial black', 14), width=18,textvariable=self.search_var,bd=5).place(x=10,y=250)

        send = Button(self.win, text='Send', font=('times new roman',10),bg='black',fg='white',bd=7,width=10,command=self.send_func).place(x=290,y=250)

        def enter(*args):
            self.send_func()
            
        self.win.bind('<Return>',enter)
        
        self.win.mainloop()
        

        
#*****************************************************************************************************************************
        
    greet = ['Hello. How are you doing?', 'Hi. It is a pleasure to meet you','Hello! I am your Computer Assistant at your service','It is a pleasure to meet you. How may I help you?','Good Day Sir! How are you doing']
    how = ['I am very much fine, Sir. What about you?','Just as fine as before, Sir!', 'Glad that you care about me. I am just as good as the last time we met','Everything is all right. What about you, Master?']
    name = ['My full name is Erbeus Griffin. But you can call me Griffin','My Name is Erbeus Griffin and I am a Computer Assistant which can perform tasks','Its Griffin here and I am a Computer Assistant at your service']
    creator = ['I was coded by Harsh Bardhan Mishra on a Python 3 Platform']
    can = ['I am created to perform Computer activities like doing Google Searches, Wikipedia requests, Weather updates and opening applications and files','I am a Computer assistant designed to perform basic tasks like searches, weather reports and more.']
    c_un = ['Pardon, but I couldnt get what you are saying','Can you please repeat that for me once again','Sorry, but I am having troubles with processing your requests.','can you be please more clear over what you are trying to say?']
    here = ['I am designed to help you with your tasks','I can perform Google Searches, Wikipedia Requests, Weather reporting and more','I am here as your humble assistantfor your service']
    frd = ['I am your friend for life']
    thanks = ['I am humbled','Glad that I can be of some use to you!!','Welcome, Master!']

#*****************************************************************************************************************************
    
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    def printing_func(self, out):
        self.text_box2.delete(1.0,END)
        self.text_box2.insert(INSERT,  out)

    def speak(self,s):
        self.engine.say(s)
        self.engine.runAndWait()

    def send_func(self):
        user_input = self.search_var.get().lower()
        self.search_var.set('')
        self.text_box1.delete(1.0,END)
        self.text_box1.insert(INSERT,user_input)
        

        if 'you' in user_input:                                           
            if 'who' in user_input and 'are' in user_input:
                r = random.randint(0,len(self.name)-1)       
                out = self.name[r]                                            
                self.printing_func(out)                                       
                self.speak(out)
                
            elif 'how are' in user_input:                               
                r = random.randint(0,len(self.how)-1)       
                out = self.how[r]                                            
                self.printing_func(out)                                       
                self.speak(out)                                                      
                                                                                          
            elif 'who made' in user_input:                       
                r = random.randint(0,len(self.creator)-1)       
                out = self.creator[r]                                              
                self.printing_func(out)                                      
                self.speak(out)                                                     
                                                                                         
            elif 'do' in user_input:                                      
                r = random.randint(0,len(self.can)-1 )             
                out = self.can[r]                                                   
                self.printing_func(out)                                       
                self.speak(out)                                                      
                                                                                          
            elif 'name' in user_input:                                
                r = random.randint(0,len(self.name)-1)          
                out = self.name[r]                                                
                self.printing_func(out)                                      
                self.speak(out)                                                     
                                                                                         
            elif 'open' in user_input:                                
                out = 'Opening Youtube'                            
                self.printing_func(out)                                      
                self.speak(out)                                                     
                webbrowser.open('youtube.com')             

            elif 'here' in user_input:
                r = random.randint(0,len(self.here)-1)            
                out = self.here[r]                                                  
                self.printing_func(out)                                       
                self.speak(out)
                
            else:                                                                               
                r = random.randint(0,len(self.c_un)-1)              
                out = self.c_un[r]                                                      
                self.printing_func(out)                                            
                self.speak(out)                                                                

#*****************************************************************************************************************************

        elif 'password' in user_input:
            chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'
            password = ''
            for c in range(15):
                password += random.choice(chars)
            out="Password has been generated. It has been copied to your Clipboard"
            self.printing_func(out)
            self.speak(out)
            pyperclip.copy(password)
            
        elif 'random fact' in user_input or 'fact' in user_input:
            with open("facts.txt", encoding='utf-8') as facts:
                fact_list = facts.read().split('\n')
                i = random.randrange(0, len(fact_list) - 1)
                out=fact_list[i]
                self.printing_func(out)
                self.speak(out)

        elif 'lock' in user_input:
            out="Locking your computer in 5 seconds"
            self.printing_func(out)
            self.speak(out)
            import time
            time.sleep(5)
            ctypes.windll.user32.LockWorkStation()

        elif 'screenshot' in user_input:
            chars='abcdefghijklmnopqrstuvwxyz'
            filename=''
            for i in range(6):
                filename +=random.choice(chars)
            filename=filename+".png"
            pic = pyautogui.screenshot()
            pic.save(filename)
            out='Screenshot has been taken. It has been saved at the Pictures Folder'
            self.printing_func(out)
            self.speak(out)                    
            
        elif 'who' in user_input and 'i' in user_input or 'my' in user_input and 'name' in user_input:
            r = random.randint(0,len(self.me)-1)                                                         
            out = self.me[r]                                                                                                 
            self.printing_func(out)                                                                                    
            self.speak(out)

         
        elif 'thank' in user_input:
            r = random.randint(0,len(self.thanks)-1)                                                         
            out = self.thanks[r]                                                                                                
            self.printing_func(out)                                                                                    
            self.speak(out)

        elif 'recycle bin' in user_input:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
            out="Recycle Bin has been emptied"
            self.printing_func(out)
            self.speak(out)

        elif 'gmail' in user_input:
             out='Opening G-Mail now'
             self.printing_func(out)
             self.speak(out)
             webbrowser.open_new("https://mail.google.com/mail/u/0/#inbox")

        elif 'good morning' in user_input:
            t = datetime.now().strftime('%H  hours and %M minutes')          
            o= t.split()
            if int(o[0]) > 12:
                tt = int(o[0]) - 12
                time = str(tt)+':'+str(o[3]+' PM')
            else:
                time = str(o[0])+':'+str(o[3]+' AM')

            try:     
                url='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Chennai'
                json_data = requests.get(url).json()
                format_add = json_data['weather'][0]['main']
                format_temp = json_data['coord']['lat']
                outa = f'Temperture In Your City is {format_temp} Deegre   Celcius, And  Climate is  {format_add}'                    

            except:
                outa = ' Weather Forcast Is Currently Unavailable'
                
                
            out = f'Good Morning Harsh, The Current Time is {time},  And {outa},    Have A Good Day Sir.'
            self.printing_func(out)
            self.speak(out)
#*****************************************************************************************************************************        

        elif 'can' in user_input and 'friend' in user_input:
            r = random.randint(0,len(self.frd)-1)                                                         
            out = self.frd[r]                                                                                                  
            self.printing_func(out)                                                                                    
            self.speak(out)
            
        elif 'bored' in user_input or 'joke' in user_input or 'jokes' in user_input:
            out = get_random()
            self.printing_func(out)                                                                                    
            self.speak(out)
            
#*****************************************************************************************************************************
            
        elif  'weather' in user_input:
            try:
                if 'in' in user_input:
                    u = user_input.split()
                    for i in range(0,len(u)):
                        if u[i] == 'in':
                            city = u[i+1]
                        
                    api='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
                    url = api+city
                    json_data = requests.get(url).json()
                    format_add = json_data['weather'][0]['main']
                    format_temp = json_data['coord']['lat']
                    out = f'Temperature In {city} is {format_temp} Deegre Celcius, And Climate is {format_add}'
                    self.printing_func(out)
                    self.speak(out)
                    
                else:
                    url='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Chennai'                            
                    json_data = requests.get(url).json()
                    format_add = json_data['weather'][0]['main']
                    format_temp = float((json_data['main']['temp']))/10
                    out = f'Temperture In Your city is {format_temp} Deegre Celcius, And Climate is {format_add}'
                    self.printing_func(out)
                    self.speak(out)
            except:
                out = 'I Was Unable To Connect To Internet.'
                self.printing_func(out)
                self.speak(out)




        
        elif 'where' in user_input and 'i' in user_input or 'location' in user_input:
            try:
                r = requests.get('https://ipinfo.io/')
                d = r.text.split()[4]
                out='You Location Is Near To ' + d
                self.printing_func(out)
                self.speak(out)
            except:
                out='I Was Unable To Track Your Location'
                self.printing_func(out)
                self.speak(out)



        elif 'hello'  in user_input or 'hi' in user_input:
            r = random.randint(0,len(self.greet)-1)              
            out = self.greet[r]                                                  
            self.printing_func(out)
            self.speak(out)

        elif 'exit' in user_input:                                          
            out = 'Okk I am going, Have a good Day sir'  
            self.printing_func(out)                                             
            self.speak(out)                                                             
            self.win.destroy()
            
        elif 'open' in user_input:
            if 'google' in user_input:
                out = 'Opening Google'
                self.printing_func(out)
                self.speak(out)
                webbrowser.open('google.com')

            elif 'youtube' in user_input:
                out = 'Opening Youtube'
                self.printing_func(out)
                self.speak(out)
                webbrowser.open('youtube.com')
                
            elif 'current' in user_input:            
                out='Opening Current Working Directory'                                                     
                self.printing_func(out)
                self.speak(out)
                path = ''
                os.startfile(path)

            elif 'VLC' in user_input:
                out='Opening VLC'
                self.printing_func(out)
                self.speak(out)
                path = 'C:\Program Files\VideoLAN\VLC\vlc.exe'
                os.startfile(path)

            elif 'paint' in user_input:
                out='Opening Paint'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Windows\System32\mspaint.exe'
                os.startfile(path)

            elif 'wordpad' in user_input:
                out='Opening WordPad'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Program Files\Windows NT\Accessories\wordpad.exe'
                os.startfile(path)


            elif 'book' in user_input:
                out='Opening your book'
                self.printing_func(out)
                self.speak(out)
                path = r'file:///F:/Books/Study%20Books/ansi-c-balaguruswamy-c-languagepdf.pdf'
                os.startfile(path)

            elif 'positioner' in user_input:
                out='Opening Positioner'
                self.printing_func(out)
                self.speak(out)
                path = r'E:\positioner.py'
                os.startfile(path)

            elif 'vlc' in user_input:
                out = 'Opening VLC'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Program Files\VideoLAN\VLC\vlc.exe'
                os.startfile(path)


            elif 'browser' in user_input or 'chrome' in user_input:
                out = 'Opening Crome Browser'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
                os.startfile(path)


            elif 'picture' in user_input or 'images' in user_input or 'photo' in user_input:
                out = 'Opening  Images'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Users\My PC\Pictures\Saved Pictures\Defence'
                os.startfile(path)
         

            elif 'cmd' or 'command prompt' in user_input:
                out='Opening Command Prompt'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Windows\System32\cmd.exe'
                os.startfile(path)
                
            else:                                                                                                                    
                r = random.randint(0,len(self.c_un)-1)                                                       
                out = self.c_un[r]                                                                                               
                self.printing_func(out)                                                                                    
                self.speak(out)
                
#*****************************************************************************************************************************
                
        elif 'music' in user_input:
            try:
                out='Playing Music'
                self.printing_func(out)
                self.speak(out)
                mus_dir = r'D:\English Songs'
                songs = os.listdir(mus_dir)
                r = random.randint(0,len(mus_dir) - 1)
                os.startfile(os.path.join(mus_dir,songs[r]))
            except:
                out='Playing Music'
                self.printing_func(out)
                self.speak(out)
                mus_dir = r'D:\Hindi Songs\Hindi Songs\Hindi Songs'
                songs = os.listdir(mus_dir)
                r = random.randint(0,len(mus_dir) - 1)
                os.startfile(os.path.join(mus_dir,songs[r]))
                
        elif 'movie' in user_input:
            out='Playing Movies'
            self.printing_func(out)
            self.speak(out)
            mov_dir = r'E:\Movies'
            songs = os.listdir(mov_dir)
            r = random.randint(0,len(mov_dir) - 2)
            os.startfile(os.path.join(mov_dir,songs[r]))


        elif 'my' in user_input and 'image' in user_input or 'photo' in user_input or 'picture' in user_input:
            out='Opening Photos'
            self.printing_func(out)
            self.speak(out)
            path = r'C:\Users\My PC\Pictures\89.jpg'
            os.startfile(path)

        elif 'get' in user_input and 'lost' in user_input:
            out = 'You Can\'t Talk To Me Like This \n I Am Going.'
            self.printing_func(out)
            self.speak(out)
            self.win.destroy()        

            
            
        elif user_input == '':        
            out = 'You Said Nothing'
            self.printing_func(out)
            self.speak(out)        

        elif 'time' in user_input:                                                                          
            t = datetime.now().strftime('%H  hours and %M minutes')        
            o= t.split()
            if int(o[0]) > 12:
                tt = int(o[0]) - 12
                time = str(tt)+':'+str(o[3]+' PM')
            else:
                time = str(o[0])+':'+str(o[3]+' AM')
            out = 'Current time is : ' + time                                                                   
            self.printing_func(out)                                                                             
            self.speak(out)                                                                                                        

        elif 'wikipedia' in user_input:                                                                    
            i_l = list(user_input.split())                                                                   
            i_l.remove('wikipedia')                                                                         
            to2 = ''.join(i_l)                                                                                          
                                                                        
            try:                                                                                                                
                out = 'According To Wikipedia ' + wikipedia.summary(to2,2)  
                self.printing_func(out)                                                                               
                self.speak(out)                                                                                               
            except:                                                                                                          
                out='cannot find'                                                                                   
                self.printing_func(out)                                                                             
                self.speak(out)                                                                                              

        elif 'fine' in user_input:
            out = 'Great'
            self.printing_func(out)                                                                            
            self.speak(out)


        elif 'shutdown' in user_input:
            out='Shutting Down The System'                                                                                   
            self.printing_func(out)                                                                            
            self.speak(out)
            os.system('shutdown -s')

#*****************************************************************************************************************************
              
        else:                                                                                                                 

                to_search = user_input
                out='I Can Search That On Google, May I?'                                                                                   
                self.printing_func(out)                                                                             
                self.speak(out)

                res = mb.askquestion('Google Search','May I Search That On Google.')

                if res == 'yes':
                    out = 'Opening Google Search'
                    self.printing_func(out)
                    self.speak(out)
                    webbrowser.open('https://www.google.co.in/search?q=' + to_search)
                else:
                    out = 'Ok Sir!!'
                    self.printing_func(out)
                    self.speak(out)

#*****************************************************************************************************************************
                    
if __name__ == '__main__':

    root = Widget()  
    
#Program Ends
