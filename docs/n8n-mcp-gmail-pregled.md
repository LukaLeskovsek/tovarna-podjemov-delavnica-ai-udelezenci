# n8n, Gmail in pregled pred nadaljevanjem

[Od lokalnega Clauda do skupnega procesa — interaktivni diagram](../gradiva/interaktivno/lokalno-in-n8n.html). Preklopi računalnik in primerjaj, kje se izvaja delo.

Najprej s Claudom pripraviš in popraviš uporaben rezultat. Ko želiš isti postopek ponavljati, povezati več storitev ali ga zagnati ob določenem dogodku, ga lahko pripravita v n8n Cloud. Za začetek zadoščata ročni zagon in en dovoljeni primer tvoje naloge.

## Kaj je n8n in kdaj ga uporabiš

n8n je orodje za povezovanje storitev in avtomatizacijo poslovnih postopkov. Potek oziroma workflow določi, kaj sproži delo, katere podatke preberemo, kako jih obdelamo in kaj naredimo z rezultatom. Nekatere korake določajo pravila, pri razumevanju podatkov ali pripravi besedila pa lahko vključimo Clauda prek API-ja.

Pogosti poslovni primeri:

- **Prodaja:** iz povpraševanja pripravimo ponudbo, jo pregledamo in shranimo osnutek odgovora.
- **Finance:** zberemo račune in jih pripravimo za pregled odgovorni osebi.
- **Podpora:** zahtevek razvrstimo ter ga s povzetkom predamo pravi osebi.
- **Poročanje:** združimo podatke iz več virov in pripravimo pregled za ekipo.

To so možnosti za lastno nalogo. Potreben dostop in rezultat preverimo na tvojem konkretnem primeru.

## Storitve, ki jih v Claudu nimamo

Claude prek MCP pomaga upravljati n8n. Povezave do drugih storitev uredimo v n8n, tudi če v Claudu zanje ni neposrednega povezovalnika. Najprej preverimo obstoječa vozlišča. Če storitev ponuja API, lahko uporabimo HTTP Request z ustrezno prijavo in dovoljenji.

Za interni portal ali ERP preverimo tudi omrežni dostop. Če primerne povezave še ni, lahko prvi poskus opravimo z dovoljenim izvozom podatkov. MCP sam ne uredi dostopa do teh storitev.

## Kje teče n8n

| Možnost | Kaj pomeni |
|---|---|
| Na tvojem računalniku | Sam skrbiš za namestitev. Za izvajanje mora računalnik ostati vključen in dosegljiv. |
| Na lastnem strežniku | Podjetje ali izvajalec upravlja okolje, posodobitve in varnostne kopije. Strežnik je lahko v podjetju ali pri ponudniku oblaka. |
| n8n Cloud | n8n upravlja gostovanje in posodobitve. Za svoje poteke, povezave in dovoljene podatke skrbiš ti. |

**Na delavnici uporabljamo n8n Cloud.** Lokalni pregled predloga v Code ali spletni strani ne pomeni, da tudi n8n teče lokalno. Izbrana navodila in podatki pri klicu Claude API pridejo do ponudnika modela tudi pri lastni namestitvi n8n.

## Od osebne naloge do skupnega postopka

Pri oddelku ali podjetju isti potek uporablja več ljudi. Določimo, kdo prispeva podatke, kdo pregleda rezultat, kdo odloči o izjemi in kdo nadaljuje delo. Naslednja oseba mora videti stanje in pravo različico. Dogovorimo se tudi, kdo vzdržuje potek in ga lahko ustavi.

Deljenje povezav, skupni projekti in organizacijske pravice so odvisni od paketa in nastavitev. Začnemo z enim procesom in ga preverimo z ljudmi, ki ga bodo uporabljali.

## Kaj dela kje

| Del | Kaj počne |
|---|---|
| Claude Desktop, Code in MCP | S tabo načrtuje in ureja potek v tvojem n8n. Preveri povezave, pogleda izvedbo in pomaga pri popravku. |
| n8n Cloud | Zažene dogovorjene korake, bere povezane vire, shrani stanje in izvede dovoljena dejanja. Objavljen sprožilec ali urnik lahko deluje tudi, ko tvoj računalnik ne deluje. |
| Claude prek Anthropic API | Med izvedbo n8n interpretira podatke ali pripravi besedilo. Dobi samo navodila in podatke, ki mu jih potek dejansko posreduje. |
| Ti | Določiš merila, preveriš predlog in odločiš, kaj se sme zgoditi naslednje. |

