# f = open('File.txt','x') #Create a new file

# f = open('File.txt','w') #Open the file in write mode
# f.write("\nSabo") #Override the content
# f.write("\nAce")
# f.close()

# with open('File.txt','a') as f:#Open the file in append mode
#     f.write("\nAsfak") #Add end of the content
#     f.write("\nSanjai")
#
# f = open('File.txt','a')
# f.write("\nNitheesh") #Add end of the content
# f.write("\nArivu")
# f.close()

f = open('File.txt','r+')
content = f.read()
print(content)

# g = open('f.txt','x')
import os
if os.path.exists("f.txt"):
  os.remove("f.txt")
  print("Deleted")
else:
  print("The file does not exist")