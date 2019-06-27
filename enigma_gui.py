from tkinter import *
from enigma_logic import EnigmaMachine
from rotor_class import *

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ROTOR_OPTIONS = []
REFLECTOR_OPTIONS = []
for option in ENIGMA_ROTORS:
    if 'UKW' in option:
        REFLECTOR_OPTIONS.append(option)
    elif 'ETW' in option:
        pass
    else:
        ROTOR_OPTIONS.append(option)

machine = EnigmaMachine('I', 'II', 'III', 'UKW-B')
left_rotor_name = str(machine.get_left_rotor)
mid_rotor_name = machine.get_middle_rotor

on_off_setting = {'A': 'grey', 'B': 'grey', 'C': 'grey',
                  'D': 'grey', 'E': 'grey', 'F': 'grey',
                  'G': 'grey', 'H': 'grey', 'I': 'grey',
                  'J': 'grey', 'K': 'grey', 'L': 'grey',
                  'M': 'grey', 'N': 'grey', 'O': 'grey',
                  'P': 'grey', 'Q': 'grey', 'R': 'grey',
                  'S': 'grey', 'T': 'grey', 'U': 'grey',
                  'V': 'grey', 'W': 'grey', 'X': 'grey',
                  'Y': 'grey', 'Z': 'grey'}

def quit():
    root.quit()

def reset_default(mach):

    update_left_rotor_name('I')
    update_left_rotor_setting('A')
    update_middle_rotor_name('II')
    update_middle_rotor_setting('A')
    update_right_rotor_name('III')
    update_right_rotor_setting('A')
    update_reflector_name('UKW-B')

    mach.reset_rotors()

    for let in ALPHABET:
        mach.set_plugboard_pair(let, let)


    sent_output_str.set('')

    for x in on_off_setting:
        on_off_setting[x] = 'grey'
    q_canvas.itemconfig('Q', fill=on_off_setting['Q'])
    w_canvas.itemconfig('W', fill=on_off_setting['W'])
    e_canvas.itemconfig('E', fill=on_off_setting['E'])
    r_canvas.itemconfig('R', fill=on_off_setting['R'])
    t_canvas.itemconfig('T', fill=on_off_setting['T'])
    z_canvas.itemconfig('Z', fill=on_off_setting['Z'])
    u_canvas.itemconfig('U', fill=on_off_setting['U'])
    i_canvas.itemconfig('I', fill=on_off_setting['I'])
    o_canvas.itemconfig('O', fill=on_off_setting['O'])
    a_canvas.itemconfig('A', fill=on_off_setting['A'])
    s_canvas.itemconfig('S', fill=on_off_setting['S'])
    d_canvas.itemconfig('D', fill=on_off_setting['D'])
    f_canvas.itemconfig('F', fill=on_off_setting['F'])
    g_canvas.itemconfig('G', fill=on_off_setting['G'])
    h_canvas.itemconfig('H', fill=on_off_setting['H'])
    j_canvas.itemconfig('J', fill=on_off_setting['J'])
    k_canvas.itemconfig('K', fill=on_off_setting['K'])
    p_canvas.itemconfig('P', fill=on_off_setting['P'])
    y_canvas.itemconfig('Y', fill=on_off_setting['Y'])
    x_canvas.itemconfig('X', fill=on_off_setting['X'])
    c_canvas.itemconfig('C', fill=on_off_setting['C'])
    v_canvas.itemconfig('V', fill=on_off_setting['V'])
    b_canvas.itemconfig('B', fill=on_off_setting['B'])
    n_canvas.itemconfig('N', fill=on_off_setting['N'])
    m_canvas.itemconfig('M', fill=on_off_setting['M'])
    l_canvas.itemconfig('L', fill=on_off_setting['L'])

def update_left_rotor_name(left_rotor_name):
    machine.set_left_rotor(left_rotor_name)

def update_left_rotor_setting(left_rotor_setting):
    machine.set_left_rotor_pos(left_rotor_setting)
    rotor_l_viewable.itemconfig('rotor_l', text=machine.get_left_rotor_pos())

def update_middle_rotor_name(middle_rotor_name):
    machine.set_middle_rotor(middle_rotor_name)

def update_middle_rotor_setting(middle_rotor_setting):
    machine.set_middle_rotor_pos(middle_rotor_setting)
    rotor_m_viewable.itemconfig('rotor_m', text=machine.get_middle_rotor_pos())

