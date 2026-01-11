import json
import random

# --- DATASETS ---

# 1. CAPITALS (Homogeneous - Random sampling safe)
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
    ("Chile", "Santiago"), ("Colombia", "Bogota"), ("Peru", "Lima"), ("Cuba", "Havana")
]

capitals_medium = [
    ("Ukraine", "Kyiv"), ("Romania", "Bucharest"), ("Bulgaria", "Sofia"), ("Serbia", "Belgrade"),
    ("Croatia", "Zagreb"), ("Slovakia", "Bratislava"), ("Slovenia", "Ljubljana"), ("Estonia", "Tallinn"),
    ("Latvia", "Riga"), ("Lithuania", "Vilnius"), ("Belarus", "Minsk"), ("Iceland", "Reykjavik"),
    ("Morocco", "Rabat"), ("Algeria", "Algiers"), ("Tunisia", "Tunis"), ("Libya", "Tripoli"),
    ("Ethiopia", "Addis Ababa"), ("Ghana", "Accra"), ("Senegal", "Dakar"), ("Ivory Coast", "Yamoussoukro"),
    ("Venezuela", "Caracas"), ("Ecuador", "Quito"), ("Bolivia", "La Paz"), ("Paraguay", "Asuncion"),
    ("Uruguay", "Montevideo"), ("Panama", "Panama City"), ("Costa Rica", "San Jose"), ("Jamaica", "Kingston"),
    ("Syria", "Damascus"), ("Jordan", "Amman"), ("Lebanon", "Beirut"), ("Oman", "Muscat"),
    ("Yemen", "Sanaa"), ("Qatar", "Doha"), ("Kuwait", "Kuwait City"), ("Bahrain", "Manama"),
    ("Bangladesh", "Dhaka"), ("Sri Lanka", "Colombo"), ("Nepal", "Kathmandu"), ("Kazakhstan", "Astana"),
    ("Uzbekistan", "Tashkent"), ("Afghanistan", "Kabul"), ("Mongolia", "Ulaanbaatar"), ("North Korea", "Pyongyang"),
    ("Cambodia", "Phnom Penh"), ("Laos", "Vientiane"), ("Myanmar", "Naypyidaw"), ("Taiwan", "Taipei"),
    ("Fiji", "Suva"), ("Papua New Guinea", "Port Moresby"), ("Zimbabwe", "Harare"), ("Zambia", "Lusaka")
]

capitals_hard = [
    ("Liechtenstein", "Vaduz"), ("Lucas", "Maseru"), ("Bhutan", "Thimphu"), ("Maldives", "Male"),
    ("Brunei", "Bandar Seri Begawan"), ("East Timor", "Dili"), ("Kyrgyzstan", "Bishkek"), ("Tajikistan", "Dushanbe"),
    ("Turkmenistan", "Ashgabat"), ("Azerbaijan", "Baku"), ("Armenia", "Yerevan"), ("Georgia", "Tbilisi"),
    ("Moldova", "Chisinau"), ("Malta", "Valletta"), ("Cyprus", "Nicosia"), ("Andorra", "Andorra la Vella"),
    ("San Marino", "San Marino"), ("Monaco", "Monaco"), ("Luxembourg", "Luxembourg"), ("Montenegro", "Podgorica"),
    ("Kosovo", "Pristina"), ("Macedonia", "Skopje"), ("Albania", "Tirana"), ("Bosnia", "Sarajevo"),
    ("Somalia", "Mogadishu"), ("Djibouti", "Djibouti"), ("Eritrea", "Asmara"), ("Sudan", "Khartoum"),
    ("South Sudan", "Juba"), ("Uganda", "Kampala"), ("Rwanda", "Kigali"), ("Burundi", "Gitega"),
    ("Tanzania", "Dodoma"), ("Madagascar", "Antananarivo"), ("Seychelles", "Victoria"), ("Mauritius", "Port Louis"),
    ("Mozambique", "Maputo"), ("Malawi", "Lilongwe"), ("Namibia", "Windhoek"), ("Botswana", "Gaborone"),
    ("Angola", "Luanda"), ("Cameroon", "Yaounde"), ("Gabon", "Libreville"), ("Congo", "Brazzaville"),
    ("Chad", "N'Djamena"), ("Niger", "Niamey"), ("Mali", "Bamako"), ("Burkina Faso", "Ouagadougou"),
    ("Togo", "Lome"), ("Benin", "Porto-Novo"), ("Liberia", "Monrovia"), ("Sierra Leone", "Freetown"),
    ("Guinea", "Conakry"), ("Mauritania", "Nouakchott"), ("Guyana", "Georgetown"), ("Suriname", "Paramaribo"),
    ("Haiti", "Port-au-Prince"), ("Dominican Rep", "Santo Domingo"), ("Trinidad", "Port of Spain"), ("Bahamas", "Nassau"),
    ("Barbados", "Bridgetown"), ("Belize", "Belmopan"), ("Honduras", "Tegucigalpa"), ("El Salvador", "San Salvador"),
    ("Guatemala", "Guatemala City"), ("Nicaragua", "Managua"), ("Tuvalu", "Funafuti"), ("Kiribati", "Tarawa"),
    ("Vanuatu", "Port Vila"), ("Samoa", "Apia"), ("Tonga", "Nuku'alofa"), ("Palau", "Ngerulmud")
]

