This is the part of My Final Year Project where the Raspberry Pi is implemented.
The use of a Connected Device was required for my Final Year project.
I chose the Raspberry Pi as it was a Connected Device I used the most in college.

The Pi has 2 Python scripts where I set up a server and connect to the client, and the Image Generation script.
Through the app(Client), When generated is clicked, the request is sent to the server.py.
The server.py gets the prompt and sends it to the ImageGen.py where it will request an image from a website.
The Image generates and processes and gets saved on the pi and sent back to the server.
The image is then sent back to the client(app).

*** Issues with connections between Client and Server on other networks at the moment. ***