def update_right_rotor_name(right_rotor_name):
    machine.set_right_rotor(right_rotor_name)

def update_right_rotor_setting(right_rotor_setting):
    machine.set_right_rotor_pos(right_rotor_setting)
    rotor_r_viewable.itemconfig('rotor_r', text=machine.get_right_rotor_pos())

def update_reflector_name(reflector_name):
    machine.set_reflector(reflector_name)

def update_switchboard_display(event, s_canvas, LETTER_POSITIONS):
    s_canvas.delete("all")
    for letter, setting in machine._plugboard.items():
        s_canvas.create_line(LETTER_POSITIONS[letter], 10,
                                       LETTER_POSITIONS[setting], 263, tags=letter)
        s_canvas.create_rectangle(LETTER_POSITIONS[letter] - 5, 5,
                                            LETTER_POSITIONS[letter] + 5, 15)
        s_canvas.create_rectangle(LETTER_POSITIONS[letter] - 5, 258,
                                            LETTER_POSITIONS[letter] + 5, 268)

def reset_switchboard(event, s_canvas, LETTER_POSITIONS):
    for let in ALPHABET:
        machine.set_plugboard_pair(let, let)

    update_switchboard_display(event, s_canvas, LETTER_POSITIONS)

def switchboard_lclick(event, input, s_canvas, LETTER_POSITIONS):
    print(event.x, event.y)
    first_click, second_click = input

    LETTER_R_BOUND = {}
    for let,pos in LETTER_POSITIONS.items():
        LETTER_R_BOUND[let] = pos+10

    if first_click == None:
        print("yay")

        for let, pos in LETTER_R_BOUND.items():
            if event.x < pos:
                s_canvas.delete(let)
                input[0] = let
                break

        """Draws the boundaries in red for each letter
        for let, pos in LETTER_POSITIONS.items():
            s_canvas.create_line(pos+10, 10, pos+10, 263, tags=let + "c", fill="red")"""

    elif second_click == None:
        print("boo")
        input[1] = True

        for let, pos in LETTER_R_BOUND.items():
            if event.x < pos:
                input[1] = let
                break


        machine.set_plugboard_pair(input[0], input[1])
        input[0] = None;input[1] = None
        update_switchboard_display(event, s_canvas, LETTER_POSITIONS)


def open_switchboard_window():
    switchboard = Tk()
    switchboard.title("Switchboard")
    switchboard.geometry('560x370')
    changing_pairs = [None, None]

    # Top letter frame
    top_letter_frame = Frame(switchboard)

    for letter in ALPHABET:
        letter_frame = Frame(top_letter_frame)
        letter_label = Label(letter_frame, text=letter)
        letter_label.pack(padx=4)
        letter_frame.pack(side=LEFT)

    top_letter_frame.pack(side=TOP, fill=X)

    # Canvas for connecting letters
    LETTER_POSITIONS = {}
    for i, letter in enumerate(ALPHABET):
        LETTER_POSITIONS[letter] = (i+1)*550/26 - 10     # Ugly hardcode... Tkinter won't recognise it's own widths
    print(LETTER_POSITIONS)

    connections_frame = Frame(switchboard)
    connections_canvas = Canvas(connections_frame, bd=2, relief=SUNKEN, width=550)
    connections_canvas.bind('<Button-1>', lambda event, arg=changing_pairs, c=connections_canvas, l=LETTER_POSITIONS:
                                switchboard_lclick(event, arg, c, l))
    connections_canvas.bind('<Button-3>', lambda event, c=connections_canvas,l=LETTER_POSITIONS:
                                reset_switchboard(event, c, l))

    for letter,setting in machine._plugboard.items():
        connections_canvas.create_line(LETTER_POSITIONS[letter], 10,
                                       LETTER_POSITIONS[setting], 263, tags=letter)
        connections_canvas.create_rectangle(LETTER_POSITIONS[letter]-5, 5,
                                            LETTER_POSITIONS[letter]+5, 15)
        connections_canvas.create_rectangle(LETTER_POSITIONS[letter] - 5, 258,
                                            LETTER_POSITIONS[letter] + 5, 268)

    connections_canvas.pack(expand=True, fill=Y)
    connections_frame.pack(side=TOP,fill=BOTH)


    # Bottom letter frame
    bottom_letter_frame = Frame(switchboard)

    for letter in ALPHABET:
        letter_frame = Frame(bottom_letter_frame)
        letter_label = Label(letter_frame, text=letter)
        letter_label.pack(padx=4)
        letter_frame.pack(side=LEFT)

    bottom_letter_frame.pack(side=TOP, fill=X)

    # Buttons frame
    buttons_frame = Frame(switchboard)

    quit_connections_button = Button(buttons_frame, text="Quit", command=switchboard.destroy)
    quit_connections_button.pack(side=LEFT)

    reset_connections_button = Button(buttons_frame, text="Reset Plugboard", command =
                                lambda event=None, c=connections_canvas,l=LETTER_POSITIONS:
                                reset_switchboard(event, c, l))
    reset_connections_button.pack(side=LEFT)

    buttons_frame.pack(side=TOP)

    switchboard.mainloop()


