import tkinter as tk
import webbrowser
import os
from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
from carread import *
from carwrite import *
from dict import *
from get_data import *

# Define window attributes
windowH = 900       # window height
windowW = 1300      # window width
fontW = 'swos'      # Right now assume font installed in system so just name it
version = 'version 0.40'
title = 'SWOS Career Team Explorer'
url = 'https://github.com/EMPI-PL/SWOS_career_team_explorer'
colortone = '#000040'
colortone_info = '#a90000'
color_gk = "#248900"
color_pl = '#2075ee'
color_16 = '#143f7e'
color_re = '#ae131a'
fcolor_headers = '#979A9A'
pythonpath = os.path.dirname(__file__)+'/'
configfile = pythonpath + 'CARexplorer.conf'
pickedfile = ''
squadfull = []

class openfiledialog():
    def __init__(self, initialdir, title, filetype):
        self.initialdir = initialdir
        self.title = title
        self.filetype = filetype
    
    def show(self):
        x = filedialog.askopenfilename(initialdir=self.initialdir, title=self.title, filetypes=self.filetype)
        return x

def opencar():
    global pickedfile
    global squadfull
    clear_frame(mf_leftframe)    
    choosecarfile = openfiledialog(default_opendir,'Select SWOS career file',[('SWOS Career file', '*.CAR')])
    pickedfile = choosecarfile.show()
    carfile_output = readcarfile(pickedfile)  # Call func to read squad details
    updateview(carfile_output)   # Call func to view data
    squadfull = carfile_output[2]

def clear_frame(framename):
    for widgets in framename.winfo_children():
        widgets.destroy()

def updatemoneydisplay(balance):
    moneycanvas = Canvas(mf_rightframe,width=280,borderwidth=0, highlightthickness=0,bg=colortone)
    moneycanvas.place(x=10,y=130)

    teamnamebox_5 = Label(moneycanvas,bg=colortone,width=15,height=1,bd=0,highlightthickness=0, font=('swos',14),anchor='w',text='BANK BALANCE:',fg='yellow')
    teamnamebox_5.grid(row=0,column=0,columnspan=2)
    teamnamebox_6 = Label(moneycanvas,bg=colortone,width=20,height=1,bd=0,highlightthickness=0, font=('swos',12),anchor='e',text="{:0,.2f}".format(float(balance)),fg='white')
    teamnamebox_6.grid(row=1,column=1,columnspan=2,pady=5)

