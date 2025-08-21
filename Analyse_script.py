# Load "18_08_2025_Umsatzliste_Girokonto.csv" with pandas
import pandas as pd
import matplotlib.pyplot as plt
import calendar

df = pd.read_csv("18_08_2025_Umsatzliste_Girokonto.csv", sep=";", header=3)

# Formatiere so, dass die Spalten komplett geschrieben werden ohne "..."
pd.set_option("display.max_columns", None)
pd.set_option("display.expand_frame_repr", False)

# Remove columns 1, 2, -1, -2, -3
df = df.drop(df.columns[[1, 2, -1, -2, -3]], axis=1)
# print(" ")
# print(df.head(20))

# Ändere den Namen der Spalte "Betrag (€)" zu "Betrag"
df = df.rename(columns={"Betrag (€)": "Betrag"})

# In Spalte Betrag ersetze "," durch "."
df["Betrag"] = df["Betrag"].str.replace(".", "", regex=False)
df["Betrag"] = df["Betrag"].str.replace(",", ".", regex=False)

# Schreibe den Datentyp der Spalte "Betrag" um
df["Betrag"] = df["Betrag"].astype(float)
df["Verwendungszweck"] = df["Verwendungszweck"].astype(str)

# Füge zwei Spalten "Kategorie" und "Unterkategorie" hinzu
df["Kategorie"] = ""
df["Unterkategorie"] = ""

# Lösche alle Transaktionen mit weniger als 0.01 € Betrag
df = df[abs(df["Betrag"]) > 0.01]

