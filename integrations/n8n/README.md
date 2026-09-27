# n8n Cloud za tvojo nalogo

S Claudom bomo povezali del tvojega postopka, pri katerem si podatke in odločitve predaja več korakov ali ljudi. Uporabljamo **n8n Cloud**. Lokalna namestitev in Docker nista del priprave.

## Pred tem sklopom

Pripravi svoj račun za n8n Cloud, dostop do nastavitev in dovoljeni vhod za svojo nalogo. Preveri naročnino oziroma preizkusno obdobje in dogovorjeno porabo. Računa ne potrebuješ že na prvem srečanju.

## Poveži n8n s Claudom

1. V n8n odpri **Settings → Instance-level MCP** in vklopi **Enable MCP access**. Če te možnosti nimaš, mora dostop urediti lastnik ali skrbnik okolja.
2. Izberi **Connect** oziroma **Connect a client**, nato OAuth. Kopiraj prikazani **Server URL**; konča se z `/mcp-server/http`.
3. V Claude Desktop odpri **Settings → Connectors → Add custom connector**, vnesi ime n8n in ta naslov. Prijavo in potrditev dostopa opravi sam.
4. Odpri svojo mapo delavnice v **Code → Local**. Claudu napiši spodnje navodilo.

> Preberi integrations/n8n/za-agenta.md. Preveri moj povezovalnik n8n in orodja, ki jih vidiš v tem pogovoru. Nato uporabi mojo dejansko nalogo in mi pomagaj pripraviti ter preveriti majhen potek. Najprej mi povej, katere odločitve, podatke in dovoljenja potrebujeva. Vprašaj po eno stvar.

Če n8n ponuja neposredno nastavitev povezovalnika za Claude, jo lahko uporabiš. Nato enako preverimo rezultat v Code. Naslov urejevalnika n8n ni naslov MCP strežnika.

## Delo na svoji nalogi

Izberi en uporaben del postopka. S Claudom določita vhod, predlog, pregled, odločitev, dejanje in rezultat. Prikazani primer izvajalca pomaga razumeti pristop; ni treba uvoziti njegovega poteka.

**Tvoje odločitve:** kdo sodeluje, kaj sme Claude narediti, katera vsebina potrebuje pregled in kdo skrbi za nadaljevanje.

**Preverjanje:** odpri izvedbo v n8n in preveri rezultat tudi v ciljni storitvi. Pri odobritvah preizkusi zavrnitev, spremembo in ponovitev istega vhoda. V napredek shrani izid in naslednji korak, brez prijavnih podatkov.

**Neobvezna vaja:** [simulirana poteka za pregled in odobritev](neobvezna-vaja.md).

[Skupni postopek](../../koraki/08-skupni-proces.md) · [Uradno povezovanje n8n](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples)
