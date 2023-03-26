def word_replace():

    str = 'example, xyz, abc, uga buga'
    word_to_replace = input("enter word for replace: ")
    word_replacement = input("Enter word for replacement")

    print(str.replace(word_to_replace, word_replacement))

word_replace()