# 3. Pripravi veščino za ponavljajoče delo

## Povezava s prvim primerom

Pri pošti uporabi svoje preverjene popravke kot osnovo metode. Poskusi običajen pogovor, nepopoln vhod in nov pogovor. Končne poslovne veščine ne dobiš vnaprej; občutljiva pravila ostanejo lokalno.

## Kaj že imaš in kaj dodamo

Imaš opis postopka in merila za pregled. Svoj način dela shrani kot poslovno veščino. Začetni delavnica-dokumenti pomaga pri iskanju virov; tvoja veščina določa pravila tvoje naloge.

Navodila, ki so se obnesla, shrani kot veščino (skill). V njej opišeš, katere podatke potrebuješ, kaj naj Claude naredi, kakšen rezultat pričakuješ in kdaj naj te vpraša za odločitev.

## Kaj napišeš Claudu

> Uporabi package-workflow, pregledani opis postopka in uspešen primer. Pripravi mojo poslovno veščino. Pokaži, katera navodila veljajo vsakič, katere podatke bom dodal na novo in kdaj se mora Claude ustaviti ali me kaj vprašati.

## Kaj potrebuješ

Pregledani opis postopka, dober rezultat, primer s težavo in nov primer. [package-workflow](../.claude/skills/package-workflow/SKILL.md) je podporna veščina za izdelavo; tvoja nova veščina bo opravljala izbrano poslovno delo.

## Tvoje odločitve

Potrdi navodila za ponovno uporabo, primere, pri katerih veljajo, in kdaj mora Claude vprašati.

## Delo na svoji nalogi

1. Veščino poimenuj tako, da bo jasno, čemu služi. Opiši potrebne podatke, korake, odločitve, pričakovani rezultat in izjeme.
2. Agent naj pripravi `moje-delo/skills/<ime>/SKILL.md` in potrebne primere. Pri prvi uporabi naj to datoteko izrecno prebere; Claude veščin v tej mapi ne najde nujno samodejno.
3. Če uporabljaš Superpowers, uporabi nameščeni vtičnik za pisanje in preverjanje veščin. Če delaš samo z navodili v pogovoru, to tudi zapiši. Za samodejno uporabo svoje veščine uredi podprto osebno ali zasebno projektno namestitev, brez objave poslovnih podatkov v skupni repozitorij.
4. Primerjaj običajni pogovor in ponovno uporabo shranjene metode na primerljivem delu. Nato uporabi nov primer, dopolni, kar manjka in ponovno preveri prejšnji primer.

Veščina lahko preverja preglednico, pripravlja sestanek, primerja ponudbe, oblikuje predlog, ureja poštni osnutek ali kaj drugega. Ne potrebuje vsaka veščina aplikacije, urnika ali dodatnih agentov. Za pravila, ki morajo veljati brez izjeme, mora pozneje poskrbeti tudi orodje ali program, ki izvaja postopek.

## Prikaz in tvoje delo

**Prikaz v živo:** izvajalec pokaže ponovno uporabo navodil na svojem izbranem dejanskem primeru. Poglej, katera pravila, odločitve in način preverjanja lahko preneseš na svojo nalogo. Spremljani prikaz še ni tvoja izvedba.

**Delo na svoji nalogi:** uporabi zgornji potek na svojih dovoljenih podatkih. Lahko nadaljuješ prejšnjo nalogo ali izbereš drugo. Če orodje ne pomaga, izboljšaj postopek brez njega.

**Neobvezna vaja:** pripravljeno vajo uporabi samo, če svojega primera trenutno ne moreš uporabiti ali želiš dodatni preizkus. Izmišljeni podatki ostanejo označeni kot učni. Vaja ne nadomesti zaključnega rezultata iz tvojega dela.

**Dodatno samostojno delo:** preizkusi isto veščino v drugem podprtem okolju za Claude ali dodatku za Office. Preveri, ali Claude najde veščino ter ali lahko shrani in preda datoteke v vsakem okolju posebej.

## Preveri in shrani

V napredek dodaj rezultat, kaj si preveril, dogovor in naslednji korak. Druge predloge uporabi samo, če pomagajo pri nalogi.

Shrani veščino, njeno različico in [dnevnik izvedb](../predloge/dnevnik-izvedbe.md). Z [verify-workflow](../.claude/skills/verify-workflow/SKILL.md) preveri običajen, nepopoln in nov primer. Z [review-workflow-run](../.claude/skills/review-workflow-run/SKILL.md) zapiši eno koristno izboljšavo. Zapiši, kaj je še zahtevalo tvojo razlago ali popravek. Veščina je uporabna, ko z njo nalogo uspešno ponoviš.

<!-- package-navigation:start -->
[2. Opis postopka](02-razcleni-postopek.md) · [4. Povezave in Intrix](04-povezi-vire.md) · [Vsa objavljena gradiva](../docs/objavljena-gradiva.md)
<!-- package-navigation:end -->
