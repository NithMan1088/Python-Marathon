
# coding: utf-8

# In[ ]:


#Given a string of even length, return the first half. So the string "WooHoo" yields "Woo"

word = str(input("Enter a word/words: "))

print(word[:int((len(word))/2)])

