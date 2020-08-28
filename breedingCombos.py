import _pickle as pickle
import matplotlib.pyplot as plt

class dog:
    def __init__ (self, name, gender, wire1,wire2,coat1,coat2,cream1,cream2,black1,black2,red1,red2,blue1,blue2,base1,base2,saddle1,saddle2,dapple1,dapple2, pied1, pied2, picture):
        self.name = name
        self.gender = gender
        self.wire1 = wire1
        self.coat1 = coat1
        self.cream1 = cream1
        self.black1 = black1
        self.red1 = red1
        self.blue1 = blue1
        self.base1 = base1
        self.saddle1 = saddle1
        self.dapple1 = dapple1
        self.wire2 = wire2
        self.coat2 = coat2
        self.cream2 = cream2
        self.black2 = black2
        self.red2 = red2
        self.blue2 = blue2
        self.base2 = base2
        self.saddle2 = saddle2
        self.dapple2 = dapple2
        self.pied1 = pied1
        self.pied2 = pied2
        self.coat = ''
        self.color = ''
        self.dapple = ''
        self.piebald = ''
        self.picture = picture


def printDog(self):
    print(self.name + ' is ' + self.color + ' with a ' + self.coat + ' coat.')

def determineDog(self):
    self.coat = determineCoat(self)
    self.color = determineColor(self)

def determineCoat(self):
    tempWire = self.wire1 + self.wire2
    tempCoat = self.coat1 + self.coat2
    if(determineWire(tempWire) == 'Wire'):
        return 'Wire'
    else:
        return coatType(tempCoat)


def determineWire(wire):
    if(wire == 'll'):
        return 'Not Wire'
    else:
        return 'Wire'

def coatType(coat):
    if(coat == 'TT'):
        return 'Long'
    else:
        return 'Smooth'


def determineColor(self):
    tempCream = self.cream1 + self.cream2
    tempRed = self.red1 + self.red2
    tempShade = self.base1 + self.base2
    tempBlue = self.blue1 + self.blue2

    if(determineRed(tempRed) == 'Red' and determineCream(tempCream) == 'Cream'):
        return 'ee Red'
    elif(determineRed(tempRed) == 'Red'):
        return 'Red'
    elif(determineCream(tempCream) == 'Cream'):
        return 'Cream'
    else:
        if(determineBlue(tempBlue) == "Blue"):
            if(tempShade == 'bb'):
                return 'Isabella and Tan'
            else:
                return 'Blue and Tan'
        else:
            return determineShade(tempShade)

def determineRed(color):
    if(color == 'atat'):
        return 'Not Red'
    else:
        return 'Red'

def determineCream(color):
    if(color == 'ee'):
        return 'Cream'
    else:
        return 'Not Cream'

def determineBlue(color):
    if(color == 'dd'):
        return 'Blue'
    else:
        return 'Not Blue'

def determineShade(color):
    if(color == 'bb'):
        return 'Chocolate and Tan'
    else:
        return 'Black and Tan'

def determineDapple(dapple):
    if(dapple=='mm'):
        return 'not dapple'
    elif(dapple=='MM'):
        return 'double dapple'
    else:
        return 'dapple'

def determinePiebald(piebald):
    if(piebald=='SS'):
        return 'not piebald'
    elif(piebald=='ss'):
        return 'piebald'
    else:
        return 'partially piebald'

def dogBreeding(dog1, dog2):
    print()
    pairTitle = dog1.name + ' X ' + dog2.name
    colors = {}
    colors['cream'], colors['notcream'] = dogBreedingCream(dog1,dog2)
    colors['blue'], colors['notblue'] = dogBreedingBlue(dog1,dog2)
    colors['red'], colors['notred'] = dogBreedingRed(dog1,dog2)
    colors['choc'], colors['black'] = dogBreedingShade(dog1, dog2)

    coats = {}
    coats['wire'], coats['notwire'] = dogBreedingWire(dog1,dog2)
    coats['smooth'], coats['long'] = dogBreedingCoat(dog1,dog2)

    dapple = {}
    dapple['dapple'], dapple['notdapple'], dapple['double'] = dogBreedingDapple(dog1, dog2)

    piebald = {}
    piebald['pied'], piebald['notpied'], piebald['partial'] = dogBreedingPiebald(dog1,dog2)

    dogColorPercentages(colors, pairTitle)
    dogCoatPercentages(coats, pairTitle)
    dogDapplePercentages(dapple, pairTitle)
    dogPiebaldPercentages(piebald, pairTitle)