def updateview(carfile_output):
    squad = carfile_output[0]
    carfileteaminfo = carfile_output[1]
    squadcanvas = Canvas(mf_leftframe,width=680,borderwidth=0, highlightthickness=0,bg=colortone)
    squadcanvas.place(x=10,y=10)
    
    counter = 0
    # Display table headers
    head_label = Label(squadcanvas,bg=colortone,width=1,height=1,bd=0,highlightthickness=0, font=('swos',16),text=" ",fg=fcolor_headers)
    num_label = Label(squadcanvas,bg=colortone,width=1,height=1,bd=0,highlightthickness=0, font=('swos',16),text="#",fg=fcolor_headers)
    name_label = Label(squadcanvas,bg=colortone,width=20,height=1,bd=0,highlightthickness=0, font=('swos',16),anchor='w',text="Player name",fg=fcolor_headers, padx=20)
    pos_label = Label(squadcanvas,bg=colortone,width=3,height=1,bd=0,highlightthickness=0, font=('swos',16),text="POS",fg=fcolor_headers)
    nat_label = Label(squadcanvas,bg=colortone,width=3,height=1,bd=0,highlightthickness=0, font=('swos',16),text="NAT",fg=fcolor_headers,padx=10)
    p_label = Label(squadcanvas,bg=colortone,width=2,height=1,bd=0,highlightthickness=0, font=('swos',16),text="P",fg=fcolor_headers)
    v_label = Label(squadcanvas,bg=colortone,width=2,height=1,bd=0,highlightthickness=0, font=('swos',16),text="V",fg=fcolor_headers)
    h_label = Label(squadcanvas,bg=colortone,width=2,height=1,bd=0,highlightthickness=0, font=('swos',16),text="H",fg=fcolor_headers)
    t_label = Label(squadcanvas,bg=colortone,width=2,height=1,bd=0,highlightthickness=0, font=('swos',16),text="T",fg=fcolor_headers)
    c_label = Label(squadcanvas,bg=colortone,width=2,height=1,bd=0,highlightthickness=0, font=('swos',16),text="C",fg=fcolor_headers)
    s_label = Label(squadcanvas,bg=colortone,width=2,height=1,bd=0,highlightthickness=0, font=('swos',16),text="S",fg=fcolor_headers)
    f_label = Label(squadcanvas,bg=colortone,width=2,height=1,bd=0,highlightthickness=0, font=('swos',16),text="F",fg=fcolor_headers)
    star_label = Label(squadcanvas,bg=colortone,width=5,height=1,bd=0,highlightthickness=0, font=('swos',16),text="SKILL",fg=fcolor_headers)
    head_label.grid(row=counter,column=0,sticky='n',pady=3)
    num_label.grid(row=counter,column=1,sticky='n',pady=3)
    name_label.grid(row=counter,column=2,sticky='n',pady=3)
    pos_label.grid(row=counter,column=3,sticky='n',pady=3)
    nat_label.grid(row=counter,column=4,sticky='n',pady=3)
    p_label.grid(row=counter,column=5,sticky='n',pady=3)
    v_label.grid(row=counter,column=6,sticky='n',pady=3)
    h_label.grid(row=counter,column=7,sticky='n',pady=3)
    t_label.grid(row=counter,column=8,sticky='n',pady=3)
    c_label.grid(row=counter,column=9,sticky='n',pady=3)
    s_label.grid(row=counter,column=10,sticky='n',pady=3)
    f_label.grid(row=counter,column=11,sticky='n',pady=3)
    star_label.grid(row=counter,column=12,sticky='n',pady=3)
    
    counter += 1
    while counter < len(squad):
        pic_load = Image.open(pythonpath+squad[counter][0])    # Read a "head picture"
        pic_set = ImageTk.PhotoImage(pic_load)
        star_load = Image.open(pythonpath+d_stars[squad[counter][12]])
        star_set = ImageTk.PhotoImage(star_load)
        head_label = Label(squadcanvas,image=pic_set,bg=color_pl,bd=0)
        head_label.image = pic_set
        star_label = Label(squadcanvas,image=star_set,bg=colortone,bd=0)
        star_label.image = star_set
        num_label = Label(squadcanvas,bg=colortone,width=3,height=1,bd=0,highlightthickness=0, font=('swos',16),text=squad[counter][1],fg='white')
        pos_label = Label(squadcanvas,bg=colortone,width=3,height=1,bd=0,highlightthickness=0, font=('swos',16),text=squad[counter][3],fg='white')
        nat_label = Label(squadcanvas,bg=colortone,width=3,height=1,bd=0,highlightthickness=0, font=('swos',16),text=squad[counter][4],fg='white',padx=10)
        # Player's skills columns
        p_label = Label(squadcanvas,bg=colortone,width=2,height=1,bd=0,highlightthickness=0, font=('swos',16),text=convert815skills(hex2int(squad[counter][5]),convert_skills),fg=d_skillcolor[hex2int(squad[counter][5])])
        v_label = Label(squadcanvas,bg=colortone,width=2,height=1,bd=0,highlightthickness=0, font=('swos',16),text=convert815skills(hex2int(squad[counter][6]),convert_skills),fg=d_skillcolor[hex2int(squad[counter][6])])
        h_label = Label(squadcanvas,bg=colortone,width=2,height=1,bd=0,highlightthickness=0, font=('swos',16),text=convert815skills(hex2int(squad[counter][7]),convert_skills),fg=d_skillcolor[hex2int(squad[counter][7])])
        t_label = Label(squadcanvas,bg=colortone,width=2,height=1,bd=0,highlightthickness=0, font=('swos',16),text=convert815skills(hex2int(squad[counter][8]),convert_skills),fg=d_skillcolor[hex2int(squad[counter][8])])
        c_label = Label(squadcanvas,bg=colortone,width=2,height=1,bd=0,highlightthickness=0, font=('swos',16),text=convert815skills(hex2int(squad[counter][9]),convert_skills),fg=d_skillcolor[hex2int(squad[counter][9])])
        s_label = Label(squadcanvas,bg=colortone,width=2,height=1,bd=0,highlightthickness=0, font=('swos',16),text=convert815skills(hex2int(squad[counter][10]),convert_skills),fg=d_skillcolor[hex2int(squad[counter][10])])
        f_label = Label(squadcanvas,bg=colortone,width=2,height=1,bd=0,highlightthickness=0, font=('swos',16),text=convert815skills(hex2int(squad[counter][11]),convert_skills),fg=d_skillcolor[hex2int(squad[counter][11])])
        # Condition for goalkeeper (match case instruction released in Python 3.10)
        if counter<12:
            match squad[counter][3]:
                case 'G':
                    name_label = Label(squadcanvas,bg=color_gk,width=20,height=1,bd=0,highlightthickness=0, font=('swos',16),anchor='w',text=squad[counter][2],fg='white', padx=20)
                case _:
                    name_label = Label(squadcanvas,bg=color_pl,width=20,height=1,bd=0,highlightthickness=0, font=('swos',16),anchor='w',text=squad[counter][2],fg='white', padx=20)
        elif counter <17:
            match squad[counter][3]:
                case 'G':
                    name_label = Label(squadcanvas,bg=color_gk,width=20,height=1,bd=0,highlightthickness=0, font=('swos',16),anchor='w',text=squad[counter][2],fg='white', padx=20)
                case _:
                    name_label = Label(squadcanvas,bg=color_16,width=20,height=1,bd=0,highlightthickness=0, font=('swos',16),anchor='w',text=squad[counter][2],fg='white', padx=20)
        else:
            match squad[counter][3]:
                case 'G':
                    name_label = Label(squadcanvas,bg=color_gk,width=20,height=1,bd=0,highlightthickness=0, font=('swos',16),anchor='w',text=squad[counter][2],fg='white', padx=20)
                case _:
                    name_label = Label(squadcanvas,bg=color_re,width=20,height=1,bd=0,highlightthickness=0, font=('swos',16),anchor='w',text=squad[counter][2],fg='white', padx=20)
        # Put the grid on screen
        head_label.grid(row=counter,column=0,sticky='n',pady=3)
        num_label.grid(row=counter,column=1,sticky='n',pady=3)
        name_label.grid(row=counter,column=2,sticky='n',pady=3)
        pos_label.grid(row=counter,column=3,sticky='n',pady=3)
        nat_label.grid(row=counter,column=4,sticky='n',pady=3)             
        p_label.grid(row=counter,column=5,sticky='n',pady=3)
        v_label.grid(row=counter,column=6,sticky='n',pady=3)
        h_label.grid(row=counter,column=7,sticky='n',pady=3)
        t_label.grid(row=counter,column=8,sticky='n',pady=3)
        c_label.grid(row=counter,column=9,sticky='n',pady=3)
        s_label.grid(row=counter,column=10,sticky='n',pady=3)
        f_label.grid(row=counter,column=11,sticky='n',pady=3)
        star_label.grid(row=counter,column=12,sticky='n',pady=3)
        counter += 1
    
    # Show team info on the right side
    teamcanvas = Canvas(mf_rightframe,width=280,borderwidth=0, highlightthickness=0,bg=colortone)
    teamcanvas.place(x=10,y=20)
    
    teamnamebox_1 = Label(teamcanvas,bg=colortone,width=15,height=1,bd=0,highlightthickness=0, font=('swos',14),anchor='w',text='TEAM NAME:',fg='yellow')
    teamnamebox_1.grid(row=0,column=0,columnspan=2)
    teamnamebox_2 = Label(teamcanvas,bg=colortone,width=20,height=1,bd=0,highlightthickness=0, font=('swos',12),anchor='e',text=carfileteaminfo.clubname,fg='white')
    teamnamebox_2.grid(row=1,column=1,columnspan=2,pady=5)
    
    box_br1 = Label(teamcanvas,bg=colortone,width=10,height=1,bd=0,highlightthickness=0, font=('swos',12),text=' ',fg='white')
    box_br1.grid(row=2,column=0,columnspan=2)

    teamnamebox_3 = Label(teamcanvas,bg=colortone,width=15,height=1,bd=0,highlightthickness=0, font=('swos',14),anchor='w',text='MANAGER NAME:',fg='yellow')
    teamnamebox_3.grid(row=3,column=0,columnspan=2)
    teamnamebox_4 = Label(teamcanvas,bg=colortone,width=20,height=1,bd=0,highlightthickness=0, font=('swos',12),anchor='e',text=carfileteaminfo.managername,fg='white')
    teamnamebox_4.grid(row=4,column=1,columnspan=2,pady=5)
    
    box_br2 = Label(teamcanvas,bg=colortone,width=10,height=1,bd=0,highlightthickness=0, font=('swos',12),text=' ',fg='white')
    box_br2.grid(row=5,column=0,columnspan=2)

    updatemoneydisplay(carfileteaminfo.money)