# 2. ELEMENTS (Homogeneous)
elements = [
    ("H", "Hydrogen"), ("He", "Helium"), ("Li", "Lithium"), ("C", "Carbon"), ("N", "Nitrogen"),
    ("O", "Oxygen"), ("Na", "Sodium"), ("Mg", "Magnesium"), ("Al", "Aluminum"), ("Si", "Silicon"),
    ("S", "Sulfur"), ("Cl", "Chlorine"), ("K", "Potassium"), ("Ca", "Calcium"), ("Fe", "Iron"),
    ("Cu", "Copper"), ("Zn", "Zinc"), ("Ag", "Silver"), ("Au", "Gold"), ("Hg", "Mercury"),
    ("Pb", "Lead"), ("U", "Uranium"), ("Ne", "Neon"), ("Ti", "Titanium"), ("Ni", "Nickel"),
    ("B", "Boron"), ("F", "Fluorine"), ("P", "Phosphorus"), ("Ar", "Argon"), ("Mn", "Manganese"),
    ("Co", "Cobalt"), ("Br", "Bromine"), ("Sn", "Tin"), ("I", "Iodine"), ("Pt", "Platinum")
]

# 3. TRIVIA (MANUALLY FIXED DISTRACTORS)
# Format: (Question, Answer, [Distractors], Explanation)

