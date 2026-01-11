import json
import random

# BATCH 1: GEOGRAPHY - 100 questions per level
# Easy: Major capitals, famous rivers, well-known countries
# Medium: Regional capitals, less famous geography
# Hard: Obscure capitals, technical geography facts

def create_batch1_geography():
    """100 questions per level on Geography"""
    
    # LEVEL 1 - EASY GEOGRAPHY (100 questions)
    easy_geo = []
    
    # Capitals (50 questions)
    capitals_easy = [
        ("France", "Paris"), ("Germany", "Berlin"), ("Italy", "Rome"), ("Spain", "Madrid"),
        ("UK", "London"), ("Japan", "Tokyo"), ("China", "Beijing"), ("India", "New Delhi"),
        ("USA", "Washington D.C."), ("Canada", "Ottawa"), ("Russia", "Moscow"), ("Brazil", "Brasilia"),
        ("Australia", "Canberra"), ("Egypt", "Cairo"), ("Mexico", "Mexico City"), ("Thailand", "Bangkok"),
        ("Greece", "Athens"), ("Turkey", "Ankara"), ("South Korea", "Seoul"), ("Argentina", "Buenos Aires"),
        ("Sweden", "Stockholm"), ("Norway", "Oslo"), ("Netherlands", "Amsterdam"), ("Switzerland", "Bern"),
        ("Portugal", "Lisbon"), ("Ireland", "Dublin"), ("New Zealand", "Wellington"), ("South Africa", "Pretoria"),
        ("Austria", "Vienna"), ("Belgium", "Brussels"), ("Denmark", "Copenhagen"), ("Finland", "Helsinki"),
        ("Poland", "Warsaw"), ("Hungary", "Budapest"), ("Czech Republic", "Prague"), ("Vietnam", "Hanoi"),
        ("Indonesia", "Jakarta"), ("Malaysia", "Kuala Lumpur"), ("Philippines", "Manila"), ("Singapore", "Singapore"),
        ("Saudi Arabia", "Riyadh"), ("UAE", "Abu Dhabi"), ("Israel", "Jerusalem"), ("Iran", "Tehran"),
        ("Iraq", "Baghdad"), ("Pakistan", "Islamabad"), ("Kenya", "Nairobi"), ("Nigeria", "Abuja"),
        ("Chile", "Santiago"), ("Colombia", "Bogota"),
    ]
    
    for country, capital in capitals_easy:
        opts = [capital, "London", "Paris", "Berlin"] if capital not in ["London", "Paris", "Berlin"] else [capital, "Rome", "Madrid", "Tokyo"]
        random.shuffle(opts)
        easy_geo.append({
            "text": f"What is the capital of {country}?",
            "options": opts[:4],
            "correctIndex": opts.index(capital),
            "explanation": f"The capital of {country} is {capital}.",
            "difficulty": 1
        })
    
    # Rivers & Mountains (30 questions)
    geo_facts_easy = [
        ("Longest river in the world?", "Nile", ["Amazon", "Yangtze", "Mississippi"], "The Nile is 6,650 km long."),
        ("Second longest river?", "Amazon", ["Nile", "Yangtze", "Mississippi"], "The Amazon is 6,400 km long."),
        ("Tallest mountain?", "Mount Everest", ["K2", "Kilimanjaro", "Denali"], "Everest is 8,849 meters tall."),
        ("Largest ocean?", "Pacific", ["Atlantic", "Indian", "Arctic"], "Pacific covers 165 million km²."),
        ("Smallest ocean?", "Arctic", ["Indian", "Southern", "Atlantic"], "Arctic is 14 million km²."),
        ("Largest desert?", "Sahara", ["Arabian", "Gobi", "Kalahari"], "Sahara covers 9 million km²."),
        ("Largest country by area?", "Russia", ["Canada", "China", "USA"], "Russia is 17.1 million km²."),
        ("Smallest country?", "Vatican City", ["Monaco", "San Marino", "Nauru"], "Vatican is 0.44 km²."),
        ("Most populated country?", "India", ["China", "USA", "Indonesia"], "India has 1.4+ billion."),
        ("Deepest ocean point?", "Mariana Trench", ["Puerto Rico Trench", "Java Trench", "Tonga Trench"], "Mariana is 11,034 m deep."),
        ("Largest continent?", "Asia", ["Africa", "Americas", "Europe"], "Asia is 44.58 million km²."),
        ("Smallest continent?", "Australia", ["Europe", "Antarctica", "South America"], "Australia is smallest."),
        ("How many continents?", "7", ["5", "6", "8"], "7: Asia, Africa, NA, SA, Antarctica, Europe, Australia."),
        ("Largest island?", "Greenland", ["New Guinea", "Borneo", "Madagascar"], "Greenland is 2.17 million km²."),
        ("Highest waterfall?", "Angel Falls", ["Niagara", "Victoria", "Iguazu"], "Angel Falls is 979 m in Venezuela."),
        ("Largest lake?", "Caspian Sea", ["Superior", "Victoria", "Baikal"], "Caspian is 371,000 km²."),
        ("Deepest lake?", "Lake Baikal", ["Caspian", "Tanganyika", "Superior"], "Baikal is 1,642 m deep."),
        ("Longest mountain range?", "Andes", ["Rockies", "Himalayas", "Alps"], "Andes is 7,000 km long."),
        ("Where is Sahara Desert?", "Africa", ["Asia", "Australia", "South America"], "Sahara is in North Africa."),
        ("Where is Amazon Rainforest?", "South America", ["Africa", "Asia", "Australia"], "Amazon is in Brazil."),
    ]
    
    for q, ans, dists, expl in geo_facts_easy:
        opts = [ans] + dists
        random.shuffle(opts)
        easy_geo.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 1
        })
    
    # Countries & Continents (20 questions)
    country_facts = [
        ("Which continent is Egypt in?", "Africa", ["Asia", "Europe", "South America"], "Egypt is in northeastern Africa."),
        ("Which continent is Brazil in?", "South America", ["North America", "Africa", "Asia"], "Brazil is in South America."),
        ("Which continent is Japan in?", "Asia", ["Europe", "Oceania", "Africa"], "Japan is an island nation in East Asia."),
        ("Which continent is France in?", "Europe", ["Asia", "Africa", "North America"], "France is in Western Europe."),
        ("Where is the Great Wall?", "China", ["Japan", "Mongolia", "Korea"], "Great Wall is in China."),
        ("Where is the Eiffel Tower?", "Paris", ["London", "Rome", "Berlin"], "Eiffel Tower is in Paris, France."),
        ("Where is the Taj Mahal?", "India", ["Pakistan", "Bangladesh", "Nepal"], "Taj Mahal is in Agra, India."),
        ("Where is the Colosseum?", "Rome", ["Athens", "Paris", "Madrid"], "Colosseum is in Rome, Italy."),
        ("Where are the Pyramids?", "Egypt", ["Sudan", "Libya", "Morocco"], "Pyramids are near Cairo, Egypt."),
        ("Where is Big Ben?", "London", ["Paris", "Berlin", "Dublin"], "Big Ben is in London, UK."),
        ("Where is Statue of Liberty?", "New York", ["Washington", "Boston", "Chicago"], "Statue of Liberty is in New York Harbor."),
        ("Where is Sydney Opera House?", "Australia", ["New Zealand", "Singapore", "Malaysia"], "Sydney Opera House is in Australia."),
        ("Mount Kilimanjaro is in?", "Tanzania", ["Kenya", "Uganda", "Ethiopia"], "Kilimanjaro is in Tanzania."),
        ("Niagara Falls is between?", "USA and Canada", ["USA and Mexico", "Canada and Mexico", "USA and Cuba"], "Niagara Falls borders USA and Canada."),
        ("Sahara Desert spans how many countries?", "11", ["5", "8", "15"], "Sahara spans 11 African countries."),
        ("Which ocean is Hawaii in?", "Pacific", ["Atlantic", "Indian", "Arctic"], "Hawaii is in the Pacific Ocean."),
        ("Amazon River flows through?", "Brazil", ["Argentina", "Peru", "Venezuel a"], "Amazon mainly flows through Brazil."),
        ("Ganges River is sacred in?", "India", ["China", "Thailand", "Japan"], "Ganges is sacred in Hinduism."),
        ("Nile River flows through?", "Egypt", ["Libya", "Sudan only", "Morocco"], "Nile flows through Egypt."),
        ("Great Barrier Reef is in?", "Australia", ["New Zealand", "Indonesia", "Philippines"], "Great Barrier Reef is off Australia's coast."),
    ]
    
    for q, ans, dists, expl in country_facts:
        opts = [ans] + dists
        random.shuffle(opts)
        easy_geo.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 1
        })
    
    # LEVEL 2 - MEDIUM GEOGRAPHY (100 questions)
    medium_geo = []
    
    # Medium Capitals (60 questions)
    capitals_medium = [
        ("Ukraine", "Kyiv"), ("Romania", "Bucharest"), ("Bulgaria", "Sofia"), ("Serbia", "Belgrade"),
        ("Croatia", "Zagreb"), ("Slovakia", "Bratislava"), ("Slovenia", "Ljubljana"), ("Estonia", "Tallinn"),
        ("Latvia", "Riga"), ("Lithuania", "Vilnius"), ("Belarus", "Minsk"), ("Iceland", "Reykjavik"),
        ("Morocco", "Rabat"), ("Algeria", "Algiers"), ("Tunisia", "Tunis"), ("Libya", "Tripoli"),
        ("Ethiopia", "Addis Ababa"), ("Ghana", "Accra"), ("Senegal", "Dakar"), ("Kenya", "Nairobi"),
        ("Venezuela", "Caracas"), ("Ecuador", "Quito"), ("Bolivia", "La Paz"), ("Paraguay", "Asuncion"),
        ("Uruguay", "Montevideo"), ("Panama", "Panama City"), ("Costa Rica", "San Jose"), ("Jamaica", "Kingston"),
        ("Bangladesh", "Dhaka"), ("Sri Lanka", "Colombo"), ("Nepal", "Kathmandu"), ("Cambodia", "Phnom Penh"),
        ("Laos", "Vientiane"), ("Myanmar", "Naypyidaw"), ("Afghanistan", "Kabul"), ("Uzbekistan", "Tashkent"),
        ("Kazakhstan", "Astana"), ("Mongolia", "Ulaanbaatar"), ("Taiwan", "Taipei"), ("North Korea", "Pyongyang"),
        ("Syria", "Damascus"), ("Jordan", "Amman"), ("Lebanon", "Beirut"), ("Oman", "Muscat"),
        ("Yemen", "Sanaa"), ("Qatar", "Doha"), ("Kuwait", "Kuwait City"), ("Bahrain", "Manama"),
        ("Peru", "Lima"), ("Cuba", "Havana"), ("Fiji", "Suva"), ("Papua New Guinea", "Port Moresby"),
        ("Zimbabwe", "Harare"), ("Zambia", "Lusaka"), ("Uganda", "Kampala"), ("Tanzania", "Dodoma"),
        ("Cameroon", "Yaounde"), ("Angola", "Luanda"), ("Somalia", "Mogadishu"), ("Sudan", "Khartoum"),
    ]
    
    for country, capital in capitals_medium:
        opts = [capital, "Paris", "London", "Tokyo"] if capital not in ["Paris", "London", "Tokyo"] else [capital, "Berlin", "Rome", "Madrid"]
        random.shuffle(opts)
        medium_geo.append({
            "text": f"What is the capital of {country}?",
            "options": opts[:4],
            "correctIndex": opts.index(capital),
            "explanation": f"The capital of {country} is {capital}.",
            "difficulty": 2
        })
    
    # Medium Geography Facts (40 questions)
    geo_facts_medium = [
        ("What is Earth's diameter?", "12,742 km", ["10,000 km", "15,000 km", "20,000 km"], "Earth's equatorial diameter is 12,742 km."),
        ("Distance from Earth to Sun?", "150 million km", ["100 million km", "200 million km", "50 million km"], "Average distance is 149.6 million km (1 AU)."),
        ("What percentage of Earth is water?", "71%", ["50%", "60%", "80%"], "About 71% of Earth's surface is water."),
        ("Largest island in Mediterranean?", "Sicily", ["Crete", "Cyprus", "Sardinia"], "Sicily is the largest Mediterranean island."),
        ("Longest river in Europe?", "Volga", ["Danube", "Rhine", "Thames"], "Volga is 3,692 km long."),
        ("Highest mountain in Africa?", "Kilimanjaro", ["Mount Kenya", "Atlas", "Drakensberg"], "Kilimanjaro is 5,895 m."),
        ("Largest country in Africa?", "Algeria", ["Sudan", "Congo", "Libya"], "Algeria is 2.38 million km²."),
        ("Smallest country in Asia?", "Maldives", ["Singapore", "Bahrain", "Brunei"], "Maldives is 298 km²."),
        ("Largest country in South America?", "Brazil", ["Argentina", "Peru", "Colombia"], "Brazil is 8.5 million km²."),
        ("Capital of Australia?", "Canberra", ["Sydney", "Melbourne", "Brisbane"], "Canberra is the capital, not Sydney."),
        ("Capital of Canada?", "Ottawa", ["Toronto", "Montreal", "Vancouver"], "Ottawa is the capital, not Toronto."),
        ("Capital of Switzerland?", "Bern", ["Zurich", "Geneva", "Basel"], "Bern is the capital, not Zurich."),
        ("What sea is between Europe and Africa?", "Mediterranean", ["Red Sea", "Black Sea", "Adriatic"], "Mediterranean separates Europe and Africa."),
        ("Panama Canal connects?", "Atlantic and Pacific", ["Indian and Pacific", "Atlantic and Indian", "Arctic and Atlantic"], "Panama Canal links Atlantic and Pacific oceans."),
        ("Suez Canal is in?", "Egypt", ["Saudi Arabia", "Iran", "UAE"], "Suez Canal is in Egypt."),
        ("Where is the Dead Sea?", "Jordan/Israel", ["Egypt", "Syria", "Lebanon"], "Dead Sea borders Jordan and Israel."),
        ("Largest gulf in the world?", "Gulf of Mexico", ["Persian Gulf", "Gulf of Thailand", "Hudson Bay"], "Gulf of Mexico is the largest."),
        ("Ring of Fire is in?", "Pacific Ocean", ["Atlantic", "Indian", "Arctic"], "Ring of Fire is a Pacific volcanic belt."),
        ("Where is Patagonia?", "Argentina/Chile", ["Brazil", "Peru", "Bolivia"], "Patagonia is in southern Argentina and Chile."),
        ("Where is Siberia?", "Russia", ["Mongolia", "Kazakhstan", "China"], "Siberia is in northern Russia."),
        ("Strait of Gibraltar connects?", "Atlantic and Mediterranean", ["Atlantic and Pacific", "Indian and Pacific", "Red Sea and Mediterranean"], "Gibraltar links Atlantic and Mediterranean."),
        ("Where is the Gobi Desert?", "Mongolia/China", ["India", "Kazakhstan", "Australia"], "Gobi is in Mongolia and China."),
        ("Where is Atacama Desert?", "Chile", ["Peru", "Argentina", "Bolivia"], "Atacama is in northern Chile."),
        ("Where is Kalahari Desert?", "Southern Africa", ["North Africa", "Asia", "Australia"], "Kalahari is in Botswana, Namibia, South Africa."),
        ("What is a fjord?", "Narrow inlet", ["Mountain", "Desert", "Forest"], "Fjords are narrow sea inlets formed by glaciers."),
        ("Where are most fjords?", "Norway", ["Iceland", "Canada", "Alaska"], "Norway is famous for its fjords."),
        ("What is the Equator latitude?", "0 degrees", ["23.5 degrees", "90 degrees", "45 degrees"], "The Equator is at 0° latitude."),
        ("What is the Prime Meridian longitude?", "0 degrees", ["90 degrees", "180 degrees", "45 degrees"], "Prime Meridian is at 0° longitude through Greenwich."),
        ("How many time zones on Earth?", "24", ["12", "36", "48"], "There are 24 standard time zones."),
        ("Tropic of Cancer latitude?", "23.5°N", ["0°", "45°N", "66.5°N"], "Tropic of Cancer is at 23.5°N."),
        ("Tropic of Capricorn latitude?", "23.5°S", ["0°", "45°S", "66.5°S"], "Tropic of Capricorn is at 23.5°S."),
        ("Arctic Circle latitude?", "66.5°N", ["23.5°N", "45°N", "90°N"], "Arctic Circle is at 66.5°N."),
        ("Antarctic Circle latitude?", "66.5°S", ["23.5°S", "45°S", "90°S"], "Antarctic Circle is at 66.5°S."),
        ("International Date Line follows?", "180° meridian", ["0° meridian", "90° meridian", "45° meridian"], "Date Line roughly follows 180° longitude."),
        ("Highest capital city?", "La Paz", ["Quito", "Bogota", "Addis Ababa"], "La Paz, Bolivia is at 3,640 m elevation."),
        ("Lowest point on land?", "Dead Sea", ["Death Valley", "Caspian Sea", "Salton Sea"], "Dead Sea shore is 430 m below sea level."),
        ("Largest bay in the world?", "Bay of Bengal", ["Hudson Bay", "Gulf of Mexico", "Baffin Bay"], "Bay of Bengal is the largest bay."),
        ("Where is the Grand Canyon?", "Arizona, USA", ["Utah", "Nevada", "California"], "Grand Canyon is in Arizona."),
        ("Where is Victoria Falls?", "Zambia/Zimbabwe", ["Tanzania", "Kenya", "South Africa"], "Victoria Falls is on Zambezi River."),
        ("Where is Iguazu Falls?", "Argentina/Brazil", ["Paraguay", "Uruguay", "Venezuela"], "Iguazu Falls borders Argentina and Brazil."),
    ]
    
    for q, ans, dists, expl in geo_facts_medium:
        opts = [ans] + dists
        random.shuffle(opts)
        medium_geo.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 2
        })
    
    # LEVEL 3 - HARD GEOGRAPHY (100 questions)
    hard_geo = []
    
    # Hard Capitals (50 questions)
    capitals_hard = [
        ("Liechtenstein", "Vaduz"), ("Bhutan", "Thimphu"), ("Maldives", "Male"), ("Brunei", "Bandar Seri Begawan"),
        ("Kyrgyzstan", "Bishkek"), ("Tajikistan", "Dushanbe"), ("Turkmenistan", "Ashgabat"), ("Azerbaijan", "Baku"),
        ("Armenia", "Yerevan"), ("Georgia", "Tbilisi"), ("Moldova", "Chisinau"), ("Malta", "Valletta"),
        ("Cyprus", "Nicosia"), ("Andorra", "Andorra la Vella"), ("San Marino", "San Marino"), ("Monaco", "Monaco"),
        ("Luxembourg", "Luxembourg"), ("Montenegro", "Podgorica"), ("Kosovo", "Pristina"), ("Macedonia", "Skopje"),
        ("Albania", "Tirana"), ("Bosnia", "Sarajevo"), ("Eritrea", "Asmara"), ("Djibouti", "Djibouti"),
        ("Rwanda", "Kigali"), ("Burundi", "Gitega"), ("Madagascar", "Antananarivo"), ("Mauritius", "Port Louis"),
        ("Seychelles", "Victoria"), ("Mozambique", "Maputo"), ("Malawi", "Lilongwe"), ("Namibia", "Windhoek"),
        ("Botswana", "Gaborone"), ("Gabon", "Libreville"), ("Congo", "Brazzaville"), ("Central African Rep", "Bangui"),
        ("Chad", "N'Djamena"), ("Niger", "Niamey"), ("Burkina Faso", "Ouagadougou"), ("Mali", "Bamako"),
        ("Mauritania", "Nouakchott"), ("Benin", "Porto-Novo"), ("Togo", "Lome"), ("Sierra Leone", "Freetown"),
        ("Liberia", "Monrovia"), ("Guinea", "Conakry"), ("Equatorial Guinea", "Malabo"), ("Sao Tome", "Sao Tome"),
        ("Cape Verde", "Praia"), ("Comoros", "Moroni"),
    ]
    
    for country, capital in capitals_hard:
        opts = [capital, "Paris", "London", "Rome"] if capital not in ["Paris", "London", "Rome"] else [capital, "Berlin", "Madrid", "Vienna"]
        random.shuffle(opts)
        hard_geo.append({
            "text": f"What is the capital of {country}?",
            "options": opts[:4],
            "correctIndex": opts.index(capital),
            "explanation": f"The capital of {country} is {capital}.",
            "difficulty": 3
        })
    
    # Hard Geography Facts (50 questions)
    geo_facts_hard = [
        ("What is the circumference of Earth?", "40,075 km", ["30,000 km", "50,000 km", "20,000 km"], "Earth's equatorial circumference is 40,075 km."),
        ("What is Earth's tilt angle?", "23.5 degrees", ["15 degrees", "30 degrees", "45 degrees"], "Earth's axial tilt is 23.5°."),
        ("Speed of Earth's rotation?", "1,670 km/h", ["1,000 km/h", "2,000 km/h", "500 km/h"], "At equator, Earth rotates at 1,670 km/h."),
        ("Earth's orbital speed?", "107,000 km/h", ["50,000 km/h", "150,000 km/h", "200,000 km/h"], "Earth orbits Sun at ~107,000 km/h."),
        ("Age of Earth?", "4.54 billion years", ["3 billion years", "5 billion years", "10 billion years"], "Earth formed 4.54 billion years ago."),
        ("Deepest cave on Earth?", "Veryovkina Cave", ["Krubera Cave", "Lamprechtsofen", "Illyuzia-Mezhonnogo"], "Veryovkina in Georgia is 2,212 m deep."),
        ("Largest volcano by volume?", "Mauna Loa", ["Mount Fuji", "Kilimanjaro", "Vesuvius"], "Mauna Loa in Hawaii is the largest."),
        ("Driest place on Earth?", "Atacama Desert", ["Sahara", "Death Valley", "Arabian Desert"], "Atacama gets < 1 mm rain/year."),
        ("Wettest place on Earth?", "Mawsynram", ["Cherrapunji", "Amazon", "Hawaii"], "Mawsynram, India gets 11,871 mm rain/year."),
        ("Hottest temperature recorded?", "56.7°C", ["50°C", "60°C", "70°C"], "Recorded in Death Valley, 1913."),
        ("Coldest temperature recorded?", "-89.2°C", ["-70°C", "-100°C", "-50°C"], "Recorded at Vostok Station, Antarctica, 1983."),
        ("Highest inhabited place?", "La Rinconada", ["La Paz", "Lhasa", "Cusco"], "La Rinconada, Peru at 5,100 m."),
        ("Largest crater on Earth?", "Vredefort Crater", ["Chicxulub", "Sudbury", "Popigai"], "Vredefort in South Africa, 300 km diameter."),
        ("What percentage of Earth is land?", "29%", ["40%", "20%", "50%"], "About 29% is land, 71% is water."),
        ("Which ocean is deepest?", "Pacific", ["Atlantic", "Indian", "Arctic"], "Pacific has the Mariana Trench."),
        ("How old are the Himalayas?", "50 million years", ["100 million", "200 million", "10 million"], "Himalayas formed ~50 million years ago."),
        ("What causes tides?", "Moon's gravity", ["Sun's gravity", "Earth's rotation", "Wind"], "Moon's gravitational pull causes tides."),
        ("What is a moraine?", "Glacial deposit", ["Mountain", "River", "Desert"], "Moraine is debris deposited by glaciers."),
        ("What is a peninsula?", "Land surrounded by water on 3 sides", ["Island", "Cape", "Isthmus"], "Peninsula is land jutting into water."),
        ("What is an isthmus?", "Narrow land connecting two larger areas", ["Island", "Peninsula", "Cape"], "Isthmus connects two land masses."),
        ("What is an archipelago?", "Group of islands", ["Single island", "Peninsula", "Bay"], "Archipelago is a cluster of islands."),
        ("Largest archipelago?", "Indonesia", ["Philippines", "Japan", "Greece"], "Indonesia has over 17,000 islands."),
        ("What is the Continental Shelf?", "Underwater extension of continent", ["Ocean trench", "Mountain range", "Island"], "Continental shelf extends underwater from land."),
        ("What is bathymetry?", "Study of underwater depths", ["Study of mountains", "Study of deserts", "Study of rivers"], "Bathymetry maps ocean floor depths."),
        ("What is topography?", "Surface features of land", ["Underground features", "Ocean features", "Atmospheric features"], "Topography describes land surface characteristics."),
        ("What causes earthquakes?", "Tectonic plate movement", ["Volcanic eruptions", "Meteor impacts", "Ocean currents"], "Earthquakes occur when tectonic plates shift."),
        ("What is the Richter Scale?", "Earthquake magnitude", ["Temperature", "Altitude", "Pressure"], "Richter scale measures earthquake intensity."),
        ("What is Pangaea?", "Ancient supercontinent", ["Ocean", "Mountain range", "Desert"], "Pangaea existed 335-175 million years ago."),
        ("When did Pangaea break up?", "175 million years ago", ["500 million", "100 million", "50 million"], "Pangaea began splitting 175 million years ago."),
        ("What is the Moho discontinuity?", "Crust-mantle boundary", ["Core boundary", "Atmospheric layer", "Ocean layer"], "Moho separates Earth's crust from mantle."),
        ("How thick is Earth's crust?", "5-70 km", ["100-200 km", "1-5 km", "200-500 km"], "Oceanic crust: 5-10 km; Continental: 30-70 km."),
        ("What is the asthenosphere?", "Upper mantle layer", ["Crust layer", "Core layer", "Atmospheric layer"], "Asthenosphere is semi-fluid upper mantle."),
        ("What is subduction?", "One plate sliding under another", ["Plates pulling apart", "Plates sliding past", "Volcanic eruption"], "Subduction creates deep ocean trenches."),
        ("What is a transform boundary?", "Plates sliding horizontally", ["Plates colliding", "Plates separating", "Plates subducting"], "Transform boundaries cause earthquakes."),
        ("What is a divergent boundary?", "Plates moving apart", ["Plates colliding", "Plates sliding", "Plates subducting"], "Divergent boundaries create new crust."),
        ("What is a convergent boundary?", "Plates colliding", ["Plates separating", "Plates sliding", "Plates sinking"], "Convergent boundaries form mountains."),
        ("What is the lithosphere?", "Rigid outer layer", ["Liquid layer", "Gaseous layer", "Core"], "Lithosphere includes crust and upper mantle."),
        ("How many major tectonic plates?", "7", ["5", "10", "15"], "There are 7 major plates and many minor ones."),
        ("What is a hot spot?", "Volcanic region fed by mantle plume", ["Earthquake zone", "Desert", "Ocean trench"], "Hawaii was formed by a hot spot."),
        ("What is permafrost?", "Permanently frozen ground", ["Temporary ice", "Glacier", "Snow"], "Permafrost stays frozen year-round."),
        ("Where is most freshwater?", "Antarctica ice", ["Lakes", "Rivers", "Groundwater"], "70% of freshwater is in Antarctic ice."),
        ("What percentage of water is freshwater?", "2.5%", ["10%", "25%", "50%"], "Only 2.5% of Earth's water is fresh."),
        ("What is karst topography?", "Limestone landscape with caves", ["Volcanic landscape", "Glacial landscape", "Desert landscape"], "Karst forms from dissolved limestone."),
        ("What is a stalactite?", "Hangs from cave ceiling", ["Rises from cave floor", "Cave wall", "Underground river"], "Stalactite hangs like icicle."),
        ("What is a stalagmite?", "Rises from cave floor", ["Hangs from ceiling", "Cave wall", "Underground lake"], "Stalagmite grows upward."),
        ("What is erosion?", "Wearing away of land", ["Building up of land", "Volcanic activity", "Earthquake"], "Erosion is caused by wind, water, ice."),
        ("What is weathering?", "Breaking down of rocks", ["Transport of rocks", "Formation of rocks", "Melting of rocks"], "Weathering can be physical or chemical."),
        ("What is sedimentation?", "Deposition of particles", ["Erosion", "Weathering", "Volcanic eruption"], "Sedimentation builds up layers."),
        ("What causes monsoons?", "Seasonal wind patterns", ["Volcanic eruptions", "Earthquakes", "Ocean currents"], "Monsoons bring seasonal heavy rains."),
        ("What is the Coriolis effect?", "Deflection due to Earth's rotation", ["Ocean currents", "Tides", "Atmospheric pressure"], "Coriolis affects wind and ocean patterns."),
    ]
    
    for q, ans, dists, expl in geo_facts_hard:
        opts = [ans] + dists
        random.shuffle(opts)
        hard_geo.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 3
        })
    
    return {
        "batch_name": "Geography",
        "l1": easy_geo,
        "l2": medium_geo,
        "l3": hard_geo
    }

if __name__ == "__main__":
    batch1 = create_batch1_geography()
    print(f"Batch 1 (Geography):")
    print(f"  Level 1: {len(batch1['l1'])} questions")
    print(f"  Level 2: {len(batch1['l2'])} questions")
    print(f"  Level 3: {len(batch1['l3'])} questions")
    
    # Save to temp file
    with open('treasure_batch1.json', 'w') as f:
        json.dump(batch1, f, indent=2)
    print("Saved to treasure_batch1.json")
