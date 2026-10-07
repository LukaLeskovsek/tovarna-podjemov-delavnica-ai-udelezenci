# Od prvega poskusa do načina dela, ki ga lahko ponoviš

Pri pripravi poročila, primerjavi ponudb in pregledu pošte se vedno vprašaj: kaj ima Claude na voljo, kaj mu moraš pojasniti in kako boš rezultat preveril? [Good Brew](../exercises/goodbrew/README.md) je izmišljeni učni primer, s katerim pokažemo razlike. Pri svojem delu uporabi dovoljene podatke svojega podjetja.

## Kaj prispeva posamezen del

| Del | Kako ti pomaga | Kaj moraš vedeti |
|---|---|---|
| Claude | Bere dostopno gradivo, pripravi predlog in ob ustreznih orodjih obdela datoteke | Ne pozna podatkov, ki mu jih nisi dal ali omogočil dostopa do njih |
| Podatki in razlaga | Povedo, kaj se je zgodilo in kaj pomeni posamezna številka | Manjkajoči podatek ni ničla; prodaja sama ne pojasni vzroka spremembe |
| Osebni in poslovni profil | Pove, za koga dela, kaj je pomembno in kako naj piše | Lepše besedilo še ne pomeni pravilnih številk |
| Primeri s pojasnilom | Pokažejo, kaj želiš obdržati in čemu naj se izogne | Iz primera naj prevzame način dela, ne starih številk |
| Podporna veščina | Claudu da navodila za pripravo, preverjanje ali izboljšavo naloge | Ne odpre računa in ne zagotovi dostopa do pošte |
| Povezovalnik | Omogoči dogovorjeni dostop do zunanje storitve | Preverita račun, obseg in dejansko dosegljiva orodja |
| Pregled rezultata | Pokaže, kaj lahko uporabiš in kaj moraš popraviti | Pomembno številko ali trditev primerjaj z izvirnikom |

V Code Local lahko začneš z datotekami v izbrani mapi. Za branje žive pošte potrebuješ ustrezen dostop. Posamezna aplikacija ali vtičnik lahko doda orodja; Claude naj najprej pove, katera dejansko vidi. Za prvo poročilo iz ene preglednice ne potrebuješ indeksa dokumentov ali povezave do pošte.

## Na poročilu pokažemo izboljšavo

1. Daj Claudu preglednico in pojasni pomen podatkov. Zahtevaj en graf in kratek odstavek za vodjo podjetja.
2. Pri drugem poskusu uporabi isti cilj in podatke ter dodaj osebni in poslovni profil. Primerjaj, ali je odgovor bolj uporaben za tega bralca. Lahko je dober že prvi poskus.
3. Preveri eno številko in eno razlago. Če Claude iz rasti prodaje sklepa, da je oglas uspešen, preveri, ali ima za to sploh podatke.
4. Povej, kaj naj popravi in zakaj. Dober in slab primer shrani z razlogom. Dogovor za vse prihodnje naloge sodi v profil; posebnost trenutnega poročila sodi k nalogi.
5. Ko postopek deluje, ga shrani kot svojo veščino. V novem pogovoru ga preizkusi na drugi preglednici, tudi na takšni, kjer podatek manjka.

Za pošteno primerjavo brez profila in s profilom potrebujemo nadzor nad navodili, ki jih Claude prejme. Nov pogovor v isti mapi lahko že pozna profil. Med običajnim delom ga uporabljaj; primerjavo dveh nastavitev pripravimo posebej za prikaz.

## Katere naše veščine pri tem pomagajo

| Trenutek | Veščina | Prošnja |
|---|---|---|
| Okolje deluje, profil še manjka | `delavnica-personalizacija` | »Pomagaj mi zapisati, za koga pripravljam poročila in kaj mi je pri njih pomembno.« |
| Ne vemo, kaj stolpec pomeni | `prepare-context` | »Preglej podatke in vprašaj, kaj moraš vedeti za primerjavo.« |
| Poročilo je pripravljeno | `verify-workflow` | »Pokaži izračun te številke in vir za to razlago.« |
| Popravek se ponavlja | `review-workflow-run` | »Ugotoviva, zakaj vedno sklepaš o vzroku. Popravi navodilo in preveri še en primer.« |
| Razumemo prvo izvedbo | `deconstruct-workflow` | »Poglejva, kako sva pripravila poročilo in kaj lahko naslednjič izpustiva.« |
| Imamo preverjen način dela | `package-workflow` | »Shrani ta postopek kot mojo veščino. Poveži ga z mojim profilom in ga preveriva na drugih podatkih.« |

Claude pred uporabo prebere navodila veščine iz trenutne mape delavnice. Osebna metoda ostane v `moje-delo/skills/`; ob ponovitvi mu povej, naj jo prebere. Profil ostane na enem mestu v `moje-delo/rezultati/profil/`.

Preostalih veščin ne potrebuješ za ta prvi prikaz. `delavnica-dokumenti` pomaga iskati po več dokumentih, `maintain-knowledge` ureja trajnejše ugotovitve, `publish-knowledge` pripravi dovoljeno gradivo za ekipo. `graduate-artifact` pomaga presoditi nadaljnji razvoj izdelka, `operate-workflow` redno izvajanje in `design-agent-team` smiselnost delitve med agente. V [celotnem pregledu](podporne-vescine.md) so njihove povezave in primeri.

## Prenos na tvoje delo

Pri ponudbah najprej dogovoriš merila in primerljivo količino. Pri pošti pojasniš pomembnost in preveriš zadnje sporočilo. Pri poročilu določiš bralca in pomen številk. V vseh primerih shraniš popravek, ki bo pomagal tudi naslednjič.

Artifact je oblika prikaza rezultata. Sam odprt prikaz ne pridobiva novih podatkov. Osveževanje in redno izvajanje uredita posebej, ko je ročni postopek uporaben. Za primerjavo prihranka upoštevaj tudi pripravo podatkov, pregled in popravke.

[Poišči svojo nalogo](izberi-nalogo.md) · [Pet vprašanj](razclenitev-naloge.md)
