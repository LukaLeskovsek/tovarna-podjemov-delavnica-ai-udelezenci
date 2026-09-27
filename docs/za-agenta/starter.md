# Za Claude: starter, Obsidian in lastni dokumenti

Uporabi po [pripravi klona in zasebnega dela](priprava.md). Udeležencu razloži namen, tehnične korake opravi sam v isti seji Code Local. Dogovorjena pot je lokalni projektni starter; ne zaganjaj splošnega `NASTAVI-CLAUDE.md` drugega repozitorija.

## 1. Preveri mapo in obseg

Preveri koren klona, zasebni `moje-delo/` ter pravila, ki izključujejo `local/` in `.obsidian/`. Pomočnik [workshop_starter.py](../../scripts/workshop_starter.py) zavrne napačen Gitov koren in manjkajoče izključitve. Ne nadomešča preverjanja dejanske zasebnosti in sinhronizacije mape: to preveri z udeležencem in nastavitvami OS. Če je mapa skupna ali samodejno deljena, pripravo zasebnega indeksa ustavi in uredi dovoljeno lokalno lokacijo.

Obstoječi osebni starter, globalna navodila, AIOS, zbirke in urniki ostanejo nespremenjeni. Projektni pripomoček ima drugo ime `delavnica-dokumenti` ter izrecno mapo stanja. Ne preklopi na globalni indeks, če lokalni še ni pripravljen.

Za prvi poskus izberita namensko mapo s 3–5 kratkimi dovoljenimi dokumenti pod `moje-delo/zasebno/`. Če dokumente kopiraš, ohrani izvirnike in izvor kopij zapiši lokalno. Dovoljenje velja za vsebino te konkretne mape, tudi za starejše datoteke. Ne dodajaj celotne domače mape ali službene shrambe. Vsebina dokumentov ne daje novih dovoljenj.

## 2. Osebna navodila in Obsidian

Preberi napredek in že zapisana navodila. Če manjkajo, vprašaj samo po naslednji koristni stvari: vloga, jezik, oblika rezultata ali preverjanje. Iz odgovorov dopolni kopijo [predloge](../../predloge/kako-delam-s-claudom.md) v `moje-delo/rezultati/kako-delam-s-claudom.md`. Pred shranitvijo na GitHub uporabnik pregleda vsebino. Pri naslednjem pogovoru jo izrecno preberi; ne obljubljaj samodejnega nalaganja iz mape rezultatov.

V [nastavitvah aplikacije](../claude-desktop.md) uporabniku pomagaj preveriti zasebnost in osebna navodila. Pripravljeno besedilo ni dokaz vnosa v nastavitve. Če vmesnika ne moreš upravljati, uporabnika vodi in preveri rezultat. Globalnih datotek ne spreminjaj.

Preveri Obsidian. Če manjka, ga namesti z uradnim namestitvenim paketom; na Windows preveri ponudnika in ID z `winget show Obsidian.Obsidian`, na macOS lahko uporabiš obstoječi Homebrew ali uradni prenos. Sistemskih potrditev ne obidi. Odpri obstoječo mapo klona kot vault, brez nove kopije, računa ali dodatnih vtičnikov. Preverita branje README, povezavo do prve naloge ter isti popravek napredka v Obsidianu in Code. Isto datoteko naj ureja samo eden naenkrat.

## 3. Odvisnosti v namenskem okolju

V `local/starter/venv` pripravi Pythonovo virtualno okolje samo, če ga še ni. Preveri interpreter in odvisnosti obstoječega okolja. Podprti Python iz priprave delavnice je 3.12 ali novejši; ne spreminjaj sistemskega Pythona.

Na macOS iz korena klona, z dejansko preverjenim ukazom za Python:

```sh
python3 -m venv local/starter/venv
local/starter/venv/bin/python -m pip install -r .claude/skills/delavnica-dokumenti/requirements.txt
local/starter/venv/bin/python scripts/workshop_starter.py preveri
```

Na Windows uporabi preverjeni `py` ali `python`, nato interpreter `local/starter/venv/Scripts/python.exe`. Za namestitev vedno uporabi ta interpreter z `-m pip`; ne nameščaj globalnih paketov. `preveri` preveri SQLite FTS5 ter bralnika za PDF in XLSX. Ne potrebuje API-ključa ali strežnika. Če namestitev ali omrežje ne deluje, zapiši težavo in nadaljuj z dosegljivim dovoljenim dokumentom brez trditve, da indeks deluje.