def close():
    quit()

def work_in_progress():
    tk.messagebox.showinfo("Stay tuned",  "One day this will be possible... :-)")

def upd_data_teams():
    update_teamdata(swos_data_directory,data_directory)
    tk.messagebox.showinfo("Done",  'DATA has been updated. The file has been saved under xml directory.')

def show_attributes(selected_name):
    def save_attributes():
        # Save the updated attributes
        selected_player.name = name_entry.get()
        selected_player.P = int(p_combobox.get())
        selected_player.V = int(v_combobox.get())
        selected_player.H = int(h_combobox.get())
        selected_player.T = int(t_combobox.get())
        selected_player.C = int(c_combobox.get())
        selected_player.S = int(s_combobox.get())
        selected_player.F = int(f_combobox.get())
        if bool(is_clean_var.get()) == True:
                selected_player.cardsinjuries = '00'

        selected_player.UpdateInCAR(pickedfile)

        attributes_popup.destroy()

        carfile_output = readcarfile(pickedfile)  # Call func to read squad details
        updateview(carfile_output)   # Call func to view data
        squadfull = carfile_output[2]

        messagebox.showinfo("Info", f"Attributes for {selected_player.name} updated successfully!")

    # Close the first pop-up window
    popup.destroy()

    # Find the selected person
    selected_player = next(curplayer for curplayer in squadfull if curplayer.name == selected_name)
    
    # Create another pop-up window to show and edit attributes
    attributes_popup = tk.Toplevel(root)
    attributes_popup.title("Edit Attributes")

    # Editable fields
    tk.Label(attributes_popup, text="Name:").grid(row=0, column=0, padx=10, pady=5)
    name_entry = tk.Entry(attributes_popup)
    name_entry.insert(0, selected_player.name)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(attributes_popup, text="P:").grid(row=1, column=0, padx=10, pady=5)
    p_combobox = ttk.Combobox(attributes_popup, values=list(range(8)), width=3)
    p_combobox.set(selected_player.P)
    p_combobox.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(attributes_popup, text="V:").grid(row=2, column=0, padx=10, pady=5)
    v_combobox = ttk.Combobox(attributes_popup, values=list(range(8)), width=3)
    v_combobox.set(selected_player.V)
    v_combobox.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(attributes_popup, text="H:").grid(row=3, column=0, padx=10, pady=5)
    h_combobox = ttk.Combobox(attributes_popup, values=list(range(8)), width=3)
    h_combobox.set(selected_player.H)
    h_combobox.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(attributes_popup, text="T:").grid(row=4, column=0, padx=10, pady=5)
    t_combobox = ttk.Combobox(attributes_popup, values=list(range(8)), width=3)
    t_combobox.set(selected_player.T)
    t_combobox.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(attributes_popup, text="C:").grid(row=5, column=0, padx=10, pady=5)
    c_combobox = ttk.Combobox(attributes_popup, values=list(range(8)), width=3)
    c_combobox.set(selected_player.C)
    c_combobox.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(attributes_popup, text="S:").grid(row=6, column=0, padx=10, pady=5)
    s_combobox = ttk.Combobox(attributes_popup, values=list(range(8)), width=3)
    s_combobox.set(selected_player.S)
    s_combobox.grid(row=6, column=1, padx=10, pady=5)

    tk.Label(attributes_popup, text="F:").grid(row=7, column=0, padx=10, pady=5)
    f_combobox = ttk.Combobox(attributes_popup, values=list(range(8)), width=3)
    f_combobox.set(selected_player.F)
    f_combobox.grid(row=7, column=1, padx=10, pady=5)

    tk.Label(attributes_popup, text="Clear Red Cards and Injuries:").grid(row=8, column=0, padx=10, pady=5)
    is_clean_var = tk.IntVar(value=1 if selected_player.cardsinjuries == 'ff' else 0)
    is_clean_checkbox = tk.Checkbutton(attributes_popup, variable=is_clean_var)
    is_clean_checkbox.grid(row=8, column=1, padx=10, pady=5)

    # Non-editable fields
    non_editable_attributes = ["value", "position", "nation"]
    for i, attr in enumerate(non_editable_attributes, start=9):
        tk.Label(attributes_popup, text=f"{attr.capitalize()}:").grid(row=i, column=0, padx=10, pady=5)
        tk.Label(attributes_popup, text=getattr(selected_player, attr)).grid(row=i, column=1, padx=10, pady=5)

    # OK button to save and close the attributes pop-up
    tk.Button(attributes_popup, text="OK", command=save_attributes).grid(row=i+1, column=0, pady=10)
    # Cancel button to close the attributes pop-up without saving
    tk.Button(attributes_popup, text="Cancel", command=attributes_popup.destroy).grid(row=i+1, column=1, pady=10)


