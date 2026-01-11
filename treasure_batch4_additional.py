import json
import random

# BATCH 4: Additional questions to reduce duplication
# Target: 45 Easy, 88 Medium, 99 Hard = 232 total

def create_batch4_additional():
    """Additional questions to minimize duplication"""
    
    # LEVEL 1 - EASY (45 questions)
    easy_additional = []
    
    # Currencies (20 questions)
    currencies = [
        ("Euro used in?", "European Union", ["USA", "UK", "Asia"], "Euro (€) is used by 19 EU countries."),
        ("Dollar used in?", "USA", ["Europe", "Japan", "India"], "US Dollar ($) is most traded currency."),
        ("Yen is currency of?", "Japan", ["China", "Korea", "Thailand"], "Japanese Yen (¥) since 1871."),
        ("Pound Sterling used in?", "United Kingdom", ["Europe", "USA", "Australia"], "British Pound (£) is oldest currency still used."),
        ("Rupee is currency of?", "India", ["Pakistan only", "Bangladesh only", "China"], "Indian Rupee (₹) symbol adopted 2010."),
        ("Yuan is currency of?", "China", ["Japan", "Korea", "Vietnam"], "Chinese Yuan (¥) or Renminbi."),
        ("Ruble is currency of?", "Russia", ["Poland", "Ukraine", "Germany"], "Russian Ruble (₽) since 13th century."),
        ("Won is currency of?", "South Korea", ["Japan", "China", "Thailand"], "South Korean Won (₩)."),
        ("Franc used in?", "Switzerland", ["France", "Germany", "Italy"], "Swiss Franc (CHF) - France uses Euro now."),
        ("Peso used in?", "Mexico", ["USA", "Brazil", "Canada"], "Mexican Peso ($) and others."),
        ("Lira used in?", "Turkey", ["Italy", "Greece", "Spain"], "Turkish Lira (₺) - Italy uses Euro now."),
        ("Baht is currency of?", "Thailand", ["Vietnam", "Malaysia", "Indonesia"], "Thai Baht (฿)."),
        ("Ringgit is currency of?", "Malaysia", ["Indonesia", "Singapore", "Thailand"], "Malaysian Ringgit (RM)."),
        ("Dirham used in?", "UAE", ["Saudi Arabia", "Kuwait", "Qatar"], "UAE Dirham (د.إ)."),
        ("Riyal used in?", "Saudi Arabia", ["UAE", "Kuwait", "Iraq"], "Saudi Riyal (﷼)."),
    ]
    
    for q, ans, dists, expl in currencies:
        opts = [ans] + dists
        random.shuffle(opts)
        easy_additional.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 1
        })
    
    # Human Body (15 questions)
    body_facts = [
        ("How many teeth in adult human?", "32", ["28", "36", "24"], "32 permanent teeth including wisdom teeth."),
        ("How many muscles in human body?", "~640", ["200", "400", "1000"], "Over 640 skeletal muscles."),
        ("Largest muscle?", "Gluteus Maximus", ["Biceps", "Quadriceps", "Heart"], "Buttock muscle is largest."),
        ("Smallest muscle?", "Stapedius", ["Biceps", "Eye muscle", "Finger muscle"], "Stapedius in ear is smallest."),
        ("Longest organ?", "Small Intestine", ["Large Intestine", "Liver", "Skin"], "Small intestine is ~7 meters long."),
        ("Heaviest organ?", "Liver", ["Brain", "Skin", "Heart"], "Liver weighs ~1.5 kg."),
        ("What percentage of body is water?", "~60%", ["40%", "80%", "90%"], "Adults are about 60% water."),
        ("How many blood groups (ABO)?", "4", ["2", "6", "8"], "A, B, AB, O blood types."),
        ("Normal heart rate?", "60-100 bpm", ["40-60 bpm", "100-120 bpm", "120-140 bpm"], "Resting heart rate for adults."),
        ("Average blood volume?", "~5 liters", ["3 liters", "10 liters", "15 liters"], "Adults have about 5 liters of blood."),
        ("How many lungs?", "2", ["1", "3", "4"], "Left and right lungs."),
        ("How many kidneys?", "2", ["1", "3", "4"], "Two kidneys filter blood."),
        ("Smallest bone location?", "Ear", ["Hand", "Foot", "Nose"], "Stapes bone is in the ear."),
        ("Largest bone location?", "Thigh", ["Arm", "Spine", "Leg"], "Femur is in the thigh."),
        ("Brain weight?", "~1.4 kg", ["0.5 kg", "2 kg", "3 kg"], "Adult brain weighs about 1.4 kg."),
    ]
    
    for q, ans, dists, expl in body_facts:
        opts = [ans] + dists
        random.shuffle(opts)
        easy_additional.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 1
        })
    
    # Basic Math & Units (10 questions)
    math_units = [
        ("1000 meters equals?", "1 kilometer", ["100 meters", "10 kilometers", "1 mile"], "1 km = 1000 m."),
        ("1000 grams equals?", "1 kilogram", ["100 grams", "10 kilograms", "1 pound"], "1 kg = 1000 g."),
        ("1000 milliliters equals?", "1 liter", ["100 ml", "10 liters", "1 gallon"], "1 L = 1000 mL."),
        ("100 centimeters equals?", "1 meter", ["10 meters", "1000 meters", "1 kilometer"], "1 m = 100 cm."),
        ("60 seconds equals?", "1 minute", ["10 seconds", "100 seconds", "1 hour"], "1 min = 60 sec."),
        ("60 minutes equals?", "1 hour", ["30 minutes", "100 minutes", "1 day"], "1 hr = 60 min."),
        ("24 hours equals?", "1 day", ["12 hours", "48 hours", "1 week"], "1 day = 24 hours."),
        ("7 days equals?", "1 week", ["10 days", "14 days", "1 month"], "1 week = 7 days."),
        ("12 months equals?", "1 year", ["6 months", "24 months", "1 decade"], "1 year = 12 months."),
        ("100 years equals?", "1 century", ["50 years", "1000 years", "1 decade"], "1 century = 100 years."),
    ]
    
    for q, ans, dists, expl in math_units:
        opts = [ans] + dists
        random.shuffle(opts)
        easy_additional.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 1
        })
    
    # LEVEL 2 - MEDIUM (88 questions)
    medium_additional = []
    
    # More Countries & States (30 questions)
    countries_medium = [
        ("Largest US state by area?", "Alaska", ["Texas", "California", "Montana"], "Alaska is 1.7 million km²."),
        ("Most populous US state?", "California", ["Texas", "New York", "Florida"], "California has 39 million people."),
        ("US capital?", "Washington D.C.", ["New York", "Los Angeles", "Chicago"], "D.C. is not a state."),
        ("India has how many states?", "28", ["25", "30", "35"], "28 states and 8 union territories."),
        ("China's most populous city?", "Shanghai", ["Beijing", "Guangzhou", "Shenzhen"], "Shanghai: 24+ million people."),
        ("Japan consists of how many main islands?", "4", ["2", "6", "10"], "Honshu, Hokkaido, Kyushu, Shikoku."),
        ("What language in Brazil?", "Portuguese", ["Spanish", "English", "French"], "Brazil is only Portuguese-speaking country in Americas."),
        ("What language in Mexico?", "Spanish", ["Portuguese", "English", "French"], "Spanish is official language."),
        ("What language in Canada?", "English and French", ["Only English", "Only French", "Spanish"], "Canada is bilingual."),
        ("Switzerland has how many official languages?", "4", ["1", "2", "3"], "German, French, Italian, Romansh."),
        ("Landlocked country?", "Switzerland", ["France", "Spain", "Italy"], "Landlocked = no ocean coast."),
        ("Which is NOT landlocked?", "France", ["Switzerland", "Austria", "Czech Republic"], "France has Mediterranean and Atlantic  coasts."),
        ("Lowest country?", "Netherlands", ["Belgium", "Denmark", "Poland"], "26% of Netherlands is below sea level."),
        ("Highest average elevation?", "Bhutan", ["Nepal", "Tibet", "Switzerland"], "Bhutan's average elevation is 3,280 m."),
        ("Driest continent?", "Antarctica", ["Africa", "Australia", "Asia"], "Antarctica is technically a desert."),
    ]
    
    for q, ans, dists, expl in countries_medium:
        opts = [ans] + dists
        random.shuffle(opts)
        medium_additional.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 2
        })
    
    # Physics & Scientists (30 questions)
    scientists_medium = [
        ("Theory of Relativity?", "Albert Einstein", ["Isaac Newton", "Galileo", "Hawking"], "Einstein published relativity 1905-1915."),
        ("Laws of Motion?", "Isaac Newton", ["Einstein", "Galileo", "Kepler"], "Newton's three laws of motion."),
        ("Telescope invention?", "Galileo Galilei", ["Newton", "Einstein", "Copernicus"], "Galileo improved telescope in 1609."),
        ("Heliocentric model?", "Nicolaus Copernicus", ["Galileo", "Ptolemy", "Kepler"], "Copernicus proposed Sun at center."),
        ("Discovered radioactivity?", "Marie Curie", ["Einstein", "Newton", "Bohr"], "Curie discovered radium and polonium."),
        ("Black hole research?", "Stephen Hawking", ["Einstein", "Newton", "Bohr"], "Hawking radiation and singularities."),
        ("Atom model?", "Niels Bohr", ["Einstein", "Rutherford", "Thomson"], "Bohr model of atomic structure."),
        ("Discovered electron?", "J.J. Thomson", ["Bohr", "Rutherford", "Planck"], "Thomson discovered electron 1897."),
        ("Discovered neutron?", "James Chadwick", ["Rutherford", "Bohr", "Thomson"], "Chadwick discovered neutron 1932."),
        ("Quantum theory founder?", "Max Planck", ["Einstein", "Bohr", "Heisenberg"], "Planck introduced quantum concept 1900."),
        ("Uncertainty principle?", "Werner Heisenberg", ["Schrödinger", "Bohr", "Planck"], "Cannot know position and momentum precisely."),
        ("Wave-particle duality?", "Louis de Broglie", ["Einstein", "Planck", "Bohr"], "Particles exhibit wave properties."),
        ("Discovered penicillin?", "Alexander Fleming", ["Pasteur", "Koch", "Curie"], "Fleming discovered penicillin 1928."),
        ("Germ theory?", "Louis Pasteur", ["Fleming", "Koch", "Lister"], "Pasteur proved microorganisms cause disease."),
        ("Evolution theory?", "Charles Darwin", ["Lamarck", "Wallace", "Mendel"], "Darwin's natural selection theory."),
    ]
    
    for q, ans, dists, expl in scientists_medium:
        opts = [ans] + dists
        random.shuffle(opts)
        medium_additional.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 2
        })
    
    # More elements & compounds (28 questions)
    compounds_medium = [
        ("Table salt formula?", "NaCl", ["KCl", "CaCl2", "MgCl2"], "Sodium chloride."),
        ("Baking soda formula?", "NaHCO3", ["Na2CO3", "NaCl", "NaOH"], "Sodium bicarbonate."),
        ("Vinegar main component?", "Acetic acid", ["Citric acid", "Sulfuric acid", "Hydrochloric acid"], "CH3COOH in vinegar."),
        ("Ammonia formula?", "NH3", ["NH4", "N2H4", "NO2"], "Nitrogen and hydrogen compound."),
        ("Methane formula?", "CH4", ["C2H6", "C3H8", "CO2"], "Simplest hydrocarbon."),
        ("Ozone formula?", "O3", ["O2", "O4", "H2O2"], "Three oxygen atoms."),
        ("Hydrogen peroxide?", "H2O2", ["H2O", "HO2", "H3O"], "Used as disinfectant."),
        ("Sulfuric acid formula?", "H2SO4", ["HCl", "HNO3", "H3PO4"], "Strong acid, battery acid."),
        ("Hydrochloric acid?", "HCl", ["H2SO4", "HNO3", "H3PO4"], "Stomach acid."),
        ("Nitric acid formula?", "HNO3", ["H2SO4", "HCl", "H3PO4"], "Strong oxidizing acid."),
        ("Glucose formula?", "C6H12O6", ["C12H22O11", "C2H6O", "CH4"], "Blood sugar molecule."),
        ("Sucrose formula?", "C12H22O11", ["C6H12O6", "C2H6O", "CH4"], "Table sugar."),
        ("Ethanol formula?", "C2H6O", ["CH4", "C6H12O6", "C3H8"], "Alcohol in beverages."),
        ("Carbon dioxide uses?", "Photosynthesis, fire extinguisher", ["Breathing", "Burning", "Cleaning"], "CO2 is plant food."),
    ]
    
    for q, ans, dists, expl in compounds_medium:
        opts = [ans] + dists
        random.shuffle(opts)
        medium_additional.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 2
        })
    
    # LEVEL 3 - HARD (99 questions)
    hard_additional = []
    
    # Advanced Physics Constants (30 questions)
    constants_hard = [
        ("Gravitational constant G?", "6.674 × 10⁻¹¹ N·m²/kg²", ["6.674 × 10⁻¹⁰", "6.674 × 10⁻¹²", "1.0 × 10⁻¹¹"], "Universal gravitation constant."),
        ("Fine structure constant α?", "~1/137", ["~1/100", "~1/200", "~1/50"], "Electromagnetic coupling constant."),
        ("Boltzmann constant?", "1.381 × 10⁻²³ J/K", ["1.381 × 10⁻²²", "1.381 × 10⁻²⁴", "1.0 × 10⁻²³"], "Links temperature to energy."),
        ("Gas constant R?", "8.314 J/(mol·K)", ["8.314 J/K", "8.314 J/mol", "10.0 J/(mol·K)"], "Universal gas constant."),
        ("Stefan-Boltzmann constant?", "5.670 × 10⁻⁸ W/(m²·K⁴)", ["5.670 × 10⁻⁷", "5.670 × 10⁻⁹", "1.0 × 10⁻⁸"], "Blackbody radiation."),
        ("Rydberg constant?", "1.097 × 10⁷ m⁻¹", ["1.097 × 10⁶", "1.097 × 10⁸", "1.0 × 10⁷"], "Atomic spectra."),
        ("Vacuum permittivity ε₀?", "8.854 × 10⁻¹² F/m", ["8.854 × 10⁻¹¹", "8.854 × 10⁻¹³", "1.0 × 10⁻¹²"], "Electric constant."),
        ("Vacuum permeability μ₀?", "4π × 10⁻⁷ H/m", ["4π × 10⁻⁶", "4π × 10⁻⁸", "1.0 × 10⁻⁷"], "Magnetic constant."),
        ("Impedance of free space?", "377 Ω", ["300 Ω", "400 Ω", "500 Ω"], "Z₀ = √(μ₀/ε₀)."),
        ("Faraday constant F?", "96,485 C/mol", ["96,485 J/mol", "96,485 N/mol", "100,000 C/mol"], "Charge per mole of electrons."),
    ]
    
    for q, ans, dists, expl in constants_hard:
        opts = [ans] + dists
        random.shuffle(opts)
        hard_additional.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 3
        })
    
    # Mathematical Constants (20 questions)
    math_constants = [
        ("Value of π (pi)?", "3.14159...", ["2.71828...", "1.61803...", "2.30258..."], "Circumference/diameter ratio."),
        ("Value of e (Euler's number)?", "2.71828...", ["3.14159...", "1.61803...", "1.41421..."], "Base of natural logarithm."),
        ("Golden ratio φ?", "1.61803...", ["3.14159...", "2.71828...", "1.41421..."], "φ = (1+√5)/2."),
        ("√2 (square root of 2)?", "1.41421...", ["1.73205...", "1.61803...", "2.0"], "Diagonal of unit square."),
        ("√3 (square root of 3)?", "1.73205...", ["1.41421...", "1.61803...", "2.0"], "Height of equilateral triangle."),
        ("Natural log of 10?", "2.30258...", ["2.71828...", "1.0", "3.14159..."], "ln(10) ≈ 2.303."),
        ("Euler-Mascheroni constant γ?", "0.57721...", ["1.0", "0.5", "1.61803..."], "Limit involving harmonic series."),
        ("Apéry's constant ζ(3)?", "1.20205...", ["1.0", "2.0", "3.0"], "Sum of cubes of reciprocals."),
        ("Catalan's constant?", "0.91596...", ["1.0", "0.5", "1.5"], "Combinatorics constant."),
        ("Feigenbaum constant δ?", "4.66920...", ["3.14159...", "2.71828...", "1.61803..."], "Chaos theory."),
    ]
    
    for q, ans, dists, expl in math_constants:
        opts = [ans] + dists
        random.shuffle(opts)
        hard_additional.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 3
        })
    
    # Advanced Chemistry (25 questions)
    advanced_chem = [
        ("Electronegativity scale?", "Pauling scale", ["Mohs scale", "pH scale", "Kelvin scale"], "Measures atom's electron attraction."),
        ("Most electronegative element?", "Fluorine", ["Oxygen", "Chlorine", "Nitrogen"], "F has highest electronegativity."),
        ("Noble gas configuration?", "Full outer shell", ["Empty outer shell", "One electron", "Seven electrons"], "Stable electron arrangement."),
        ("Hund's rule?", "Maximize unpaired electrons", ["Pair all electrons", "Minimize energy", "Fill lowest first"], "Orbital filling rule."),
        ("Pauli exclusion principle?", "No two electrons same quantum state", ["Electrons pair up", "Orbitals fill sequentially", "Energy minimized"], "Quantum mechanics rule."),
        ("Aufbau principle?", "Fill lowest energy orbitals first", ["Fill highest first", "Random filling", "Pair electrons"], "Electron configuration rule."),
        ("Oxidation state of O in H2O?", "-2", ["+2", "0", "-1"], "Oxygen usually -2."),
        ("Oxidation state of H in H2O?", "+1", ["-1", "0", "+2"], "Hydrogen usually +1."),
        ("Valence electrons in Carbon?", "4", ["2", "6", "8"], "Carbon has 4 valence electrons."),
        ("Valence electrons in Nitrogen?", "5", ["3", "7", "8"], "Nitrogen has 5 valence electrons."),
        ("Valence electrons in Oxygen?", "6", ["2", "4", "8"], "Oxygen has 6 valence electrons."),
        ("Octet rule?", "Atoms want 8 valence electrons", ["Atoms want 10 electrons", "Atoms want 2 electrons", "Atoms want 16 electrons"], "Stability through full shell."),
        ("What is hybridization?", "Mixing atomic orbitals", ["Breaking bonds", "Forming ions", "Electron transfer"], "sp, sp², sp³ hybrids."),
        ("sp³ hybridization geometry?", "Tetrahedral", ["Linear", "Trigonal", "Octahedral"], "4 bonds, 109.5° angles."),
        ("sp² hybridization geometry?", "Trigonal planar", ["Tetrahedral", "Linear", "Octahedral"], "3 bonds, 120° angles."),
        ("sp hybridization geometry?", "Linear", ["Tetrahedral", "Trigonal", "Bent"], "2 bonds, 180° angle."),
        ("VSEPR theory predicts?", "Molecular geometry", ["Electron configuration", "Bond strength", "Melting point"], "Valence shell electron pair repulsion."),
        ("London dispersion forces?", "Weakest intermolecular force", ["Strongest force", "Ionic bond", "Covalent bond"], "Van der Waals forces."),
        ("Hydrogen bonding occurs with?", "F, O, N", ["C, H, S", "All elements", "Metals only"], "Highly electronegative atoms."),
        ("Dipole-dipole forces?", "Between polar molecules", ["Between nonpolar molecules", "Within molecules", "In metals"], "Permanent dipole interaction."),
        ("Ionic bond forms between?", "Metal and nonmetal", ["Two metals", "Two nonmetals", "Noble gases"], "Electron transfer."),
        ("Covalent bond forms between?", "Nonmetals", ["Metals", "Metal and nonmetal", "Noble gases"], "Electron sharing."),
        ("Metallic bond features?", "Sea of delocalized electrons", ["Electron transfer", "Electron sharing", "No electrons"], "Explains conductivity."),
        ("Lewis structure shows?", "Valence electrons and bonds", ["All electrons", "Nucleus", "Energy levels"], "Dot diagram."),
        ("Formal charge formula?", "V - N - B/2", ["V + N + B", "V - N + B", "V + N - B"], "V=valence, N=nonbonding, B=bonding."),
    ]
    
    for q, ans, dists, expl in advanced_chem:
        opts = [ans] + dists
        random.shuffle(opts)
        hard_additional.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 3
        })
    
    # Earth Science (24 questions)
    earth_science = [
        ("Mohs hardness of diamond?", "10", ["5", "8", "12"], "Hardest natural material."),
        ("Mohs hardness of talc?", "1", ["2", "5", "10"], "Softest mineral on Mohs scale."),
        ("What is igneous rock?", "Formed from cooled magma", ["Sedimentary layers", "Metamorphic transformation", "Organic material"], "Volcanic origin."),
        ("What is sedimentary rock?", "Formed from compressed sediments", ["Cooled magma", "Metamorphic transformation", "Crystallized minerals"], "Layered structure."),
        ("What is metamorphic rock?", "Transformed by heat/pressure", ["Cooled magma", "Compressed sediments", "Organic deposits"], "Changed form."),
        ("Example of igneous rock?", "Granite", ["Limestone", "Marble", "Sandstone"], "Cooled magma rock."),
        ("Example of sedimentary rock?", "Limestone", ["Granite", "Marble", "Basalt"], "Compressed shells/sediments."),
        ("Example of metamorphic rock?", "Marble", ["Granite", "Limestone", "Sandstone"], "Metamorphosed limestone."),
        ("Earth's core composition?", "Iron and nickel", ["Silicon", "Carbon", "Aluminum"], "Metallic core."),
        ("Earth's mantle composition?", "Silicate rocks", ["Iron", "Carbon", "Water"], "Rocky mantle."),
        ("Earth's crust composition?", "Oxygen and silicon", ["Iron", "Carbon", "Nitrogen"], "Silicate minerals."),
        ("Continental crust vs oceanic?", "Continental is thicker", ["Oceanic is thicker", "Same thickness", "No difference"], "Continental 30-70km, oceanic 5-10km."),
        ("What causes earthquakes?", "Plate movement", ["Volcanic eruptions", "Meteor impacts", "Ocean currents"], "Tectonic stress release."),
        ("What causes volcanoes?", "Magma reaching surface", ["Earthquake", "Erosion", "Sedimentation"], "Molten rock eruption."),
        ("What is magma vs lava?", "Magma underground, lava surface", ["Same thing", "Lava underground", "Magma hotter"], "Location difference."),
        ("Ring of Fire location?", "Pacific Ocean rim", ["Atlantic", "Indian Ocean", "Arctic"], "Volcanic belt."),
        ("Most active volcano?", "Kilauea", ["Vesuvius", "Etna", "Fuji"], "Hawaii volcano."),
        ("Pompeii destroyed by?", "Mount Vesuvius", ["Etna", "Krakatoa", "St Helens"], "AD 79 eruption."),
        ("Krakatoa eruption year?", "1883", ["1783", "1983", "1683"], "Massive Indonesian eruption."),
        ("What is tsunami?", "Ocean wave from underwater disturbance", ["Tidal wave", "Storm surge", "Rip current"], "Often earthquake-caused."),
        ("Largest recorded earthquake?", "9.5 magnitude", ["8.0", "10.0", "12.0"], "1960 Chile earthquake."),
        ("Richter vs moment magnitude?", "Moment magnitude more accurate for large quakes", ["Same thing", "Richter better", "Richter for small quakes only"], "Modern measurement."),
        ("What is epicenter?", "Surface point above earthquake focus", ["Underground earthquake origin", "Deepest point", "Volcano crater"], "Directly above focus."),
        ("What is focus/hypocenter?", "Underground earthquake origin", ["Surface point", "Volcano", "Fault line"], "Where rupture starts."),
    ]
    
    for q, ans, dists, expl in earth_science:
        opts = [ans] + dists
        random.shuffle(opts)
        hard_additional.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 3
        })
    
    return {
        "batch_name": "Additional Questions (Batch 4)",
        "l1": easy_additional,
        "l2": medium_additional,
        "l3": hard_additional
    }

if __name__ == "__main__":
    batch4 = create_batch4_additional()
    print(f"Batch 4 (Additional):")
    print(f"  Level 1: {len(batch4['l1'])} questions")
    print(f"  Level 2: {len(batch4['l2'])} questions")
    print(f"  Level 3: {len(batch4['l3'])} questions")
    print(f"  Total: {sum(len(batch4[k]) for k in ['l1', 'l2', 'l3'])} questions")
    
    with open('treasure_batch4.json', 'w') as f:
        json.dump(batch4, f, indent=2)
    print("Saved to treasure_batch4.json")
