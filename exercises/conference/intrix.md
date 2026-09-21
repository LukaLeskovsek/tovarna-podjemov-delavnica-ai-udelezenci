# Kako se podatki iz vaje povežejo z Intrixom

Na delavnici za skupni CRM primer uporabljamo **Intrix**. Najprej iz desetih vrstic pripravimo predlog. Za ta del ne potrebuješ prijave v CRM. Ko bomo vadili vnos, bo vsak uporabljal svojo prijavo v dogovorjeno vadbeno okolje.

Spodnja imena polj so bila preverjena v Intrixu izvajalca 21. 9. 2026. V drugem okolju so lahko obrazci prilagojeni. Imena stolpcev v naši preglednici so oznake učnih podatkov; datoteka ni pripravljena za neposreden uvoz v Intrix.

## Kam sodi posamezen podatek

| Stolpec v preglednici | Polje ali mesto v Intrixu | Kaj preveriš pri predlogu |
|---|---|---|
| `company` | **Podjetja → Naziv**; pri kontaktu povezava **Podjetje** | Najprej poišči podjetje. Kontakt poveži z izbranim zapisom, ne samo z njegovim imenom. |
| `company_website` | **Podjetja → Spletna stran** | Za primerjavo uporabi domeno, v predlogu pa ohrani celotni spletni naslov. Skupna domena še ne dokazuje, da gre za isto podjetje. |
| `contact_name` | **Kontakti → Ime** in **Priimek** | Prikaži razdelitev. Če ni jasno, kateri del je ime ali priimek, vprašaj. |
| `business_email` | **Kontakti → E-pošta** | Tu iščeš obstoječo osebo. Naslova osebe ne vpisuj med splošne podatke podjetja. |
| `role` | **Kontakti → Funkcija v podjetju** | Izbereš obstoječo vrednost iz šifranta. Če ustrezne ni, to zapiši kot odprto vprašanje; nove vrednosti ne dodajaj sam. |
| `country` | **Kontakti → Država** | Oznako, npr. `SI`, poveži z ustrezno državo na seznamu. Iz nje ne sklepaj o sedežu podjetja. |
| `assigned_salesperson` | **Kontakti → Skrbnik** | Izmišljeno osebo iz vaje je treba pred vnosom povezati z dejanskim uporabnikom. Vnaprej izbran prijavljeni uporabnik ni nujno pravi skrbnik. Skrbnika novega podjetja določimo posebej; obstoječega ne spreminjamo. |
| `conference`, `meeting_note`, `source_row_id` | **Kontakti → Ostalo → Dodatne informacije** | Za nov kontakt pripravimo besedilo z nazivom konference, izvorno vrstico in zapisom pogovora. To je naš dogovor za vajo, ne posebna vrsta zapisa v Intrixu. |
| `next_action` | Besedilo predloga v **Dodatnih informacijah** | Označi ga kot predlagani naslednji korak. Samo zaradi tega besedila ne nastane naloga ali sporočilo. |

Imena odgovornih oseb v učni datoteki so izmišljena. Za prvi osnutek jih ohrani in označi, da izbira uporabnika v Intrixu še ni potrjena. Zaradi manjkajoče prijave ali preslikave uporabnikov ne spreminjaj učnih statusov iz [pravil](rules.md).

## Kaj ostane v tvojem pregledu

Statusi `ready`, `needs_review`, `existing` in `duplicate` opisujejo naše odločitve o vrsticah. Niso Intrixovi statusi kontaktov. `ready` pomeni, da lahko pripraviš predlog; pred vnosom še vedno preverimo polja, uporabnika in konkretne zapise v izbranem okolju.

[existing-crm.json](existing-crm.json) je izmišljena primerjalna zbirka. Ni izvoz iz Intrixa. Oznake `ORG-…` in `CON-…` niso dejanski Intrixovi identifikatorji in jih ne uporabljaj za iskanje v živem okolju. V pregledu loči učni ID od pozneje preverjene povezave na pravi zapis.

Pri iskanju v Intrixu preveri filtre in vse strani rezultatov. Več zadetkov ali neujemanje podjetja zahteva pregled. Obstoječega kontakta ne prestavljaj v drugo podjetje in ne prepisuj njegovih podatkov. Pravila ujemanja iz te vaje izvaja agent; ne predpostavljaj, da jih Intrix samodejno uveljavlja.

## Zapis pogovora, sestanek in naloga

Zapis pogovora s konference bomo pri novem kontaktu dodali v **Dodatne informacije**. Iz tega ne ustvarjamo samodejno sestanka ali kampanje. Za uporabo polja **Vključen v kampanje** bi morali posebej izbrati pravo kampanjo.

**Sestanki** imajo med drugim zadevo, začetek, konec, prisotne in poročilo. **Naloge** imajo naziv, izvajalca, začetek, rok in možnost **Obvesti izvajalca (e-pošta)**. Teh odločitev učna tabela ne vsebuje. Če bomo pozneje ustvarjali naloge ali sestanke, bomo najprej dopolnili podatke in se dogovorili tudi o obvestilih.

V začetni vaji pripraviš samo pregled in predlog. Podatkov še ne shranjuješ v Intrix.

[Vaja](README.md) · [Pravila](rules.md)
