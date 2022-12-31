from PIL import Image
from tkinter.messagebox import showinfo
import os

def passFilter(image, OrigenX, OrigenY, grade, size):
    #Get the original pixel
    pixel = image.getpixel((OrigenX, OrigenY))
    count = 0
    width, height = image.size
    if OrigenX + size > width:
        return False
    elif OrigenY + size > height:
        return False
    elif OrigenX - size < 0:
        return False
    elif OrigenY - size < 0:
        return False
    #Check each pixel in the range to match, if it does mark it
    for pos in range(1, size):
        if image.getpixel((OrigenX + pos, OrigenY)) == pixel:
            count += 1
        elif image.getpixel((OrigenX, OrigenY + pos)) == pixel:
            count += 1
        elif image.getpixel((OrigenX - pos, OrigenY)) == pixel:
            count += 1
        elif image.getpixel((OrigenX, OrigenY - pos)) == pixel:
            count += 1
    #if there are more correct sounding pixels than the grade return true
    if count >= grade:
        return True
    else:
        return False

def isEdge(image, OrigenX, OrigenY, color):
    if image.getpixel((OrigenX + 1, OrigenY)) == color and image.getpixel((OrigenX, OrigenY + 1)) == color and image.getpixel((OrigenX - 1, OrigenY)) == color and image.getpixel((OrigenX, OrigenY - 1)) == color:
        return False
    else:
        return True

def makeInstuctions(img_name, widthAjust, heightAjust, inputColor, edge):
    #Convert color to rgb
    color = (0,0,0)

    if inputColor == 0:
        color = (0,0,0)
    elif inputColor == 255:
        color = (255,255,255)
    elif inputColor == 127:
        color = (127,127,127)

    #Open the image file
    image = Image.open(img_name)

    #Define the width and height of the image in millimeters
    width, height = image.size
    width_mm = widthAjust / 10
    height_mm = heightAjust / 10

    #Calculate the pixel size in millimeters
    px_size_x = width_mm / width
    px_size_y = height_mm / height

    #Initialize the G-code commands
    gcode = []
    gcode.append("%")
    gcodeItterations = 1

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            #Check if the pixel is the correct color
            if pixel == color and (isEdge(image, x, y, color) or not edge):
                #Apply a low grade filter to see if it is surrounded by other pixels of the same color
                if (passFilter(image, x, y, 30, 48)):
                    #Apply location correction
                    gcodeItterations += 1
                    pos_x = x * px_size_x
                    pos_y = y * px_size_y
                    #Generate a G-code command to move to the position and extrude material
                    gcode.append(f"N{(gcodeItterations * 10) + 100} X{pos_x:.3f} Y{pos_y:.3f}")

    # Save the G-code commands to a file
    colorName = ""
    if color == (0,0,0):
        colorName = "Black"
    elif color == (255,255,255):
        colorName = "White"
    elif color == (127,127,127):
        colorName = "Gray"

    if os.path.exists(f"{img_name}{colorName}.gcode"):
        os.remove(f"{img_name}{colorName}.gcode")
    with open(f"{img_name}{colorName}.gcode", 'w') as f:
        f.write('\n'.join(gcode))
    showinfo(
        title='Sucess!',
        message="Generated G-CODE!"
    )