def dogBreedingDapple(dog1,dog2):
    temp = {}
    temp['1'] = determineDapple(dog1.dapple1 + dog2.dapple1)
    temp['2'] = determineDapple(dog1.dapple1 + dog2.dapple2)
    temp['3'] = determineDapple(dog1.dapple2 + dog2.dapple1)
    temp['4'] = determineDapple(dog1.dapple2 + dog2.dapple2)
    dapple = 0
    notdapple = 0
    double = 0
    for item in temp:
        if(temp[item] == 'dapple'):
            dapple+=1
        elif(temp[item] =='not dapple'):
            notdapple+=1
        else:
            double+=1
    return dapple, notdapple, double

def dogDapplePercentages(dapple,pairTitle):
    totalDapple = dapple['dapple'] + dapple['notdapple'] + dapple['double']
    slices = []
    allColors = []
    graphColors = []
    explodeArray = []
    totalDap = dapple['dapple'] / totalDapple
    totalNot = dapple['notdapple'] / totalDapple
    totalDouble = dapple['double'] / totalDapple


    if(totalDap):
        slices.append(totalDapple)
        allColors.append('Dapple')
        graphColors.append('Grey')
        explodeArray.append(0)
    if(totalNot):
        slices.append(totalNot)
        allColors.append('Not Dapple')
        graphColors.append('steelblue')
        explodeArray.append(0)
    if(totalDouble):
        slices.append(totalDouble)
        allColors.append('Double Dapple')
        graphColors.append('indianred')
        explodeArray.append(0)

    pairTitle = 'Dapple: ' + pairTitle
    plt.title(pairTitle, fontdict=None, loc='center', pad=None)
    plt.pie(slices, labels = allColors, colors = graphColors,
    startangle = 90, shadow = False, explode = explodeArray,
    radius= 1.0, autopct = '%1.2f%%')

    plt.savefig('graphDapple.jpg')
    plt.clf()

def dogBreedingPiebald(dog1,dog2):
    temp = {}
    temp['1'] = determinePiebald(dog1.pied1 + dog2.pied2)
    temp['2'] = determinePiebald(dog1.pied1 + dog2.pied1)
    temp['3'] = determinePiebald(dog1.pied2 + dog2.pied1)
    temp['4'] = determinePiebald(dog1.pied2 + dog2.pied2)
    pied = 0
    notpied = 0
    partial = 0
    for item in temp:
        if(temp[item] == 'piebald'):
            pied+=1
        elif(temp[item] =='not piebald'):
            notpied+=1
        else:
            partial+=1
    return pied, notpied, partial

def dogPiebaldPercentages(piebald,pairTitle):
    totalPiebald = piebald['pied'] + piebald['notpied'] + piebald['partial']
    slices = []
    allColors = []
    graphColors = []
    explodeArray = []
    totalPied = piebald['pied'] / totalPiebald
    totalNot = piebald['notpied'] / totalPiebald
    totalPartial = piebald['partial'] / totalPiebald


    if(totalPied):
        slices.append(totalPied)
        allColors.append('Piebald')
        graphColors.append('steelblue')
        explodeArray.append(0)
    if(totalNot):
        slices.append(totalNot)
        allColors.append('Not Piebald')
        graphColors.append('grey')
        explodeArray.append(0)
    if(totalPartial):
        slices.append(totalPartial)
        allColors.append('Partially Piebald')
        graphColors.append('lightsteelblue')
        explodeArray.append(0)

    pairTitle = 'Piebald: ' + pairTitle
    plt.title(pairTitle, fontdict=None, loc='center', pad=None)
    plt.pie(slices, labels = allColors, colors = graphColors,
    startangle = 90, shadow = False, explode = explodeArray,
    radius= 1.0, autopct = '%1.2f%%')

    plt.savefig('graphPiebald.jpg')
    plt.clf()


