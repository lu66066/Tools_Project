def import_squirrel_data(path):
    import csv
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Sighting.objects.get_or_create(
                X=row[0],
                Y=row[1],
                Unique_Squirrel_ID=row[2],
                Hectare=row[3],
                Shift=row[4],
                Date=row[5],
                Hectare_Squirrel_Number=row[6],
                Age=row[7],
                Primary_Fur_Color=row[8],
                Highlight_Fur_Color=row[9],
                Color_Notes=row[10],
                Location=row[11],
                Above_Ground_Sighter_Measurement=row[12],
                Specific_Location=row[13],
                Running=row[14],
                Chasing=row[15],
                Climbing=row[16],
                Eating=row[17],
                Foraging=row[18],
                Other_Activities=row[19],
                Kuks=row[20],
                Quaas=row[21],
                Moans=row[22],
                Tail_Flags=row[23],
                Tail_Twitches=row[24],
                Approaches=row[25],
                Indifferent=row[26],
                Runs_From=row[27],
                Other_Interactions=row[28]
                )
