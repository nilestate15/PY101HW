#Week 2 HW1
#Niles Tate


#Problem 3
#Input function
def MK_choose(characters):
    #Number of inputs
    fighters = 2
    #opens file and writes to it
    o = open(characters, "w")
    for i in range(fighters):
        p1_choose = input("Please choose character")
        #enters users input into file
        o.write(p1_choose + "\n")
    o.close()
#Append function
def MK_chosen(characters):
    #opens file to add new text
    o = open(characters, "a")
    #adds this string to file
    o.write("Characters chosen" + "\n")
    o.close()
#Module being run standalone by user
if __name__ == "__main__":
    characters = "MKcharacters.txt"
    #Call functions
    MK_choose(characters)
    MK_chosen(characters)
