import json

input_dict = [
    {
        "category": "polevky",
        "imgsource": "image-5e7f9d82abf36.jpg",
        "title_dia": "Hovězí vývar s masem a nudlemi",
    },
    {
        "category": "polevky",
        "imgsource": "image-5e81d9515faf2.jpg",
        "title_dia": "Kulajda",
    },
    {
        "category": "polevky",
        "imgsource": "image-5f00448c4aa99.jpg",
        "title_dia": "Gulášová",
    },
    {
        "category": "polevky",
        "imgsource": "image-5ea3ef41292da.jpg",
        "title_dia": "Boršč",
    },
    {
        "category": "polevky",
        "imgsource": "image-5eba656baaace.jpg",
        "title_dia": "Frankfurtská",
    },
    {
        "category": "polevky",
        "imgsource": "image-5ece47d918a12.jpg",
        "title_dia": "Zelná s uzeninou",
    },
    {
        "category": "polevky",
        "imgsource": "image-5e7f71415405c.jpg",
        "title_dia": "Čočková",
    },
    {
        "category": "polevky",
        "imgsource": "image-5e98a24cf290f.jpg",
        "title_dia": "Fazolová",
    },
    {
        "category": "polevky",
        "imgsource": "image-5f8431da214c7.jpg",
        "title_dia": "Krupicová s vejcem",
    },
    {
        "category": "polevky",
        "imgsource": "image-5e948825b3d7c.jpg",
        "title_dia": "Rajská s rýží",
    },
    {
        "category": "polevky",
        "imgsource": "image-5e9051c2f069c.jpg",
        "title_dia": "Bramborová",
    },
    {
        "category": "polevky",
        "imgsource": "image-5ec63ce1a9ca8.jpg",
        "title_dia": "Zeleninová",
    },
    {
        "category": "polevky",
        "imgsource": "image-5eb1e050b69a1.jpg",
        "title_dia": "Pórková s vejcem",
    },
    {
        "category": "polevky",
        "imgsource": "image-5f3e2a8a256e0.jpg",
        "title_dia": "Květáková",
    },
    {
        "category": "polevky",
        "imgsource": "image-5f00438d856c4.jpg",
        "title_dia": "Brokolicová",
    },
    {
        "category": "polevky",
        "imgsource": "image-609a3b60be916.jpg",
        "title_dia": "Česneková polévka s bramborami",
    },
    {
        "category": "polevky",
        "imgsource": "image-5f01961398152.jpg",
        "title_dia": "Hrachová se smaženým hráškem",
    },
    {
        "category": "polevky",
        "imgsource": "image-5fa5490109745.jpg",
        "title_dia": "Dršťková",
    },
    {
        "category": "polevky",
        "imgsource": "image-5e80fcbacb9e5.jpg",
        "title_dia": "Drůbeží vývar s masem a nudlemi",
    },
    {
        "category": "polevky",
        "imgsource": "image-5eb1dfc02b39b.jpg",
        "title_dia": "Hovězí vývar s játrovými knedlíčky",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607ff9e93c2b4.jpg",
        "title_dia": "Staročeské pečené koleno, hořčice, křen, kyselá okurka, chléb / 900g v syrovém stavu",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d8fabaa96a.jpg",
        "title_dia": "Pečené vepřové koleno na černém pivu, hořčice, křen, zelný salát, chléb",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ee6186b90db3.jpg",
        "title_dia": "Pečené kachní stehno, bílé zelí, bramborový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ee61870e4fe4.jpg",
        "title_dia": "Pečené kachní stehno, bílé zelí, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-608c77acc85a3.jpg",
        "title_dia": "Vepřová marinovaná žebra, chléb 3ks plátek",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e85806b107b0.jpg",
        "title_dia": "Svíčková na smetaně, hovězí maso zadní, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d7501bbf38.jpg",
        "title_dia": "Hovězí na česneku, špenát, bramborový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c8db43dbe1.jpg",
        "title_dia": "Hovězí na česneku, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c8c2735f44.jpg",
        "title_dia": "Hovězí na česneku, vařená rýže",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c8c1da8c81.jpg",
        "title_dia": "Hovězí na česneku, bramborový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c8c43367de.jpg",
        "title_dia": "Hovězí na česneku, vařený brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c8c4d09514.jpg",
        "title_dia": "Hovězí na česneku, těstoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-633e8fc6a16bf.jpg",
        "title_dia": "Moravský vrabec, dušené zelí, bramborový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-633e8ffc5e732.jpg",
        "title_dia": "Moravský vrabec, dušené zelí, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-633e90a8bccd2.jpg",
        "title_dia": "Moravský vrabec, špenát, bramborový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-633e90cb4a2ca.jpg",
        "title_dia": "Moravský vrabec, špenát, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-61dedd472998b.jpg",
        "title_dia": "Plzeňský guláš, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-61dedd522a807.jpg",
        "title_dia": "Plzeňský guláš, bramborový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-61dedd5da39d0.jpg",
        "title_dia": "Plzeňský guláš, vařená rýže",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-61dedd7027379.jpg",
        "title_dia": "Plzeňský guláš, vařený brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-61dedd81bf07e.jpg",
        "title_dia": "Plzeňský guláš, těstoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e8580b5eb8b6.jpg",
        "title_dia": "Hovězí guláš, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d80e01a32b.jpg",
        "title_dia": "Hovězí guláš, bramborový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec41873a7146.jpg",
        "title_dia": "Hovězí guláš, vařená rýže",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec63f5ddd749.jpg",
        "title_dia": "Hovězí guláš, vařený brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f3389fd6cbf9.jpg",
        "title_dia": "Hovězí guláš, těstoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e7f503bbef30.jpg",
        "title_dia": "Maďarský guláš, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d81cf94da6.jpg",
        "title_dia": "Maďarský guláš, bramborový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec418a943597.jpg",
        "title_dia": "Maďarský guláš, vařená rýže",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec63f9bde427.jpg",
        "title_dia": "Maďarský guláš, vařený brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f3389ecf379a.jpg",
        "title_dia": "Maďarský guláš, těstoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-60e8610956fe3.jpg",
        "title_dia": "Vepřový guláš, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-60e86115c08dd.jpg",
        "title_dia": "Vepřový guláš, bramborový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-60e861229b650.jpg",
        "title_dia": "Vepřový guláš, vařená rýže",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-60e8612ba33ec.jpg",
        "title_dia": "Vepřový guláš, vařený brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-60e86133563af.jpg",
        "title_dia": "Vepřový guláš, těstoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c892cb34c9.jpg",
        "title_dia": "Havelské vepřové srdce na smetaně, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c8913b22ee.jpg",
        "title_dia": "Havelské vepřové srdce na smetaně, bramborový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c891d48f5f.jpg",
        "title_dia": "Havelské vepřové srdce na smetaně, vařený brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c8935199d3.jpg",
        "title_dia": "Havelské vepřové srdce na smetaně, vařená rýže",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-6048848bac3e0.jpg",
        "title_dia": "Krkonošský guláš, houskové knedlíky",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-604940b984ec4.jpg",
        "title_dia": "Krkonošský guláš, bramborový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-6048849a243ef.jpg",
        "title_dia": "Krkonošský guláš, vařená rýže",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-604884a842353.jpg",
        "title_dia": "Krkonošský guláš, vařený brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-604884bd370b5.jpg",
        "title_dia": "Krkonošský guláš, těstoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e883c594ed1d.jpg",
        "title_dia": "Segedínský guláš speciál, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-633e90fc1914a.jpg",
        "title_dia": "Segedínský guláš speciál, bramborový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e8580c629c5a.jpg",
        "title_dia": "Koprová omáčka, hovězí maso vařené přední, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f436763d5725.jpg",
        "title_dia": "Koprová omáčka, hovězí maso vařené přední, brambory vařené",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f84aaac7f9b2.jpg",
        "title_dia": "Koprová omáčka, vejce vařené 2ks, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f84a882e2691.jpg",
        "title_dia": "Koprová omáčka, vejce vařené 2x, brambory vařené",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e8580d3943c7.jpg",
        "title_dia": "Rajská omáčka, hovězí maso vařené přední, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e883cef97285.jpg",
        "title_dia": "Rajská omáčka, hovězí maso vařené přední, rýže vařená",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f338a135619d.jpg",
        "title_dia": "Rajská omáčka, hovězí maso vařené přední, těstoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ea3ee90a9b36.jpg",
        "title_dia": "Plněný paprikový lusk, rajská omáčka , houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-60edd0c24c4af.jpg",
        "title_dia": "Plněný paprikový lusk, rajská omáčka, vařená rýže",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-626a92799a172.jpg",
        "title_dia": "Houbová omáčka - tmavá, hovězí maso zadní, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d8a9020aab.jpg",
        "title_dia": "Houbová omáčka - tmavá, hovězí maso zadní, bramborový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f3389b183695.jpg",
        "title_dia": "Houbová omáčka - tmavá, hovězí maso zadní, těstoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d89b9c27c5.jpg",
        "title_dia": "Houbová omáčka - tmavá, hovězí maso zadní, vařený brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e7f504ad2464.jpg",
        "title_dia": "Hovězí pečeně na žampionech, rýže vařená",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5eb97e94d9748.jpg",
        "title_dia": "Jitrnicový prejt, zelí, brambory vařené",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ed27523c94eb.jpg",
        "title_dia": "Houbová omáčka - světlá, hovězí maso přední, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f3389c15bd23.jpg",
        "title_dia": "Houbová omáčka - světlá, hovězí maso přední, těstoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e8580e58725f.jpg",
        "title_dia": "Bramborové knedlíky plněné uzeným masem 2ks, zelí",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ecb97b8dc898.jpg",
        "title_dia": "Bramborové knedlíky plněné uzeným masem 2ks, špenát",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5fabc52458fb5.jpg",
        "title_dia": "Bramborový knedlík plněný uzeným masem, 1ks, zelí",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5fabc53032e76.jpg",
        "title_dia": "Bramborový knedlík plněný uzeným masem 1ks, špenát",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-6065a78f50c92.jpg",
        "title_dia": "Vinná klobása, vařený brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-6065a6ef2cff0.jpg",
        "title_dia": "Vinná klobása, bramborová kaše",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-6065a70633e32.jpg",
        "title_dia": "Vinná klobása, čočka na kyselo, okurka sterilovaná",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-60a4c675a5828.jpg",
        "title_dia": "Vinná klobása, hrachová kaše s cibulkou, okurka sterilovaná",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e7f5188dd040.jpg",
        "title_dia": "Čočka na kyselo, uzená vepřová plec, okurka sterilovaná",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f84a6fae091c.jpg",
        "title_dia": "Čočka na kyselo, vejce vařené 2ks, okurka sterilovaná",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f7c7a3a07ec1.jpg",
        "title_dia": "Hrachová kaše s cibulkou, uzená vepřová plec, okurka sterilovaná",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-602f7d0ee3775.jpg",
        "title_dia": "Hrachová kaše s cibulkou, vejce vařené 2ks, okurka sterilovaná",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f00419572032.jpg",
        "title_dia": "Kuřecí steak zapečený, bramborová kaše",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f0042a2d1fbb.jpg",
        "title_dia": "Kuřecí steak zapečený, vařený brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-63ea6eae27606.jpg",
        "title_dia": "Kuřecí steak zapečený, bramborový salát",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f84ae6d8c9ee.jpg",
        "title_dia": "Kuřecí špíz, brambory vařené",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f84aed34c436.jpg",
        "title_dia": "Kuřecí špíz, bramborová kaše",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec40ddc5e570.jpg",
        "title_dia": "Čevabčiči s cibulí, vařené brambory, hořčice",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec63def5c7e9.jpg",
        "title_dia": "Sekaná pečeně, bramborová kaše",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e8580efd21a0.jpg",
        "title_dia": "Sekaná pečeně, vařený brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5eba4bd9b52a5.jpg",
        "title_dia": "Kuře pečené, bramborová kaše",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ea56fce876d6.jpg",
        "title_dia": "Kuře pečené, vařený brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ea56fa4586ca.jpg",
        "title_dia": "Kuře pečené, rýže vařená",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e858111de8fa.jpg",
        "title_dia": "Uzená plec, dušené zelí, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f7741a47e183.jpg",
        "title_dia": "Uzená plec, dušené zelí, bramborový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e866216bbe95.jpg",
        "title_dia": "Uzená plec, špenát, bramborový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d763029fe9.jpg",
        "title_dia": "Uzená vepřová plec, bramborová kaše, okurka sterilovaná",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ecb984bdc4a7.jpg",
        "title_dia": "Znojemská hovězí pečeně, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ecb984459e51.jpg",
        "title_dia": "Znojemská hovězí pečeně, rýže vařená",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-608c781a57556.jpg",
        "title_dia": "Cikánská hovězí pečeně, bramborový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-608c782c06025.jpg",
        "title_dia": "Cikánská hovězí pečeně, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-608c783b09f56.jpg",
        "title_dia": "Cikánská hovězí pečeně, rýže vařená",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-608c784855c3a.jpg",
        "title_dia": "Cikánská hovězí pečeně, vařený brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-608c7851d7611.jpg",
        "title_dia": "Cikánská hovězí pečeně, těstoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e90542ac5d9a.jpg",
        "title_dia": "Záhorský závitek z vepřové krkovice, brambory vařené",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e904c62bc973.jpg",
        "title_dia": "Halušky se zelím a uzeným masem",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f61dc1d70b21.jpg",
        "title_dia": "Záhorský závitek z vepřové krkovice, bramborový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e9049d2daed4.jpg",
        "title_dia": "Havelská pochoutka, rýže vařená",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ea403d1da4f2.jpg",
        "title_dia": "Kuřecí maso na nudličky, rýže vařená",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e9050c9e901e.jpg",
        "title_dia": "Španělský ptáček, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e904ce4dc761.jpg",
        "title_dia": "Španělský ptáček, rýže vařená",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e98b3c4dc5d2.jpg",
        "title_dia": "Vepřová po selsku, zelí, bramborový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5fad76c789695.jpg",
        "title_dia": "Vepřová po selsku, rýže vařená",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec63d9a1376b.jpg",
        "title_dia": "Vepřová po selsku, bramborová kaše, šťáva",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e905122c64e8.jpg",
        "title_dia": "Vepřová játra na cibulce, rýže vařená",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606db175e8475.jpg",
        "title_dia": "Vepřová játra na cibulce, vařený brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606da99abf9fa.jpg",
        "title_dia": "Vepřová játra na cibulce, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d7a35396fe.jpg",
        "title_dia": "Vepřová játra na cibulce, bramborový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e98a2f477b74.jpg",
        "title_dia": "Vepřová plec na žampionech, rýže vařená",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d82e9da328.jpg",
        "title_dia": "Vepřová plec na žampionech, těstoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d83f618d1f.jpg",
        "title_dia": "Vepřová plec na žampionech, vařený brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d8cfe0e784.jpg",
        "title_dia": "Vepřová plec na žampionech, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d8493083a7.jpg",
        "title_dia": "Vepřová plec na žampionech, bramborový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ea3eeafb0d08.jpg",
        "title_dia": "Rizoto s kuřecím masem, kyselá okurka",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e9057be9aed7.jpg",
        "title_dia": "Špagety s vepřovým masem",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ea6f7488654b.jpg",
        "title_dia": "Havelská kapsa",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5eb1dfa0d729b.jpg",
        "title_dia": "Josefovy šunkofleky, okurka sterilovaná",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ece48ea481a0.jpg",
        "title_dia": "Francouzské brambory, okurka sterilovaná",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec40e0061cc6.jpg",
        "title_dia": "Vepřové maso dušené v mrkvi, vařené brambory",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec4f7a07864e.jpg",
        "title_dia": "Vepřové maso na paprice, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f338a29d2058.jpg",
        "title_dia": "Vepřové maso na paprice, těstoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5fb15ec6c13a9.jpg",
        "title_dia": "Kuřecí maso na paprice, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5fb15ed43fb82.jpg",
        "title_dia": "Kuřecí maso na paprice, těstoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ee618bf15e5c.jpg",
        "title_dia": "Křenová omáčka, hovězí maso vařené zadní, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ee618c5ae98d.jpg",
        "title_dia": "Křenová omáčka, uzená vepřová plec, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ece47a70253d.jpg",
        "title_dia": "Mexické fazole",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e8985e455675.jpg",
        "title_dia": "Svíčková omáčka, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e898700d2f91.jpg",
        "title_dia": "Koprová omáčka, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e89862a53eac.jpg",
        "title_dia": "Rajská omáčka, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e89b8dbf095a.jpg",
        "title_dia": "Rajská omáčka, rýže vařená",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-6034e2741951c.jpg",
        "title_dia": "Rajská omáčka, těstoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e8987f7ecdca.jpg",
        "title_dia": "Houbová omáčka - tmavá, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d8eba15147.jpg",
        "title_dia": "Houbová omáčka - tmavá, bramborový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f3389d592718.jpg",
        "title_dia": "Houbová omáčka - tmavá, těstoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d85f5795cb.jpg",
        "title_dia": "Houbová omáčka - tmavá, rýže vařená",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d8deabe1c7.jpg",
        "title_dia": "Houbová omáčka - tmavá, vařený brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ed276209e729.jpg",
        "title_dia": "Houbová omáčka - světlá, houskový knedlík",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f3389e0dddbf.jpg",
        "title_dia": "Houbová omáčka - světlá, těstoviny",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5eb97d8401d18.jpg",
        "title_dia": "Smažený kuřecí řízek, bramborová kaše",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e8241cdafc40.jpg",
        "title_dia": "Smažený kuřecí řízek, salát bramborový",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e85813fb2e19.jpg",
        "title_dia": "Smažený kuřecí řízek, brambory vařené",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5eca2adab89fd.jpg",
        "title_dia": "Smažený vepřový řízek, bramborová kaše",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e8241c0ee609.jpg",
        "title_dia": "Smažený vepřový řízek, salát bramborový",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e7f51d55a528.jpg",
        "title_dia": "Smažený vepřový řízek, brambory vařené",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ece4bd329e86.jpg",
        "title_dia": "Smažený sýr Gouda 48%, bramborová kaše",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e85814a34341.jpg",
        "title_dia": "Smažený sýr Gouda 48%, brambory vařené",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ece4963ef01d.jpg",
        "title_dia": "Smažený sýr Hermelín, bramborová kaše",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e905276aa685.jpg",
        "title_dia": "Smažený sýr Hermelín, brambory vařené",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ed0c45ef2cc4.jpg",
        "title_dia": "Smažené rybí filé, bramborová kaše",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ea3efbb7b915.jpg",
        "title_dia": "Smažené rybí filé, salát bramborový",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ea3efac46d0c.jpg",
        "title_dia": "Smažené rybí filé , brambory vařené",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5f006370ba890.jpg",
        "title_dia": "Smažený květák, bramborová kaše",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e98b2162c9b0.jpg",
        "title_dia": "Smažený květák, brambory vařené",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-628230bcebb67.jpg",
        "title_dia": "Smažený květák, brambory vařené, tatarská omáčka",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-60d9b95be9b96.jpg",
        "title_dia": "Smažená brokolice, bramborová kaše",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-60d9b99289938.jpg",
        "title_dia": "Smažená brokolice, brambory vařené",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ecb9813d60d1.jpg",
        "title_dia": "Smažený karbanátek, bramborová kaše",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ed3920c37294.jpg",
        "title_dia": "Smažený karbanátek, bramborový salát",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ecb9824a5535.jpg",
        "title_dia": "Smažený karbanátek, vařený brambor",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5f0055d975c78.jpg",
        "title_dia": "Ondrův Holandský řízek, bramborová kaše",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e91aaec68626.jpg",
        "title_dia": "Ondrův Holandský řízek, brambory vařené",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ece4c24d1e46.jpg",
        "title_dia": "Smažené žampiony, kaše bramborová",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ed24c5c6ba9d.jpg",
        "title_dia": "Smažené žampiony, bramborový salát",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e98a27d3b87c.jpg",
        "title_dia": "Smažené žampiony, brambory vařené",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60af53787d9ae.jpg",
        "title_dia": "Jablková žemlovka",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5e7f53562815d.jpg",
        "title_dia": "Dukátové buchtičky s vanilkovým krémem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-626a3f6917391.jpg",
        "title_dia": "Bramborové šišky, mák, máslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc7d4be3bd.jpg",
        "title_dia": "Bramborové šišky, sypaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc80c741e7.jpg",
        "title_dia": "Bramborové šišky, šlehaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-606f8a850dc42.jpg",
        "title_dia": "Bramborové šišky, skořice, cukr, máslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-606f8b08568dd.jpg",
        "title_dia": "Těstoviny, strouhaný tvaroh, máslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-606f8b74ea822.jpg",
        "title_dia": "Těstoviny, mák, cukr, máslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-606f71cbd625a.jpg",
        "title_dia": "Kynutý blboun plněný povidly, vanilkový krém",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-606f7196b085b.jpg",
        "title_dia": "Kynutý blboun plněný povidly, mák, cukr, máslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60741b74c62ff.jpg",
        "title_dia": "Kynutý blboun plněný povidly, šlehaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-606f70ac0aae0.jpg",
        "title_dia": "Ovocné knedlíky 2ks - jablko, skořice, cukr, máslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-6071a6633cb26.jpg",
        "title_dia": "Ovocné knedlíky 2ks - jablko, vanilkový krém",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-6071a66d07230.jpg",
        "title_dia": "Ovocné knedlíky 2ks - jablko, sypaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-6071a659381c8.jpg",
        "title_dia": "Ovocné knedlíky 2ks - jablko, šlehaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702426dcf70.jpg",
        "title_dia": "Ovocné knedlíky 2ks - jahoda, vanilkový krém",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff5f58e9f1.jpg",
        "title_dia": "Ovocné knedlíky 2ks - jahoda, sypaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff64eb20e4.jpg",
        "title_dia": "Ovocné knedlíky 2ks - jahoda, šlehaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff68a408f3.jpg",
        "title_dia": "Ovocné knedlíky 2ks - jahoda, mák, máslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff60d7e087.jpg",
        "title_dia": "Ovocné knedlíky 2ks - meruňka, sypaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff66e20739.jpg",
        "title_dia": "Ovocné knedlíky 2ks - meruňka, šlehaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff6a70b0f0.jpg",
        "title_dia": "Ovocné knedlíky 2ks - meruňka, mák, máslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702444a56dc.jpg",
        "title_dia": "Ovocné knedlíky 2ks - malina, vanilkový krém",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff601539a3.jpg",
        "title_dia": "Ovocné knedlíky 2ks - malina, sypaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff6624075a.jpg",
        "title_dia": "Ovocné knedlíky 2ks - malina, šlehaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff69a40ebc.jpg",
        "title_dia": "Ovocné knedlíky 2ks - malina, mák, máslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-6070245928030.jpg",
        "title_dia": "Ovocné knedlíky 2ks - švestka, vanilkový krém",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff6192186c.jpg",
        "title_dia": "Ovocné knedlíky 2ks - švestka, sypaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff67d8d5ba.jpg",
        "title_dia": "Ovocné knedlíky 2ks - švestka, šlehaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff6b202639.jpg",
        "title_dia": "Ovocné knedlíky 2ks - švestka, mák, máslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702469568e2.jpg",
        "title_dia": "Ovocné knedlíky 2ks - borůvka, vanilkový krém",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f95e72e95223.jpg",
        "title_dia": "Ovocné knedlíky 2ks - borůvka, sypaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f95e724547e2.jpg",
        "title_dia": "Ovocné knedlíky 2ks - borůvka, šlehaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f95e717b2b37.jpg",
        "title_dia": "Ovocné knedlíky 2ks - borůvka, mák, máslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702cda2db79.jpg",
        "title_dia": "Ovocné knedlíky 2ks - ostružina, vanilkový krém",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702cecd6637.jpg",
        "title_dia": "Ovocné knedlíky 2ks - ostružina, sypaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702cfe255c4.jpg",
        "title_dia": "Ovocné knedlíky 2ks - ostružina, šlehaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702d0736201.jpg",
        "title_dia": "Ovocné knedlíky 2ks - ostružina, mák, máslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607ff502d20dd.jpg",
        "title_dia": "Bramborové knedlíky švestkové 4ks, sypaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607ff50cca110.jpg",
        "title_dia": "Bramborové knedlíky švestkové 4ks, šlehaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607ff51c4ec46.jpg",
        "title_dia": "Bramborové knedlíky švestkové 4ks, mák, máslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-606f7112c3548.jpg",
        "title_dia": "Ovocný knedlík 1ks - jablko, skořice, cukr, máslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-6071a63b16bb4.jpg",
        "title_dia": "Ovocný knedlík 1ks - jablko, vanilkový krém",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-6071a646a919f.jpg",
        "title_dia": "Ovocný knedlík 1ks - jablko, sypaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-6071a6324587b.jpg",
        "title_dia": "Ovocný knedlík 1ks - jablko, šlehaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607028ab4f463.jpg",
        "title_dia": "Ovocný knedlík 1ks - jahoda, vanilkový krém",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc334c86a5.jpg",
        "title_dia": "Ovocný knedlík 1ks - jahoda, sypaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc38eb8e4a.jpg",
        "title_dia": "Ovocný knedlík 1ks - jahoda, šlehaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc4308649c.jpg",
        "title_dia": "Ovocný knedlík 1ks - jahoda, mák, máslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607028b883aad.jpg",
        "title_dia": "Ovocný knedlík 1ks - meruňka, vanilkový krém",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc35fc843a.jpg",
        "title_dia": "Ovocný knedlík 1ks - meruňka, sypaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc3d0a3a4e.jpg",
        "title_dia": "Ovocný knedlík 1ks - meruňka, šlehaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc45490c87.jpg",
        "title_dia": "Ovocný knedlík 1ks - meruňka, mák, máslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607028c867513.jpg",
        "title_dia": "Ovocný knedlík 1ks - malina, vanilkový krém",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc351dc9d7.jpg",
        "title_dia": "Ovocný knedlík 1ks - malina, sypaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc3de54ce7.jpg",
        "title_dia": "Ovocný knedlík 1ks - malina, šlehaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc44586068.jpg",
        "title_dia": "Ovocný knedlík 1ks - malina, mák, máslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607028d81cf14.jpg",
        "title_dia": "Ovocný knedlík 1ks - švestka, vanilkový krém",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc36cf318c.jpg",
        "title_dia": "Ovocný knedlík 1ks - švestka, sypaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc3e793bb7.jpg",
        "title_dia": "Ovocný knedlík 1ks - švestka, šlehaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc46145b82.jpg",
        "title_dia": "Ovocný knedlík 1ks - švestka, mák, máslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607028e7e0ee8.jpg",
        "title_dia": "Ovocný knedlík 1ks - borůvka, vanilkový krém",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc3216ca82.jpg",
        "title_dia": "Ovocný knedlík 1ks - borůvka, sypaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc37cceacb.jpg",
        "title_dia": "Ovocný knedlík 1ks - borůvka, šlehaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc41b70cbd.jpg",
        "title_dia": "Ovocný knedlík 1ks - borůvka, mák, máslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702e371a9b4.jpg",
        "title_dia": "Ovocný knedlík 1ks - ostružina, vanilkový krém",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702e4775c78.jpg",
        "title_dia": "Ovocný knedlík 1ks - ostružina, sypaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702e54c485b.jpg",
        "title_dia": "Ovocný knedlík 1ks - ostružina, šlehaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702e645be77.jpg",
        "title_dia": "Ovocný knedlík 1ks - ostružina, mák, máslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607ef4db64d76.jpg",
        "title_dia": "Bramborové knedlíky švestkové 2ks, sypaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607ef4eda106b.jpg",
        "title_dia": "Bramborové knedlíky švestkové 2ks, šlehaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607ef504c6d89.jpg",
        "title_dia": "Bramborové knedlíky švestkové 2ks, mák, máslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5e8241917f35c.jpg",
        "title_dia": "Ovocné knedlíky, sypaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5e824168e07ef.jpg",
        "title_dia": "Ovocné knedlíky, šlehaný tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f0051a6b701c.jpg",
        "title_dia": "Ovocný knedlík, mák, máslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60c23ced4c111.jpg",
        "title_dia": "Jahodová pochoutka",
    },
]