def upd_data_players():     # This feature is planned for future releases
    global popup
    global pickedfile
    global squadfull
    popup = tk.Toplevel(root)
    popup.title("Select Name")

    # Dropdown list
    selected_name = tk.StringVar()
    dropdown = ttk.Combobox(popup, textvariable=selected_name, values=[curplayer.name for curplayer in squadfull])
    dropdown.pack(pady=10)

    # OK button
    tk.Button(popup, text="OK", command=lambda: show_attributes(selected_name.get())).pack(side=tk.LEFT, padx=10)

    # Cancel button
    tk.Button(popup, text="Cancel", command=popup.destroy).pack(side=tk.RIGHT, padx=10)

def change_balance():      # This feature is planned for future releases
    global pickedfile
    global squadfull
    if pickedfile != '':
        user_input = simpledialog.askstring("Input", "Enter a new Bank Balance Amount:")
        
        try:
            newbalance = max(0, min(100000000, int(user_input))) #do not allow crazy values
        except ValueError:
            tk.messagebox.showinfo("Invalid", "Please enter a valid number.")
            return

        updateCARbalance(pickedfile, newbalance)

        updatemoneydisplay(newbalance)

        tk.messagebox.showinfo("Done", "Balance updated in CAR file")

    else:
        tk.messagebox.showinfo("No CAR", "Please load a .CAR file first.")



