# Good Brew: agent pripravi predlog pokušine

Na skupnem primeru se naučimo agentu določiti cilj, mu omogočiti uporabo podatkov in orodij ter preveriti, kako je prišel do priporočila. Ponudba nam pomaga preveriti, ali je njegovo delo uporabno. Za neobvezno vajo so pripravljeni [izmišljeni podatki Good Brew](../exercises/goodbrew/pokusina/README.md). Pri prikazu v živo uporabljamo testna povpraševanja in dejanske račune storitev.

V ponedeljek začnemo s Claudom ob pogovoru. Nato preverjeni način dela vključimo v n8n. V petek dodamo aplikacijo za ljudi, ki povpraševanja dopolnjujejo in pregledujejo. Pri svojem delu uporabi pristop za svojo nalogo; pokušina in prodaja nista obvezni.

## Dve vlogi Clauda

| Kje dela | Kaj naredi |
|---|---|
| Claude Desktop → Code → Local | Z nami razume nalogo, pripravi načrt, gradi potek prek n8n MCP, prebere izvedbo in pomaga popraviti napako. |
| Agent v n8n s Claude prek Anthropic API | Razume povpraševanje, uporabi prejete podatke in orodje za izračun ter pripravi priporočilo. |

Agentu določimo cilj in omejen nabor orodij. V našem prikazu n8n prebere oddajo obrazca in cenik, Claude pa presodi zahtevo ter uporabi izračun. Koledar preverimo v drugem poteku, ko pripravljamo popravek s točnim terminom. Razčlenitev naloge ne pomeni, da potrebujemo več agentov. Za ta primer zadostuje en agent.

## Kaj agent presoja in kaj preverimo drugače

Agent prepozna, kaj stranka želi, kateri podatki manjkajo in katere dovoljene možnosti ustrezajo. Pojasni razlog, navede vir ter opozori na negotovost. Nejasno povpraševanje lahko zaključi z vprašanji za dopolnitev.

Cene izračunamo po ceniku z ločenim preverjenim izračunom. Koledar pokaže zasedenost, ne rezervacije. Človek presodi izjeme in potrdi točno različico ponudbe. n8n vodi zagon, čakanje in nadaljnja dejanja. Praznega ali nedostopnega vira ne obravnavamo kot potrditev, da ni omejitev.

## Razčleni svojo nalogo

| Naše vprašanje | Pri pripravi pokušine |
|---|---|
| Kaj želim doseči? | Izvedljiv predlog, ki ustreza želji stranke in ga lahko pregledam. |
| Kaj potrebujem za delo? | Povpraševanje, podatke stranke, cenik, koledar ter pravila podjetja in znamke. |
| Kako poteka naloga in kje se odločamo? | Agent poišče podatke, primerja možnosti in predlaga. Manjkajoče podatke dopolnimo, izjeme in ponudbo pregleda človek. |
| Kako preverim rezultat? | Preverim priporočilo v virih, ceno v izračunu ter vsebino PDF-ja in Gmailovega osnutka. |
| Kaj shranim in kako nadaljujem? | Preverjena pravila, razlog za popravek, različico in stanje. Poslovne podatke hranim v dogovorjeni zasebni shrambi. |

[Pet vprašanj](razclenitev-naloge.md) pomaga pri delu; za majhen poskus zadošča kratek dogovor.

## Začetna prošnja agentu

> Iz povpraševanja pripravi izvedljiv predlog pokušine. Upoštevaj naše pakete, cenik, razpoložljivost in poslovna pravila. Poišči potrebne podatke, pojasni priporočilo in opozori na manjkajoče informacije. Če nimaš dovolj podatkov, pripravi konkretna vprašanja. Pred potrditvijo potrebujem pregled predloga. Ne rezerviraj termina in ponudbe še ne pošiljaj stranki.

Za svoj primer zamenjaj pokušino s svojo nalogo. Claude naj najprej prebere tvoj profil in napredek. Učni profil Good Brew uporabi samo, kadar izrecno delaš na tej vaji; svojega profila ne prepisuj.

## Od prvega poskusa do ponovitve

1. Določi cilj in daj Claudu majhen dovoljen izbor podatkov.
2. Preglej, kaj je predlagal in katere informacije je uporabil.
3. Preveri pomembno trditev v viru. Popravi eno presojo in pojasni razlog.
4. Loči splošno pravilo od posebnosti tega povpraševanja. Shrani dogovor na pravo mesto.
5. Poskusi še drugo povpraševanje in preveri, ali je uporabil popravek.
6. Ko metoda deluje, dodaj povezave in ponavljajoče izvajanje.

Primerjava z osebnimi in poslovnimi navodili ter brez njih uporablja iste podatke. Preveri razliko v priporočilu, jeziku in tonu, tudi morebitne nove napačne obljube. Razlike ne predpostavljamo vnaprej.

## Kaj dodamo z n8n

V prikazu uporabljamo n8n Cloud, obrazec HubSpot, Google Sheets, Google Calendar, Gmail in Supabase. Delo je razdeljeno v dva poteka:

1. **Priprava predloga:** n8n prebere izbrano povpraševanje iz HubSpota in cenik. Claude pripravi priporočilo in uporabi orodje za izračun. n8n preveri rezultat ter ga shrani v Supabase. Ta potek trenutno zaženemo ročno za izbrane oddaje; nov vnos obrazca ga še ne sproži samodejno.
2. **Popravek in dokumenti:** na strani za pregled se prijaviš, odpreš ponudbo in napišeš, kaj je treba spremeniti. Zahteva sproži drugi potek v n8n. Ta pripravi novo različico, PDF in Gmailov osnutek s prilogo. Če navedeš točen datum in uro, preveri tudi koledar. Če termin manjka, pripravi osnutek z vprašanji za dopolnitev.

Pregled poteka na lokalni spletni strani, povezani s Supabase. Baza preveri prijavljenega uporabnika in različico, o kateri odloča. Odprta vprašanja preprečijo potrditev. Osvežitev strani samo prebere shranjeno stanje; nove priprave ne zažene.

Po pripravi n8n ponovno prebere Gmailov osnutek ter preveri naslovnika in prilogo. Ničesar ne pošlje, ne rezervira termina in ne posodobi CRM-ja. Za ta dejanja bi morali pripraviti ločene korake ter določiti, kdaj jih sme izvesti. Iskanje prostega termina po širšem obdobju še ni vključeno; za zdaj potrebujemo točen datum in uro.

Supabase hrani predloge, različice in odločitve. Petkova aplikacija lahko uporablja iste zapise. Pri svoji nalogi izberi shrambo po potrebi. Lokalna datoteka ni samodejno dostopna oblačnemu poteku.

Claude v Code pomaga graditi in preverjati n8n prek MCP. Zahteva za popravek pride v n8n iz strani za pregled. [Podrobnosti za agenta](../integrations/n8n/za-agenta.md).

## Kaj doda aplikacija

Aplikacija Ponudbe zbere povpraševanje, priporočilo, vire, izračun, popravke in odločitve. Uporabnik lahko dopolni podatke in zahteva ponovno pripravo. Preverimo dostop do posameznih zapisov in pravico do odobritve. »Odobreno«, »dokument izdelan« in »poslano« so različna stanja.

[Ponedeljek](ponedeljek-n8n.md) · [Petek](petek-aplikacija.md) · [Izbira orodja](izbira-orodja.md) · [Podporne veščine](podporne-vescine.md)
