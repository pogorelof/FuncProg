list_of_kiril = ['А','Ә','Б','В','Г','Ғ','Д','Е','Ё','Ж','З','И','Й','К',
                'Қ','Л','М','Н','Ң','О','Ө','П','Р','С','Т','У','Ұ','Ү','Ф','Х','Һ',
                'Ц','Ш','Щ','Ы','І', 'Э', 'Я']
list_of_kiril_lowercase = [letter.lower() for letter in list_of_kiril]

list_of_latin = ['А','Ä','B','V','G','Ğ','D','E','E','J','Z','I','I','K',
                'Q','L','M','N','Ñ','O','Ö','P','R','S','T','U','Ū','Ü','F','H','H',
                'C','Ş','Ş','Y','I', 'E', 'YA']
list_of_latin_lowercase = [letter.lower() for letter in list_of_latin]

kazakh_text = '''«Оғыз қаған» дастаны – түркітектес халықтардың ежелгі шежіресін генеологиялық 
аңыздар негізінде көркем тілмен баяндайтын эпостық туынды. «Оғыз» сөзінің мағынасы уыз, уыздас, 
сүттес, емшектес, яғни бір анадан сүт емген деген мағынаны береді. Ежелгі ғұндардың ұрпақтары «Оғыз» 
сөзін тайпалардың бірлестігі, одағы деген мағынада қолданған.'''

print('Текст на кириллице: ')
print(kazakh_text)
kazakh_text = list(kazakh_text)

kazakh_text_str = ''
for i in range(len(kazakh_text)):
    if kazakh_text[i] in list_of_kiril:
        index = list_of_kiril.index(kazakh_text[i])
        kazakh_text[i] = list_of_latin[index]
    if kazakh_text[i] in list_of_kiril_lowercase:
        index = list_of_kiril_lowercase.index(kazakh_text[i])
        kazakh_text[i] = list_of_latin_lowercase[index]
    kazakh_text_str += kazakh_text[i]

print('\nТекст на латинице: ')
print(kazakh_text_str)