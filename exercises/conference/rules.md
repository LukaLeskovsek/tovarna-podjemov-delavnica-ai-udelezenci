# Pravila vaje A, različica 1

To so dogovorjena pravila izmišljene učne vaje. Niso splošna poslovna pravila CRM-ja. Vse osebe, podjetja in domene `.test` so izmišljeni.

Ohrani vrstni red in izvorne podatke. Odstrani odvečne presledke na robovih; za ujemanje pretvori e-pošto v male črke, spletni naslov v gostitelja brez `www.`, ime podjetja pa v male črke z enojnimi presledki. Ne ugibaj e-pošte, podjetja, lastnika ali dovoljenja za stik.

Odločaj v naslednjem vrstnem redu:

1. Zahtevana so polja `source_row_id`, `conference`, `company`, `contact_name`, `business_email` in `assigned_salesperson`. E-pošta mora vsebovati eno `@`, ime pred njo in domeno s piko, brez presledkov. Vrstica s pomanjkljivostjo je `needs_review` (`missing_required` ali `invalid_email`), tudi če kontakt že obstaja. Če se ID ponovi, so vse vrstice s tem ID-jem `needs_review` (`duplicate_source_id`).
2. Pri ponovljeni normalizirani e-pošti v veljavnih vhodnih vrsticah ima prednost prva. Poznejša je `duplicate` (`duplicate_in_input`) in kaže na prvi ID. Zapiski se ne združijo. Prva vrstica je lahko tudi sama predmet pregleda; dvojnik zato še ne pomeni uspešnega uvoza.
3. Pri enoličnem ujemanju e-pošte z obstoječim CRM kontaktom je rezultat `existing` (`contact_exists`). Več CRM kontaktov z isto e-pošto pomeni `needs_review` (`ambiguous_contact`). Obstoječih kontaktov ali zapiskov v tej vaji ne spreminjamo.
4. Podjetje ujemaj po gostitelju spletnega naslova, če je naveden. Brez spletnega naslova uporabi natančno normalizirano ime. Več kandidatov pomeni `needs_review` (`ambiguous_company`). Če naslov ne zadene, ime pa zadene drugo podjetje, zahtevaj pregled (`company_domain_conflict`). Če ni kandidata, predlagaj novo podjetje. Ob enoličnem kandidatu predlagaj povezavo na njegov ID.
5. Preostale vrstice so `ready` (`new_contact`). Njihov predlog vsebuje podjetje, kontakt, konferenco, zapis, odgovorno osebo in besedilo naslednjega koraka. Besedilo naslednjega koraka je podatek; ne ustvari naloge in ne pošlje sporočila.

Pregled vrne vseh deset izvornih vrstic, status, razlog in dokaz ujemanja. Za vsako pripravljeno vrstico prikaže natančno vsebino predlaganega zapisa. Status `ready` v tej vaji pomeni »pripravljena za predlog«, ne že opravljenega vnosa.

V tej izdaji pripravljamo in pregledujemo osnutek. Sprememba vsebine zahteva ponoven pregled ustreznih odločitev. Uporaba pravega CRM-ja, zapisovanje in pošiljanje niso del te naloge.
