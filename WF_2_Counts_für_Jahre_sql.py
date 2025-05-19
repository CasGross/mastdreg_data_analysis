/* Daten in  2025 

*/

SELECT * FROM public.einheiten_stromspeicher_ungefiltert_1 Limit 200;

CREATE MATERIALIZED VIEW IF NOT EXISTS es_einheiten_01_bis_05_2025_6 AS
SELECT 
    mastr_nr_der_einheit, 
    bruttoleistung_einheit, 
    nettonennleistung_einheit,  
    inbetriebnahmedatum_einheit, 
    bundesland, 
    nutzbare_speicherkapazitaet_kwh, 
    mastr_nr_anlagenbetreiber, 
    volleinspeisung_teileinspeisung
FROM einheiten_stromspeicher_ungefiltert_1
WHERE inbetriebnahmedatum_einheit > '2023-12-31';

SELECT * FROM es_einheiten_01_bis_05_2025_6 LIMIT 200;


CREATE MATERIALIZED VIEW IF NOT EXISTS leistung_vs_kapazitaet_0_5_kw_2025_6 AS
SELECT 
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 0 AND bruttoleistung_einheit < 10) AS count_0_10,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 10 AND bruttoleistung_einheit < 11) AS count_10_11,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 11 AND bruttoleistung_einheit < 12) AS count_11_12,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 12 AND bruttoleistung_einheit < 13) AS count_12_13,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 13 AND bruttoleistung_einheit < 14) AS count_13_14,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 14 AND bruttoleistung_einheit < 15) AS count_14_15,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 15 AND bruttoleistung_einheit < 16) AS count_15_16,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 16 AND bruttoleistung_einheit < 17) AS count_16_17,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 17 AND bruttoleistung_einheit < 18) AS count_17_18,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 18 AND bruttoleistung_einheit < 19) AS count_18_19,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 19 AND bruttoleistung_einheit < 20) AS count_19_20,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 20 AND bruttoleistung_einheit < 21) AS count_20_21,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 21 AND bruttoleistung_einheit < 22) AS count_21_22,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 22 AND bruttoleistung_einheit < 23) AS count_22_23,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 23 AND bruttoleistung_einheit < 24) AS count_23_24,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 24 AND bruttoleistung_einheit < 25) AS count_24_25,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 25 AND bruttoleistung_einheit < 26) AS count_25_26
FROM es_einheiten_01_bis_05_2025_6 
WHERE nutzbare_speicherkapazitaet_kwh >0 AND nutzbare_speicherkapazitaet_kwh <= 5 ;

SELECT* FROM leistung_vs_kapazitaet_0_5_kw_2025_6;

CREATE MATERIALIZED VIEW IF NOT EXISTS leistung_vs_kapazitaet_5_10_kw_2025_6 AS
SELECT 
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 0 AND bruttoleistung_einheit < 10) AS count_0_10,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 10 AND bruttoleistung_einheit < 11) AS count_10_11,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 11 AND bruttoleistung_einheit < 12) AS count_11_12,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 12 AND bruttoleistung_einheit < 13) AS count_12_13,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 13 AND bruttoleistung_einheit < 14) AS count_13_14,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 14 AND bruttoleistung_einheit < 15) AS count_14_15,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 15 AND bruttoleistung_einheit < 16) AS count_15_16,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 16 AND bruttoleistung_einheit < 17) AS count_16_17,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 17 AND bruttoleistung_einheit < 18) AS count_17_18,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 18 AND bruttoleistung_einheit < 19) AS count_18_19,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 19 AND bruttoleistung_einheit < 20) AS count_19_20,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 20 AND bruttoleistung_einheit < 21) AS count_20_21,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 21 AND bruttoleistung_einheit < 22) AS count_21_22,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 22 AND bruttoleistung_einheit < 23) AS count_22_23,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 23 AND bruttoleistung_einheit < 24) AS count_23_24,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 24 AND bruttoleistung_einheit < 25) AS count_24_25,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 25 AND bruttoleistung_einheit < 26) AS count_25_26
FROM es_einheiten_01_bis_05_2025_6
WHERE nutzbare_speicherkapazitaet_kwh >5 AND nutzbare_speicherkapazitaet_kwh <= 10;

