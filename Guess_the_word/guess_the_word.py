


from os import path
from random import randint
from time import sleep

class Main():
    class Part:
        def __init__(self,obj,exists) -> None:
            self.obj= obj
            self.exists = exists
            
    def __init__(self,direct_path) -> None:
        try:
            with open(f"{direct_path}","r") as file:
                if path.getsize(direct_path) == 0:
                    
                    raise FileExistsError

                if path.exists(direct_path) == False:
                    raise FileNotFoundError
                
                self.words = file.readlines()
                
                self.words = map(lambda x : x.strip("\n"),self.words)
                self.words = list(self.words)
                    
        except FileExistsError:
            print("File is empty! ")
            exit()
        except FileNotFoundError:
            print("The file cannot be found")
            exit()

    
        self.man=["O","^","|","^"]

        self.body_parts=[self.Part(i,False) for i in self.man]

        self.secret_word = self.words[randint(0,len(self.words)-1)]

        self.all_digits = ["_" for i in range (len(self.secret_word))]
        self.used_letters = []
       

               
    def Drawing_the_dead(self):
        
        print("-"*7,end="")

        print()

        print("|",end="")

        print(" "*5,end="")

        print("|")



        for i in range(4):
            print("|",end="")

            print(" "*5,end="")
            if self.body_parts[i].exists == True:
                print(self.body_parts[i].obj)
            else:
                print()
        print("^")
    
    def Game_Controller(self,guessed):

        flag=False




        if "_" in self.all_digits:
            for i in range(len(self.secret_word)):
                if self.secret_word[i] == guessed:
                    self.all_digits[i] = guessed
                    flag=True

            if flag == False:
                
                for i in range(len(self.body_parts)):
                    if self.body_parts[i].exists == True:
                        continue
                    else:
                        self.body_parts[i].exists = True
                        break
                flag = True
        
            
            
            

                        
            
    def Name_the_letter(self):

        given = input("Guess the secret word by guessing every letter: ")
        
        given = str(given)
        given = given[0]

        while True:

            if given in self.used_letters:
                self.Drawing_the_dead()
                given = input("This letter has been already used, name another one: ")
                given = given[0]
            
            else:
                given = given[0]
                self.used_letters.append(given)
               
                break


        self.Game_Controller(given)
                
                

                
        
    def HUD(self):
        
        print()
        for i in self.body_parts:

            if i.exists == False:
                break
  
        else:
            print("You have losen the game")
            print(f"The secret word is {self.secret_word}")

            sleep(1)

            exit()

        for i in range(len(self.all_digits)):

            print(self.all_digits[i],end=" ")

        print()

        if "_" not in self.all_digits:

            print("You have guessed the secret word. Congratulation!!!")
            sleep(1)

            exit()
        print(f"Already used letter {self.used_letters}")
        self.Name_the_letter()
       
    
       

    def All_parts_present(self):
        for i in self.body_parts:
            if i.exists == False:
                return False
        return True




        
        
       




Game = Main(input("Give a global path: "))
while True: 
    Game.Drawing_the_dead()
    Game.HUD()

   

