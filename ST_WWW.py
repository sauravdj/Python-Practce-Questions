import string
import operator
sentence = "Wwas iiit a rat I saw zzgh?"


def letter_count(str):
    count_dict = {}
    '''Counts the frequency of letters in a sentence and returns it as a dictonary'''
    uppercase = str.upper()
    if len(uppercase) < 15:
        print("Please enter a senter that is longer than 15 characters")
    else:
        for letter in uppercase:
            if letter in string.ascii_uppercase:
                if letter in count_dict:
                    count_dict[letter] += 1
                else:
                    count_dict[letter] = 1
            sorted_dict = dict(sorted(count_dict.items()))
          
    return sorted_dict


def most_common_letter(str):
    '''sorts dictionary by values and appends the most common value to a list'''
    common_lst = []
    lett_lst = []
    sorted_dict = letter_count(str)
    sort_by_value = sorted(sorted_dict.items(), key=operator.itemgetter(1))
    sort = sort_by_value.pop(-1)
    common_lst.append(sort)
    for i in sort_by_value:
        if i[1] == sort_by_value[-1][1]:
            common_lst.append(i)
    for i in range(len(common_lst)):
        lett_lst.append(common_lst[i][0])
    lett_lst.append(sort_by_value[-1][1])
    return lett_lst


def string_count_histogram(str):
    '''prints the current letter from the dictionary the amount of times that it shows in the given sentence'''
    sorted_dict = letter_count(str)
    letter_lst = []
    letter_tup = ()
    last_el = -1
    for i in sorted_dict:
        num = sorted_dict.get(i)
        for j in range(num):
            letter_lst.append(i)
    return letter_lst


def results(f1, f2, f3):
    '''takes in functions and returns as a print statemnt statments'''
    str_letter_count = str(f1).replace("{", "").replace("}", "")
    letter_no_count = str(f2[0:-1]).replace("[", "").replace("]", "")
    hist_lst = f3
    new_hist_lst = []
    # for i, j in zip(hist_lst[0:], hist_lst[1:]):
    #     if i != j:
    #         new_hist_lst.append(i+"\n")
    #     else:
    #         new_hist_lst.append(i)
             
    # print(new_hist_lst)    
    for i in range(len(hist_lst)):
      if i+1 != len(hist_lst): 
        if hist_lst[i] != hist_lst[i+1] :
            new_hist_lst.append(hist_lst[i]+"\n")
        else:
            new_hist_lst.append(hist_lst[i])
      else:
        if(hist_lst[-1] == hist_lst[-2] ):
          new_hist_lst.append(hist_lst[i]+"\n") 
        else:
            new_hist_lst.append(hist_lst[i])        
     
    str_new_hist = ''.join(new_hist_lst)
    
    print(f"1. Letter counts: {str_letter_count}")
    if len(f2) > 2:
        print(
            f"2. Most frequent letters: {letter_no_count} each appear {f2[-1]} times.")
    else:
        print(f"2. Most frequent letters: {f2[1]} each appear {f2[-1]} times.")
    print(f"Histogram:\n{str_new_hist}")

def main():
    l = letter_count(sentence)
    m = most_common_letter(sentence)
    s = string_count_histogram(sentence)
    results(l, m, s)
    
main()    