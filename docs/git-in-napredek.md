# Posodabljanje gradiva in shranjevanje dela

Gradivo kloniraš ob začetku delavnice, nove datoteke pa pozneje preneseš s posodobitvijo. Svoje delo shranjuješ ločeno, v zasebnem repozitoriju, ki ga Claude ustvari v podmapi `moje-delo/`.

```text
delavnica/                 skupna javna gradiva
  CLAUDE.md
  koraki/
  moje-delo/               tvoj samostojni zasebni repozitorij
    napredek.md
    skills/                tvoje veščine za ponavljajoče delo
    rezultati/             izbrani pregledani rezultati
    zasebno/               izvorni podatki in prepisi, zunaj Gita
```

To sta dva običajna neodvisna repozitorija. Zunanji ignorira celotno `moje-delo/`; notranji ima svoja pravila za izključene podatke. Mapa ni podmodul in ne potrebuje posebnega načina posodabljanja.

Spodnje ukaze lahko zate izvede Claude. Ti izbereš nalogo, pregledaš rezultat in se odločiš, katere datoteke želiš shraniti.

Za prvo namestitev in prijavo sledi [navodilom za pripravo](setup.md). Spodnji `python3` na Windows po potrebi zamenjaj s preverjenim `python` ali `py` različice 3.12 ali novejše. Ukaze izvajaj v istem okolju in prvotnem lokalnem klonu, kjer je tvoj `moje-delo/`.

## 1. Uredi svojo zasebno shrambo

Claude naj preveri [potrebna orodja in prijavo](racuni-in-dostopi.md), uporabnika v GitHubu ter ime in e-pošto, s katerima Git označuje shranjene spremembe (commite). Preveri naj tudi, ali lahko Git pošlje datoteke na GitHub; prijava na spletni strani sama ne zadošča. Če to še ni urejeno, po razlagi uporabi `gh auth setup-git --hostname github.com`, kot piše v [navodilih za pripravo](setup.md). O preklopu računa ali spremembi splošnih nastavitev Gita se najprej dogovorita. Ime in e-pošto avtorja lahko nastavi samo za notranji repozitorij.

Iz korena `delavnica/`:

```sh
python3 scripts/participant_git.py init
```

Ta korak pripravi lokalni samostojni repozitorij `moje-delo/` ter pravila, katere datoteke naj Git izpusti. Sam ne ustvarja spletnega repozitorija. Če osebno delo ali povezava že obstajata, ju najprej preverita in ohranita.

Claude preveri račun z `gh api user --jq .login`. Nato udeleženec izbere prosto ime svojega zasebnega repozitorija. V naslednjem primeru zamenjaj `TVOJ-LOGIN` z dejanskim preverjenim uporabniškim imenom in `IME-REPOZITORIJA` z izbranim imenom:

```sh
gh repo create TVOJ-LOGIN/IME-REPOZITORIJA --private
git -C moje-delo remote add origin https://github.com/TVOJ-LOGIN/IME-REPOZITORIJA.git
```

Pred ustvarjanjem se dogovorita za račun in ime. Drugi ukaz naj Claude izvede šele, ko preveri, da je nastal pravi zasebni repozitorij. Če repozitorij že obstaja ali ustvarjanje ne uspe, naj najprej ugotovi, kaj se je zgodilo. Obstoječe povezave ne sme prepisati. Na GitHubu preverita še lastnika in oznako Private. Izvajalca ni treba dodati kot sodelavca.

Kopijo [predloge napredka](../predloge/napredek.md) shrani kot `moje-delo/napredek.md`. Izvorne poslovne datoteke shrani v `moje-delo/zasebno/`. V `rezultati/` daj samo kopijo rezultata, ki si ga pregledal in želiš shraniti.

## 2. »Posodobi gradiva«

Claude preveri zunanji repozitorij in nato posodobi njegovo vejo `main`:

```sh
python3 scripts/participant_git.py check-update
git pull --ff-only
```

Drugi ukaz izvede samo, če je preverjanje uspešno, in iz korena skupnega gradiva. Predhodno preverjanje zahteva pričakovani javni izvor, vejo `main`, čisto stanje in odsotnost razhajanja z zadnjim lokalno znanim stanjem `origin/main`. Sam `pull --ff-only` nato pridobi in preveri najnovejše oddaljeno stanje. Morebitne lokalne osebne spremembe v `moje-delo/` niso ovira.

Če so v skupnem gradivu tvoji popravki ali dodatni commiti, se Claude ustavi in pojasni težavo. Sprememb ne sme samodejno umakniti, ponastaviti zgodovine ali česa prepisati na silo. Osebne prilagoditve shranjujta v `moje-delo/`.

Oznake, kot sta `start-v1` in `meeting-01-v1`, označujejo izdaje skupnega gradiva. Za običajno nadaljevanje ostaneš na `main`; ni treba preklapljati na oznako. Claude po posodobitvi pove, kaj je na novo na voljo.

## 3. »Shrani srečanje«

Najprej dopolni napredek: kaj je narejeno in preverjeno, kaj sta se dogovorila, kaj še ni jasno in kaj sledi. Nato s Claudom izbereta datoteke, ki jih želiš shraniti. Spodnji primer shrani napredek in že pripravljeni pregled. Poti štejejo od mape `moje-delo/`:

```sh
python3 scripts/participant_git.py checkpoint --tag session-01 --files napredek.md rezultati/pregled.md --preview
```

Claude pregleda seznam datotek in njihove spremembe. Preveri, da je koren Gita točno `moje-delo/` in da je povezan s tvojim zasebnim repozitorijem. V izboru ne sme biti izvornih podatkov, prepisov, ključev ali podatkov, za katere nimaš dovoljenja. Pri prvem shranjevanju se doda tudi notranji `.gitignore`. Drugih že pripravljenih sprememb ne sme vključiti brez dogovora.

Ko je izbor pravilen in ustreza temu, kar želiš shraniti, izvede isti ukaz brez `--preview`:

```sh
python3 scripts/participant_git.py checkpoint --tag session-01 --files napredek.md rezultati/pregled.md
```

Pomočnik ustvari commit in osebno oznako ter ju pošlje v tvoj zasebni repozitorij. Naslednjo shranitev označi drugače, na primer z `session-02`. Te oznake niso vezane na izdaje gradiva ali število srečanj. Obstoječih oznak ne premikaj.

Če pošiljanje ne uspe, naj Claude pove **»Shranjeno lokalno, ni varnostno kopirano.«** Ko je povezava spet na voljo, ponovi pošiljanje istega checkpointa:

```sh
python3 scripts/participant_git.py retry --tag session-01
```

Datoteke pod `zasebno/` niso vključene v to varnostno kopijo. Zanje uporabi drugo dovoljeno shrambo. Pravila podjetja za prenos podatkov veljajo tudi za zasebni repozitorij na GitHubu.

## 4. Nadaljevanje na drugem računalniku

Ponovno kloniraj javno gradivo. Nato v njegovem korenu kloniraj svoj preverjeni zasebni repozitorij v `moje-delo/`; te mape pred kloniranjem še ne sme biti. Claude naj najprej preveri natančni URL tvojega repozitorija in stanje map.

Izvorne podatke po potrebi obnovi iz svoje dovoljene shrambe. Nato napiši: **»Preberi moj napredek in nadaljuj.«** Zapisani napredek omogoča nadaljevanje brez celotne zgodovine pogovora.

[Začetek](../README.md) · [1. korak](../koraki/01-zacetek.md)
