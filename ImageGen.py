import requests
import json
from io import BytesIO
from PIL import Image
import time
import sys


def remove_white_background(input_path, givenName):
    # Open the PNG image
    img = Image.open("./images/"+input_path)

    # Convert the image to RGBA if it's not already
    img = img.convert("RGBA")

    # Get the pixel data
    pixel_data = img.getdata()

    # Iterate through each pixel
    new_data = []
    treshold = 225
    for item in pixel_data:
        # Set the alpha channel to 0 for white pixels
        if item[0] > treshold and item[1] > treshold and item[2] > treshold:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    # Update the image with the new pixel data
    img.putdata(new_data)

    # Save the image with a transparent background
    img.save("./processed_images/" + givenName + ".png" , "PNG")

prompt = sys.argv[1].replace("_"," ")#input("Enter your tattoo idea: ")
print(prompt)
name = sys.argv[2]
headers = {'Content-type': 'application/json', "X-Dezgo-Key":"DEZGO-D419ED1700B5068E5B88617E29F438D9FA8C31247DA8B99F64157063DA50713A7BFA8CC4"}
body = { "prompt": "A tattoo design ONLY of{} on a plain white background, background R:255 B:255 G:255, without any surrounding elements such as a human".format(prompt) }
json_data = json.dumps(body)

response=requests.get("https://api.dezgo.com/text2image", data=json_data, headers=headers)

print(response.status_code)

if response.status_code == 200:
    print("amount: " + response.headers["x-dezgo-job-amount-usd"])
    print("credits remaining in dollars: " + response.headers["x-dezgo-balance-total-usd"])
    
    image_data = response.content
    image_stream = BytesIO(image_data)
    # Open the image using PIL (Python Imaging Library)
    img = Image.open(image_stream)

    path = "image_"+str(name)+".png"
    # Save the image to a file
    img.save("./images/"+path)
    print("Image saved successfully!")
    
    remove_white_background(path, name)
    print("Processed image saved successfully!")
    
