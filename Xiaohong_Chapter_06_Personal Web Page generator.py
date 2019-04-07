inputName = input("Entering your name:")
inputDescribe = input("Entering a sentence that describes yourself:")

outfile = open("personalWeb.html","w")

outfile.write("<html>"+'\n')
outfile.write("<head>"+'\n')
outfile.write("</head>"+'\n')
outfile.write("<body>"+'\n')
outfile.write("     <center>"+'\n')
outfile.write("     <h1>"+inputName+"</h1>"+'\n')
outfile.write("     </center>"+'\n')
outfile.write("     <hr/>"+inputDescribe+'\n')
outfile.write("     <hr/>"+'\n')
outfile.write("</body>"+'\n')
outfile.write("</html>"+'\n')

outfile.close()