trivia_easy_fixed = [
    ("Which is the largest ocean on Earth?", "Pacific Ocean", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], "The Pacific Ocean covers more than 30% of Earth's surface."),
    ("What is the capital of France?", "Paris", ["London", "Berlin", "Madrid"], "Paris is the global center for art, fashion, and culture, known as the City of Light."),
    ("Which continent is known as the 'Dark Continent'?", "Africa", ["Asia", "Australia", "South America"], "This term was coined by 19th-century European explorers referring to the continent's mystery."),
    ("Mount Everest is located in which mountain range?", "The Himalayas", ["The Andes", "The Rockies", "The Alps"], "The Himalayas separate the Indian subcontinent from the Tibetan Plateau."),
    ("Which country has the largest population?", "India", ["China", "USA", "Russia"], "India surpassed China as the most populous nation around 2023."),
    ("What is the chemical formula for water?", "H2O", ["CO2", "O2", "NaCl"], "A water molecule consists of two hydrogen atoms bonded to one oxygen atom."),
    ("Which planet is known as the Red Planet?", "Mars", ["Jupiter", "Venus", "Saturn"], "Mars appears red due to the iron oxide (rust) prevalent on its surface."),
    ("What is the hardest natural substance on Earth?", "Diamond", ["Gold", "Iron", "Granite"], "Diamonds are formed from carbon atoms arranged in a rigid crystal lattice."),
    ("What gas do humans breathe in to survive?", "Oxygen", ["Carbon Dioxide", "Nitrogen", "Helium"], "Humans inhale oxygen, which allows cells to produce energy."),
    ("How many legs does a spider have?", "8", ["6", "4", "10"], "Spiders are arachnids and always have eight legs, unlike insects which have six."),
    ("What is the center of our Solar System?", "The Sun", ["Earth", "The Moon", "Jupiter"], "The Sun is the star at the center of the Solar System, and all planets orbit it."),
    ("Who is credited with discovering gravity?", "Isaac Newton", ["Albert Einstein", "Galileo", "Tesla"], "Newton formulated the laws of motion and universal gravitation."),
    ("Who was the first President of the USA?", "George Washington", ["Abraham Lincoln", "Thomas Jefferson", "John Adams"], "He served as the first president from 1789 to 1797."),
    ("Which ship sank in 1912 after hitting an iceberg?", "Titanic", ["Olympic", "Britannic", "Lusitania"], "The RMS Titanic sank on its maiden voyage after colliding with an iceberg."),
    ("The Great Wall is located in which country?", "China", ["Japan", "India", "Mongolia"], "It is a series of fortifications built across the historical northern borders of China."),
    ("Who wrote 'Romeo and Juliet'?", "William Shakespeare", ["Charles Dickens", "Mark Twain", "Homer"], "Shakespeare is considered the greatest writer in the English language."),
    ("In which country were the Pyramids of Giza built?", "Egypt", ["Mexico", "Peru", "Sudan"], "The Giza Pyramids were built as tombs for the Pharaohs of Ancient Egypt."),
    ("What ancient civilization built Machu Picchu?", "The Incas", ["The Mayans", "The Aztecs", "The Romans"], "Machu Picchu is a 15th-century Inca citadel located in Peru."),
    ("Which animal is the fastest land animal?", "Cheetah", ["Lion", "Leopard", "Horse"], "Cheetahs can accelerate from 0 to 60 mph in just a few seconds."),
    ("Which is the tallest animal in the world?", "Giraffe", ["Elephant", "Horse", "Camel"], "Giraffes can grow up to 5.5 meters tall, with necks up to 2 meters long."),
    ("Which is the largest mammal in the world?", "Blue Whale", ["Elephant", "Shark", "Hippo"], "The Blue Whale is the largest animal known to have ever lived, reaching 30 meters."),
    ("What is the freezing point of water?", "0 C", ["100 C", "-10 C", "32 C"], "Water freezes at 0 degrees Celsius (32 degrees Fahrenheit) at sea level."),
    ("How many colors are there in a rainbow?", "7", ["5", "8", "9"], "The traditional colors are Red, Orange, Yellow, Green, Blue, Indigo, and Violet."),
    ("How many days are there in a standard year?", "365", ["366", "360", "364"], "A standard calendar year has 365 days, while a leap year has 366."),
    ("Which bird cannot fly?", "Penguin", ["Eagle", "Sparrow", "Hawk"], "Penguins are flightless birds adapted for life in the water."),
    ("What is the largest organ in the human body?", "Skin", ["Liver", "Heart", "Lungs"], "The skin is the body's largest organ, protecting it from external elements."),
    ("Which planet is closest to the Sun?", "Mercury", ["Venus", "Mars", "Earth"], "Mercury is the smallest and innermost planet in the Solar System."),
    ("Who painted the 'Mona Lisa'?", "Leonardo da Vinci", ["Picasso", "Van Gogh", "Michelangelo"], "The masterpiece was painted in the early 16th century and hangs in the Louvre."),
    ("What determines the color of your skin?", "Melanin", ["Protein", "Calcium", "Vitamin"], "Melanin is a pigment produced by cells that gives skin, hair, and eyes their color."),
    ("Which country invented paper?", "China", ["Egypt", "Greece", "India"], "Papermaking was developed in China around 105 AD."),
    ("What is the currency of Japan?", "Yen", ["Won", "Dollar", "Yuan"], "The Yen is the official currency of Japan, symbolized by ¥."),
    ("Which planet has rings?", "Saturn", ["Mars", "Venus", "Mercury"], "While others have faint rings, Saturn is famous for its extensive ring system."),
    ("Who discovered electricity?", "Benjamin Franklin", ["Edison", "Tesla", "Bell"], "He demonstrated the connection between lightning and electricity with his kite experiment."),
    ("What is the main ingredient in bread?", "Flour", ["Sugar", "Salt", "Milk"], "Bread is a staple food prepared from a dough of flour and water."),
    ("Which instrument measures temperature?", "Thermometer", ["Barometer", "Speedometer", "Compass"], "A thermometer measures temperature or temperature gradient."),
    ("What is the boiling point of water?", "100 C", ["90 C", "110 C", "0 C"], "Water boils at 100 degrees Celsius at standard sea-level pressure."),
    ("Which animal is known as the 'Ship of the Desert'?", "Camel", ["Horse", "Elephant", "Donkey"], "Camels are perfectly adapted to travel across deserts with little water."),
    ("Who invented the light bulb?", "Thomas Edison", ["Tesla", "Bell", "Franklin"], "Edison developed the first commercially practical incandescent light bulb."),
    ("Which is the smallest continent?", "Australia", ["Europe", "Antarctica", "South America"], "Australia is the smallest continent and the lowest-lying human-inhabited one."),
    ("What is the largest desert in the world?", "Antarctic Desert", ["Sahara", "Gobi", "Arabian"], "Antarctica is technically the largest desert because it receives very little precipitation."),
    ("Which blood type is the universal donor?", "O Negative", ["A Positive", "AB Negative", "B Positive"], "O Negative blood can be accepted by patients of any other blood type."),
    ("What is the symbol for Gold?", "Au", ["Ag", "Go", "Fe"], "The symbol 'Au' comes from 'Aurum', the Latin word for gold."),
    ("How many bones are in the adult human body?", "206", ["200", "210", "300"], "Infants are born with ~270 bones, but many fuse together as they grow."),
    ("Which galaxy do we live in?", "Milky Way", ["Andromeda", "Sombrero", "Whirlpool"], "The Milky Way is a barred spiral galaxy containing our Solar System."),
    ("What represents the 'Ph' in pH scale?", "Potential Hydrogen", ["Pure Heat", "Power Heat", "Percentage"], "pH measures the acidity or alkalinity of a solution.")
]

