# socket-based-connection

This is demo project using socket programming. In this project, client is in python and sever used django channels.

Client wil communicate to server and server will recieve request from client with **authentication** and server can send command to client for processing command.

It has two directory **cleint** and **server**. Server is django project using proper django-channels 2 with **authentication backend**.

For execution client-

Need to go inside client and run only python main.py.

For execution server-

Need to run django server and daphne worker.
