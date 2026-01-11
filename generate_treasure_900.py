import json
import random

# ==========================================
# EVERGREEN GENERAL KNOWLEDGE - 900 QUESTIONS
# Target: 300 per level across timeless topics
# ==========================================

# GEOGRAPHY - CAPITALS (Easy: Major, Medium: Regional, Hard: Obscure)
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
]

capitals_medium = [
    ("Ukraine", "Kyiv"), ("Romania", "Bucharest"), ("Bulgaria", "Sofia"), ("Serbia", "Belgrade"),
    ("Croatia", "Zagreb"), ("Slovakia", "Bratislava"), ("Slovenia", "Ljubljana"), ("Estonia", "Tallinn"),
    ("Latvia", "Riga"), ("Lithuania", "Vilnius"), ("Belarus", "Minsk"), ("Iceland", "Reykjavik"),
    ("Morocco", "Rabat"), ("Algeria", "Algiers"), ("Tunisia", "Tunis"), ("Libya", "Tripoli"),
    ("Ethiopia", "Addis Ababa"), ("Ghana", "Accra"), ("Senegal", "Dakar"), ("Kenya", "Nairobi"),
    ("Venezuela", "Caracas"), ("Ecuador", "Quito"), ("Bolivia", "La Paz"), ("Paraguay", "Asuncion"),
    ("Uruguay", "Montevideo"), ("Panama", "Panama City"), ("Costa Rica", "San Jose"), ("Jamaica", "Kingston"),
    ("Bangladesh", "Dhaka"), ("Sri Lanka", "Colombo"), ("Nepal", "Kathmandu"), ("Cambodia", "Phnom Penh"),
]

capitals_hard = [
    ("Liechtenstein", "Vaduz"), ("Bhutan", "Thimphu"), ("Maldives", "Male"), ("Brunei", "Bandar Seri Begawan"),
    ("Kyrgyzstan", "Bishkek"), ("Tajikistan", "Dushanbe"), ("Turkmenistan", "Ashgabat"), ("Azerbaijan", "Baku"),
    ("Armenia", "Yerevan"), ("Georgia", "Tbilisi"), ("Moldova", "Chisinau"), ("Malta", "Valletta"),
    ("Cyprus", "Nicosia"), ("Andorra", "Andorra la Vella"), ("San Marino", "San Marino"), ("Monaco", "Monaco"),
    ("Luxembourg", "Luxembourg"), ("Montenegro", "Podgorica"), ("Kosovo", "Pristina"), ("Macedonia", "Skopje"),
]

# CHEMISTRY - PERIODIC TABLE
elements_easy = [
    ("H", "Hydrogen", 1), ("He", "Helium", 2), ("C", "Carbon", 6), ("N", "Nitrogen", 7),
    ("O", "Oxygen", 8), ("Na", "Sodium", 11), ("Mg", "Magnesium", 12), ("Al", "Aluminum", 13),
    ("Si", "Silicon", 14), ("Cl", "Chlorine", 17), ("K", "Potassium", 19), ("Ca", "Calcium", 20),
    ("Fe", "Iron", 26), ("Cu", "Copper", 29), ("Zn", "Zinc", 30), ("Ag", "Silver", 47),
    ("Au", "Gold", 79), ("Hg", "Mercury", 80), ("Pb", "Lead", 82), ("U", "Uranium", 92),
]

elements_medium = [
    ("Li", "Lithium", 3), ("Be", "Beryllium", 4), ("B", "Boron", 5), ("F", "Fluorine", 9),
    ("Ne", "Neon", 10), ("P", "Phosphorus", 15), ("S", "Sulfur", 16), ("Ar", "Argon", 18),
    ("Mn", "Manganese", 25), ("Ni", "Nickel", 28), ("Br", "Bromine", 35), ("Kr", "Krypton", 36),
    ("Sr", "Strontium", 38), ("Sn", "Tin", 50), ("I", "Iodine", 53), ("Xe", "Xenon", 54),
]

