dicOfMonths = {"01": "JANUARY", "02": "FEBRUARY", "03": "MARCH", "04": "APRIL", "05": "MAY", "06": "JUNE",
               "07": "JULY", "08": "AUGUST", "09": "SEPTEMBER", "10": "OCTOBER", "11": "NOVEMBER", "12": "DECEMBER"}

inpCountry = "France"
inpDateFirst = "2020-01-25"
inpDateLast = "2020-02-25"

with open("covid_data.txt", "r") as data:

    firstLine = True

    with open(inpCountry + ".txt", "w") as c:

        confirmed = 0
        recovered = 0
        deaths = 0
        dayCount = 0
        isBetweenDate = False

        for i in data:

            if firstLine:
                firstLine = False
                continue

            i = i.replace("\n", "").replace("\t", " ").strip() # Ör: i = "2020-12-05 Denmark 88858 69869 878"
            
            spaceIndex = 0
            spaceIndexes = []
            for j in i:
                if j == " ":
                    spaceIndexes.append(spaceIndex)
                spaceIndex += 1

            country = i[spaceIndexes[0] + 1: spaceIndexes[-3] - 1]
            if country.startswith('Canada'):
                continue

            date = i.split(" ")[0]
            if date == inpDateFirst:  # Tarihler arası
                isBetweenDate = True
            if isBetweenDate and country.startswith(inpCountry):
                confirmed += int(i.split(" ")[-3])
                recovered += int(i.split(" ")[-2])
                deaths += int(i.split(" ")[-1])
                dayCount += 1
            if date == inpDateLast:
                isBetweenDate = False
        # Tarihler arası ortalama
        c.write(f"AVERAGES OF {inpCountry.upper()} BETWEEN {inpDateFirst} <-> {inpDateLast}\nConfirmed: {int(confirmed / dayCount)}\nRecovered: {int(recovered / dayCount)}\nDeaths: {int(deaths / dayCount)}\n\n")

        confirmed = 0
        recovered = 0
        deaths = 0
        dayCount = 0
        data.seek(0)  # İmleci ilk veri satırına taşıyorum
        firstLine = True

        for i in data:

            if firstLine:
                firstLine = False
                continue

            i = i.replace("\n", "").replace("\t", " ").strip()

            spaceIndex = 0
            spaceIndexes = []
            for j in i:
                if j == " ":
                    spaceIndexes.append(spaceIndex)
                spaceIndex += 1

            country = i[spaceIndexes[0] + 1: spaceIndexes[-3] - 1]
            if country.startswith('Canada'):
                continue

            date = i.split(" ")[0]
            # Girilen başlangıç tarihine ait ayın ortalamasını bulmak için gerekli hesaplamalar
            if date.split("-")[1] == inpDateFirst.split("-")[1] and country.startswith(inpCountry):
                confirmed += int(i.split(" ")[-3])
                recovered += int(i.split(" ")[-2])
                deaths += int(i.split(" ")[-1])
                dayCount += 1
        # Girilen başlangıç tarihine ait ayın ortalaması
        c.write("AVERAGES OF " + inpCountry.upper() + " IN " + dicOfMonths[inpDateFirst.split("-")[1]] + 
                f"\nConfirmed: {int(confirmed / dayCount)}\nRecovered: {int(recovered / dayCount)}\nDeaths: {int(deaths / dayCount)}\n\n")
        
        confirmed = 0
        recovered = 0
        deaths = 0
        dayCount = 0
        data.seek(0)  # İmleci ilk veri satırına taşıyorum
        firstLine = True
        
        for i in data:

            if firstLine:
                firstLine = False
                continue

            i = i.replace("\n", "").replace("\t", " ").strip()

            spaceIndex = 0
            spaceIndexes = []
            for j in i:
                if j == " ":
                    spaceIndexes.append(spaceIndex)
                spaceIndex += 1

            country = i[spaceIndexes[0] + 1: spaceIndexes[-3] - 1]
            if country.startswith('Canada'):
                continue

            date = i.split(" ")[0]
            # Girilen bitiş tarihine ait ayın ortalamasını bulmak için gerekli hesaplamalar
            if date.split("-")[1] == inpDateLast.split("-")[1] and country.startswith(inpCountry):
                confirmed += int(i.split(" ")[-3])
                recovered += int(i.split(" ")[-2])
                deaths += int(i.split(" ")[-1])
                dayCount += 1
        # Girilen bitiş tarihine ait ayın ortalaması
        c.write("AVERAGES OF " + inpCountry.upper() + " IN " + dicOfMonths[inpDateLast.split("-")[1]] + 
                f"\nConfirmed: {int(confirmed / dayCount)}\nRecovered: {int(recovered / dayCount)}\nDeaths: {int(deaths / dayCount)}")
