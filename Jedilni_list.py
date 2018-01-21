#-*- coding: utf-8 -*-
#Program za vnašanje dnevnega menija

menu_dict = {}

while True:
    ime_jedi = raw_input("Vnesi ime jedi: ")
    cena_jedi = float(raw_input("Vnesi ceno za jed %s:" % ime_jedi))
    menu_dict[ime_jedi] = cena_jedi
    nov_vnos = raw_input("Želite vnesti novo jed (da/ne)?")
    if nov_vnos == "ne":
        break

print menu_dict

menu_file = open("menu.txt", "w+")

menu_file.write("Dnevni menu:\n")
for item in menu_dict:
    menu_file.write("%s - %s EUR\n" % (item, menu_dict[item]))
menu_file.write("Vse cene vsebujejo DDV.")
menu_file.close()