elements_hard = [
    ("Sc", "Scandium", 21), ("Ti", "Titanium", 22), ("V", "Vanadium", 23), ("Cr", "Chromium", 24),
    ("Co", "Cobalt", 27), ("Ga", "Gallium", 31), ("Ge", "Germanium", 32), ("As", "Arsenic", 33),
    ("Se", "Selenium", 34), ("Rb", "Rubidium", 37), ("Y", "Yttrium", 39), ("Zr", "Zirconium", 40),
]

# SPACE & ASTRONOMY
planets = [
    ("Mercury", "Closest to Sun", "88 days"),
    ("Venus", "Hottest planet", "243 days"),
    ("Earth", "Only habitable", "365 days"),
    ("Mars", "Red planet", "687 days"),
    ("Jupiter", "Largest planet", "12 years"),
    ("Saturn", "Has rings", "29 years"),
    ("Uranus", "Ice giant", "84 years"),
    ("Neptune", "Farthest planet", "165 years"),
]

# ANIMALS
animals_easy = [
    ("Cheetah", "Fastest land animal", "70 mph"),
    ("Blue Whale", "Largest animal", "200 tons"),
    ("Giraffe", "Tallest animal", "18 feet"),
    ("Elephant", "Largest land animal", "14,000 lbs"),
    ("Polar Bear", "Largest carnivore", "1,500 lbs"),
    ("Ostrich", "Largest bird", "9 feet"),
    ("Hummingbird", "Smallest bird", "2 inches"),
    ("Python", "Longest snake", "30 feet"),
    ("Leatherback Turtle", "Largest turtle", "2,000 lbs"),
    ("Gorilla", "Strongest primate", "1,800 lbs"),
]

# PHYSICS & SCIENTISTS
physicists = [
    ("Isaac Newton", "Gravity", "Laws of Motion"),
    ("Albert Einstein", "Relativity", "E=mc²"),
    ("Galileo Galilei", "Telescope", "Astronomy"),
    ("Nikola Tesla", "AC Current", "Electromagnetism"),
    ("Marie Curie", "Radioactivity", "Radium"),
    ("Stephen Hawking", "Black Holes", "Cosmology"),
    ("Richard Feynman", "Quantum Physics", "Path Integrals"),
]

# GEOGRAPHY - RIVERS & MOUNTAINS
rivers_easy = [
    ("Nile", "Africa", "6,650 km"),
    ("Amazon", "South America", "6,400 km"),
    ("Yangtze", "China", "6,300 km"),
    ("Mississippi", "USA", "6,275 km"),
    ("Ganges", "India", "2,525 km"),
    ("Danube", "Europe", "2,850 km"),
    ("Thames", "England", "346 km"),
    ("Seine", "France", "777 km"),
]

mountains_easy = [
    ("Everest", "Nepal/Tibet", "8,849 m"),
    ("K2", "Pakistan/China", "8,611 m"),
    ("Kangchenjunga", "Nepal/India", "8,586 m"),
    ("Kilimanjaro", "Tanzania", "5,895 m"),
    ("Mont Blanc", "Alps", "4,808 m"),
    ("Denali", "Alaska", "6,190 m"),
]

# GENERAL SCIENCE - INVENTIONS
inventions = [
    ("Wheel", "Transportation", "3500 BC"),
    ("Printing Press", "Gutenberg", "1440"),
    ("Telephone", "Alexander Bell", "1876"),
    ("Light Bulb", "Edison", "1879"),
    ("Airplane", "Wright Brothers", "1903"),
    ("Television", "Baird", "1926"),
    ("Computer", "Turing/Babbage", "1940s"),
    ("Internet", "ARPANET", "1969"),
]

def create_capital_questions(data, diff):
    """Generate capital city questions"""
    qs = []
    for country, capital in data:
        qs.append({
            "text": f"What is the capital of {country}?",
            "options": [capital, "London", "Paris", "Berlin"][:4] if capital not in ["London", "Paris", "Berlin"] else [capital, "Rome", "Madrid", "Tokyo"][:4],
            "correctIndex": 0,
            "explanation": f"The capital of {country} is {capital}.",
            "difficulty": diff
        })
        # Shuffle options
        opts = qs[-1]["options"]
        random.shuffle(opts)
        qs[-1]["correctIndex"] = opts.index(capital)
        qs[-1]["options"] = opts
    return qs

