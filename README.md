# pisschat
pissy TCP chat client/server made with wxpython

# server
run server.py to run a server that both wxpython and terminal clients can connect to, you can use ngrok or port forwarding to make it available for other people

# clients
pisschat-client-wx contains a cross-platform GUI client made with wxpython

the code is organized into the "front end" and "back end" files, the first one containing only code having to do with wxpython GUI stuff while the second one has actual client-side TCP socket stuff, this makes the code more modular i think (im trying my best)

there are also pre-compiled binaries for amd64 linux and windows because i forgot to leave them out when i published this

you can also use the terminal-client.py which has the same functionality as the wxpython version

# screenshots

the wxpython version looks something like this (on linux at least)

![screenshot_079](https://user-images.githubusercontent.com/86350819/206936861-8fac56fd-b234-4e2a-869b-511c6b8aa2ff.png)

(dont mind the textbox on the upper right corner it's supposed to show a list of members but i havent gotten arround to implementing that yet)

there's also the terminal version which looks like this

![screenshot_080](https://user-images.githubusercontent.com/86350819/206937223-8a4cd821-55c1-44c2-84f3-6d41c291ca42.png)