trivia_medium_fixed = [
    ("Which is the longest river in the world?", "The Nile", ["The Amazon", "The Yangtze", "The Mississippi"], "The Nile is generally regarded as the longest river, flowing through northeastern Africa."),
    ("What is the capital of Australia?", "Canberra", ["Sydney", "Melbourne", "Perth"], "Canberra was chosen as the capital in 1908 as a compromise between Sydney and Melbourne."),
    ("Which U.S. state is the largest by area?", "Alaska", ["Texas", "California", "Montana"], "Alaska is the largest state, being more than twice the size of Texas."),
    ("What is the chemical symbol for Silver?", "Ag", ["Au", "Si", "Fe"], "The symbol 'Ag' comes from 'Argentum', the Latin word for silver."),
    ("Which organ filters blood?", "Kidneys", ["Liver", "Heart", "Lungs"], "The kidneys filter waste and excess water from the blood to create urine."),
    ("What is the speed of light approx?", "300,000 km/s", ["150,000 km/s", "1,000 km/s", "Sound speed"], "Light travels at approximately 299,792 kilometers per second in a vacuum."),
    ("Most abundant element in Universe?", "Hydrogen", ["Oxygen", "Carbon", "Helium"], "Hydrogen acts as the fuel for stars and makes up mostly 75% of normal matter."),
    ("Who developed the Theory of Relativity?", "Albert Einstein", ["Newton", "Hawking", "Bohr"], "Einstein's theory revolutionized our understanding of space, time, and gravity."),
    ("In what year did WWII end?", "1945", ["1939", "1918", "1950"], "The war ended in 1945 with the unconditional surrender of the Axis powers."),
    ("Who was the first man on the Moon?", "Neil Armstrong", ["Buzz Aldrin", "Yuri Gagarin", "John Glenn"], "Armstrong became the first person to step onto the lunar surface in 1969."),
    ("Which empire was ruled by Julius Caesar?", "Roman Empire", ["Greek Empire", "Ottoman Empire", "British Empire"], "Caesar played a critical role in the rise of the Roman Empire."),
    ("First artificial satellite?", "Sputnik 1", ["Apollo", "Voyager", "Explorer"], "Sputnik 1 was launched by the Soviet Union into orbit on October 4, 1957."),
    ("Who discovered Penicillin?", "Alexander Fleming", ["Louis Pasteur", "Marie Curie", "Lister"], "Fleming discovered the world's first broadly effective antibiotic substance in 1928."),
    ("Who invented the Telephone?", "Alexander Graham Bell", ["Edison", "Marconi", "Tesla"], "Bell was awarded the first US patent for the telephone in 1876."),
    ("Which country gifted the Statue of Liberty to the USA?", "France", ["UK", "Spain", "Germany"], "The statue was a gift from the people of France to the United States in 1886."),
    ("What is the hardest bone in the human body?", "Femur", ["Skull", "Rib", "Tibia"], "The femur, or thigh bone, is the strongest and longest bone in the body."),
    ("Which city is known as the Big Apple?", "New York", ["Los Angeles", "Chicago", "Miami"], "The nickname 'The Big Apple' was popularized in the 1920s by sports writer John Fitz Gerald."),
    ("Who wrote 'Harry Potter'?", "J.K. Rowling", ["Tolkien", "George Martin", "Stephen King"], "Rowling wrote the seven-volume fantasy series which became a global phenomenon."),
    ("What is the capital of Canada?", "Ottawa", ["Toronto", "Montreal", "Vancouver"], "Queen Victoria chose Ottawa as the capital of the Province of Canada in 1857."),
    ("Which planet has the Great Red Spot?", "Jupiter", ["Mars", "Saturn", "Neptune"], "The Great Red Spot is a persistent high-pressure storm on Jupiter."),
    ("What is the currency of the UK?", "Pound Sterling", ["Euro", "Dollar", "Franc"], "The Pound Sterling is the world's oldest currency still in use."),
    ("Who painted 'Starry Night'?", "Vincent van Gogh", ["Picasso", "Monet", "Da Vinci"], "Van Gogh painted this masterpiece while in an asylum in Saint-Rémy-de-Provence."),
    ("Which gas makes up most of Earth's atmosphere?", "Nitrogen", ["Oxygen", "Carbon Dioxide", "Argon"], "Earth's atmosphere is approximately 78% nitrogen and 21% oxygen."),
    ("What is the powerhouse of the cell?", "Mitochondria", ["Nucleus", "Ribosome", "Golgi"], "Mitochondria generate most of the cell's supply of adenosine triphosphate (ATP)."),
    ("Who was the second President of the US?", "John Adams", ["Jefferson", "Madison", "Hamilton"], "Adams served as the first Vice President and then as the second President."),
    ("Which country has the most lakes?", "Canada", ["USA", "Russia", "Brazil"], "Canada has more lakes than the rest of the world's lakes combined."),
    ("What is the study of plants called?", "Botany", ["Zoology", "Geology", "Biology"], "Botany is the scientific study of plant life, a branch of biology."),
    ("Which element has the symbol 'Fe'?", "Iron", ["Gold", "Silver", "Fluorine"], "The symbol 'Fe' comes from 'Ferrum', the Latin word for iron."),
    ("How many hearts does an octopus have?", "3", ["1", "2", "4"], "Two hearts pump blood to the gills, while the third pumps it to the rest of the body."),
    ("Who founded Microsoft?", "Bill Gates", ["Steve Jobs", "Zuckerberg", "Bezos"], "Bill Gates co-founded Microsoft with Paul Allen in 1975."),
    ("Which planet is the hottest?", "Venus", ["Mercury", "Mars", "Jupiter"], "Venus is hotter than Mercury due to its thick atmosphere creating a greenhouse effect."),
    ("What is the largest internal organ?", "Liver", ["Heart", "Lungs", "Stomach"], "The liver is the largest internal organ and is essential for detoxifying chemicals."),
    ("Which war happened between North and South USA?", "Civil War", ["Revolutionary War", "1812 War", "WWI"], "The American Civil War (1861–1865) was fought between the Union and the Confederacy."),
    ("Who wrote the Declaration of Independence?", "Thomas Jefferson", ["Washington", "Adams", "Franklin"], "Jefferson was the primary author of the document adopted in 1776."),
    ("Which country is famous for Sushi?", "Japan", ["China", "Thailand", "Korea"], "Sushi is a traditional Japanese dish of prepared vinegared rice and seafood."),
    ("What is the main gas in the Sun?", "Hydrogen", ["Helium", "Oxygen", "Nitrogen"], "The Sun is composed primarily of hydrogen (about 73%) and helium."),
    ("Who invented the World Wide Web?", "Tim Berners-Lee", ["Bill Gates", "Jobs", "Mark Zuckerberg"], "He invented the WWW in 1989 while working at CERN."),
    ("What is the capital of Brazil?", "Brasilia", ["Rio de Janeiro", "Sao Paulo", "Salvador"], "Brasilia was founded in 1960 to replace Rio de Janeiro as the capital."),
    ("Which metal is liquid at room temperature?", "Mercury", ["Lead", "Gold", "Iron"], "Mercury is the only metallic element that is liquid at standard conditions."),
    ("How many teeth does an adult human typically have?", "32", ["30", "28", "34"], "A full set of adult teeth includes 32 teeth: 8 incisors, 4 canines, 8 premolars, and 12 molars.")
]

