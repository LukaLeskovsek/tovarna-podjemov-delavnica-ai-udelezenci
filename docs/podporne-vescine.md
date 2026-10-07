# Veščine, ki ti pomagajo pri delu

V mapi `.claude/skills/` je dvanajst podpornih veščin. Vsaka vsebuje navodila za določeno vrsto pomoči. Claude naj uporabi tisto, ki koristi tvoji nalogi. Račune, dostop do podatkov in delovanje povezav preverita posebej.

Za konkreten potek od prvega osnutka do shranjene metode odpri [primer poročila](od-poskusa-do-metode.md). Če še nimaš svoje naloge, ti pomaga [kratek pogovor o prejšnjem tednu](izberi-nalogo.md).

## Pregled veščin

| Veščina (skill) | Pri čem pomaga | Kaj lahko napišeš |
|---|---|---|
| [delavnica-personalizacija](../.claude/skills/delavnica-personalizacija/SKILL.md) | Tvoj profil in podjetje | »Pomagaj mi pripraviti profil.« |
| [delavnica-dokumenti](../.claude/skills/delavnica-dokumenti/SKILL.md) | Iskanje po dokumentih | »Poišči dogovor o rokih.« |
| [deconstruct-workflow](../.claude/skills/deconstruct-workflow/SKILL.md) | Pregled postopka | »Kako poenostavim pripravo poročila?« |
| [prepare-context](../.claude/skills/prepare-context/SKILL.md) | Podatki za nalogo | »Kaj še potrebuješ za to analizo?« |
| [package-workflow](../.claude/skills/package-workflow/SKILL.md) | Navodila za ponovitev | »Shrani ta postopek kot mojo veščino.« |
| [verify-workflow](../.claude/skills/verify-workflow/SKILL.md) | Preverjanje rezultata | »Preveri poročilo in manjkajoče podatke.« |
| [review-workflow-run](../.claude/skills/review-workflow-run/SKILL.md) | Iskanje vzroka napake | »Zakaj si sporočilo označil kot nujno?« |
| [maintain-knowledge](../.claude/skills/maintain-knowledge/SKILL.md) | Popravljanje znanja | »Popravi rok in preveri naslednji odgovor.« |
| [publish-knowledge](../.claude/skills/publish-knowledge/SKILL.md) | Gradivo za ekipo | »Pripravi navodila, ki jih smem deliti.« |
| [graduate-artifact](../.claude/skills/graduate-artifact/SKILL.md) | Od prototipa do aplikacije | »Kaj manjka za uporabo v ekipi?« |
| [operate-workflow](../.claude/skills/operate-workflow/SKILL.md) | Redna opravila | »Uredi dnevni pregled in njegovo ustavitev.« |
| [design-agent-team](../.claude/skills/design-agent-team/SKILL.md) | Delitev dela med agente | »Bi tu pomagalo več agentov?« |

Prošnjo dopolni s svojo nalogo, podatki, ki jih smeš uporabiti, in želenim rezultatom. Veščin ti ni treba znati na pamet ali jih uporabiti vseh. Pregled lahko odpreš tudi kot [enostranski PDF](../gradiva/vescine-hiter-pregled-v2.pdf).

## Kako jo Claude uporabi

Nalogo mu razloži v običajnem jeziku. Po potrebi izbere ustrezno veščino in prebere njena navodila. Če je ne najde, mu lahko poveš neposredno:

> Preberi `.claude/skills/deconstruct-workflow/SKILL.md` in mi pomagaj pregledati, kako sem zadnjič opravil svojo nalogo.

Preveri, da uporablja datoteko iz trenutne mape delavnice. Če imaš starejšo osebno nameščeno kopijo, je ne prepisujta; Claude naj pove, katera navodila je prebral.

## Tvoja lastna veščina

Iz postopka, ki si ga preizkusil in pregledal, pripraviš svojo poslovno veščino. Shraniš jo v `moje-delo/skills/`. Claude jo po potrebi prebere; ta mapa sama ne omogoči, da jo samodejno najde.

Podporne veščine uporabljajo isti [profil](personalizacija.md). Dogovore o tebi in podjetju zato hranimo na enem mestu. Po popravku preverita, ali ga Claude upošteva pri naslednjem rezultatu. GBrain in Internal OS Starter sta [neobvezni nadgradnji](neobvezne-nadgradnje.md).

[Kaj je v paketu](kaj-dobis-s-paketom.md) · [Tvoja prva naloga](../koraki/01-zacetek.md) · [Pet vprašanj za pregled naloge](razclenitev-naloge.md)
