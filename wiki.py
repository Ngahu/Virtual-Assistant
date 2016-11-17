import wikipedia

while true :
    input = raw_input("Q:")
    wikipedia.set_lang("es") #setting of language to b used
    print wikipedia.summary(input, sentences=2 )
