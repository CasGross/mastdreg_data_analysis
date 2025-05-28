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


