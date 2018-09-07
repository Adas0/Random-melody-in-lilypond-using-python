#This code belongs to Adam Korytowski, Kraków, Poland


from random import randint

header = '\\version "2.18.2" \
\paper {\
  #(set-paper-size "a4landscape") \
  print-all-headers = ##t \
} \
\layout{ \
  indent = 0\in \
  ragged-last = ##f \
  \context { \
    \Score \
      \\remove "Bar_number_engraver" \
  } \
}'

notes = [" c", " d", " e", " f", " g", " a", " b", " r", " r", " r"];
changedNote=["is", "es", "", "", ""];
changedOctave=["'", "''", ""];


rythms = ["4", "8", "16", "4.", "8."];


def getRythmValue(randomRythm):
    values=0;
    if (randomRythm == "4"):
        values += 4;
    elif (randomRythm == "8"):
        values += 2;
    elif (randomRythm == "16"):
        values += 1;
    elif (randomRythm == "4."):
        values += 6;
    elif (randomRythm == "8."):
        values += 3;
    return values;

allNotes=[" ces", " c", " cis", " des"," d", " dis", " ees"," e", " eis",
        " fes", " f", " fis"," ges", " g", " gis", " aes", " a", " ais", " bes", " b", " bis",
        " ces'", " c'", " cis'", " des'"," d'", " dis'", " ees'"," e'", " eis'",
        " fes'", " f'", " fis'", " ges'", " g'", " gis'"," aes'", " a'", " ais'",
        " bes'", " b'", " bis'", " ces''", " c''", " cis''", " des''"," d''", " dis''", " ees''"," e''", " eis''",
        " fes''", " f''", " fis''", " ges''", " g''", " gis''"," aes''", " a''", " ais''",
        " bes''", " b''", " bis''"];

with open('sekwe.ly', 'w') as projectFile:

    tempo = 4;
    tacts=5;
    startingNote=" b";
    NOTES = [];
    NOTES.append(startingNote);
    notesLoop=[" c", " cis", " d", " dis", " e", " f", " fis", " g", " gis", " a", " ais"," b",
               " c", " cis", " d", " dis", " e", " f", " fis"];

    idxStartingNote=notesLoop.index(startingNote);
    subdominant=notesLoop[idxStartingNote+5];
    dominant=notesLoop[idxStartingNote+7];

    # print(subdominant);
    # print(dominant);

    for el in range(0,5):           #zwiekszenie prawdop. wystapienia subdominanty i dominanty
        notes.append(subdominant);
        notes.append(dominant);

    startingNote+="'";
    if (tempo==3):
        tacts-=1;

    dur_mol="\\major";

    projectFile.write(header)
    projectFile.write("{ \\key " + 'c' + dur_mol + " \\transpose c " + 'c' + "{");
    projectFile.write(" \\time %d/4" % tempo)

    values = 0;
    tempRandRymth=rythms[randint(0, 4)];        #pierwsza nuta
    values+=getRythmValue(tempRandRymth);       #zebranie wartosci rytmicznej pierwszej nuty
    projectFile.write(startingNote + tempRandRymth);    #zapisanie pierwszej nuty do pliku

    randNote = notes[randint(0, 10)];
    for el in range(0, tacts*4):
        randomRythm = rythms[randint(0, 4)];
        if (values>tempo*4-6 and values <=tempo*4): #values to jest chyba liczba 16-tek, razy 4 bo cwiercnuta to 4 16-tki
            rest=tempo*4-values;                    #-6 bo moze wylosowac cwiercnute z kropka
            for el in range(0, rest):
                if (randNote != " r"):
                    randNote = randNote + changedNote[randint(0, 3)];   #dodanie krzyzyka/bemola
                    randNote += changedOctave[randint(0, 2)];           #dodanie oktawy
                    NOTES.append(randNote);                #wektor wszystkich nut ktore zostaly stworzone
                    #chce zeby byl interwal ponizej oktawy:
                    indexLast = allNotes.index(NOTES[len(NOTES) - 1]);
                    index2fromEnd = allNotes.index(NOTES[len(NOTES) - 2]);
                    distance = abs(indexLast - index2fromEnd);
                    while (True):
                        if (distance > 21): #jezeli interwal jest powyzej oktawy to:
                            randNote = notes[randint(0, 10)];       #losuje nowa nute
                            randNote = randNote + changedNote[randint(0, 3)];  # dodanie krzyzyka/bemola
                            randNote += changedOctave[randint(0, 2)];       #dodanie oktawy

                            NOTES = NOTES[:-1];
                            NOTES.append(randNote);
                        else:
                            projectFile.write(randNote + "16");     #jeżeli jest ponizej oktawy to dodaje do tego taktu 16-tke
                            break;
                else:
                    projectFile.write(randNote + "16");
                values += 1;


            else:   #jezeli nie jest to koniec taktu to:
                randNote = notes[randint(0, len(notes) - 1)];
                randNote += changedNote[randint(0, 3)];  # dodanie krzyzyka/bemola
                randNote += changedOctave[randint(0, 2)];  # dodanie oktawy
                NOTES.append(randNote);
                projectFile.write(randNote + randomRythm);



    print(NOTES);

    projectFile.write(' \\bar "||"');
    projectFile.write("} }");
