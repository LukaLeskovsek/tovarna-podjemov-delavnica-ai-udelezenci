# Dnevni pregled in spremljanje pogovora

To dodaj, ko znaš ročni pregled ponoviti in mu zaupaš. Najprej uporabljamo lokalno izvajanje v Claude Desktop.

## Dnevni pregled

> Moj način pregleda pošte je preizkušen. Pomagaj mi nastaviti lokalni dnevni pregled. Dogovoriva se za uro, časovni pas, obseg, dovoljeno porabo in rezultat. Uporabi isto delovno mapo in moja shranjena pravila. Preveri dostop v novi seji, izvedi »Run now« in nato preveriva še dejanski zagon ob dogovorjenem času. Pošte ne spreminjaj. Povej, kako opravilo ustavim.

Pregled mora uporabiti sveže podatke in pokazati čas izvedbe. Če dostop ne uspe, dobiš obvestilo o težavi, ne starega povzetka z novim datumom. Ob zagonu po zamujenem terminu jasno pove, kdaj je bil načrtovan in kateri obseg je dejansko preveril.

Računalnik mora biti buden in Claude Desktop odprt. Nastavitev urnika še ni dokaz, da se je naloga izvedla. V **Routines** preveri zgodovino, dejanski rezultat in možnost **Paused**.

## Spremljaj izbrani pogovor

> Ta pogovor želim spremljati. Najprej določiva, na čigav odgovor čakam, kakšna sprememba je pomembna, kako pogosto preverjaš in kdaj nehaš. Obvesti me ob dogovorjeni spremembi, izteku roka ali težavi z dostopom. Brez spremembe ostani tiho. Vodi lokalni zapis, da istega dogodka ne javljaš znova. Ne pošiljaj sporočil v mojem imenu.

Za prikaz uporabimo omejeno spremljanje v odprti seji. Dogovorimo se za konec tudi, če odgovor ne prispe. Lasten odgovor lahko spremeni, kaj še čakaš; ne sme šteti kot odgovor druge osebe. Pogovor lahko ustaviš tudi prej.

V samodejnem načinu izbereš le en aktiven zapisovalec stanja. Dnevni pregled bere stanje spremljanja, ne ustvarja drugega spremljevalnika. Ob ponovnem zagonu Claude najprej preveri, ali prejšnji še teče.

## Kaj preveriš

- Prispeli odgovor je res odgovor na izbrani pogovor.
- Ponovljeno preverjanje ne povzroči istega obvestila.
- Izpad povezave je viden, stanje zadnjega uspešnega branja pa se ne premakne.
- Ustavitev dejansko ustavi nadaljnja preverjanja.
- Nov pogovor najde zapis; nova naprava brez tega zapisa ne nadaljuje samodejno.

Artifact pokaže zadnji pripravljeni pregled. Odprt Artifact sam ne spremlja pošte. Oblak in skupni proces obravnavamo pozneje, ko potrebujemo delovanje neodvisno od računalnika.

[7. korak](../koraki/07-rutina-in-naprave.md) · [Podrobnosti za Claude](za-agenta/redna-posta.md) · [Uradna navodila za lokalne rutine](https://code.claude.com/docs/en/desktop-scheduled-tasks)