root = Tk()
root.title("Enigma Machine")

top_frame = Frame(root)
top_frame.pack()

# Reflector frame
reflector_frame = Frame(top_frame)

## Reflector label
reflector_label = Label(reflector_frame, text="Reflector")
reflector_label.pack(side=TOP)

## Reflector options
reflector_user_choice = StringVar(root)
reflector_user_choice.set(machine.get_reflector())
reflector_choice_list = OptionMenu(reflector_frame, reflector_user_choice, *REFLECTOR_OPTIONS, command=update_reflector_name)
reflector_choice_list.pack(side=TOP)

reflector_frame.pack(side=LEFT)

# Left rotor frame
left_rotor_frame = Frame(top_frame)

## Left rotor's label
left_rotor_label = Label(left_rotor_frame, text="Left Rotor")
left_rotor_label.pack(side = TOP)

## Left rotor options
left_rotor_user_choice = StringVar(root)
left_rotor_user_choice.set(machine.get_left_rotor())
left_rotor_choice_list = OptionMenu(left_rotor_frame, left_rotor_user_choice, *ROTOR_OPTIONS, command=update_left_rotor_name)
left_rotor_choice_list.pack(side=TOP)

## Left rotor settings label
left_rotor_setting_label = Label(left_rotor_frame, text="Settings")
left_rotor_setting_label.pack(side = TOP)

## Left rotor's position selection
left_rotor_user_setting = StringVar(root)
left_rotor_user_setting.set(machine.get_left_rotor_pos())
left_rotor_list = OptionMenu(left_rotor_frame, left_rotor_user_setting, *ALPHABET, command=update_left_rotor_setting)
left_rotor_list.pack(side = TOP)

## Left rotor viewable letter
rotor_l_viewable = Canvas(left_rotor_frame, width=50, height=50)
rotor_l_viewable.pack(side=TOP)
rotor_l_viewable.create_rectangle(15,15,35,50, fill="#b67057")
rotor_l_viewable.create_text((25,33),text=machine.get_left_rotor_pos(), tags='rotor_l')

left_rotor_frame.pack(side = LEFT)

# Middle rotor frame
middle_rotor_frame = Frame(top_frame)

## Middle rotor's label
middle_rotor_label = Label(middle_rotor_frame, text="Middle Rotor")
middle_rotor_label.pack(side = TOP)

## Middle rotor options
middle_rotor_user_choice = StringVar(root)
middle_rotor_user_choice.set(machine.get_middle_rotor())
middle_rotor_choice_list = OptionMenu(middle_rotor_frame, middle_rotor_user_choice, *ROTOR_OPTIONS, command=update_middle_rotor_name)
middle_rotor_choice_list.pack(side=TOP)

## Middle rotor settings label
middle_rotor_setting_label = Label(middle_rotor_frame, text="Settings")
middle_rotor_setting_label.pack(side = TOP)

## Middle rotor's position selection
middle_rotor_user_setting = StringVar(root)
middle_rotor_user_setting.set(machine.get_middle_rotor_pos())
middle_rotor_list = OptionMenu(middle_rotor_frame, middle_rotor_user_setting, *ALPHABET, command=update_middle_rotor_setting)
middle_rotor_list.pack(side = TOP)

