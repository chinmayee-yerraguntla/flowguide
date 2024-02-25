import sys; args = sys.argv[1:]


#categories: brand, period product (type of), "Internal"/"External", eco-friendly, sports-friendly, organic cotton, teen-friendly, "No"-show, small-business ownes, biodegradable, vegan, cruelty-free, size-inclusivity, price range

indicatorMap = {"Type":0,"Placement":1,"Ecofriendly":2,"Sportsfriendly":3,"OrganicCotton":4,"Teenfriendly":5,"NoShow":6,"SmallBusiness":7,"Biodegradable":8,"Vegan":9,"CrueltyFree":10,"SizeInclusivity":11,"Prices":12}

information = {"Always":["Disposable Pads","External","Varies","Yes","Varies","Yes","Yes","No","Varies","No","No","Yes","$ - $$"],
               "Natracare":["Disposable Pads","External","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$ - $$"], 
               "Always": ["Disposable Pads","External","No","Yes","No","Yes","Yes","No","No","No","No","Yes","$"],
                "Poise":["Disposable Pads","External","No","Yes","No","Yes","Yes","No","No","No","No","Yes","$"],
                "Cora": ["Disposable Pads","External","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$ - $$"], 
                "Maxim": ["Disposable Pads","External","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$ - $$"], 
                "Saalt": ["Menstrual Cups","Internal","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$ - $$$"], 
                "Organicup":["Menstrual Cups","Internal","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$ - $$$"], 
                "Lunette":["Menstrual Cups","Internal","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$ - $$$"], 
                "Charlie Banana": ["Menstrual Cups","Internal","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$ - $$$"], 
                "Flex": ["Menstrual Discs","Internal","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$ - $$$"], 
                "Femly":["Menstrual Discs","Internal","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$ - $$$"], 
                "WUKA":["Period Leggings","External","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$ - $$$"],
                "Ruby Love":["Period Panties","External","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$ - $$$"], 
                "Rael":["Period Panties","External","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$ - $$$"] , 
                "Flo": ["Period Panties","External","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$ - $$$"], 
                "Dear Kate":["Period Shorts","External","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$$ - $$$$"], 
                "Modibodi": ["Period Swimwear","External","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$ - $$$"], 
                "Knix": ["Period Swimwear","External","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$ - $$$"], 
                "Aisle":["Period Swimwear","External","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$ - $$$"], 
                "Thinx":["Period Underwear","External","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$ - $$$"], 
                "Cora":["Period Underwear","External","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$ - $$$"], 
                "Sustain": ["Period Underwear","External","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$ - $$$"], 
                "Hannahpad":["Reusable Pads","External","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$ - $$$"], 
                "Lunapads":["Reusable Pads","External","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$ - $$$"], 
                "Aisle":["Reusable Pads","External","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$ - $$$"], 
                "Hey Girls":["Reusable Pads","External","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$"], 
                "GladRags":["Reusable Pads","External","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$ - $$$"], 
                "Lola":["Tampons","Internal","Yes","Yes","Yes","Yes","No","Yes","Yes","Yes","Yes","No","$$"], 
                "Cora":["Tampons","Internal","Yes","Yes","Yes","Yes","No","Yes","Yes","Yes","Yes","Yes","$$ - $$$"], 
                "Tampax":["Tampons","Internal","No","Yes","No","Yes","No","No","No","No","No","Yes","$"], 
                "U By Kotex":["Tampons","Internal","No","Yes","No","Yes","No","No","No","No","No","Yes","$"], 
                "L.":["Tampons","Internal","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$"], \
                "Veeda":["Tampons","Internal","Yes","Yes","Yes","Yes","No","Yes","Yes","Yes","Yes","Yes","$ - $$"], 
                "Sustain":["Tampons","Internal","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$"], 
                "The Honey Pot":["Tampons","Internal","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","$$"]}



def findBrands(indicator,information):
    listy = []
    listy2 = []
    listy3 = []
    listy4 = []
    listy5 = []
    listy6 = []
    index = indicatorMap[indicator]
    for val in information:
        if(index==0):
            if(information[val][index]=="Disposable Pads"):
                listy.append(val)
            elif(information[val][index]=="Menstrual Cups" or information[val][index]=="Menstrual Discs"):
                listy2.append(val)
            elif(information[val][index]=="Period Leggings" or information[val][index]=="Period Panties" or information[val][index]=="Period Shorts"):
                listy3.append(val)
            elif(information[val][index]=="Period Swimwear"):
                listy4.append(val)
            elif(information[val][index]=="Reusable Pads"):
                listy5.append(val)
            elif(information[val][index]=="Tampons"):
                listy6.append(val)
        elif(index==1):
            if(information[val][index]=="External"):
                listy.append(val)
            elif(information[val][index]=="Internal"):
                listy2.append(val)
        elif(index==12):
            if(information[val][index]=="$" or information[val][index]=="$ - $$"):
                listy.append(val)
            elif(information[val][index]=="$$" or information[val][index]=="$$ - $$$"):
                listy2.append(val)
            elif(information[val][index]=="$$$" or information[val][index]=="$$$ - $$$$"):
                listy3.append(val)
        else:
            if(information[val][index]=="Yes"):
                listy.append(val)
    for val in listy:
        print(val)
    print()
    if(listy2):
        for b in listy2:
            print(b)
    print()
    if(listy3):
        for b in listy3:
            print(b)
    print()
    if(listy4):
        for b in listy4:
            print(b)
    print()
    if(listy5):
        for b in listy5:
            print(b)
    print()
    if(listy6):
        for b in listy6:
            print(b)
    return

findBrands("SizeInclusivity",information)
