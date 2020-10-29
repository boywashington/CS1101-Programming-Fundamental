#This function will print 9 lines
def nine_lines():
    def three_lines():
        def new_line():
              print('.')
        new_line()
        new_line()
        new_line()
    three_lines()
    three_lines()
    three_lines()

#This function will print 16 lines
def clear_screen():
    def nine_lines():
        def three_lines():
            def new_line():
                print('.')
            new_line()
            new_line()
            new_line()
            new_line()
        three_lines()
        three_lines()
        three_lines()
        three_lines()    
    nine_lines()

print('Printing nine lines')
nine_lines() #calling function to print 9 lines

print('Printing 25 lines')
nine_lines() #calling function to print 9 lines
clear_screen() #calling function to print additional 16 lines