# Befülle die Spalte Kategorie automatisiert
def categorize_transaction(row):
    if "Tankstelle" in row["Zahlungsempfänger*in"]:
        return "Tanken"
    elif "Mensa Stuttgart-Vaihingen" in row["Zahlungsempfänger*in"]:
        return "Uni Essen"
    elif "BAECKER" in row["Zahlungsempfänger*in"]:
        return "Bäckerei"
    elif "REWE" in row["Zahlungsempfänger*in"]:
        return "Supermarkt"
    elif "ALDI" in row["Zahlungsempfänger*in"]:
        return "Supermarkt"
    elif "LIDL" in row["Zahlungsempfänger*in"]:
        return "Supermarkt"
    elif "PayPal" in row["Zahlungsempfänger*in"]:
        return "PayPal"
    elif "Amazon" in row["Zahlungsempfänger*in"]:
        return "Amazon"
    elif "EDEKA" in row["Zahlungsempfänger*in"]:
        return "Supermarkt"
    elif "SumUp" in row["Zahlungsempfänger*in"]:
        return "Uni Essen"
    elif "Kaufland" in row["Zahlungsempfänger*in"]:
        return "Supermarkt"
    elif "Cafeteria" in row["Zahlungsempfänger*in"]:
        return "Uni Essen"
    elif "klaus roth" in row["Zahlungsempfänger*in"]:
        return "Supermarkt"
    elif "DEVK" in row["Zahlungsempfänger*in"]:
        return "Versicherung"
    elif "McDonald" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "Stefanie Lopez" in row["Zahlungsempfänger*in"]:
        return "Miete"
    elif "Subway" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "Restaurant" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "DB Vertrieb" in row["Zahlungsempfänger*in"]:
        return "Deutsche Bahn"
    elif "Pizza Hut" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "EL.SOMBRERO" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "Oishii" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "Bäckerei" in row["Zahlungsempfänger*in"]:
        return "Bäckerei"
    elif "Burger" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "Bauhaus" in row["Zahlungsempfänger*in"]:
        return "Baumarkt"
    elif "Nanu-Nana" in row["Zahlungsempfänger*in"]:
        return "Sonstiges"
    elif "ACCES.SERVICE.STATION/STUTTGART" in row["Zahlungsempfänger*in"]:
        return "Tanken"
    elif "Curry.Corner" in row["Zahlungsempfänger*in"]:
        return "Uni Essen"
    elif "Agip" in row["Zahlungsempfänger*in"]:
        return "Tanken"
    elif "Saarland Versicherung" in row["Zahlungsempfänger*in"]:
        return "Versicherung"
    elif "Saarland Feuerversicherung" in row["Zahlungsempfänger*in"]:
        return "Auto Versicherung"
    elif "Volksbank" in row["Zahlungsempfänger*in"]:
        return "Geld abheben"
    elif "Apotheke" in row["Zahlungsempfänger*in"]:
        return "Apotheke"
    elif "Backkultur" in row["Zahlungsempfänger*in"]:
        return "Bäckerei"
    elif "Zeit für Brot" in row["Zahlungsempfänger*in"]:
        return "Bäckerei"
    elif "BAUSTOFFE RAIMUND LESCH" in row["Zahlungsempfänger*in"]:
        return "Baumarkt"
    elif "ING-DiBa AG" in row["Zahlungsempfänger*in"]:
        return "Kapitalanlage"
    elif "Scalable Capital" in row["Zahlungsempfänger*in"]:
        return "Kapitalanlage"
    elif "Tanzschule" in row["Zahlungsempfänger*in"]:
        return "Kurs"
    elif "Gloria" in row["Zahlungsempfänger*in"]:
        return "Eintritt"
    elif "Cafeteria Hochschule für Technik" in row["Zahlungsempfänger*in"]:
        return "Uni Essen"
    elif "AMAZON" in row["Zahlungsempfänger*in"]:
        return "Amazon"
    elif "Shell" in row["Zahlungsempfänger*in"]:
        return "Tanken"
    elif "Stadt.Herrenberg/Herrenberg" in row["Zahlungsempfänger*in"]:
        return "Parkticket"
    elif "Klaus.Roth" in row["Zahlungsempfänger*in"]:
        return "Supermarkt"
    elif "Brauhaus" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "Klaus.Roth" in row["Zahlungsempfänger*in"]:
        return "Supermarkt"
    elif "Brauhaus" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "ADRIAN.EMANUEL.EBERHAR/STUTTGART" in row["Zahlungsempfänger*in"]:
        return "Sonstiges"
    elif "Lohn" in row["Verwendungszweck"]:
        return "Einkommen"
    elif "KREDITKARTENABRECHNUNG" in row["Verwendungszweck"]:
        return "Urlaub Sonstiges"
    elif "Lago Maggiore" in row["Verwendungszweck"]:
        return "Urlaub Sonstiges"
    elif "ECSA.Monteggio.Sessa/Sessa" in row["Zahlungsempfänger*in"]:
        return "Urlaub Essen"
    elif "Gotthard Raststätte" in row["Zahlungsempfänger*in"]:
        return "Urlaub Essen"
    elif "Deutsche Post" in row["Zahlungsempfänger*in"]:
        return "Sonstiges"
    elif "Deutsches Komitee fuer UNICEF e.V." in row["Zahlungsempfänger*in"]:
        return "Spenden"
    elif "ERSTATT.97831/10996 EST-VERANL. 24" in row["Verwendungszweck"]:
        return "Einkommen"
    elif "Do.Quan/Hamburg" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "cafe" in row["Zahlungsempfänger*in"]:
        return "Bäckerei"
    elif "Rundfunk" in row["Zahlungsempfänger*in"]:
        return "Abgaben"
    elif "ROCCADION" in row["Zahlungsempfänger*in"]:
        return "Eintritt"
    elif "JET" in row["Zahlungsempfänger*in"]:
        return "Tanken"
    elif "Mensa.Vaihingen" in row["Zahlungsempfänger*in"]:
        return "Uni Essen"
    elif "Schuh" in row["Zahlungsempfänger*in"]:
        return "Kleidung"
    elif "Baumarkt" in row["Zahlungsempfänger*in"]:
        return "Baumarkt"
    elif "Zettle..Hollerbusch...D/Hauenstein" in row["Zahlungsempfänger*in"]:
        return "Bäckerei"
    elif "FRECH.POSTPLATZ/BOEBLINGEN" in row["Zahlungsempfänger*in"]:
        return "Bäckerei"
    elif "WERNER.BOST.MUEHLENBAE/WALLERFANGEN" in row["Zahlungsempfänger*in"]:
        return "Bäckerei"
    elif "WASGAU" in row["Zahlungsempfänger*in"]:
        return "Supermarkt"
    elif "Sparkasse" in row["Zahlungsempfänger*in"]:
        return "Geld abheben"
    elif "TT.RACES.MERCHANDISE/CHEADLE" in row["Zahlungsempfänger*in"]:
        return "Kleidung"
    elif "Marian Rockenhäuser" in row["Zahlungsempfänger*in"]:
        return "Sonstiges"
    elif "RESTAURANT" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "Fuel" in row["Zahlungsempfänger*in"]:
        return "Tanken"
    elif "Digitalnautic" in row["Zahlungsempfänger*in"]:
        return "Urlaub Sonstiges"
    elif "ARIANE HASCHKA" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "FRANKFURT.DE" in row["Zahlungsempfänger*in"]:
        return "Sonstiges"
    elif "CONSORZIO.MOTOSCAFISTI/STRESA" in row["Zahlungsempfänger*in"]:
        return "Urlaub Sonstiges"
    elif "BIGLIETTERIA.ISOLA.BELL/STRESA" in row["Zahlungsempfänger*in"]:
        return "Urlaub Sonstiges"
    elif "CAFFETTERIA.ISOLA.BELLA/STRESA" in row["Zahlungsempfänger*in"]:
        return "Urlaub Essen"
    elif "LANDESHAUPTSTADT.STUTT/STUTTGART" in row["Zahlungsempfänger*in"]:
        return "Parkticket"
    elif "Nautica" in row["Zahlungsempfänger*in"]:
        return "Urlaub Sonstiges"
    elif "Parking" in row["Zahlungsempfänger*in"]:
        return "Urlaub Sonstiges"
    elif "Roedean.Cafe.and.Mini.G/Brighton" in row["Zahlungsempfänger*in"]:
        return "Urlaub Essen"
    elif "AUTOHAUS.STAUCH/FILDERSTADT" in row["Zahlungsempfänger*in"]:
        return "Tanken"
    elif "RISTOR..VILLA.BIANCA/GHIFFA" in row["Zahlungsempfänger*in"]:
        return "Urlaub Essen"
    elif "23.06.25" in row["Buchungsdatum"]:
        return "Urlaub Sonstiges"
    elif "SQ..SALTMARSH.FARMHOUSE/Seaford" in row["Zahlungsempfänger*in"]:
        return "Urlaub Essen"
    elif "30.05.25" in row["Buchungsdatum"] or "27.05.25" in row["Buchungsdatum"] or "26.05.25" in row["Buchungsdatum"]:
        return "Urlaub Sonstiges"
    elif "Bäckerhaus" in row["Zahlungsempfänger*in"]:
        return "Bäckerei"
    elif "PIZZERIA" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "LE.PETIT.COQ" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "Buergerhaus" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "ASIA.GOURMET" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "Theaterhaus" in row["Zahlungsempfänger*in"]:
        return "Eintritt"
    elif "Sehne" in row["Zahlungsempfänger*in"]:
        return "Bäckerei"
    elif "Herber +amp Pitz" in row["Zahlungsempfänger*in"]:
        return "Auto Werkstatt"
    elif "Ratskeller" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "DLR" in row["Zahlungsempfänger*in"]:
        return "Spenden"
    elif "HEINZ MICHAEL TSCHOEPE" in row["Zahlungspflichtige*r"]:
        return "Kapitalanlage"
    elif "Kfz-Steuer fuer BB AA 102" in row["Verwendungszweck"]:
        return "Auto Steuern"
    elif "Schnitzelbar...Dornbirn/Dornbirn" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "UK GOV Visa & Immigration" in row["Zahlungsempfänger*in"]:
        return "Urlaub Sonstiges"
    elif "Avec.Store/Stuttgart" in row["Zahlungsempfänger*in"]:
        return "Supermarkt"
    elif "Baeckerei" in row["Zahlungsempfänger*in"]:
        return "Bäckerei"
    elif "CAFE" in row["Zahlungsempfänger*in"]:
        return "Bäckerei"
    elif "Ristorante" in row["Zahlungsempfänger*in"]:
        return "Restaurant"

    elif "Martin Tschoepe" in row["Zahlungspflichtige*r"]:
        return "Kapitalanlage"
    elif "Martin Tschope" in row["Zahlungspflichtige*r"]:
        return "Kapitalanlage"
    elif "Kreisssparkasse" in row["Zahlungsempfänger*in"]:
        return "Geld abheben"
    elif "Cafeteria.Denkpause/Stuttgart" in row["Zahlungspflichtige*r"]:
        return "Uni Essen"
    elif "AUTOHAUS.HAEMMERLE.GMBH/Herrenberg" in row["Zahlungsempfänger*in"]:
        return "Tanken"
    elif "WASCHHAUS.BIOREINIGUNG/Stuttgart" in row["Zahlungsempfänger*in"]:
        return "Kleidung"
    elif "Mitgliedsbeitrag HV THW Illingen" in row["Verwendungszweck"]:
        return "Spenden"
    elif "Ansparen Auto 6000 Euro" in row["Verwendungszweck"]:
        return "Kapitalanlage"
    elif "Mario Zinßer" in row["Zahlungspflichtige*r"]:
        return "Urlaub Sonstiges"
    elif "Mario Zinßer" in row["Zahlungsempfänger*in"]:
        return "Urlaub Sonstiges"
    elif "Udos.GmbH/Stuttgart" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "VIELEN.DANK/STUTTGART" in row["Zahlungsempfänger*in"]:
        return "Sonstiges"
    elif "POKKEZ/STUTTGART" in row["Zahlungsempfänger*in"]:
        return "Uni Essen"
    elif "Deutsche Physikalische Gesellschaft e.V." in row["Zahlungsempfänger*in"]:
        return "Spenden"
    elif "WIRTSHAUS" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "easyJet" in row["Zahlungsempfänger*in"]:
        return "Urlaub Flüge"
    elif "KRUU.COM..5024C23.FB/BAD.FRIEDRICH" in row["Zahlungsempfänger*in"]:
        return "Sonstiges"
    elif "Cafe" in row["Zahlungsempfänger*in"]:
        return "Bäckerei"
    elif "SYNCRO24  Beitragskonto 3228" in row["Zahlungsempfänger*in"]:
        return "Versicherung"
    elif "UZR.Illusion.GmbH/Stuttgart" in row["Zahlungsempfänger*in"]:
        return "Eintritt"
    elif "Bäkerei" in row["Zahlungsempfänger*in"]:
        return "Bäckerei"
    elif "Genusswerkstatt Wanner" in row["Zahlungsempfänger*in"]:
        return "Bäckerei"
    elif "BaeCKEREI" in row["Zahlungsempfänger*in"]:
        return "Bäckerei"
    elif "DKV KRANKENVERS. AG" in row["Zahlungsempfänger*in"]:
        return "Versicherung"
    elif "SCHWANGAU" in row["Zahlungsempfänger*in"]:
        return "Urlaub Sonstiges"
    elif "Nebenkosten für 2 Monate" in row["Verwendungszweck"]:
        return "Miete"
    elif "Peek & Cloppenburg" in row["Zahlungsempfänger*in"]:
        return "Kleidung"
    elif "STADT FUESSEN" in row["Zahlungsempfänger*in"]:
        return "Parkticket"
    elif "Frittenwerk" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "GUSTAGGIO.HERRENBERG/HERRENBERG" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "Express.Kebap/Herrenberg" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "COC.AUSZEIT.UND.GENUSS/HERRENBERG" in row["Zahlungsempfänger*in"]:
        return "Bäckerei"
    elif "LTI..AROSA.TIX/Lenzerheide.L" in row["Zahlungspflichtige*r"]:
        return "Eintritt"
    elif "EM.Theater/Stuttgart" in row["Zahlungsempfänger*in"]:
        return "Eintritt"
    elif "Oman Air" in row["Zahlungsempfänger*in"]:
        return "Urlaub Flüge"
    elif "WANNER.GMBH/HERRENBERG" in row["Zahlungsempfänger*in"]:
        return "Bäckerei"
    elif "Schwedenschanze/Lochau" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "DLR e.V." in row["Zahlungspflichtige*r"]:
        return "Einkommen"
    elif "Sarah Suchaneck" in row["Zahlungspflichtige*r"]:
        return "Urlaub Sonstiges"
    elif "DKB AG" in row["Zahlungspflichtige*r"]:
        return "Kapitalanlage"
    elif "Deutscher Alpenverein (DAV) Sektion Stuttgart" in row["Zahlungspflichtige*r"]:
        return "Eintritt"
    elif "ma ts" in row["Zahlungspflichtige*r"]:
        return "Sonstiges"
    elif "DAV Sektion Stuttgart" in row["Zahlungsempfänger*in"]:
        return "Eintritt"
    elif "WWW.LIZENZSTAR.DE/LONDON" in row["Zahlungsempfänger*in"]:
        return "Sonstiges"
    elif "Saturn" in row["Zahlungsempfänger*in"]:
        return "Sonstiges"
    elif "Napolivibes/Neuhausen" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "Deutscher Alpenverein (DAV) Sektion Stuttgart" in row["Zahlungsempfänger*in"]:
        return "Eintritt"
    elif "HANS IM GLÜCK" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "NARU...Traditions.of.Ja/Saarlouis" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "VEGAN.BURGER.RESTAURAN/DUBAI" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "SOHAR.INT.BANK.SOHAR/MUSCAT.REGION" in row["Zahlungsempfänger*in"]:
        return "Urlaub Sonstiges"
    elif "A.AKCAY.HOTEL.FUESSEN/FUESSEN" in row["Zahlungsempfänger*in"]:
        return "Urlaub Sonstiges"
    elif "SANTA.POD.RACEWAY/PODINGTON" in row["Zahlungsempfänger*in"]:
        return "Urlaub Sonstiges"
    elif "PINAR.FOOD.DRINK/STUTTGART" in row["Zahlungsempfänger*in"]:
        return "Restaurant"
    elif "DAYS.HOTEL.WDDL/DUBAI" in row["Zahlungsempfänger*in"]:
        return "Urlaub Essen"
    elif "Dollar Car Rental" in row["Zahlungsempfänger*in"]:
        return "Urlaub Sonstiges"
    elif "k kiosk" in row["Zahlungsempfänger*in"]:
        return "Sonstiges"
    else:
        return "Nicht-zugeordnet"
