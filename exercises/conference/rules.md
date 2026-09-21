# Pravila konferenčne vaje za Intrix

Na delavnici za skupni CRM primer uporabljamo **Intrix**. Ta pravila določajo, kako pregledamo deset izmišljenih vrstic in pripravimo predlog za njegova polja. [Tabela polj za Intrix](intrix.md) pojasni, kam sodi posamezen podatek. Vse osebe, podjetja in domene `.test` so izmišljeni.

`existing-crm.json` je učna primerjalna zbirka, ne izvoz iz Intrixa. Imena stolpcev in statusi v teh pravilih so oznake vaje. Obvezna polja spodaj veljajo za naš pregled; niso seznam obveznih polj Intrixovega obrazca.

Ohrani vrstni red in izvorne podatke. Odstrani presledke na začetku in koncu vrednosti. Za primerjavo pretvori e-pošto v male črke, spletni naslov v ime gostitelja brez `www.`, ime podjetja pa v male črke z enojnimi presledki. Ne ugibaj e-pošte, podjetja, lastnika ali dovoljenja za stik.

Učna pravila odločanja ostajajo v različici 1. Odločaj v naslednjem vrstnem redu:

1. Za učni pregled so zahtevana polja `source_row_id`, `conference`, `company`, `contact_name`, `business_email` in `assigned_salesperson`. E-pošta mora vsebovati eno `@`, ime pred njo in domeno s piko, brez presledkov. Vrstica s pomanjkljivostjo je `needs_review` (`missing_required` ali `invalid_email`), tudi če kontakt že obstaja. Če se ID ponovi, so vse vrstice s tem ID-jem `needs_review` (`duplicate_source_id`).
2. Pri ponovljeni normalizirani e-pošti v veljavnih vhodnih vrsticah ima prednost prva. Poznejša je `duplicate` (`duplicate_in_input`) in kaže na prvi ID. Zapiski se ne združijo. Tudi prva vrstica lahko zahteva dodaten pregled. Oznaka dvojnika torej ne pomeni, da je bila prva vrstica že uspešno uvožena.
3. Pri enoličnem ujemanju e-pošte z obstoječim CRM kontaktom je rezultat `existing` (`contact_exists`). Več CRM kontaktov z isto e-pošto pomeni `needs_review` (`ambiguous_contact`). Obstoječih kontaktov ali zapiskov v tej vaji ne spreminjamo.
4. Podjetje poišči po imenu gostitelja spletnega naslova, če je naveden. Brez spletnega naslova uporabi natančno normalizirano ime. Več kandidatov pomeni `needs_review` (`ambiguous_company`). Če po spletnem naslovu ni ujemanja, po imenu pa najdeš drugo podjetje, zahtevaj pregled (`company_domain_conflict`). Če ni kandidata, predlagaj novo podjetje. Ob enoličnem kandidatu predlagaj povezavo na njegov ID.
5. Preostale vrstice so `ready` (`new_contact`). Njihov predlog vsebuje podjetje, kontakt, konferenco, zapis, odgovorno osebo in besedilo naslednjega koraka. Besedilo naslednjega koraka je podatek; ne ustvari naloge in ne pošlje sporočila.

V pregledu prikaži vseh deset izvornih vrstic. Pri vsaki navedi status, razlog zanj in podatek, na katerem temelji ujemanje. Pri vrsticah, ki so pripravljene za predlog, pokaži natančno vsebino predlaganega zapisa. Status `ready` v tej vaji pomeni »pripravljena za predlog«, ne že opravljenega vnosa.

V tej izdaji pripravljamo in pregledujemo osnutek. Sprememba vsebine zahteva ponoven pregled ustreznih odločitev. Uporaba pravega CRM-ja, zapisovanje in pošiljanje niso del te naloge.

Pred vnosom v Intrix še posebej preverimo povezavo s podjetjem, razdelitev imena in priimka, izbiro skrbnika ter vrednosti šifrantov. Te odločitve zapiši ločeno od učnega statusa. Obstoječih oseb ne prestavljamo med podjetji. Zapis pogovora predlagamo v **Kontakti → Ostalo → Dodatne informacije**; naloga, sestanek, kampanja ali obvestilo potrebujejo svoj dogovor. Podrobnosti so v [navodilu za polja](intrix.md).