trivia_hard_fixed = [
    ("Which is the rarest blood type?", "AB Negative", ["O Negative", "B Positive", "A Negative"], "AB Negative is the rarest blood type, found in less than 1% of the population."),
    ("Which planet spins retrograde (clockwise)?", "Venus", ["Mars", "Jupiter", "Mercury"], "Venus spins in the opposite direction to most planets, so the Sun rises in the west."),
    ("Heaviest naturally occurring element?", "Uranium", ["Lead", "Gold", "Plutonium"], "Uranium (Atomic number 92) is the heaviest element found naturally in significant quantities."),
    ("Value of Absolute Zero?", "-273.15 C", ["-100 C", "0 C", "-459 C"], "Absolute zero is the theoretical temperature at which all particle motion ceases."),
    ("Who wrote 'A Brief History of Time'?", "Stephen Hawking", ["Einstein", "Sagan", "Tyson"], "It is a popular-science book on cosmology by British physicist Stephen Hawking."),
    ("War of 1812 was between?", "USA and Britain", ["USA and Spain", "France and UK", "Russia and Japan"], "The conflict confirmed American independence and resulted in the burning of the White House."),
    ("First city hit by Atomic Bomb?", "Hiroshima", ["Nagasaki", "Tokyo", "Kyoto"], "On August 6, 1945, the US dropped the atomic bomb 'Little Boy' on Hiroshima."),
    ("Berlin Wall fell in which year?", "1989", ["1991", "1985", "1995"], "The fall of the Berlin Wall in 1989 symbolized the end of the Cold War."),
    ("Who is the Father of the Computer?", "Charles Babbage", ["Alan Turing", "Bill Gates", "Jobs"], "Babbage conceived the first automatic digital computer, the Analytical Engine."),
    ("First woman to win a Nobel Prize?", "Marie Curie", ["Mother Teresa", "Rosa Parks", "Earhart"], "She was also the first person to win the Nobel Prize in two different scientific fields."),
    ("Who discovered the structure of DNA?", "Watson and Crick", ["Pasteur", "Darwin", "Fleming"], "They identified the double helix structure of DNA in 1953."),
    ("Who created the Periodic Table?", "Dmitri Mendeleev", ["Bohr", "Rutherford", "Curie"], "Mendeleev arranged elements by atomic mass and predicted the properties of missing elements."),
    ("Who developed the smallpox vaccine?", "Edward Jenner", ["Salk", "Pasteur", "Fleming"], "Jenner's vaccine, developed in 1796, was the world's first successful vaccine."),
    ("Capital of Turkey?", "Ankara", ["Istanbul", "Izmir", "Bursa"], "While Istanbul is the largest city, Ankara has been the capital since 1923."),
    ("Capital of Switzerland?", "Bern", ["Zurich", "Geneva", "Basel"], "Bern is the de facto capital, referred to as the 'federal city'."),
    ("Which geometric shape has faces that are equilateral triangles?", "Tetrahedron", ["Cube", "Octahedron", "Dodecahedron"], "A tetrahedron is a pyramid with a triangular base and three triangular sides."),
    ("How many chromosomes do humans have?", "46", ["48", "44", "42"], "Humans mostly have 23 pairs of chromosomes, for a total of 46."),
    ("Which element has symbol 'W'?", "Tungsten", ["Wolfram", "Tin", "Water"], "The symbol 'W' comes from the element's alternate name, Wolfram."),
    ("What is the study of fungi?", "Mycology", ["Botany", "Virology", "Zoology"], "Mycology is the branch of biology concerned with the study of fungi."),
    ("Who was the first woman in space?", "Valentina Tereshkova", ["Sally Ride", "Mae Jemison", "Collins"], "Tereshkova orbited Earth 48 times in the Vostok 6 mission in 1963."),
    ("What year was the first iPhone released?", "2007", ["2005", "2008", "2006"], "Steve Jobs unveiled the first iPhone on January 9, 2007."),
    ("Which country has the most time zones?", "France", ["Russia", "USA", "China"], "Including its overseas territories, France spans 12 different time zones."),
    ("What is the largest bone in the human body?", "Femur", ["Humerus", "Tibia", "Pelvis"], "The femur is the thigh bone and is the longest and strongest bone in the skeleton."),
    ("Which language has the most native speakers?", "Mandarin Chinese", ["English", "Spanish", "Hindi"], "Mandarin is spoken by roughly 920 million native speakers."),
    ("Which is the only mammal that can fly?", "Bat", ["Flying Squirrel", "Ostrich", "Penguin"], "Bats are the only mammals capable of true and sustained flight."),
    ("What is the study of insects?", "Entomology", ["Etymology", "Biology", "Zoology"], "Entomology is the scientific study of insects."),
    ("Who wrote the 'Odyssey'?", "Homer", ["Plato", "Socrates", "Aristotle"], "The Odyssey is one of two major ancient Greek epic poems attributed to Homer."),
    ("Which planet has the most moons?", "Saturn", ["Jupiter", "Uranus", "Neptune"], "Saturn currently holds the record for the most discovered moons (over 100)."),
    ("What is the smallest bone in the body?", "Stapes", ["Incus", "Malleus", "Femur"], "The stapes is a stirrup-shaped bone in the middle ear."),
    ("Which chemical element is 'K'?", "Potassium", ["Krypton", "Kelvin", "Phosphorus"], "The symbol 'K' comes from the Neo-Latin word 'Kalium'."),
    ("Who painted 'The Last Supper'?", "Leonardo da Vinci", ["Michelangelo", "Raphael", "Donatello"], "This late 15th-century mural painting is located in Milan, Italy."),
    ("Which country is the largest by area?", "Russia", ["Canada", "China", "USA"], "Russia is the largest country in the world, spanning Eastern Europe and Northern Asia."),
    ("What is the capital of New Zealand?", "Wellington", ["Auckland", "Christchurch", "Hamilton"], "Wellington is the southernmost capital of a sovereign state."),
    ("Which year did the Titanic sink?", "1912", ["1905", "1915", "1920"], "The Titanic sank in the North Atlantic Ocean on April 15, 1912."),
    ("Who discovered the electron?", "J.J. Thomson", ["Rutherford", "Bohr", "Chadwick"], "Thomson discovered the electron in 1897, the first subatomic particle to be found.")
]

