# Ponedeljek: agent uporablja podatke in orodja

Na srečanju 12. oktobra 2026 s Claudom pripravimo in preverimo agenta za pripravo predloga pokušine Good Brew. Najprej opazujemo, kako razume zahtevo in presoja. Nato dodamo orodja, popravimo eno pravilo ter pripravimo ponovljivo izvedbo v n8n. Vodeni del traja približno 75 minut, nato delaš na svoji nalogi. [Opis skupnega primera](povprasevanje-ponudba.md).

## Pred srečanjem

Pripravi svoj Claude, delovno mapo z napredkom in dovoljen primer svoje naloge. Za živo povezavo uporabi svoj n8n Cloud in [povezovalnik n8n](../integrations/n8n/README.md). Dodatne storitve pripravi, kadar jih tvoja naloga potrebuje. Za Good Brew uporabljamo HubSpot Free in Google Workspace; Intrix ostane ločen CRM-primer v programu.

Za Claude v n8n potrebuješ svoj Anthropic API dostop z dogovorjeno omejitvijo porabe. Naročnina na Claude Desktop sama ne uredi teh klicev. Ključ vneseš v shrambo poverilnic n8n. Povezave do Google Workspace in CRM urediš posebej v n8n; povezovalniki iz Desktopa se ne prenesejo samodejno.

Če računi še niso pripravljeni, začni z dovoljenimi lokalnimi podatki. To potrdi način dela, ne povezave do storitev.

## Kaj boš videl

| Del | Njegova naloga |
|---|---|
| Claude v Code | Z nami načrtuje, gradi prek MCP, pregleda izvedbo in popravi napako. |
| Agent v n8n s Claude | Uporabi prejete podatke in izračun ter pojasni, zakaj predlaga določeno ponudbo. |
| Poslovna pravila in izračun | Določajo cene in dovoljene pogoje. Agent jih ne spreminja po svoje. |
| n8n | Vodi zagon, stanje, čakanje na človeka in dogovorjena dejanja. |
| Ti | Določiš cilj in pooblastila, preveriš presojo ter odločiš o izjemah in ponudbi. |

Lokalni profil, veščine in CLAUDE.md niso samodejno na voljo modelu v n8n. Izbereš samo pregledana navodila podjetja in znamke, ki jih potrebuje. Za osnovni prikaz uporabljamo Anthropicov model, izvajanje agenta pa vodi n8n. Claude Managed Agents so neobvezna nadgradnja.

## Začni na svoji nalogi

V prikazu prvi potek zaženemo ročno za izbrano oddajo HubSpot. Popravek nato sprožiš na strani za pregled ponudbe. Nastaneta PDF in Gmailov osnutek; pošiljanje, rezervacija in zapisovanje v CRM še niso vključeni. [Opis obeh potekov](povprasevanje-ponudba.md#kaj-dodamo-z-n8n).

Za neposreden začetek uporabi [prošnjo za n8n, Gmail in lokalni pregled](n8n-mcp-gmail-pregled.md). V njej so tudi povezava Gmail, pregled predloga in preverjanje osnutka.

> Preberi moj napredek in profil. Pomagaj mi izbrati majhen del naloge, kjer potrebujem presojo in delo s podatki. Določiva cilj, vire, dovoljena orodja in način preverjanja. Vprašaj me po eni manjkajoči stvari. Najprej narediva poskus ob pogovoru, preveriva rezultat in popraviva eno težavo. Ko metoda deluje, uporabi operate-workflow in integrations/n8n/za-agenta.md za načrt ponovljive izvedbe. Zunanjega pošiljanja in urnika še ne vklopi.

Za [neobvezni primer Good Brew](../exercises/goodbrew/pokusina/README.md) uporabi učni profil in začetno prošnjo iz njegovega kazala. Ne prepisuj svojega osebnega profila.

## Prenesi pristop na svoje delo

1. Povej, kaj naj agent doseže in kaj bo uporaben rezultat.
2. Daj mu dosegljive podatke. Preveri, ali so za sklep dovolj dobri.
3. Preglej priporočilo in izvirnik. Popravi eno presojo ter pojasni razlog.
4. S package-workflow shrani preverjeno metodo. Poskusi drug primer.
5. Za povezave in ponovitev uporabi operate-workflow. Z verify-workflow preveri celotno nalogo; review-workflow-run pomaga pri napaki.

Pri odobritvi moraš videti vire, izračun, besedilo, opozorila in naslednja dejanja. Popravek potrebuje novo različico in nov pregled. Ponovitev istega povpraševanja ne sme ustvariti novega dokumenta. Če dokument nastane, CRM pa odpove, naj bo vidno, kateri del še manjka.

Prikaz s čakanjem na odločitev zaženemo skozi dejanski obrazec oziroma dogovorjeni sprožilec. Pri prvem lokalnem pregledu lahko ločimo pripravo predloga in nadaljevanje po tvoji potrditvi. Claude prek MCP pomaga graditi in pregledovati; razpoložljiva orodja preveri v tvoji seji.

## Kaj shraniš

Shrani pregledana pravila, opis metode in kratek napredek brez občutljivih podatkov. Dejanska povpraševanja, podatki strank, ključi in dnevniki ostanejo v dogovorjeni zasebni shrambi. Iz izvoza n8n odstrani tudi pripete vzorčne podatke.

Naslednjič napiši »Nadaljujva.« Za svojo nalogo ni treba uporabiti vseh prikazanih storitev.

[Arhitektura: računalnik, n8n in oddelki](../gradiva/interaktivno/lokalno-in-n8n.html) · [Interaktivni prikaz poteka](../gradiva/interaktivno/zakaj-n8n.html) · [Petek: aplikacija](petek-aplikacija.md) · [Neobvezna vaja odobritve](../integrations/n8n/neobvezna-vaja.md)
