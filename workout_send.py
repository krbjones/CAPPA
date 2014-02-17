# THIS PART PARSES THROUGH THE GARMIN XML WORKOUT FILE
from xml.dom import minidom

xmldoc = minidom.parse("garmin.xml")
dbase = xmldoc.getElementsByTagName("TrainingCenterDatabase")[0]
lap = dbase.getElementsByTagName("Lap")[0]
StartTime = dbase.getElementsByTagName("Id")[0].firstChild.data
TotTime = lap.getElementsByTagName("TotalTimeSeconds")[0].firstChild.data
AvgHRval = lap.getElementsByTagName("Value")[0].firstChild.data
MaxHRval = lap.getElementsByTagName("Value")[1].firstChild.data

# Print results to the Python Shell Window
print ("<h1>Votre execise a commencer a: "+StartTime+"</h1><br>\n")
print ("<h1>Felicitation, la duree de votre session d'exercise etait: "+TotTime+ " secondes!"+"</h1><br>\n")
print ("<h1>Frequence cardiaque moyenne: "+AvgHRval+"</h1><br>\n")
print ("<h1>La frequence cardiaque maximale: "+MaxHRval+"</h1><br>\n")

#Write out the results to an HTML file
text_file = open("res_p2.html", "w")
text_file.write("<h1>Votre execise a commencer a: "+StartTime+"</h1><br>\n"+
                "<h1>Felicitation, la duree de votre session d'exercise etait: "+TotTime+ " secondes!"+"</h1><br>\n"+
                "<h1>Frequence cardiaque moyenne: "+AvgHRval+"</h1><br>\n"+
                "<h1>La frequence cardiaque maximale: "+MaxHRval+"</h1><br>\n")
text_file.close()


filenames = ['res_p1.html', 'res_p2.html','res_p3.html']
with open('resultats.html', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())


# FTP results to the Webserver
import ftplib
from ftplib import FTP 

File2Send = "resultats.html"
Output_Directory = "/public_html/cappa" 

ftp = FTP("ftp.ekoot.ca")
ftp.login("krbjones", "0Kl@h@m@") 
file = open(File2Send, "rb") 
ftp.cwd(Output_Directory)
ftp.storbinary('STOR ' + File2Send, file) 
print "STORing File now..." 
ftp.quit() 
file.close() 