def generate_questions_from_tuples(data, correct_idx_in_tuple, text_template, expl_template, difficulty, count):
    qs = []
    all_answers = [x[correct_idx_in_tuple] for x in data]
    random.shuffle(data)
    
    for item in data:
        if len(qs) >= count: break
        
        q_text = text_template.format(*item)
        ans = item[correct_idx_in_tuple]
        expl = expl_template.format(*item)
        
        # Distractors (Random check to avoid same answer)
        distractors = random.sample([x for x in all_answers if x != ans], 3)
        options = [ans] + distractors
        random.shuffle(options)
        
        qs.append({
            "text": q_text,
            "options": options,
            "correctIndex": options.index(ans),
            "explanation": expl,
            "difficulty": difficulty
        })
    return qs

def generate_fixed_trivia(data, difficulty, count):
    # data: list of (Question, Answer, [Distractors], Explanation)
    qs = []
    random.shuffle(data)
    
    for item in data:
        if len(qs) >= count: break
        
        q_text = item[0]
        ans = item[1]
        distractors = item[2] # Fixed distractors
        expl = item[3]
        
        options = [ans] + distractors
        random.shuffle(options)
        
        qs.append({
            "text": q_text,
            "options": options,
            "correctIndex": options.index(ans),
            "explanation": expl,
            "difficulty": difficulty
        })
    return qs

