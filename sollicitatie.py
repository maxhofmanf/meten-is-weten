prak = float(input("hoeveel jaar praktijkervaring heeft u met acrobatiek? "))
if prak >= 3:
    MBO = input("Heeft u een MBO-4 Diploma? ")
    if MBO == ("nee"):
        print("Sorry u bent niet geschikt u heeft niet de voldoende benodigt heden.")
    elif MBO == ("ja"):
        lengte = float(input("wat is uw lengte? "))
        if lengte < 150:
            print("Sorry u bent niet geschikt u heeft niet de voldoende benodigt heden.")
        elif lengte >= 150:
            vracht = input("bent u in bezit van een geldig vrachtwagen rijbewijs? ")
            if vracht == ("nee"):
                print("Sorry u bent niet geschikt u heeft niet de voldoende benodigt heden.")
            elif vracht == ("ja"):
                hoed = input("bent u in bezit van een hoed? ")
                if hoed == ("nee"):
                    print("Sorry u bent niet geschikt u heeft niet de voldoende benodigt heden. u heeft niet de voldoende benodigt heden.")
                elif hoed == ("ja"):
                    overleven = input("Heeft u het Certificaat “Overleven met gevaarlijk personeel? ")  
                    if overleven == ("nee"):
                        print("Sorry u bent niet geschikt u heeft niet de voldoende benodigt heden. u heeft niet de voldoende benodigt heden.")
                    elif overleven == ("ja"):
                            print("gefeliciteerd, u heeft alle voldoeningen, u bent aangenomen.")
                    else:
                            print("gebruik alleen ja of nee A.U.B.")
                else:
                    print("gebruik alleen ja of nee A.U.B.")
            else:
                print("gebruik alleen ja of nee A.U.B")
    else:
        print("gebruik ja of nee A.U.B. ")
elif prak <= 3:
     print('Sorry u bent niet geschikt u heeft niet de voldoende benodigt heden.')
else:
       print("gebruikt ja of nee A.U.B. ")
    