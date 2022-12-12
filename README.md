# pisschat
pissy TCP chat client/server made with wxpython

# server
run server.py to run a server that both wxpython and terminal clients can connect to, you can use ngrok or port forward ur stuff to make it available for other people

# clients
pisschat-client-wx contains a cross-platform GUI client made with wxpython, there are also pre-compiled binaries for amd64 linux and windows because i forgot to leave them out when i published this
you can also use the terminal-client.py which has the same functionality as the wxpython version (to change your name type !set-name \[name])

the wxpython version looks something like this (on linux at least, on windows it will use native windows calls will make it look v different)

![screenshot_079](https://user-images.githubusercontent.com/86350819/206936861-8fac56fd-b234-4e2a-869b-511c6b8aa2ff.png)

(dont mind the textbox on the upper right corner it's supposed to show a list of members but i havent gotten arround to implementing that yet)
