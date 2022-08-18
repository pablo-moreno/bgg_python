from boardgg.tests.mocks import MockedResponse


def search_boardgame(*args, **kwargs):
    return MockedResponse(
        data='<boardgames termsofuse="https://boardgamegeek.com/xmlapi/termsofuse">\n\t\t\t<boardgame objectid="173346">\n\t\t\t<name primary="true">7 Wonders Duel</name>\t\t\t\n\t\t\t\t\t\t\t<yearpublished>2015</yearpublished>\n\t\t\t\t\t</boardgame>\n\t\t\t<boardgame objectid="274383">\n\t\t\t<name primary="true">7 Wonders Duel Leaders (fan expansion)</name>\t\t\t\n\t\t\t\t\t\t\t<yearpublished>2019</yearpublished>\n\t\t\t\t\t</boardgame>\n\t\t\t<boardgame objectid="309116">\n\t\t\t<name primary="true">7 Wonders Duel: Agora</name>\t\t\t\n\t\t\t\t\t\t\t<yearpublished>2020</yearpublished>\n\t\t\t\t\t</boardgame>\n\t\t\t<boardgame objectid="348601">\n\t\t\t<name primary="true">7 Wonders Duel: Agora \xe2\x80\x93 Tu Quoque Fili promo card</name>\t\t\t\n\t\t\t\t\t\t\t<yearpublished>2021</yearpublished>\n\t\t\t\t\t</boardgame>\n\t\t\t<boardgame objectid="202976">\n\t\t\t<name primary="true">7 Wonders Duel: Pantheon</name>\t\t\t\n\t\t\t\t\t\t\t<yearpublished>2016</yearpublished>\n\t\t\t\t\t</boardgame>\n\t\t\t<boardgame objectid="310215">\n\t\t\t<name primary="true">7 Wonders Duel: Solo</name>\t\t\t\n\t\t\t\t\t\t\t<yearpublished>2020</yearpublished>\n\t\t\t\t\t</boardgame>\n\t\t\t<boardgame objectid="196339">\n\t\t\t<name primary="true">7 Wonders Duel: Statue of Liberty</name>\t\t\t\n\t\t\t\t\t\t\t<yearpublished>2016</yearpublished>\n\t\t\t\t\t</boardgame>\n\t\t\t<boardgame objectid="186069">\n\t\t\t<name primary="true">7 Wonders Duel: The Messe Essen Promo Card</name>\t\t\t\n\t\t\t\t\t\t\t<yearpublished>2015</yearpublished>\n\t\t\t\t\t</boardgame>\n\t</boardgames>\n',
        status_code=200,
    )


