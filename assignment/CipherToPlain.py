
cipher1 = "slnpzshabylzohssthrluvshdylzwljapunhulzahispzotluavmylspnpvuvywyvopipapunaolmylllelyjpzlaolylvmvyh"
cipher2 = "iypknpunaolmyllkvtvmzwlljovyvmaolwylzzvyaolypnoavmaolwlvwslwlhjlhisfavhzzltislhukavwlapapvuaolnvcl"
cipher3 = "yutluamvyhylkylzzvmnyplchujlz"

alphabets_frequency = dict()

def find_frequency(text1,text2,text3):
    global alphabets_frequency
    for alphabet in text1:
        # print alphabet
        if alphabet not in alphabets_frequency:
            alphabets_frequency[alphabet] = 1
        else:
            alphabets_frequency[alphabet] += 1

    for alphabet in text2:
        # print alphabet
        if alphabet not in alphabets_frequency:
            alphabets_frequency[alphabet] = 1
        else:
            alphabets_frequency[alphabet] += 1

    for alphabet in text3:
        # print alphabet
        if alphabet not in alphabets_frequency:
            alphabets_frequency[alphabet] = 1
        else:
            alphabets_frequency[alphabet] += 1

    #for key in alphabets_frequency:
        #print key,alphabets_frequency[key]

    # after seeing the frequencies one can easily figure out the less possibility of using transposition technique.

def substitution_cipher_direct(text1,text2,text3):
    cipher = text1+text2+text3
    cipher_new = ""
    for i in range(27):
        print "*** "+ str(i)+"  ***"
        for j in range(len(cipher)):
            val = (ord(cipher[j])+i)
            if val>122:
                val = (val%122)+96
            cipher_new += str(chr(val))
        print cipher_new
        print "\n"
        cipher_new = ""

# 19th iteration is giving some meaningful text
find_frequency(cipher1,cipher2,cipher3)
substitution_cipher_direct(cipher1,cipher2,cipher3)