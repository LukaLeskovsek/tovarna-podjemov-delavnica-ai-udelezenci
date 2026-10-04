# Pravila konferenčne vaje za Intrix

Na delavnici za skupni CRM primer uporabljamo **Intrix**. Ta pravila določajo, kako pregledamo deset izmišljenih vrstic in pripravimo predlog za njegova polja. [Tabela polj za Intrix](intrix.md) pojasni, kam sodi posamezen podatek. Vse osebe, podjetja in domene `.test` so izmišljeni.

`existing-crm.json` je učna primerjalna zbirka, ne izvoz iz Intrixa. Imena stolpcev in statusi v teh pravilih so oznake vaje. Obvezna polja spodaj veljajo za naš pregled; niso seznam obveznih polj Intrixovega obrazca.

Ohrani vrstni red in izvorne podatke. Odstrani odvečne presledke na robovih; za ujemanje pretvori e-pošto v male črke, spletni naslov v gostitelja brez `www.`, ime podjetja pa v male črke z enojnimi presledki. Ne ugibaj e-pošte, podjetja, lastnika ali dovoljenja za stik.

Učna pravila odločanja ostajajo v različici 1. Odločaj v naslednjem vrstnem redu:

1. Za učni pregled so zahtevana polja `source_row_id`, `conference`, `company`, `contact_name`, `business_email` in `assigned_salesperson`. E-pošta mora vsebovati eno `@`, ime pred njo in domeno s piko, brez presledkov. Vrstica s pomanjkljivostjo je `needs_review` (`missing_required` ali `invalid_email`), tudi če kontakt že obstaja. Če se ID ponovi, so vse vrstice s tem ID-jem `needs_review` (`duplicate_source_id`).
2. Pri ponovljeni normalizirani e-pošti v veljavnih vhodnih vrsticah ima prednost prva. Poznejša je `duplicate` (`duplicate_in_input`) in kaže na prvi ID. Zapiski se ne združijo. Prva vrstica je lahko tudi sama predmet pregleda; dvojnik zato še ne pomeni uspešnega uvoza.
3. Pri enoličnem ujemanju e-pošte z obstoječim CRM kontaktom je rezultat `existing` (`contact_exists`). Več CRM kontaktov z isto e-pošto pomeni `needs_review` (`ambiguous_contact`). Obstoječih kontaktov ali zapiskov v tej vaji ne spreminjamo.
4. Podjetje ujemaj po gostitelju spletnega naslova, če je naveden. Brez spletnega naslova uporabi natančno normalizirano ime. Več kandidatov pomeni `needs_review` (`ambiguous_company`). Če naslov ne zadene, ime pa zadene drugo podjetje, zahtevaj pregled (`company_domain_conflict`). Če ni kandidata, predlagaj novo podjetje. Ob enoličnem kandidatu predlagaj povezavo na njegov ID.
5. Preostale vrstice so `ready` (`new_contact`). Njihov predlog vsebuje podjetje, kontakt, konferenco, zapis, odgovorno osebo in besedilo naslednjega koraka. Besedilo naslednjega koraka je podatek; ne ustvari naloge in ne pošlje sporočila.

Pregled vrne vseh deset izvornih vrstic, status, razlog in dokaz ujemanja. Za vsako pripravljeno vrstico prikaže natančno vsebino predlaganega zapisa. Odobritev velja za celoten prikazani načrt, njegov ID in prstni odtis SHA-256. Sprememba načrta zahteva nov pregled. Zavrnitev zapre ta poskus. Ponovitev že izvedene vrstice ne ustvari drugega zapisa.

Lokalni simulator te odločitve uveljavlja v kodi, vse učinke pa shrani v lokalno datoteko SQLite. Za izvedbo v Intrixu uporabi [postopek prvega vnosa](vnos-v-intrix.md). Preverjanje obrazcev samo po sebi še ne potrjuje uspešnega vnosa ali varne ponovitve v CRM-ju.

Pred vnosom v Intrix še posebej preverimo povezavo s podjetjem, razdelitev imena in priimka, izbiro skrbnika ter vrednosti šifrantov. Te odločitve zapiši ločeno od učnega statusa. Obstoječih oseb ne prestavljamo med podjetji. Zapis pogovora predlagamo v **Kontakti → Ostalo → Dodatne informacije**; naloga, sestanek, kampanja ali obvestilo potrebujejo svoj dogovor. Podrobnosti so v [navodilu za polja](intrix.md).
