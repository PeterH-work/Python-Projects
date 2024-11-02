
# map_of_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
import string
map_of_characters = string.ascii_uppercase + string.digits + "_"
list = [165,248,94,346,299,73,198,221,313,137,205,87,336,110,186,69,223,213,216,216,177,138]

for items in list:
    numbers = items % 37
    print(map_of_characters[numbers], end='')
     
#     if 0 <= numbers <=25:
#        print(map_of_characters[numbers])

#    elif 26 <= numbers <= 35:
#        print(map_of_characters[numbers])

#    elif numbers == 36:
#        print(map_of_characters[numbers])