## Middle rotor viewable letter
rotor_m_viewable = Canvas(middle_rotor_frame, width=50, height=50)
rotor_m_viewable.pack(side=TOP)
rotor_m_viewable.create_rectangle(15,15,35,50, fill="#b67057")
rotor_m_viewable.create_text((25,33),text=machine.get_middle_rotor_pos(), tags='rotor_m')

middle_rotor_frame.pack(side = LEFT)

# Right rotor frame
right_rotor_frame = Frame(top_frame)

## Right rotor's label
right_rotor_label = Label(right_rotor_frame, text="Right Rotor")
right_rotor_label.pack(side = TOP)

## Right rotor options
right_rotor_user_choice = StringVar(root)
right_rotor_user_choice.set(machine.get_right_rotor())
right_rotor_choice_list = OptionMenu(right_rotor_frame, right_rotor_user_choice, *ROTOR_OPTIONS, command=update_right_rotor_name)
right_rotor_choice_list.pack(side=TOP)

## Right rotor settings label
right_rotor_setting_label = Label(right_rotor_frame, text="Settings")
right_rotor_setting_label.pack(side=TOP)

## Right rotor's position selection
right_rotor_user_setting = StringVar(root)
right_rotor_user_setting.set(machine.get_right_rotor_pos())
right_rotor_list = OptionMenu(right_rotor_frame, right_rotor_user_setting, *ALPHABET, command=update_right_rotor_setting)
right_rotor_list.pack(side=TOP)

## Right rotor viewable letter
rotor_r_viewable = Canvas(right_rotor_frame, width=50, height=50)
rotor_r_viewable.pack(side=TOP)
rotor_r_viewable.create_rectangle(15,15,35,50, fill="#b67057")
rotor_r_viewable.create_text((25,33),text=machine.get_right_rotor_pos(), tags='rotor_r')

right_rotor_frame.pack(side=LEFT)

## Switchboard Frame
switchboard_frame = Frame(top_frame)

switchboard_middle_frame = Frame(switchboard_frame)

switchboard_text = Label(switchboard_middle_frame, text="Open Switchboard")
switchboard_text.pack(side=TOP)

switchboard_button = Button(switchboard_middle_frame, text="Switchbaord", command=open_switchboard_window)
switchboard_button.pack(side=TOP)

switchboard_middle_frame.pack(side=LEFT)
switchboard_frame.pack(side=LEFT)



# Output frame

output = Frame(root)
output.pack(side=TOP)

## Top row

output_top = Frame(output)
output_top.pack(side=TOP)

### Q light
q_canvas = Canvas(output_top, width=100, height=100)
q_canvas.pack(side=LEFT)
q_canvas.create_oval(40,40,60,60, fill=on_off_setting['Q'], tags='Q')
q_canvas.create_text((50,50),text='Q')

### W light
w_canvas = Canvas(output_top, width=100, height=100)
w_canvas.pack(side=LEFT)
w_canvas.create_oval(40,40,60,60, fill=on_off_setting['W'], tags='W')
w_canvas.create_text((50,50),text='W')

### E light
e_canvas = Canvas(output_top, width=100, height=100)
e_canvas.pack(side=LEFT)
e_canvas.create_oval(40,40,60,60, fill=on_off_setting['E'], tags='E')
e_canvas.create_text((50,50),text='E')

### R light
r_canvas = Canvas(output_top, width=100, height=100)
r_canvas.pack(side=LEFT)
r_canvas.create_oval(40,40,60,60, fill=on_off_setting['R'], tags='R')
r_canvas.create_text((50,50),text='R')

### T light
t_canvas = Canvas(output_top, width=100, height=100)
t_canvas.pack(side=LEFT)
t_canvas.create_oval(40,40,60,60, fill=on_off_setting['T'], tags='T')
t_canvas.create_text((50,50),text='T')

### Z light
z_canvas = Canvas(output_top, width=100, height=100)
z_canvas.pack(side=LEFT)
z_canvas.create_oval(40,40,60,60, fill=on_off_setting['Z'], tags='Z')
z_canvas.create_text((50,50),text='Z')

### U light
u_canvas = Canvas(output_top, width=100, height=100)
u_canvas.pack(side=LEFT)
u_canvas.create_oval(40,40,60,60, fill=on_off_setting['U'], tags='U')
u_canvas.create_text((50,50),text='U')

