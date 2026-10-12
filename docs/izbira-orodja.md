# Kdaj uporabimo Claude, n8n ali svojo aplikacijo

Začni pri opravilu, ki ga želiš izboljšati. Več orodij pomeni tudi več priprave in vzdrževanja. Novo orodje dodamo, ko nam pri konkretni nalogi prihrani delo ali omogoči nekaj, kar potrebujemo.

## Zakaj n8n

V prvem pogovoru s Claudom določimo nalogo, podatke in merila. Pri povpraševanju za degustacijo skupaj preverimo stranko, cenik in termin ter popravimo predlog. Tako ugotovimo, kaj agent potrebuje za samostojno delo.

V n8n povežemo branje podatkov, Claudovo presojo in pregled ponudbe. V našem prikazu n8n prebere povpraševanje in cenik, Claude pa razume zahtevo, uporabi izračun ter pripravi priporočilo ali vprašanja. Predlog shranimo v Supabase. Človek ga pregleda na spletni strani; zahteva za popravek sproži pripravo nove različice, PDF-ja in Gmailovega osnutka. Koledar preverimo pri točnem terminu. Pošiljanje, rezervacija in spremembe v CRM-ju še niso vključeni.

Agent presoja, n8n pa skrbi za dogovorjeni potek, stanje in dovoljene zapise. Če je postopek popolnoma določen s pravili, modela za ta del ne potrebujemo. Pri nejasnem povpraševanju je njegova korist v razumevanju zahteve, izbiri virov ter utemeljitvi predloga.

Claude v Desktop Code nam pomaga tak potek zgraditi prek MCP. To je ločena vloga od Clauda, ki med zagonom prejema API klice iz n8n. Povezava MCP ne nadomesti povezav do modela ali drugih storitev.

To je koristno, kadar:

- se večji del postopka ponavlja in znaš opisati njegove korake;
- podatke ali odločitve predajaš med več storitvami in ljudmi;
- potrebuješ vidno stanje izvedbe, čakanje na odločitev in obravnavo napak;
- želiš postopek izvajati v oblaku neodvisno od odprtega računalnika.

n8n sam ne določi poslovnih pravil, ne preveri kakovosti besedila in ne prepreči vsake podvojitve. To moramo zasnovati in preizkusiti. Tudi preprosta avtomatizacija potrebuje odgovorno osebo, delujoče povezave in dogovorjeno porabo.

Če nalogo opravljaš občasno in ti sodelovanje s Claudom že ustreza, ostani pri njem. Tudi Claude ima možnosti načrtovanega dela; urnik sam zato ni razlog za n8n. Prednost n8n pri našem primeru je pregledno povezovanje korakov, storitev in človeške odločitve.

[Odpri interaktivno primerjavo](../gradiva/interaktivno/zakaj-n8n.html). V GitHubu prenesi HTML in ga odpri v brskalniku. To je učni prikaz z vnaprej pripravljenimi odzivi, brez povezave do računov in modela.

## Kam sodijo Claude Managed Agents

