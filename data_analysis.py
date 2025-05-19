
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LogNorm

from ref_speicher_auswert_functions import postgres_session, query_database, compact_df

def add_new_bar_for_gesamt_bat(x, df_l_vs_c_i, list_of_labels):
    colors = sns.color_palette("Dark2", 6)
    ax.bar(x, df_l_vs_c_i.loc[0, 'gesamt'], label=list_of_labels[0], color=colors[0])
    new_bottom_1 = df_l_vs_c_i.loc[0, 'gesamt']
    #percentage = 100 * df_l_vs_c_i.loc[0, 'gesamt']/ sum(df_l_vs_c_i.loc[:, 'gesamt'])
    #ax.text(x, new_bottom_1 - 1, f"{percentage:.1f}%",             ha="center", va="top", color="white", fontsize=12, fontweight="bold")

    ax.bar(x, df_l_vs_c_i.loc[1, 'gesamt'], bottom=new_bottom_1, label=list_of_labels[1], color=colors[1])
    new_bottom_2 = new_bottom_1 + df_l_vs_c_i.loc[1, 'gesamt']
    percentage = 100 * df_l_vs_c_i.loc[1, 'gesamt'] / sum(df_l_vs_c_i.loc[:, 'gesamt'])
    ax.text(x, new_bottom_2 - 10, f"{percentage:.1f}%", ha="center", va="top", color="white", fontsize=12, fontweight="bold")

    ax.bar(x, df_l_vs_c_i.loc[2, 'gesamt'], bottom=new_bottom_2, label=list_of_labels[2], color=colors[2])
    new_bottom_3 = new_bottom_2 + df_l_vs_c_i.loc[2, 'gesamt']
    percentage = 100 * df_l_vs_c_i.loc[2, 'gesamt'] / sum(df_l_vs_c_i.loc[:, 'gesamt'])
    ax.text(x, new_bottom_3 - 10, f"{percentage:.1f}%", ha="center", va="top", color="white", fontsize=12,
            fontweight="bold")

    ax.bar(x, df_l_vs_c_i.loc[3, 'gesamt'], bottom=new_bottom_3, label=list_of_labels[3], color=colors[3])
    new_bottom_4 = new_bottom_3 + df_l_vs_c_i.loc[3, 'gesamt']
    percentage = 100 * df_l_vs_c_i.loc[3, 'gesamt'] / sum(df_l_vs_c_i.loc[:, 'gesamt'])
    ax.text(x, new_bottom_4 - 10, f"{percentage:.1f}%", ha="center", va="top", color="white", fontsize=12,
            fontweight="bold")

    ax.bar(x, df_l_vs_c_i.loc[4, 'gesamt'], bottom=new_bottom_4, label=list_of_labels[4], color=colors[4])
    new_bottom_5 = new_bottom_4 + df_l_vs_c_i.loc[4, 'gesamt']
    percentage = 100 * df_l_vs_c_i.loc[4, 'gesamt'] / sum(df_l_vs_c_i.loc[:, 'gesamt'])
    ax.text(x, new_bottom_5 - 10, f"{percentage:.1f}%", ha="center", va="top", color="white", fontsize=12,
            fontweight="bold")

    ax.bar(x, df_l_vs_c_i.loc[5, 'gesamt'], bottom=new_bottom_5, label=list_of_labels[5], color=colors[5])
    new_bottom_6 = new_bottom_5 + df_l_vs_c_i.loc[5, 'gesamt']
    percentage = 100 * df_l_vs_c_i.loc[5, 'gesamt'] / sum(df_l_vs_c_i.loc[:, 'gesamt'])
    ax.text(x, new_bottom_6 - 10, f"{percentage:.1f}%", ha="center", va="top", color="white", fontsize=12,
            fontweight="bold")




if __name__ == "__main__":

    # dataframes laden aus der Datenbank
        # selects all the data from my PostgreSQL-Database
    schema = 'public'
    list_of_labels= ['0-5 kWh',"5-10 kWh",'10-15 kWh','15-20 kWh','20-25 kWh','25+ kWh']

    con = postgres_session()
    table_bis_23 = 'leistung_vs_kapazitaet_bis_2023_tbl'
    df_l_vs_c_bis_23 = query_database(con, schema, table_bis_23)
    df_l_vs_c_bis_23_compact = compact_df(df_l_vs_c_bis_23)
    #  not possible df_l_vs_c_bis_23_compact_pm = df_l_vs_c_bis_23_compact/12  # hier kann man keine Rate pro Monat ermitteln, weil ja alles bis 2023 einfließt

    con = postgres_session()
    table_23 = 'leistung_vs_kapazitaet_2023_tbl'
    df_l_vs_c_23 = query_database(con, schema, table_23)
    df_l_vs_c_23_compact = compact_df(df_l_vs_c_23)
    df_l_vs_c_23_compact_pm = df_l_vs_c_23_compact/12 # alle Werte werden pro Monat berechnet, da sonst ein Vergleich mit 2025 nicht möglich wäre


    con = postgres_session()
    table_24 = 'leistung_vs_kapazitaet_2024_tbl'
    df_l_vs_c_24 = query_database(con, schema, table_24)
    df_l_vs_c_24_compact = compact_df(df_l_vs_c_24)
    df_l_vs_c_24_compact_pm = df_l_vs_c_24_compact /12

    con = postgres_session()
    table_25 = 'leistung_vs_kapazitaet_01_bis_05_2025_6_tbl'
    df_l_vs_c_25 = query_database(con, schema, table_25)
    df_l_vs_c_25_compact = compact_df(df_l_vs_c_25)
    df_l_vs_c_25_compact_pm = df_l_vs_c_25_compact /4  # weil nur 01.01. - 01.05. analysiert werden (4 Monate)

    df_test = df_l_vs_c_25_compact/ df_l_vs_c_24_compact  # --> ich muss 2024 und 25 nochmal neu machen
    print(df_test)

    print(df_l_vs_c_25_compact)
    print(df_l_vs_c_25_compact_pm)

