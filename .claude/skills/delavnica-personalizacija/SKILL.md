---
name: delavnica-personalizacija
description: Vodi kratek pogovor o osebi, podjetju in znamki, pripravi skupni profil za Claude ter ga dopolnjuje iz preverjenih popravkov pri delu.
---
# Personalizacija za delo

Uporabi takoj po pripravi lokalne mape, orodij in zasebnega dela; pred prvo vsebinsko nalogo. Ob nadaljevanju intervjuja ali prošnji za spremembo profila dopolni obstoječi zapis. Ne nameščaj dokumentnega starterja in ne spreminjaj njegovih zbirk.

## Kratek pogovor

Preberi napredek, `moje-delo/rezultati/profil/INDEX.md` in že dovoljena osebna navodila. Starejši `kako-delam-s-claudom.md` uporabi pri prenosu odgovorov v profil. Novih pravil ne zapisuj na obeh mestih. Druge osebne mape odpri samo po dogovoru. Če je profil pripravljen, uporabi potrjene dogovore in vprašaj samo, kaj je treba dopolniti.

Največ sedem osnovnih tem, po eno vprašanje naenkrat. Preskoči odgovore, ki jih že poznaš. Vprašanja prilagodi človeku:

1. Kaj delaš in kako ti lahko Claude pri tem pomaga?
2. Za katero podjetje delaš in komu pomaga oziroma kaj ponuja?
3. Kdo bo uporabljal rezultat in kaj pri njem šteje?
4. Katera poslovna pravila, omejitve ali trditve mora Claude upoštevati?
5. Kako naj piše: jezik, ton, izrazi in običajna oblika?
6. Imaš kratek dober primer ali primer, ki ti ni všeč? Kaj je razlog?
7. Kaj moraš pred uporabo preveriti sam in pri čem naj Claude opozori na negotovost?

Ni treba imeti priročnika znamke ali vseh primerov. Manjkajoče označi kot še nedogovorjeno. Ob prekinitvi shrani že potrjene odgovore in naslednjo temo v INDEX.md; ne ponavljaj celega pogovora. Pokaži kratek povzetek, popravi nesporazume in preverita profil na majhnem dejanskem rezultatu.

## Ena skupna zbirka

Uporabi [vzorec](assets/output.md) in ustvari samo datoteke, ki jih potrebuje trenutni kontekst, pod `moje-delo/rezultati/profil/`:

- `PERSON.md`: osebna vloga, sodelovanje in preference, brez samodejne vezave na eno podjetje.
- `INDEX.md`: stanje pogovora, relativne povezave do podjetij in izrecno potrjene povezave med delovnimi mapami ter podjetji. Za vsako mapo zapiši, ali velja tudi za njene podmape.
- `podjetja/<oznaka>/COMPANY.md`: dejstva o podjetju, občinstvo, poslovna pravila in omejitve.
- `podjetja/<oznaka>/BRAND.md`: jezik, ton, izrazi in slog. Če ima podjetje več znamk, dodaj ločene datoteke in izbiro v kazalo.
- `podjetja/<oznaka>/PRIMERI.md`: kratki dovoljeni dobri/slabi primeri, razlog in popravljena različica. Osebne primere hrani posebej ob PERSON.md, če niso vezani na podjetje.

Uporabi kratke razumljive oznake brez presledkov. Ne izmišljaj poslovnih dejstev. V profilu ne shranjuj poverilnic ali izvornih dokumentov. Občutljivi primeri ostanejo v `moje-delo/zasebno/profil/`; za profil uporabi samo dovoljen kratek povzetek. Globalnih absolutnih poti ne prepisuj v vsebino poslovnih veščin.

## Uporaba tudi v drugih projektih

Razloži, da globalna navodila vplivajo na vse pogovore Code tega uporabnika. Na skupnem računalniškem računu najprej uredi zasebno uporabniško okolje. Ohranjenih globalnih pravil ne nadomeščaj. Če nasprotujejo novemu profilu, razjasni neskladje; povezovalni blok ne izbriše starih navodil.

Preberi [podrobni postopek](../../../docs/za-agenta/personalizacija.md). Za varno dodajanje označenega bloka uporabi `scripts/povezi_profil.py` iz te veščine. Pomočnik preveri profil in pravi zasebni Gitov koren, pred spremembo naredi zasebno kopijo ter ob ponovitvi ne podvaja bloka. Najprej uporabi `pregled`, pokaži spremembo, nato `povezi`, ko je obseg dogovorjen. Račun in zasebnost oddaljenega cilja preveri po navodilu za shranjevanje.

V novem pogovoru Code preveri, ali so globalna navodila in oba uvoza dejansko naloženi (pregled konteksta, če je na voljo), nato preizkusi vedenje. Sam obstoj bloka ni dokaz, da ga je okolje uporabilo. Ob selitvi preveri dejanske poti in blok popravi s pomočnikom. Chat in Cowork dobita kratek povzetek v `ZA-CHAT-COWORK.md`; uporabnik preveri vnos v nastavitve oziroma priloži profil. Tam ne obljubljaj samodejnega branja lokalnih datotek.

## Popravki med uporabo

Pred nalogo preberi PERSON.md in INDEX.md. Poslovni kontekst izberi po potrjeni povezavi mape ali uporabnikovi nalogi; ob več možnostih vprašaj po eni manjkajoči izbiri. Ne prenašaj pravil drugega podjetja. Nato preberi ustrezni COMPANY.md, BRAND.md in PRIMERI.md.

Popravek, ki velja tudi naslednjič, zapiši v ustrezni profil. Posebnost trenutnega primera shrani pri nalogi, dober ali slab primer pa v PRIMERI.md z razlago in popravljeno različico. Povej, kaj si dopolnil. Če popravek nasprotuje dogovoru ali ni jasno, za katere primere velja, vprašaj pred spremembo pravila. Po popravku ponovno preveri rezultat; primer ni novo dovoljenje za zunanje dejanje.
