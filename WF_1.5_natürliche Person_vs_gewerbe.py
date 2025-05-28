/*

*/

SELECT * FROM public.einheiten_stromspeicher_ungefiltert_1 Limit 200;

CREATE MATERIALIZED VIEW IF NOT EXISTS nat_pers_condensed_4 AS
SELECT
    mastr_nr_der_einheit,
    bruttoleistung_einheit,
    nettonennleistung_einheit,
    inbetriebnahmedatum_einheit,
    bundesland,
    nutzbare_speicherkapazitaet_kwh,
    mastr_nr_anlagenbetreiber,
    volleinspeisung_teileinspeisung,
	name_anlagenbetreiber
FROM einheiten_stromspeicher_ungefiltert_1
WHERE name_anlagenbetreiber LIKE '%natürliche Person%';

SELECT * FROM nat_pers_condensed_4 ;


CREATE MATERIALIZED VIEW IF NOT EXISTS nat_pers_verteilung_nach_Kapazitaet AS
SELECT
    COUNT(*) FILTER (WHERE nutzbare_speicherkapazitaet_kwh >0  AND nutzbare_speicherkapazitaet_kwh <= 5)  AS kap_0_5,
    COUNT(*) FILTER (WHERE nutzbare_speicherkapazitaet_kwh > 5 AND nutzbare_speicherkapazitaet_kwh <= 10) AS kap_5_10,
    COUNT(*) FILTER (WHERE nutzbare_speicherkapazitaet_kwh >10 AND nutzbare_speicherkapazitaet_kwh <= 15) AS kap_10_15,
    COUNT(*) FILTER (WHERE nutzbare_speicherkapazitaet_kwh >15 AND nutzbare_speicherkapazitaet_kwh <= 20) AS kap_15_20,
    COUNT(*) FILTER (WHERE nutzbare_speicherkapazitaet_kwh >20 AND nutzbare_speicherkapazitaet_kwh <= 25) AS kap_20_25,
    COUNT(*) FILTER (WHERE nutzbare_speicherkapazitaet_kwh >25) 											AS kap_25_plus
FROM nat_pers_condensed_4;

CREATE MATERIALIZED VIEW IF NOT EXISTS gesamt_verteilung_nach_Kapazitaet AS
SELECT
    COUNT(*) FILTER (WHERE nutzbare_speicherkapazitaet_kwh >0  AND nutzbare_speicherkapazitaet_kwh <= 5)  AS kap_0_5,
    COUNT(*) FILTER (WHERE nutzbare_speicherkapazitaet_kwh >5  AND nutzbare_speicherkapazitaet_kwh <= 10) AS kap_5_10,
    COUNT(*) FILTER (WHERE nutzbare_speicherkapazitaet_kwh >10 AND nutzbare_speicherkapazitaet_kwh <= 15) AS kap_10_15,
    COUNT(*) FILTER (WHERE nutzbare_speicherkapazitaet_kwh >15 AND nutzbare_speicherkapazitaet_kwh <= 20) AS kap_15_20,
    COUNT(*) FILTER (WHERE nutzbare_speicherkapazitaet_kwh >20 AND nutzbare_speicherkapazitaet_kwh <= 25) AS kap_20_25,
    COUNT(*) FILTER (WHERE nutzbare_speicherkapazitaet_kwh >25) 											AS kap_25_plus
FROM einheiten_stromspeicher_ungefiltert_1;


CREATE MATERIALIZED VIEW IF NOT EXISTS nat_pers_vs_gesamt_verteilung_nach_Kapazitaet_4 AS
SELECT *, 'nat_Pers' AS Art_der_Einheit
FROM nat_pers_verteilung_nach_Kapazitaet
UNION ALL
SELECT *, 'gesamt' AS Art_der_Einheit
FROM gesamt_verteilung_nach_Kapazitaet;

CREATE TABLE nat_pers_vs_gesamt_verteilung_nach_Kapazitaet_tbl AS
SELECT * FROM nat_pers_vs_gesamt_verteilung_nach_Kapazitaet_4;

--speichern als csv
COPY (SELECT * FROM nat_pers_vs_gesamt_verteilung_nach_Kapazitaet_tbl) TO 'C:/data/marktstammdatenregister/nat_pers_vs_gesamt_verteilung_nach_Kapazitaet_tbl.csv' WITH CSV HEADER;

SELECT * FROM nat_pers_vs_gesamt_verteilung_nach_Kapazitaet_tbl;
