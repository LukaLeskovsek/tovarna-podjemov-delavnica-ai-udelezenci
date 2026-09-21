# Delavnica AI · Tovarna podjemov

Na delavnici boš s Claudom delal na svojih nalogah. Lahko pripraviš sestanek, primerjaš ponudbe, urediš preglednico ali napišeš odgovor na sporočilo. Začeli bomo s konkretnim primerom in sproti pogledali, kaj ti pri delu pomaga.

## Pred začetkom

Na pripravljalnem srečanju bomo uredili račune in računalnik. V [navodilih za pripravo](docs/setup.md) najdeš, kaj potrebuješ, kako namestiš orodja na Windows ali macOS in kako preveriš, da lahko svoje delo shraniš ter naslednjič nadaljuješ.

1. Potrebuješ svoj račun za Claude in svoj račun za GitHub. Na računalniku naj bodo Claude Code, Git, GitHub CLI in Python 3.12 ali novejši. Podrobnosti so v [navodilih za račune in dostop](docs/racuni-in-dostopi.md).
2. Prenesi gradivo z naslednjim ukazom. Izvedeš ga lahko v terminalu ali za pomoč prosiš agenta:

   ```sh
   git clone https://github.com/LukaLeskovsek/tovarna-podjemov-delavnica-ai-udelezenci.git delavnica
   ```

3. Odpri mapo `delavnica` v Claude Code in napiši:

   > Začniva delavnico. Preberi CLAUDE.md in me vodi skozi prvi korak.

4. Claude ti bo zastavljal po eno vprašanje. Skupaj bosta uredila shranjevanje in izbrala prvo nalogo. Uporabiš lahko svoj primer, če imaš dovoljenje za uporabo podatkov, ali eno od pripravljenih vaj.

## Ko se vrneš k delu

| Kaj želiš narediti | Kaj napišeš Claudu |
|---|---|
| Nadaljevati | »Preberi moj napredek in nadaljuj tam, kjer sva ostala.« |
| Prenesti novo gradivo | »Posodobi gradiva.« |
| Shraniti opravljeno delo | »Shrani srečanje.« |

Novo gradivo preneseš z `git pull --ff-only`. Svoje delo hraniš ločeno, v zasebnem repozitoriju v mapi `moje-delo/`. Posodobitev gradiva zato ne posega v tvoje datoteke. Claude pred shranjevanjem preveri, v kateri mapi dela in kam bo poslal datoteke. [Več o shranjevanju in posodobitvah](docs/git-in-napredek.md).

## Gradivo za začetek

- [1. korak: opravi prvo nalogo](koraki/01-zacetek.md).
- [Vaja z desetimi izmišljenimi kontakti](exercises/conference/README.md): Excel in CSV, pravila ter kopija podatkov iz izmišljenega CRM-ja.
- [Predlogi za Word in PowerPoint ter vaja s sporočili](assets/office/README.md).
- [Predloga za zapis napredka](predloge/napredek.md).

Prodajna vaja je eden od primerov. Izberi nalogo, ki jo potrebuješ pri svojem delu.

## Kaj sledi

Na naslednjih srečanjih bomo spoznali še druga orodja in načine dela. Več časa bomo namenili temam, ki vam pri delu najbolj koristijo. Gradivo bomo dodajali sproti.

| Tema | Kaj boš lahko naredil | Gradivo |
|---|---|---|
| 1. Vsakdanje delo | Opraviš prvo nalogo, preveriš rezultat in shraniš dogovore za naslednjič | Na voljo |
| 2. Opis postopka | Zapišeš korake, pravila in odločitve pri svoji nalogi | Dodamo pozneje |
| 3. Ponovna uporaba | Shraniš navodila kot veščino, ki jo lahko uporabiš tudi na drugih primerih | Dodamo pozneje |
| 4. Povezave z drugimi storitvami | Claudu omogočiš dostop do izbranih virov in določiš, kaj sme z njimi narediti | Dodamo pozneje |
| 5. Znanje in popravki | Shraniš uporabne ugotovitve skupaj z viri in jih po potrebi popraviš | Dodamo pozneje |
| 6. Prototip in aplikacija | Svojo zamisel preizkusiš v preprostem prototipu | Dodamo pozneje |
| 7. Redna opravila in druge naprave | Nastaviš ponavljajoče opravilo ali nadaljuješ delo na drugi napravi | Dodamo pozneje |
| 8. Skupno delo | Povežeš korake, pri katerih sodeluje več ljudi, in določiš, kdo o čem odloča | Dodamo pozneje |
| 9. Preizkus in predaja | Preveriš postopek na novem primeru in pripraviš navodila za sodelavca | Dodamo pozneje |
| 10. Predstavitev rezultatov | Pokažeš, kaj uporabljaš, kaj se je izboljšalo in kaj želiš razvijati naprej | Dodamo pozneje |

Pri vsaki temi lahko delaš na svoji nalogi, sodeluješ pri skupni vaji ali spremljaš prikaz. Če te kaj posebej zanima, lahko nadaljuješ tudi samostojno. V navodilih so te možnosti označene kot **Delo na svoji nalogi**, **Skupna vaja ali prikaz** in **Dodatno samostojno delo**. Ni treba, da za svojo nalogo uporabiš vsa orodja.

Ta repozitorij je javen. Osebnih podatkov, poslovnih primerov in rezultatov ne dodajaj vanj. Zase uporabljaš svoj zasebni repozitorij na GitHubu; izvajalec nima samodejnega dostopa do njega.
