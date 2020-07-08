while True:
    # simpan input kedalam pembolehubah pilihan
    pilihan = input('\nWhat is the answer to Life, Universe, And Everything?\n')

    # pilihan adalah 42, maka benar, papar ucapan dalam range 1, tamatkan program
    [print('\nCORRECT\nCongratulations\n') & exit() for i in range(0,1) if pilihan == '42']

    # pilihan bukan 42, maka palsu, bayangan jawapan diberikan, papar ucapan dalam range 1
    [print('\nWRONG\nAnswer can be referenced from Hitchiker\'s Guide to Galaxy\n') for i in range(0, 1) if pilihan != '42']
    
    # pilihan 'q', utili tamatkan program
    [print('\nSelamat Tinggal!!\n') & exit() for i in range(0,1) if pilihan == 'q']