
import customtkinter as ctk
import tkinter as tk
from PIL import Image
import json

from PasswordManager import PasswordManager as PM





class Menu1(ctk.CTk):
    
    def __init__(self):
        super().__init__()
       
        ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
      
        # configure window
        self.title("Password Generator")
        self.geometry(f"{1100}x{580}")
        
        self.password_manager = PM()
        
        self.font=("Arial", 20, "bold")
        
        self.menu2()      
        
    def menu1(self):
            
        self.clear_widgets()
        
        pad = 0.1
        self.title_label= ctk.CTkLabel(self, text="Password Generator", font=("Arial", 26, "bold", "underline"))
        self.title_label.place(relx = 0.5, rely = 0.07 + pad, anchor = tk.CENTER)

        
        self.website_label = ctk.CTkLabel(self, text="Website :", font=self.font)
        self.website_label.place(relx = 0.275, rely = 0.225 + pad, anchor = tk.CENTER)

        self.website_entry = ctk.CTkEntry(self, width = 400)
        self.website_entry.place(relx = 0.5, rely = 0.225 + pad, anchor = tk.CENTER)
        
        self.username_label = ctk.CTkLabel(self, text="Username :", font=self.font)
        self.username_label.place(relx = 0.265, rely = 0.325 + pad, anchor = tk.CENTER)

        self.username_entry = ctk.CTkEntry(self, width = 400)
        self.username_entry.place(relx = 0.5, rely = 0.325 + pad, anchor = tk.CENTER)
        
        self.slider_label = ctk.CTkLabel(self, text="Password length : 8", font=self.font)
        self.slider_label.place(relx = 0.25, rely = 0.425 + pad, anchor = tk.CENTER)
        
        self.slider_value= tk.IntVar(value=8)  # Valeur initiale (ici 0.5)
        self.slider_1 = ctk.CTkSlider(self, from_=4, to=50, number_of_steps=26, width=400, variable=self.slider_value, command = self.slider_changed)
        self.slider_1.place(relx = 0.35, rely = 0.415 + pad, anchor = tk.NW)
        
        
        self.generate_button = ctk.CTkButton(self, text="Generate", font=self.font, width=250, height=50, command = self.generate)
        self.generate_button.place(relx = 0.33, rely = 0.55 + pad, anchor = tk.CENTER)
        
        self.save_button = ctk.CTkButton(self, text="Generate and Save", font=self.font, width=250, height=50, command = self.save)
        self.save_button.place(relx = 0.67, rely = 0.55 + pad, anchor = tk.CENTER)
        
        self.output_text = tk.Text(self, font=("Arial", 34), wrap="none", height=1, width=50, state="disabled", bd=1, relief="solid")
        self.output_text.place(relx= 0.5, rely = 0.65 + pad, anchor= tk.CENTER)

        # Créez un bouton avec l'image
        self.menu1_button = ctk.CTkButton(self)
        self.menu1_button.configure(text ="History", width= 100, command=self.menu2)
        self.menu1_button.place(relx = 0.99, rely= 0.02, anchor=ctk.NE)

        
    def slider_changed(self, value):
        self.slider_label.configure(text=f"Password lenght : {int(value)}")

    
    def update_output_text(self, new_text):
        self.output_text.configure(state="normal")  # Active l'écriture temporairement
        self.output_text.delete("1.0", "end")  # Efface le texte actuel
        self.output_text.insert("1.0", new_text)  # Insère le nouveau texte
        self.output_text.configure(state="disabled")  # Désactive l'écriture à nouveau


    def save(self):
        
        website = self.website_entry.get()
        self.website_entry.delete('0', 'end')
        
        username = self.username_entry.get()
        self.username_entry.delete('0', 'end')
        
        length = self.slider_value.get()
        self.slider_1.set(8)
        self.slider_changed(8)
        
        
        password = self.password_manager.generate_passwords(website, username, length)
        self.update_output_text(password)

        
    def generate(self):
        
        password = self.password_manager.generate_password(self.slider_value.get())
        self.update_output_text(password)

        return password

    
    def select_dict(self):
        with open("passwords.json", 'r') as fichier:
            donnees = json.load(fichier)
        
        resultats = []

        for element in donnees:
            resultats.append(element)
        return resultats

    def clear_widgets(self):
            
        for widget in self.winfo_children():
            widget.destroy()  # Cachez les widgets au lieu de les détruire

    
    def menu2(self):
       
        self.clear_widgets()
        # Créez un bouton de retour au menu 1
        self.menu1_button = ctk.CTkButton(self)
        self.menu1_button.configure(text ="Menu", width= 100, command=self.menu1)
        self.menu1_button.place(relx = 0.99, rely= 0.02, anchor=ctk.NE)
        
        # Créez un bouton de retour à la page précédente
        self.menu1_button = ctk.CTkButton(self)
        self.menu1_button.configure(text ="←", width= 100, command=self.previous_page)
        self.menu1_button.place(relx = 0.1, rely= 0.02, anchor=ctk.NE)
        
        # Créez un bouton de retour à la page suivante
        self.menu1_button = ctk.CTkButton(self)
        self.menu1_button.configure(text ="→", width= 100, command=self.next_page)
        self.menu1_button.place(relx = 0.2, rely= 0.02, anchor=ctk.NE)
        
        self.page_label = ctk.CTkLabel(self, text="Page 1")
        self.page_label.place(relx = 0.25, rely= 0.02, anchor=ctk.NE)
        
        self.scrollable_frame = ctk.CTkScrollableFrame(self, label_text="Historique des mots de passe")
        self.scrollable_frame.place(relx=0, rely = 0.075, relwidth = 1, relheight= 1)
        
        with open("passwords.json", 'r') as file:
            json_data = json.load(file)
            if isinstance(json_data, list):
                self.passwords_numbers = len(json_data)
            else: 
                self.passwords_numbers = 1
        
        self.dict_list = self.select_dict()
        
        self.box_list = []
        
        self.page = 0
        
        self.page_coef = 10
        self.frame_display()
    
    def frame_display(self):
        
        for i in range(self.page_coef*self.page, self.page_coef + self.page_coef*self.page):
            if i <= self.passwords_numbers -1:
                # Créer une boîte/frame pour chaque ligne de données
                box = ctk.CTkFrame(self.scrollable_frame, fg_color="#5b7fa6",  height=50)
                box.pack(fill="x", padx=10, pady=10)  # Le paramètre fill="x" permet l'extension horizontale
                box.propagate(True)
                self.box_list.append(box)
            
                # create entry for website
                self.website_entry = ctk.CTkEntry(box, placeholder_text="website", state="normal")
                self.website_entry.place(relx=0.05, rely=0.1, relwidth=0.25, relheight=0.8)
                
                # create entry for username
                self.username_entry = ctk.CTkEntry(box, placeholder_text="username", state="normal")
                self.username_entry.place(relx=0.35, rely=0.1, relwidth=0.25, relheight=0.8)
                
                # create entry for password
                self.password_entry = ctk.CTkEntry(box, placeholder_text="password", state="normal")
                self.password_entry.place(relx=0.65, rely=0.1, relwidth=0.25, relheight=0.8)
                
                dict = self.dict_list[i]
                
                self.website_entry.insert(0, dict["website"])
                self.username_entry.insert(0, dict["username"])
                self.password_entry.insert(0, dict["password"])
                
                self.website_entry.configure(state="readonly")            
                self.username_entry.configure(state="readonly") 
                self.password_entry.configure(state="readonly")
                
        print(self.passwords_numbers, self.page)

    def previous_page(self):
        if self.page > 0:
            self.page -= 1
            self.page_label.configure(text=f"Page {self.page+1}")
            for box in self.box_list:
                box.destroy()    
            self.frame_display()
            
            
    def next_page(self):
        if (self.page+1) * self.page_coef <= self.passwords_numbers:
            self.page +=1
            self.page_label.configure(text=f"Page {self.page+1}")
            for box in self.box_list:
                box.destroy()
            self.frame_display()

if __name__ == "__main__":
    
    app = Menu1()
    app.mainloop()
