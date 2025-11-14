from tkinter import messagebox, filedialog
import os

#select rom.nds
rom = filedialog.askopenfilename(title="Select a ROM", filetypes=(("NDS ROMs", "*.nds"), ("All files", "*.*")))
#read rom    
def read_rom_header(rom): 
    full_path = os.path.join(rom)
    with open(rom, "rb") as rom_file:
        header_data = rom_file.read(512)  # NDS header is typically 512 bytes
    title = header_data[12:15].decode("utf-8").rstrip('\x00')  # Title of the game
    print(title)
    #TAKE FIRST 3 LETTERS OF TITLE AND MAKE IT UPPERCASE
    title = title[0:8].upper()
    title = title.replace(" ", "")
    title = title.strip()  # Remove trailing spaces
    for i in title:
        #a = getvalue of i
        a = title.index(i)
        print(title[a])
    print(title)
    #check if title is in list1

    list1 = ["ADA", "APA", "CPU", "IPK", "IPG", "IRB", "IRA", "IRE", "IRD" ]
    list2 = ["diamond", "pearl", "platinum", "heartgold", "soulsilver", "black", "white", "black2", "white2"]
    print(f"list1:{list1}, list2:{list2}")
    # is title in list1?
    if title in list1:
        print("yes")
        #if yes, get index of title in list1
        index = list1.index(title)
        print(index)
        #get value of index in list2
        print(list2[index])
        #if no, print error
        
        
variable = "something"
print(variable)

