# Delovna mapa in Obsidian

Claude in Obsidian uporabljata **isto mapo delavnica**. Obsidian je priročen za branje in urejanje zapisov Markdown (`.md`); nove kopije gradiv ne potrebujemo.

```text
delavnica/                  odpri v Code in Obsidianu
  README.md                 začni tukaj
  .obsidian/                nastavitve Obsidiana; zunaj Gita
  local/starter/            lokalni indeks in nastavitve; zunaj Gita
  moje-delo/                tvoja ločena zasebna shramba
    napredek.md
    skills/
    rezultati/
    zasebno/                izvorni podatki; zunaj Gita
```

## Odpri mapo

Claude preveri oziroma pomaga namestiti [Obsidian](https://obsidian.md/download). V Obsidianu izberi **Open folder as vault** oziroma možnost za odpiranje obstoječe mape. Izberi isto mapo `delavnica`, ki je odprta v Code. »Vault« je Obsidianovo ime za mapo z zapiski.

Za ta korak ne potrebuješ dodatnega računa, sinhronizacije ali vtičnikov. Claude naj preveri, da so lokalne nastavitve izključene iz skupnega Gita.

## Preizkusi na svojem zapisu

1. Odpri začetni `README.md` in sledi povezavi do prve naloge.
2. Odpri svoj `moje-delo/napredek.md` in dopiši naslednji korak.
3. Claudu naroči, naj isti zapis prebere s diska. Preveri, da vidi popravek.
4. Če Claude spremeni zapis, ga znova odpri v Obsidianu. Ne urejajta istega zapisa hkrati.

Svoje prilagoditve piši v `moje-delo/`. Skupna gradiva posodabljamo s prošnjo »Posodobi gradiva«. Če jih spremeniš, se posodobitev ustavi, dokler sprememb ne razjasnimo.

Obsidian prikazuje datoteke. [Indeks](dokumenti-in-starter.md) išče po dovoljenih dokumentih. [GitHub](git-in-napredek.md) hrani izbrano delo in njegove različice. To so ločene naloge.

[Uradna navodila za odpiranje mape](https://obsidian.md/help/vault) · [Priprava](setup.md)
