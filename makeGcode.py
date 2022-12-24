from PIL import Image
from tkinter.messagebox import showinfo
import os

def generate_Gcode(img_name):
    # Open the image file
    image = Image.open(img_name)

    # Convert the image to grayscale
    image = image.convert('L')

    # Define the width and height of the image in millimeters
    width, height = image.size
    width_mm = 152.4 / 10
    height_mm = 152.4 / 10

    # Calculate the pixel size in millimeters
    px_size_x = width_mm / width
    px_size_y = height_mm / height

    # Initialize the G-code commands
    gcode = []
    gcode.append("%")
    gcodeItterations = 1

    # Location Correction
    xCorrection = -1
    yCorrection = -1

# Black Pass
    for y in range(height):
        for x in range(width):
            # Get the pixel value (0-255)
            pixel = image.getpixel((x, y))

            # Check if pixel is white
            if pixel == 0:
                #Increase the Instuction Count
                gcodeItterations += 1

                # Calculate the position in millimeters
                pos_x = x * px_size_x
                pos_y = y * px_size_y

                # Get Location Corrections
                if xCorrection == -1:
                    if pos_x > 0:
                        xCorrection *= pos_x
                    else:
                        xCorrection = 0

                if yCorrection == -1:
                    if pos_y > 0:
                        yCorrection *= pos_y * 2 #Warning! This is a magic 2 to make the printer start in the -s' please remove if breaks on Y axis
                    else:
                        yCorrection = 0

                # Apply the location corrections
                pos_x = pos_x + xCorrection
                pos_y = pos_y + yCorrection

                # Generate a G-code command to move to the position and extrude material
                gcode.append(f"N{(gcodeItterations * 10) + 100} X{pos_x:.3f} Y{pos_y:.3f}")

    # Save the G-code commands to a file
    if os.path.exists(f"{img_name}BLACK.gcode"):
        os.remove(f"{img_name}BLACK.gcode")
    with open(f"{img_name}BLACK.gcode", 'w') as f:
        f.write('\n'.join(gcode))


# Gray Pass
    for y in range(height):
        for x in range(width):
            # Get the pixel value (0-255)
            pixel = image.getpixel((x, y))

            # Check if pixel is white
            if pixel == 127:
                #Increase the Instuction Count
                gcodeItterations += 1

                # Calculate the position in millimeters
                pos_x = x * px_size_x
                pos_y = y * px_size_y

                # Get Location Corrections
                if xCorrection == -1:
                    if pos_x > 0:
                        xCorrection *= pos_x
                    else:
                        xCorrection = 0

                if yCorrection == -1:
                    if pos_y > 0:
                        yCorrection *= pos_y * 2 #Warning! This is a magic 2 to make the printer start in the -s' please remove if breaks on Y axis
                    else:
                        yCorrection = 0

                # Apply the location corrections
                pos_x = pos_x + xCorrection
                pos_y = pos_y + yCorrection

                # Generate a G-code command to move to the position and extrude material
                gcode.append(f"N{(gcodeItterations * 10) + 100} X{pos_x:.3f} Y{pos_y:.3f}")

    # Save the G-code commands to a file
    if os.path.exists(f"{img_name}GRAY.gcode"):
        os.remove(f"{img_name}GRAY.gcode")
    with open(f"{img_name}GRAY.gcode", 'w') as f:
        f.write('\n'.join(gcode))

    showinfo(
        title='Selected Files',
        message="Generated G-CODE!"
    )