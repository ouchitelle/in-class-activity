#Opens a file
with open("numbers.html", "w") as f:
    #write to file
    f.write("<html>\n<head>\n<title>List of Numbers</title>\n</head>\n<body>\n")
    f.write("<table>\n<tr><th>Even Numbers</th><th>Odd Numbers</th></tr>\n")
    #loop
    for i in range(1, 50):
        if i % 2 == 0:
            #write this if even
            g.write("<tr><td>{}</td><td></td></tr>\n".format(i))
        if i % 3 == 0:
            #write this if multiple of three
            g.write("<tr><td></td><td>{}</td></tr>\n".format(i))
            #write this at end
    f.write("</table>\n</body>\n</html>")

#write to this file
with open("numbers.html"") as f:
          #read the file
    print(f.read())
    
