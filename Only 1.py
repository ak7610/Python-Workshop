import datetime

'''ToDo:Print the current date and time at the start of the program
(hint: use the datetime library and search the internet)'''

i = datetime.datetime.now()
print('-'*80)
print('Current Date is {} and Current Time is {}'.format(i.date(), i.time()))
print('-'*80)

'''Print out all the even numbers from the below given list of numbers. Write the 
solution into a function and have it called in your main block for the requested answer
 (hint: use loops)

numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 
544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 
462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 
918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 
767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 
380, 126, 721, 328, 753, 470, 743, 527'}]'''

numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]

def function():
    # extract dictionary out of the list
    my_dict = numbers[0]
    # extract values from dictionary, split on coma and conver to an integer
    for n, v in my_dict.items():
        new_list = v.split(',')
        for value in new_list:
            integer_value = int(value)
            if integer_value % 2 == 0:
                print(integer_value)
if __name__ == '__main__':
    function()