df["Unterkategorie"] = df.apply(categorize_transaction, axis=1)


# Schreibe eine Liste mit allen Unterkategorien sortiert in alphabetischer Reihenfolge
print(sorted(df["Unterkategorie"].unique()))

# Schreibe eine Liste mit allen Unterkategorien sortiert häufigkeit und schreibe die Häufigkeit dahinter
print(df["Unterkategorie"].value_counts())

# # Fülle die Spalte Kategorie automatisiert
# def categorize_main_category(row):
#     if row["Unterkategorie"] in ["Urlaub Flüge", "Urlaub Essen", "Urlaub Sonstiges", "Eintritt"]:
#         return "Freizeitgestaltung"
#     elif row["Unterkategorie"] in ["Tanken", "Parkticket", "Auto Steuern", "Auto Versicherung", "Auto Werkstatt"]:
#         return "Auto"
#     elif row["Unterkategorie"] in ["Einkommen"]:
#         return "Einkommen"
#     elif row["Unterkategorie"] in ["Restaurant", "Bäckerei", "Uni Essen"]:
#         return "Essen"
#     elif row["Unterkategorie"] in ["Amazon", "Baumarkt", "Kleidung", "Apotheke", "Supermarkt"]:
#         return "Kaufen"    
#     elif row["Unterkategorie"] in ["Miete"]:
#         return "Miete"
#     elif row["Unterkategorie"] in ["Kapitalanlage"]:
#         return "Kapitalanlage"
#     elif row["Unterkategorie"] in ["Sonstiges", "Abgaben", "PayPal", "Deutsche Bahn", "Kurs", "Spenden", "Versicherung", "Geld abheben"]:
#         return "Sonstiges"
#     else:
#         return "Nicht-zugeordnet"

