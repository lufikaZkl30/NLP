# berbeda

# from textblob import Word

# def spell_correction(sentence):
#     corrected_sentence = []
#     words = sentence.split()
#     for word in words:
#         corrected_word = Word(word).correct()
#         corrected_sentence.append(str(corrected_word))
#     return ' '.join(corrected_sentence)

# # Contoh pemanggilan fungsi 
# input_sentence = "Thiss is a sample sentance with some misspelled words."
# corrected_sentence = spell_correction(input_sentence)
# print("Input Sentence:", input_sentence)
# print("Corrected Sentence:", corrected_sentence)



# fix 
from textblob import TextBlob

text = input("Enter Text: \n")
text = text.split(" ")
correctText = " "

for i in text:
    correctWord = TextBlob(i)
    correctText += str(correctWord.correct()) + " "

print("Correct Spelling is: ") 
print(correctText) 


