####  REGEX = REGULAR EXPRESSION
# 1. INTRODUCTION TO REGEX
# 2. SIMPLE CHARACTER MATCHES
# 3. CHARACTER CLASSES 
# 4. SPECIAL CHARACTERS
# 5. QUANTIFIERS 
# 6. SUBSTITUTING 
# 7. COMPILING REGULAR EXPRESSION
# 8. SPLIT FUNCTION 

import re

#QUANTIFIERS
text = 'a aa aaa aaaa aaaaa'
pattern = r'a*' #extract for matches of 0 or more
print(re.findall(pattern,text))

pattern=r'a+' # extract for matches of 1 or more
print(re.findall(pattern,text))

pattern=r'a{3}' # extract for matches of3 occurence
print(re.findall(pattern,text))

pattern=r'a{4}' # extract for matches of 4 occurance
print(re.findall(pattern,text)) #to make it show 4 or more is to add a comma at the endof the number ie {4,}

pattern=r'a{6}' # extract for matches of 6 occurance.
print(re.findall(pattern,text)) #this would bring out none []

pattern=r'a{2,4}' # extract for matches between 2 to 4 
print(re.findall(pattern,text))



########  SUBSTITUTION
text = 'Daniel and Marvelous are friends'
pattern ='friends' #word we are trying to substitute
output =re.sub(pattern,'opps', text)
print(output)



########  COMPILING REGULAR EXPRESSION
text ="C"
pattern= '[0-9]'
print(re.findall(pattern,text))

text ="there are 10 apples and 20 oranges"
pattern= '\d+'
print(re.findall(pattern,text))

#########  CODE REUSABILITY
pattern=re.compile('\d+')
daniel_text = "there are 10 apples, 30 mangoes and 20 oranges "
output=pattern.findall(daniel_text)
print(output)


##### RANDOM EXPLANATION
text='there are 10 apples and 20 oranges'
pattern='[a-zA-Z]'# to make the mubojumbo letters make sense to words add +sign [a-zA-Z]
print(re.findall(pattern,text))

text='there are 10 apples and 20 oranges'
pattern='[\w]'# to extract letters and numbers, adding +sign makes it into word
print(re.findall(pattern,text))


########  SPLIT FUNCTION
text='Split this text for me right away'
pattern=r'\s+' #split with respect to white spaces , adding +sign splits it in words
output =re.split(pattern, text)
print(output)
print(text.split('t'))# this would remove t from the texts

