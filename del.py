# SUPPRIME LE FICHIER SUR LE SERVEUR
import ftplib
from ftplib import FTP 

File2Del = "resultats.html"
Output_Directory = "/public_html/ektejones.ca/cappa" 

ftp = FTP("hostname")
ftp.login("username", "password") 
file = open(File2Del, "rb") 
ftp.cwd(Output_Directory)
ftp.delete(File2Del) 
print "File resultats.html was deleted" 
ftp.quit() 
file.close() 