### I light
i_canvas = Canvas(output_top, width=100, height=100)
i_canvas.pack(side=LEFT)
i_canvas.create_oval(40,40,60,60, fill=on_off_setting['I'], tags='I')
i_canvas.create_text((50,50),text='I')

### O light
o_canvas = Canvas(output_top, width=100, height=100)
o_canvas.pack(side=LEFT)
o_canvas.create_oval(40,40,60,60, fill=on_off_setting['O'], tags='O')
o_canvas.create_text((50,50),text='O')

## Middle row

output_middle = Frame(output)
output_middle.pack(side=TOP)

### A light
a_canvas = Canvas(output_middle, width=100, height=100)
a_canvas.pack(side=LEFT)
a_canvas.create_oval(40,40,60,60, fill=on_off_setting['A'], tags='A')
a_canvas.create_text((50,50),text='A')

### S light
s_canvas = Canvas(output_middle, width=100, height=100)
s_canvas.pack(side=LEFT)
s_canvas.create_oval(40,40,60,60, fill=on_off_setting['S'], tags='S')
s_canvas.create_text((50,50),text='S')

### D light
d_canvas = Canvas(output_middle, width=100, height=100)
d_canvas.pack(side=LEFT)
d_canvas.create_oval(40,40,60,60, fill=on_off_setting['D'], tags='D')
d_canvas.create_text((50,50),text='D')

### F light
f_canvas = Canvas(output_middle, width=100, height=100)
f_canvas.pack(side=LEFT)
f_canvas.create_oval(40,40,60,60, fill=on_off_setting['F'], tags='F')
f_canvas.create_text((50,50),text='F')

### G light
g_canvas = Canvas(output_middle, width=100, height=100)
g_canvas.pack(side=LEFT)
g_canvas.create_oval(40,40,60,60, fill=on_off_setting['G'], tags='G')
g_canvas.create_text((50,50),text='G')

### H light
h_canvas = Canvas(output_middle, width=100, height=100)
h_canvas.pack(side=LEFT)
h_canvas.create_oval(40,40,60,60, fill=on_off_setting['H'], tags='H')
h_canvas.create_text((50,50),text='H')

### J light
j_canvas = Canvas(output_middle, width=100, height=100)
j_canvas.pack(side=LEFT)
j_canvas.create_oval(40,40,60,60, fill=on_off_setting['J'], tags='J')
j_canvas.create_text((50,50),text='J')

### K light
k_canvas = Canvas(output_middle, width=100, height=100)
k_canvas.pack(side=LEFT)
k_canvas.create_oval(40,40,60,60, fill=on_off_setting['K'], tags='K')
k_canvas.create_text((50,50),text='K')

## Bottom row

output_bottom = Frame(output)
output_bottom.pack(side=TOP)

### P light
p_canvas = Canvas(output_bottom, width=100, height=100)
p_canvas.pack(side=LEFT)
p_canvas.create_oval(40,40,60,60, fill=on_off_setting['P'], tags='P')
p_canvas.create_text((50,50),text='P')

### Y light
y_canvas = Canvas(output_bottom, width=100, height=100)
y_canvas.pack(side=LEFT)
y_canvas.create_oval(40,40,60,60, fill=on_off_setting['Y'], tags='Y')
y_canvas.create_text((50,50),text='Y')

### X light
x_canvas = Canvas(output_bottom, width=100, height=100)
x_canvas.pack(side=LEFT)
x_canvas.create_oval(40,40,60,60, fill=on_off_setting['X'], tags='X')
x_canvas.create_text((50,50),text='X')

### C light
c_canvas = Canvas(output_bottom, width=100, height=100)
c_canvas.pack(side=LEFT)
c_canvas.create_oval(40,40,60,60, fill=on_off_setting['C'], tags='C')
c_canvas.create_text((50,50),text='C')

### V light
v_canvas = Canvas(output_bottom, width=100, height=100)
v_canvas.pack(side=LEFT)
v_canvas.create_oval(40,40,60,60, fill=on_off_setting['V'], tags='V')
v_canvas.create_text((50,50),text='V')

### B light
b_canvas = Canvas(output_bottom, width=100, height=100)
b_canvas.pack(side=LEFT)
b_canvas.create_oval(40,40,60,60, fill=on_off_setting['B'], tags='B')
b_canvas.create_text((50,50),text='B')

