import csv
from unesco.models import Category, State, Region, Iso, Site


def run():
    fhand = open('unesco/whc-sites-2018.csv')
    reader = csv.reader(fhand)
    next(reader)

    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    for row in reader:
        # print(row)
        c, created = Category.objects.get_or_create(name = row[7])
        s, created = State.objects.get_or_create(name = row[8])
        r, created = Region.objects.get_or_create(name = row[9])
        i, created = Iso.objects.get_or_create(name = row[10])

        try:
            ah = float(row[6])
        except:
            ah = None

        site = Site(
            name = row[0],
            description = row[1],
            justification = row[2],
            year = row[3],
            longitude = row[4],
            latitude = row[5],
            area_hectares = ah,

            category = c,
            state = s,
            region = r,
            iso = i
        )

        site.save()
