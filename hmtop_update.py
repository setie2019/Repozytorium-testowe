def hmtopfive_update(result):  
    from ast import literal_eval  # import funkcji z stringa na dict
    tf_dict = {}
    with open('hmtopfive.txt', 'r') as file:
        string = file.read()   # zawartość file do stringa
    tf_dict = literal_eval(string)  # zmiana stringa na dict
    end_key = []
    end_key = list(tf_dict.keys())[-1]  # wskazanie ostatniego klucza
    lowest_result = int(tf_dict[end_key])   # wskazanie ostaniej value
    if result > lowest_result:
        print('Your score is good enough to be placed in the Top Five Scores Ever')
        odp = ""
        odp = input('If you would like to be placed, press Y')
        odp = odp.upper()
        if odp == 'Y':
            nazwa = ""
            nazwa = input("Please enter your name or nickname: ")
            while nazwa in list(tf_dict.keys()):
                print('use more unique nickname')
                nazwa = input("Please enter your name or nickname")
            del tf_dict[end_key]
            tf_dict[nazwa] = result
            sortowanie = sorted(tf_dict.items(), key = lambda x:x[1], reverse = True)

            def Convert(tup, di):
                di = dict(tup)
                return di
   
            tf_dict = Convert(sortowanie, tf_dict)
            print('The current Top Five Scores Ever: ')
            print(tf_dict)
            with open('hmtopfive.txt', 'w') as fa:
                fa.write(str(tf_dict))
    else:
        print('The current Top Five Scores Ever: ')
        print(tf_dict)    
