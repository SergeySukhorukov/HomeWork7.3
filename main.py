len_list = []


def add_len(file_name):
    for file in file_name:
        with open(file) as new_file:
            counter = 0
            for line in new_file:
                counter += 1
        len_list.append(counter)


def result(file_name):
    add_len(file_name)
    len_list.sort()
    for i in len_list:
        for file in file_name:
            with open(file) as new_file:
                linelist = []
                counter = 0
                for line in new_file:
                    linelist.append(line)
                    counter += 1
                if i == counter:
                    with open("result.txt", 'a') as result_file:
                        result_file.write(file+'\n')
                        result_file.write('Количество строк: '+str(i)+'\n')
                        result_file.write("".join(linelist))
                        result_file.write('\n')


result(['1.txt','2.txt','3.txt'])
