"""
Assignment 1-A
==============

Update the Python script below to make it more compact and readable; use at least variables and f-strings.
For those who are already familiar with Python – write the best code you can to conform to the Zen of Python.

"""




list1 = ["This is ","That "]
list2 = ["lay in ", "ate ","killed ","worried ", "tossed ", "milk'd ", "kisse'd ",
                                                       "married ","waked ","kept "]
list3 = ["the house that Jack built. "  ,  "the malt "  ,  "the rat, "  ,  "the cat,","the dog, ",
         "the cow with the crumpled horn,","the maiden all forlorn,","the man all tatter'd and torn, ",
         "the priest all shaven and shorn,","the cock that crow'd in the morn, ","the farmer sowing his corn, " ]
for i in range(len(list3)) :
    print(list1[0] + list3[i])
    for j in range(i-1,-1 ,-1) :
        print(list1[1] + list2[j] + list3[j])
    print('\n\n\n')

