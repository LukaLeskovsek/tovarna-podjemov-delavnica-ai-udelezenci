# Shrani in nadaljuj

Gradiva delavnice in tvoje delo so ločeni. Claude uredi shranjevanje v tvojem zasebnem GitHubu in posodabljanje skupnih gradiv.

| Kaj želiš | Kaj napišeš Claudu |
|---|---|
| Shraniti opravljeno delo | **»Shrani moje delo.«** |
| Dobiti nova gradiva | **»Posodobi gradiva.«** |
| Nadaljevati | **»Nadaljujva.«** |

## Shrani moje delo

Claude povzame rezultat, preverjanje in naslednji korak. Pokaže, katere datoteke bo shranil, ter preveri tvoj račun in zasebni cilj. Izvorni poslovni podatki, prepisi pogovorov in prijavni podatki niso del te varnostne kopije. Zanje ohrani svojo dovoljeno shrambo.

Če prenos v GitHub ne uspe, Claude pove: **»Shranjeno lokalno, ni varnostno kopirano.«** Po odpravi težave pošlje isto shranjeno različico.

## Posodobi gradiva

Vseh deset korakov že imaš. Posodobitev uporabi ob popravkih ali dopolnitvah gradiva, ne za prehod na naslednji korak. Ostaneš na isti veji `main`; oznak različic ti ni treba izbirati.

Claude prenese popravke. Tvoje prilagoditve ostanejo v `moje-delo/`. Če si spremenil skupne datoteke, se ustavi in pojasni, kaj je treba urediti. Ničesar ne prepiše na silo.

Oznake, kot sta `full-v2` in `full-v3`, so imena izdaj gradiva, ne številke tvojega koraka. Ostaneš na veji `main`; oznak ne preklapljaš ročno. Nova izdaja ne pomeni, da si novo temo že opravil.

## Nadaljujva

Odpri isto mapo **delavnica** v lokalnem zavihku **Code**. Claude prebere tvoj napredek in nadaljuje. Ni treba iskati starega pogovora. Če spremeniš nalogo, to povej; prejšnji rezultat ostane shranjen.

Na novem računalniku naj Claude obnovi javna gradiva in tvojo zasebno kopijo. Izvorne podatke obnovi iz svoje dovoljene shrambe.

[Podrobni postopek za Claude](za-agenta/shranjevanje.md) · [Priprava](setup.md) · [Začetek](../README.md)

## Obsidian, osebna navodila in indeks

Odpri isto mapo v Code in Obsidianu. Nastavitve `.obsidian/` in `local/starter/` zunanji Git ignorira. Osebna in poslovna navodila so v `moje-delo/rezultati/profil/`. Za zasebno kopijo izberi samo pregledane dovoljene datoteke. Surovi in občutljivi primeri ostanejo v `moje-delo/zasebno/profil/`. Globalna navodila in njihove kopije niso del te izbire.

Obnovitev na novi napravi ohrani napredek in izbrane rezultate. Izvirnike obnovi iz njihove dovoljene shrambe, nato ponovno pripravi lokalni indeks in preveri poti. GitHubova kopija rezultatov ne vsebuje indeksa, izvornih dokumentov ali nastavitev povezav. Če izvirnikov še ni, nadaljuj iz dosegljivega pregledanega rezultata in manjkajoči del jasno označi.

Pri selitvi ali obnovi naj Claude preveri dejansko lokacijo profila, povezave delovnih map in globalni povezovalni blok. Pred novo uporabo podjetja preveri izbiro. GitHubova kopija profila ne obnovi izvornih datotek ali povezave v globalnih navodilih.
