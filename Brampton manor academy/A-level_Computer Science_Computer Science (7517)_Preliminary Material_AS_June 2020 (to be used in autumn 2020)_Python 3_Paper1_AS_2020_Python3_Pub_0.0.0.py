# Skeleton Program for the AQA AS1 Summer 2020 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA AS1 Programmer Team
# developed in a Python 3 environment

# Version number: 0.0.0
EMPTY_STRING = ""
MAX_WIDTH = 100
MAX_HEIGHT = 100

class FileHeader:
  def __init__(self):
    self.Title = EMPTY_STRING
    self.Width = MAX_WIDTH
    self.Height = MAX_HEIGHT
    self.FileType = EMPTY_STRING 

def DisplayError(ErrorMessage):
  """
     Parameters:string
     Description: It displays an error message
  """
  print("Error: ", ErrorMessage)

def PrintHeading(Heading):
  """
     Parameters:string
     Description: Prints the heading
  """
  print(Heading)
  HeadingLength = len(Heading)
  for Position in range(1, HeadingLength + 1):
    print('=', end='')
  print()

def DisplayImage(Grid, Header):
  """
     Parameters:list,object
     Description: Displays the Image 
  """
  print()
  PrintHeading(Header.Title)
  for ThisRow in range(Header.Height):
    for ThisColumn in range(Header.Width):
      print(Grid[ThisRow][ThisColumn], end='')
    print()



def SaveImage(Grid, Header):
  """
     Parameters:list,object
     Description: Saves the Image and tells you to choose the name of the file
  """
  print("The current title of your image is: " + Header.Title)
  Answer = input("Do you want to use this as your filename? (Y/N) ")
  if Answer == "N" or Answer == "n":
    FileName = input("Enter a new filename: ")
  else:
    FileName = Header.Title
  FileOut = open(FileName + ".txt", 'w')
  FileOut.write(Header.Title + '\n')
  for Row in range(Header.Height):
    for Column in range(Header.Width):
      FileOut.write(Grid[Row][Column])
    FileOut.write('\n')
  FileOut.close()

def EditImage(Grid, Header):
  """
   Parameters:list,object
   Return type:List
   Description:Edits the Image by replacing a symbol with a new one
  """

  DisplayImage(Grid, Header)
  Answer = EMPTY_STRING
  while Answer != "N":
    Symbol = EMPTY_STRING
    NewSymbol = EMPTY_STRING
    while len(Symbol) != 1:
      Symbol = input("Enter the symbol you want to replace: ")
    while len(NewSymbol) != 1:
      NewSymbol = input("Enter the new symbol: ")
    for ThisRow in range(Header.Height):
      for ThisColumn in range(Header.Width):
        if Grid[ThisRow][ThisColumn] == Symbol:
          Grid[ThisRow][ThisColumn] = NewSymbol
    DisplayImage(Grid, Header)
    Answer = input("Do you want to make any further changes? (Y/N) ")
  return Grid

def ConvertChar(PixelValue):
  """
   Parameters:integer
   Return type:string
   Description:Converts pixel values to Ascii
  """

  if PixelValue <= 32:
    AsciiChar = '#'
  elif PixelValue <= 64:
    AsciiChar = '&'
  elif PixelValue <= 96:
    AsciiChar = '+'
  elif PixelValue <= 128:
    AsciiChar = ';'
  elif PixelValue <= 160:
    AsciiChar = ':'
  elif PixelValue <= 192:
    AsciiChar = ','
  elif PixelValue <= 224:
    AsciiChar = '.'
  else:
    AsciiChar = ' '
  return AsciiChar

def LoadGreyScaleImage(FileIn, Grid, Header):
  """
   Parameters:File object,List,object
   Return type:List
   Description:Loads the greyscale image
  """
  try:
    for Row in range(Header.Height):
      for Column in range(Header.Width):
        NextPixel = FileIn.readline()
        PixelValue = int(NextPixel)
        Grid[Row][Column] = ConvertChar(PixelValue)
  except:
    DisplayError("Image data error")    
  return Grid
  
def LoadAsciiImage(FileIn, Grid, Header):
  """
   Parameters:File object,List,object
   Return type:List
   Description:Loads the Ascii image
  """
  
  try:
    ImageData = FileIn.readline()
    NextChar = 0
    for Row in range(Header.Height):
      for Column in range(Header.Width):
        Grid[Row][Column] = ImageData[NextChar]
        NextChar += 1
  except:
    DisplayError("Image data error")
  return Grid