def dogCoatPercentages(coats, pairTitle):
    totalCoats = coats['wire'] + coats['notwire']
    slices = []
    allColors = []
    graphColors = []
    explodeArray = []

    #First Determine Chance of Wire
    totalWire = coats['wire'] / totalCoats
    totalSmooth = coats['smooth'] / totalCoats * coats['notwire'] / totalCoats
    totalLong = coats['long'] / totalCoats * coats['notwire'] / totalCoats


    if(totalWire):
        #print(str(totalWire * 100) + '% Wire')
        slices.append(totalWire)
        allColors.append('Wire')
        graphColors.append('red')
        explodeArray.append(0)
    if(totalSmooth):
        #print(str(totalSmooth * 100) + '% Smooth')
        slices.append(totalSmooth)
        allColors.append('Smooth')
        graphColors.append('blue')
        explodeArray.append(0)
    if(totalLong):
        #print(str(totalLong * 100) + '% Long')
        slices.append(totalLong)
        allColors.append('Long')
        graphColors.append('yellow')
        explodeArray.append(0)

    pairTitle = 'Coats: ' + pairTitle
    plt.title(pairTitle, fontdict=None, loc='center', pad=None)
    plt.pie(slices, labels = allColors, colors = graphColors,
    startangle = 90, shadow = False, explode = explodeArray,
    radius= 1.0, autopct = '%1.2f%%')

    plt.savefig('graphCoats.jpg')
    plt.clf()

def dogBreedingWire(dog1, dog2):
    temp = {}
    temp['1'] = determineWire(dog1.wire1 + dog2.wire1)
    temp['2'] = determineWire(dog1.wire1 + dog2.wire2)
    temp['3'] = determineWire(dog1.wire2 + dog2.wire1)
    temp['4'] = determineWire(dog1.wire2 + dog2.wire2)
    wire = 0
    notwire = 0
    for item in temp:
        if(temp[item] == 'Wire'):
            wire+=1
        else:
            notwire+=1
    return wire, notwire

def dogBreedingCoat(dog1,dog2):
    temp = {}
    temp['1'] = coatType(dog1.coat1 + dog2.coat1)
    temp['2'] = coatType(dog1.coat1 + dog2.coat2)
    temp['3'] = coatType(dog1.coat2 + dog2.coat1)
    temp['4'] = coatType(dog1.coat2 + dog2.coat2)
    smooth = 0
    long = 0
    for item in temp:
        if(temp[item] == 'Smooth'):
            smooth+=1
        else:
            long+=1
    return smooth, long

