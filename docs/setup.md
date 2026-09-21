# Priprava na delavnico

Na pripravljalnem srečanju bomo namestili potrebna orodja, uredili prijave in odprli mapo za tvoje delo. Nato boš opravil kratko nalogo, jo shranil v svoj zasebni repozitorij na GitHubu in nadaljeval v novem pogovoru. Pri tem ti bosta pomagala izvajalec in Claude. Ukazov si ni treba zapomniti.

## Pred prihodom

- Prinesi svoj prenosnik in polnilec. Potrebuješ internetno povezavo, dostop do svoje e-pošte in telefon oziroma aplikacijo za potrditev prijave.
- Preveri, ali se lahko prijaviš v svoj [račun za Claude](https://claude.ai/) in svoj [račun za GitHub](https://github.com/). Če računa za GitHub še nimaš, ga ustvari po [uradnih navodilih](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) ter potrdi e-pošto. Uredi tudi dodatno preverjanje ob prijavi (MFA) in obnovitvene kode shrani na varno.
- Za delavnico potrebuješ **Claude Code**. V svojem računu preveri, ali ga lahko uporabljaš. To preveri posebej, tudi če običajni pogovor s Claudom že deluje. O izbiri ali spremembi naročnine se odločiš sam. Možnosti preveri v [uradnem začetnem vodniku](https://code.claude.com/docs/en/quickstart).
- Če uporabljaš službeno napravo, vnaprej preveri dovoljenje za namestitve, uporabo računov in poslovnih podatkov. Če to ureja IT, prinesi informacijo, kaj še manjka.
- Izberi eno ponavljajočo se nalogo. Za pripravo zadošča izmišljeni primer, zato zaupnih datotek še ni treba prinašati.
- Če so orodja že nameščena, jih ohrani. Njihovo delovanje bomo najprej preverili. Če pri namestitvi potrebuješ pomoč, jo bomo uredili skupaj na pripravljalnem srečanju.

Vsak uporablja svoje račune. Gesel, ključev in obnovitvenih kod ne deli z izvajalcem ali Claudom in jih ne zapisuj v gradiva.

## 1. Pripravi računalnik

Osnovna orodja so **Claude Code**, **Git**, **GitHub CLI (`gh`)** in **Python 3.12 ali novejši**. Git beleži spremembe datotek, na GitHub pa shraniš njihovo varnostno kopijo. Z orodjem `gh` lahko Claude uporablja tvoj račun za GitHub. Python potrebujemo za priloženi program, ki preverja in shranjuje delo.

Izberi eno okolje in v njem opravi vse korake. Spodnja navodila za Windows veljajo za delo neposredno v Windows. Če že uporabljaš WSL, z izvajalcem preverita, da tudi orodja in mapa delavnice uporabljajo to okolje.

### Windows

Odpri **PowerShell**. Najprej preveri `git --version`, `gh --version` in `python --version`. Če Python ni najden, preveri še `py --version`. Namesti samo manjkajoče:

| Orodje | Namestitev |
|---|---|
| Git | [Git for Windows](https://git-scm.com/install/windows); če je WinGet na voljo: `winget install --id Git.Git -e --source winget` |
| GitHub CLI | Po [uradnih navodilih](https://github.com/cli/cli/blob/trunk/docs/install_windows.md#winget): `winget install --id GitHub.cli --source winget`. Brez WinGet uporabi uradni namestitveni paket za svojo napravo. |
| Python | [Uradni prenos](https://www.python.org/downloads/). Trenutna Windows navodila uporabljajo Python Install Manager; nato odpri nov terminal in preveri, ali je nameščeni Python različice 3.12 ali novejši. [Podrobnosti](https://docs.python.org/3/using/windows.html). |
| Claude Code | Za delo v aplikaciji namesti [Claude Desktop](https://code.claude.com/docs/en/desktop) in uporabi zavihek **Code**. Če boš uporabljal terminal, je ukaz za namestitev spodaj. |

Za namestitev Claude Code v terminalu v PowerShell vpiši:

```powershell
irm https://claude.ai/install.ps1 | iex
```

Ukaz prenese in zažene uradni namestitveni program. Uporabi ga le, če smeš nameščati programsko opremo na tej napravi. Po namestitvah **zapri terminalno okno in odpri novo**; ponovno zaženi tudi Claude Desktop. Če odpreš samo nov zavihek, terminal novih orodij morda še ne bo našel.

### macOS

Odpri **Terminal**. Najprej preveri `git --version`, `gh --version` in `python3 --version`. Namesti samo manjkajoče:

| Orodje | Namestitev |
|---|---|
| Git | Po [uradnih možnostih za macOS](https://git-scm.com/install/mac): `xcode-select --install` za Apple Command Line Tools; če že uporabljaš Homebrew, lahko uporabiš `brew install git`. |
| GitHub CLI | Če že uporabljaš Homebrew: `brew install gh`. Sicer izberi uradni paket za svoj Mac po [navodilih GitHub CLI](https://github.com/cli/cli#installation). |
| Python | Uporabi obstoječi Python 3.12+ ali stabilni macOS namestitveni paket z [uradne strani](https://www.python.org/downloads/). |
| Claude Code | Za delo v aplikaciji namesti [Claude Desktop](https://code.claude.com/docs/en/desktop) in uporabi **Code**. Za delo v terminalu uporabi spodnji ukaz. |

```sh
curl -fsSL https://claude.ai/install.sh | bash
```

Ukaz prenese in zažene uradni namestitveni program. Po namestitvi ponovno odpri terminal in Claude Desktop.

### Preveri, da orodja res delujejo

Ukaza za preverjanje Gita in `gh` morata izpisati različico. Če uporabljaš terminal, preveri še `claude --version`. V aplikaciji Claude Desktop pa preveri, ali lahko v zavihku Code odpreš lokalno mapo. Izbereš lahko eno od teh dveh možnosti. Ukazi za namestitev so iz [uradnega vodnika](https://code.claude.com/docs/en/quickstart).

Pythonov ukaz mora pokazati različico **3.12 ali višjo**. V nadaljevanju gradivo uporablja `python3`. Če na tvojem računalniku z Windows deluje ukaz `python` ali `py`, ga uporabi namesto `python3` pri vseh priloženih skriptah. Izbiro zapišita v tvoj napredek. Ne ustvarjaj dodatnih namestitev samo zaradi imena ukaza.

Če Claude orodja ne najde, v terminalu pa deluje, naj izvajalec preveri, kje je nameščeno in v katerem okolju dela Claude. Po potrebi ponovno zaženita aplikacijo.

## 2. Poveži račun za GitHub

Izvajalec ti pomaga preveriti obstoječo prijavo. Če je še ni, v terminalu zaženi:

```sh
gh auth login --hostname github.com --git-protocol https --web
```

Prijavo dokončaj v brskalniku. Pred potrditvijo poglej, kateri račun je odprt. Nato preveri:

```sh
gh api user --jq .login
```

Izpisati se mora uporabniško ime računa, ki ga želiš uporabljati. Orodje `gh` se prijavi posebej, zato prijava na spletni strani sama ne zadošča. Če imaš več računov, z izvajalcem najprej izberita pravega. [Uradna navodila za prijavo](https://cli.github.com/manual/gh_auth_login).

Da bo Git lahko poslal datoteke v tvoj zasebni repozitorij, mora imeti urejeno prijavo. Če je še nima, ti izvajalec razloži nastavitev, nato uporabi:

```sh
gh auth setup-git --hostname github.com
```

S tem Git za prijavo v GitHub uporablja orodje `gh`. Ukaz spremeni tvoje uporabniške nastavitve Gita, zato najprej preverita, kaj je že nastavljeno. [Kaj ukaz nastavi](https://cli.github.com/manual/gh_auth_setup-git).

## 3. Kloniraj gradivo

Z izvajalcem izberi mesto za mapo delavnice na svojem računalniku. Naj bo zunaj drugih Git projektov. V terminalu odpri mapo, v kateri želiš ustvariti mapo delavnice. `delavnica` naj bo novo ime mape; če že obstaja, najprej preverita vsebino.

```sh
git clone https://github.com/LukaLeskovsek/tovarna-podjemov-delavnica-ai-udelezenci.git delavnica
cd delavnica
```

S tem ustvariš klon repozitorija, ki ga boš lahko pozneje posodabljal. Na GitHubu ti ni treba ustvariti forka ali uporabiti predloge.

## 4. Odpri Clauda v pravi mapi

**Claude Desktop:** odpri **Code**, izberi okolje **Local** in obstoječo mapo `delavnica`. Delaj v tej mapi na veji `main`, brez dodatne kopije projekta (worktree). Claude naj preveri, v kateri mapi dela, saj bo tvoja osebna podmapa `moje-delo/` v tem klonu. [Navodila za izbiro okolja in mape](https://code.claude.com/docs/en/desktop).

**Terminal:** iz mape `delavnica` zaženi `claude`. Ob prvem zagonu se prijavi s svojim računom za Claude, ki omogoča uporabo Code. Uporabimo prijavo z naročnino, zato za delavnico ne nastavljamo ločenega API ključa. Če že uporabljaš službeno API okolje, ga najprej preveri z izvajalcem.

Skupaj preverita, kako ustaviš agenta in pregledaš predlagano spremembo. Za prvi preizkus izberi način, v katerem vidiš in potrjuješ spremembe. Nato v **pogovor s Claudom** kopiraj:

> Danes pripravljava okolje za delavnico. Preberi CLAUDE.md in docs/setup.md. Preveri, ali delaš v pravi lokalni mapi na veji main, ali orodja delujejo in kateri uporabnik je prijavljen v GitHub. Nato mi pomagaj urediti zasebno shranjevanje in narediti kratek preizkus z izmišljenimi podatki. Povej, kaj boš ustvaril ali spremenil. Prijavim se sam. Sprašuj me po eno stvar.

## 5. Uredi zasebno shranjevanje

Claude sledi [postopku za Git in napredek](git-in-napredek.md). Pomaga ti ustvariti samostojni repozitorij `moje-delo/`, izbrati ime za svoj zasebni repozitorij na GitHubu ter preveriti, ali pripada tebi in je res zaseben. Primer imena je `tp-ai-moje-delo`.

Preden nadaljuješ, naj ti pokaže:

- javno mapo `delavnica/` in ločeno osebno mapo `delavnica/moje-delo/`;
- prijavljenega uporabnika in njegov zasebni repozitorij na GitHubu;
- ime in e-poštni naslov, ki bosta zapisana ob shranjenih spremembah;
- kam shraniš pregledane rezultate in kam izvorne podatke.

Izbrane in pregledane rezultate shranjuješ v `moje-delo/rezultati/`, napredek v `moje-delo/napredek.md`. Izvorni podatki v `moje-delo/zasebno/` niso vključeni v varnostno kopijo na GitHubu. Izvajalec ne dobi dostopa do tvojega zasebnega repozitorija samodejno. Za službene podatke uporabi shrambo, ki jo dovoljuje tvoje podjetje.

## 6. Naredi majhno nalogo, shrani in nadaljuj

Izberi svojo majhno nalogo ali vpiši:

> Iz tega izmišljenega sporočila pripravi kratek odgovor: »Delavnica je v četrtek ob 9.00. Prinesi prenosnik in polnilec. Lokacijo še potrdimo.« Odgovor naj potrdi uro in opremo ter vpraša za lokacijo. Shrani ga v moje-delo/rezultati/setup-preizkus.md. Ničesar ne pošiljaj. Nato me prosi, naj preverim tri podatke.

Odpri rezultat in preveri uro, opremo ter neznano lokacijo. Nato napiši:

> Posodobi moj napredek in shrani to srečanje. V moj zasebni repozitorij shrani samo pregledani napredek in ta rezultat. Najprej pokaži izbrane datoteke in spremembe.

Claude shrani trenutno različico tvojega dela in jo označi, na primer s `session-01`. Tako označeni različici rečemo checkpoint. Odpri svoj repozitorij na GitHubu: preveri oznako **Private**, datoteki in checkpoint. Ob prvem shranjevanju je pričakovan tudi `.gitignore`. Če pošiljanje ne uspe, je rezultat **»Shranjeno lokalno, ni varnostno kopirano.«** Po odpravi težave ponovita pošiljanje istega checkpointa.

Zapri pogovor, odpri novega v isti mapi in napiši **»Preberi moj napredek in nadaljuj.«** Claude mora najti shranjeni rezultat in naslednje dejanje. Nato poskusi še **»Posodobi gradiva.«** Tvoj rezultat mora po posodobitvi ostati na mestu.

## 7. Preveri, ali je vse pripravljeno

- [ ] V svojem računu uporabljam Claude Code in znam odpreti pravo lokalno mapo.
- [ ] Claude iz te seje vidi Git, `gh` in ustrezen Python.
- [ ] Znam pokazati svoj GitHub račun in ločeni zasebni repozitorij.
- [ ] Prvi rezultat sem odprl in pregledal.
- [ ] Shranjene datoteke in njihovo oznako vidim v svojem zasebnem repozitoriju na GitHubu.
- [ ] V novem pogovoru znam nadaljevati iz napredka.
- [ ] Posodobitev gradiv je uspela in osebno delo je ostalo na mestu.

Če kaj manjka, v napredek zapišita: **kaj manjka, kdo uredi in kaj preverimo naslednjič**. Samo lokalno shranjena datoteka še nima varnostne kopije na GitHubu.

## Druge storitve

Za prvi korak dodatni CRM, avtomatizacijski servis ali API ključ niso potrebni. Če pri svoji nalogi potrebuješ Microsoft 365 ali drugo storitev, pripravi svoj račun in preveri, ali ga smeš uporabiti za to delo. Z izvajalcem izberita povezavo, preverita dovoljenja in naredita majhen preizkus v tvojem računu. Pred nakupom, povezovanjem ali objavo naj bo jasno, kaj potrjuješ. Nato preverita, ali povezava tudi deluje.

Namestitve in prijava: uradni viri preverjeni **20. 9. 2026**. Če se prikaz razlikuje, z izvajalcem odpri povezani aktualni vir.

[Začetek](../README.md) · [Računi in dostopi](racuni-in-dostopi.md) · [Shranjevanje in posodobitve](git-in-napredek.md)