def CompressFile():
  FileName=input("Enter the name of the file you want to be compressed")
  Fileread = open(FileName + ".txt", 'r')
  FileHeader=Fileread.readline()
  FileType=FileHeader.split(",")
  FileType[3]="C"
  LineOne=(f'{FileType[0]},{FileType[1]},{FileType[2]},{FileType[3]}')
  newFile=open("CMP"+FileName+".txt","w")
  newFile.write(LineOne+'\n')
  Line2=Fileread.readline()
  count=1
  for i in range(len(Line2)-1):
    if Line2[i]==Line2[i+1]:
      count+=1
    else:
      newFile.write(f"{count},{Line2[i]}")
      newFile.write("\n")
      count=1
  return newFile
      

  
  
    
    




  
  
  

  

  
  
def LoadFile(Grid, Header):
  """
   Parameters:List,object
   Return type:List,object
   Description:Loads the file you choose
  """

  FileFound = False
  FileTypeOK = False
  FileName = input("Enter filename to load: ")
  try:
    FileIn = open(FileName + ".txt", 'r')
    FileFound = True
    HeaderLine = FileIn.readline()
    Fields = HeaderLine.split(',')
    Header.Title = Fields[0]
    Header.Width = int(Fields[1])
    Header.Height = int(Fields[2])
    Header.FileType = Fields[3]
    Header.FileType = Header.FileType[0]
    if Header.FileType == 'A':  
      Grid = LoadAsciiImage(FileIn, Grid, Header)
      FileTypeOK = True
    elif Header.FileType == 'G': 
      Grid = LoadGreyScaleImage(FileIn, Grid, Header)
      FileTypeOK = True
    FileIn.close()
    if not FileTypeOK:
      DisplayError("Unknown file type")
    else:
      DisplayImage(Grid, Header)
  except:
    if not FileFound:
      DisplayError("File not found")
    else:
      DisplayError("Unknown error")
  return Grid, Header

def SaveFile(Grid, Header):
  """
   Parameters:List,object
   Description:Saves the file you choose
  """

  FileName = input("Enter filename: ")
  FileOut = open(FileName + ".txt", 'w')
  FileOut.write(Header.Title + ',' + str(Header.Width) + ',' + str(Header.Height) + ',' + 'A' + '\n')
  for Row in range(Header.Height):
    for Column in range(Header.Width):
      FileOut.write(Grid[Row][Column])
  FileOut.close()

def ClearGrid(Grid):
  """
   Parameters:List
   Return type:List
   Description:Clears the grid with a gird of full stops
  """
  
  for Row in range(MAX_HEIGHT):
    for Column in range(MAX_WIDTH):
      Grid[Row][Column] = '.'
  return Grid
   
def DisplayMenu():
  """
   Description:Displays the menu
  """
  
  print()
  print("Main Menu")
  print("=========")
  print("L - Load graphics file") 
  print("D - Display image")
  print("E - Edit image")
  print("S - Save image")
  print("C- Compress File")
  print("X - Exit program") 
  print()

def GetMenuOption():
  """
   Return type:String
   Description: It makes sure you input something otherwise it will ask again
  """

  MenuOption = EMPTY_STRING
  while len(MenuOption) != 1:
    MenuOption = input("Enter your choice: ")
  return MenuOption
  
def Graphics():
  """
   Description: It does wht you input so for example if you input s it will save the image
  """

  Grid = [['' for Column in range(MAX_WIDTH)] for Row in range(MAX_HEIGHT)]
  Grid = ClearGrid(Grid)
  Header = FileHeader()
  ProgramEnd = False
  while not ProgramEnd:
    DisplayMenu()
    MenuOption = GetMenuOption()
    if MenuOption == 'L':
      Grid, Header = LoadFile(Grid, Header)
    elif MenuOption == 'D':
      DisplayImage(Grid, Header)
    elif MenuOption == 'E':
      Grid = EditImage(Grid, Header) 
    elif MenuOption == 'S':    
      SaveImage(Grid, Header)
    elif MenuOption=='C':
      CompressFile()
    elif MenuOption == 'X':
      ProgramEnd = True
    else:
      print("You did not choose a valid menu option. Try again")
  print("You have chosen to exit the program")
  Answer = input("Do you want to save the image as a graphics file? (Y/N) ")
  if Answer == "Y" or Answer == "y":
    SaveFile(Grid, Header)
      
if __name__ == "__main__":
  Graphics()
  
  