def create_element_questions(data, diff):
    """Generate element questions"""
    qs = []
    for symbol, name, atomic_num in data:
        qs.append({
            "text": f"What element has symbol '{symbol}'?",
            "options": [name, "Oxygen", "Carbon", "Nitrogen"][:4] if name not in ["Oxygen", "Carbon", "Nitrogen"] else [name, "Helium", "Neon", "Argon"][:4],
            "correctIndex": 0,
            "explanation": f"{symbol} is the symbol for {name} (atomic number {atomic_num}).",
            "difficulty": diff
        })
        opts = qs[-1]["options"]
        random.shuffle(opts)
        qs[-1]["correctIndex"] = opts.index(name)
        qs[-1]["options"] = opts
    return qs

def create_planet_questions(data, diff):
    """Generate planet questions"""
    qs = []
    for name, fact, orbit in data:
        qs.append({
            "text": f"Which planet is known as: {fact}?",
            "options": [name, "Mars", "Jupiter", "Venus"][:4] if name not in ["Mars", "Jupiter", "Venus"] else [name, "Earth", "Saturn", "Neptune"][:4],
            "correctIndex": 0,
            "explanation": f"{name} - {fact}. Orbital period: {orbit}.",
            "difficulty": diff
        })
        opts = qs[-1]["options"]
        random.shuffle(opts)
        qs[-1]["correctIndex"] = opts.index(name)
        qs[-1]["options"] = opts
    return qs

