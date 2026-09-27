# Neobvezna vaja: pregled in odobritev v n8n Cloud

To je dodatna vaja z izmišljenimi podatki. Uporabi svoj n8n Cloud. Uvoz ni pogoj za delo na svoji nalogi. Datoteki ne vsebujeta prijavnih podatkov in ne zapisujeta v CRM ali pošiljata sporočil. Spodaj je navedeno tudi, kaj je bilo že preizkušeno in kaj je treba še preveriti.

## 1. Preveri odločanje

V n8n izberi uvoz iz datoteke in odpri [approval-lab.json](approval-lab.json). Pritisni Execute workflow. Zadnji korak mora vrniti šest zapisov:

| Primer | Pričakovano stanje |
|---|---|
| approved | simulated_ready |
| rejected | rejected |
| changed | needs_new_approval |
| expired | expired |
| repeated | already_completed |
| wrong_identity | denied_identity |

Vsi rezultati imajo `externalActionPerformed: false`. Identiteta in stanje sta v tej vaji izmišljena vhoda. Primer dokazuje odločanje, ne prijave resničnega uporabnika ali trajnega preprečevanja dvojnikov. Za trajno stanje in nadaljevanje uporabi še [lokalno generalko](../../exercises/conference/README.md).

## 2. Počakaj na človeka

Uvozi [human-review.json](human-review.json), zaženi in odpri obrazec, ki ga pokaže čakajoči korak. Preglej celotno besedilo osnutka. Vpiši `approve` ali `reject` in njegov ID `TP01-v1`. Postopek se nadaljuje po oddaji. Ponovi z zavrnitvijo in napačnim ID-jem. Brez veljavnega odgovora izid ne sme biti `reviewed_draft`.

Obrazec je namenjen izmišljenemu lokalnemu primeru; dostop do povezave sam ne dokazuje identitete. Poteka po 30 minutah. Postopek ne zapisuje v zunanje storitve. Če spremeniš besedilo osnutka, spremeni tudi revizijo ID-ja in besedilo za pregled. To je učna vaja pregleda, ne kontrola za dinamične poslovne zapise.

## 3. Kaj lahko preneseš na svojo nalogo

Z agentom preberi svoj opis postopka. Zamenjaj pripravljene vhode s svojim dovoljenim virom. Preden dodaš zapisovanje v drugo storitev, določi in preizkusi:

1. Identiteto in pravice resničnega odobritelja; izmišljeno polje `actor` jih ne zagotovi.
2. Nespremenljiv posnetek točne vsebine odobritve. Primerjaj ga z vsebino tik pred dejanjem.
3. Trajni ključ izvedbe in en sam zapis v ciljno storitev, tudi ob ponovitvi ali prekinitvi. Stanja ne pošiljaj kot zaupanja vrednega podatka iz javnega obrazca.
4. Zavrnitev, spremembo po odobritvi, iztek in napačen račun.
5. En dovoljen vadbeni zapis in ponovno branje na cilju. Zapiši ID cilja in izvršitve v svoj dnevnik.

Pred pošiljanjem ali pisanjem v resnični sistem preglej konkretno dejanje. Povezave, poverilnice in rezultate hrani v svojem računu. V izvozu za skupni repozitorij odstrani prijave, zasebne URL-je in osebne podatke.

## Kaj vaja potrjuje

Rezultati simuliranega odločanja potrjujejo le pravila na učnih vhodih. Prijavo, obrazec, trajno stanje in povezave preveri v svojem n8n Cloud. Sam uvoz ne potrjuje uspešne izvedbe.

[Nazaj na lastno nalogo](README.md)
