from tkinter import *
window = Tk()
globalweight = 0

# vytvoření tlačítek pro výběr zvířete 
def create_button(name, animal):
    return Button(frame1, text=f"{name}",  command=lambda: set_slider(animal), bg = "#008587", fg = "#edffff", activebackground="#007476" )

# nastavení šoupátek na rozmezí minimální a maximální doporučené hodnoty tří anestetik v mg/kg podle druhu vybraného zvířete
def set_slider(animal):
    s_ket.configure(from_=ketamine_min_dose_dict[animal], to=ketamine_max_dose_dict[animal], tickinterval=ketamine_min_dose_dict[animal])
    s_med.configure(from_=medetomidin_min_dose_dict[animal], to=medetomidin_max_dose_dict[animal], tickinterval=medetomidin_min_dose_dict[animal])
    s_mid.configure(from_=midazolam_min_dose_dict[animal], to=midazolam_max_dose_dict[animal], tickinterval=midazolam_min_dose_dict[animal])


# nastavení globální proměnné - pro uložení vepsané hmotnosti pacienta a následné využití v dalších funkcích
def save_weight(): 
    global globalweight
    weight = int(e_weight.get())
    
    globalweight = weight
    print(globalweight)
    
# výpočet dávky anestetik podle zadané hmotnosti pacienta a ručně nastavených hodnot na šoupátcích
def count_dose():
    ket_drug = value_inside_ket.get()
    ket_davka = s_ket.get()

    ket_final = round(globalweight * 0.001 * ket_davka /ketamine_drug_dict[ket_drug], 2)
            
    med_drug = value_inside_med.get()
    med_davka = s_med.get()

    med_final = round(globalweight * 0.001 * med_davka /medetomidine_drug_dict[med_drug], 2)
           
    mid_drug = value_inside_mid.get()
    mid_davka = s_mid.get()

    mid_final = round(globalweight * 0.001 * mid_davka /midazolam_drug_dict[mid_drug], 2)
    
    result_label_ket.config(text = f"{ket_final} ml {ket_drug} ")
    
    result_label_med.config (text = f" {med_final} ml {med_drug} ")
    
    result_label_mid.config(text = f"{mid_final} ml {mid_drug} ")
    


ketamine_min_dose_dict = {
    "rabbit": 5,
    "ferret": 3,
    "guineapig": 10,
    "chinchilla": 5,
    "rat": 3,
    }

ketamine_max_dose_dict = {
    "rabbit": 15,
    "ferret": 6,
    "guineapig": 15,
    "chinchilla": 10,
    "rat": 10,
    }

medetomidin_max_dose_dict = {
    "rabbit": 0.15,
    "ferret": 0.03,
    "guineapig": 0.18,
    "chinchilla": 0.06,
    "rat": 0.15,
    }

medetomidin_min_dose_dict = {
    "rabbit": 0.04,
    "ferret": 0.02,
    "guineapig": 0.08,
    "chinchilla": 0.02,
    "rat": 0.08,
    }

midazolam_min_dose_dict = {
    "rabbit": 0.3,
    "ferret": 0.1,
    "guineapig": 0.3,
    "chinchilla": 0.15,
    "rat": 0.3,
    }

midazolam_max_dose_dict = {
    "rabbit": 0.4,
    "ferret": 0.2,
    "guineapig": 0.5,
    "chinchilla": 0.25,
    "rat": 0.5,
    }

ketamine_drug_dict = {
    "Anaestamine": 100,
    "Ketabel" : 100,
    "Ketamidor" : 100, 
    "Kettex" : 100,
    "Narkamon 50" : 50,
    "Narkamon 100" : 100,
    }

medetomidine_drug_dict = {
    "Cepetor" : 1,
    "Dorbene" : 1,
    "Sedator" : 1,
    }

midazolam_drug_dict = {
    "Dormicum" : 5,
    "Midazolam Accord 1" : 1,
    "Midazolam Accord 5" : 5,
    "Midazolam Kalceks" : 5,
    }

window.title ("Anesteziologická kalkulačka pro drobné savce")
window.minsize(200, 150)
window.resizable(False, False)
window.iconbitmap("kralik.ico")
window.config (bg="#76fdff", padx=20, pady=20, )

frame1 = Frame (window, bg="#76fdff")
frame1.grid(row=0, column=0)

frame2 = Frame (window, bg="#76fdff")
frame2.grid(row=1, column=0)

label_animal = Label(frame1, text="Vyber druh zvířete: ", bg = "#76fdff", fg="#002021")
label_animal.grid(ipadx=10, ipady=5, pady=10, row=0, columnspan=5)

animals = {
    "rabbit" : "kralík", 
    "ferret": "fretka",
    "guineapig" : "morče", 
    "chinchilla" : "činčila", 
    "rat" : "potkan",
}

# cyklus pro vytvoření tlačítek se zvířaty
for i, (animal_key, animal_value) in enumerate (animals.items()):
    btn_animal = create_button(animal_value, animal_key)
    
    btn_animal.grid(ipadx=10, padx = 10, ipady=5, pady=10, row=1,  column = i)