Tvoj lokalni profil, veščine in `CLAUDE.md` pomagajo pri gradnji. Model v n8n jih ne bere samodejno. V potek prenesita samo pregledana pravila podjetja in sloga, ki jih naloga potrebuje. Zabeležita, katera pravila sta uporabila. Tudi Gmailova povezava v Claude Desktopu ne poveže Gmaila v n8n.

## Povezave pred prvim preizkusom

1. **n8n MCP:** uporabi svoj n8n Cloud. V nastavitvah omogoči Instance-level MCP, kopiraj njegov Server URL in ga dodaj v Claude Desktop med Connectors. Opravi prijavo OAuth. Nato odpri svojo delovno mapo v Code → Local in preveri, ali Claude vidi prava orodja. [Navodila za povezavo](../integrations/n8n/README.md).
2. **Gmail v n8n:** odpri Credentials oziroma izbiro povezave v vozlišču Gmail. Izberi Managed OAuth2 in Sign in with Google. Prijavi se v svoj dovoljeni račun. Na n8n Cloud pri tej poti ne potrebuješ lastnega projekta v Google Cloud Console. Če službena politika zavrne prijavo, potrebujeta pomoč skrbnika. Povezava lahko dovoljuje več dejanj, kot jih uporabimo v prvem poteku; dejanja posebej omejimo v poteku.
3. **Claude med izvedbo:** v n8n dodaj svojo povezavo Anthropic API, izberi razpoložljivi model in dogovorita omejitev porabe. Ključ vneseš neposredno v n8n. Dostop do Desktopa in nastavitev API sta ločena. Max in Team po aktualnih navodilih vključujeta mesečno dobroimetje za API; v svojem računu preveri stanje in omejitve porabe. Če tvoje okolje ponuja dostop prek n8n Gateway, naj Claude najprej preveri dejansko podporo in strošek; ne predpostavi, da je na voljo brezplačno.
4. **Dostop do podatkov:** določita en dokument, eno povpraševanje ali en pogovor. Ime shranjene povezave samo po sebi še ne potrjuje, da prava storitev in račun delujeta. Pred širšim branjem preverita račun in dovoljeni obseg.

## Začetna prošnja za Claude

Odpri mapo delavnice v Code → Local in prilepi:

```text
Preberi CLAUDE.md, moj napredek in relevantni profil. Nato preberi
integrations/n8n/za-agenta.md.

Želim pripraviti majhen potek v svojem n8n Cloud za eno svojo nalogo.
Pomagaj mi izbrati uporaben rezultat. Če je naloga že v napredku,
nadaljuj iz nje. Vprašaj me po eni manjkajoči stvari.

Najprej preveri povezavo MCP in orodja, ki jih dejansko vidiš.
Povej, kateri n8n projekt uporabljaš in katere povezave še manjkajo.
Prijave in vnos ključev opravim sam v oknih storitev.

Pred izdelavo predlagaj kratek načrt: katere podatke bomo uporabili,
kaj presodi Claude prek API-ja, kaj preverijo pravila in kje jaz
pregledam rezultat. V n8n prenesiva samo pregledana navodila iz
profila, ki jih ta naloga potrebuje.

Začniva z ročnim zagonom in enim dovoljenim primerom. Predlog mi
pokaži lokalno v Code ali v dogovorjenem prikazu. Pomagaj mi preveriti
vir in popraviti eno pomanjkljivost. Jasno povej, katero različico
pregledujem in kaj se bo zgodilo po moji potrditvi.

Če naloga vključuje e-pošto, preveri pravi Gmail račun in po potrditvi
pripravi samo osnutek. Nato ga ponovno preberi in preveri naslovnika,
besedilo ter priloge, če jih ima. Pošte ne pošiljaj. Ne pregleduj
celotnega predala, ne rezerviraj termina in ne vklopi urnika ali
javnega sprožilca brez posebnega dogovora.

Uporabi operate-workflow za pripravo izvedbe in verify-workflow za
preverjanje. Ob napaki najprej ugotovi, kaj je že nastalo; osnutka
ne ustvarjaj ponovno na slepo. V napredek shrani pregledana pravila,
opaženi rezultat in naslednji korak, brez pošte, ključev ali občutljivih
podatkov. Loči pripravljeno zasnovo od dejansko preverjene povezave.
```