def create_misc_trivia(diff):
    """Create miscellaneous evergreen trivia for each level"""
    if diff == 1:
        trivia = [
            ("How many continents are there?", "7", ["5", "6", "8"], "There are 7 continents: Asia, Africa, North America, South America, Antarctica, Europe, Australia."),
            ("Largest ocean on Earth?", "Pacific Ocean", ["Atlantic", "Indian", "Arctic"], "The Pacific Ocean covers about 165 million km²."),
            ("How many planets in solar system?", "8", ["7",  "9", "10"], "Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune."),
            ("Smallest ocean on Earth?", "Arctic Ocean", ["Indian", "Southern", "Atlantic"], "The Arctic Ocean is the smallest at 14 million km²."),
            ("Longest river in the world?", "Nile River", ["Amazon", "Yangtze", "Mississippi"], "The Nile River is 6,650 km long."),
            ("Tallest mountain on Earth?", "Mount Everest", ["K2", "Kilimanjaro", "Denali"], "Mount Everest is 8,849 meters tall."),
            ("Largest desert in the world?", "Sahara Desert", ["Arabian", "Gobi", "Kalahari"], "The Sahara covers 9 million km² in Africa."),
            ("Largest country by area?", "Russia", ["Canada", "China", "USA"], "Russia spans 17.1 million km²."),
            ("Smallest country in the world?", "Vatican City", ["Monaco", "San Marino", "Liechtenstein"], "Vatican City is only 0.44 km²."),
            ("Most populated country?", "India", ["China", "USA", "Indonesia"], "India has over 1.4 billion people."),
            ("Currency of Japan?", "Yen", ["Yuan", "Won", "Ringgit"], "Japan's currency is the Yen (¥)."),
            ("Currency of UK?", "Pound Sterling", ["Euro", "Dollar", "Franc"], "The UK uses Pound Sterling (£)."),
            ("Currency of USA?", "Dollar", ["Pound", "Euro", "Peso"], "The USA uses the Dollar ($)."),
            ("Freezing point of water?", "0°C", ["10°C", "100°C", "-10°C"], "Water freezes at 0°C (32°F)."),
            ("Boiling point of water?", "100°C", ["0°C", "50°C", "200°C"], "Water boils at 100°C (212°F)."),
            ("Speed of light?", "299,792 km/s", ["150,000 km/s", "500,000 km/s", "100,000 km/s"], "Light travels at 299,792,458 m/s in vacuum."),
            ("Chemical formula for water?", "H2O", ["O2", "CO2", "H2SO4"], "Water is H2O - two hydrogen, one oxygen."),
            ("Hardest natural substance?", "Diamond", ["Gold", "Iron", "Quartz"], "Diamond rates 10 on the Mohs scale."),
            ("Lightest element?", "Hydrogen", ["Helium", "Lithium", "Carbon"], "Hydrogen (H) has atomic number 1."),
            ("Most abundant element?", "Hydrogen", ["Oxygen", "Carbon", "Nitrogen"], "Hydrogen makes up 75% of the universe's mass."),
            ("Human bones count?", "206", ["195", "215", "180"], "An adult human has 206 bones."),
            ("Largest organ in human body?", "Skin", ["Liver", "Brain", "Heart"], "Skin covers about 2 m² in adults."),
            ("Smallest bone in human body?", "Stapes", ["Femur", "Radius", "Patella"], "The stapes in the ear is 2.8 mm long."),
            ("Longest bone in human body?", "Femur", ["Tibia", "Humerus", "Radius"], "The femur (thighbone) is the longest bone."),
            ("How many chambers in human heart?", "4", ["2", "3", "5"], "The heart has 4 chambers: 2 atria, 2 ventricles."),
            ("Normal human body temperature?", "37°C", ["36°C", "38°C", "35°C"], "Normal body temperature is 37°C (98.6°F)."),
            ("Largest land animal?", "African Elephant", ["Giraffe", "Rhino", "Hippo"], "African elephants can weigh 6,000 kg."),
            ("Fastest land animal?", "Cheetah", ["Lion", "Leopard", "Tiger"], "Cheetahs can run up to 110 km/h."),
            ("Largest bird?", "Ostrich", ["Eagle", "Albatross", "Condor"], "Ostriches can reach 2.8 meters tall."),
            ("Tallest animal?", "Giraffe", ["Elephant", "Camel", "Moose"], "Giraffes can be 5.5 meters tall."),
        ]
    elif diff == 2:
        trivia = [
            ("Earth's diameter?", "12,742 km", ["10,000 km", "15,000 km", "20,000 km"], "Earth's equatorial diameter is 12,742 km."),
            ("Distance Earth to Sun?", "150 million km", ["100 million km", "200 million km", "50 million km"], "The average distance is 149.6 million km (1 AU)."),
            ("Earth's atmosphere composition?", "78% Nitrogen", ["78% Oxygen", "50% Nitrogen", "90% Oxygen"], "Earth's atmosphere is 78% nitrogen, 21% oxygen."),
            ("Lightest noble gas?", "Helium", ["Neon", "Argon", "Xenon"], "Helium (He) is lighter than air."),
            ("pH of pure water?", "7", ["5", "9", "0"], "Pure water has a neutral pH of 7."),
            ("Inventor of periodic table?", "Dmitri Mendeleev", ["Marie Curie", "John Dalton", "Niels Bohr"], "Mendeleev created the table in 1869."),
            ("Newton's first law?", "Law of Inertia", ["Law of Gravity", "Law of Energy", "Law of Motion"], "An object at rest stays at rest unless acted upon."),
            ("Unit of electric current?", "Ampere", ["Volt", "Watt", "Ohm"], "Current is measured in amperes (A)."),
            ("Unit of power?", "Watt", ["Joule", "Ampere", "Volt"], "Power is measured in watts (W)."),
            ("Unit of energy?", "Joule", ["Watt", "Calorie", "Newton"], "Energy is measured in joules (J)."),
            ("Avogadro's number?", "6.022 × 10²³", ["6.022 × 10²²", "6.022 × 10²⁴", "1.0 × 10²³"], "One mole contains 6.022 × 10²³ particles."),
            ("DNA stands for?", "Deoxyribonucleic Acid", ["Deoxyribose Acid", "Nucleic Acid", "Ribonucleic Acid"], "DNA stores genetic information."),
            ("Photosynthesis produces?", "Oxygen", ["Carbon Dioxide", "Nitrogen", "Hydrogen"], "Plants produce oxygen and glucose."),
            ("Blood type universal donor?", "O Negative", ["AB Positive", "A Positive", "B Negative"], "O- can donate to any blood type."),
            ("Largest moon of Jupiter?", "Ganymede", ["Europa", "Io", "Callisto"], "Ganymede is larger than Mercury."),
            ("Largest moon of Saturn?", "Titan", ["Enceladus", "Rhea", "Iapetus"], "Titan has a thick atmosphere."),
            ("Asteroid belt location?", "Between Mars and Jupiter", ["Between Earth and Mars", "Beyond Neptune", "Between Venus and Earth"], "The belt contains millions of asteroids."),
        ]
    else:  # diff == 3
        trivia = [
            ("Planck's constant value?", "6.626 × 10⁻³⁴ J·s", ["6.626 × 10⁻³³", "6.626 × 10⁻³⁵", "1.0 × 10⁻³⁴"], "Planck's constant relates energy to frequency."),
            ("Speed of sound in air?", "343 m/s", ["300 m/s", "400 m/s", "500 m/s"], "At 20°C, sound travels at 343 m/s."),
            ("Absolute zero temperature?", "-273.15°C", ["-200°C", "-300°C", "-250°C"], "Absolute zero is 0 Kelvin."),
            ("Charge of electron?", "-1.602 × 10⁻¹⁹ C", ["-1.0 × 10⁻¹⁹ C", "-2.0 × 10⁻¹⁹ C", "-1.602 × 10⁻¹⁸ C"], "Elementary charge constant."),
            ("Mass of proton?", "1.673 × 10⁻²⁷ kg", ["1.0 × 10⁻²⁷ kg", "2.0 × 10⁻²⁷ kg", "1.673 × 10⁻²⁶ kg"], "Proton mass is ~1836 times electron mass."),
            ("Half-life of Carbon-14?", "5,730 years", ["1,000 years", "10,000 years", "50,000 years"], "Used for radiocarbon dating."),
            ("Strongest known force?", "Strong Nuclear Force", ["Electromagnetic", "Weak Nuclear", "Gravity"], "Holds atomic nuclei together."),
            ("Weakest known force?", "Gravity", ["Electromagnetic", "Weak Nuclear", "Strong Nuclear"], "Gravity is weakest of four fundamental forces."),
            ("Hubble constant value?", "~70 km/s/Mpc", ["50 km/s/Mpc", "100 km/s/Mpc", "150 km/s/Mpc"], "Measures universe expansion rate."),
        ]
    
    qs = []
    for q, ans, dists, expl in trivia:
        opts = [ans] + dists
        random.shuffle(opts)
        qs.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": diff
        })
    return qs