SELECT* FROM leistung_vs_kapazitaet_5_10_kw_2025_6;

CREATE MATERIALIZED VIEW IF NOT EXISTS leistung_vs_kapazitaet_10_15_kw_2025_6 AS
SELECT 
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 0 AND bruttoleistung_einheit < 10) AS count_0_10,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 10 AND bruttoleistung_einheit < 11) AS count_10_11,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 11 AND bruttoleistung_einheit < 12) AS count_11_12,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 12 AND bruttoleistung_einheit < 13) AS count_12_13,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 13 AND bruttoleistung_einheit < 14) AS count_13_14,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 14 AND bruttoleistung_einheit < 15) AS count_14_15,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 15 AND bruttoleistung_einheit < 16) AS count_15_16,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 16 AND bruttoleistung_einheit < 17) AS count_16_17,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 17 AND bruttoleistung_einheit < 18) AS count_17_18,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 18 AND bruttoleistung_einheit < 19) AS count_18_19,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 19 AND bruttoleistung_einheit < 20) AS count_19_20,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 20 AND bruttoleistung_einheit < 21) AS count_20_21,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 21 AND bruttoleistung_einheit < 22) AS count_21_22,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 22 AND bruttoleistung_einheit < 23) AS count_22_23,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 23 AND bruttoleistung_einheit < 24) AS count_23_24,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 24 AND bruttoleistung_einheit < 25) AS count_24_25,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 25 AND bruttoleistung_einheit < 26) AS count_25_26
FROM es_einheiten_01_bis_05_2025_6
WHERE nutzbare_speicherkapazitaet_kwh >10 AND nutzbare_speicherkapazitaet_kwh <= 15;

SELECT* FROM leistung_vs_kapazitaet_10_15_kw_2025_6;



CREATE MATERIALIZED VIEW IF NOT EXISTS leistung_vs_kapazitaet_15_20_kw_2025_6 AS
SELECT 
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 0 AND bruttoleistung_einheit < 10) AS count_0_10,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 10 AND bruttoleistung_einheit < 11) AS count_10_11,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 11 AND bruttoleistung_einheit < 12) AS count_11_12,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 12 AND bruttoleistung_einheit < 13) AS count_12_13,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 13 AND bruttoleistung_einheit < 14) AS count_13_14,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 14 AND bruttoleistung_einheit < 15) AS count_14_15,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 15 AND bruttoleistung_einheit < 16) AS count_15_16,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 16 AND bruttoleistung_einheit < 17) AS count_16_17,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 17 AND bruttoleistung_einheit < 18) AS count_17_18,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 18 AND bruttoleistung_einheit < 19) AS count_18_19,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 19 AND bruttoleistung_einheit < 20) AS count_19_20,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 20 AND bruttoleistung_einheit < 21) AS count_20_21,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 21 AND bruttoleistung_einheit < 22) AS count_21_22,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 22 AND bruttoleistung_einheit < 23) AS count_22_23,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 23 AND bruttoleistung_einheit < 24) AS count_23_24,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 24 AND bruttoleistung_einheit < 25) AS count_24_25,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 25 AND bruttoleistung_einheit < 26) AS count_25_26
FROM es_einheiten_01_bis_05_2025_6
WHERE nutzbare_speicherkapazitaet_kwh >15 AND nutzbare_speicherkapazitaet_kwh <= 20;

SELECT* FROM leistung_vs_kapazitaet_15_20_kw_2025_6;