# šoupátko - dávka ketaminu
l_ket = Label(frame2, text = "Nastav dávku ketaminu:", bg = "#dcfeff", fg="#002021")
l_ket.grid(ipadx=10,  ipady=5, pady=10, row=0, column=0, sticky=W)

s_ket =Scale( frame2, label ="Dávka ketaminu v mg/kg",  resolution=0.01, width = "30", length = "200", bg ="#dcfeff", fg ="#002021", orient = "horizontal")
s_ket.grid(ipadx=10, row=1, column=0, sticky=W)

# šoupátko - dávka medetomidinu
l_med = Label( frame2, text = "Nastav dávku medetomidinu:", bg = "#feffff", fg="#002021")
l_med.grid(ipadx=10,  ipady=5, pady=10, row=0, column=1, sticky=W)

s_med = Scale(frame2, label ="Dávka medetomidinu v mg/kg", resolution=0.001, width = "30", length = "200", bg ="#feffff", fg ="#002021", orient = "horizontal")
s_med.grid(ipadx=10, row=1, column=1, sticky=W)

# šoupátko - dávka midazolamu
l_mid = Label(frame2, text = "Nastav dávku midazolamu:", bg = "#00d9dc", fg="#002021")
l_mid.grid(ipadx=10,  ipady=5, pady=10, row=0, column=2, sticky=W)

s_mid = Scale(frame2,  label ="Dávka midazolamu v mg/kg", resolution=0.001, width = "30", length = "200", bg ="#00d9dc", fg ="#002021", orient = "horizontal")
s_mid.grid(ipadx=10, row=1, column=2, sticky=W)

# zadání hmotnosti pacienta
l_weight = Label(frame2, text = "Zadej hmotnost pacienta v gramech: ", bg = "#76fdff", fg="#002021")
l_weight.grid(ipadx=10, ipady=5, pady=10, row=2, column=0, sticky=W)

e_weight = Entry (frame2, width= 10)
e_weight.focus_set( )
e_weight.grid(row=2, column=1,sticky=W)

# tlačítko pro uložení hmotnosti zvířete
count_dose_patient_button = Button(frame2, text='Ulož hmotnost pacienta', command=save_weight, bg ="#008587", fg ="#edffff", activebackground="#007476")
count_dose_patient_button.grid(ipadx=10, ipady=5, pady=10, row=2,column=2, sticky=W)

#výběr přípravků
label_option = Label(master=frame2, text="Vyber přípravky: ", bg = "#76fdff", fg="#002021")
label_option.grid(ipadx=10, ipady=5, pady=10, row=3, columnspan=3)

# přípravky - ketamin
value_inside_ket = StringVar(frame2)
value_inside_ket.set("Přípravky s ketaminem")
question_menu_ket = OptionMenu (frame2, value_inside_ket, *ketamine_drug_dict.keys())
question_menu_ket.grid(ipadx=10, ipady=5, pady=10, row=4, column=0, sticky=W )
question_menu_ket.config (bg='#dcfeff',fg='#002021', width = 30)

# přípravky - medetomidin
value_inside_med = StringVar(frame2)
value_inside_med.set("Přípravky s medetomidinem")
question_menu_med = OptionMenu (frame2, value_inside_med, *medetomidine_drug_dict.keys())
question_menu_med.grid(ipadx=10, ipady=5, pady=10, row=4, column=1, sticky=W)
question_menu_med.config (bg ="#feffff", fg ="#002021", width = 30)

#přípravky midazolam
value_inside_mid = StringVar(frame2)
value_inside_mid.set("Přípravky s midazolamem")
question_menu_mid = OptionMenu (frame2, value_inside_mid, *midazolam_drug_dict.keys())
question_menu_mid.grid(ipadx=10, ipady=5, pady=10, row=4, column=2, sticky=W)
question_menu_mid.config (bg ="#00d9dc", fg ="#002021", width = 30)

# tlačítko pro výpočet dávek v ml všech 3 vybraných přípravků
count_button = Button(frame2, text='Spočítej dávky přípravků', command = count_dose, bg='#008587',fg='#edffff', activebackground="#007476")
count_button.grid(ipadx=10, ipady=5, pady=10, row=5, columnspan=3)

# výpis finální hodnoty všech tří přípravků v ml
result_label_ket = Label (frame2, text = "", font=("Arial", 20, "bold"), bg='#dcfeff', fg='#002021')
result_label_ket.grid(ipadx=10,row=9, column=0)

result_label_med = Label (frame2, text = "", font=("Arial", 20, "bold"), bg ="#feffff", fg ="#002021")
result_label_med.grid(ipadx=10,row=9, column=1)

result_label_mid = Label (frame2, text = "", font=("Arial", 20, "bold"), bg ="#00d9dc", fg ="#002021")
result_label_mid.grid(ipadx=10,row=9, column=2)

# hlavní cyklus
window.mainloop()

