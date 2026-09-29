# Priprava za Claude: od prvega zagona do nadaljevanja

To so podrobna navodila za agenta. Udeležencu razloži namen naslednjega dejanja, nato izvedi tehnični del. Ne zasuj ga z ukazi. Upoštevaj že dogovorjena dovoljenja. Ne nameščaj orodij, če uporabnik želi samo pregled navodil.

## 1. Preveri okolje

Glavna pot je **Claude Desktop → Code → Local**, neposredno na Windows ali macOS. Uporabnik namesti aplikacijo in se prijavi, preden lahko prevzameš pripravo. Ne preusmerjaj začetnika v terminal, WSL, oblak ali worktree. Če obstoječa organizacijska nastavitev preprečuje Local, zapiši blokado in potrebni ukrep IT.

Pred kloniranjem preveri absolutno pot, vsebino pripravljalne mape in ali je del drugega repozitorija. Gradiva kloniraj v novo podmapo `delavnica`. Če cilj že obstaja, ga preglej; ne briši ga in ne kloniraj čez osebno delo. Obstoječi pravi klon uporabi po preverjanju.

## 2. Namesti samo manjkajoče

Preverjanja izvajaš iz svojega okolja, ne le iz drugega odprtega terminala. Zabeleži uporabni rezultat, ne prepisov seje.

| Orodje | Preverjanje | Namen |
|---|---|---|
| Git | `git --version` | Prenos gradiv in shranjevanje različic. |
| Python 3.12+ | `python3 --version`; na Windows tudi `python --version` ali `py --version` | Obstoječi pomočnik za zasebno shranjevanje in delo z datotekami. |
| Node.js, podprta izdaja LTS | `node --version` in `npm --version` | Delo z dodatnimi programi in izdelki, kadar jih naloga potrebuje. |
| GitHub CLI | `gh --version` | Urejanje zasebne shrambe v uporabnikovem GitHubu. |

Python in Node.js pripravljamo za program delavnice; nista navedena kot pogoj za samo namestitev aplikacije Claude. Posebne namestitve terminalnega Claude CLI ne zahtevaj, če lokalni Code deluje.

Na Windows najprej preveri WinGet in uporabi uradne ponudnike: Git.Git, GitHub.cli, ustrezni Python in OpenJS.NodeJS.LTS. Pred namestitvijo preveri identifikator in ponudnika z `winget show`; različice Pythona ne sklepaj samo iz imena paketa. Če WinGet ni na voljo, uporabi uradni namestitveni paket in uporabniku prepusti sistemsko potrditev.

Na macOS uporabi že nameščeni Homebrew, če je na voljo in ga uporabnik uporablja. Git lahko zagotavljajo Apple Command Line Tools. Brez upravljalnika uporabi uradne namestitve; ne dodajaj novega upravljalnika samo zaradi enega orodja. Ohranjenih namestitev ne nadomeščaj na slepo in ne spreminjaj sistemskega Pythona. Predlagaj podprto različico šele po pregledu obstoječe.

Uradni viri: [Git](https://git-scm.com/install/), [Python](https://www.python.org/downloads/), [Node.js](https://nodejs.org/en/download), [GitHub CLI](https://cli.github.com/), [Claude Desktop](https://code.claude.com/docs/en/desktop).

Po namestitvi preveri orodja v Code. Če jih aplikacija še ne vidi, jo ponovno odpri in ponovi preverjanje. Na Windows ni dovolj nov zavihek starega terminala. Zapiši delujoči ukaz za Python; pri vseh nadaljnjih ukazih uporabi isto preverjeno različico.

Preizkusi še majhen Pythonov in Node.js izračun oziroma zapis v začasno mapo. Obstoj datoteke in prebrana vsebina potrdita, da lahko orodji dejansko zaženeš. Ne nameščaj globalnih dodatkov za prihodnje sklope.

## 3. Prijava in klon

Uporabnik se v GitHub prijavi sam, po potrebi z `gh auth login --hostname github.com --web`. Preveri `gh api user --jq .login` in se z uporabnikom prepričaj, da je to pravi račun. Gesel, žetonov ali obnovitvenih kod ne izpisuj.

Če Git še nima primernega načina prijave, po razlagi uporabi `gh auth setup-git --hostname github.com`. Obstoječe druge prijave in nastavitve najprej preveri, ne prepiši jih na slepo. [Uradna prijava](https://cli.github.com/manual/gh_auth_login).

Iz preverjene pripravljalne mape kloniraj:

```sh
git clone https://github.com/LukaLeskovsek/tovarna-podjemov-delavnica-ai-udelezenci.git delavnica
```

Preveri `origin`, vejo `main` in prisotnost `CLAUDE.md`. Povej točno mapo, ki naj jo uporabnik odpre v **Code → Local**, brez worktree izolacije. V novem pogovoru preberi tamkajšnja navodila. Ne uporabljaj ZIP-a namesto klona.

## 4. Zasebno delo, Obsidian in starter

Preberi [postopek shranjevanja](shranjevanje.md). Najprej preveri, da zunanji repozitorij ignorira celotno `moje-delo/`, nato pripravi notranji repozitorij in zasebni cilj v lasti preverjenega uporabnika. Pred zapisovanjem poslovnih vhodov preveri izključene poti.

Nato pripravi osebna navodila in isto mapo v Obsidianu po [navodilih](starter.md). Dokumentni indeks preizkusi na nekaj dovoljenih dokumentih, vendar ne ustavljaj prve naloge s pošto, če dokumentov še ni. Za skupni primer preberi [navodila za pošto](e-posta.md); računa in dostop preveri pred branjem. Pred uporabo podatkov skupaj preglejta [osnove in nastavitve aplikacije](../claude-desktop.md).

Vprašaj po dejanski nalogi. Če datoteke ni, predlagaj izvedljivo nalogo iz udeleženčevega dela, ki jo lahko opiše. Neobvezno vajo ponudi šele, če svojega primera ne more uporabiti. Udeleženec pregleda vsebino rezultata, ti pa preveriš datoteko, točen izbor za shranjevanje in zasebno varnostno kopijo.

V novem pogovoru preberi `moje-delo/napredek.md` in `moje-delo/rezultati/kako-delam-s-claudom.md`, če obstaja, najdi rezultat in predlagaj pravo naslednje dejanje. Že obstoječega napredka ne ponastavi. Obnovitev iz drugega računalnika sledi navodilu za shranjevanje.

## 5. Kaj zapišeš

V napredek zapiši OS, Local in delovno mapo, delujoči ukaz za Python, stanje orodij, preverjeni GitHub račun in zasebni cilj brez skrivnosti. Dodaj stanje Obsidiana, lokalnega indeksa in Artifakta (ali označene nadomestne datoteke), prvi rezultat, opaženo preverjanje, stanje varnostne kopije in naslednje dejanje. Ne ustvarjaj ločenih administrativnih dokumentov, če zadošča ta zapis.

Če kaj manjka, zapiši natančno težavo, naslednji ukrep in odgovorno osebo. Preverjen del ohrani. Priprave ne označi kot uspešne samo zato, ker so navodila napisana ali ker je namestitev delovala na drugem računalniku.

Dodatne račune pripravi pred pripadajočim sklopom. n8n uporabljamo v **n8n Cloud**, brez lokalne namestitve ali Dockerja. Podrobna navodila pridejo z objavo tega sklopa.
