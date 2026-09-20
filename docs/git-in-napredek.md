# Nova gradiva in tvoje shranjeno delo

Skupna gradiva kloniraš enkrat. Nova dobiš z običajnim Git pull. Tvoje delo je v ločenem zasebnem repozitoriju, ki ga Claude ustvari v podmapi `moje-delo/`.

```text
delavnica/                 skupna javna gradiva
  CLAUDE.md
  koraki/
  moje-delo/               tvoj samostojni zasebni repozitorij
    napredek.md
    skills/                tvoje ponovno uporabne spretnosti
    rezultati/             izbrani pregledani rezultati
    zasebno/               surovi vhodi in prepisi, zunaj Gita
```

To sta dva običajna neodvisna repozitorija. Zunanji ignorira celotno `moje-delo/`; notranji ima svoja pravila za izključene podatke. Mapa ni podmodul in ne potrebuje posebnega načina posodabljanja.

Naslednje ukaze lahko izvede Claude. Udeleženec izbere nalogo, pregleda rezultat in odloča o vsebini, ki jo želi shraniti.

Za prvo namestitev in prijavo sledi [setup vodniku](setup.md). Spodnji `python3` na Windows po potrebi zamenjaj s preverjenim `python` ali `py` različice 3.12 ali novejše. Ukaze izvajaj v istem okolju in prvotnem lokalnem klonu, kjer je tvoj `moje-delo/`.

## 1. Priprava osebnega shranjevanja

Claude naj preveri [predpogoje in prijavo](racuni-in-dostopi.md), trenutno GitHub identiteto ter avtorja commitov. Preveri tudi prijavo za Git push; prijava na spletni strani sama ne zadostuje. Če Git še ni ustrezno povezan, po razlagi uporabi `gh auth setup-git --hostname github.com`, kot opisuje [setup](setup.md). Ne preklaplja računov ali ne spreminja globalnih Git nastavitev brez razlage in dogovora. Za avtorja tega projekta lahko uporabi lokalne nastavitve notranjega repozitorija.

Iz korena `delavnica/`:

```sh
python3 scripts/participant_git.py init
```

Ta korak pripravi lokalni samostojni repozitorij `moje-delo/` in njegove izključitve. Sam ne ustvarja spletnega repozitorija. Če osebno delo ali povezava že obstajata, ju najprej preverita in ohranita.

Claude preveri račun z `gh api user --jq .login`. Nato udeleženec izbere prosto ime svojega zasebnega repozitorija. V naslednjem primeru zamenjaj `TVOJ-LOGIN` z dejanskim preverjenim uporabniškim imenom in `IME-REPOZITORIJA` z izbranim imenom:

```sh
gh repo create TVOJ-LOGIN/IME-REPOZITORIJA --private
git -C moje-delo remote add origin https://github.com/TVOJ-LOGIN/IME-REPOZITORIJA.git
```

Pred ustvarjanjem mora biti jasno, kateri račun in ime bosta uporabljena. Drugi ukaz izvede šele po uspešnem ustvarjanju in preverjanju pravega zasebnega repozitorija. Ob obstoječem repozitoriju ali neuspelem ustvarjanju naj Claude najprej preveri stanje, namesto da poskuša prepisati izvor. Nato preveri lastništvo in zasebnost na GitHubu. Izvajalca ni treba dodati kot sodelavca.

Kopijo [predloge napredka](../predloge/napredek.md) shrani kot `moje-delo/napredek.md`. Izvorne poslovne datoteke sodijo v `moje-delo/zasebno/`. Samo namenska kopija pregledanega rezultata sodi v `rezultati/`.

## 2. »Posodobi gradiva«

Claude preveri zunanji repozitorij in nato posodobi njegovo vejo `main`:

```sh
python3 scripts/participant_git.py check-update
git pull --ff-only
```

Drugi ukaz izvede samo, če je preverjanje uspešno, in iz korena skupnega gradiva. Predhodno preverjanje zahteva pričakovani javni izvor, vejo `main`, čisto stanje in odsotnost razhajanja z zadnjim lokalno znanim stanjem `origin/main`. Sam `pull --ff-only` nato pridobi in preveri najnovejše oddaljeno stanje. Morebitne lokalne osebne spremembe v `moje-delo/` niso ovira.

Če si spremenil/a skupno gradivo ali ustvaril/a svoj commit v zunanjem repozitoriju, Claude pojasni težavo in se ustavi. Ne shrani sprememb skrito na stran, ne ponastavi zgodovine in ničesar ne prepiše na silo. Osebne prilagoditve naredita v `moje-delo/`.

Oznake, kot sta `start-v1` in `meeting-01-v1`, označujejo izdaje skupnega gradiva. Za običajno nadaljevanje ostaneš na `main`; ni treba preklapljati na oznako. Claude po posodobitvi pove, kaj je na novo na voljo.

## 3. »Shrani srečanje«

Najprej posodobi napredek: rezultat, dokaz, odločitve, odprta vprašanja in naslednje dejanje. Nato s Claudom izbereta konkretne pregledane datoteke. Ta primer shrani napredek in že pripravljen pregled, pri čemer so poti podane glede na `moje-delo/`:

```sh
python3 scripts/participant_git.py checkpoint --tag session-01 --files napredek.md rezultati/pregled.md --preview
```

Claude prebere predogled in točne spremembe. Preveri, da je Git koren točno `moje-delo/`, izvor tvoj zasebni repozitorij, izbor pa ne vsebuje surovih vhodov, prepisov, ključev ali drugih neodobrenih podatkov. Prvemu checkpointu se samodejno pridruži notranji `.gitignore`. Nepovezanih že pripravljenih sprememb ne dodaja na skrivaj.

Ko izbor ustreza tvoji prošnji za shranjevanje, izvede isti ukaz brez `--preview`:

```sh
python3 scripts/participant_git.py checkpoint --tag session-01 --files napredek.md rezultati/pregled.md
```

Pomočnik ustvari commit in osebno oznako ter ju pošlje v tvoj zasebni izvor. Naslednji dosežek dobi novo oznako, npr. `session-02`. Osebne oznake so neodvisne od izdaj gradiva; število checkpointov ni vezano na urnik srečanj. Obstoječih oznak ne premikaj.

Če pošiljanje ne uspe, je pravilen status **»Shranjeno lokalno, ni varnostno kopirano.«** Ko je povezava spet na voljo, ponovi pošiljanje istega checkpointa:

```sh
python3 scripts/participant_git.py retry --tag session-01
```

Izključene datoteke pod `zasebno/` s tem postopkom niso varnostno kopirane. Zanje uporabi svojo dovoljeno shrambo. Tudi zaseben Git repozitorij je zunanja shramba; poslovna pravila za podatke še vedno veljajo.

## 4. Nadaljevanje na drugem računalniku

Ponovno kloniraj javno gradivo. Nato v njegovem korenu kloniraj svoj preverjeni zasebni repozitorij v `moje-delo/`; ta mapa mora biti pred kloniranjem neobstoječa. Claude naj najprej preveri natančni URL tvojega repozitorija in stanje map.

Surove vhode po potrebi obnovi iz svoje dovoljene shrambe. Nato napiši: **»Preberi moj napredek in nadaljuj.«** Zapisani napredek omogoča nadaljevanje brez celotne zgodovine pogovora.

[Začetek](../README.md) · [1. korak](../koraki/01-zacetek.md)