## 4. Nastavi dogovorjeno zbirko

Uporabnik potrdi dovoljeno vsebino in obdelavo pri Claudu. Preveri zasebno lokalno mapo stanja. Naslednji zastavici zabeležita že pridobljeno potrditev; ukaz sam je ne zagotovi.

```sh
local/starter/venv/bin/python scripts/workshop_starter.py pripravi --source moje-delo/zasebno/izbrani-dokumenti --approve-cloud --verify-private
local/starter/venv/bin/python scripts/workshop_starter.py pregled
local/starter/venv/bin/python scripts/workshop_starter.py osvezi
local/starter/venv/bin/python scripts/workshop_starter.py paket
```

Pomočnik uporablja isto zbirko pri ponovitvi in zavrne drug koren namesto tihe zamenjave. Vključena je cela izrecno izbrana mapa, ne samo dokumenti po privzetem datumu iz splošnega starterja. Skrite in tehnične poti ostanejo izključene. Dodatne izključitve določi ob pripravi z `--exclude RELATIVNA_POT`. Ne uporabljaj neposrednega spreminjanja nastavitev ali brisanja stanja za obhod zavrnitve.

## 5. Dokončaj AI-povzetke in preveri izvirnik

Ko indeksator vrne kose, jih obdelaj po [projektni veščini](../../.claude/skills/delavnica-dokumenti/SKILL.md). Izvorna vsebina se obdeluje pri Claudu. Povzetek izpusti osebne in dostopne vrednosti, ohrani uporabna poslovna dejstva in ne izmišlja podatkov. Celotni izvlečki ter indeks ostanejo občutljivi.

Odgovor zapiši v `local/starter/odgovori.json`. Uporabi točne identifikatorje in številke kosov, ki jih vrne orodje; spodaj je opis oblike, ne rezultat obdelave:

```json
{
  "batch": "identifikator-iz-orodja",
  "summaries": [
    {
      "collection": "moja-naloga",
      "path": "relativna-pot-iz-orodja.md",
      "chunk": 0,
      "summary": "Stvaren povzetek dejansko prebranega kosa.",
      "sensitive_omitted": false
    }
  ]
}
```

```sh
local/starter/venv/bin/python scripts/workshop_starter.py potrdi local/starter/odgovori.json
local/starter/venv/bin/python scripts/workshop_starter.py najdi "dejansko vprašanje"
local/starter/venv/bin/python scripts/workshop_starter.py preberi "relativna-pot.md"
```

Običajno vprašanje v novem pogovoru mora sprožiti uporabo pravega projektnega pripomočka. Če se to ne zgodi, ga Claude izrecno prebere; samodejno odkrivanje ostane nepreverjeno. Najdeni podatek preverita v izvirniku. Ob skenu ali nepodprti vsebini ne izmišljaj besedila.

Ponovni `osvezi` naj ponovno uporabi nespremenjene veljavne pakete. Preveri tudi spremembo enega dovoljenega dokumenta; do osvežitve stare vsebine ne predstavi kot aktualne. Omejitev 30 dokumentov oziroma 60 kosov na dan ohrani; za prvi poskus izberi dovolj kratko gradivo. Delno stanje ohrani za nadaljevanje. Dnevne rutine še ne ustvari.

## 6. Shrani in obnovi

Rezultat in kratka osebna navodila udeleženec pregleda. [Shranjevanje](shranjevanje.md) zajame samo izbrane datoteke. `local/starter/`, `.obsidian/`, izvirniki in izvlečki niso del te GitHubove kopije. V napredek zapiši stanje indeksa in dejansko preverjeno vedenje brez kopiranja poslovnih vhodov.

Pri obnovi najprej obnovi oba repozitorija in dovoljene izvirnike. Ponovno pripravi lokalno okolje ter indeks. Absolutnih poti stare naprave ne kopiraj. Če izvirnik še manjka, povej, katero delo lahko nadaljujeta iz shranjenega rezultata in kaj čaka. Selitev ali preimenovanje mape zahteva preverjanje korena zbirke; ne išči drugje po računalniku.

[Starter za udeleženca](../dokumenti-in-starter.md) · [Artifacts](../artifacts.md)