def retrieve_boardgame(*args, **kwargs):
    return MockedResponse(
        data='<boardgames termsofuse="https://boardgamegeek.com/xmlapi/termsofuse">\n\t\t\t\t\t<boardgame objectid="173346">\n\t\t\t<yearpublished>2015</yearpublished>\n\t\t\t<minplayers>2</minplayers>\n\t\t\t<maxplayers>2</maxplayers>\n\t\t\t<playingtime>30</playingtime>\n\t\t\t<minplaytime>30</minplaytime>\n\t\t\t<maxplaytime>30</maxplaytime>\n\t\t\t<age>10</age>\n\n\t\t\t\t\t\t\t<name  sortindex="1">7 Csoda P\xc3\xa1rbaj</name>\n\t\t\t\t\t\t\t<name  sortindex="1">7 Cud\xc3\xb3w \xc5\x9awiata: Pojedynek</name>\n\t\t\t\t\t\t\t<name  sortindex="1">7 Div\xc5\xaf sv\xc4\x9bta: Duel</name>\n\t\t\t\t\t\t\t<name primary="true" sortindex="1">7 Wonders Duel</name>\n\t\t\t\t\t\t\t<name  sortindex="1">7 \xd0\xa7\xd1\x83\xd0\xb4\xd0\xb5\xd1\x81: \xd0\x94\xd1\x83\xd1\x8d\xd0\xbb\xd1\x8c</name>\n\t\t\t\t\t\t\t<name  sortindex="1">7 \xe0\xb8\xaa\xe0\xb8\xb4\xe0\xb9\x88\xe0\xb8\x87\xe0\xb8\xa1\xe0\xb8\xab\xe0\xb8\xb1\xe0\xb8\xa8\xe0\xb8\x88\xe0\xb8\xa3\xe0\xb8\xa3\xe0\xb8\xa2\xe0\xb9\x8c \xe0\xb8\x94\xe0\xb8\xa7\xe0\xb8\xa5</name>\n\t\t\t\t\t\t\t<name  sortindex="1">7 \xec\x9b\x90\xeb\x8d\x94\xec\x8a\xa4 \xeb\x8c\x80\xea\xb2\xb0</name>\n\t\t\t\t\t\t\t<name  sortindex="1">\xe4\xb8\x83\xe5\xa4\xa7\xe5\xa5\x87\xe8\xb9\x9f \xe5\xb0\x8d\xe6\xb1\xba</name>\n\t\t\t\t\t\t\t<name  sortindex="1">\xe4\xb8\x83\xe5\xa4\xa7\xe5\xa5\x87\xe8\xbf\xb9:\xe5\xaf\xb9\xe5\x86\xb3</name>\n\t\t\t\t\t\t\t<name  sortindex="1">\xe4\xb8\x83\xe5\xa4\xa7\xe5\xa5\x87\xe8\xbf\xb9\xef\xbc\x9a\xe5\xaf\xb9\xe5\x86\xb3</name>\n\t\t\t\t\t\t\t<name  sortindex="1">\xe4\xb8\x83\xe5\xa4\xa7\xe5\xaf\xb9\xe5\x86\xb3</name>\n\t\t\t\t\t\t\t<name  sortindex="1">\xe4\xb8\x96\xe7\x95\x8c\xe3\x81\xae\xe4\xb8\x83\xe4\xb8\x8d\xe6\x80\x9d\xe8\xad\xb0:\xe3\x83\x87\xe3\x83\xa5\xe3\x82\xa8\xe3\x83\xab</name>\n\t\t\t\t\t\t\t\t\t\n\t\t\t<description></description>\n\n\t\t\t\t\t\t\t<thumbnail>https://noesiten.jpg</thumbnail>\n\t\t\t\t<image>https://noesiten.jpg</image>\n\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t<boardgameaccessory objectid="333853">7 Wonders Duel + Pantheon + Agora: Eurohell Design Insert</boardgameaccessory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameaccessory objectid="334636">7 Wonders Duel: reDrewno Insert</boardgameaccessory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepublisher objectid="4384">Repos Production</boardgamepublisher>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="171077">#11: 2015, A Year in Review</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="420622">#26 - Did Jack Get Off?</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="192970">#34: Double Six-Pack Review! 7 Wonders Duel &amp;amp; Agamemnon; 7 Wonders on Tap; iOS game reviews</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="198575">#39: Two Player Games six-pack; Citrus on tap; Isle of Skye &amp;amp; Avenue</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="312013">029 \xe2\x80\x93 Card Drafting Mechanic \xe2\x80\x93 Part 2</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="168899">2-Player Board Games Review Special</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="61767">2015 Board Game Quest Awards Best Card Game Nominee</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="61779">2015 Board Game Quest Awards Best Card Game Winner</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="34501">2015 Golden Geek Best 2-Player Board Game Nominee</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="34776">2015 Golden Geek Best 2-Player Board Game Winner</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="34503">2015 Golden Geek Best Card Game Nominee</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="34778">2015 Golden Geek Best Card Game Winner</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="34510">2015 Golden Geek Best Strategy Board Game Nominee</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="34500">2015 Golden Geek Board Game of the Year Nominee</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="38070">2015 Jocul Anului \xc3\xaen Rom\xc3\xa2nia Beginners Finalist</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="65408">2015 Jocul Anului \xc3\xaen Rom\xc3\xa2nia Beginners Winner</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="37315">2015 Meeples&#039; Choice Nominee</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="34948">2015 Swiss Gamers Award Winner</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="35458">2015 Tric Trac d&#039;Or Winner</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="35457">2015 Tric Trac Nominee</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="35436">2016 As d&#039;Or - Jeu de l&#039;Ann\xc3\xa9e Expert Nominee</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="63957">2016 Fairplay \xc3\x80 la carte Winner</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="48616">2016 Gioco dell\xe2\x80\x99Anno Nominee</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="64051">2016 Gra Roku Advanced Game of the Year Nominee</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="37770">2016 International Gamers Award - General Strategy: Two-players Nominee</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="37772">2016 International Gamers Award - General Strategy: Two-players Winner</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="65399">2016 Juego del A\xc3\xb1o Recommended</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="35995">2016 Kennerspiel des Jahres Recommended</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="65353">2016 Lys Passion\xc3\xa9 Finalist</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamehonor objectid="64115">2017 Hra roku Winner</boardgamehonor>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="426824">244 - 7 Wonders Duel</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="284339">64. DDP Lots of Board Games Again: Architects of the West Kingdom, Clank In Space, Die hard</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<videogamebg objectid="289722">7 Wonders Duel</videogamebg>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameaccessory objectid="354399">7 Wonders Duel + Pantheon + Agora: Folded Space Insert</boardgameaccessory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameaccessory objectid="347408">7 Wonders Duel + Pantheon + Agora: Game Tamer organizer</boardgameaccessory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameaccessory objectid="333852">7 Wonders Duel + Pantheon: Eurohell Design Insert</boardgameaccessory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameaccessory objectid="291721">7 Wonders Duel + Pantheon: Folded Space Insert</boardgameaccessory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameexpansion objectid="274383">7 Wonders Duel Leaders (fan expansion)</boardgameexpansion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameexpansion objectid="309116">7 Wonders Duel: Agora</boardgameexpansion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameaccessory objectid="207907">7 Wonders Duel: Broken Token Organizer</boardgameaccessory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameaccessory objectid="309490">7 Wonders Duel: e-Raptor Insert</boardgameaccessory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameaccessory objectid="336659">7 Wonders Duel: Eurohell Design Insert</boardgameaccessory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameaccessory objectid="347023">7 Wonders Duel: Gold, silver and bronze Conflict pawns</boardgameaccessory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameaccessory objectid="271935">7 Wonders Duel: Insert Here Insert</boardgameaccessory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameaccessory objectid="306199">7 Wonders Duel: Laserox Dueling Wonders Organizer</boardgameaccessory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameaccessory objectid="219880">7 Wonders Duel: Metal Coins</boardgameaccessory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameaccessory objectid="186070">7 Wonders Duel: Metal Conflict Pawn</boardgameaccessory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameexpansion objectid="202976">7 Wonders Duel: Pantheon</boardgameexpansion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameaccessory objectid="255878">7 Wonders Duel: Sagrada Familia</boardgameaccessory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameexpansion objectid="310215">7 Wonders Duel: Solo</boardgameexpansion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameexpansion objectid="196339">7 Wonders Duel: Statue of Liberty</boardgameexpansion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameaccessory objectid="228690">7 Wonders Duel: Stonehenge</boardgameaccessory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameaccessory objectid="348618">7 Wonders Duel: The GiftForge Insert</boardgameaccessory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameexpansion objectid="186069">7 Wonders Duel: The Messe Essen Promo Card</boardgameexpansion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameaccessory objectid="272265">7 Wonders Duel: Tower Rex Organizer</boardgameaccessory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="177456">7LandHand: Episode 65 \xe2\x80\x93 7 Wonders Duel</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="399233">88 \xe2\x80\x93 The Game Design Process of Bruno Cathala</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="295672">Ad Libs &amp;amp; Mad Fibs</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepublisher objectid="23043">ADC Blackfire Entertainment</boardgamepublisher>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamecategory objectid="1050">Ancient</boardgamecategory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamefamily objectid="27524">Ancient: Babylon</boardgamefamily>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamefamily objectid="72535">Ancient: Egypt</boardgamefamily>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamefamily objectid="52373">Ancient: Greece</boardgamefamily>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepublisher objectid="47848">Asmodee China</boardgamepublisher>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepublisher objectid="42032">Asmodee Italia</boardgamepublisher>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepublisher objectid="15889">Asterion Press</boardgamepublisher>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="175397">ba001 \xe2\x80\x93 Von \xe2\x80\x98Das ist Sparta!\xe2\x80\x99 bis \xe2\x80\x98Ich bin dann mal weg\xe2\x80\x99</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamedesigner objectid="9714">Antoine Bauza</boardgamedesigner>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="169936">Best Board Games of 2015 Awards Spectacular</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="158473">BGA Ep 83 - Top Ten Games that Bumped Other Games from Our Shelves</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="208726">BGA Episode 122: Top 10 Two Player Games</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="182491">Breaking Bad....Medicine - Part 2</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamecategory objectid="1002">Card Game</boardgamecategory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="420370">Cardboard Time Episode 27 - The 1 Year Anniversary Episode!</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="220560">Carson City, Best Games to Play While Traveling - Boards &amp;amp; Swords #77</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamedesigner objectid="1727">Bruno Cathala</boardgamedesigner>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="374197">Chinese edition 2015</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="558587">Chinese edition 2020</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamecategory objectid="1029">City Building</boardgamecategory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamecategory objectid="1015">Civilization</boardgamecategory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameartist objectid="12016">Miguel Coimbra</boardgameartist>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="164014">Cult of the New Board Game Podcast 004 \xe2\x80\x93 Essen 2015 Diary!</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="164903">Cult of the New Board Game Podcast 005 \xe2\x80\x93 7 Wonders vs Nevermore</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="170157">Cult of the New Board Game Podcast Episode 009 \xe2\x80\x93 Top 10 Games of 2015</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="332231">Czech edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="603529">Czech edition 2021</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamefamily objectid="70360">Digital Implementations: Board Game Arena</boardgamefamily>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="206074">Dirk Gently, Ghost Recon Wildlands, The Battle of Polytopia and 7 Wonders Duel - Ep27</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="336145">Dutch-only edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="326707">Dutch/English/Korean edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="288074">Dutch/English/Spanish edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamecategory objectid="1021">Economic</boardgamecategory>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="599189">English-only edition 2016 R10</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="591175">English-only edition 2016 R6</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="422327">English-only edition 2016 R7</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="620933">English-only edition 2016 R9</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="484266">English-only edition 2019, first printing</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="526264">English-only edition 2019, second printing</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="559421">English-only edition 2020</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="594224">English-only edition 2021</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="266502">English-only first edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="441367">English-only third edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="290902">English/Japanese edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="423307">English/Korean edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="164424">Ep 012 \xe2\x80\x93 Essen 2015 Highlights Show</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="166969">Ep 016 \xe2\x80\x93 BGG Con 2015 Recap Extravaganza!!</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="182502">Ep 035 \xe2\x80\x93 Spiel des Jahres predictions and discussion</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="183386">Ep 036 &amp;ndash; BGG Spring Con &amp;amp; Spiel des Jahres 2016 Nominees</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="252168">Ep 070 &amp;ndash; 3rd Anniversary Special &amp;amp; Tournament to the Death!!!</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="301287">Ep 13- Top 3 Con Games &amp;amp; TTS Con Recap</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="170029">Ep 34 Drama</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="227767">Ep. 10: PacifiCon Game Expo</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="174331">Episode #222 - The Spiel on 7 Wonders: Duel</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="227754">Episode #22: Cooperative Games</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="227739">Episode #37: Card Drafting Games</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="227738">Episode #38: Two Player Games</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="174335">Episode 03: Gaming On Valentine&#039;s Day</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="179403">Episode 10 Akrotiri &amp;amp; 7 Wonders Duel</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="229606">Episode 11: Two Player Games</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="230242">Episode 11: Two Players</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="199090">Episode 13: The one about our top 10 2-player games</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="168548">Episode 14 - Le Havre Review</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="391320">Episode 145 :: Joy of the Stick</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="370408">Episode 14: Bruno Cathala</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="169938">Episode 17:  Mysterium Review - Christmas Song - Giveaway - Christmas Wishes</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="171213">Episode 18: Codenames Review - Games of the Year - Giveaways</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="194598">Episode 192</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="168553">Episode 23: Bloody Scotland</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="199154">Episode 34 - 7 Wonders Duel and Giveaway Results</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="241214">Episode 35: Sakura, 1960: The Making of the President, Pit Crew, 7 Wonders Duel, Citrus</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="174327">Episode 41: The 7 Wonders Episode: From Base to Duel!</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="195640">Episode 42 :: Board Game of the Year 2016 - Brawling Brothers Awards</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="223663">Episode 53 - Revisiting Our Top 10 Two-Player Games</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="157913">Episode 54- GenCon 2015 and La Granja (Plus a CONTEST!)</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="213602">Episode 58 :: Codenames Duet Review + Kingdomino Review</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="433306">Episode 5: Bruno Cthulhu</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="260592">Episode 63 - A Variety of Victories</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="227236">Episode 65 :: Raiders of the North Sea Review - Secret Santa</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="240564">Episode 73 :: Castell Review + Top Board Games according to BGG Rankings</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="182515">Episode 73- Two Player Games</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="241767">Episode 74 :: Our Favorite Board Games (21-50) + Origins Meetup Discussion</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="206268">Episode 75 - Interview with Cephalofair Games Isaac Childres</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="267176">Episode 89 :: The Re-Envisioning</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="281299">Episode 9 - Root, Top 5 Games We Play with our Wives, &amp;amp; Contest Time</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="360736">Episode 9: Fugitive, Pandemic Legacy: Season 1, Orleans</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="205870">Episode Eight - 7 Wonders: Duel, Yokohama, Deception: Murder in Hong Kong</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="170060">Favorite Games of 2015</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="266501">French edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepublisher objectid="15605">Gal\xc3\xa1pagos Jogos</boardgamepublisher>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamefamily objectid="17552">Game: 7 Wonders</boardgamefamily>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamefamily objectid="39540">Game: 7 Wonders Duel</boardgamefamily>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="170384">Garrett&#039;s Games 497 - Three new 2-player-only releases</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<commerceweblink objectid="305624">Geek Game Shop listing for 7 Wonders Duel</commerceweblink>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepublisher objectid="8820">G\xc3\xa9m Klub Kft.</boardgamepublisher>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="157195">GenCon 2015 - Cathala and Bauza</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="266503">German first edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="339356">German second edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="558031">German third edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="316509">Greek edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="174089">GrogCast Season 3, Episode Two-o!</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="172962">GrogCast Season 3, Episode Uno!</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="194522">HLG 13: Terugblik op 2016</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="206078">Holidays in Paris, Escaping from Aliens, and Fancy Names - Ep23</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="333351">Hungarian edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="288317">Italian first edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="389078">Italian second edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="564473">Italian third edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="227730">It\xe2\x80\x99s Our Turn! Episode #45: Ancient Era Games</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepublisher objectid="9634">KADABRA</boardgamepublisher>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepublisher objectid="6214">Kaissa Chess &amp; Games</boardgamepublisher>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepublisher objectid="8291">Korea Boardgames Co., Ltd.</boardgamepublisher>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="498260">Korean-only edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepublisher objectid="3218">Lautapelit.fi</boardgamepublisher>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamemechanic objectid="3001">Layering</boardgamemechanic>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepublisher objectid="9325">Lifestyle Boardgames Ltd</boardgamepublisher>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="162592">Low Player Count - Ep 13 - Luck in Games</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="168788">Low Player Count - Ep 17 - Replayability</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="177179">Low Player Count - Ep 24 - Card Drafting</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="174498">Low Player Count - Ep. 21 - Our Top 5 Two Player Games</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="150416">Low Player Count - Ep. 6 - Mano a Mano: Co-op or Competitive</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="152297">Low Player Count - Ep. 7 - The Good, The Bad, and the Dummy</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepublisher objectid="30399">Ludicus</boardgamepublisher>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="337458">M\xc3\xa5l og Point</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamefamily objectid="27646">Mechanism: Tableau Building</boardgamefamily>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="210009">MeepleCore Podcast Episode 32 - SNES Classic, GenCon Math Trade Debacle, Top Disney Movies, and more!</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="166632">MN 0084 Holiday Gift Guide 2015</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="184347">MN 0117 Even More Two Player Games</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="205419">MN 0162 International Tabletop Day 2017 and Clank! Sunken Treasures</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="318316">Nordic edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamemechanic objectid="2041">Open Drafting</boardgamemechanic>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="305369">Out of the Dust Ep48 - 7 Wonders Duel, Hadara, and Catan Rise of the Inkas</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="166294">Perfect Information Episode 6 - Echo chamber</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamefamily objectid="65851">Players: Games with expansions that add solo play</boardgamefamily>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamefamily objectid="61979">Players: Two Player Only Games</boardgamefamily>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="184323">Podcast EP02 \xe2\x80\x93 Recommandations de jeux \xc3\xa0 2 joueurs</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="191473">Podcast EP10 \xe2\x80\x93 Top 10 jeux de soci\xc3\xa9t\xc3\xa9</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="194356">Podcast EP13 \xe2\x80\x93 Suggestions de cadeaux de No\xc3\xabl</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="612653">Polish edition 2019</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="278388">Polish first edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepublisher objectid="31904">Ponva d.o.o.</boardgamepublisher>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="348109">Portuguese edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepublisher objectid="36366">Pridemage Games</boardgamepublisher>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepublisher objectid="7466">Rebel Sp. z o.o.</boardgamepublisher>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="333004">Romanian edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="331603">Russian edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="407829">Serbian/Slovenian/Croatian edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamemechanic objectid="2004">Set Collection</boardgamemechanic>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepublisher objectid="33998">Siam Board Games</boardgamepublisher>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepublisher objectid="32645">Sombreros Production</boardgamepublisher>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="320839">Spanish-only edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamesubdomain objectid="5497">Strategy Games</boardgamesubdomain>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamemechanic objectid="2884">Sudden Death Ending</boardgamemechanic>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="212865">TGT 054: Gaming Trends</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="242724">TGT 094: Dueling Games</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="492145">Thai edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="173829">The Game Pit - Episode 56 - The Bumper Review of 2015 (with Top 5s)</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="161546">The Game Pit: Episode 49 - Treasure Hunt Essen 2015 Part 1</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="164260">The Game Pit: Episode 54 - Essen 2015 - The Good, The Bad and The Surprising</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="220834">The Long View of 7 Wonders with the Hexagamers</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamemechanic objectid="2888">Tug of War</boardgamemechanic>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="431609">Ukrainian/Bulgarian/Korean edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameversion objectid="562735">Ukrainian/Latvian/Lithuanian/Estonian edition</boardgameversion>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamemechanic objectid="2015">Variable Player Powers</boardgamemechanic>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamefamily objectid="62276">Versions &amp; Editions: Two-Player Versions of More-Player Games</boardgamefamily>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="176592">Vox Republica 113: Sentinels of the Kickstarterverse</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="162213">What Did You Play This Week Podcast Thing Week 43!!! All By Myself</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="168230">What Did You Play This Week Podcast Thing Week 53 Ft Derek Davis, Patrick Hillier, Ray Shell and Kerensa and I!!!</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="168787">What Did You Play This Week Podcast Thing Week 54!!!!</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="169413">What Did You Play This Week Podcast Thing Week 55!!! T.I.M.E Stories(Spoiler Free)</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepodcastepisode objectid="170386">What Did You Play This Week Podcast Thing Week 58!!!</boardgamepodcastepisode>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgamepublisher objectid="44209">\xd0\x86\xd0\xb3\xd1\x80\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xb3</boardgamepublisher>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<boardgameimplementation objectid="68448" inbound="true">7 Wonders</boardgameimplementation>\n\t\t\t\t\t\t\n\t\t\t<poll name="suggested_numplayers" title="User Suggested Number of Players" totalvotes="987">\n\t\t\t\n\t\t<results numplayers="1">\t\t\n\t\t\t\t\t<result value="Best" numvotes="9" />\n\t\t\t\t\t<result value="Recommended" numvotes="57" />\n\t\t\t\t\t<result value="Not Recommended" numvotes="719" />\n\t\t\t\t</results>\t\t\t\t\t\n\t\t\t\n\t\t<results numplayers="2">\t\t\n\t\t\t\t\t<result value="Best" numvotes="954" />\n\t\t\t\t\t<result value="Recommended" numvotes="22" />\n\t\t\t\t\t<result value="Not Recommended" numvotes="3" />\n\t\t\t\t</results>\t\t\t\t\t\n\t\t\t\n\t\t<results numplayers="2+">\t\t\n\t\t\t\t\t<result value="Best" numvotes="5" />\n\t\t\t\t\t<result value="Recommended" numvotes="5" />\n\t\t\t\t\t<result value="Not Recommended" numvotes="753" />\n\t\t\t\t</results>\t\t\t\t\t\n\t</poll>\n\n\t\t\t<poll name="language_dependence" title="Language Dependence" totalvotes="91">\n\t\t\t\n\t\t<results>\t\t\n\t\t\t\t\t<result level="1" value="No necessary in-game text" numvotes="83" />\n\t\t\t\t\t<result level="2" value="Some necessary text - easily memorized or small crib sheet" numvotes="8" />\n\t\t\t\t\t<result level="3" value="Moderate in-game text - needs crib sheet or paste ups" numvotes="0" />\n\t\t\t\t\t<result level="4" value="Extensive use of text - massive conversion needed to be playable" numvotes="0" />\n\t\t\t\t\t<result level="5" value="Unplayable in another language" numvotes="0" />\n\t\t\t\t</results>\t\t\t\t\t\n\t</poll>\n\n\t\t\t<poll name="suggested_playerage" title="User Suggested Player Age" totalvotes="282">\n\t\t\t<results>\t\t\n\t\t\t\t\t<result value="2" numvotes="0" />\n\t\t\t\t\t<result value="3" numvotes="0" />\n\t\t\t\t\t<result value="4" numvotes="0" />\n\t\t\t\t\t<result value="5" numvotes="2" />\n\t\t\t\t\t<result value="6" numvotes="3" />\n\t\t\t\t\t<result value="8" numvotes="81" />\n\t\t\t\t\t<result value="10" numvotes="126" />\n\t\t\t\t\t<result value="12" numvotes="60" />\n\t\t\t\t\t<result value="14" numvotes="9" />\n\t\t\t\t\t<result value="16" numvotes="1" />\n\t\t\t\t\t<result value="18" numvotes="0" />\n\t\t\t\t\t<result value="21 and up" numvotes="0" />\n\t\t\t\t</results>\t\t\t\t\t\n\t</poll>\n\n\n\t\t\t\n\t\t\t\n\t\t\t\n\t\t\n\t\t\t\t\n\t\t</boardgame>\n\t</boardgames>\n'
    )


def boardgame_not_found(*args, **kwargs):
    return MockedResponse(
        data="",
        status_code=404,
    )