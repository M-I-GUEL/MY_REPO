import telebot

API_TOKEN ='7442229134:AAGvMeYrniiV6v1bUol4qBKgzRO7RTYQhXw'
bot = telebot.TeleBot(API_TOKEN)
EXAM = [{'question': 'which of these countries have NOT won the world cup before',
         'options' : {'A': 'USA',
                      'B':'Brazil',
                      'C':'Uruguay',
                      'D':'England'
                      },

          'ANS':'A'},

          {'question':'WAUG stands for',
           'options' : {'A':'West Africa Universities Games',
                        'B':'west African Universities Games',
                        'C':'west African University Games',
                        'D':'west African Universities Game'
                        },

            'ANS' : 'C'
              
            },

            {'question':'The first WAUG was in the year',
             'options' : {'A':'1965',
                          'B':'1971',
                          'C':'1999',
                          'D':'1987'
                          },
        
             
             'ANS' : 'A'},

            {'question':'Which of these is not a planet',
              'options' : {'A':'Earth',
                           'B':'Neptune',
                           'C':'Jupitar',
                           'D':'Pluto'
                           },

               'ANS' : 'D'},


            {'question':'Which of these is the most populolus country',
                'options' : {'A':'Russia',
                             'B':'Nigeria',
                             'C':'India',
                             'D':'China'
                              },

                'ANS' : 'D'},




            {'question':'The capital of Mali is',
                 'options' : {'A':'Bamako',
                              'B':'Mozambique',
                              'C':'Namibia',
                              'D':'Tripoli'
                             },
                 'ANS' : 'A'},



             {'question':'The first female african president was from',
              'options' : {'A':'Sierra-leone',
                           'B':'Gambia',
                           'C':'Cameroon',
                           'D':'Liberia'
                           },
              
              'ANS' : 'D'},


             {'question':'largest country in africa?',
              'options' : {'A':'Nigeria',
                           'B':'Sudan',
                           'C':'Egypt',
                           'D':'Namibia'
                           },
              
              'ANS' : 'B'},



             {'question':'Chukwuemeka Ojukwu was born in?',
              'options' : {'A':'Kotongora',
                           'B':'Nnewi',
                           'C':'Zungeru',
                           'D':'Kaduna'
                           },
              
              'ANS' : 'C'},




             {'question':'The official money spent in australia is?',
              'options' : {'A':'Dollar',
                           'B':'Euro',
                           'C':'Cedi',
                           'D':'pound'
                           },
              
              'ANS' : 'D'},



             {'question':'Which of these is the smallest continent?',
              'options' : {'A':'Asia',
                           'B':'Europe',
                           'C':'Australia',
                           'D':'Africa'
                           },
              
              'ANS' : 'C'},



             {'question':'Which of these does not belong to the group',
              'options' : {'A':'Dog',
                           'B':'Goat',
                           'C':'Rat',
                           'D':'Hen'
                           },
              
              'ANS' : 'D'},


             {'question':'The process of making beer is called?',
              'options' : {'A':'Brewing',
                           'B':'Browning',
                           'C':'Bearing',
                           'D':'Boring'
                           },
              
              'ANS' : 'A'},


             {'question':'The rainbow has how many colours?',
              'options' : {'A':'5',
                           'B':'6',
                           'C':'8',
                           'D':'7'
                           },
              
              'ANS' : 'D'},


             {'question':'Which of the professionals travel into space?',
              'options' : {'A':'Pilots',
                           'B':'Divers',
                           'C':'Astronauts',
                           'D':'Space wagon'
                           },
              
              'ANS' :'C'}
              
              
]

candidate_score = {}



@bot.message_handler(commands=['start','quiz'])
def handle_start_messages(message):
     candidate_id = message.chat.id
     global candidate_score
     candidate_score[candidate_id] = {'current_question_index': 0, 'score': 0}
     send_question_response(message)
     
    



def send_question_response(message):
     global candidate_score
     candidate_id = message.chat.id
     print(candidate_score[candidate_id])
     print(candidate_id)
     print(candidate_score)
     question_number = candidate_score[candidate_id]['current_question_index']
     candidate_score[candidate_id]['current_question_index'] += 1
     print(candidate_score)
    
     options=EXAM[question_number]['options']
     question_and_answer= EXAM[question_number]['question']+'\n'+'A.'+ options['A']+'\n'+'B.'+ options['B']+'\n'+'C.'+ options['C']+'\n'+'D.'+ options['D']
     bot.reply_to(message, question_and_answer)
     

    

@bot.message_handler(func=lambda message: True)
def handle_response(message):
    global candidate_score
    candidate_id = message.chat.id

#this will tell the user that his/her exam has ended once he/she surpasses the given amount of question in our EXAM list
    question_number = candidate_score[candidate_id]['current_question_index']
    if question_number>=len(EXAM):
        user = message.from_user
        first_name = user.first_name
        bot.reply_to(message,f'{first_name} YOUR EXAM HAS ENDED!\nyour score is\n { candidate_score[candidate_id]['score']}/{len(EXAM)}\nkindly send /start to try again.\nThank you')
        return



    
#changes the user input to capital letter     
    answer = message.text.upper()
# retrieves the 'current question index' from our question_number variable which can be used to compare the user's input with the correct answer from the EXAM list 

    
    correct_option = EXAM[question_number]['ANS']
    opt =  EXAM[question_number]['options']
    


#sends the user a message after completing the questions from the EXAM list

   
#this helps us check if the user input is among our EXAM options
    
    if answer in opt.keys():
         send_question_response(message)
    

#increases the user score if the user input is == correct_option
         if answer == correct_option:
             candidate_score[candidate_id]['score']+=1
             candidate_score[candidate_id]['current_question_index']+1
             
         elif answer != correct_option: 
              candidate_score[candidate_id]['current_question_index']+1
         else:
              pass
            
    else:
            user = message.from_user
            first_name = user.first_name
            bot.reply_to(message,f'Hi {first_name} kindly insert any of the options:\n[A,B,C or D]')
        
         



    
bot.infinity_polling()

