def read_file():
    # opens the file, catches any errors, and closes the file
    try:
        file = open('Assignment 3/names.txt', 'r')
        # takes each line of the file and adds it as an item in the list file_list
        file_list = file.read().splitlines()
        # takes the words and numbers of each line and adds it as an item in a list
        file_list = [line.split() for line in file_list]
    except:
        print('Error')
    finally:
        file.close()
    name_dictionary = {}
    # takes the items in each line and adds a list with the rank as the first element and the decade to the second element to ranking_list
    for item in file_list:
        ranking_list = []
        decade = 1900
        for i in range(len(item)):
            if i != 0:
                ranking = int(item[i])
                if ranking == 0:
                    ranking_list.append([1001, decade])
                else:
                    ranking_list.append([ranking, decade])
                decade += 10
        name_dictionary[item[0]] = ranking_list
    return name_dictionary


def create_dictionary(file_list):
    for i in range(file_list):
        i = i+1

# shows the different selections and routes the selection to the correct function


def show_menu(name_dictionary):
    selection = 0
    while selection >= 7 or selection <= 1:
        print('''
Options:
Enter 1 to search for names.
Enter 2 to display data for one name.
Enter 3 to display all names that appear in only one decade.
Enter 4 to display all names that appear in all decades.
Enter 5 to display all names that are more popular in every decade.
Enter 6 to display all names that are less popular in every decade.
Enter 7 to quit.
        ''')
        selection = int(input('Enter Choice: '))
        if selection == 1:
            search(name_dictionary)
            break
        if selection == 2:
            name_data(name_dictionary)
            break
        if selection == 3:
            one_decade(name_dictionary)
            break
        if selection == 4:
            all_decades(name_dictionary)
            break
        if selection == 5:
            more_popular(name_dictionary)
            break
        if selection == 6:
            less_popular(name_dictionary)
            break
        if selection == 7:
            print('Goodbye.')
            break

# finds if a name is in the dictionary as well as the decade with the highest rank


def search(name_dictionary):
    name = str(input('Enter Name: '))
    if name in name_dictionary:
        highest_rank = [1001, 1890]
        # finds the decade with the highest rank of the name
        for rank in name_dictionary[name]:
            if rank[0] < highest_rank[0]:
                highest_rank = rank
        print('The matches with their highest ranking decade are:')
        print(name + ' ' + str(highest_rank[1]))
    else:
        print(name + ' does not appear in any decade.')


def name_data(name_dictionary):
    # prints out the rankings of the names
    name = str(input('Enter Name: '))
    output = ''
    for rank in name_dictionary[name]:
        output = output + str(rank[0]) + ' '
    print(name + ': ' + output)
    for rank in name_dictionary[name]:
        print(str(rank[0]))


def one_decade(name_dictionary):
    decade = int(input('Enter Decade: '))
    name_list = []
    for name in name_dictionary.items():
        index = (decade - 1900)//10
        # if the rank of the name during the decade is 1000 or less, add it to name_list
        if name[1][index][0] < 1001:
            name_list.append([name[0], name[1][index][0]])
    # sorts the names by the rank during the decade

    def take_decade(element):
        return element[1]
    name_list.sort(key=take_decade)
    print('The names are in order of rank: ')
    for name in name_list:
        print(name[0] + ': ' + str(name[1]))


def all_decades(name_dictionary):
    name_list = []
    for name in name_dictionary.items():
        # adds name to name_list if the rank of the name every decade is less than 1001
        is_ranked = []
        for decade in name[1]:
            if decade[0] < 1001:
                is_ranked.append(True)
            else:
                is_ranked.append(False)
        if all(is_ranked):
            name_list.append(name[0])
    # sorts the list alphabetically
    name_list.sort()
    print(str(len(name_list)) + ' names appear in every decade. The names are: ')
    for name in name_list:
        print(name)


def more_popular(name_dictionary):
    # print(name_dictionary)
    # copies list of name_dictionary and removes a name from the name_list if its rank is not less than it was prior year
    name_list = name_dictionary.copy()
    for name in name_dictionary.items():
        prior_rank = 1001
        for decade in name[1]:
            if prior_rank - decade[0] <= 0:
                if name[0] in name_list:
                    del name_list[name[0]]
            else:
                # updates prior rank to the current decade's value
                prior_rank = decade[0]
    print(str(len(name_list)) + ' names are more popular in every decade. ')
    for name in name_list:
        print(name)


def less_popular(name_dictionary):
    # print(name_dictionary)
    # copies list of name_dictionary and removes a name from the name_list if its rank is not higher than it was prior year
    name_list = name_dictionary.copy()
    for name in name_dictionary.items():
        prior_rank = 0
        for decade in name[1]:
            if prior_rank - decade[0] >= 0:
                if name[0] in name_list:
                    del name_list[name[0]]
            else:
                # updates prior rank to current decade's value
                prior_rank = decade[0]
    print(str(len(name_list)) + ' names are more popular in every decade. ')
    for name in name_list:
        print(name)


def main():
    show_menu(read_file())


main()