CREATE MATERIALIZED VIEW IF NOT EXISTS leistung_vs_kapazitaet_20_25_kw_2025_6 AS
SELECT 
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 0 AND bruttoleistung_einheit < 10) AS count_0_10,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 10 AND bruttoleistung_einheit < 11) AS count_10_11,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 11 AND bruttoleistung_einheit < 12) AS count_11_12,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 12 AND bruttoleistung_einheit < 13) AS count_12_13,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 13 AND bruttoleistung_einheit < 14) AS count_13_14,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 14 AND bruttoleistung_einheit < 15) AS count_14_15,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 15 AND bruttoleistung_einheit < 16) AS count_15_16,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 16 AND bruttoleistung_einheit < 17) AS count_16_17,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 17 AND bruttoleistung_einheit < 18) AS count_17_18,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 18 AND bruttoleistung_einheit < 19) AS count_18_19,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 19 AND bruttoleistung_einheit < 20) AS count_19_20,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 20 AND bruttoleistung_einheit < 21) AS count_20_21,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 21 AND bruttoleistung_einheit < 22) AS count_21_22,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 22 AND bruttoleistung_einheit < 23) AS count_22_23,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 23 AND bruttoleistung_einheit < 24) AS count_23_24,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 24 AND bruttoleistung_einheit < 25) AS count_24_25,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 25 AND bruttoleistung_einheit < 26) AS count_25_26
FROM es_einheiten_01_bis_05_2025_6
WHERE nutzbare_speicherkapazitaet_kwh >20 AND nutzbare_speicherkapazitaet_kwh <= 25;

SELECT* FROM leistung_vs_kapazitaet_20_25_kw_2025_6;


CREATE MATERIALIZED VIEW IF NOT EXISTS leistung_vs_kapazitaet_25_plus_kw_2025_6 AS
SELECT 
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 0 AND bruttoleistung_einheit < 10) AS count_0_10,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 10 AND bruttoleistung_einheit < 11) AS count_10_11,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 11 AND bruttoleistung_einheit < 12) AS count_11_12,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 12 AND bruttoleistung_einheit < 13) AS count_12_13,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 13 AND bruttoleistung_einheit < 14) AS count_13_14,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 14 AND bruttoleistung_einheit < 15) AS count_14_15,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 15 AND bruttoleistung_einheit < 16) AS count_15_16,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 16 AND bruttoleistung_einheit < 17) AS count_16_17,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 17 AND bruttoleistung_einheit < 18) AS count_17_18,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 18 AND bruttoleistung_einheit < 19) AS count_18_19,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 19 AND bruttoleistung_einheit < 20) AS count_19_20,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 20 AND bruttoleistung_einheit < 21) AS count_20_21,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 21 AND bruttoleistung_einheit < 22) AS count_21_22,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 22 AND bruttoleistung_einheit < 23) AS count_22_23,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 23 AND bruttoleistung_einheit < 24) AS count_23_24,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 24 AND bruttoleistung_einheit < 25) AS count_24_25,
    COUNT(*) FILTER (WHERE bruttoleistung_einheit >= 25 AND bruttoleistung_einheit < 26) AS count_25_26
FROM es_einheiten_01_bis_05_2025_6
WHERE nutzbare_speicherkapazitaet_kwh >25;

SELECT* FROM leistung_vs_kapazitaet_25_plus_kw_2025_6;


CREATE MATERIALIZED  VIEW IF NOT EXISTS leistung_vs_kapazitaet_2025_6 AS
SELECT * FROM leistung_vs_kapazitaet_0_5_kw_2025_6
UNION ALL
SELECT * FROM leistung_vs_kapazitaet_5_10_kw_2025_6
UNION ALL
SELECT * FROM leistung_vs_kapazitaet_10_15_kw_2025_6
UNION ALL
SELECT * FROM leistung_vs_kapazitaet_15_20_kw_2025_6
UNION ALL
SELECT * FROM leistung_vs_kapazitaet_20_25_kw_2025_6
UNION ALL
SELECT * FROM leistung_vs_kapazitaet_25_plus_kw_2025_6;


SELECT* FROM leistung_vs_kapazitaet_2025_6;

CREATE TABLE IF NOT EXISTS leistung_vs_kapazitaet_01_bis_05_2025_6_tbl AS
SELECT * FROM leistung_vs_kapazitaet_2025_6;

SELECT * FROM leistung_vs_kapazitaet_01_bis_05_2025_6_tbl;

--speichern als csv
COPY (SELECT * FROM leistung_vs_kapazitaet_01_bis_05_2025_6_tbl) TO 'C:/data/marktstammdatenregister/leistung_vs_kapazitaet_01_bis_05_2025_6_tbl.csv' WITH CSV HEADER;