input_dict2 = [
    {
        "category": "polevky",
        "imgsource": "image-5e7f9d82abf36.jpg",
        "title_curred": "Hovezi_vyvar_s_masem_a_nudlemi",
    },
    {
        "category": "polevky",
        "imgsource": "image-5e81d9515faf2.jpg",
        "title_curred": "Kulajda",
    },
    {
        "category": "polevky",
        "imgsource": "image-5f00448c4aa99.jpg",
        "title_curred": "Gulasova",
    },
    {
        "category": "polevky",
        "imgsource": "image-5ea3ef41292da.jpg",
        "title_curred": "Borsc",
    },
    {
        "category": "polevky",
        "imgsource": "image-5eba656baaace.jpg",
        "title_curred": "Frankfurtska",
    },
    {
        "category": "polevky",
        "imgsource": "image-5ece47d918a12.jpg",
        "title_curred": "Zelna_s_uzeninou",
    },
    {
        "category": "polevky",
        "imgsource": "image-5e7f71415405c.jpg",
        "title_curred": "Cockova",
    },
    {
        "category": "polevky",
        "imgsource": "image-5e98a24cf290f.jpg",
        "title_curred": "Fazolova",
    },
    {
        "category": "polevky",
        "imgsource": "image-5f8431da214c7.jpg",
        "title_curred": "Krupicova_s_vejcem",
    },
    {
        "category": "polevky",
        "imgsource": "image-5e948825b3d7c.jpg",
        "title_curred": "Rajska_s_ryzi",
    },
    {
        "category": "polevky",
        "imgsource": "image-5e9051c2f069c.jpg",
        "title_curred": "Bramborova",
    },
    {
        "category": "polevky",
        "imgsource": "image-5ec63ce1a9ca8.jpg",
        "title_curred": "Zeleninova",
    },
    {
        "category": "polevky",
        "imgsource": "image-5eb1e050b69a1.jpg",
        "title_curred": "Porkova_s_vejcem",
    },
    {
        "category": "polevky",
        "imgsource": "image-5f3e2a8a256e0.jpg",
        "title_curred": "Kvetakova",
    },
    {
        "category": "polevky",
        "imgsource": "image-5f00438d856c4.jpg",
        "title_curred": "Brokolicova",
    },
    {
        "category": "polevky",
        "imgsource": "image-609a3b60be916.jpg",
        "title_curred": "Cesnekova_polevka_s_bramborami",
    },
    {
        "category": "polevky",
        "imgsource": "image-5f01961398152.jpg",
        "title_curred": "Hrachova_se_smazenym_hraskem",
    },
    {
        "category": "polevky",
        "imgsource": "image-5fa5490109745.jpg",
        "title_curred": "Drstkova",
    },
    {
        "category": "polevky",
        "imgsource": "image-5e80fcbacb9e5.jpg",
        "title_curred": "Drubezi_vyvar_s_masem_a_nudlemi",
    },
    {
        "category": "polevky",
        "imgsource": "image-5eb1dfc02b39b.jpg",
        "title_curred": "Hovezi_vyvar_s_jatrovymi_knedlicky",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607ff9e93c2b4.jpg",
        "title_curred": "Staroceske_pecene_koleno,_horcice,_kren,_kysela_okurka,_chleb_900g_v_syrovem_stavu",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d8fabaa96a.jpg",
        "title_curred": "Pecene_veprove_koleno_na_cernem_pivu,_horcice,_kren,_zelny_salat,_chleb",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ee6186b90db3.jpg",
        "title_curred": "Pecene_kachni_stehno,_bile_zeli,_bramborovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ee61870e4fe4.jpg",
        "title_curred": "Pecene_kachni_stehno,_bile_zeli,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-608c77acc85a3.jpg",
        "title_curred": "Veprova_marinovana_zebra,_chleb_3ks_platek",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e85806b107b0.jpg",
        "title_curred": "Svickova_na_smetane,_hovezi_maso_zadni,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d7501bbf38.jpg",
        "title_curred": "Hovezi_na_cesneku,_spenat,_bramborovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c8db43dbe1.jpg",
        "title_curred": "Hovezi_na_cesneku,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c8c2735f44.jpg",
        "title_curred": "Hovezi_na_cesneku,_varena_ryze",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c8c1da8c81.jpg",
        "title_curred": "Hovezi_na_cesneku,_bramborovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c8c43367de.jpg",
        "title_curred": "Hovezi_na_cesneku,_vareny_brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c8c4d09514.jpg",
        "title_curred": "Hovezi_na_cesneku,_testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-633e8fc6a16bf.jpg",
        "title_curred": "Moravsky_vrabec,_dusene_zeli,_bramborovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-633e8ffc5e732.jpg",
        "title_curred": "Moravsky_vrabec,_dusene_zeli,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-633e90a8bccd2.jpg",
        "title_curred": "Moravsky_vrabec,_spenat,_bramborovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-633e90cb4a2ca.jpg",
        "title_curred": "Moravsky_vrabec,_spenat,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-61dedd472998b.jpg",
        "title_curred": "Plzensky_gulas,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-61dedd522a807.jpg",
        "title_curred": "Plzensky_gulas,_bramborovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-61dedd5da39d0.jpg",
        "title_curred": "Plzensky_gulas,_varena_ryze",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-61dedd7027379.jpg",
        "title_curred": "Plzensky_gulas,_vareny_brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-61dedd81bf07e.jpg",
        "title_curred": "Plzensky_gulas,_testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e8580b5eb8b6.jpg",
        "title_curred": "Hovezi_gulas,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d80e01a32b.jpg",
        "title_curred": "Hovezi_gulas,_bramborovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec41873a7146.jpg",
        "title_curred": "Hovezi_gulas,_varena_ryze",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec63f5ddd749.jpg",
        "title_curred": "Hovezi_gulas,_vareny_brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f3389fd6cbf9.jpg",
        "title_curred": "Hovezi_gulas,_testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e7f503bbef30.jpg",
        "title_curred": "Madarsky_gulas,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d81cf94da6.jpg",
        "title_curred": "Madarsky_gulas,_bramborovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec418a943597.jpg",
        "title_curred": "Madarsky_gulas,_varena_ryze",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec63f9bde427.jpg",
        "title_curred": "Madarsky_gulas,_vareny_brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f3389ecf379a.jpg",
        "title_curred": "Madarsky_gulas,_testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-60e8610956fe3.jpg",
        "title_curred": "Veprovy_gulas,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-60e86115c08dd.jpg",
        "title_curred": "Veprovy_gulas,_bramborovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-60e861229b650.jpg",
        "title_curred": "Veprovy_gulas,_varena_ryze",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-60e8612ba33ec.jpg",
        "title_curred": "Veprovy_gulas,_vareny_brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-60e86133563af.jpg",
        "title_curred": "Veprovy_gulas,_testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c892cb34c9.jpg",
        "title_curred": "Havelske_veprove_srdce_na_smetane,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c8913b22ee.jpg",
        "title_curred": "Havelske_veprove_srdce_na_smetane,_bramborovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c891d48f5f.jpg",
        "title_curred": "Havelske_veprove_srdce_na_smetane,_vareny_brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c8935199d3.jpg",
        "title_curred": "Havelske_veprove_srdce_na_smetane,_varena_ryze",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-6048848bac3e0.jpg",
        "title_curred": "Krkonossky_gulas,_houskove_knedliky",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-604940b984ec4.jpg",
        "title_curred": "Krkonossky_gulas,_bramborovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-6048849a243ef.jpg",
        "title_curred": "Krkonossky_gulas,_varena_ryze",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-604884a842353.jpg",
        "title_curred": "Krkonossky_gulas,_vareny_brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-604884bd370b5.jpg",
        "title_curred": "Krkonossky_gulas,_testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e883c594ed1d.jpg",
        "title_curred": "Segedinsky_gulas_special,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-633e90fc1914a.jpg",
        "title_curred": "Segedinsky_gulas_special,_bramborovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e8580c629c5a.jpg",
        "title_curred": "Koprova_omacka,_hovezi_maso_varene_predni,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f436763d5725.jpg",
        "title_curred": "Koprova_omacka,_hovezi_maso_varene_predni,_brambory_varene",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f84aaac7f9b2.jpg",
        "title_curred": "Koprova_omacka,_vejce_varene_2ks,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f84a882e2691.jpg",
        "title_curred": "Koprova_omacka,_vejce_varene_2x,_brambory_varene",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e8580d3943c7.jpg",
        "title_curred": "Rajska_omacka,_hovezi_maso_varene_predni,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e883cef97285.jpg",
        "title_curred": "Rajska_omacka,_hovezi_maso_varene_predni,_ryze_varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f338a135619d.jpg",
        "title_curred": "Rajska_omacka,_hovezi_maso_varene_predni,_testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ea3ee90a9b36.jpg",
        "title_curred": "Plneny_paprikovy_lusk,_rajska_omacka_,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-60edd0c24c4af.jpg",
        "title_curred": "Plneny_paprikovy_lusk,_rajska_omacka,_varena_ryze",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-626a92799a172.jpg",
        "title_curred": "Houbova_omacka_-_tmava,_hovezi_maso_zadni,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d8a9020aab.jpg",
        "title_curred": "Houbova_omacka_-_tmava,_hovezi_maso_zadni,_bramborovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f3389b183695.jpg",
        "title_curred": "Houbova_omacka_-_tmava,_hovezi_maso_zadni,_testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d89b9c27c5.jpg",
        "title_curred": "Houbova_omacka_-_tmava,_hovezi_maso_zadni,_vareny_brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e7f504ad2464.jpg",
        "title_curred": "Hovezi_pecene_na_zampionech,_ryze_varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5eb97e94d9748.jpg",
        "title_curred": "Jitrnicovy_prejt,_zeli,_brambory_varene",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ed27523c94eb.jpg",
        "title_curred": "Houbova_omacka_-_svetla,_hovezi_maso_predni,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f3389c15bd23.jpg",
        "title_curred": "Houbova_omacka_-_svetla,_hovezi_maso_predni,_testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e8580e58725f.jpg",
        "title_curred": "Bramborove_knedliky_plnene_uzenym_masem_2ks,_zeli",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ecb97b8dc898.jpg",
        "title_curred": "Bramborove_knedliky_plnene_uzenym_masem_2ks,_spenat",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5fabc52458fb5.jpg",
        "title_curred": "Bramborovy_knedlik_plneny_uzenym_masem,_1ks,_zeli",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5fabc53032e76.jpg",
        "title_curred": "Bramborovy_knedlik_plneny_uzenym_masem_1ks,_spenat",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-6065a78f50c92.jpg",
        "title_curred": "Vinna_klobasa,_vareny_brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-6065a6ef2cff0.jpg",
        "title_curred": "Vinna_klobasa,_bramborova_kase",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-6065a70633e32.jpg",
        "title_curred": "Vinna_klobasa,_cocka_na_kyselo,_okurka_sterilovana",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-60a4c675a5828.jpg",
        "title_curred": "Vinna_klobasa,_hrachova_kase_s_cibulkou,_okurka_sterilovana",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e7f5188dd040.jpg",
        "title_curred": "Cocka_na_kyselo,_uzena_veprova_plec,_okurka_sterilovana",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f84a6fae091c.jpg",
        "title_curred": "Cocka_na_kyselo,_vejce_varene_2ks,_okurka_sterilovana",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f7c7a3a07ec1.jpg",
        "title_curred": "Hrachova_kase_s_cibulkou,_uzena_veprova_plec,_okurka_sterilovana",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-602f7d0ee3775.jpg",
        "title_curred": "Hrachova_kase_s_cibulkou,_vejce_varene_2ks,_okurka_sterilovana",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f00419572032.jpg",
        "title_curred": "Kureci_steak_zapeceny,_bramborova_kase",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f0042a2d1fbb.jpg",
        "title_curred": "Kureci_steak_zapeceny,_vareny_brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-63ea6eae27606.jpg",
        "title_curred": "Kureci_steak_zapeceny,_bramborovy_salat",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f84ae6d8c9ee.jpg",
        "title_curred": "Kureci_spiz,_brambory_varene",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f84aed34c436.jpg",
        "title_curred": "Kureci_spiz,_bramborova_kase",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec40ddc5e570.jpg",
        "title_curred": "Cevabcici_s_cibuli,_varene_brambory,_horcice",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec63def5c7e9.jpg",
        "title_curred": "Sekana_pecene,_bramborova_kase",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e8580efd21a0.jpg",
        "title_curred": "Sekana_pecene,_vareny_brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5eba4bd9b52a5.jpg",
        "title_curred": "Kure_pecene,_bramborova_kase",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ea56fce876d6.jpg",
        "title_curred": "Kure_pecene,_vareny_brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ea56fa4586ca.jpg",
        "title_curred": "Kure_pecene,_ryze_varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e858111de8fa.jpg",
        "title_curred": "Uzena_plec,_dusene_zeli,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f7741a47e183.jpg",
        "title_curred": "Uzena_plec,_dusene_zeli,_bramborovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e866216bbe95.jpg",
        "title_curred": "Uzena_plec,_spenat,_bramborovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d763029fe9.jpg",
        "title_curred": "Uzena_veprova_plec,_bramborova_kase,_okurka_sterilovana",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ecb984bdc4a7.jpg",
        "title_curred": "Znojemska_hovezi_pecene,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ecb984459e51.jpg",
        "title_curred": "Znojemska_hovezi_pecene,_ryze_varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-608c781a57556.jpg",
        "title_curred": "Cikanska_hovezi_pecene,_bramborovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-608c782c06025.jpg",
        "title_curred": "Cikanska_hovezi_pecene,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-608c783b09f56.jpg",
        "title_curred": "Cikanska_hovezi_pecene,_ryze_varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-608c784855c3a.jpg",
        "title_curred": "Cikanska_hovezi_pecene,_vareny_brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-608c7851d7611.jpg",
        "title_curred": "Cikanska_hovezi_pecene,_testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e90542ac5d9a.jpg",
        "title_curred": "Zahorsky_zavitek_z_veprove_krkovice,_brambory_varene",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e904c62bc973.jpg",
        "title_curred": "Halusky_se_zelim_a_uzenym_masem",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f61dc1d70b21.jpg",
        "title_curred": "Zahorsky_zavitek_z_veprove_krkovice,_bramborovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e9049d2daed4.jpg",
        "title_curred": "Havelska_pochoutka,_ryze_varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ea403d1da4f2.jpg",
        "title_curred": "Kureci_maso_na_nudlicky,_ryze_varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e9050c9e901e.jpg",
        "title_curred": "Spanelsky_ptacek,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e904ce4dc761.jpg",
        "title_curred": "Spanelsky_ptacek,_ryze_varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e98b3c4dc5d2.jpg",
        "title_curred": "Veprova_po_selsku,_zeli,_bramborovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5fad76c789695.jpg",
        "title_curred": "Veprova_po_selsku,_ryze_varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec63d9a1376b.jpg",
        "title_curred": "Veprova_po_selsku,_bramborova_kase,_stava",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e905122c64e8.jpg",
        "title_curred": "Veprova_jatra_na_cibulce,_ryze_varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606db175e8475.jpg",
        "title_curred": "Veprova_jatra_na_cibulce,_vareny_brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606da99abf9fa.jpg",
        "title_curred": "Veprova_jatra_na_cibulce,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d7a35396fe.jpg",
        "title_curred": "Veprova_jatra_na_cibulce,_bramborovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e98a2f477b74.jpg",
        "title_curred": "Veprova_plec_na_zampionech,_ryze_varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d82e9da328.jpg",
        "title_curred": "Veprova_plec_na_zampionech,_testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d83f618d1f.jpg",
        "title_curred": "Veprova_plec_na_zampionech,_vareny_brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d8cfe0e784.jpg",
        "title_curred": "Veprova_plec_na_zampionech,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d8493083a7.jpg",
        "title_curred": "Veprova_plec_na_zampionech,_bramborovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ea3eeafb0d08.jpg",
        "title_curred": "Rizoto_s_kurecim_masem,_kysela_okurka",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e9057be9aed7.jpg",
        "title_curred": "Spagety_s_veprovym_masem",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ea6f7488654b.jpg",
        "title_curred": "Havelska_kapsa",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5eb1dfa0d729b.jpg",
        "title_curred": "Josefovy_sunkofleky,_okurka_sterilovana",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ece48ea481a0.jpg",
        "title_curred": "Francouzske_brambory,_okurka_sterilovana",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec40e0061cc6.jpg",
        "title_curred": "Veprove_maso_dusene_v_mrkvi,_varene_brambory",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec4f7a07864e.jpg",
        "title_curred": "Veprove_maso_na_paprice,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f338a29d2058.jpg",
        "title_curred": "Veprove_maso_na_paprice,_testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5fb15ec6c13a9.jpg",
        "title_curred": "Kureci_maso_na_paprice,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5fb15ed43fb82.jpg",
        "title_curred": "Kureci_maso_na_paprice,_testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ee618bf15e5c.jpg",
        "title_curred": "Krenova_omacka,_hovezi_maso_varene_zadni,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ee618c5ae98d.jpg",
        "title_curred": "Krenova_omacka,_uzena_veprova_plec,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ece47a70253d.jpg",
        "title_curred": "Mexicke_fazole",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e8985e455675.jpg",
        "title_curred": "Svickova_omacka,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e898700d2f91.jpg",
        "title_curred": "Koprova_omacka,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e89862a53eac.jpg",
        "title_curred": "Rajska_omacka,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e89b8dbf095a.jpg",
        "title_curred": "Rajska_omacka,_ryze_varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-6034e2741951c.jpg",
        "title_curred": "Rajska_omacka,_testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e8987f7ecdca.jpg",
        "title_curred": "Houbova_omacka_-_tmava,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d8eba15147.jpg",
        "title_curred": "Houbova_omacka_-_tmava,_bramborovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f3389d592718.jpg",
        "title_curred": "Houbova_omacka_-_tmava,_testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d85f5795cb.jpg",
        "title_curred": "Houbova_omacka_-_tmava,_ryze_varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d8deabe1c7.jpg",
        "title_curred": "Houbova_omacka_-_tmava,_vareny_brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ed276209e729.jpg",
        "title_curred": "Houbova_omacka_-_svetla,_houskovy_knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f3389e0dddbf.jpg",
        "title_curred": "Houbova_omacka_-_svetla,_testoviny",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5eb97d8401d18.jpg",
        "title_curred": "Smazeny_kureci_rizek,_bramborova_kase",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e8241cdafc40.jpg",
        "title_curred": "Smazeny_kureci_rizek,_salat_bramborovy",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e85813fb2e19.jpg",
        "title_curred": "Smazeny_kureci_rizek,_brambory_varene",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5eca2adab89fd.jpg",
        "title_curred": "Smazeny_veprovy_rizek,_bramborova_kase",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e8241c0ee609.jpg",
        "title_curred": "Smazeny_veprovy_rizek,_salat_bramborovy",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e7f51d55a528.jpg",
        "title_curred": "Smazeny_veprovy_rizek,_brambory_varene",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ece4bd329e86.jpg",
        "title_curred": "Smazeny_syr_Gouda_48%,_bramborova_kase",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e85814a34341.jpg",
        "title_curred": "Smazeny_syr_Gouda_48%,_brambory_varene",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ece4963ef01d.jpg",
        "title_curred": "Smazeny_syr_Hermelin,_bramborova_kase",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e905276aa685.jpg",
        "title_curred": "Smazeny_syr_Hermelin,_brambory_varene",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ed0c45ef2cc4.jpg",
        "title_curred": "Smazene_rybi_file,_bramborova_kase",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ea3efbb7b915.jpg",
        "title_curred": "Smazene_rybi_file,_salat_bramborovy",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ea3efac46d0c.jpg",
        "title_curred": "Smazene_rybi_file_,_brambory_varene",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5f006370ba890.jpg",
        "title_curred": "Smazeny_kvetak,_bramborova_kase",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e98b2162c9b0.jpg",
        "title_curred": "Smazeny_kvetak,_brambory_varene",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-628230bcebb67.jpg",
        "title_curred": "Smazeny_kvetak,_brambory_varene,_tatarska_omacka",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-60d9b95be9b96.jpg",
        "title_curred": "Smazena_brokolice,_bramborova_kase",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-60d9b99289938.jpg",
        "title_curred": "Smazena_brokolice,_brambory_varene",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ecb9813d60d1.jpg",
        "title_curred": "Smazeny_karbanatek,_bramborova_kase",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ed3920c37294.jpg",
        "title_curred": "Smazeny_karbanatek,_bramborovy_salat",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ecb9824a5535.jpg",
        "title_curred": "Smazeny_karbanatek,_vareny_brambor",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5f0055d975c78.jpg",
        "title_curred": "Ondruv_Holandsky_rizek,_bramborova_kase",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e91aaec68626.jpg",
        "title_curred": "Ondruv_Holandsky_rizek,_brambory_varene",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ece4c24d1e46.jpg",
        "title_curred": "Smazene_zampiony,_kase_bramborova",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ed24c5c6ba9d.jpg",
        "title_curred": "Smazene_zampiony,_bramborovy_salat",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e98a27d3b87c.jpg",
        "title_curred": "Smazene_zampiony,_brambory_varene",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60af53787d9ae.jpg",
        "title_curred": "Jablkova_zemlovka",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5e7f53562815d.jpg",
        "title_curred": "Dukatove_buchticky_s_vanilkovym_kremem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-626a3f6917391.jpg",
        "title_curred": "Bramborove_sisky,_mak,_maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc7d4be3bd.jpg",
        "title_curred": "Bramborove_sisky,_sypany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc80c741e7.jpg",
        "title_curred": "Bramborove_sisky,_slehany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-606f8a850dc42.jpg",
        "title_curred": "Bramborove_sisky,_skorice,_cukr,_maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-606f8b08568dd.jpg",
        "title_curred": "Testoviny,_strouhany_tvaroh,_maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-606f8b74ea822.jpg",
        "title_curred": "Testoviny,_mak,_cukr,_maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-606f71cbd625a.jpg",
        "title_curred": "Kynuty_blboun_plneny_povidly,_vanilkovy_krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-606f7196b085b.jpg",
        "title_curred": "Kynuty_blboun_plneny_povidly,_mak,_cukr,_maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60741b74c62ff.jpg",
        "title_curred": "Kynuty_blboun_plneny_povidly,_slehany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-606f70ac0aae0.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_jablko,_skorice,_cukr,_maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-6071a6633cb26.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_jablko,_vanilkovy_krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-6071a66d07230.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_jablko,_sypany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-6071a659381c8.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_jablko,_slehany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702426dcf70.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_jahoda,_vanilkovy_krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff5f58e9f1.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_jahoda,_sypany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff64eb20e4.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_jahoda,_slehany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff68a408f3.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_jahoda,_mak,_maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff60d7e087.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_merunka,_sypany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff66e20739.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_merunka,_slehany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff6a70b0f0.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_merunka,_mak,_maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702444a56dc.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_malina,_vanilkovy_krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff601539a3.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_malina,_sypany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff6624075a.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_malina,_slehany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff69a40ebc.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_malina,_mak,_maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-6070245928030.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_svestka,_vanilkovy_krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff6192186c.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_svestka,_sypany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff67d8d5ba.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_svestka,_slehany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff6b202639.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_svestka,_mak,_maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702469568e2.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_boruvka,_vanilkovy_krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f95e72e95223.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_boruvka,_sypany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f95e724547e2.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_boruvka,_slehany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f95e717b2b37.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_boruvka,_mak,_maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702cda2db79.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_ostruzina,_vanilkovy_krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702cecd6637.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_ostruzina,_sypany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702cfe255c4.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_ostruzina,_slehany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702d0736201.jpg",
        "title_curred": "Ovocne_knedliky_2ks_-_ostruzina,_mak,_maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607ff502d20dd.jpg",
        "title_curred": "Bramborove_knedliky_svestkove_4ks,_sypany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607ff50cca110.jpg",
        "title_curred": "Bramborove_knedliky_svestkove_4ks,_slehany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607ff51c4ec46.jpg",
        "title_curred": "Bramborove_knedliky_svestkove_4ks,_mak,_maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-606f7112c3548.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_jablko,_skorice,_cukr,_maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-6071a63b16bb4.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_jablko,_vanilkovy_krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-6071a646a919f.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_jablko,_sypany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-6071a6324587b.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_jablko,_slehany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607028ab4f463.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_jahoda,_vanilkovy_krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc334c86a5.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_jahoda,_sypany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc38eb8e4a.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_jahoda,_slehany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc4308649c.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_jahoda,_mak,_maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607028b883aad.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_merunka,_vanilkovy_krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc35fc843a.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_merunka,_sypany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc3d0a3a4e.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_merunka,_slehany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc45490c87.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_merunka,_mak,_maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607028c867513.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_malina,_vanilkovy_krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc351dc9d7.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_malina,_sypany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc3de54ce7.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_malina,_slehany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc44586068.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_malina,_mak,_maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607028d81cf14.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_svestka,_vanilkovy_krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc36cf318c.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_svestka,_sypany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc3e793bb7.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_svestka,_slehany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc46145b82.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_svestka,_mak,_maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607028e7e0ee8.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_boruvka,_vanilkovy_krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc3216ca82.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_boruvka,_sypany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc37cceacb.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_boruvka,_slehany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc41b70cbd.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_boruvka,_mak,_maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702e371a9b4.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_ostruzina,_vanilkovy_krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702e4775c78.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_ostruzina,_sypany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702e54c485b.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_ostruzina,_slehany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702e645be77.jpg",
        "title_curred": "Ovocny_knedlik_1ks_-_ostruzina,_mak,_maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607ef4db64d76.jpg",
        "title_curred": "Bramborove_knedliky_svestkove_2ks,_sypany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607ef4eda106b.jpg",
        "title_curred": "Bramborove_knedliky_svestkove_2ks,_slehany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607ef504c6d89.jpg",
        "title_curred": "Bramborove_knedliky_svestkove_2ks,_mak,_maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5e8241917f35c.jpg",
        "title_curred": "Ovocne_knedliky,_sypany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5e824168e07ef.jpg",
        "title_curred": "Ovocne_knedliky,_slehany_tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f0051a6b701c.jpg",
        "title_curred": "Ovocny_knedlik,_mak,_maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60c23ced4c111.jpg",
        "title_curred": "Jahodova_pochoutka",
    },
]