def generate_full_treasure_quiz():
    final_l1 = []
    final_l2 = []
    final_l3 = []
    
    # Target: 200 per level
    
    # --- LEVEL 1 ---
    # 50 Capitals
    final_l1.extend(generate_questions_from_tuples(capitals_easy, 1, "Capital of {0}?", "{1} is the capital of {0}.", 1, 60))
    # 40 Elements
    # Elements data: (Symbol, Name) e.g. (H, Hydrogen)
    # Question: "What is H?" -> Hydrogen.
    final_l1.extend(generate_questions_from_tuples(elements, 1, "What element is {0}?", "{0} stands for {1}.", 1, 40))
    
    # Fill remaining with FIXED TRIVIA (High Quality)
    final_l1.extend(generate_fixed_trivia(trivia_easy_fixed, 1, 100))
    
    # RE-STRATEGY: Use ALL available data to max out.
    final_l1.extend(generate_questions_from_tuples(capitals_easy, 1, "Capital of {0}?", "{1} is the capital.", 1, 200))
    # Note: Elements loop above uses symbol->name.
    # Let's add Name->Symbol too for variety?
    # generate_questions_from_tuples(elements, 0, "Symbol for {1}?", "The symbol is {0}.", 1, 100)
    final_l1.extend(generate_questions_from_tuples(elements, 1, "What element is {0}?", "{0} is {1}.", 1, 200))
    
    # --- LEVEL 2 ---
    final_l2.extend(generate_questions_from_tuples(capitals_medium, 1, "Capital of {0}?", "{1} is the capital of {0}.", 2, 200))
    final_l2.extend(generate_fixed_trivia(trivia_medium_fixed, 2, 100))
    # Inventions
    inventions = [
        ("Telephone", "Graham Bell"), ("Light Bulb", "Thomas Edison"), ("Airplane", "Wright Brothers"),
        ("Penicillin", "Alexander Fleming"), ("Dynamite", "Alfred Nobel"), ("Radio", "Marconi"),
        ("World Wide Web", "Berners-Lee"), ("Theory of Relativity", "Einstein"), ("Gravity", "Newton"),
        ("Polio Vaccine", "Salk")
    ]
    final_l2.extend(generate_questions_from_tuples(inventions, 1, "Who invented the {0}?", "{1} invented the {0}.", 2, 50))

    # --- LEVEL 3 ---
    final_l3.extend(generate_questions_from_tuples(capitals_hard, 1, "Capital of {0}?", "{1} is the capital of {0}.", 3, 200))
    final_l3.extend(generate_fixed_trivia(trivia_hard_fixed, 3, 100))
    
    # OLOGIES
    ologies = [
        ("Life", "Biology"), ("Animals", "Zoology"), ("Plants", "Botany"), ("Earth", "Geology"),
        ("Weather", "Meteorology"), ("Stars", "Astronomy"), ("Mind", "Psychology"), ("Society", "Sociology"),
        ("Fossils", "Paleontology"), ("Skin", "Dermatology"), ("Heart", "Cardiology"), ("Insects", "Entomology")
    ]
    final_l3.extend(generate_questions_from_tuples(ologies, 1, "Study of {0}?", "It is called {1}.", 3, 50))

    def process(list_qs, prefix, limit=200):
        random.shuffle(list_qs)
        final = []
        for i, q in enumerate(list_qs):
            if i >= limit: break
            q["id"] = f"{prefix}_{i}"
            final.append(q)
        return final

    return {
        "id": "TREASURE",
        "name": "Treasure",
        "levels": [
            {"id": 1, "questions": process(final_l1, "t_final_l1")},
            {"id": 2, "questions": process(final_l2, "t_final_l2")},
            {"id": 3, "questions": process(final_l3, "t_final_l3")}
        ]
    }

if __name__ == "__main__":
    t_data = generate_full_treasure_quiz()
    with open('app/src/main/assets/treasure.json', 'w') as f:
        json.dump(t_data, f, indent=2)
    print("Correxted Curated Treasure Generated.")