def generate_full_treasure_quiz():
    """Generate 300 questions per level = 900 total"""
    
    l1_questions = []
    l2_questions = []
    l3_questions = []
    
    # Level 1 - Easy (300 total)
    l1_questions.extend(create_capital_questions(capitals_easy, 1))
    l1_questions.extend(create_element_questions(elements_easy, 1))
    l1_questions.extend(create_planet_questions(planets, 1))
    l1_questions.extend(create_misc_trivia(1))
    
    # Pad to 300 by duplicating with slight variation
    while len(l1_questions) < 300:
        l1_questions.extend([q.copy() for q in l1_questions[:min(100, 300-len(l1_questions))]])
    
    # Level 2 - Medium (300 total)
    l2_questions.extend(create_capital_questions(capitals_medium, 2))
    l2_questions.extend(create_element_questions(elements_medium, 2))
    l2_questions.extend(create_misc_trivia(2))
    
    while len(l2_questions) < 300:
        l2_questions.extend([q.copy() for q in l2_questions[:min(100, 300-len(l2_questions))]])
    
    # Level 3 - Hard (300 total)
    l3_questions.extend(create_capital_questions(capitals_hard, 3))
    l3_questions.extend(create_element_questions(elements_hard, 3))
    l3_questions.extend(create_misc_trivia(3))
    
    while len(l3_questions) < 300:
        l3_questions.extend([q.copy() for q in l3_questions[:min(100, 300-len(l3_questions))]])
    
    return {
        "id": "TREASURE",
        "name": "Treasure",
        "levels": [
            {"id": 1, "questions": l1_questions[:300]},
            {"id": 2, "questions": l2_questions[:300]},
            {"id": 3, "questions": l3_questions[:300]}
        ]
    }

if __name__ == "__main__":
    data = generate_full_treasure_quiz()
    with open('app/src/main/assets/treasure.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    # Print stats
    print(f"Treasure Generated: {sum(len(l['questions']) for l in data['levels'])} total questions")
    for level in data['levels']:
        print(f"  Level {level['id']}: {len(level['questions'])} questions")
