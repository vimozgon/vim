pool = list(range(1,10))

def make_pool(pool):
  print("-------------")
  for i in range(3):
    print("|",pool[0+i*3],"|",pool[1+i*3],"|",pool[2+i*3],"|")
    print("-------------")

def take_input(player_inp):
  valid = False
  while not valid:
   pl_answer = input("Делай ход " + player_inp+"? ")
   try:
     pl_answer = int(pl_answer)
   except:
     print ("Неверный ввод..., уверен, что это число?")
     continue
   if pl_answer >= 1 and pl_answer <= 9:
    if (str(pool[pl_answer-1]) not in "XO"):
      pool[pl_answer-1] = player_inp
      valid = True
    else:
        print ("Поле уже занято, попробуй другое!")
   else:
      print ("Не верно, попробуй от 1 до 9")

def check_win(pool):
  win_coord = ((3,4,5),(0,1,2),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
  for each in win_coord:
    if pool[each[0]] == pool[each[1]]==pool[each[2]]:
      return pool[each[0]]
  return False

def main(pool):
  counter = 0
  win = False
  while not win:
    make_pool(pool)
    if counter %2==0:
      take_input("X")
    else:
     take_input ("O")
    counter +=1
    if counter >4:
      tmp=check_win(pool)
      if tmp:
        print (tmp,"Победа!")
        win = True
        break
    if counter == 9:
      print("Ничья!")
      break
  make_pool(pool)
main(pool)
input("\n\nНажми кнопку для завершения")