# Erstelle ein Dictionary für die Zuordnung zwischen Unterkategorie und Kategorie
# und wende es auf die Spalte "Unterkategorie" an, um die Spalte "Kategorie" zu füllen
category_mapping = {
    "Urlaub Flüge": "Freizeitgestaltung",
    "Urlaub Essen": "Freizeitgestaltung",
    "Urlaub Sonstiges": "Freizeitgestaltung",
    "Eintritt": "Freizeitgestaltung",
    "Tanken": "Auto",
    "Parkticket": "Auto",
    "Auto Steuern": "Auto",
    "Auto Versicherung": "Auto",
    "Auto Werkstatt": "Auto",
    "Einkommen": "Einkommen",
    "Restaurant": "Essen",
    "Bäckerei": "Essen",
    "Uni Essen": "Essen",
    "Amazon": "Kaufen",
    "Baumarkt": "Kaufen",
    "Kleidung": "Kaufen",
    "Apotheke": "Kaufen",
    "Supermarkt": "Kaufen",
    "Miete": "Miete",
    "Kapitalanlage": "Kapitalanlage",
    "Sonstiges": "Sonstiges",
    "Abgaben": "Sonstiges",
    "PayPal": "Sonstiges",
    "Deutsche Bahn": "Sonstiges",
    "Kurs": "Sonstiges",
    "Spenden": "Sonstiges",
    "Versicherung": "Sonstiges",
    "Geld abheben": "Sonstiges"
}

