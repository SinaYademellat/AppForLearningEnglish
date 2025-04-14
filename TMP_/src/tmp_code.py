def usefile(nameOfFile:str = "db.txt"):
   nextWord=[]
   f=open(nameOfFile,'r')
   tmp_str=f.read()
   nextWord=tmp_str.split()
   f.close()
   return nextWord

# if __name__=="__main__":
#   M=[]
#   M=usefile("db.txt")
#   print(M)