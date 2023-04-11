from recognizers_number import recognize_number, recognize_ordinal, recognize_percentage, Culture
from recognizers_number_with_unit import recognize_age, recognize_currency, Culture

text = open('C:\\text.txt', 'r')

# results - набор найденных чисел
results = recognize_number(text.read(), Culture.English)
 
for result in results:
    print(f"Распознанный текст: {result.text}")
    print(f"Расспознаное значение: {result.resolution['value']}")

text.close()

#нахождение порядковых чисел
results = recognize_ordinal('The fifth book', Culture.English)
 
for result in results:
    print(result.resolution["value"]) 

#нахождение процентов в тексте
results = recognize_percentage("sixty-seven percents", Culture.English)
 
for result in results:
    print(result.resolution["value"])  

#нахождение возраста в тексте
results = recognize_age("Tom is thirty-eight years old\nshe with her twenty two years of age", Culture.English)
 
for result in results:
    print(result.resolution["value"])  
 

#распознование валют
results = recognize_currency("the sum was $ 15.4 million", Culture.English)
 
for result in results:
    print(result.resolution["value"])  