Claude Managed Agents je Anthropicova storitev za izvajanje agentov v upravljanem okolju. Določiš model, navodila, orodja, veščine in okolje ter zaženeš sejo. Agent lahko izvaja daljšo nalogo in uporablja več orodij. Storitev podpira tudi načrtovane zagone in nadaljevanje sej. Trenutno je v beta različici. [Uradni pregled](https://platform.claude.com/docs/en/managed-agents/overview)

Smiselna je na primer za zahtevnejšo zadevo, pri kateri mora agent primerjati več dokumentov, poiskati manjkajoče podatke in šele nato pripraviti predlog. n8n lahko vodi širši postopek, takšno zadevo preda agentu in nadaljuje po prejetem rezultatu. To povezavo je treba posebej zgraditi in preveriti.

| Možnost | Primer prošnje | Kaj moraš urediti |
|---|---|---|
| Claude ob pogovoru | Pomagaj mi pripraviti predlog za to povpraševanje. | Dovoljeni podatki, navodila in pregled rezultata. |
| n8n z modelom Claude | Preveri vire, pripravi predlog ponudbe in počakaj na odločitev. | Potek, povezave, pravila, stanje, izjeme in poraba API-ja. |
| Claude Managed Agents | Razišči to nejasno zadevo in pripravi utemeljen predlog. | Agentska seja, orodja, dovoljenja, podatki, proračun in merila uspeha. |
| Kombinacija | Zahtevne zadeve predaj agentu, ostale obdela dogovorjeni potek. | Poleg obeh delov še njuna predaja, čakanje, napake in glavno stanje. |

Pri orodjih, ki jih izvaja storitev Managed Agents, lahko nastavimo zahtevo za odobritev. Pri lastnih orodjih mora dovoljenje uveljaviti naša aplikacija. Nastavitev orodja, poslovna odobritev in identiteta odločevalca so ločene stvari. [Pravila dovoljenj](https://platform.claude.com/docs/en/managed-agents/permission-policies)

V ponedeljek ostanemo pri modelu Claude v n8n AI Agent. Managed Agents je neobvezna nadgradnja. Potrebuje svoj API dostop in obračun. Lokalni profil ter povezovalniki Desktop se ne prenesejo samodejno. Pred uporabo preveri tudi hranjenje podatkov: dokumentacija navaja shranjevanje zgodovine, stanja in rezultatov na strežniku ter trenutno ne podpira Zero Data Retention za to storitev. Za prikaz uporabljamo dovoljene podatke; pošte ne nalagamo samo zato, da preizkusimo novo orodje.

## Zakaj bi gradili interno aplikacijo

Artifact je lahko uporabno orodje tudi po prvem preizkusu. V podprtih paketih omogoča uporabo Clauda, povezovalnikov ter osebno ali skupno shrambo podatkov. Več uporabnikov, povezava ali shranjevanje sami po sebi še ne pomenijo, da moramo zgraditi aplikacijo. Možnosti preveri v svojem računu in glede na vrsto Artifakta. [Aktualna navodila za Artifacts](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)

Pri aplikaciji Ponudbe vprašamo: ali ustvarjalec vidi svoje predloge, ali pregledovalec potrdi pravo različico in ali znamo ugotoviti, kaj se je zgodilo po potrditvi? Ko dodamo svoje poslovne zahteve, se lahko pokaže potreba po aplikaciji.

| Potreba | Kaj najprej preverimo |
|---|---|
| Osebni ali skupni seznam | Ali Artifact že omogoča potrebno shranjevanje in deljenje? |
| Različne pravice do posameznih zapisov | Ali lahko z drugim računom dejansko preprečimo nedovoljen dostop? |
| Zgodovina poslovnih odločitev | Ali hranimo avtorja, čas, različico predloga in rezultat izvedbe? |
| Lastna podatkovna baza in integracije | Ali lahko podatke upravljamo, izvozimo in obnovimo tako, kot podjetje potrebuje? |
| Neodvisno gostovanje ali drugačna prijava | Ali obstoječa platforma omogoča zahtevani način uporabe? |
| Delovanje v ozadju | Kje teče opravilo? Potrebujemo n8n ali drugo storitev; sam vmesnik ga ne zažene. |

Internal OS Starter pomaga pri prijavi, podatkovni bazi, modulih in dostopih. Poslovno funkcijo in pravila moramo še zgraditi. Prevzamemo tudi vzdrževanje, stroške, varnostne kopije in odpravljanje napak. Začnemo z eno funkcijo, ki ima jasen razlog in konkreten preizkus.

[Odpri interaktivni izbor zahtev](../gradiva/interaktivno/od-artifakta-do-aplikacije.html). Izbirnik uporabniške vloge je samo ponazoritev; resničen preizkus pravic zahteva dve prijavi in preverjanje na strežniku.

## Kaj napišeš Claudu

> Preberi mojo nalogo, napredek in profil. Pomagaj mi ugotoviti, ali mi zadošča Claude oziroma Artifact, ali potrebujem n8n, daljšo agentsko izvedbo ali svojo aplikacijo. Pri vsaki dodatni storitvi pojasni konkretno korist, potrebno pripravo in vzdrževanje. Najprej preveriva eno resnično omejitev trenutne rešitve. Ne nameščaj dodatnih orodij samo zaradi primerjave.

Viri preverjeni 10. in 11. oktobra 2026. To potrjuje vsebino dokumentacije, ne delovanja povezav v posameznem računu.
