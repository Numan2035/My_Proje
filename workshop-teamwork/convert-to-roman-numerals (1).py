
# convert the given number to the roman numerals
def convert(decimal_num):
    # set the dictionary for roman numerals
    roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
             50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    # initialize the result variable
    num_to_roman = ''
    # loop the roman numerals, calculate for each symbol and add to the result
    for i in roman.keys():
        num_to_roman += roman[i] * (decimal_num // i)
        decimal_num %= i
    return num_to_roman

# flag to show warning to the user, default is False.
is_invalid = False

# start endless loop to get user input continuously
while True:
    # info text to be shown to the user
    info = """
###  This program converts decimal numbers to Roman Numerals ###
(To exit the program, please type "exit")
Please enter a number between 1 and 3999, inclusively : """

    # get the user input after showing info text.
    # if is_invalid set to True then show additional warning to the user
    # pass the input the alphanum variable after stripping white space characters
    alphanum = input('\nNot Valid Input !!!\n'*is_invalid + info).strip()
    # if the input is not decimal number
    if not alphanum.isdecimal():
        # then check, if it is the "exit" keyword
        if alphanum.lower() == 'exit':
            # if it is "exit", then say goodbye and terminate the program
            print('\nExiting the program... Good Bye')
            break
        # if it is a strint other than "exit"
        else:
            # then set to invalid flag to True to show warning and continue with next cycle
            is_invalid = True
            continue
    # convert the given string to the integer
    number = int(alphanum)
    # if the number is between 1 and 3999, inclusively
    if 0 < number < 4000:
        # then convert to roman numerals and print out the user
        print(
            f'\nRoman numerals representation of decimal number "{alphanum}"" is equal to {convert(number)}')
        # and set invalid flag to the False, it might be set the True in previous cycle
        is_invalid = False
    # if the number is out of bounds
    else:
        # then set to invalid flag to True to show warning
        is_invalid = True
# verilen sayıyı Roma rakamlarına çevir
def cevir(ondalik_numara):
    # Roma rakamları için bir sözlük oluştur
    roma = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
            50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    # sonuç değişkenini başlat
    numara_roma = ''
    # Roma rakamlarında döngü oluştur, her sembol için hesapla ve sonuca ekle
    for i in roma.keys():
        numara_roma += roma[i] * (ondalik_numara // i)
        ondalik_numara %= i
    return numara_roma

# kullanıcıya uyarı göstermek için kullanılacak bayrak, varsayılan olarak False.
gecersiz_girdi = False

# kullanıcıdan sürekli olarak giriş almak için sonsuz döngü başlat
while True:
    # kullanıcıya gösterilecek bilgi metni
    bilgi = """
###  Bu program ondalık sayıları Roma Rakamlarına çevirir ###
(Programdan çıkmak için "exit" yazın)
Lütfen 1 ile 3999 arasında bir sayı girin: """

    # bilgi metnini gösterdikten sonra kullanıcı girişini al
    # eğer gecerli_girdi True olarak ayarlanmışsa, kullanıcıya ekstra uyarı göster
    # alphanum değişkenine girişi gönder, baştaki ve sondaki boşluk karakterlerini kaldırmak için strip() kullan
    alphanum = input('\nGeçersiz Giriş !!!\n'*gecersiz_girdi + bilgi).strip()
    # eğer giriş ondalık sayı değilse
    if not alphanum.isdecimal():
        # ardından, "exit" kelimesi olup olmadığını kontrol et
        if alphanum.lower() == 'exit':
            # eğer "exit" ise, hoşça kalın deyin ve programı sonlandırın
            print('\nProgramdan çıkılıyor... İyi günler')
            break
        # eğer "exit" dışında bir metin girişi yapılmışsa
        else:
            # daha sonra gecersiz_girdi bayrağını True olarak ayarlayarak uyarı göster ve sonraki döngüye devam et
            gecersiz_girdi = True
            continue
    # verilen metni tamsayıya çevir
    sayi = int(alphanum)
    # eğer sayı 1 ile 3999 arasındaysa
    if 0 < sayi < 4000:
        # sonra Roma rakamlarına çevir ve kullanıcıya yazdır
        print(
            f'\n"{alphanum}" ondalık sayısının Roma rakamları temsili: {cevir(sayi)}')
        # ve gecersiz_girdi bayrağını False olarak ayarla, önceki döngüde True olarak ayarlanmış olabilir
        gecersiz_girdi = False
    # eğer sayı sınırların dışında ise
    else:
        # ardından gecersiz_girdi bayrağını True olarak ayarlayarak uyarı göster
        gecersiz_girdi = True
