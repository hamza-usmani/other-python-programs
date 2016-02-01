import zipfile 
import os, glob, sys

def main():
    todo= input("Zippy Tool: Hamza Usmani 2015 \n(1) Extract\n(2) Zip Files in a Directory\n")
    function_dict[todo]()
    
def zipup ():
    
    path= input ("Enter the folder directory here: ")
    file_type = input ("Enter file extension to zip: ")
    file_name = input ("Name your zip file: ")
    zip = zipfile.ZipFile("%s.zip" %file_name, 'w',zipfile.ZIP_DEFLATED) 
    os.chdir(path) 
    for file in glob.glob("*.%s" %file_type):
        zip.write(file)          
    
    zip.close()

def extract ():  
    path= input ("Enter the file's url here: ")
    zip = zipfile.ZipFile(path)
    zip.extractall()
    zip.close()
      
function_dict = {'1':extract, '2':zipup}		    
main()