input_dict3 = [
    {
        "category": "polevky",
        "imgsource": "image-5e7f9d82abf36.jpg",
        "title_no_dia": "Hovezi vyvar s masem a nudlemi",
    },
    {
        "category": "polevky",
        "imgsource": "image-5e81d9515faf2.jpg",
        "title_no_dia": "Kulajda",
    },
    {
        "category": "polevky",
        "imgsource": "image-5f00448c4aa99.jpg",
        "title_no_dia": "Gulasova",
    },
    {
        "category": "polevky",
        "imgsource": "image-5ea3ef41292da.jpg",
        "title_no_dia": "Borsc",
    },
    {
        "category": "polevky",
        "imgsource": "image-5eba656baaace.jpg",
        "title_no_dia": "Frankfurtska",
    },
    {
        "category": "polevky",
        "imgsource": "image-5ece47d918a12.jpg",
        "title_no_dia": "Zelna s uzeninou",
    },
    {
        "category": "polevky",
        "imgsource": "image-5e7f71415405c.jpg",
        "title_no_dia": "Cockova",
    },
    {
        "category": "polevky",
        "imgsource": "image-5e98a24cf290f.jpg",
        "title_no_dia": "Fazolova",
    },
    {
        "category": "polevky",
        "imgsource": "image-5f8431da214c7.jpg",
        "title_no_dia": "Krupicova s vejcem",
    },
    {
        "category": "polevky",
        "imgsource": "image-5e948825b3d7c.jpg",
        "title_no_dia": "Rajska s ryzi",
    },
    {
        "category": "polevky",
        "imgsource": "image-5e9051c2f069c.jpg",
        "title_no_dia": "Bramborova",
    },
    {
        "category": "polevky",
        "imgsource": "image-5ec63ce1a9ca8.jpg",
        "title_no_dia": "Zeleninova",
    },
    {
        "category": "polevky",
        "imgsource": "image-5eb1e050b69a1.jpg",
        "title_no_dia": "Porkova s vejcem",
    },
    {
        "category": "polevky",
        "imgsource": "image-5f3e2a8a256e0.jpg",
        "title_no_dia": "Kvetakova",
    },
    {
        "category": "polevky",
        "imgsource": "image-5f00438d856c4.jpg",
        "title_no_dia": "Brokolicova",
    },
    {
        "category": "polevky",
        "imgsource": "image-609a3b60be916.jpg",
        "title_no_dia": "Cesnekova polevka s bramborami",
    },
    {
        "category": "polevky",
        "imgsource": "image-5f01961398152.jpg",
        "title_no_dia": "Hrachova se smazenym hraskem",
    },
    {
        "category": "polevky",
        "imgsource": "image-5fa5490109745.jpg",
        "title_no_dia": "Drstkova",
    },
    {
        "category": "polevky",
        "imgsource": "image-5e80fcbacb9e5.jpg",
        "title_no_dia": "Drubezi vyvar s masem a nudlemi",
    },
    {
        "category": "polevky",
        "imgsource": "image-5eb1dfc02b39b.jpg",
        "title_no_dia": "Hovezi vyvar s jatrovymi knedlicky",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607ff9e93c2b4.jpg",
        "title_no_dia": "Staroceske pecene koleno, horcice, kren, kysela okurka, chleb / 900g v syrovem stavu",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d8fabaa96a.jpg",
        "title_no_dia": "Pecene veprove koleno na cernem pivu, horcice, kren, zelny salat, chleb",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ee6186b90db3.jpg",
        "title_no_dia": "Pecene kachni stehno, bile zeli, bramborovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ee61870e4fe4.jpg",
        "title_no_dia": "Pecene kachni stehno, bile zeli, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-608c77acc85a3.jpg",
        "title_no_dia": "Veprova marinovana zebra, chleb 3ks platek",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e85806b107b0.jpg",
        "title_no_dia": "Svickova na smetane, hovezi maso zadni, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d7501bbf38.jpg",
        "title_no_dia": "Hovezi na cesneku, spenat, bramborovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c8db43dbe1.jpg",
        "title_no_dia": "Hovezi na cesneku, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c8c2735f44.jpg",
        "title_no_dia": "Hovezi na cesneku, varena ryze",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c8c1da8c81.jpg",
        "title_no_dia": "Hovezi na cesneku, bramborovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c8c43367de.jpg",
        "title_no_dia": "Hovezi na cesneku, vareny brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c8c4d09514.jpg",
        "title_no_dia": "Hovezi na cesneku, testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-633e8fc6a16bf.jpg",
        "title_no_dia": "Moravsky vrabec, dusene zeli, bramborovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-633e8ffc5e732.jpg",
        "title_no_dia": "Moravsky vrabec, dusene zeli, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-633e90a8bccd2.jpg",
        "title_no_dia": "Moravsky vrabec, spenat, bramborovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-633e90cb4a2ca.jpg",
        "title_no_dia": "Moravsky vrabec, spenat, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-61dedd472998b.jpg",
        "title_no_dia": "Plzensky gulas, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-61dedd522a807.jpg",
        "title_no_dia": "Plzensky gulas, bramborovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-61dedd5da39d0.jpg",
        "title_no_dia": "Plzensky gulas, varena ryze",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-61dedd7027379.jpg",
        "title_no_dia": "Plzensky gulas, vareny brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-61dedd81bf07e.jpg",
        "title_no_dia": "Plzensky gulas, testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e8580b5eb8b6.jpg",
        "title_no_dia": "Hovezi gulas, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d80e01a32b.jpg",
        "title_no_dia": "Hovezi gulas, bramborovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec41873a7146.jpg",
        "title_no_dia": "Hovezi gulas, varena ryze",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec63f5ddd749.jpg",
        "title_no_dia": "Hovezi gulas, vareny brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f3389fd6cbf9.jpg",
        "title_no_dia": "Hovezi gulas, testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e7f503bbef30.jpg",
        "title_no_dia": "Madarsky gulas, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d81cf94da6.jpg",
        "title_no_dia": "Madarsky gulas, bramborovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec418a943597.jpg",
        "title_no_dia": "Madarsky gulas, varena ryze",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec63f9bde427.jpg",
        "title_no_dia": "Madarsky gulas, vareny brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f3389ecf379a.jpg",
        "title_no_dia": "Madarsky gulas, testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-60e8610956fe3.jpg",
        "title_no_dia": "Veprovy gulas, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-60e86115c08dd.jpg",
        "title_no_dia": "Veprovy gulas, bramborovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-60e861229b650.jpg",
        "title_no_dia": "Veprovy gulas, varena ryze",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-60e8612ba33ec.jpg",
        "title_no_dia": "Veprovy gulas, vareny brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-60e86133563af.jpg",
        "title_no_dia": "Veprovy gulas, testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c892cb34c9.jpg",
        "title_no_dia": "Havelske veprove srdce na smetane, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c8913b22ee.jpg",
        "title_no_dia": "Havelske veprove srdce na smetane, bramborovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c891d48f5f.jpg",
        "title_no_dia": "Havelske veprove srdce na smetane, vareny brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-607c8935199d3.jpg",
        "title_no_dia": "Havelske veprove srdce na smetane, varena ryze",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-6048848bac3e0.jpg",
        "title_no_dia": "Krkonossky gulas, houskove knedliky",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-604940b984ec4.jpg",
        "title_no_dia": "Krkonossky gulas, bramborovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-6048849a243ef.jpg",
        "title_no_dia": "Krkonossky gulas, varena ryze",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-604884a842353.jpg",
        "title_no_dia": "Krkonossky gulas, vareny brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-604884bd370b5.jpg",
        "title_no_dia": "Krkonossky gulas, testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e883c594ed1d.jpg",
        "title_no_dia": "Segedinsky gulas special, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-633e90fc1914a.jpg",
        "title_no_dia": "Segedinsky gulas special, bramborovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e8580c629c5a.jpg",
        "title_no_dia": "Koprova omacka, hovezi maso varene predni, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f436763d5725.jpg",
        "title_no_dia": "Koprova omacka, hovezi maso varene predni, brambory varene",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f84aaac7f9b2.jpg",
        "title_no_dia": "Koprova omacka, vejce varene 2ks, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f84a882e2691.jpg",
        "title_no_dia": "Koprova omacka, vejce varene 2x, brambory varene",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e8580d3943c7.jpg",
        "title_no_dia": "Rajska omacka, hovezi maso varene predni, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e883cef97285.jpg",
        "title_no_dia": "Rajska omacka, hovezi maso varene predni, ryze varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f338a135619d.jpg",
        "title_no_dia": "Rajska omacka, hovezi maso varene predni, testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ea3ee90a9b36.jpg",
        "title_no_dia": "Plneny paprikovy lusk, rajska omacka , houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-60edd0c24c4af.jpg",
        "title_no_dia": "Plneny paprikovy lusk, rajska omacka, varena ryze",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-626a92799a172.jpg",
        "title_no_dia": "Houbova omacka - tmava, hovezi maso zadni, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d8a9020aab.jpg",
        "title_no_dia": "Houbova omacka - tmava, hovezi maso zadni, bramborovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f3389b183695.jpg",
        "title_no_dia": "Houbova omacka - tmava, hovezi maso zadni, testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d89b9c27c5.jpg",
        "title_no_dia": "Houbova omacka - tmava, hovezi maso zadni, vareny brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e7f504ad2464.jpg",
        "title_no_dia": "Hovezi pecene na zampionech, ryze varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5eb97e94d9748.jpg",
        "title_no_dia": "Jitrnicovy prejt, zeli, brambory varene",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ed27523c94eb.jpg",
        "title_no_dia": "Houbova omacka - svetla, hovezi maso predni, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f3389c15bd23.jpg",
        "title_no_dia": "Houbova omacka - svetla, hovezi maso predni, testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e8580e58725f.jpg",
        "title_no_dia": "Bramborove knedliky plnene uzenym masem 2ks, zeli",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ecb97b8dc898.jpg",
        "title_no_dia": "Bramborove knedliky plnene uzenym masem 2ks, spenat",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5fabc52458fb5.jpg",
        "title_no_dia": "Bramborovy knedlik plneny uzenym masem, 1ks, zeli",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5fabc53032e76.jpg",
        "title_no_dia": "Bramborovy knedlik plneny uzenym masem 1ks, spenat",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-6065a78f50c92.jpg",
        "title_no_dia": "Vinna klobasa, vareny brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-6065a6ef2cff0.jpg",
        "title_no_dia": "Vinna klobasa, bramborova kase",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-6065a70633e32.jpg",
        "title_no_dia": "Vinna klobasa, cocka na kyselo, okurka sterilovana",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-60a4c675a5828.jpg",
        "title_no_dia": "Vinna klobasa, hrachova kase s cibulkou, okurka sterilovana",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e7f5188dd040.jpg",
        "title_no_dia": "Cocka na kyselo, uzena veprova plec, okurka sterilovana",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f84a6fae091c.jpg",
        "title_no_dia": "Cocka na kyselo, vejce varene 2ks, okurka sterilovana",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f7c7a3a07ec1.jpg",
        "title_no_dia": "Hrachova kase s cibulkou, uzena veprova plec, okurka sterilovana",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-602f7d0ee3775.jpg",
        "title_no_dia": "Hrachova kase s cibulkou, vejce varene 2ks, okurka sterilovana",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f00419572032.jpg",
        "title_no_dia": "Kureci steak zapeceny, bramborova kase",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f0042a2d1fbb.jpg",
        "title_no_dia": "Kureci steak zapeceny, vareny brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-63ea6eae27606.jpg",
        "title_no_dia": "Kureci steak zapeceny, bramborovy salat",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f84ae6d8c9ee.jpg",
        "title_no_dia": "Kureci spiz, brambory varene",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f84aed34c436.jpg",
        "title_no_dia": "Kureci spiz, bramborova kase",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec40ddc5e570.jpg",
        "title_no_dia": "Cevabcici s cibuli, varene brambory, horcice",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec63def5c7e9.jpg",
        "title_no_dia": "Sekana pecene, bramborova kase",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e8580efd21a0.jpg",
        "title_no_dia": "Sekana pecene, vareny brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5eba4bd9b52a5.jpg",
        "title_no_dia": "Kure pecene, bramborova kase",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ea56fce876d6.jpg",
        "title_no_dia": "Kure pecene, vareny brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ea56fa4586ca.jpg",
        "title_no_dia": "Kure pecene, ryze varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e858111de8fa.jpg",
        "title_no_dia": "Uzena plec, dusene zeli, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f7741a47e183.jpg",
        "title_no_dia": "Uzena plec, dusene zeli, bramborovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e866216bbe95.jpg",
        "title_no_dia": "Uzena plec, spenat, bramborovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d763029fe9.jpg",
        "title_no_dia": "Uzena veprova plec, bramborova kase, okurka sterilovana",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ecb984bdc4a7.jpg",
        "title_no_dia": "Znojemska hovezi pecene, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ecb984459e51.jpg",
        "title_no_dia": "Znojemska hovezi pecene, ryze varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-608c781a57556.jpg",
        "title_no_dia": "Cikanska hovezi pecene, bramborovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-608c782c06025.jpg",
        "title_no_dia": "Cikanska hovezi pecene, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-608c783b09f56.jpg",
        "title_no_dia": "Cikanska hovezi pecene, ryze varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-608c784855c3a.jpg",
        "title_no_dia": "Cikanska hovezi pecene, vareny brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-608c7851d7611.jpg",
        "title_no_dia": "Cikanska hovezi pecene, testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e90542ac5d9a.jpg",
        "title_no_dia": "Zahorsky zavitek z veprove krkovice, brambory varene",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e904c62bc973.jpg",
        "title_no_dia": "Halusky se zelim a uzenym masem",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f61dc1d70b21.jpg",
        "title_no_dia": "Zahorsky zavitek z veprove krkovice, bramborovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e9049d2daed4.jpg",
        "title_no_dia": "Havelska pochoutka, ryze varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ea403d1da4f2.jpg",
        "title_no_dia": "Kureci maso na nudlicky, ryze varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e9050c9e901e.jpg",
        "title_no_dia": "Spanelsky ptacek, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e904ce4dc761.jpg",
        "title_no_dia": "Spanelsky ptacek, ryze varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e98b3c4dc5d2.jpg",
        "title_no_dia": "Veprova po selsku, zeli, bramborovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5fad76c789695.jpg",
        "title_no_dia": "Veprova po selsku, ryze varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec63d9a1376b.jpg",
        "title_no_dia": "Veprova po selsku, bramborova kase, stava",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e905122c64e8.jpg",
        "title_no_dia": "Veprova jatra na cibulce, ryze varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606db175e8475.jpg",
        "title_no_dia": "Veprova jatra na cibulce, vareny brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606da99abf9fa.jpg",
        "title_no_dia": "Veprova jatra na cibulce, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d7a35396fe.jpg",
        "title_no_dia": "Veprova jatra na cibulce, bramborovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e98a2f477b74.jpg",
        "title_no_dia": "Veprova plec na zampionech, ryze varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d82e9da328.jpg",
        "title_no_dia": "Veprova plec na zampionech, testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d83f618d1f.jpg",
        "title_no_dia": "Veprova plec na zampionech, vareny brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d8cfe0e784.jpg",
        "title_no_dia": "Veprova plec na zampionech, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d8493083a7.jpg",
        "title_no_dia": "Veprova plec na zampionech, bramborovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ea3eeafb0d08.jpg",
        "title_no_dia": "Rizoto s kurecim masem, kysela okurka",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e9057be9aed7.jpg",
        "title_no_dia": "Spagety s veprovym masem",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ea6f7488654b.jpg",
        "title_no_dia": "Havelska kapsa",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5eb1dfa0d729b.jpg",
        "title_no_dia": "Josefovy sunkofleky, okurka sterilovana",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ece48ea481a0.jpg",
        "title_no_dia": "Francouzske brambory, okurka sterilovana",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec40e0061cc6.jpg",
        "title_no_dia": "Veprove maso dusene v mrkvi, varene brambory",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ec4f7a07864e.jpg",
        "title_no_dia": "Veprove maso na paprice, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f338a29d2058.jpg",
        "title_no_dia": "Veprove maso na paprice, testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5fb15ec6c13a9.jpg",
        "title_no_dia": "Kureci maso na paprice, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5fb15ed43fb82.jpg",
        "title_no_dia": "Kureci maso na paprice, testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ee618bf15e5c.jpg",
        "title_no_dia": "Krenova omacka, hovezi maso varene zadni, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ee618c5ae98d.jpg",
        "title_no_dia": "Krenova omacka, uzena veprova plec, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ece47a70253d.jpg",
        "title_no_dia": "Mexicke fazole",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e8985e455675.jpg",
        "title_no_dia": "Svickova omacka, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e898700d2f91.jpg",
        "title_no_dia": "Koprova omacka, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e89862a53eac.jpg",
        "title_no_dia": "Rajska omacka, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e89b8dbf095a.jpg",
        "title_no_dia": "Rajska omacka, ryze varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-6034e2741951c.jpg",
        "title_no_dia": "Rajska omacka, testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5e8987f7ecdca.jpg",
        "title_no_dia": "Houbova omacka - tmava, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d8eba15147.jpg",
        "title_no_dia": "Houbova omacka - tmava, bramborovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f3389d592718.jpg",
        "title_no_dia": "Houbova omacka - tmava, testoviny",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d85f5795cb.jpg",
        "title_no_dia": "Houbova omacka - tmava, ryze varena",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-606d8deabe1c7.jpg",
        "title_no_dia": "Houbova omacka - tmava, vareny brambor",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5ed276209e729.jpg",
        "title_no_dia": "Houbova omacka - svetla, houskovy knedlik",
    },
    {
        "category": "hlavni_jidla",
        "imgsource": "image-5f3389e0dddbf.jpg",
        "title_no_dia": "Houbova omacka - svetla, testoviny",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5eb97d8401d18.jpg",
        "title_no_dia": "Smazeny kureci rizek, bramborova kase",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e8241cdafc40.jpg",
        "title_no_dia": "Smazeny kureci rizek, salat bramborovy",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e85813fb2e19.jpg",
        "title_no_dia": "Smazeny kureci rizek, brambory varene",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5eca2adab89fd.jpg",
        "title_no_dia": "Smazeny veprovy rizek, bramborova kase",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e8241c0ee609.jpg",
        "title_no_dia": "Smazeny veprovy rizek, salat bramborovy",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e7f51d55a528.jpg",
        "title_no_dia": "Smazeny veprovy rizek, brambory varene",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ece4bd329e86.jpg",
        "title_no_dia": "Smazeny syr Gouda 48%, bramborova kase",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e85814a34341.jpg",
        "title_no_dia": "Smazeny syr Gouda 48%, brambory varene",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ece4963ef01d.jpg",
        "title_no_dia": "Smazeny syr Hermelin, bramborova kase",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e905276aa685.jpg",
        "title_no_dia": "Smazeny syr Hermelin, brambory varene",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ed0c45ef2cc4.jpg",
        "title_no_dia": "Smazene rybi file, bramborova kase",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ea3efbb7b915.jpg",
        "title_no_dia": "Smazene rybi file, salat bramborovy",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ea3efac46d0c.jpg",
        "title_no_dia": "Smazene rybi file , brambory varene",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5f006370ba890.jpg",
        "title_no_dia": "Smazeny kvetak, bramborova kase",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e98b2162c9b0.jpg",
        "title_no_dia": "Smazeny kvetak, brambory varene",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-628230bcebb67.jpg",
        "title_no_dia": "Smazeny kvetak, brambory varene, tatarska omacka",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-60d9b95be9b96.jpg",
        "title_no_dia": "Smazena brokolice, bramborova kase",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-60d9b99289938.jpg",
        "title_no_dia": "Smazena brokolice, brambory varene",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ecb9813d60d1.jpg",
        "title_no_dia": "Smazeny karbanatek, bramborova kase",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ed3920c37294.jpg",
        "title_no_dia": "Smazeny karbanatek, bramborovy salat",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ecb9824a5535.jpg",
        "title_no_dia": "Smazeny karbanatek, vareny brambor",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5f0055d975c78.jpg",
        "title_no_dia": "Ondruv Holandsky rizek, bramborova kase",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e91aaec68626.jpg",
        "title_no_dia": "Ondruv Holandsky rizek, brambory varene",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ece4c24d1e46.jpg",
        "title_no_dia": "Smazene zampiony, kase bramborova",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5ed24c5c6ba9d.jpg",
        "title_no_dia": "Smazene zampiony, bramborovy salat",
    },
    {
        "category": "smazena_jidla",
        "imgsource": "image-5e98a27d3b87c.jpg",
        "title_no_dia": "Smazene zampiony, brambory varene",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60af53787d9ae.jpg",
        "title_no_dia": "Jablkova zemlovka",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5e7f53562815d.jpg",
        "title_no_dia": "Dukatove buchticky s vanilkovym kremem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-626a3f6917391.jpg",
        "title_no_dia": "Bramborove sisky, mak, maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc7d4be3bd.jpg",
        "title_no_dia": "Bramborove sisky, sypany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc80c741e7.jpg",
        "title_no_dia": "Bramborove sisky, slehany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-606f8a850dc42.jpg",
        "title_no_dia": "Bramborove sisky, skorice, cukr, maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-606f8b08568dd.jpg",
        "title_no_dia": "Testoviny, strouhany tvaroh, maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-606f8b74ea822.jpg",
        "title_no_dia": "Testoviny, mak, cukr, maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-606f71cbd625a.jpg",
        "title_no_dia": "Kynuty blboun plneny povidly, vanilkovy krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-606f7196b085b.jpg",
        "title_no_dia": "Kynuty blboun plneny povidly, mak, cukr, maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60741b74c62ff.jpg",
        "title_no_dia": "Kynuty blboun plneny povidly, slehany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-606f70ac0aae0.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - jablko, skorice, cukr, maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-6071a6633cb26.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - jablko, vanilkovy krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-6071a66d07230.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - jablko, sypany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-6071a659381c8.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - jablko, slehany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702426dcf70.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - jahoda, vanilkovy krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff5f58e9f1.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - jahoda, sypany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff64eb20e4.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - jahoda, slehany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff68a408f3.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - jahoda, mak, maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff60d7e087.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - merunka, sypany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff66e20739.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - merunka, slehany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff6a70b0f0.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - merunka, mak, maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702444a56dc.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - malina, vanilkovy krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff601539a3.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - malina, sypany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff6624075a.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - malina, slehany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff69a40ebc.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - malina, mak, maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-6070245928030.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - svestka, vanilkovy krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff6192186c.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - svestka, sypany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff67d8d5ba.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - svestka, slehany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f8ff6b202639.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - svestka, mak, maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702469568e2.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - boruvka, vanilkovy krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f95e72e95223.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - boruvka, sypany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f95e724547e2.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - boruvka, slehany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f95e717b2b37.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - boruvka, mak, maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702cda2db79.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - ostruzina, vanilkovy krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702cecd6637.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - ostruzina, sypany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702cfe255c4.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - ostruzina, slehany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702d0736201.jpg",
        "title_no_dia": "Ovocne knedliky 2ks - ostruzina, mak, maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607ff502d20dd.jpg",
        "title_no_dia": "Bramborove knedliky svestkove 4ks, sypany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607ff50cca110.jpg",
        "title_no_dia": "Bramborove knedliky svestkove 4ks, slehany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607ff51c4ec46.jpg",
        "title_no_dia": "Bramborove knedliky svestkove 4ks, mak, maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-606f7112c3548.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - jablko, skorice, cukr, maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-6071a63b16bb4.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - jablko, vanilkovy krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-6071a646a919f.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - jablko, sypany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-6071a6324587b.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - jablko, slehany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607028ab4f463.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - jahoda, vanilkovy krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc334c86a5.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - jahoda, sypany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc38eb8e4a.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - jahoda, slehany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc4308649c.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - jahoda, mak, maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607028b883aad.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - merunka, vanilkovy krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc35fc843a.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - merunka, sypany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc3d0a3a4e.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - merunka, slehany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc45490c87.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - merunka, mak, maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607028c867513.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - malina, vanilkovy krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc351dc9d7.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - malina, sypany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc3de54ce7.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - malina, slehany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc44586068.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - malina, mak, maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607028d81cf14.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - svestka, vanilkovy krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc36cf318c.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - svestka, sypany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc3e793bb7.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - svestka, slehany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc46145b82.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - svestka, mak, maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607028e7e0ee8.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - boruvka, vanilkovy krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc3216ca82.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - boruvka, sypany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc37cceacb.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - boruvka, slehany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5fabc41b70cbd.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - boruvka, mak, maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702e371a9b4.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - ostruzina, vanilkovy krem",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702e4775c78.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - ostruzina, sypany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702e54c485b.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - ostruzina, slehany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60702e645be77.jpg",
        "title_no_dia": "Ovocny knedlik 1ks - ostruzina, mak, maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607ef4db64d76.jpg",
        "title_no_dia": "Bramborove knedliky svestkove 2ks, sypany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607ef4eda106b.jpg",
        "title_no_dia": "Bramborove knedliky svestkove 2ks, slehany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-607ef504c6d89.jpg",
        "title_no_dia": "Bramborove knedliky svestkove 2ks, mak, maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5e8241917f35c.jpg",
        "title_no_dia": "Ovocne knedliky, sypany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5e824168e07ef.jpg",
        "title_no_dia": "Ovocne knedliky, slehany tvaroh",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-5f0051a6b701c.jpg",
        "title_no_dia": "Ovocny knedlik, mak, maslo",
    },
    {
        "category": "sladka_jidla",
        "imgsource": "image-60c23ced4c111.jpg",
        "title_no_dia": "Jahodova pochoutka",
    },
]


output_list = []
output_list2 = []

for item in input_dict:
    for item2 in input_dict2:
        if item["imgsource"] == item2["imgsource"]:
            new_item = dict(item)
            new_item["title_curred"] = item2["title_curred"]
            output_list.append(new_item)

for item in output_list:
    for item2 in input_dict3:
        if item["imgsource"] == item2["imgsource"]:
            new_item = dict(item)
            new_item["title_no_dia"] = item2["title_no_dia"]
            output_list2.append(new_item)


print(output_list2)

with open("test2.json", "w", encoding="utf-8") as file:
    json.dump(output_list2, file, ensure_ascii=False)