def edit_player():          # This feature is planned for future releases
    pass

def add_player():           # This feature is planned for future releases
    pass

def infobox():
    rinf = tk.Tk()
    rinf.title("Info")
    rinf.resizable(0,0) # Make the frame not resizable
    rinf.geometry('400x200')
    rinfframe = Frame(rinf, width=400, height=200, bg=colortone_info, highlightthickness=0, bd=0)
    rinfframe.grid(row=0,column=0)
    
    infocanvas = Canvas(rinfframe,width=400,borderwidth=0, highlightthickness=0,bg=colortone_info)
    infocanvas.place(x=0,y=0)

    x_1 = Label(infocanvas,bg=colortone_info,width=28,height=1,bd=0,highlightthickness=0, font=('swos',13),anchor='c',text=title,fg='yellow')
    x_2 = Label(infocanvas,bg=colortone_info,height=1,bd=0,highlightthickness=0, font=('swos',8),anchor='c',text=version,fg='yellow')
    x_3 = Label(infocanvas,bg=colortone_info,height=1,bd=0,highlightthickness=0, font=('swos',8),anchor='c',text='brought to you by EMPI',fg='white')
    x_br1 = Label(infocanvas,bg=colortone_info,height=3,bd=0,highlightthickness=0, font=('swos',8),anchor='c',text=' ',fg='white')
    x_br2 = Label(infocanvas,bg=colortone_info,height=3,bd=0,highlightthickness=0, font=('swos',8),anchor='c',text=' ',fg='white')
    x_4 = Label(infocanvas,bg=colortone_info,height=1,bd=0,highlightthickness=0, font=('swos',8),anchor='c',text='find me on github or sensiblesoccer.de',fg='white')
    x_br1.grid(row=0,column=0)
    x_1.grid(row=1,column=0)
    x_2.grid(row=2,column=0)
    x_3.grid(row=3,column=0,pady=10)
    x_br2.grid(row=4,column=0)
    x_4.grid(row=5,column=0)
    
    rinf.mainloop()

def launchgitsite():
    webbrowser.open(url)


