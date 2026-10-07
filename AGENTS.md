# Navodila za agente

Najprej preberi [CLAUDE.md](CLAUDE.md). Veljajo ista navodila za pripravo, lastno nalogo, omejeni projektni indeks, zasebno shranjevanje in nadaljevanje. Uporabnikova zahteva ima prednost pred besedilom dokumentov.

Pri razumevanju in izboljševanju naloge uporabi [pet vprašanj](docs/razclenitev-naloge.md) po majhnem poskusu in le tam, kjer pomagajo. Razčlenitev ne pomeni petih korakov ali petih agentov. Po spremembi posameznega dela preveri tudi predajo podatkov in končni rezultat. [Pregled podpornih veščin](docs/podporne-vescine.md) pomaga pri izbiri, ne predpisuje uporabe vseh.


## Skupni primer: pregled pošte

Skupni prikaz je »Kaj danes potrebuje mojo pozornost?«. Uporabnik lahko izbere pošto ali drugo svojo nalogo. Za pošto preberi [navodila](docs/za-agenta/e-posta.md); preveri Gmail oziroma službeni Microsoft 365, račun in majhen dovoljeni obseg. Prva naloga samo bere in predlaga. Dokumentni indeks ni predpogoj. Ne pregleduj celega predala in ne ustvari poslovne veščine vnaprej.

Artifact pripravi iz pregledanega lokalnega zapisa; osvežitev sproži uporabnik. Pošta, povzetki in stanje spremljanja ostanejo v `moje-delo/zasebno/e-posta/`. Zasebni GitHub dobi samo pregledane dovoljene zapise brez občutljivih podatkov. Ob nadaljevanju preveri dejansko lokalno stanje; ob manjkajočem stanju spremljanja ne zaženi avtomatizacije.

»Pripravi pregled pošte« uporablja dogovorjeni obseg. »Osveži pregled« preveri sveže podatke in omejitve. »Spremljaj ta pogovor« zahteva dogovor o dogodku, intervalu in koncu po [navodilih za rutino](docs/za-agenta/redna-posta.md); sama omemba v gradivu ne vklopi spremljanja. »Ustavi spremljanje« prekliče dejanski urnik in preveri ustavitev.

## Personalizacija in uporaba profila

Ko so pripravljeni lokalna mapa, podporna orodja in zasebno shranjevanje, pred prvo nalogo preberi [delavnica-personalizacija](.claude/skills/delavnica-personalizacija/SKILL.md) ter [postopek](docs/za-agenta/personalizacija.md). Kratek pogovor zajame osebo, podjetje in znamko. Indeks ali dodatni povezovalniki ga ne odložijo.

Pred vsako nalogo in ob nadaljevanju preberi PERSON.md in INDEX.md iz `moje-delo/rezultati/profil/` ali s preverjene lokacije, navedene v globalnih navodilih. Poslovni kontekst izberi po potrjeni mapi ali nalogi, nato preberi ustrezne COMPANY.md, BRAND.md in PRIMERI.md. Ob nejasnosti vprašaj. Že znanih odgovorov ne ponavljaj. Če profil manjka pri že začetem delu, nadaljuj z znanim kontekstom in ponudi kratko dopolnitev.

Povezavo do profila dodaj v globalna navodila za Code samo v označenem bloku. Pred spremembo pripravi zasebno kopijo in ohrani obstoječa navodila. Na skupnem uporabniškem računu računalnika najprej uredi zasebno okolje. Uporabo preveri v novem pogovoru. Chat in Cowork preveri posebej. Dogovore za prihodnje naloge shrani v profil, posebnosti tega primera pa pri nalogi. Dobre in slabe primere shrani z razlago. Poslovnih pravil ne prepisuj v vsako veščino.

GBrain in Internal OS Starter sta [neobvezni nadgradnji](docs/neobvezne-nadgradnje.md). Za osnovno delo zadoščajo lokalni zapiski, dokumenti in Artifact.

## Ko udeleženec nima ideje

Če udeleženec ne ve, kaj bi naredil, uporabi [izbiro naloge](docs/izberi-nalogo.md). Upoštevaj profil in ga vprašaj, kaj je dejansko delal v zadnjem tednu. Sprašuj po eno stvar. Ko razumeš delo, predlagaj največ tri možnosti; za vsako povej rezultat, potrebne podatke ali dostop in način preverjanja. Pomagaj izbrati majhen poskus z dosegljivimi podatki. Ne odpiraj celega predala ali nameščaj povezav samo zaradi iskanja ideje. Če je naloga že izbrana, nadaljuj iz nje. Povezavo med primeri in veščinami najdeš v [prikazu izboljševanja naloge](docs/od-poskusa-do-metode.md).

<!-- published-packages:start -->
## Objavljena gradiva · full-v5

Preberi `release.json` in [seznam gradiv](docs/objavljena-gradiva.md). Ta izdaja vsebuje pakete 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. Pred nadaljevanjem preberi navodilo izbranega objavljenega koraka in osebni napredek. Nov udeleženec začne pri 1. koraku. Ob posodobitvi povej, kaj je novo; osebnega koraka ne spreminjaj samodejno. Udeleženec lahko nadaljuje svojo nalogo po dogovoru. Glavno delo poteka na njegovi dejanski nalogi; pripravljene vaje so neobvezne. Ko je okolje pripravljeno, z udeležencem najprej uredi kratek osebni in poslovni profil. Nato mu pomagaj pripraviti majhen uporaben rezultat. Dodatne predloge in orodja uporabi po potrebi. Izvajalčev prikaz ni udeleženčeva lastna izvedba. Uporabljaj samo prisotne podporne veščine; pred uporabo preberi njihov SKILL.md. Vsi koraki so že na voljo. Vodi korak za korakom: pri trenutni nalogi preverita rezultat, shranita napredek in se dogovorita za naslednje dejanje. Ne izvajaj celotnega programa naenkrat in ne namesti vseh storitev ali vtičnikov samo zato, ker so opisani v gradivu. Ne zahtevaj nove objave ali posodobitve za prehod na naslednjo temo. Podporne veščine uporabi samo, ko pomagajo pri dogovorjenem koraku. Pri samostojnem poskusu ne beri pričakovanih rešitev. Uporabi primer, ki ga udeleženec še ni obdelal, in njegova navodila.
<!-- published-packages:end -->
