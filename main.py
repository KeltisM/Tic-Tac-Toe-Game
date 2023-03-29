b={
  "1":" ","2":" ","3":" ",
  "4":" ","5":" ","6":" ",
  "7":" ","8":" ","9":" "
}
def printboard(b):
  print(b["1"]+"|"+b["2"]+"|"+b["3"])
  print("-+-+-")
  print(b["4"]+"|"+b["5"]+"|"+b["6"])
  print("-+-+-")
  print(b["7"]+"|"+b["8"]+"|"+b["9"])
  
 

def game():
  turn="X"
  count=0
  for i in range(9):
    print(turn,"your turn")
    printboard(b)
    a=input("enter the position \n")
    if b[a]  == " ":
      b[a]=turn
      count=count+1
    else:
      print("this position is filled")
      continue
    if count>=5:
      if(b["1"]and b["2"]and b["3"])!=" ":
         print(turn,"wins")
         
         printboard(b)
         break
      elif(b["4"]==b["5"]==b["6"])!=" ":
         print(turn,"wins")
         
         printboard(b)
         break
      elif(b["7"]==b["8"]==b["9"])!=" ":
         print(turn,"wins")
         
         printboard(b) 
         break
      elif(b["1"]==b["4"]==b["7"])!=" ":
         print(turn,"wins")
         
         printboard(b)
         break
      elif(b["2"]==b["5"]==b["8"])!=" ":
         print(turn,"wins")
         
         printboard(b)
         break
      elif(b["3"]==b["6"]==b["9"])!=" ":
         print(turn,"wins")
         
         printboard(b)
         break
      elif(b["1"]==b["5"]==b["9"])!=" ":
         print(turn,"wins")
         printboard(b) 
         break
      elif(b["3"]==b["5"]==b["7"])!=" ":
         print(turn,"wins")
         
         printboard(b)
         break


        
    if turn=="X":
      turn="O"
    else:
      turn="X"
    if count==9:
      print("game over its a draw")
      
game()
  
