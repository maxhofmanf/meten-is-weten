ant = input('is de kaas geel? geef antwoord met ja of nee. ') 
if ant == ("ja"):
    ant = input ('heeft de kaas gaten? ')
    if ant == ("ja"):
        ant = input ("is de kaas ongelofelijk duur? ")
        if ant == ("ja"):
            print("Emmenthaler")
        elif ant == ("nee"):
            print ("leerdammer")
    elif ant == ("nee"):
        ant = input ("is de kaas hard als steen? ")
        if ant == ("ja"):
            print ("Pammigiano Reggiano")
        elif ant == ("nee"):
            print ("Goudse kaas")
elif ant == ("nee"):
    ant == input("heeft de kaas blauwe schimmels? ")
    if ant == ("ja"):
        ant = input ("heeft de kaas een korst? ")
        if ant == ("ja"):
            print ("bleu de rochbaron")
        elif ant == ("nee"):
            print ("foume d.ambert")
    elif ant == ("nee"):
        ant = input ("heeft de kaas een korst? ")
        if ant == ("ja"):
            print ("camembert")
        elif ant == ("nee"):
            print ("mozzarella")
else:
    print ("gebruik alstublieft alleen ja of nee")