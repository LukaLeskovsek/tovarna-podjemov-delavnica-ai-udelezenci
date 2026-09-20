# Priprava na delavnico

Skupaj bomo pripravili Claude, račune in mapo za tvoje delo. Na koncu boš naredil/a majhno nalogo, jo shranil/a v svoj zasebni GitHub repozitorij ter nadaljeval/a v novem pogovoru. Izvajalec in Claude te vodita po korakih; ukazov si ni treba zapomniti.

## Pred prihodom

- Prinesi svoj prenosnik in polnilec. Potrebuješ dostop do interneta, svoje e-pošte in telefona oziroma aplikacije za potrditev prijave.
- Preveri prijavo v svoj [Claude račun](https://claude.ai/) in svoj [GitHub račun](https://github.com/). Če GitHub računa še nimaš, ga ustvari po [uradnih navodilih](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) ter potrdi e-pošto. Poskrbi tudi za večfaktorsko prijavo in varno shranjene obnovitvene kode.
- Za osnovno pot potrebuješ dostop do **Claude Code**. Preveri ga v svojem računu; prijava v običajni pogovor še ni dokaz dostopa do Code. Izbiro ali spremembo naročnine potrdiš sam/a. Možnosti preveri v [uradnem začetnem vodniku](https://code.claude.com/docs/en/quickstart).
- Če uporabljaš službeno napravo, vnaprej preveri dovoljenje za namestitve, uporabo računov in poslovnih podatkov. Če to ureja IT, prinesi informacijo, kaj še manjka.
- Izberi eno ponavljajočo se nalogo. Za pripravo zadošča izmišljeni primer, zato zaupnih datotek še ni treba prinašati.
- Če so orodja že nameščena, jih ohrani. Njihovo delovanje bomo najprej preverili. Če pri namestitvi nisi prepričan/a, jo opravi na setup urah z izvajalcem.

Vsak uporablja svoje račune. Gesel, ključev in obnovitvenih kod ne deli z izvajalcem ali Claudom in jih ne zapisuj v gradiva.

## 1. Pripravi računalnik

Osnovna orodja so **Claude Code**, **Git**, **GitHub CLI (`gh`)** in **Python 3.12 ali novejši**. Git vodi različice datotek, GitHub hrani izbrane varnostne kopije, `gh` omogoča delo s tvojim GitHub računom. Python poganja priloženi pomočnik za preverjanje in shranjevanje.

Izberi eno okolje in v njem opravi vse korake. Spodnja Windows pot uporablja običajni Windows. Če že uporabljaš WSL, naj izvajalec najprej preveri, da so orodja in mapa v istem okolju.

### Windows

Odpri **PowerShell**. Najprej preveri `git --version`, `gh --version` in `python --version`. Če Python ni najden, preveri še `py --version`. Namesti samo manjkajoče:

| Orodje | Namestitev |
|---|---|
| Git | [Git for Windows](https://git-scm.com/install/windows); če je WinGet na voljo: `winget install --id Git.Git -e --source winget` |
| GitHub CLI | Po [uradnih navodilih](https://github.com/cli/cli/blob/trunk/docs/install_windows.md#winget): `winget install --id GitHub.cli --source winget`. Brez WinGet uporabi uradni namestitveni paket za svojo napravo. |
| Python | [Uradni prenos](https://www.python.org/downloads/). Trenutna Windows navodila uporabljajo Python Install Manager; odpri nov terminal in preveri delujoči Python 3.12+. [Podrobnosti](https://docs.python.org/3/using/windows.html). |
| Claude Code | Za grafično delo namesti [Claude Desktop](https://code.claude.com/docs/en/desktop) in uporabi zavihek **Code**. Za terminalno pot je spodaj uradni ukaz. |

Terminalni Claude Code namestiš v PowerShell z:

```powershell
irm https://claude.ai/install.ps1 | iex
```

Ukaz prenese in zažene uradni namestitveni program. Uporabi ga le, če smeš nameščati programsko opremo na tej napravi. Po namestitvah **zapri terminalno okno in odpri novo**; ponovno zaženi tudi Claude Desktop. Nov zavihek starega terminala morda ne prevzame nove poti do orodij.

### macOS

Odpri **Terminal**. Najprej preveri `git --version`, `gh --version` in `python3 --version`. Namesti samo manjkajoče:

| Orodje | Namestitev |
|---|---|
| Git | Po [uradnih možnostih za macOS](https://git-scm.com/install/mac): `xcode-select --install` za Apple Command Line Tools; če že uporabljaš Homebrew, lahko uporabiš `brew install git`. |
| GitHub CLI | Če že uporabljaš Homebrew: `brew install gh`. Sicer izberi uradni paket za svoj Mac po [navodilih GitHub CLI](https://github.com/cli/cli#installation). |
| Python | Uporabi obstoječi Python 3.12+ ali stabilni macOS namestitveni paket z [uradne strani](https://www.python.org/downloads/). |
| Claude Code | Za grafično delo namesti [Claude Desktop](https://code.claude.com/docs/en/desktop) in uporabi **Code**. Za terminalno pot uporabi spodnji ukaz. |

```sh
curl -fsSL https://claude.ai/install.sh | bash
```

Ukaz prenese in zažene uradni namestitveni program. Po namestitvi ponovno odpri terminal in Claude Desktop.

### Preveri, da orodja res delujejo

Git in `gh` morata izpisati različico. Za terminalno pot mora delovati tudi `claude --version`; pri Desktop preveri dostop do lokalne seje v zavihku Code. To sta dve možnosti za uporabo Claude Code, ni treba namestiti obeh. Namestitveni ukazi so povzeti po [uradnem vodniku](https://code.claude.com/docs/en/quickstart).

Pythonov ukaz mora pokazati različico **3.12 ali višjo**. V nadaljevanju gradivo uporablja `python3`. Če je na tvojem Windows računalniku delujoči ukaz `python` ali `py`, ga uporabi namesto `python3` pri vseh priloženih skriptah. Izbiro zapišita v tvoj napredek. Ne ustvarjaj dodatnih namestitev samo zaradi imena ukaza.

Če agent v svoji seji orodja ne najde, čeprav deluje v terminalu, naj izvajalec preveri delovno okolje in pot do orodja ter ponovno zažene aplikacijo.

## 2. Prijavi svoj GitHub račun

Izvajalec ti pomaga preveriti obstoječo prijavo. Če je še ni, v terminalu zaženi:

```sh
gh auth login --hostname github.com --git-protocol https --web
```

Sam/a dokončaj prijavo in potrdi pravo identiteto v brskalniku. Nato preveri:

```sh
gh api user --jq .login
```

Izpis mora biti tvoje predvideno GitHub uporabniško ime. Prijava na spletni strani ni isto kot prijava tega orodja. Če imaš več računov, pred nadaljevanjem izberita pravega. [Uradna navodila za prijavo](https://cli.github.com/manual/gh_auth_login).

Za zasebno shranjevanje mora biti prijavljen tudi Git. Če še nima ustrezne nastavitve, po razlagi izvajalca uporabi:

```sh
gh auth setup-git --hostname github.com
```

To v uporabniških Git nastavitvah poveže prijavo za GitHub z `gh`. Obstoječe nastavitve najprej preverita. [Kaj ukaz nastavi](https://cli.github.com/manual/gh_auth_setup-git).

## 3. Kloniraj gradivo

Z izvajalcem izberi lokalno mapo za delavnico, zunaj drugih Git projektov. V terminalu odpri njeno nadrejeno mapo. `delavnica` naj bo novo ime mape; če že obstaja, najprej preverita vsebino.

```sh
git clone https://github.com/LukaLeskovsek/tovarna-podjemov-delavnica-ai-udelezenci.git delavnica
cd delavnica
```

Za nadaljnje posodabljanje potrebuješ običajni klon. Na GitHubu ti ni treba ustvariti forka ali uporabiti predloge.

## 4. Odpri Claude v pravi mapi

**Claude Desktop:** odpri **Code**, izberi okolje **Local** in obstoječo mapo `delavnica`. Delaj v tej mapi na veji `main`, brez dodatne izolirane kopije prek worktree. Agent naj preveri dejansko pot: osebna podmapa `moje-delo/` pripada temu klonu. [Navodila za izbiro okolja in mape](https://code.claude.com/docs/en/desktop).

**Terminal:** iz mape `delavnica` zaženi `claude`. Ob prvem zagonu se prijavi s svojim ustreznim Claude računom. Za to pot uporabi prijavo z naročnino; ločenega API ključa za delavnico ne nastavljamo. Če že uporabljaš službeno API okolje, ga najprej preveri z izvajalcem.

Skupaj preverita, kako ustaviš agenta in pregledaš predlagano spremembo. Za prvi preizkus izberi način s pregledom in potrditvijo sprememb. Nato v **pogovor s Claudom** kopiraj:

> Danes pripravljava okolje za delavnico. Preberi CLAUDE.md in docs/setup.md. Preveri mojo lokalno mapo, vejo main, orodja in GitHub identiteto. Nato me vodi skozi pripravo zasebnega shranjevanja in majhno nalogo z izmišljenimi podatki. Povej, kaj boš ustvaril ali spremenil; prijave opravim sam/a. Sprašuj po eno vprašanje.

## 5. Uredi zasebno shranjevanje

Claude sledi [postopku za Git in napredek](git-in-napredek.md). Pomaga ti ustvariti samostojni repozitorij `moje-delo/`, izbrati prosto ime lastnega zasebnega repozitorija na GitHubu ter preveriti lastnika in zasebnost. Primer imena je `tp-ai-moje-delo`.

Preden nadaljuješ, naj ti pokaže:

- javno mapo `delavnica/` in ločeno osebno mapo `delavnica/moje-delo/`;
- tvojega GitHub uporabnika in zasebni cilj, ki mu pripada;
- ime ter izbrano e-pošto avtorja shranitev;
- kam sodijo pregledani rezultati in kam surovi vhodi.

Pregledane izbrane rezultate shranjuješ v `moje-delo/rezultati/`, napredek v `moje-delo/napredek.md`. Surovi vhodi v `moje-delo/zasebno/` ostanejo zunaj GitHub varnostne kopije. Izvajalec ne dobi dostopa do tvojega zasebnega repozitorija samodejno. Službene podatke uporabi le v dovoljeni shrambi.

## 6. Naredi majhno nalogo, shrani in nadaljuj

Izberi svojo majhno nalogo ali vpiši:

> Iz tega izmišljenega sporočila pripravi kratek odgovor: »Delavnica je v četrtek ob 9.00. Prinesi prenosnik in polnilec. Lokacijo še potrdimo.« Odgovor naj potrdi uro in opremo ter vpraša za lokacijo. Shrani ga v moje-delo/rezultati/setup-preizkus.md. Ničesar ne pošiljaj. Nato me prosi, naj preverim tri podatke.

Odpri rezultat in preveri uro, opremo ter neznano lokacijo. Nato napiši:

> Posodobi moj napredek in shrani to srečanje. V moj zasebni repozitorij shrani samo pregledani napredek in ta rezultat. Najprej pokaži izbrane datoteke in spremembe.

Claude uporabi osebni checkpoint, na primer `session-01`. Odpri svoj repozitorij na GitHubu: preveri oznako **Private**, datoteki in checkpoint. Ob prvem shranjevanju je pričakovan tudi `.gitignore`. Če pošiljanje ne uspe, je rezultat **»Shranjeno lokalno, ni varnostno kopirano.«** Po odpravi težave ponovita pošiljanje istega checkpointa.

Zapri pogovor, odpri novega v isti mapi in napiši **»Preberi moj napredek in nadaljuj.«** Claude mora najti shranjeni rezultat in naslednje dejanje. Nato poskusi še **»Posodobi gradiva.«** Tvoj rezultat mora po posodobitvi ostati na mestu.

## 7. Preveri zaključek priprave

- [ ] V svojem računu uporabljam Claude Code in znam odpreti pravo lokalno mapo.
- [ ] Claude iz te seje vidi Git, `gh` in ustrezen Python.
- [ ] Znam pokazati svoj GitHub račun in ločeni zasebni repozitorij.
- [ ] Odprl/a in pregledal/a sem prvi rezultat.
- [ ] Moj checkpoint je viden v zasebnem repozitoriju na GitHubu.
- [ ] V svežem pogovoru znam nadaljevati iz napredka.
- [ ] Posodobitev gradiv je uspela in osebno delo je ostalo na mestu.

Če kaj manjka, v napredek zapišita: **kaj manjka, kdo uredi in kaj preverimo naslednjič**. Samo lokalno shranjena datoteka še nima varnostne kopije na GitHubu.

## Druge storitve

Za prvi korak dodatni CRM, avtomatizacijski servis ali API ključ niso potrebni. Če tvoja naloga uporablja Microsoft 365 ali drugo storitev, pripravi svoj dovoljeni račun. Z izvajalcem izberita povezavo, preverita dovoljenja in naredita majhen preizkus v tvojem računu. Nakup, povezavo ali objavo potrdiš za dejansko izbrano uporabo. Namestitev sama še ni dokaz delovanja.

Namestitve in prijava: uradni viri preverjeni **20. 9. 2026**. Če se prikaz razlikuje, z izvajalcem odpri povezani aktualni vir.

[Začetek](../README.md) · [Računi in dostopi](racuni-in-dostopi.md) · [Shranjevanje in posodobitve](git-in-napredek.md)
