import removebg   # We can make API of Removebg on my own
from rembg import remove
import easygui
from PIL import Image
# Open and Save File
inputFile = easygui.fileopenbox("Select ay File.....")
Outfile =   easygui.filesavebox("Save File")
# Take image as input
input = Image.open(inputFile)
output = remove(input)
# Save the Output
output.save(Outfile)
