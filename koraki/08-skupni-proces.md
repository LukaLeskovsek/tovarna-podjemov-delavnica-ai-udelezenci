# 8. Uredi skupni postopek

## Povezava s prvim primerom

Osebni pregled lahko nadgradiš v skupni postopek samo, če imaš dejansko skupno nalogo, dovoljenja in odgovorno osebo. V n8n Cloud preveri predajo, odobritev, zavrnitev in ponovitev; osebne lokalne mape niso samodejno dostopne oblaku.

## Pet vprašanj pri tej nalogi

S [petimi vprašanji](../docs/razclenitev-naloge.md) ponovno preglej celoten postopek. S sodelavci se dogovori, kdo prevzame naslednji korak, katere podatke potrebuje in kaj sme narediti. Preveri, ali je rezultat res prejel, ter preizkusi zavrnitev in ponovitev.

## Kaj bomo nadgradili

Imaš preverjen posamezni postopek in znaš prepoznati izjemo. Določi druge ljudi, odgovornost, skupno stanje in predaje. Uporabi n8n Cloud, Instance-level MCP in povezovalnik v Claudu. Preveri tudi zavrnitev, spremembo in ponovitev.

Izberi resnični postopek, v katerem si več ljudi predaja delo ali mora nekdo pregledati predlog. Najprej s sodelavci poenostavi korake in razjasni odgovornost. Nato poveži izbrani del postopka.

## Kaj potrebuješ

Svoj opis naloge, dovoljeni vhod, sodelujoče osebe in eno dejanje, katerega rezultat lahko preveriš. Pred tem sklopom pripravi svoj **n8n Cloud** in povezovalnik po [navodilu za n8n](../integrations/n8n/README.md). Dodatnih računov ne potrebuješ že na prvem srečanju.

## Kaj napišeš Claudu

> Uporabi moj opis naloge in operate-workflow. Najprej preveri moj n8n Cloud in povezovalnik v lokalnem zavihku Code. Pomagaj mi pripraviti majhen potek za moje delo: podatki, predlog, pregled, odločitev, dovoljeno dejanje in zapis izida. Vprašaj po eno manjkajočo odločitev. Pokaži konkretno vsebino pred zunanjim dejanjem in upoštevaj že dogovorjeno dovoljenje.

## Tvoje odločitve

S sodelavci določi odgovorno osebo pri vsakem koraku, kdo sme odobriti dejanje, kaj točno odobri in kaj se zgodi ob zavrnitvi, spremembi ali prekinitvi. Dogovorite se tudi, koliko časa odobritev velja in kdo skrbi za nadaljnje delovanje.

## Delo na svoji nalogi

1. Opiši sedanji postopek in s sodelavci odstrani nepotrebne korake. Izberi en uporaben del, ki ga lahko izvedete do konca.
2. Claude preveri povezavo v **n8n Cloud**, potrebna orodja, prijavljeni račun in dostop do izbranega poteka. Sledi [podrobnim navodilom](../integrations/n8n/za-agenta.md).
3. S Claudom pripravi potek na podatkih, ki jih smeš uporabiti. Določi, kje se trajno beleži opravljeno delo in kako povežeš predlog, odobreno različico ter izvedeno dejanje.
4. Preizkusi odobritev in zavrnitev. Ob spremembi vsebine je potreben nov pregled. Preveri napačen račun ali manjkajoči dostop ter potek veljavnosti odobritve, kadar sta pomembna za tvoj postopek.
5. Ponovi obdelavo istih podatkov in preveri, da se že končano dejanje v drugi storitvi ne ponovi. Če izid ni jasen, najprej preveri stanje v ciljni storitvi.
6. Preglej dnevnik n8n in rezultat v ciljni storitvi. Dogovori se, kdo odpravi napako in kako ustavi nadaljnje zagone.

## Prikaz in dodatne možnosti

**Prikaz v živo:** izvajalec pokaže svoj izbrani dejanski postopek v n8n Cloud. Poglej, kje pri tvojem delu sodelavci prevzemajo nalogo ali sprejemajo odločitev.

**Neobvezna vaja:** pripravljena simulirana poteka sta v [dodatni vaji](../integrations/n8n/neobvezna-vaja.md). Njun uvoz ni pogoj za lastno delo in ne potrjuje delovanja tvojih povezav.

**Dodatno samostojno delo:** razširi svoj potek. Cloudflare Workflows ostane dodatna možnost za kodirano izvedbo, kadar obstaja konkretna potreba in odgovorna oseba za vzdrževanje.

## Preveri in shrani

V napredek zapiši uporabljeni račun brez skrivnosti, ID izvedbe, rezultat, preverjeno zavrnitev oziroma ponovitev in odprta vprašanja. Po potrebi dodaj pregled poteka, konfiguracijo brez poverilnic in kratka navodila za uporabo. Z verify-workflow preveri dejanski izid. Narisani načrt in delujoča povezava sta različna dosežka.

<!-- package-navigation:start -->
[7. Redna opravila in naprave](07-rutina-in-naprave.md) · [9. Preizkus, predaja in ekipe agentov](09-preizkusi-in-predaja.md) · [Vsa objavljena gradiva](../docs/objavljena-gradiva.md)
<!-- package-navigation:end -->