def dogColorPercentages(colors, pairTitle):
    totalColors = 0
    slices = []
    allColors = []
    graphColors = []
    explodeArray = []
    for item in colors:
        totalColors+=colors[item]
    #First Determine Chance of Red/Cream
    try:
        totalCream = colors['cream'] / (colors['cream'] + colors['notcream'])
        modCream = 1/totalCream
    except:
        totalCream = 0
        modCream = totalColors+1

    try:
        totalRed = colors['red'] / (colors['red'] + colors['notred'])
        modRed = 1/totalRed
    except:
        totalRed = 0
        modRed = totalColors+1

    temp = ''
    countCream = 0
    countRed = 0
    countBoth = 0
    countNeither = 0
    countBlack = 0
    countChoc = 0
    percentageCream = 0
    percentageRed = 0
    percentageBlack = 0
    percentageBoth = 0
    percentageChocolate = 0
    percentageBlueTan = 0
    percentageIsabella = 0
    #determine percetages for cream and red
    for i in range(0, totalColors):
        #print(temp)
        temp = ''
        if(i<(totalCream*totalColors)):
            temp = 'Cream'
        if(i%modRed == 0 and modRed < totalColors):
            temp += 'Red'
        if(temp == 'CreamRed'):
            countBoth+=1
        if(temp == ''):
            countNeither+=1
        if(temp == 'Red'):
            countRed+=1
        if(temp == 'Cream'):
            countCream+=1
    if(countCream):
        percentageCream = countCream/totalColors
        slices.append(percentageCream)
        allColors.append('Cream')
        graphColors.append('lemonchiffon')
        explodeArray.append(0)
        #print(str(percentageCream * 100) + '% Cream')
    if(countRed):
        percentageRed = countRed/totalColors
        slices.append(percentageRed)
        allColors.append('Red')
        graphColors.append('indianred')
        explodeArray.append(0)
        #print(str(percentageRed * 100) + '% Red')
    if(countBoth):
        percentageBoth = countBoth/totalColors
        slices.append(percentageBoth)
        allColors.append('ee Red')
        graphColors.append('coral')
        explodeArray.append(0)
        #print(str(percentageBoth * 100) + '% ee Cream')

    percenatageNeither = countNeither/totalColors
    totalNeither = int(percenatageNeither * totalColors)

    #Then Determine Chance base color will show
    try:
        totalBlack = colors['black'] / (colors['black'] + colors['choc'])
        modBlack = 1/totalBlack
    except:
        totalBlack = 0
        modBlack = totalColors+1

    try:
        totalChoc = colors['choc'] / (colors['black'] + colors['choc'])
        modChoc = 1/totalChoc
    except:
        totalChoc = 0
        modChoc = totalColors+1

    for i in range(totalNeither):
        temp = 'Black'
        if(i%modChoc == 0):
            temp = 'Choc'
        if(temp== 'Black'):
            countBlack+=1
        if(temp=='Choc'):
            countChoc+=1
    try:
        percentageBlue = colors['blue'] / (colors['blue'] + colors['notblue'])

    except:
        percentageBlue = 0

    if(countBlack):
        percentageBlack = countBlack/totalColors * (1 - percentageBlue)
        slices.append(percentageBlack)
        allColors.append('Black&Tan')
        graphColors.append('grey')
        explodeArray.append(0)
        #print(str(percentageBlack * 100) + '% Black and Tan')
        if(percentageBlue):
            percentageBlueTan = countBlack/totalColors * (percentageBlue)
            slices.append(percentageBlueTan)
            allColors.append('Blue&Tan')
            graphColors.append('steelblue')
            explodeArray.append(0)
            #print(str(countBlack/totalColors * 100 * (percentageBlue)) + '% Blue and Tan')
    if(countChoc):
        percentageChocolate = countChoc/totalColors * (1 - percentageBlue)
        slices.append(percentageChocolate)
        allColors.append('Chocolate&Tan')
        graphColors.append('chocolate')
        explodeArray.append(0)
        #print(str(countChoc/totalColors * 100 * (1 - percentageBlue)) + '% Chocolate and Tan')
        if(percentageBlue):
            percentageIsabella = countChoc/totalColors * (percentageBlue)
            slices.append(percentageIsabella)
            allColors.append('Isabella&Tan')
            graphColors.append('lightsteelblue')
            explodeArray.append(0)
            #print(str(countBlack/totalColors * 100 * (percentageBlue)) + '% Isabella and Tan')

    pairTitle = 'Colors: ' + pairTitle
    plt.title(pairTitle, fontdict=None, loc='center', pad=None)
    plt.pie(slices, labels = allColors, colors = graphColors,
    startangle = 90, shadow = False, explode = explodeArray,
    radius= 1.0, autopct = '%1.2f%%')

    #plt.legend()
    #plt.show()
    plt.savefig('graphColors.jpg')
    plt.clf()


    #Then Determine Chance of Blue
    #totalBlue = 1/colors['blue'] * totalColors

    #print(str(totalCream))
    #print(str(totalRed))
    #print(str(totalBlue))
    #print(str(totalBlack))
    #print(str(totalChoc))

def dogBreedingShade(dog1, dog2):
    temp = {}
    temp['1'] = determineShade(dog1.base1 + dog2.base1)
    temp['2'] = determineShade(dog1.base1 + dog2.base2)
    temp['3'] = determineShade(dog1.base2 + dog2.base1)
    temp['4'] = determineShade(dog1.base2 + dog2.base2)
    choc = 0
    black = 0
    for item in temp:
        if(temp[item] == 'Chocolate and Tan'):
            choc+=1
        if(temp[item] == 'Black and Tan'):
            black+=1

    #print(str(choc*25) + '% Chocolate and Tan')
    #print(str(black*25) + '% Black and Tan')

    return choc, black

