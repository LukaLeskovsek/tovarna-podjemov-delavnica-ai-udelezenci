# Petek: pripravi svojo interno aplikacijo

Na srečanju 16. oktobra bomo iz preverjene naloge naredili en uporaben del aplikacije. Vodeni del traja približno 75 minut, nato gradiš svojo rešitev. Cilj je prijava, uporabna funkcija, shranjeni podatki in preverjen dostop. Spletna objava je naslednji korak za tiste, ki pridejo do nje.

## Kaj že prinese starter

[Internal OS Starter](https://github.com/LukaLeskovsek/internal-os-starter) vsebuje osnovo za prijavo, podatkovno bazo, uporabniške pravice in module. Modul je del aplikacije za določeno delo, na primer pregled odprtih zadev. Claude sledi navodilom starterja in pomaga zgraditi tvojo funkcijo.

Aplikacija je smiselna, ko preizkus pokaže, da potrebuješ pravice, podatkovno ureditev ali povezave, ki jih obstoječa rešitev ne omogoča na zahtevan način. Če dokument ali Artifact zadošča, ga lahko še naprej uporabljaš.

## Pred srečanjem

Pripravi opis ene naloge, dovoljen primer in merilo, po katerem boš preveril rezultat. Uporabi svoj GitHub in Supabase račun. Claude pripravi ločeno zasebno kopijo aplikacije, preveri podporna orodja in pomaga nastaviti podatkovno bazo. Uporabniških ključev ne lepi v pogovor.

Mapa aplikacije je ob mapi delavnice, ne znotraj javnih učnih gradiv ali njihovega moje-delo/. Osebni profil ostane na preverjenem mestu. Povezavo z njim uredi Claude; ni treba ponovno odgovarjati na isti intervju. Pred javnim gostovanjem posebej preveri dostop. Zasebni GitHub sam ne omeji dostopa do spletne aplikacije.

V skupnem prikazu lahko aplikacija uporablja istega agenta v n8n s Claude prek Anthropic API. Ta povezava je ločena od AI v aplikaciji. Lokalni starter privzeto uporablja preverjeno naročniško prijavo Claude; ob napaki ne preklopi na API. Za AI v objavljeni aplikaciji posebej pripravimo OpenRouter, ključ z omejitvijo porabe in preverjeni model. Aplikacija za ekipo lahko deluje tudi brez AI. Vercel potrebuješ, ko se odločiš za spletno objavo. Resend, Sentry in Intrix niso pogoji za prvo lokalno funkcijo.

## Začni v mapi delavnice

> Preberi moj napredek in relevantni profil. Uporabi graduate-artifact ter mi pomagaj izbrati eno uporabno funkcijo za interno aplikacijo. Zapiši, kdo jo uporablja, katere podatke potrebuje, kaj mora shraniti in kako bova preverila dostop ter rezultat. Uporabi že sprejete odločitve. Pripravi kratko predajo za Internal OS Starter, brez poverilnic ali resnične pošte.

Nato odpri mapo svoje aplikacije v Code in napiši:

> Preberi CLAUDE.md in mojo predajo. Preveri, kje je moj osebni profil, ter uporabi pravila za izbrano podjetje. S postopkom /plan pripravi načrt ene uporabne funkcije. Uporabi že dogovorjene odgovore. Pred gradnjo mi pokaži rezultat, podatke in preverjanja. Ne objavljaj aplikacije.

Po pregledu načrta:

> Izvedi dogovorjeno prvo funkcijo s /build. Nato uporabi /verify: preveri shranjevanje, ponovno odpiranje ter dostop drugega uporabnika. Jasno loči lokalni preizkus od delovanja v povezanih storitvah. Povej mi, kaj še manjka.

## Skupni prikaz: aplikacija Ponudbe

Nadaljujemo [ponedeljkovo pripravo ponudbe](povprasevanje-ponudba.md). Pripravimo seznam in podrobnosti povpraševanj Good Brew: agentovo priporočilo z razlogom, vire, izračun, odprta vprašanja, popravek in shranjeno odločitev. Uporabnik dopolni podatke in zahteva novo pripravo. Za prvo lokalno funkcijo lahko uporabimo jasno označen shranjeni osnutek. Po osvežitvi mora sprememba ostati. Preverimo, kdo sme videti posamezno ponudbo in kdo jo lahko potrdi.

Sprememba obsega ali postavke potrebuje nov izračun ter pregled. Če izračun še ni povezan, je predlog označen kot nepopoln in ga ne potrdimo. »Odobreno«, »dokument izdelan« in »poslano« so različna stanja.

Supabase iz ponedeljkovega prikaza ostane glavno mesto za poslovno stanje. Aplikacija bere iste zapise in odločitve. Povezavo z n8n dodamo, ko osnovna funkcija deluje, ter preverimo dostop med storitvama. n8n izvede samo veljavno odobreno različico in vrne dejanski izid. Pošiljanje ponudbe stranki je ločena odločitev.

## Delo na svoji nalogi

1. Izberi eno funkcijo in en običajen primer. Celotnega informacijskega sistema ne načrtuj za prvi poskus.
2. S Claudom preglej načrt. Povej mu, kateri rezultat boš preveril.
3. Zgradi funkcijo in jo uporabi od začetka do konca.
4. Osveži stran, odpri shranjen zapis ter poskusi še napačen ali nepopoln podatek.
5. Z drugim testnim uporabnikom preveri dostop do modula in do posameznih zapisov. Skrit gumb ni dovolj.
6. Shrani kodo in pregledano navodilo v svojo zasebno kopijo aplikacije. V napredek delavnice zapiši lokacijo, preverjeni rezultat in naslednji korak.

Za objavo uporabi /ship šele, ko jo želiš in so preverjanja uspešna. Predhodno preveri tudi morebitno samodejno objavo ob pushu. Če računi še niso pripravljeni, dokončaj zasnovo; ne označi je kot delujočo aplikacijo.

## Najprej preveri, ali Artifact zadošča

Artifacts v podprtih paketih že omogočajo povezovalnike ter osebno ali skupno shrambo. Pri [izboru zahtev](../gradiva/interaktivno/od-artifakta-do-aplikacije.html) zato najprej preizkusi dejansko omejitev. Lastna aplikacija je smiselna, ko potrebuješ drugačne pravice, nadzor nad podatki ali vključitev v svoje sisteme. [Razlaga in aktualni viri](izbira-orodja.md).

## Od lokalnega razvoja do uporabe v ekipi

Odpri [interaktivni diagram](../gradiva/interaktivno/od-artifakta-do-sistema.html). Primerja Artifact, lokalno aplikacijo, aplikacijo za ekipo in neobvezni n8n. Izklop računalnika v shemi pokaže, kaj se ustavi. Izbor vloge je ponazoritev; ne prijavi uporabnika in ne potrdi dejanskih pravic.

**Vercel** je storitev, kjer aplikacija teče in jo sodelavci odprejo v brskalniku. **Supabase** ureja prijavo ter hrani podatke in datoteke. `localhost:3000` pomeni, da aplikacija teče na tvojem računalniku; Supabase je lahko že takrat v oblaku. Javni naslov aplikacije ne pomeni javnih poslovnih podatkov.

Claude, s katerim razvijaš kodo, in AI, ki ga aplikacija uporablja pri poslovni nalogi, imata različni vlogi. Lokalni AI v starterju preveri naročniško prijavo in uporablja model pri ponudniku. Omejitve paketa in dodatno plačljive dobropise preveri v svojem računu. Na Vercelu tega lokalnega načina ne uporabljamo.

Pred vklopom OpenRouterja pripravi namenski ključ z denarno omejitvijo in brez samodejnega polnjenja. Aplikacija ima tudi dnevni limit klicev. Ob izčrpanem proračunu se zahteva ustavi; omejitev ni povabilo k ponavljanju. V izračunu »Ali se nam splača?« upoštevaj pregled in popravke, vse klice AI, gostovanje ter vzdrževanje. Ne prištej prihranka samo zato, ker je predlog nastal hitro.

[Prijava v Claude](https://code.claude.com/docs/en/authentication) · [Poraba naročnine](https://code.claude.com/docs/en/costs) · [Omejitve OpenRouterja](https://openrouter.ai/docs/api/reference/limits) · [Poraba na Vercelu](https://vercel.com/docs/spend-management)

## Dodajanje sodelavcev

V Supabase odpri **Authentication → Sign In / Providers** in izklopi **Allow new users to sign up**. Obstoječi računi ostanejo uporabni, novi uporabniki pa se ne morejo sami registrirati.

**Confirm Email lahko ostane vklopljen.** V Internal OS lastnik odpre **Administracija → Uporabniki → Dodaj osebo**, ustvari račun z začasnim geslom in določi dostopna orodja. Modul uporabnika ustvari kot že potrjenega; ne pošlje e-poštnega povabila. Zahteva nastavljen skrivni strežniški ključ za upravljanje uporabnikov.

Claude lahko pomaga pri dodajanju samo z urejenim skrbniškim dostopom in jasnim pooblastilom. Gesel in enkratnih povezav ne pošiljaj v pogovor; osebi jih predaj po varni poti. Nato preveri prijavo ter dostop do modulov in posameznih zapisov. Izklop registracije sam po sebi ne določi teh pravic.

[Supabase: nastavitve registracije in potrjevanja e-naslova](https://supabase.com/docs/guides/auth/general-configuration).
