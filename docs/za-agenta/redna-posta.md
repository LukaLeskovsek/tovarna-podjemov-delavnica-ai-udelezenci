# Za Claude: lokalna rutina in omejeno spremljanje

Uporabi preizkušeno osebno metodo in [pravila za pošto](e-posta.md). Nastavitev opravi šele ob udeleženčevi zahtevi. Navodilo v gradivu samo ne vklopi rutine.

## Dnevna rutina

1. Preveri trenutno podprte možnosti v [Claude Desktop](https://code.claude.com/docs/en/desktop-scheduled-tasks). V Routines izberi Local, prvotno mapo delavnice in brez worktree izolacije, da vidiš isti zasebni zapis.
2. Pred zagonom določi uro, časovni pas, obdobje pošte, konec oziroma pregled uporabe, porabo in način obvestila. V novih sejah izrecno preberi osebno metodo in lokalna pravila. Ne zanašaj se na zgodovino pogovora.
3. Preveri račun in bralna orodja v dejanski seji rutine. Odobri le potrebna branja; ne vključuj pisanja v predal. Orodje z obvezno potrditvijo ob vsakem klicu lahko onemogoči nenadzorovano delo. To je omejitev, ne razlog za izklop vseh zaščit.
4. Izvedi Run now, nato še eno dejansko izvedbo ob dogovorjenem terminu. Shrani ID oziroma povezavo izvedbe, dejanski čas, obseg, rezultat in opaženo obvestilo. Računalnik mora biti buden in aplikacija odprta.
5. Pri zamujenem terminu preveri dejanski čas. Izvedi en svež pregled dogovorjenega obdobja; ne simuliraj vseh zamujenih dni. Če je izven dogovorjenega časa uporabe, ga preskoči z razlogom. Vedno loči načrtovani in dejanski zagon.
6. Pri napaki ohrani prejšnji uspešni rezultat z njegovim prvotnim časom. Napako zabeleži ločeno in jasno sporoči, da svež pregled ni uspel. Preveri Paused in ponovni ročni zagon.

## Omejeno spremljanje

V odprti lokalni seji preveri razpoložljivost /loop oziroma podprtega sejnega razporejanja. Če te možnosti ni, izvedi ročni ponovni pregled in tako označi omejitev. Ne nadomeščaj ga tiho z neomejenim procesom, sistemskim cron opravilom ali oddaljeno avtomatizacijo.

Dogovor zapiši v lokalno `spremljanje.json`: ponudnik in račun, ID niti, pričakovana oseba/dogodek, izhodiščna sporočila, interval, rok čakanja, končni čas spremljanja, status, zadnje uspešno preverjanje, opaženi dogodki in že poslana obvestila. Poverilnice ostanejo v povezovalniku. Roke hrani s časovnim pasom. Pred prvim preverjanjem samo vzpostavi izhodišče; že obstoječa sporočila niso novi dogodki.

En spremljevalnik zapisuje to stanje. Pred ponovnim zagonom preveri obstoječo sejo in njen urnik; podvojeni zagon zavrni ali najprej ustavi prejšnjega. Dnevni pregled stanje samo bere. Če lastništva ni mogoče preveriti, ostani pri ročnem poskusu.

Pri vsakem preverjanju:

- Preberi svežo nit in primerjaj dejanske ID-je sporočil. Enaka zadeva ni dokaz iste niti. Dogodek prepoznaj po niti, sporočilu in dogovorjenem pomenu.
- Lasten odgovor ne izpolni pričakovanja »odgovor druge osebe«. Če spremeni dogovor, predlagaj nov status in počakaj na poslovno odločitev.
- Pri delnem branju ali napaki ne premakni izhodišča oziroma časa uspešne osvežitve. Obvesti o novi težavi, nato ostani tih do spremembe napake ali obnovitve dostopa.
- Ob dogovorjenem dogodku ali izteku roka zapiši en trajni dogodek in prikaži eno obvestilo. Označi uspešno prikazano obvestilo; če je bila seja prekinjena med zapisom in obvestilom, ob nadaljevanju pokaži »dostava ni potrjena« in preveri dnevnik, namesto da trdiš zagotovljeno dostavo ali ga slepo ponoviš.
- Privzeto ustavi ob izpolnjenem pričakovanju, roku ali dogovorjenem koncu. Uporabnik lahko določi drugače. Prekliči urnik, preveri odsotnost aktivnega zagona in zapiši ustavitev.

Ob prekinitvi seje ne obljubljaj delovanja v ozadju. Ob nadaljevanju preveri obstoječi urnik, trajno stanje in ali je dogovor še veljaven. Brez lokalnega stanja na novi napravi ne nadaljuj samodejno.

## Dokaz in prenos

Potrebujemo dejanski zagon, dogodek, pregledan rezultat, preizkus podvajanja, izpad in ustavitev. Izmišljeni test preveri pravila, ne dostopa do storitve. Posnetek ali rezervni rezultat jasno označi. Povezava s telefonom ne spremeni mesta izvajanja.

Za skupni proces nadaljuj v [8. koraku](../../koraki/08-skupni-proces.md): n8n Cloud, Instance-level MCP in povezovalnik v Claudu. Lokalnega JSON stanja ne obljubljaj kot samodejno dosegljivega oblaku; selitev zahteva nov dogovor o trajni shrambi, dostopih in lastniku.
