# Za Claude: preverjena povezava n8n Cloud

Glavna pot je uporabnikov **n8n Cloud**, vgrajeni **Instance-level MCP**, OAuth in povezovalnik v **Claude Desktop → Settings → Connectors**. Delaj v lokalnem zavihku Code. Ne nameščaj lokalnega n8n, Dockerja ali dodatnega neuradnega MCP posrednika.

## Povezava pred izdelavo

1. Preveri, ali si v Code Local, kateri račun oziroma okolje je uporabnik izbral in ali ima v n8n vklopljen Instance-level MCP. Vklop zahteva lastnika ali skrbnika.
2. Uporabi Server URL iz nastavitev n8n. Naslov se konča z `/mcp-server/http`; ne sestavljaj ga iz nepreverjenih podatkov. Uporabnik opravi OAuth v uradnem oknu.
3. Preveri seznam orodij v dejanski Code seji. Lokalni Desktop Code uporablja povezovalnike iz aplikacije. Če n8n že deluje, ne ustvari druge povezave z drugim imenom.
4. Če orodij ni, preveri različico aplikacije, Local, omogočen povezovalnik, organizacijsko politiko in ponovni zagon seje. Šele če to ne zadošča, uporabi dokumentirano ročno nastavitev za konkretno okolje. Ključev ne zapisuj v navodila ali javni projekt.
5. Preveri dovoljenja orodij, ki jih naloga potrebuje. Po dogovoru preberi opis izbranega poteka. Vidnost povezovalnika sama ne dokazuje pravice za ustvarjanje, spreminjanje ali zagon.

## Majhen potek iz lastne naloge

Najprej preberi napredek in udeleženčev dejanski vhod. Razjasni koristni končni rezultat in največ eno manjkajočo odločitev naenkrat. Ni obveznega uvoza `approval-lab.json` ali `human-review.json`.

Preveri aktualne MCP zmožnosti v tem računu; dokumentirane nove zmožnosti niso dokaz, da jih konkretna namestitev že podpira. Za ustvarjanje ali urejanje uporabi prisotna orodja in preveri nastali potek v n8n. Če določeno dejanje ni podprto, pripravi pregledan izvoz za uvoz v Cloud ali natančno pojasni potrebno dejanje v vmesniku; ne predstavljaj ga kot že opravljenega.

MCP je treba omogočiti tudi za izbrani potek. Preveri **Available in MCP**, zahtevano objavo in podprt sprožilec. **MCP Server Trigger** je druga možnost za izpostavljanje orodij posameznega poteka in ni pogoj za to povezavo. Ne vklapljaj samodejnega izpostavljanja vseh prihodnjih potekov brez potrebe.

Pred zagonom preveri, katero različico bo izvedel izbrani način: produkcijski zagon lahko uporablja objavljeno različico, ročni preizkus pa trenutno neobjavljeno. Tudi ročni preizkus lahko izvede zunanje dejanje. Objavo in dovoljeni obseg uskladi s konkretno nalogo; ne objavljaj aktivnega urnika ali javnega sprožilca kot skritega koraka priprave.

## Odločitev človeka in zunanji rezultat

Za vsak korak določi odgovorno osebo. Odobritev mora pripadati točni vsebini in različici predloga ter resničnemu upravičenemu uporabniku. Povezava na obrazec sama ne dokazuje identitete. Določi veljavnost odobritve in odziv na neodgovor.

Stanje izvedbe in ključ, ki prepreči ponovitev istega dejanja, hranita trajno v izbrani storitvi. Ne zaupaj javno poslanemu polju »že izvedeno«. Pri spremembi predloga prejšnja odobritev ne velja.

Pokaži konkreten predlog pred zunanjim dejanjem in upoštevaj že dogovorjeno pooblastilo. Preveri odobritev, zavrnitev, spremembo, ponovitev in prekinitev; iztek in napačno identiteto, kadar se uporabljata. Če se izid izgubi ali ni jasen, najprej preberi cilj in dnevnik. Ne ponavljaj dejanja na slepo.

## Preverjanje in shranjevanje

Preveri ID izvedbe, uporabljeno različico, stanje v dnevniku n8n ter zapis oziroma datoteko v ciljni storitvi. Rezultat odpri z vidika uporabnika. Za preprečevanje podvojitve ponovi isti vhod in preveri število zapisov na cilju.

V napredek shrani opaženi izid, povezavo oziroma ID brez poverilnic, omejitve in naslednji korak. Konfiguracijo izvozi brez prijavnih podatkov; pred shranjevanjem preglej tudi pripete podatke vozlišč in zasebne URL-je. Zapiši, kdo vzdržuje potek, kako ga ustavi in kdo krije porabo.

Ob nedelujoči povezavi nadaljuj z opisom in dovoljenim lokalnim delom ali uporabi neobvezno vajo po izbiri udeleženca. To stanje označi kot nepreverjeno v n8n Cloud.

## Viri in stanje navodil

Dokumentacija preverjena 27. 9. 2026. To ni potrdilo živega priklopa v računu udeleženca.

- [n8n MCP in dovoljenja](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)
- [n8n: povezave za Claude](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples)
- [Claude Desktop: povezovalniki](https://code.claude.com/docs/en/desktop#connect-external-tools)
