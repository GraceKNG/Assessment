from tkinter import *
import random

names_list= []
global questions_answers
asked = []

questions_answers = {
    1: ["What is the meaning of Aotearoa", 'land of sheep', 'land of New Zealand','land of milk and honey','land of long white clouds','land of long white clouds',4],
    2: ["When was New Zealand discovered", '1935', '1653','1642', '1762','1642', 3],   
    3: ["What is the line for emergency services?", '911', '199', '111','104','111',3],
    4: ["Who is the current prime minister?", 'Barack Obama', 'Jacinda Adern','John key', 'Bee','Jacinda Adern',2],
    5: ["How tall is the Sky Tower", '328m', '327m', '326m', '325m','328m',1]     
}

def randomiser():
    global qnum
    qnum = random.randint(1,5)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()


class QuizStarter:
    def __init__(self, parent):
        background_color = "pink"
        self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()
        
        self.heading_label = Label (self.quiz_frame, text = "NZ History Quiz", font=("Tw Cen MT", "18", "bold"), bg=background_color)
        self.heading_label.grid(row=0)
        
        self.user_label = Label (self.quiz_frame, text = "Please enter your name in the box below", font=("Tw Cen MT", "16"), bg=background_color)
        self.user_label.grid(row=1, pady=20)
        
        self.entry_box = Entry (self.quiz_frame)
        self.entry_box.grid(row=2, pady=20)
             
        self.continue_button = Button (self.quiz_frame, text = "Continue", bg="white", font=("Tw Cen MT", "14"), command=self.name_collection)
        self.continue_button.grid(row=3, pady=20)
        
    def name_collection(self):
        name = self.entry_box.get()
        names_list.append(name)
        self.quiz_frame.destroy()
        Quiz(root)
        
class Quiz:
    
    def __init__(self, parent):
            background_color = "pink"
            self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
            self.quiz_frame.grid()
            
            randomiser()
            
            self.question_label = Label (self.quiz_frame, text = questions_answers[qnum][0], font=("Tw Cen MT", "18", "bold"), bg=background_color)
            self.question_label.grid(row=0, padx=10, pady=10)
            
            self.var1=IntVar()
            
            #radio button1
            self.rb1 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg=background_color, value=1,padx=10,pady=10,
                                    variable=self.var1, background = background_color)
            self.rb1.grid(row=1, sticky=W) 
            
            #radio button2
            self.rb2 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg=background_color, value=2,padx=10,pady=10,
                                    variable=self.var1,  background = background_color)
            self.rb2.grid(row=2, sticky=W)
            
            #radio button3
            self.rb3 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg=background_color, value=3,padx=10,pady=10,
                                    variable=self.var1,  background = background_color)
            self.rb3.grid(row=3, sticky=W)
            
            
            #radio button4
            self.rb4 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg=background_color, value=4,padx=10,pady=10,
                                    variable=self.var1,  background = background_color)
            self.rb4.grid(row=4, sticky=W) 
           
            
            #radio button5
            self.confirm_button = Button(self.quiz_frame, text="Confirm", bg="white", command=self.test_progress)
            self.confirm_button.grid(row=5)
                      
            self.score_label = Label(self.quiz_frame, text="SCORE", font=("Tw Cen Mt","16"),bg=background_color,)
            self.score_label.grid(row=6, pady=1)
            
    def questions_setup(self):
       randomiser()
       self.var1.set(0)
       self.question_label.config(text=questions_answers[qnum][0])
       self.rb1.config(text=questions_answers[qnum][1])
       self.rb2.config(text=questions_answers[qnum][2])
       self.rb3.config(text=questions_answers[qnum][3])
       self.rb4.config(text=questions_answers[qnum][4])

    def test_progress(self):
      global score
      score =0 
      scr_label = self.score_label
      choice = self.var1.get()
      if len(asked)>4: 
        if choice == questions_answers[qnum][6]:
          score +=1
          scr_label.configure(text=score)
          self.confirm_button.config(text="Confirm")
        else:
          score+=0
          scr_label.configure(text="The correct answer was " + questions_answers[qnum][5])
          self.confirm_button.config(text="Confirm")
      else:
        if choice==0:
          self.confirm_button.config(text="Try again please,you did not select anything")
          choice-self.var1.get()
        else:
          if choice==questions_answers[qnum][6]:
            score+=1
            scr_label.configure(text=score)
            self.confirm_button.config(text="Confirm")
            self.questions_setup()
          else:
            score+=0
            scr_label.configure(text="The correct answer was " + questions_answers[qnum][5])
            self.confirm_button.configure(text="Confirm")
            self.questions_setup()
        
                    
randomiser()     
if __name__ == "__main__":
    root =Tk()
    root.title("NZ History Quiz")
    quiz_instance = QuizStarter(root)
    root.mainloop()


