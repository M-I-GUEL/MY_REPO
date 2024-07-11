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
Exam_count = 0
no_question = 0
for question in EXAM:
    print(question['question'])
    print(question['options'])

    answer =input('\nEnter your answer:').capitalize()
    no_question+=1
    if answer == question['ANS']:
        Exam_count+=1
    else:
        pass

print(f'\nYour score is {Exam_count}/{no_question}')