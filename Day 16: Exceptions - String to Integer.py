S = input() 
result = '' 
try:     
    result = int(S) 
except ValueError: 
    result = 'Bad String' 
finally: print(result)
