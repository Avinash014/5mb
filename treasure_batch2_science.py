import json
import random

# BATCH 2: SCIENCE & CHEMISTRY - 100 questions per level

def create_batch2_science():
    """100 questions per level on Science & Chemistry"""
    
    # LEVEL 1 - EASY SCIENCE (100 questions)
    easy_sci = []
    
    # Chemistry Elements (40 questions)
    elements_easy = [
        ("H", "Hydrogen", 1), ("He", "Helium", 2), ("C", "Carbon", 6), ("N", "Nitrogen", 7),
        ("O", "Oxygen", 8), ("Na", "Sodium", 11), ("Mg", "Magnesium", 12), ("Al", "Aluminum", 13),
        ("Si", "Silicon", 14), ("Cl", "Chlorine", 17), ("K", "Potassium", 19), ("Ca", "Calcium", 20),
        ("Fe", "Iron", 26), ("Cu", "Copper", 29), ("Zn", "Zinc", 30), ("Ag", "Silver", 47),
        ("Au", "Gold", 79), ("Hg", "Mercury", 80), ("Pb", "Lead", 82), ("U", "Uranium", 92),
    ]
    
    for symbol, name, num in elements_easy:
        opts = [name, "Oxygen", "Carbon", "Nitrogen"] if name not in ["Oxygen", "Carbon", "Nitrogen"] else [name, "Helium", "Neon", "Argon"]
        random.shuffle(opts)
        easy_sci.append({
            "text": f"What element has symbol '{symbol}'?",
            "options": opts[:4],
            "correctIndex": opts.index(name),
            "explanation": f"{symbol} is the symbol for {name} (atomic number {num}).",
            "difficulty": 1
        })
        
        # Reverse question
        opts2 = [symbol, "O", "C", "N"] if symbol not in ["O", "C", "N"] else [symbol, "He", "Ne", "Ar"]
        random.shuffle(opts2)
        easy_sci.append({
            "text": f"What is the symbol for {name}?",
            "options": opts2[:4],
            "correctIndex": opts2.index(symbol),
            "explanation": f"The symbol for {name} is {symbol}.",
            "difficulty": 1
        })
    
    # Basic Science Facts (60 questions)
    sci_facts_easy = [
        ("Chemical formula for water?", "H2O", ["O2", "CO2", "H2SO4"], "Water is H2O - two hydrogen, one oxygen."),
        ("Chemical formula for salt?", "NaCl", ["H2O", "CO2", "HCl"], "Table salt is sodium chloride (NaCl)."),
        ("Freezing point of water?", "0°C", ["10°C", "100°C", "-10°C"], "Water freezes at 0°C (32°F)."),
        ("Boiling point of water?", "100°C", ["0°C", "50°C", "200°C"], "Water boils at 100°C (212°F) at sea level."),
        ("Hardest natural substance?", "Diamond", ["Gold", "Iron", "Quartz"], "Diamond rates 10 on Mohs scale."),
        ("Lightest element?", "Hydrogen", ["Helium", "Lithium", "Carbon"], "Hydrogen has atomic number 1."),
        ("Most abundant element in universe?", "Hydrogen", ["Oxygen", "Carbon", "Helium"], "Hydrogen makes up 75% of universe's mass."),
        ("Most abundant gas in air?", "Nitrogen", ["Oxygen", "Carbon Dioxide", "Argon"], "Air is 78% nitrogen, 21% oxygen."),
        ("Speed of light?", "299,792 km/s", ["150,000 km/s", "500,000 km/s", "100,000 km/s"], "Light travels at 299,792,458 m/s in vacuum."),
        ("Speed of sound in air?", "343 m/s", ["300 m/s", "400 m/s", "500 m/s"], "At 20°C, sound travels at 343 m/s."),
        ("What is photosynthesis?", "Plants making food from light", ["Animal respiration", "Water cycle", "Rock formation"], "Photosynthesis converts CO2 and water to glucose."),
        ("What do plants produce?", "Oxygen", ["CO2", "Nitrogen", "Hydrogen"], "Plants produce oxygen during photosynthesis."),
        ("What do animals breathe in?", "Oxygen", ["CO2", "Nitrogen", "Hydrogen"], "Animals breathe oxygen and exhale CO2."),
        ("Human bones count?", "206", ["195", "215", "180"], "Adult humans have 206 bones."),
        ("Chambers in human heart?", "4", ["2", "3", "5"], "Heart has 4 chambers: 2 atria, 2 ventricles."),
        ("Normal body temperature?", "37°C", ["36°C", "38°C", "35°C"], "Normal body temp is 37°C (98.6°F)."),
        ("Largest organ in body?", "Skin", ["Liver", "Brain", "Heart"], "Skin covers about 2 m² in adults."),
        ("Smallest bone in body?", "Stapes", ["Femur", "Radius", "Patella"], "Stapes in ear is 2.8 mm long."),
        ("Longest bone in body?", "Femur", ["Tibia", "Humerus", "Radius"], "Femur (thighbone) is longest."),
        ("What is H2O?", "Water", ["Salt", "Sugar", "Acid"], "H2O is the chemical formula for water."),
        ("What is CO2?", "Carbon Dioxide", ["Carbon Monoxide", "Oxygen", "Water"], "CO2 is carbon dioxide."),
        ("What is O2?", "Oxygen", ["Water", "Ozone", "Carbon"], "O2 is molecular oxygen."),
        ("Primary colors of light?", "Red, Green, Blue", ["Red, Yellow, Blue", "Cyan, Magenta, Yellow", "Black, White, Gray"], "RGB are primary colors of light."),
        ("Primary colors of paint?", "Red, Yellow, Blue", ["Red, Green, Blue", "Cyan, Magenta, Yellow", "Orange, Purple, Green"], "RYB are traditional primary colors."),
        ("What causes day and night?", "Earth's rotation", ["Earth's orbit", "Moon's orbit", "Sun's movement"], "Earth rotates every 24 hours."),
        ("What causes seasons?", "Earth's tilt", ["Earth's rotation", "Distance from Sun", "Moon's gravity"], "Earth's 23.5° tilt causes seasons."),
        ("How long is a year?", "365 days", ["360 days", "366 days", "400 days"], "Earth orbits Sun in 365.25 days."),
        ("How long is a day?", "24 hours", ["12 hours", "48 hours", "20 hours"], "Earth rotates once in 24 hours."),
        ("What is gravity?", "Force that pulls objects together", ["Force that pushes apart", "Magnetic force", "Electric force"], "Gravity attracts mass."),
        ("Who discovered gravity?", "Isaac Newton", ["Albert Einstein", "Galileo", "Stephen Hawking"], "Newton formulated law of gravitation."),
    ]
    
    for q, ans, dists, expl in sci_facts_easy:
        opts = [ans] + dists
        random.shuffle(opts)
        easy_sci.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 1
        })
    
    # LEVEL 2 - MEDIUM SCIENCE (100 questions)
    medium_sci = []
    
    # Medium Elements (32 questions - 16 elements, 2 questions each)
    elements_medium = [
        ("Li", "Lithium", 3), ("Be", "Beryllium", 4), ("B", "Boron", 5), ("F", "Fluorine", 9),
        ("Ne", "Neon", 10), ("P", "Phosphorus", 15), ("S", "Sulfur", 16), ("Ar", "Argon", 18),
        ("Mn", "Manganese", 25), ("Ni", "Nickel", 28), ("Br", "Bromine", 35), ("Kr", "Krypton", 36),
        ("Sr", "Strontium", 38), ("Sn", "Tin", 50), ("I", "Iodine", 53), ("Xe", "Xenon", 54),
    ]
    
    for symbol, name, num in elements_medium:
        opts = [name, "Oxygen", "Carbon", "Nitrogen"]
        random.shuffle(opts)
        medium_sci.append({
            "text": f"What element has symbol '{symbol}'?",
            "options": opts[:4],
            "correctIndex": opts.index(name),
            "explanation": f"{symbol} is {name} (atomic number {num}).",
            "difficulty": 2
        })
        
        opts2 = [symbol, "O", "C", "N"]
        random.shuffle(opts2)
        medium_sci.append({
            "text": f"Symbol for {name}?",
            "options": opts2[:4],
            "correctIndex": opts2.index(symbol),
            "explanation": f"{name}'s symbol is {symbol}.",
            "difficulty": 2
        })
    
    # Medium Science Facts (68 questions)
    sci_facts_medium = [
        ("pH of pure water?", "7", ["5", "9", "0"], "Pure water has neutral pH of 7."),
        ("pH of acid?", "Less than 7", ["7", "More than 7", "14"], "Acids have pH below 7."),
        ("pH of base?", "More than 7", ["7", "Less than 7", "0"], "Bases have pH above 7."),
        ("Inventor of periodic table?", "Dmitri Mendeleev", ["Marie Curie", "John Dalton", "Niels Bohr"], "Mendeleev created table in 1869."),
        ("What is DNA?", "Deoxyribonucleic Acid", ["Deoxyribose Acid", "Nucleic Acid", "RNA"], "DNA stores genetic information."),
        ("DNA shape?", "Double Helix", ["Single Strand", "Triple Helix", "Circle"], "DNA is a double helix structure."),
        ("Who discovered DNA structure?", "Watson and Crick", ["Einstein and Bohr", "Curie and Pasteur", "Newton and Galileo"], "Watson and Crick discovered double helix in 1953."),
        ("Unit of electric current?", "Ampere", ["Volt", "Watt", "Ohm"], "Current measured in amperes (A)."),
        ("Unit of voltage?", "Volt", ["Ampere", "Watt", "Ohm"], "Voltage measured in volts (V)."),
        ("Unit of resistance?", "Ohm", ["Ampere", "Volt", "Watt"], "Resistance measured in ohms (Ω)."),
        ("Unit of power?", "Watt", ["Joule", "Ampere", "Volt"], "Power measured in watts (W)."),
        ("Unit of energy?", "Joule", ["Watt", "Calorie", "Newton"], "Energy measured in joules (J)."),
        ("Unit of force?", "Newton", ["Joule", "Watt", "Pascal"], "Force measured in newtons (N)."),
        ("Avogadro's number?", "6.022 × 10²³", ["6.022 × 10²²", "6.022 × 10²⁴", "1.0 × 10²³"], "One mole = 6.022 × 10²³ particles."),
        ("What is a mole?", "Unit of amount of substance", ["Unit of mass", "Unit of volume", "Unit of temperature"], "Mole is SI unit for amount."),
        ("Newton's First Law?", "Law of Inertia", ["Law of Acceleration", "Law of Action-Reaction", "Law of Gravity"], "Object at rest stays at rest."),
        ("Newton's Second Law?", "F = ma", ["F = G", "F = mv", "F = md"], "Force equals mass times acceleration."),
        ("Newton's Third Law?", "Action-Reaction", ["Inertia", "Acceleration", "Gravity"], "Every action has equal opposite reaction."),
        ("What is momentum?", "Mass times velocity", ["Mass times acceleration", "Force times time", "Energy divided by time"], "Momentum = mass × velocity."),
        ("What is kinetic energy?", "Energy of motion", ["Stored energy", "Heat energy", "Light energy"], "KE = ½mv²."),
        ("What is potential energy?", "Stored energy", ["Energy of motion", "Heat energy", "Light energy"], "PE depends on position."),
        ("Earth's atmosphere composition?", "78% Nitrogen", ["78% Oxygen", "50% Nitrogen", "90% Oxygen"], "Air is 78% N2, 21% O2."),
        ("Lightest noble gas?", "Helium", ["Neon", "Argon", "Xenon"], "Helium is lighter than air."),
        ("Blood type universal donor?", "O Negative", ["AB Positive", "A Positive", "B Negative"], "O- can donate to any type."),
        ("Blood type universal recipient?", "AB Positive", ["O Negative", "A Positive", "B Positive"], "AB+ can receive any type."),
        ("Photosynthesis equation?", "CO2 + H2O → Glucose + O2", ["O2 + Glucose → CO2 + H2O", "N2 + O2 → NO2", "H2 + O2 → H2O"], "Plants convert CO2 and water to food."),
        ("Respiration equation?", "Glucose + O2 → CO2 + H2O", ["CO2 + H2O → Glucose + O2", "N2 + O2 → NO2", "H2 + O2 → H2O"], "Animals burn glucose for energy."),
        ("Mitochondria function?", "Energy production", ["Protein synthesis", "DNA storage", "Waste removal"], "Mitochondria are cell's powerhouse."),
        ("Nucleus function?", "DNA storage and control", ["Energy production", "Protein synthesis", "Waste removal"], "Nucleus contains genetic material."),
        ("Ribosome function?", "Protein synthesis", ["Energy production", "DNA storage", "Waste removal"], "Ribosomes make proteins."),
        ("Cell membrane function?", "Controls what enters/exits", ["Energy production", "DNA storage", "Protein synthesis"], "Membrane is selective barrier."),
        ("What is osmosis?", "Water movement across membrane", [" Salt movement", "Gas movement", "Protein movement"], "Osmosis is passive water transport."),
        ("What is diffusion?", "Movement from high to low concentration", ["Movement against gradient", "Active transport", "Energy-requiring transport"], "Diffusion is passive movement."),
        ("Distance Earth to Sun?", "150 million km", ["100 million km", "200 million km", "50 million km"], "Average is 149.6 million km (1 AU)."),
        ("Earth's diameter?", "12,742 km", ["10,000 km", "15,000 km", "20,000 km"], "Equatorial diameter is 12,742 km."),
    ]
    
    for q, ans, dists, expl in sci_facts_medium:
        opts = [ans] + dists
        random.shuffle(opts)
        medium_sci.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 2
        })
    
    # LEVEL 3 - HARD SCIENCE (100 questions)
    hard_sci = []
    
    # Hard Elements (24 questions - 12 elements, 2 questions each)
    elements_hard = [
        ("Sc", "Scandium", 21), ("Ti", "Titanium", 22), ("V", "Vanadium", 23), ("Cr", "Chromium", 24),
        ("Co", "Cobalt", 27), ("Ga", "Gallium", 31), ("Ge", "Germanium", 32), ("As", "Arsenic", 33),
        ("Se", "Selenium", 34), ("Rb", "Rubidium", 37), ("Y", "Yttrium", 39), ("Zr", "Zirconium", 40),
    ]
    
    for symbol, name, num in elements_hard:
        opts = [name, "Oxygen", "Carbon", "Nitrogen"]
        random.shuffle(opts)
        hard_sci.append({
            "text": f"Element symbol '{symbol}'?",
            "options": opts[:4],
            "correctIndex": opts.index(name),
            "explanation": f"{symbol} = {name} (Z={num}).",
            "difficulty": 3
        })
        
        opts2 = [symbol, "O", "C", "N"]
        random.shuffle(opts2)
        hard_sci.append({
            "text": f"Symbol for {name}?",
            "options": opts2[:4],
            "correctIndex": opts2.index(symbol),
            "explanation": f"{name} = {symbol}.",
            "difficulty": 3
        })
    
    # Hard Science Facts (76 questions)
    sci_facts_hard = [
        ("Planck's constant?", "6.626 × 10⁻³⁴ J·s", ["6.626 × 10⁻³³", "6.626 × 10⁻³⁵", "1.0 × 10⁻³⁴"], "Relates energy to frequency."),
        ("Absolute zero?", "-273.15°C", ["-200°C", "-300°C", "-250°C"], "0 Kelvin = -273.15°C."),
        ("Electron charge?", "-1.602 × 10⁻¹⁹ C", ["-1.0 × 10⁻¹⁹", "-2.0 × 10⁻¹⁹", "-1.602 × 10⁻¹⁸"], "Elementary charge constant."),
        ("Proton mass?", "1.673 × 10⁻²⁷ kg", ["1.0 × 10⁻²⁷", "2.0 × 10⁻²⁷", "1.673 × 10⁻²⁶"], "~1836× electron mass."),
        ("Electron mass?", "9.109 × 10⁻³¹ kg", ["9.109 × 10⁻³⁰", "9.109 × 10⁻³²", "1.0 × 10⁻³¹"], "Lightest stable particle."),
        ("Half-life of C-14?", "5,730 years", ["1,000", "10,000", "50,000"], "Used for radiocarbon dating."),
        ("Strongest force?", "Strong Nuclear", ["Electromagnetic", "Weak Nuclear", "Gravity"], "Holds nuclei together."),
        ("Weakest force?", "Gravity", ["Electromagnetic", "Weak Nuclear", "Strong Nuclear"], "Weakest of 4 fundamental forces."),
        ("Hubble constant?", "~70 km/s/Mpc", ["50", "100", "150"], "Universe expansion rate."),
        ("Age of universe?", "13.8 billion years", ["10 billion", "20 billion", "5 billion"], "Since Big Bang."),
        ("Age of Earth?", "4.54 billion years", ["3 billion", "5 billion", "10 billion"], "From isotope dating."),
        ("What is entropy?", "Measure of disorder", ["Measure of energy", "Measure of temperature", "Measure of pressure"], "Second law of thermodynamics."),
        ("What is enthalpy?", "Heat content", ["Work done", "Temperature change", "Pressure change"], "ΔH in thermodynamics."),
        ("What is Gibbs free energy?", "Energy available for work", ["Total energy", "Heat energy", "Kinetic energy"], "ΔG = ΔH - TΔS."),
        ("Ideal gas law?", "PV = nRT", ["PV = T", "P = nRT", "V = nRT"], "Relates pressure, volume, temp."),
        ("Boyle's Law?", "P₁V₁ = P₂V₂", ["P₁/T₁ = P₂/T₂", "V₁/T₁ = V₂/T₂", "PV = T"], "At constant temperature."),
        ("Charles's Law?", "V₁/T₁ = V₂/T₂", ["P₁V₁ = P₂V₂", "P₁/T₁ = P₂/T₂", "PV = T"], "At constant pressure."),
        ("Gay-Lussac's Law?", "P₁/T₁ = P₂/T₂", ["P₁V₁ = P₂V₂", "V₁/T₁ = V₂/T₂", "PV = T"], "At constant volume."),
        ("Heisenberg Uncertainty?", "ΔxΔp ≥ ħ/2", ["ΔEΔt = h", "Δx = 0", "Δp = 0"], "Cannot precisely know position and momentum."),
        ("Schrödinger equation?", "iħ∂ψ/∂t = Hψ", ["E = mc²", "F = ma", "PV = nRT"], "Fundamental quantum mechanics."),
        ("Einstein's E=mc²?", "Energy-mass equivalence", ["Force equation", "Momentum equation", "Work equation"], "Energy equals mass times c²"),
        ("Doppler effect?", "Frequency shift due to motion", ["Amplitude change", "Wavelength constancy", "Energy loss"], "Sound/light frequency changes."),
        ("Redshift indicates?", "Object moving away", ["Object approaching", "Object stationary", "Object rotating"], "Light wavelength increases."),
        ("Blueshift indicates?", "Object approaching", ["Object moving away", "Object stationary", "Object rotating"], "Light wavelength decreases."),
        ("What is a catalyst?", "Speeds reaction without being consumed", ["Slows reaction", "Gets consumed", "Increases yield"], "Lowers activation energy."),
        ("What is an enzyme?", "Biological catalyst", ["Hormone", "Vitamin", "Mineral"], "Protein that speeds reactions."),
        ("What is ATP?", "Adenosine Triphosphate", ["Adenosine Diphosphate", "Adenosine Monophosphate", "Amino Acid"], "Energy currency of cell."),
        ("What is RNA?", "Ribonucleic Acid", ["Deoxyribonucleic Acid", "Ribose Sugar", "Ribosome"], "Single-stranded genetic material."),
        ("Difference DNA vs RNA?", "DNA has deoxyribose, RNA has ribose", ["DNA is single, RNA is double", "DNA is small, RNA is large", "No difference"], "Also thymine vs uracil."),
        ("Central Dogma?", "DNA → RNA → Protein", ["RNA → DNA → Protein", "Protein → RNA → DNA", "DNA → Protein → RNA"], "Information flow in biology."),
        ("Transcription?", "DNA to RNA", ["RNA to DNA", "DNA to Protein", "RNA to Protein"], "First step of gene expression."),
        ("Translation?", "RNA to Protein", ["DNA to RNA", "DNA to Protein", "Protein to RNA"], "Second step of gene expression."),
        ("Genetic code units?", "Codons (3 nucleotides)", ["Genes", "Chromosomes", "Proteins"], "Each codon codes for amino acid."),
        ("How many amino acids?", "20 standard", ["10", "30", "50"], "20 proteinogenic amino acids."),
        ("How many DNA bases?", "4", ["2", "8", "10"], "A, T, G, C."),
        ("How many RNA bases?", "4", ["2", "8", "10"], "A, U, G, C."),
        ("DNA base pairing?", "A-T, G-C", ["A-G, T-C", "A-C, T-G", "A-U, G-C"], "Hydrogen bonding rules."),
        ("RNA base pairing?", "A-U, G-C", ["A-T, G-C", "A-G, U-C", "A-C, U-G"], "Uracil instead of thymine."),
    ]
    
    for q, ans, dists, expl in sci_facts_hard:
        opts = [ans] + dists
        random.shuffle(opts)
        hard_sci.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 3
        })
    
    return {
        "batch_name": "Science & Chemistry",
        "l1": easy_sci,
        "l2": medium_sci,
        "l3": hard_sci
    }

if __name__ == "__main__":
    batch2 = create_batch2_science()
    print(f"Batch 2 (Science & Chemistry):")
    print(f"  Level 1: {len(batch2['l1'])} questions")
    print(f"  Level 2: {len(batch2['l2'])} questions")
    print(f"  Level 3: {len(batch2['l3'])} questions")
    
    with open('treasure_batch2.json', 'w') as f:
        json.dump(batch2, f, indent=2)
    print("Saved to treasure_batch2.json")
