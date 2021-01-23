import placeholder


NyTimesHeadlines = []

def smllhdLinesFiltered(smallHLines):
    listeSmallHeadLines = []

    # Non Information which is Sometimes Included, have to be actual everyTime. It may get very Big
    listNoString = [
        'Live',
        'live',
        '2021',
        'Disney+',
        'The New York Times Company',
        'Ashley Gilbertson / VII,  for The New York Times',
        'Erin Scott for The New York Times',
        'Anna Moneymaker for The New York Times',
        'Todd Heisler / The New York Times',
        'via Linda Zall',
        'Tatan Syuflana/Associated Press',
        'Octavio Jones for The New York Times',
        'Kunal Patil/Hindustan Times via Getty Images',
        'Victor J. Blue/Bloomberg',
        'Bobby Yip/Reuters',
        'Josh Haner / The New York Times',
        'Todd Heisler/The New York Times',
        'Eduardo Munoz/Reuters',
        'Chang W.Lee/The New York Times',
        'Eduardo Munoz/Reuters',
        'Erin Schaff/The New York Times',
        'Chang W. Lee/The New York Times',
        'John Taggart for The New York Times',
        'Amr Alfiky/The New York Times',
        '12:21',
        'Illustration by Justin Metz',
        'L. Kasimu Harris for The New York Times',
        'Gilles Sabrié for The New York Times',
        'Monica Almeida/The New York Times',
        'Anton Vaganov/Reuters',
        'JerSean Golatt for The New York Times'
    ]
    #Safe all elements in Lowercase to a list
    listNoString = [x.lower() for x in listNoString]

    #Delete all Empty Spaces and safe the Headlines
    for i in smallHLines:
        for j in i:
            if len(j) > 1:
                listeSmallHeadLines.append(j)

    liste = listeSmallHeadLines[3:]

    #filter Non Information from the Headlines so you can get the Headlines only
    listeNewSmllHdLnes = [x for x in liste if x.strip().lower() not in listNoString]

    for i in listeNewSmllHdLnes:
        NyTimesHeadlines.append(i)


def h3HeadlinesNYT(h3Headlines):
    listeH3Headlines = []
    listNoString = [
        'Opinion',
        'Editors’ Picks',
        'Advertisement'
    ]
    listNoString = [x.lower() for x in listNoString]

    for i in h3Headlines:
        for l in i:
            if len(l) > 1:
                listeH3Headlines.append(l)

    listNewH3HdLines = [x for x in listeH3Headlines if x.strip().lower() not in listNoString]

    for i in listNewH3HdLines:
        NyTimesHeadlines.append(i)


def h2HeadlinesNYT(h2Headlines):
    listH2HeadLines = []

    listNoString = [
        'Your Monday Briefing',
        'Listen to ‘The Sunday Read’',
        'Site Index',
        'In the ‘At Home’ Newsletter',
        'Site Information Navigation',
        'Listen to ‘The Argument’',
        'Listen to ‘The Daily’'
    ]
    listNoString = [x.lower() for x in listNoString]

    for i in h2Headlines:
        for l in i:
            if len(l) > 1:
                listH2HeadLines.append(l)


    listNewH2HdLines = [x for x in listH2HeadLines if x.strip().lower() not in listNoString]

    matchers = ["a", "e", "i", "o", "u"]
    matching = [s for s in listNewH2HdLines if any(xs in s for xs in matchers)]

    for i in matching:
        NyTimesHeadlines.append(i)
