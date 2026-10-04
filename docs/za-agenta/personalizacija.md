# Za Claude: skupni osebni in poslovni profil

Po pripravi klona, podpornih orodij in zasebnega dela preberi [delavnica-personalizacija](../../.claude/skills/delavnica-personalizacija/SKILL.md). Izvedi jo pred prvo vsebinsko nalogo. Indeks in dodatne povezave niso pogoj za intervju.

## Branje pri vsaki nalogi

1. Preberi `moje-delo/rezultati/profil/PERSON.md` in `INDEX.md` oziroma preverjene poti iz globalnega povezovalnega bloka. Preberi napredek in že znane odgovore.
2. Poslovni kontekst določi po potrjeni povezavi trenutne mape v kazalu ali izrecni izbiri uporabnika. Ne sklepaj iz zadnjega uporabljenega podjetja. Ob nejasnosti vprašaj po eni izbiri. Upoštevaj, ali povezava velja tudi za podmape; bolj specifična potrjena mapa ima prednost, nasprotje pa razjasni.
3. Preberi relevantne COMPANY.md, BRAND.md in PRIMERI.md. Profil daje kontekst, ne dokazov za spremenljive trditve ali novih dovoljenj. Če podatki manjkajo, povej omejitev in nadaljuj z znanim delom.

## Globalna povezava za Code

Globalni `~/.claude/CLAUDE.md` omogoča uvoze z `@pot`. Pomočnik [povezi_profil.py](../../.claude/skills/delavnica-personalizacija/scripts/povezi_profil.py) doda označeni blok z uvozoma PERSON.md in INDEX.md ter navodilom za izbiro podjetja. Absolutne poti pripravi na dejanski napravi; presledke ubeži. Ne kopiraj poti izvajalca.

Pred spremembo povej, da velja za vse Code projekte uporabnika. Preveri obstoječa navodila in morebitna nasprotja. Ohrani AIOS, osebni starter, druge zbirke in urnike. Spreminjaš samo označeni blok. Na skupnem uporabniškem računu računalnika globalne povezave ne vzpostavi pred ureditvijo zasebnega okolja.

Iz korena klona, s preverjenim Pythonovim ukazom:

```sh
python .claude/skills/delavnica-personalizacija/scripts/povezi_profil.py pregled
python .claude/skills/delavnica-personalizacija/scripts/povezi_profil.py povezi
```

`pregled` ne piše. `povezi` preveri točen notranji Gitov koren in zunanje izključevanje, pred spremembo obstoječe datoteke naredi zasebno kopijo ter ohrani vso vsebino zunaj označenega bloka. Prijavo, lastništvo in zasebnost cilja preveri po [postopku shranjevanja](shranjevanje.md). Simbolno povezano globalno datoteko pomočnik zavrne; ne zamenjaj je na slepo.

V novem pogovoru preveri naložena navodila in dejanski rezultat. Preveri, ali Claude navodila pri rezultatu upošteva. Za drugo podjetje preveri pravilno izbiro konteksta. Globalnega bloka ne shranjuj v osebni GitHub z absolutnimi potmi ali kopijo vseh drugih globalnih navodil.

Uradni opis: [Claude Code memory in uvozi](https://code.claude.com/docs/en/memory).

## Nadaljevanje, selitev in popravki

Ob prekinitvi uporabi stanje v INDEX.md. Stara osebna navodila preberi kot vhod in po selitvi označi, da je profil edino aktualno mesto za dogovore. Ne prepisuj starih zapisov ali osebnih veščin brez potrebe.

Pri selitvi preveri dejansko lokacijo profila, popravi potrjene povezave map v kazalu in ponovno izvedi pregled ter povezavo. Dovoljeno lokalno gradivo in občutljivi primeri se ne obnovijo iz GitHuba; manjkajoče vire označi.

Jasen trajnejši popravek shrani v ustrezni profil, izjemo v zapis naloge, primer z razlogom v PRIMERI.md. Pri nejasni posplošitvi ali nasprotju vprašaj. Na novem primeru preveri, ali Claude dogovor upošteva. Druge podporne veščine uporabljajo isto zbirko; poslovnih dejstev ne podvajaj v njihovih navodilih.

Za Chat in Cowork pripravi ZA-CHAT-COWORK.md z osebnimi preferencami. Uporabnik vnese ali priloži dovoljen povzetek in posebej izbere podjetje. Preveri uporabo v dejanskem načinu; ne trdi, da globalni Code uvoz velja povsod.
