def locate_card(cards,query):
    #create variable position with the value 0
    position=0

    #set up a loop for repetition
    while True:
        #check  if element at the current position match the query
        if cards[position] == query:
            #answer found! return and exit
            return position
        #increase the position
        position += 1
    
        #check if we have reached the end of the array
        if position == len(cards):
        #number not found, return 1
             return -1
    

cards=[13,11,10,7,4,3,2,1]
query=7
output=3
locate_card(cards,query)

test={
    'input':{
        'cards':[13,11,10,7,4,3,2,1],
        'query':7
    },
    'output':3
}
print(test)
result=locate_card(test['input']['cards'],test['input']['query'])    #test['input']['card'],test['input']['query']   = **test['input']

print(result)
print(result==output)



#print(test)
