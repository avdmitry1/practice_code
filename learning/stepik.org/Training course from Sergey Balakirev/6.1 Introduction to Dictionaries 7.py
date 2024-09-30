# The test web server returns HTML pages by URLs (strings). The program receives various URLs as
# input. If the address came for the first time, then display the string on the screen (without quotes):
# "HTML page for <URL>"
# If the address comes again, then you should take the string "HTML page for the address <URL address>"
# from the dictionary and display a message on the screen (without quotes):
# "Fetched from cache: HTML page for <URL>" Display messages each on a new line.
# P.S. To read the entire list, the program has already written the initial lines.

a_list = ['ustanovka-i-zapusk-yazyka',
          'ustanovka-i-poryadok-raboty-pycharm',
          'peremennyye-operator-prisvaivaniya-tipy-dannykh',
          'arifmeticheskiye-operatsii',
          'ustanovka-i-poryadok-raboty-pycharm']
d = {}
for i in a_list:
    if i not in d:
        d[i] = i
        print(f'HTML-страница для адреса {d[i]}')
    else:
        print(f'Взято из кэша: HTML-страница для адреса {d[i]}')