def dogBreedingCream(dog1, dog2):
    temp = {}
    temp['1'] = determineCream(dog1.cream1 + dog2.cream1)
    temp['2'] = determineCream(dog1.cream1 + dog2.cream2)
    temp['3'] = determineCream(dog1.cream2 + dog2.cream1)
    temp['4'] = determineCream(dog1.cream2 + dog2.cream2)
    cream = 0
    notcream = 0
    for item in temp:
        if(temp[item] == 'Cream'):
            cream+=1
        else:
            notcream+=1

    #print(str(cream*25) + '% Cream')
    #print(str(notcream*25) + '% Not Cream')

    return cream, notcream

def dogBreedingRed(dog1, dog2):
    temp = {}
    temp['1'] = determineRed(dog1.red1 + dog2.red1)
    temp['2'] = determineRed(dog1.red1 + dog2.red2)
    temp['3'] = determineRed(dog1.red2 + dog2.red1)
    temp['4'] = determineRed(dog1.red2 + dog2.red2)
    red = 0
    notred = 0
    for item in temp:
        if(temp[item] == 'Red'):
            red+=1
        else:
            notred+=1

    #print(str(red*25) + '% Red')
    #print(str(notred*25) + '% Not Red')

    return red, notred

def dogBreedingBlue(dog1, dog2):
    temp = {}
    temp['1'] = determineBlue(dog1.blue1 + dog2.blue1)
    temp['2'] = determineBlue(dog1.blue1 + dog2.blue2)
    temp['3'] = determineBlue(dog1.blue2 + dog2.blue1)
    temp['4'] = determineBlue(dog1.blue2 + dog2.blue2)
    blue = 0
    notblue = 0
    for item in temp:
        if(temp[item] == 'Blue'):
            blue+=1
        else:
            notblue+=1

    #print(str(blue*25) + '% Blue')
    #print(str(notblue*25) + '% Not Blue')

    return blue, notblue

def dogList():

    Dogs = {}

    #Dogs['Eevee'] = dog('Eevee', 'Female', 'l', 'l', 'T', 'T', 'E', 'e', 'ky', 'ky', 'ay', 'at', 'D', 'D', 'B', 'b', 'N', 'l', 'm', 'm','S','S', 'eevee.jpg')
    Dogs['Poppy'] = dog('Poppy', 'Female', 'l', 'l', 'G', 'G', 'E', 'E', 'ky', 'ky', 'at', 'at', 'D', 'd', 'B', 'b', 'l', 'l', 'm', 'm','S','S', 'poppy.jpg')
    Dogs['Pretzel'] = dog('Pretzel', 'Male', 'F', 'l', 'G', 'T', 'e', 'e', 'ky', 'ky', 'at', 'at', 'D', 'D', 'B', 'b', 'l', 'l', 'm', 'm','S','S', 'pretzel.jpg')
    Dogs['Blue'] = dog('Blue', 'Male', 'F', 'l', 'G', 'T', 'e', 'e', 'ky', 'ky', 'at', 'at', 'D', 'd', 'B', 'b', 'l', 'l', 'm', 'm','S','S', 'pretzel.jpg')
    #Dogs['newDog'] = dog('Random', 'Male', 'F', 'l', 'T', 'T', 'E', 'e', 'ky', 'ky', 'at', 'at', 'D', 'D', 'B', 'b', 'l', 'l', 'm', 'm')
    #Dogs['blueDog'] = dog('Blue', 'Male', 'l', 'l', 'G', 'G', 'E', 'E', 'ky', 'ky', 'at', 'at', 'd', 'd', 'b', 'b', 'l', 'l', 'm', 'm')

    for pet in Dogs:
        determineDog(Dogs[pet])
        #printDog(Dogs[pet])

    dogBreeding(Dogs['Poppy'], Dogs['Blue'])
    #dogBreeding(Dogs['Eevee'], Dogs['Pretzel'])
    #dogBreeding(Dogs['poppy'], Dogs['blueDog'])
"""
    with open('dogText.txt', 'wb') as file:
        file.write(pickle.dumps(Dogs))

    with open('dogText.txt', 'rb') as file:
        Dogs = pickle.load(file)
"""
    #print(Dogs['Eevee'].wire1)
