# To close the file automatically without calling the close() metho 

# with open(path_to_file) as f: ...

M=[]

def usefile(nameOfFile):
   nextWord=[]
   f=open(nameOfFile,'r')
   tmp_str=f.read()
   nextWord=tmp_str.split()
   f.close()
   return nextWord

if __name__=="__main__":
  M=usefile("db.txt")
  print(M)