df["Kategorie"] = df["Unterkategorie"].map(category_mapping)

# Schreibe 20 Zeilen ins Terminal bei denen df["Unterkategorie"] == "Nicht-zugeordnet"
print(df[df["Unterkategorie"] == "Nicht-zugeordnet"].head(20))

print(" ")

print(len(df[df["Unterkategorie"] == "Nicht-zugeordnet"]))
print(len(df))

# Buchungsdatum hat aktuell das Format TT.MM.JJ. Füge beim Jahr "20" hinzu. Beispiel: 12.03.25 -> 12.03.2025
df["Buchungsdatum"] = df["Buchungsdatum"].apply(lambda x: x[:6] + "20" + x[6:] if len(x) == 8 else x)

df["Buchungsdatum"] = pd.to_datetime(df["Buchungsdatum"], format="%d.%m.%Y")

# Füge eine Spalte Monat zu df hinzu und nehme den Wert aus dem Buchungsdatum Beispiel 12.03.25 -> 03
df["Monat"] = df["Buchungsdatum"].dt.month

# Füge eine Spalte Jahr zu df hinzu und nehme den Wert aus dem Buchungsdatum Beispiel 12.03.25 -> März
df["Jahr"] = df["Buchungsdatum"].dt.year

# Entferne die Zeilen mit Unterkategorie "Kapitalanlage" oder "Einkommen"
df = df[~df["Unterkategorie"].isin(["Kapitalanlage", "Einkommen"])]