Če ne potrebuješ e-pošte, isti pristop uporabi pri svojem dokumentu, primerjavi ali drugem rezultatu. Za uspešno delo ni treba uporabiti vseh prikazanih storitev.

## Kako poteka lokalni pregled

Pri prvem poskusu naj n8n pripravi predlog, Claude pa ti ga pokaže v lokalnem Code pogovoru ali datoteki. Preveriš vsebino in pojasniš popravek. Ko potrdiš konkretni predlog, Claude začne posebej dogovorjeni naslednji korak, na primer shranjevanje osnutka v Gmail.

To sta dve ločeni izvedbi. Ne predpostavimo, da en klic MCP ostane odprt in čaka na tvojo odločitev. Trenutni `execute_workflow` ne podpira potekov s čakanjem na človeka ali večstopenjskimi obrazci. Za tak proces uporabimo dejanski obrazec oziroma drug podprti sprožilec. Claude lahko prek MCP pomaga pri gradnji in branju stanja.

Pri postopku, ki mora nadaljevati tudi po novem pogovoru ali z drugim pregledovalcem, n8n oziroma izbrana shramba ohrani predlog, njegovo različico in odločitev. Lokalna stran lahko prek prijavljene povezave bere to stanje in shrani odločitev. n8n Cloud sam ne more odpreti tvojega `127.0.0.1`, lokalnih datotek ali pogovora. Odločitev mu mora izrecno poslati dogovorjeni način nadaljevanja. Če pregleda ni, potek ostane brez dovoljenja za naslednje dejanje.

| Tvoja odločitev | Kaj se zgodi |
|---|---|
| Potrdiš predlog | Nadaljuje se samo dogovorjeno dejanje za to različico. Potrditev osnutka ne pomeni dovoljenja za pošiljanje. |
| Zahtevaš popravek | Komentar pojasni spremembo. Nastane nova različica, ki jo ponovno pregledaš. |
| Zavrneš ali ne odgovoriš | Končno dejanje se ne izvede. Pri daljšem čakanju določita tudi rok in ravnanje po izteku. |

## Gmailov osnutek in zaključni preizkus

V n8n za pripravo e-pošte uporabimo **Gmail → Resource: Draft → Operation: Create**. Osnutek odpreš v Gmailovi mapi Drafts oziroma Osnutki. Preveriš naslovnika, zadevo, besedilo in prilogo. Pošiljanje je poznejše, ločeno dejanje.

Preizkus naj pokaže, da:

- pravi račun vrne dogovorjene podatke, ne celega predala;
- predlog uporablja preverjena pravila in navede, kaj manjka;
- popravek spremeni rezultat, stara potrditev pa ne velja za novo vsebino;
- Gmail vsebuje pravi osnutek in prilogo, n8n pa shrani njun dejanski ID;
- ponovitev istega primera ne ustvari dodatnega osnutka;
- pri nedoločenem izidu najprej preverita Gmail, nato odločita o nadaljevanju.

Za vsak preizkus povej, ali je uporabil dejanski račun ali nadomestne podatke. Preizkus s pripetimi podatki potrjuje logiko poteka, ne delovanja Gmaila ali modela API.

[Gradivo za ponedeljek](ponedeljek-n8n.md) · [Navodila za agenta](../integrations/n8n/za-agenta.md)

## Uradna navodila

Preverjeno 12. 10. 2026. Razpoložljivost orodij, modelov in dovoljenj preverimo še v tvojem računu.

- [n8n MCP: povezovanje](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)
- [MCP: zagon in omejitve](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference)
- [Google Managed OAuth2 na n8n Cloud](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-single-service/)
- [Gmail: ustvarjanje in branje osnutkov](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations/)

- [Claude: dostop do aplikacije, API in dobroimetje](https://support.claude.com/en/articles/9876003-i-have-a-paid-claude-subscription-pro-max-or-team-plans-why-do-i-have-to-pay-separately-to-use-the-api)

- [Kaj je n8n](https://docs.n8n.io/)
- [n8n Cloud in lastna namestitev](https://docs.n8n.io/choose-n8n/)
- [HTTP Request za dostop do API-ja](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/)
