import customtkinter

    
class Punkt(object):
    def __init__(self,x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
    def d_punkt_to_punkt(self, punkt):
        return "{:.4f}".format(((self.x1 - punkt.x1) ** 2 + (self.x2 - punkt.x2) ** 2 + (self.x3 - punkt.x3) ** 2)**0.5)

class Ebene(object):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def d_to_punkt(self, punkt):
        lot_g = Gerade([punkt.x1, punkt.x2, punkt.x3], [self.a, self.b, self.c])
        t = (self.d - self.a * punkt.x1 - self.b * punkt.x2 -self.c * punkt.x3 ) / (self.a ** 2 + self.b ** 2 + self.c ** 2)
        F = Punkt(lot_g.s[0] + lot_g.r[0] * t,lot_g.s[1] + lot_g.r[1] * t, lot_g.s[2] + lot_g.r[2] * t)
        return punkt.d_punkt_to_punkt(F)

class Gerade(object):
    def __init__(self,s, r):
        self.s = s
        self.r = r
    def d_gerade_punkt(self, punkt):
        t = (self.r[0] * (punkt.x1 - self.s[0]) + self.r[1] * (punkt.x2 - self.s[1]) + self.r[2] * (punkt.x3 - self.s[2])) / (self.r[0] ** 2 + self.r[1] ** 2 + self.r[2] ** 2)
        fuspunk = Punkt(self.s[0] + t * self.r[0], self.s[1] + t * self.r[1], self.s[2] + t * self.r[2])
        return fuspunk.d_punkt_to_punkt(punkt)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("der Abstand")
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('dark-blue')
        self.geometry("500x350")
        self.click_button1_flag = False

        def button_callback():
            #print(calculate_answer())
            if not self.click_button1_flag:
                self.answer = customtkinter.CTkLabel(self, text=str(calculate_answer()))
                self.answer.place(x = 225, y = 250)
                self.click_button1_flag = True
            else:
                self.answer.destroy()
                self.answer = customtkinter.CTkLabel(self, text=str(calculate_answer()))
                self.answer.place(x = 225, y = 250)

        # Разместите кнопку в верхней части окна (row=0, column=0)
        self.button = customtkinter.CTkButton(self, text="Rechnen", command=button_callback)
        self.button.place(x = 175, y = 300)

        self.cur_wid = []
        self.cur_wid2 = []
        def combobox_callback1(choice):
            if choice == "Punkt":
                delete_for_all(1)
                create_for_punkt(x_box=70, y_box=20, num_box=1)
            elif choice == 'Ebene':
                delete_for_all(1)
                create_for_ebene(70, 20, 1)
            elif choice == 'Gerade':
                delete_for_all(1)
                create_for_gerade(70, 20, 1)
        def combobox_callback2(choice):
            if choice == "Punkt":
                delete_for_all(2)
                create_for_punkt(x_box=300, y_box=20, num_box=2)
            elif choice == 'Ebene':
                delete_for_all(2)
                create_for_ebene(300, 20, 2)
            elif choice == 'Gerade':
                delete_for_all(2)
                create_for_gerade(300, 20, 2)

        options = ["Punkt", "Gerade", "Ebene"]
        self.combo_box1 = customtkinter.CTkComboBox(self, values=options, command=combobox_callback1)
        self.combo_box2 = customtkinter.CTkComboBox(self, values=options, command=combobox_callback2)
        # Разместите выпадающий список ниже кнопки (row=1, column=0)
        self.combo_box1.place(x = 70, y = 20)
        self.combo_box2.place(x = 300, y = 20)
        def create_for_ebene(x_box, y_box, num_box):
            if num_box == 1:
                self.a_lable1 = customtkinter.CTkLabel(self, width=40, height=20, text="a")
                self.a_lable1.place(x = x_box - 50, y = y_box + 60)
                self.a_ebene1 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.a_ebene1.place(x=x_box - 10, y= y_box + 60)
                self.b_lable1 = customtkinter.CTkLabel(self, width=40, height=20, text="b")
                self.b_lable1.place(x = x_box -50, y = y_box + 100)
                self.b_ebene1 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.b_ebene1.place(x=x_box - 10, y= y_box + 100)
                self.c_lable1 = customtkinter.CTkLabel(self, width=40, height=20, text="c")
                self.c_lable1.place(x = x_box - 50, y = y_box + 140)
                self.c_ebene1 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.c_ebene1.place(x= x_box - 10, y= y_box + 140)
                self.d_lable1 = customtkinter.CTkLabel(self, width=40, height=20, text="d")
                self.d_lable1.place(x = x_box - 50, y = y_box + 180)
                self.d_ebene1 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.d_ebene1.place(x= x_box - 10, y= y_box + 180)
                self.cur_wid.extend([self.a_lable1, self.b_lable1,self.c_lable1,self.d_lable1, self.a_ebene1, self.b_ebene1, self.c_ebene1, self.d_ebene1])
            elif num_box == 2:
                self.a_lable2 = customtkinter.CTkLabel(self, width=20, height=20, text="a")
                self.a_lable2.place(x = x_box - 50, y = y_box + 60)
                self.a_ebene2 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.a_ebene2.place(x=x_box - 10, y= y_box + 60)
                self.b_lable2 = customtkinter.CTkLabel(self, width=20, height=20, text="b")
                self.b_lable2.place(x = x_box -50, y = y_box + 100)
                self.b_ebene2 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.b_ebene2.place(x=x_box - 10, y= y_box + 100)
                self.c_lable2 = customtkinter.CTkLabel(self, width=20, height=20, text="c")
                self.c_lable2.place(x = x_box - 50, y = y_box + 140)
                self.c_ebene2 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.c_ebene2.place(x= x_box - 10, y= y_box + 140)
                self.d_lable2 = customtkinter.CTkLabel(self, width=20, height=20, text="d")
                self.d_lable2.place(x = x_box - 50, y = y_box + 180)
                self.d_ebene2 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.d_ebene2.place(x= x_box - 10, y= y_box + 180)
                self.cur_wid2.extend([self.a_lable2, self.b_lable2,self.c_lable2,self.d_lable2, self.a_ebene2, self.b_ebene2, self.c_ebene2, self.d_ebene2])
        def create_for_punkt(x_box, y_box, num_box):
            if num_box == 1:
                self.x_lable1 = customtkinter.CTkLabel(self, width=20, height=20, text="x")
                self.x_lable1.place(x = x_box - 50, y = y_box + 60)
                self.x_punkt1 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.x_punkt1.place(x=x_box - 10, y= y_box + 60)
                self.y_lable1 = customtkinter.CTkLabel(self, width=20, height=20, text="y")
                self.y_lable1.place(x = x_box -50, y = y_box + 100)
                self.y_punkt1 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.y_punkt1.place(x=x_box - 10, y= y_box + 100)
                self.z_lable1 = customtkinter.CTkLabel(self, width=20, height=20, text="z")
                self.z_lable1.place(x = x_box - 50, y = y_box + 140)
                self.z_punkt1 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.z_punkt1.place(x= x_box - 10, y= y_box + 140)
                self.cur_wid.extend([self.x_lable1, self.y_lable1, self.z_lable1, self.x_punkt1, self.y_punkt1, self.z_punkt1])
            elif num_box == 2:
                self.x_lable2 = customtkinter.CTkLabel(self, width=20, height=20, text="x")
                self.x_lable2.place(x = x_box - 50, y = y_box + 60)
                self.x_punkt2 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.x_punkt2.place(x=x_box - 10, y= y_box + 60)
                self.y_lable2 = customtkinter.CTkLabel(self, width=20, height=20, text="y")
                self.y_lable2.place(x = x_box -50, y = y_box + 100)
                self.y_punkt2 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.y_punkt2.place(x=x_box - 10, y= y_box + 100)
                self.z_lable2 = customtkinter.CTkLabel(self, width=20, height=20, text="z")
                self.z_lable2.place(x = x_box - 50, y = y_box + 140)
                self.z_punkt2 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.z_punkt2.place(x= x_box - 10, y= y_box + 140)
                self.cur_wid2.extend([self.x_lable2, self.y_lable2, self.z_lable2, self.x_punkt2, self.y_punkt2, self.z_punkt2])
        

        def create_for_gerade(x_box, y_box, num_box):
            if num_box == 1:
                self.s_lable1 = customtkinter.CTkLabel(self, width=40, height=20, text="vekt.s")
                self.s_lable1.place(x = x_box - 65, y = y_box + 85)
                self.s1_gerade1 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.s1_gerade1.place(x=x_box - 10, y= y_box + 40)
            
                self.s2_gerade1 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.s2_gerade1.place(x=x_box - 10, y= y_box + 80)
                
                self.s3_gerade1 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.s3_gerade1.place(x= x_box - 10, y= y_box + 120)
                self.r_lable1 = customtkinter.CTkLabel(self, width=40, height=20, text="vekt.r")
                self.r_lable1.place(x = x_box - 65, y = y_box + 205)
                self.r1_gerade1 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.r1_gerade1.place(x= x_box - 10, y= y_box + 160)
                self.r2_gerade1 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.r2_gerade1.place(x= x_box - 10, y= y_box + 200)
                self.r3_gerade1 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.r3_gerade1.place(x= x_box - 10, y= y_box + 240)
                self.cur_wid.extend([self.s_lable1, self.r_lable1, self.s1_gerade1, self.s2_gerade1, self.s2_gerade1, self.s3_gerade1, self.r1_gerade1, self.r2_gerade1, self.r3_gerade1])
            elif num_box == 2:
                self.s_lable2 = customtkinter.CTkLabel(self, width=40, height=20, text="vekt.s")
                self.s_lable2.place(x = x_box - 65, y = y_box + 85)
                self.s1_gerade2 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.s1_gerade2.place(x=x_box - 10, y= y_box + 40)
            
                self.s2_gerade2 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.s2_gerade2.place(x=x_box - 10, y= y_box + 80)
                
                self.s3_gerade2 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.s3_gerade2.place(x= x_box - 10, y= y_box + 120)
                self.r_lable2 = customtkinter.CTkLabel(self, width=40, height=20, text="vekt.r")
                self.r_lable2.place(x = x_box - 65, y = y_box + 205)
                self.r1_gerade2 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.r1_gerade2.place(x= x_box - 10, y= y_box + 160)
                self.r2_gerade2 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.r2_gerade2.place(x= x_box - 10, y= y_box + 200)
                self.r3_gerade2 = customtkinter.CTkTextbox(self, width = 150, height = 20)
                self.r3_gerade2.place(x= x_box - 10, y= y_box + 240)
                self.cur_wid2.extend([self.s_lable2, self.r_lable2, self.s1_gerade2, self.s2_gerade2, self.s2_gerade2, self.s3_gerade2, self.r1_gerade2, self.r2_gerade2, self.r3_gerade2])


        def delete_for_all(num_box):
            if num_box == 1:
                if self.cur_wid:
                    for elem in self.cur_wid:
                        elem.destroy()
            elif num_box == 2:
                if self.cur_wid2:
                    for elem in self.cur_wid2:
                        elem.destroy()
        
        def calculate_answer():
            if self.combo_box1.get() == "Punkt" and self.combo_box2.get() == "Ebene":
                p1 = Punkt(float(self.x_punkt1.get("1.0", "end-1c")), float(self.y_punkt1.get("1.0", "end-1c")), float(self.z_punkt1.get("1.0", "end-1c")))
                e2 = Ebene(float(self.a_ebene2.get("1.0", "end-1c")), float(self.b_ebene2.get("1.0", "end-1c")), float(self.c_ebene2.get("1.0", "end-1c")), int(self.d_ebene2.get("1.0", "end-1c")))
                return e2.d_to_punkt(p1)
            elif self.combo_box1.get() == "Ebene" and self.combo_box2.get() == "Punkt":
                p2 = Punkt(float(self.x_punkt2.get("1.0", "end-1c")), float(self.y_punkt2.get("1.0", "end-1c")), float(self.z_punkt2.get("1.0", "end-1c")))
                e1 = Ebene(float(self.a_ebene1.get("1.0", "end-1c")), float(self.b_ebene1.get("1.0", "end-1c")), float(self.c_ebene1.get("1.0", "end-1c")), int(self.d_ebene1.get("1.0", "end-1c")))
                return e1.d_to_punkt(p2)
            elif self.combo_box1.get() == "Punkt" and self.combo_box2.get() == "Punkt":
                p2 = Punkt(float(self.x_punkt2.get("1.0", "end-1c")), float(self.y_punkt2.get("1.0", "end-1c")), float(self.z_punkt2.get("1.0", "end-1c")))
                p1 = Punkt(float(self.x_punkt1.get("1.0", "end-1c")), float(self.y_punkt1.get("1.0", "end-1c")), float(self.z_punkt1.get("1.0", "end-1c")))
                return p1.d_punkt_to_punkt(p2)
            elif self.combo_box1.get() == "Gerade" and self.combo_box2.get() == "Punkt":
                p2 = Punkt(float(self.x_punkt2.get("1.0", "end-1c")), float(self.y_punkt2.get("1.0", "end-1c")), float(self.z_punkt2.get("1.0", "end-1c")))
                g1 = Gerade([float(self.s1_gerade1.get("1.0", "end-1c")), float(self.s2_gerade1.get("1.0", "end-1c")), float(self.s3_gerade1.get("1.0", "end-1c"))], [float(self.r1_gerade1.get("1.0", "end-1c")), float(self.r2_gerade1.get("1.0", "end-1c")), float(self.r3_gerade1.get("1.0", "end-1c"))])
                return g1.d_gerade_punkt(p2)
            elif self.combo_box1.get() == "Punkt" and self.combo_box2.get() == "Gerade":
                p1 = Punkt(float(self.x_punkt1.get("1.0", "end-1c")), float(self.y_punkt1.get("1.0", "end-1c")), float(self.z_punkt1.get("1.0", "end-1c")))
                g2 = Gerade([float(self.s1_gerade2.get("1.0", "end-1c")), float(self.s2_gerade2.get("1.0", "end-1c")), float(self.s3_gerade2.get("1.0", "end-1c"))], [float(self.r1_gerade2.get("1.0", "end-1c")), float(self.r2_gerade2.get("1.0", "end-1c")), float(self.r3_gerade2.get("1.0", "end-1c"))])

                return g2.d_gerade_punkt(p1)

app = App()
app.mainloop()