# ---------------------------------------------------------------------


    # Balkendiagramm erstellen
    fig, ax = plt.subplots(figsize=(8, 6))

    x_labelssss = ['df_l_vs_c_23_compact_pm', 'df_l_vs_c_24_compact_pm', 'df_l_vs_c_25_compact_pm'] # in der End-Darstellung würde hierr einfach [2023,2024,2025] reichen

    #einzelne Diagramme erstellen # formel ist oben/in anderem Dok --> erstellt einfach farblich struktureierte Säulen für die einzelnen Tabellen (Jahre)
    add_new_bar_for_gesamt_bat(x_labelssss[0], df_l_vs_c_23_compact_pm, list_of_labels)
    add_new_bar_for_gesamt_bat(x_labelssss[1], df_l_vs_c_24_compact_pm, list_of_labels)
    add_new_bar_for_gesamt_bat(x_labelssss[2], df_l_vs_c_25_compact_pm, list_of_labels)

    colors = sns.color_palette("Dark2", 6) # "schöne" Farben fürs Balkendiagramm
    #print(colors)

    # Diagramm formatieren
    ax.set_ylabel("Anzahl der Anlagen in der Leistungsklasse")
    ax.set_title("Zubau an Stromspeichern in versch. Leistungsklassen und Jahren ")
    ax.legend(list_of_labels)
    # plt.savefig("Balkendiagramm_Speicher_Zubau_pro_Monat_2023_bis_2025.png", dpi=3000, bbox_inches="tight")
    #plt.show()
    # hier muss ich nochmal gucken... Die Daten von 2025 sing genau gleich wie 2024 * 3,5



# ---------------------------------------------------------------------

    # Heatmap für Leistung vs Kapazität

    # 2025

    plt.figure(figsize=(8, 6))
    hm = sns.heatmap(df_l_vs_c_25_compact_pm.iloc[:,:-1], annot=True, cmap="coolwarm", norm=LogNorm(vmin=df_l_vs_c_25_compact_pm.min().min(), vmax=df_l_vs_c_25_compact_pm.max().max()), linewidths=.5)
    hm.set_yticklabels(list_of_labels, rotation=0)  # Labels setzen, ohne Rotation

    plt.title("Heatmap für Leistung vs Kapazität 2025")
    plt.xlabel("Bruttoleistung")
    plt.ylabel("Kapazität der Batterie")
    plt.savefig("Heatmap_Speicherkapazität_vs_Bruttoleistung_2025.png", dpi=1000, bbox_inches="tight")
    #plt.show()
    # hier sieht man halt den "sweetspot, dass 10-12kW mit 10-15 kWh der absolute "sweetspot" ist momentan
    # --> interessant wäre jetzt halt noch in jeder Zeile einzeln zu untersuchen, wo es am meisten gibt
    #  später "nachweisen" von C=1 Regel mit Heatmat von kwh zu kW


    # 2024

    plt.figure(figsize=(8, 6))
    hm = sns.heatmap(df_l_vs_c_24_compact_pm.iloc[:, :-1], annot=True, cmap="coolwarm",
                     norm=LogNorm(vmin=df_l_vs_c_24_compact_pm.min().min(), vmax=df_l_vs_c_24_compact_pm.max().max()),
                     linewidths=.5)
    hm.set_yticklabels(list_of_labels, rotation=0)  # Labels setzen, ohne Rotation

    plt.title("Heatmap für Leistung vs Kapazität 2024")
    plt.xlabel("Bruttoleistung")
    plt.ylabel("Kapazität der Batterie")
    plt.savefig("Heatmap_Speicherkapazität_vs_Bruttoleistung_2024.png", dpi=1000, bbox_inches="tight")
    #plt.show()

    # 2024

    plt.figure(figsize=(8, 6))
    hm = sns.heatmap(df_l_vs_c_23_compact_pm.iloc[:, :-1], annot=True, cmap="coolwarm",
                     norm=LogNorm(vmin=df_l_vs_c_23_compact_pm.min().min(), vmax=df_l_vs_c_23_compact_pm.max().max()),
                     linewidths=.5)
    hm.set_yticklabels(list_of_labels, rotation=0)  # Labels setzen, ohne Rotation

    plt.title("Heatmap für Leistung vs Kapazität 2023")
    plt.xlabel("Bruttoleistung")
    plt.ylabel("Kapazität der Batterie")
    plt.savefig("Heatmap_Speicherkapazität_vs_Bruttoleistung_2023.png", dpi=1000, bbox_inches="tight")
    plt.show()



    ''' 
    To Do:
    prozentueller Anteil der verschiedenen Leistungsklassen
    natürliche Person filtern (--> alles was "natürliche Person" in Spalte name_anlagenbetreiber hat
    Kreisdiagramm und Balkendiagramm: was gibt es gerade für Batterien im Netz (Gegenüberstellung insgesamt)
    
    '''