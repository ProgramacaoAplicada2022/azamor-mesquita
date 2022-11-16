# tutorial from https://www.youtube.com/watch?v=RtrZcoVD1WM&list=PLqx8fDb-FZDFznZcXb_u_NyiQ7Nai674-
from tkinter import *
import bubbleDriver as bubble

root = Tk()

class Funcs():
    def login(self):
        #print(self.nome_entry.get())
        self.frame_1.destroy()

        #self.widgets_frame2()

        email = "prog.aplic.bubble@gmail.com"
        password = "Um2345678"
        
        bubble.google_signin(email, password)
        bubble.bubbleLogin(email)
        
        self.frames_da_tela()
        self.widgets_select_app()

        
    def go_to_page(self):
        self.frame_1.destroy()
        self.frames_da_tela()
        bubble.driver.get("https://bubble.io/page?name=index&id=apptestpee&tab=tabs-3&subtab=Data+Types&type_id=bhjnmkl")


class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_login()


        #self.select_lista()
        #self.Menus()
        root.mainloop()
    def tela(self):
        self.root.title("BubbleLang")
        self.root.configure(background= '#1e3743')
        self.root.geometry("700x250")
        self.root.resizable(True, True)
        self.root.maxsize(width= 500, height= 700)
        self.root.minsize(width=500, height= 400)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg= '#dfe3ee',
                             highlightbackground= '#759fe6', highlightthickness=3 )
        self.frame_1.place(relx= 0.02, rely=0.02, relwidth= 0.96, relheight= 0.95)

        
    def widgets_login(self):
        ## Criação da label
        self.lb_codigo = Label(self.frame_1, text = "BubbleLang", bg= '#dfe3ee', fg = '#107db2', font=("Courier", 44))
        self.lb_codigo.place(relx= 0.05, rely= 0.05 )

        ## Criação da label e entrada
        self.lb_nome = Label(self.frame_1, text="Email", bg= '#dfe3ee', fg = '#107db2')
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

        ## Criação da label e entrada
        self.lb_nome = Label(self.frame_1, text="Senha", bg= '#dfe3ee', fg = '#107db2')
        self.lb_nome.place(relx=0.05, rely=0.6)

        self.fone_entry = Entry(self.frame_1)
        self.fone_entry.place(relx=0.05, rely=0.7, relwidth=0.8)

        ### Criação do botao
        self.bt_apagar = Button(self.frame_1, text="Login", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.login)
        self.bt_apagar.place(relx=0.35, rely=0.8, relwidth=0.15, relheight=0.05)
        

    def widgets_create_type(self):
        #TODO::::
        ## Criação da label e entrada
        self.lb_nome = Label(self.frame_1, text="App id", bg= '#dfe3ee', fg = '#107db2')
        self.lb_nome.place(relx=0.05, rely=0.05)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.15, relwidth=0.8)

        ### Criação do botao
        self.bt_apagar = Button(self.frame_1, text="Select", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.go_to_page)
        self.bt_apagar.place(relx=0.35, rely=0.5, relwidth=0.15, relheight=0.05)

    def widgets_select_app(self):
        ## Criação da label e entrada
        self.lb_nome = Label(self.frame_1, text="App id", bg= '#dfe3ee', fg = '#107db2')
        self.lb_nome.place(relx=0.05, rely=0.05)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.15, relwidth=0.8)

        ### Criação do botao
        self.bt_apagar = Button(self.frame_1, text="Select", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.go_to_page)
        self.bt_apagar.place(relx=0.35, rely=0.5, relwidth=0.15, relheight=0.05)
        

    def widgets_logging(self):
        ## Criação da label
        self.widgets_logging = Label(self.frame_1, text = "Loading...", bg= '#dfe3ee', fg = '#107db2', font=("Courier", 25))
        self.widgets_logging.place(relx= 0.05, rely= 0.05 )
        
    def widgets_frame2(self):
        ## Criação da label
        self.widgets_frame2 = Label(self.frame_1, text = "Bubble", bg= '#dfe3ee', fg = '#107db2', font=("Courier", 25))
        self.widgets_frame2.place(relx= 0.05, rely= 0.05 )

Application()