### N light
n_canvas = Canvas(output_bottom, width=100, height=100)
n_canvas.pack(side=LEFT)
n_canvas.create_oval(40,40,60,60, fill=on_off_setting['N'], tags='N')
n_canvas.create_text((50,50),text='N')

### M light
m_canvas = Canvas(output_bottom, width=100, height=100)
m_canvas.pack(side=LEFT)
m_canvas.create_oval(40,40,60,60, fill=on_off_setting['M'], tags='M')
m_canvas.create_text((50,50),text='M')

### L light
l_canvas = Canvas(output_bottom, width=100, height=100)
l_canvas.pack(side=LEFT)
l_canvas.create_oval(40,40,60,60, fill=on_off_setting['L'], tags='L')
l_canvas.create_text((50,50),text='L')

bot_frame = Frame(root)
bot_frame.pack(side = BOTTOM)
reset_button = Button(bot_frame, text='Reset', fg='Green', command= lambda m=machine: reset_default(m))
reset_button.pack(side = RIGHT)

quit_button = Button(bot_frame, text="Quit", fg='Green', command=quit)
quit_button.pack(side = LEFT)

# Sentence ouput frame

sentence = Frame(root)
sentence.pack(side=TOP)

description = Frame(sentence)
description.pack(side=LEFT)

desc_text = Label(description, text="Sentence Output: ", relief=SUNKEN)
desc_text.pack()

sent_output_str = StringVar(desc_text)
sent_output = Label(description, textvariable=sent_output_str, relief=SUNKEN)
sent_output.pack(side=LEFT)


def key_pressed(event):
    encoded = machine.full_encode(event.char.upper())
    sent_output_str.set(sent_output_str.get() + encoded)

    rotor_l_viewable.itemconfig('rotor_l', text=machine.get_left_rotor_pos())
    rotor_m_viewable.itemconfig('rotor_m', text=machine.get_middle_rotor_pos())
    rotor_r_viewable.itemconfig('rotor_r', text=machine.get_right_rotor_pos())

    for x in on_off_setting:
        on_off_setting[x] = 'grey'
    on_off_setting[encoded] = 'yellow'

    q_canvas.itemconfig('Q', fill=on_off_setting['Q'])
    w_canvas.itemconfig('W', fill=on_off_setting['W'])
    e_canvas.itemconfig('E', fill=on_off_setting['E'])
    r_canvas.itemconfig('R', fill=on_off_setting['R'])
    t_canvas.itemconfig('T', fill=on_off_setting['T'])
    z_canvas.itemconfig('Z', fill=on_off_setting['Z'])
    u_canvas.itemconfig('U', fill=on_off_setting['U'])
    i_canvas.itemconfig('I', fill=on_off_setting['I'])
    o_canvas.itemconfig('O', fill=on_off_setting['O'])
    a_canvas.itemconfig('A', fill=on_off_setting['A'])
    s_canvas.itemconfig('S', fill=on_off_setting['S'])
    d_canvas.itemconfig('D', fill=on_off_setting['D'])
    f_canvas.itemconfig('F', fill=on_off_setting['F'])
    g_canvas.itemconfig('G', fill=on_off_setting['G'])
    h_canvas.itemconfig('H', fill=on_off_setting['H'])
    j_canvas.itemconfig('J', fill=on_off_setting['J'])
    k_canvas.itemconfig('K', fill=on_off_setting['K'])
    p_canvas.itemconfig('P', fill=on_off_setting['P'])
    y_canvas.itemconfig('Y', fill=on_off_setting['Y'])
    x_canvas.itemconfig('X', fill=on_off_setting['X'])
    c_canvas.itemconfig('C', fill=on_off_setting['C'])
    v_canvas.itemconfig('V', fill=on_off_setting['V'])
    b_canvas.itemconfig('B', fill=on_off_setting['B'])
    n_canvas.itemconfig('N', fill=on_off_setting['N'])
    m_canvas.itemconfig('M', fill=on_off_setting['M'])
    l_canvas.itemconfig('L', fill=on_off_setting['L'])

    print(repr(event.char).upper(), "pressed")

for key in "abcdefghijklmnopqrstuvwxyz":
    root.bind(key, key_pressed)

def space_pressed(event):
    sent_output_str.set(sent_output_str.get() + " ")


root.bind('<space>', space_pressed)

root.mainloop()