# Read config file setup
cfg = open(configfile, 'r') # Open read-only
cfglines = cfg.readlines()  # Load config file lines
for cfgentry in cfglines:
    if cfgentry[0] != '#' and cfgentry[0] != '\n':
        eqpos = cfgentry.index('=')
        match cfgentry[:cfgentry.index('=')]:
            case 'carpath':
                default_opendir = cfgentry[cfgentry.index('=')+1:cfgentry.index('\n')]
            case 'datadir':
                swos_data_directory = cfgentry[cfgentry.index('=')+1:cfgentry.index('\n')]
            case 'xmldir':
                data_directory = cfgentry[cfgentry.index('=')+1:]
            case 'convert815skills':
                convert_skills = cfgentry[cfgentry.index('=')+1:cfgentry.index('\n')] == 'true'
cfg.close()

# Setup and show MAIN WINDOW
root = tk.Tk()
root.title(title)
root.resizable(0,0) # Make the frame not resizable
root.geometry(str(windowW)+'x'+str(windowH))

# Define buttons/images used in app's window
b1 = PhotoImage(file=pythonpath+'img/button_quit.png')             # Quit menu button
b2 = PhotoImage(file=pythonpath+'img/button_opencar.png')          # Open *.CAR file menu button
b3 = PhotoImage(file=pythonpath+'img/button_updatexml.png')        # Update team db in XML
b4 = PhotoImage(file=pythonpath+'img/button_change_bbalance.png')  # Change BBalance
b5 = PhotoImage(file=pythonpath+'img/button_edt_plr.png')          # Edit player
b6 = PhotoImage(file=pythonpath+'img/button_add_plr.png')          # Add player
b7 = PhotoImage(file=pythonpath+'img/button_gen_job.png')          # Generate job offer
img1 = PhotoImage(file=pythonpath+'res/sensi_logo_small.png')      # Left-upper corner logo
bg = PhotoImage(file=pythonpath+'img/bgswos.png')                  # Left's side background
info = PhotoImage(file=pythonpath+'img/button_info.png')           # Open info
git = PhotoImage(file=pythonpath+'img/button_git.png')             # Open GitHUB

# Upper frame section (title)
#- - - - - - - - - - - - - - - - -
mf_upperframe = Frame(root, height=50, width=windowW, bg=colortone, highlightthickness=0, bd=0)
mf_upperframe.grid(row=0,column=0,columnspan=2)
ImgLogo = Label(mf_upperframe,image=img1,bg=colortone)
ImgLogo.place(x=0,y=4)
txt = Label(mf_upperframe, text='SWOS Career Team Explorer', font=('swos',20), fg='white',bg=colortone,bd=0, anchor='w',width=50,highlightthickness='0')
txt.place(x=80,y=15)
txt = Label(mf_upperframe, text=version, font=('swos',8), fg=fcolor_headers,bg=colortone,bd=0, anchor='w',width=50,highlightthickness='0')
txt.place(x=windowW-100,y=22)

# Left frame section (squad)
#- - - - - - - - - - - - - - - - -
mf_leftframe = Frame(root, height=850, width=windowW-300,bg=colortone, highlightthickness=0, bd=0)
mf_leftframe.grid(row=1,column=0)
bg_label = Label(mf_leftframe,image=bg,bd=0,highlightthickness=0)   # Label to store bg image
bg_label.place(x=0,y=0)

# Right frame section (menu)
#- - - - - - - - - - - - - - - - -
mf_rightframe = Frame(root, height=850, width=300, bg=colortone, highlightthickness=0,bd=0) # Label with menu
mf_rightframe.grid(row=1,column=1)
Button(mf_rightframe, image=b4, borderwidth=0, highlightthickness=0, command=change_balance).place(y=400,x=30)
Button(mf_rightframe, image=b7, borderwidth=0, highlightthickness=0, command=work_in_progress).place(y=450,x=30)
Button(mf_rightframe, image=b3, borderwidth=0, highlightthickness=0, command=upd_data_teams).place(y=500,x=30)
Button(mf_rightframe, image=b5, borderwidth=0, highlightthickness=0, command=upd_data_players).place(y=550,x=30)
Button(mf_rightframe, image=b6, borderwidth=0, highlightthickness=0, command=work_in_progress).place(y=600,x=30)
Button(mf_rightframe, image=b1, borderwidth=0, highlightthickness=0, command=close).place(y=750,x=30)
Button(mf_rightframe, image=b2, borderwidth=0, highlightthickness=0, command=opencar).place(y=700,x=30)
Button(mf_rightframe, image=info, borderwidth=0, highlightthickness=0, command=infobox).place(y=650,x=160)
Button(mf_rightframe, image=git, borderwidth=0, highlightthickness=0, command=launchgitsite).place(y=650,x=30)




root.mainloop()
