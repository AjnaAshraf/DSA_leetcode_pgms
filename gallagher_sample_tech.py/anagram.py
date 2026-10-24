def are_anagram(a,b):

    a=a.replace(" ","").lower()
    b=b.replace(" ","").lower()

    return sorted(a) == sorted(b)

print(are_anagram("listen","silent"))

         


    