# Entferne alle Datenpunkte von 2024
df = df[df["Jahr"] != 2024]

# Erstelle eine neue Datenbank bei der die Spaltennamen jeweile den Namen Unterkategorie aus der Datenbank df entsprechen
# Es soll jeder Monat angelegt werden, egal ob er vorkommt oder nicht. Wenn es in ener Kategorie keinen Beträge gibt, dann soll 0 eingetragen werden.
# Gib den Spalten die entsprechenden Namen
def create_month_and_year_report(df, category):
    # Group by month and year, summing the amounts for each category
    monthly_report = df.groupby(["Monat", "Jahr", category])["Betrag"].sum().unstack(fill_value=0)
    
    return monthly_report

df_monthly_unterkategorie = create_month_and_year_report(df, "Unterkategorie")
df_monthly_kategorie = create_month_and_year_report(df,"Kategorie")

print(" ")
print(df_monthly_unterkategorie)

print(" ")
print(df_monthly_kategorie)

# Erstelle analog eine Datenbanke für die Jahre
def create_year_report(df, category):
    # Group by year, summing the amounts for each category
    yearly_report = df.groupby(["Jahr", category])["Betrag"].sum().unstack(fill_value=0)
    return yearly_report

df_yearly_unterkategorie = create_year_report(df, "Unterkategorie")
df_yearly_kategorie = create_year_report(df,"Kategorie")

# Ersetzte alle positiven Werte durch 0 und nehme den Betrag der negativen Werte
def remove_negatives_and_take_absolute_values(dataframe):
    dataframe[dataframe > 0] = 0
    dataframe = dataframe.abs()
    return dataframe

df_monthly_kategorie = remove_negatives_and_take_absolute_values(df_monthly_kategorie)
df_yearly_kategorie = remove_negatives_and_take_absolute_values(df_yearly_kategorie)
df_monthly_unterkategorie = remove_negatives_and_take_absolute_values(df_monthly_unterkategorie)
df_yearly_unterkategorie = remove_negatives_and_take_absolute_values(df_yearly_unterkategorie)

# Erstelle Gitter mit mehreren Plots und Ordne sie an. Die Anzahl soll der Anzahl Monate in 2025 entsprechen.
# Jeder Plot soll ein Tortendiagramm für df_monthly_kategorie sein.
# Beginne mit dem Erstellen einer Liste von Monaten bei denen df_monthly_kategorie im Jahr 2025 existiert.
months_with_data = df_monthly_kategorie[df_monthly_kategorie.index.get_level_values("Jahr") == 2025].index.get_level_values("Monat").unique().tolist()

fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 10))
axes = axes.flatten()

for i in months_with_data:
    df_monthly_kategorie.loc[i, 2025].plot.pie(autopct="%.1f%%", ax=axes[i-1])
    axes[i-1].set_title(f"Ausgaben im {calendar.month_name[i]} 2025 nach Kategorien")

# Füge als 9. Plot eine Gesamtübersicht für 2025 hinzu
df_yearly_kategorie.loc[2025].plot.pie(autopct="%.1f%%", ax=axes[8])
axes[8].set_title("Gesamtausgaben im Jahr 2025 nach Kategorien")

plt.tight_layout()

# # Entferne leere Subplots
# for i in range(len(months_with_data), 9+1):
#     fig.delaxes(axes[i])

# Es gibt eine vertikale Schrift (1, 2025). Diese wird mit folgender Zeile entfernt.
for ax in axes:
    ax.set_ylabel("")  # Remove the y-label for each subplot

plt.show()

# Erstelle eine Jahresübersicht für 2025 mit den Informationen aus df_yearly_unterkategorie und dem dictionary category_mapping
# Es soll erstmal eine Liste mit folgenden Kategorien erstellt werden, die in Tortendiagrammen genauer analysiert werden sollen: 
# "Freizeitgestaltung"
# "Auto"
# "Essen"
# "Kaufen"
# "Sonstiges"
# Anschließend soll ein Gitter aus Tortendiagrammen für die einzelnen Kategorien erstellt werden. Leere Subplots werden Entfernt.
# Dabei muss in der Schleife immer im dicationary geschaut werden welche Unterkategorien zu einer Kategorie gehören.

categories_of_interest = ["Freizeitgestaltung", "Auto", "Essen", "Kaufen", "Sonstiges"]

fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 12))
axes = axes.flatten()

for i, category in enumerate(categories_of_interest):
    df_yearly_unterkategorie_temp = df_yearly_unterkategorie.copy()
    for subcategory in df_yearly_unterkategorie.columns:
        if category_mapping[subcategory] != category:
            df_yearly_unterkategorie_temp.drop(subcategory, axis=1, inplace=True)
    df_yearly_unterkategorie_temp.loc[2025].plot.pie(autopct="%.1f%%", ax=axes[i])
    axes[i].set_title(f"Ausgaben für {category} im Jahr 2025")

# Füge als 9. Plot eine Gesamtübersicht für 2025 hinzu
df_yearly_kategorie.loc[2025].plot.pie(autopct="%.1f%%", ax=axes[5])
axes[5].set_title("Gesamtausgaben im Jahr 2025 nach Kategorien")

# Es gibt eine vertikale Schrift (1, 2025). Diese wird mit folgender Zeile entfernt.
for ax in axes:
    ax.set_ylabel("")  # Remove the y-label for each subplot

plt.tight_layout()
plt.show()


# Erstelle ein Diagramm in dem das Dictionary category_mapping visualisiert wird
# In der obersten Zeile sollen die Namen der Kategorien stehen
# In den zugehörigen Zeilen stehen dann die Unterkategorien
# Je mehr Unterkategorien es gibt, desto mehr Zeilen werden benötigt.

import matplotlib.pyplot as plt
import pandas as pd
from collections import defaultdict

# Umkehren: Hauptkategorie -> Liste von Unterkategorien
reverse_mapping = defaultdict(list)
for subcat, maincat in category_mapping.items():
    reverse_mapping[maincat].append(subcat)

max_len = max(len(v) for v in reverse_mapping.values())

data = {}
for maincat, subcats in reverse_mapping.items():
    data[maincat] = subcats + ["" for _ in range(max_len - len(subcats))]

df = pd.DataFrame(data)

# Tabelle plotten
fig, ax = plt.subplots(figsize=(12,6))
ax.axis("off")

table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc="center",
    cellLoc="center"
)
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Header farbig hinterlegen & dickerer oberer Rand
for key, cell in table.get_celld().items():
    row, col = key
    # Header-Zeile einfärben
    if row == 0:
        cell.set_facecolor("#cccccc")   # hellgrau
        cell.set_edgecolor("black")
        cell.set_linewidth(2)           # dickerer oberer Rand
    else:
        # vertikale Striche entfernen
        cell.set_edgecolor("white")     # unsichtbar machen
        cell.set_linewidth(0.5)

# Füge eine Randbemerkung hinzu, dass "Einkommen" und "Kapitalanlagen" nicht in den Plots für die Ausgaben berücksichtigt werden
plt.figtext(0.5, 0.01, "Hinweis: 'Einkommen' und 'Kapitalanlagen' sind nicht in den Ausgaben-Analysen enthalten.", ha="center", fontsize=10)

plt.show()