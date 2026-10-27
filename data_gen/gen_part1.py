import json

questions = [
    {
        "id": "toefl-r-153",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "The monarch butterfly undertakes one of the longest insect migrations on Earth, traveling up to 4,800 kilometers from Canada and the United States to central Mexico each autumn. Unlike most migratory animals, no single butterfly completes the round trip; it takes three to four generations to finish the full cycle, with each generation passing the migration route to the next. Researchers discovered in 2021 that monarchs use a time-compensated sun compass located in their antennae to navigate, allowing them to maintain a steady heading even as the sun moves across the sky. During winter the butterflies cluster on oyamel fir trees in dense groups to conserve heat and reduce exposure to cold mountain temperatures. Deforestation in Mexico, which removes the forests where they overwinter, and the widespread use of herbicides that reduce milkweed—their sole food source—pose serious threats to the migration.",
        "question": "What is the primary threat to the monarch butterfly migration?",
        "options": [
            "Deforestation and herbicide use that reduce their habitat and food source",
            "Overcrowding on oyamel fir trees during winter",
            "The inability of a single butterfly to complete the migration",
            "The use of a time-compensated sun compass for navigation"
        ],
        "answer": 0,
        "explanation": "文章末尾明确指出 deforestation in Mexico 和 herbicides that reduce milkweed pose serious threats to the migration，故选A。"
    },
    {
        "id": "toefl-r-154",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "The discovery of exoplanets orbiting distant stars has revolutionized our understanding of planetary systems. NASA's Kepler mission has identified thousands of potential exoplanets, many in the habitable zone where liquid water could exist. These planets vary in size and composition, with some being rocky like Earth while others are gas giants. The transit method, which measures the dimming of a star as a planet passes in front of it, has been instrumental in these discoveries. Recent advances in spectroscopy allow scientists to analyze the chemical composition of exoplanet atmospheres, searching for biosignatures that might indicate life. However, challenges remain in detecting Earth-like planets due to their small size relative to their host stars and the brightness of the stars themselves.",
        "question": "According to the passage, how does the transit method help detect exoplanets?",
        "options": [
            "By measuring the dimming of a star when a planet passes in front of it",
            "By analyzing the chemical composition of stellar atmospheres",
            "By calculating the gravitational pull of planets on distant stars",
            "By directly photographing planets in the habitable zone"
        ],
        "answer": 0,
        "explanation": "文章第三句指出 transit method measures the dimming of a star as a planet passes in front of it，故选A。"
    },
    {
        "id": "toefl-r-155",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Quantum computing represents a paradigm shift in computational capabilities, leveraging quantum mechanics to solve problems beyond the reach of classical computers. Unlike traditional bits that represent either 0 or 1, quantum bits or qubits can exist in superposition, representing multiple states simultaneously. This property, combined with entanglement, enables exponential speedup for certain algorithms. Quantum computers are particularly promising for factoring large numbers, simulating complex molecules, and optimizing complex systems. However, current quantum computers face challenges such as quantum decoherence and error rates, which limit their practical applications. Researchers are developing error-correcting codes and more stable qubit architectures to overcome these limitations.",
        "question": "What is the main advantage of qubits over traditional bits?",
        "options": [
            "They can exist in superposition, representing multiple states simultaneously",
            "They are completely immune to quantum decoherence and error rates",
            "They eliminate the need for error-correcting codes entirely",
            "They operate at much lower temperatures than classical bits"
        ],
        "answer": 0,
        "explanation": "文章指出 qubits can exist in superposition, representing multiple states simultaneously，故选A。"
    },
    {
        "id": "toefl-r-156",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Memory formation in the human brain involves complex neural processes that transform short-term experiences into long-term stores. The hippocampus plays a crucial role in the initial consolidation of episodic memories, while the neocortex is responsible for long-term storage and retrieval. Sleep, particularly deep non-REM sleep, is essential for memory consolidation as the brain replays neural patterns from the day's experiences. Research suggests that emotional intensity enhances memory retention through the release of stress hormones like cortisol. Additionally, the process of reconsolidation allows memories to be updated or modified when recalled, contributing to the dynamic nature of human memory.",
        "question": "Which brain structure is primarily responsible for the initial consolidation of episodic memories?",
        "options": [
            "The hippocampus",
            "The neocortex",
            "The amygdala",
            "The cerebellum"
        ],
        "answer": 0,
        "explanation": "文章第二句指出 The hippocampus plays a crucial role in the initial consolidation of episodic memories，故选A。"
    },
    {
        "id": "toefl-r-157",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Behavioral economics examines how psychological, social, cognitive, and emotional factors influence economic decisions. Traditional economic models assume rational actors making optimal choices, but behavioral research reveals systematic biases such as loss aversion, where people fear losses more than they value equivalent gains. The endowment effect demonstrates that individuals place higher value on objects merely because they own them. Nudge theory, popularized by Thaler and Suntein, suggests that small changes in choice architecture can significantly influence behavior without restricting freedom of choice. These insights have important implications for policy-making in areas ranging from health choices to financial planning.",
        "question": "What does loss aversion refer to in behavioral economics?",
        "options": [
            "People fearing losses more than they value equivalent gains",
            "Individuals placing higher value on objects they own",
            "The assumption that economic actors always make optimal choices",
            "Small changes in choice architecture influencing behavior"
        ],
        "answer": 0,
        "explanation": "文章解释 loss aversion 为 where people fear losses more than they value equivalent gains，故选A。"
    },
    {
        "id": "toefl-r-158",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Plastic pollution has become a pervasive global environmental issue affecting ecosystems and wildlife. Each year, approximately 8 million tons of plastic enter the oceans, where it breaks down into microplastics that are ingested by marine organisms. These microplastics can accumulate up the food chain, potentially impacting human health. Marine animals such as sea turtles mistake plastic bags for jellyfish, their natural prey, leading to fatal internal blockages. Despite recycling efforts, plastic production continues to increase, driven by consumer demand for convenience. Solutions include reducing single-use plastics, improving waste management infrastructure, and developing biodegradable alternatives. International agreements like the Basel Convention aim to regulate the transboundary movement of hazardous waste, including plastic.",
        "question": "Why do sea turtles frequently ingest plastic bags according to the passage?",
        "options": [
            "They mistake plastic bags for jellyfish, their natural prey",
            "Plastics accumulate directly in their primary nesting sites",
            "They are attracted to the bright colors of floating debris",
            "Microplastics alter their sensory perception of food"
        ],
        "answer": 0,
        "explanation": "文章指出 sea turtles mistake plastic bags for jellyfish, their natural prey，故选A。"
    },
    {
        "id": "toefl-r-159",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "The Silk Road, an extensive network of trade routes connecting Asia, Europe, and Africa, flourished between the 2nd century BCE and the 15th century CE. This ancient highway facilitated not only the exchange of goods like silk, spices, and precious metals but also the transmission of ideas, religions, and technologies across civilizations. Cities along the route, such as Samarkand and Kashgar, became melting pots of cultural diversity. The decline of the Silk Road was accelerated by the rise of maritime trade routes after the 15th century, which offered faster and safer transportation. Nevertheless, the legacy of these routes persists in the linguistic, artistic, and culinary influences that continue to shape modern societies across Eurasia.",
        "question": "What primarily accelerated the decline of the Silk Road?",
        "options": [
            "The rise of maritime trade routes after the 15th century",
            "The destruction of major trading cities like Samarkand",
            "Severe climate changes along the overland pathways",
            "Political isolation policies enacted by Asian empires"
        ],
        "answer": 0,
        "explanation": "文章指出 decline was accelerated by the rise of maritime trade routes after the 15th century，故选A。"
    },
    {
        "id": "toefl-r-160",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Postmodern novels often challenge traditional narrative structures and question the nature of reality and truth. Authors like Thomas Pynchon and Don DeLillo employ fragmented storytelling, metafictional elements, and intertextual references to create complex, layered narratives. These works frequently blur the lines between fiction and reality, reflecting the uncertainty of the postmodern condition. The use of irony, pastiche, and non-linear chronology are common techniques that critique contemporary society and media culture. Postmodern literature also engages with historical narratives, reinterpreting the past through a contemporary lens to question established truths and perspectives.",
        "question": "Which of the following is a characteristic technique of postmodern novels?",
        "options": [
            "Fragmented storytelling and non-linear chronology",
            "Strict adherence to traditional linear narrative structures",
            "Complete separation of fiction from real-world politics",
            "Exclusive focus on romanticism and idealism"
        ],
        "answer": 0,
        "explanation": "文章提到 authors employ fragmented storytelling... and non-linear chronology，故选A。"
    },
    {
        "id": "toefl-r-161",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "The Renaissance period marked a revival of classical learning and artistic innovation in Europe, particularly in painting. Artists such as Leonardo da Vinci, Michelangelo, and Raphael pioneered techniques like linear perspective, chiaroscuro, and sfumato to create more realistic and emotionally resonant works. The patronage system, supported by wealthy families like the Medici, provided crucial funding for artistic production. Religious themes dominated early Renaissance paintings, but secular subjects became increasingly popular as humanism emphasized the value of individual experience. The period's emphasis on observation and anatomical accuracy laid the foundation for the scientific revolution that followed.",
        "question": "What role did the patronage system play during the Renaissance?",
        "options": [
            "It provided crucial funding for artistic production",
            "It restricted artists to painting strictly religious themes",
            "It prohibited the use of linear perspective and chiaroscuro",
            "It replaced humanism with classical scientific theories"
        ],
        "answer": 0,
        "explanation": "文章指出 patronage system... provided crucial funding for artistic production，故选A。"
    },
    {
        "id": "toefl-r-162",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "The evolution of human language reflects both biological and cultural factors over thousands of years. Linguists identify two primary mechanisms driving language change: internal development and external influence. Internal factors include phonetic shifts, grammatical simplification, and semantic broadening, while external influences involve contact with other languages through trade, conquest, or migration. For example, English has incorporated numerous words from Latin, French, and Norse through historical events. The process of language change is continuous and dynamic, with new words emerging and existing terms evolving in meaning to adapt to new concepts and technologies.",
        "question": "According to the passage, what is an example of an external influence on language?",
        "options": [
            "Contact with other languages through trade, conquest, or migration",
            "Spontaneous phonetic shifts occurring within a single isolated community",
            "Grammatical simplification driven by younger speakers",
            "Semantic broadening of ancient root words"
        ],
        "answer": 0,
        "explanation": "文章指出 external influences involve contact with other languages through trade, conquest, or migration，故选A。"
    },
    {
        "id": "toefl-r-163",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Plate tectonics is the scientific theory that explains the large-scale motion of Earth's lithospheric plates. The lithosphere, composed of the crust and upper mantle, is divided into several major plates that float on the semi-fluid asthenosphere beneath. Movement occurs at plate boundaries, which are classified as divergent (where plates move apart), convergent (where plates collide), and transform (where plates slide past each other). Divergent boundaries create new oceanic crust through seafloor spreading, while convergent boundaries can form mountain ranges or subduction zones. Transform boundaries result in earthquakes but not significant crustal deformation. This theory revolutionized geology by providing a unifying framework for understanding earthquakes, volcanic activity, and mineral resources.",
        "question": "What happens at divergent plate boundaries?",
        "options": [
            "New oceanic crust is created through seafloor spreading",
            "Plates collide to form massive mountain ranges",
            "Plates slide past each other without crustal deformation",
            "Subduction zones pull the crust deep into the mantle"
        ],
        "answer": 0,
        "explanation": "文章指出 divergent boundaries create new oceanic crust through seafloor spreading，故选A。"
    },
    {
        "id": "toefl-r-164",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Cultural practices vary widely across societies but often serve to maintain social cohesion and transmit values across generations. Rituals surrounding birth, marriage, and death provide frameworks for navigating life transitions. Festivals celebrate seasonal changes, religious holidays, or community achievements, reinforcing shared identity. Oral traditions, including storytelling, songs, and proverbs, preserve cultural knowledge and history. The globalization of media has introduced new influences, creating hybrid cultural forms that blend traditional practices with modern elements, sometimes challenging established norms and values.",
        "question": "What is one primary function of cultural practices such as rituals and festivals?",
        "options": [
            "To maintain social cohesion and transmit values across generations",
            "To completely eliminate the influence of global media",
            "To prevent any future changes to traditional norms",
            "To replace oral traditions with written legal codes"
        ],
        "answer": 0,
        "explanation": "文章首句指出 cultural practices often serve to maintain social cohesion and transmit values across generations，故选A。"
    },
    {
        "id": "toefl-r-165",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Archaeological discoveries of ancient cities continue to reshape our understanding of early human civilizations. Recent excavations in the Indus Valley have uncovered sophisticated urban planning with grid layouts, advanced drainage systems, and standardized brick sizes. These features suggest a high degree of social organization and technological development. The decipherment of the Indus script remains a challenge, as no bilingual text has been found to provide a key for translation. Similarly, excavations in Mesopotamia have revealed cuneiform tablets detailing legal codes, trade records, and literary texts that illuminate the complexity of ancient bureaucratic systems. Such discoveries highlight the importance of interdisciplinary research combining archaeology, linguistics, and history to reconstruct the past.",
        "question": "Why has the decipherment of the Indus script remained difficult?",
        "options": [
            "No bilingual text has been found to provide a translation key",
            "The bricks and drainage systems lacked any written markings",
            "Mesopotamian cuneiform tablets contradicted Indus records",
            "Archaeologists have not yet excavated any urban centers"
        ],
        "answer": 0,
        "explanation": "文章指出 decipherment remains a challenge, as no bilingual text has been found to provide a key，故选A。"
    },
    {
        "id": "toefl-r-166",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Graph theory, a branch of mathematics concerned with networks of objects, has found applications in diverse fields. In computer science, it models computer networks, social media connections, and transportation systems. The traveling salesman problem, which seeks the shortest route visiting all cities, is a classic optimization challenge. In epidemiology, graph theory helps track disease transmission through contact networks. Social network analysis uses graph metrics to identify influential individuals and understand community structures. Recent advances in big data analytics have enabled the visualization and analysis of massive graphs containing billions of nodes and edges, revealing patterns previously hidden from view.",
        "question": "How is graph theory utilized in epidemiology?",
        "options": [
            "To help track disease transmission through contact networks",
            "To solve the traveling salesman problem for transportation",
            "To analyze massive financial transactions in big data",
            "To design computer networks and social media platforms"
        ],
        "answer": 0,
        "explanation": "文章指出 in epidemiology, graph theory helps track disease transmission through contact networks，故选A。"
    },
    {
        "id": "toefl-r-167",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "As machine learning systems become increasingly integrated into society, ethical considerations have gained prominence. Issues such as algorithmic bias, privacy invasion, and lack of transparency pose significant challenges. Training data often reflects historical biases, leading to discriminatory outcomes in hiring, lending, and law enforcement. The black box nature of deep learning models makes it difficult to explain decision-making processes to affected individuals. Researchers advocate for fairness-aware algorithms, explainable AI techniques, and robust data governance practices. Regulatory frameworks like the EU's AI Act aim to ensure accountability and protect fundamental rights. Ethical AI development requires interdisciplinary collaboration between computer scientists, ethicists, and social scientists to create systems that are both effective and socially responsible.",
        "question": "What causes discriminatory outcomes in machine learning systems according to the passage?",
        "options": [
            "Training data often reflecting historical biases",
            "The complete absence of regulatory frameworks like the AI Act",
            "Too much transparency in deep learning model decisions",
            "An oversupply of interdisciplinary ethicists and scientists"
        ],
        "answer": 0,
        "explanation": "文章指出 training data often reflects historical biases, leading to discriminatory outcomes，故选A。"
    },
    {
        "id": "toefl-r-168",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Telemedicine has experienced rapid growth, particularly accelerated by the COVID-19 pandemic, enabling remote healthcare delivery through video consultations, mobile apps, and remote monitoring devices. This approach expands access to specialized care in rural and underserved areas while reducing travel time and costs for patients. Electronic health records integrated with telehealth platforms allow for seamless information sharing between providers. However, limitations include the inability to perform physical examinations, potential technical issues, and concerns about data privacy and security. The future of telemedicine likely involves hybrid models combining virtual and in-person care to optimize patient outcomes and resource utilization.",
        "question": "What is considered a major limitation of telemedicine?",
        "options": [
            "The inability to perform physical examinations",
            "Increased travel time and costs for patients",
            "Complete incompatibility with electronic health records",
            "A lack of interest from rural and underserved areas"
        ],
        "answer": 0,
        "explanation": "文章指出 limitations include the inability to perform physical examinations，故选A。"
    },
    {
        "id": "toefl-r-169",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Green chemistry focuses on designing chemical processes and products that reduce or eliminate the use and generation of hazardous substances. The 12 principles of green chemistry provide a framework for sustainable chemical synthesis, emphasizing waste prevention, atom economy, and safer solvents. Catalysis plays a crucial role in enabling reactions that proceed under milder conditions with higher selectivity, minimizing energy consumption and byproduct formation. Biodegradable materials derived from renewable resources offer alternatives to traditional petroleum-based plastics. Industrial adoption of green chemistry principles requires innovation in process design, supply chain management, and regulatory compliance to achieve economic viability alongside environmental benefits.",
        "question": "What role does catalysis play in green chemistry?",
        "options": [
            "Enabling reactions to proceed under milder conditions with higher selectivity",
            "Replacing renewable resources with petroleum-based plastics",
            "Maximizing the generation of hazardous chemical byproducts",
            "Increasing energy consumption during chemical synthesis"
        ],
        "answer": 0,
        "explanation": "文章指出 catalysis plays a crucial role in enabling reactions that proceed under milder conditions... minimizing energy consumption，故选A。"
    },
    {
        "id": "toefl-r-170",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Urbanization represents a significant global trend where populations shift from rural to urban areas, driven by economic opportunities, educational access, and improved infrastructure. Currently, over half of the world's population resides in urban areas, a proportion expected to rise to 68% by 2050 according to United Nations projections. This rapid growth presents challenges such as housing shortages, strain on public services, and increased pollution. However, well-planned urban environments can enhance quality of life through efficient public transportation, green spaces, and mixed-use development. Addressing urbanization requires integrated policies that balance economic development with social equity and environmental sustainability.",
        "question": "What drives the shift of populations from rural to urban areas?",
        "options": [
            "Economic opportunities, educational access, and improved infrastructure",
            "Severe housing shortages and strain on public services",
            "Strict government policies limiting rural development",
            "An increase in pollution and traffic congestion"
        ],
        "answer": 0,
        "explanation": "文章首句指出 populations shift... driven by economic opportunities, educational access, and improved infrastructure，故选A。"
    },
    {
        "id": "toefl-r-171",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Existentialism is a philosophical movement that emphasizes individual freedom, choice, and the search for meaning in an apparently indifferent universe. Central to existentialist thought is the concept of existence precedes essence, which asserts that individuals create their own meaning rather than inheriting predefined purposes. Key figures such as Jean-Paul Sartre and Albert Camus explored themes of absurdity, authenticity, and responsibility. Existentialist literature often portrays characters confronting the void and making authentic choices despite life's inherent uncertainty. This philosophical perspective has influenced literature, psychology, and political theory, encouraging individuals to take responsibility for their actions and values.",
        "question": "What does the existentialist concept 'existence precedes essence' imply?",
        "options": [
            "Individuals create their own meaning rather than inheriting predefined purposes",
            "Human beings are born with a fixed and immutable purpose in life",
            "The universe provides clear moral guidance for every individual",
            "Essence must be studied before any human action can occur"
        ],
        "answer": 0,
        "explanation": "文章指出 existence precedes essence asserts that individuals create their own meaning rather than inheriting predefined purposes，故选A。"
    },
    {
        "id": "toefl-r-172",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Online learning has transformed education by providing flexible access to courses and resources beyond traditional classroom settings. Massive Open Online Courses (MOOCs) and learning management systems enable learners to progress at their own pace, access diverse instructional materials, and engage in virtual discussions. Educational technology has evolved to support interactive experiences through video lectures, virtual labs, and adaptive assessments that adjust difficulty based on learner performance. However, challenges such as digital divide, reduced face-to-face interaction, and concerns about credential recognition persist. The effectiveness of online learning depends on instructional design, learner motivation, and institutional support structures.",
        "question": "What is one persistent challenge of online learning mentioned in the text?",
        "options": [
            "The digital divide and reduced face-to-face interaction",
            "An excess of face-to-face classroom interactions",
            "The inability to use video lectures or virtual labs",
            "A complete lack of flexible course access"
        ],
        "answer": 0,
        "explanation": "文章指出 challenges such as digital divide, reduced face-to-face interaction... persist，故选A。"
    },
    {
        "id": "toefl-r-173",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Coral reefs, often called the rainforests of the sea, support immense biodiversity and provide critical ecosystem services including coastal protection and fisheries. However, they face severe threats from climate change, ocean acidification, and destructive fishing practices. Coral reef restoration initiatives employ techniques such as coral gardening, where broken coral fragments are grown in nurseries before being transplanted to damaged reefs. Other innovative approaches include micro-fragmentation and assisted gene flow to enhance thermal tolerance in warming waters. While these methods show promise for local recovery, scaling them globally remains a major challenge requiring urgent reductions in greenhouse gas emissions.",
        "question": "What is coral gardening in the context of reef restoration?",
        "options": [
            "Growing broken coral fragments in nurseries before transplanting them to damaged reefs",
            "Building artificial coastlines to protect reefs from destructive fishing",
            "Genetically modifying fish species to increase ocean biodiversity",
            "Eliminating greenhouse gas emissions through local marine policies"
        ],
        "answer": 0,
        "explanation": "文章指出 coral gardening is where broken coral fragments are grown in nurseries before being transplanted to damaged reefs，故选A。"
    },
    {
        "id": "toefl-r-174",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "CRISPR-Cas9 technology has revolutionized genetic engineering by offering a precise, efficient, and cost-effective method for editing DNA. Derived from the natural defense mechanisms of bacteria against phages, the system uses a guide RNA to target specific nucleotide sequences, allowing the Cas9 enzyme to cut the DNA strand at the desired location. Scientists can then disable genes, correct mutations, or insert new genetic material. This breakthrough has immense applications in agriculture, such as developing crop varieties resistant to pests and extreme weather, and in medicine, offering potential cures for genetic disorders like sickle cell anemia. However, ethical concerns regarding germline editing and off-target mutations remain subjects of intense debate among researchers and policymakers.",
        "question": "What is the primary function of the guide RNA in the CRISPR-Cas9 system?",
        "options": [
            "To target specific nucleotide sequences for the Cas9 enzyme to cut",
            "To physically repair broken DNA strands after editing occurs",
            "To generate natural bacterial defenses against viral phages",
            "To replace diseased genes with artificial agricultural crops"
        ],
        "answer": 0,
        "explanation": "文章指出 system uses a guide RNA to target specific nucleotide sequences, allowing the Cas9 enzyme to cut the DNA，故选A。"
    },
    {
        "id": "toefl-r-175",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Neuroplasticity refers to the brain's ability to reorganize itself by forming new neural connections throughout life, especially in response to learning, experience, or brain injury. Historically, scientists believed that the adult brain was a fixed organ incapable of generating new neurons. However, modern neuroimaging studies have demonstrated that neural pathways can adapt, strengthen, or weaken based on mental activity and environmental demands. This adaptability is crucial for recovering lost functions after strokes or trauma, as undamaged areas can take over tasks previously handled by damaged regions. Educational strategies that promote active learning and cognitive training leverage neuroplasticity to enhance memory and problem-solving skills in learners of all ages.",
        "question": "What did historical scientific views maintain about the adult brain?",
        "options": [
            "It was a fixed organ incapable of generating new neurons",
            "It could easily reorganize itself after any brain injury",
            "It relied entirely on neuroplasticity for daily learning",
            "It was more adaptable than the brains of children"
        ],
        "answer": 0,
        "explanation": "文章第二句指出 historically, scientists believed that the adult brain was a fixed organ incapable of generating new neurons，故选A。"
    },
    {
        "id": "toefl-r-176",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Modern aerospace engineering has been profoundly transformed by the deployment of satellite constellations in low Earth orbit. Unlike traditional geostationary satellites that orbit at high altitudes, mega-constellations consist of hundreds or thousands of smaller satellites working in coordination. This configuration provides global broadband internet coverage with significantly lower latency, bridging digital divides in remote regions. However, this proliferation of space hardware raises serious concerns among astronomers and environmentalists regarding orbital debris, light pollution, and potential collision risks. Regulatory bodies face the challenge of establishing international guidelines for sustainable space traffic management.",
        "question": "What is a major advantage of low Earth orbit satellite mega-constellations over traditional geostationary satellites?",
        "options": [
            "They provide global broadband internet coverage with significantly lower latency",
            "They orbit at much higher altitudes to avoid space debris collisions",
            "They eliminate all forms of light pollution for optical astronomy",
            "They require fewer individual satellites to achieve global coverage"
        ],
        "answer": 0,
        "explanation": "文章指出 mega-constellations provides global broadband internet coverage with significantly lower latency，故选A。"
    },
    {
        "id": "toefl-r-177",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Nanotechnology involves the manipulation of matter on an atomic and molecular scale, typically between 1 and 100 nanometers. At this scale, materials exhibit novel physical, chemical, and biological properties that differ significantly from their macroscopic counterparts due to increased surface area-to-volume ratios and quantum effects. Nanomaterials are currently utilized in diverse fields, including targeted drug delivery systems in medicine, lightweight composite materials in aerospace, and more efficient catalysts in energy conversion. Despite these promising advancements, potential toxicity and environmental accumulation of engineered nanoparticles pose risks that require rigorous toxicological evaluation and safety regulation before widespread commercial deployment.",
        "question": "Why do nanomaterials exhibit novel properties compared to macroscopic materials?",
        "options": [
            "Due to increased surface area-to-volume ratios and quantum effects",
            "Because they are composed exclusively of biological molecules",
            "Due to their lower surface area-to-volume ratios in medicine",
            "Because they operate at scales larger than 100 nanometers"
        ],
        "answer": 0,
        "explanation": "文章指出 materials exhibit novel properties... due to increased surface area-to-volume ratios and quantum effects，故选A。"
    },
    {
        "id": "toefl-r-178",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Vertical farming is an innovative agricultural practice that involves growing crops in vertically stacked layers, often within controlled indoor environments such as warehouses or skyscrapers. By utilizing advanced hydroponic or aeroponic nutrient systems and artificial LED lighting that simulates optimal solar spectrums, vertical farms can achieve significantly higher crop yields per square foot than traditional agriculture. Furthermore, this method eliminates weather-related crop failures, reduces water usage by up to ninety percent, and removes the need for synthetic pesticides. However, high initial capital costs, substantial energy consumption for lighting and climate control, and limited crop variety remain economic hurdles for commercial scalability.",
        "question": "What is one major environmental benefit of vertical farming?",
        "options": [
            "It reduces water usage by up to ninety percent and removes pesticide needs",
            "It relies entirely on natural sunlight without any artificial LED lighting",
            "It lowers initial capital costs for commercial agricultural facilities",
            "It eliminates energy consumption for climate control systems"
        ],
        "answer": 0,
        "explanation": "文章指出 reduces water usage by up to ninety percent, and removes the need for synthetic pesticides，故选A。"
    },
    {
        "id": "toefl-r-179",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Deep-sea exploration has revealed remarkable ecosystems thriving in extreme conditions previously thought uninhabitable. Hydrothermal vents, discovered along tectonic spreading centers, spew mineral-rich water heated to over 400 degrees Celsius into the pitch-black ocean abyss. Instead of relying on photosynthesis, organisms such as giant tube worms and vent clams survive through chemosynthesis, utilizing hydrogen sulfide from the vent fluid. Bacteria form the base of this unique food web, converting chemical energy into organic matter. Exploring these remote environments expands our understanding of life's biochemical limits and offers clues about the potential for life on icy moons in our solar system.",
        "question": "How do organisms near hydrothermal vents sustain themselves without sunlight?",
        "options": [
            "Through chemosynthesis, utilizing hydrogen sulfide from vent fluid",
            "By performing specialized forms of deep-water photosynthesis",
            "By migrating to upper ocean layers during seasonal feeding cycles",
            "Through direct consumption of mineral-rich water heated to 400 degrees"
        ],
        "answer": 0,
        "explanation": "文章指出 organisms survive through chemosynthesis, utilizing hydrogen sulfide from the vent fluid，故选A。"
    },
    {
        "id": "toefl-r-180",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Paleontological discoveries of feathered dinosaurs have fundamentally transformed our understanding of avian evolution. Fossils unearthed in Liaoning, China, preserve exquisite details of feathers, ranging from simple filamentous structures to complex vaned plumes on dinosaurs like Sinosauropteryx and Velociraptor. These findings confirm that feathers originally evolved for insulation or display rather than powered flight, with aerodynamic functions developing later in small theropod lineages. Furthermore, sophisticated analyses of melanosomes preserved in fossil feathers have even allowed scientists to reconstruct the actual coloration and patterning of prehistoric animals, bridging the gap between imagination and empirical science in paleontology.",
        "question": "According to the passage, why did feathers originally evolve in dinosaurs?",
        "options": [
            "For insulation or display rather than powered flight",
            "For immediate aerodynamic lift and powered flight",
            "To help aquatic dinosaurs swim in deep prehistoric lakes",
            "To camouflage theropods against dense forest canopies"
        ],
        "answer": 0,
        "explanation": "文章指出 feathers originally evolved for insulation or display rather than powered flight，故选A。"
    },
    {
        "id": "toefl-r-181",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Climate change is driving significant geographic shifts in species distributions as ecosystems respond to rising global temperatures. Many terrestrial and marine organisms are migrating toward higher latitudes or higher elevations to remain within their preferred thermal envelopes. However, the rate of climate change often outpaces the dispersal capabilities of many plants and animals, leading to ecological mismatches and increased extinction risks. For example, migratory birds arriving earlier in spring may find that their insect food sources have already peaked. Conservation strategies now emphasize establishing climate corridors and protected migratory pathways to facilitate natural adaptation and biodiversity preservation.",
        "question": "What is one consequence when climate change outpaces a species' dispersal capabilities?",
        "options": [
            "Ecological mismatches and increased extinction risks",
            "Instantaneous evolution of thermal tolerance traits",
            "Successful migration toward equatorial regions",
            "A complete halt to global temperature increases"
        ],
        "answer": 1,
        "explanation": "文章指出 rate of climate change often outpaces dispersal... leading to ecological mismatches and increased extinction risks，故选A。"
    },
    {
        "id": "toefl-r-182",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Social media platforms have profoundly altered public discourse by reshaping how information is disseminated, consumed, and debated. Algorithms designed to maximize user engagement frequently create echo chambers, where individuals are exposed predominantly to viewpoints that align with their existing beliefs. This selective exposure can polarize societal debates and accelerate the spread of misinformation and sensationalized content. At the same time, social media empowers grassroots social movements by enabling rapid mobilization and direct communication without traditional media gatekeepers. Researchers study these dynamics to develop interventions that promote digital literacy and constructive civic engagement online.",
        "question": "What role do engagement-maximizing algorithms play on social media platforms?",
        "options": [
            "They frequently create echo chambers that expose users to aligned viewpoints",
            "They prevent the spread of misinformation and sensationalized content",
            "They act as traditional media gatekeepers for grassroots movements",
            "They eliminate all forms of societal polarization and debate"
        ],
        "answer": 1,
        "explanation": "文章指出 algorithms designed to maximize user engagement frequently create echo chambers，故选A。"
    },
    {
        "id": "toefl-r-183",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Cryptocurrency markets have introduced decentralized digital assets enabled by blockchain technology, challenging traditional fiat monetary systems. Cryptocurrencies like Bitcoin operate on distributed ledgers maintained by a network of computers, eliminating the need for central banking authorities. While this decentralization offers financial inclusion and transparency, high price volatility, regulatory uncertainty, and environmental concerns regarding energy-intensive mining processes present significant challenges. Central banks worldwide are currently exploring central bank digital currencies (CBDCs) as a regulated alternative that combines the efficiency of digital transactions with monetary stability and government oversight.",
        "question": "What is a major challenge associated with cryptocurrencies like Bitcoin?",
        "options": [
            "High price volatility and energy-intensive mining processes",
            "Total dependence on central banking authorities for transactions",
            "Complete elimination of blockchain and distributed ledger technology",
            "A lack of transparency in distributed computer networks"
        ],
        "answer": 1,
        "explanation": "文章指出 high price volatility... and environmental concerns regarding energy-intensive mining present challenges，故选A。"
    },
    {
        "id": "toefl-r-184",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Human decision making is frequently influenced by cognitive biases and heuristics, which are mental shortcuts that simplify complex choices but can lead to systematic errors. Daniel Kahneman and Amos Tversky identified key heuristics such as availability heuristic, where people judge the frequency of an event by how easily examples come to mind, and anchoring effect, where initial information disproportionately influences subsequent estimates. Understanding these cognitive limitations is crucial in fields such as public policy, finance, and medicine, where flawed judgment can have severe consequences. Debiasing techniques and structured analytical frameworks are often implemented to help professionals make more objective and rational decisions.",
        "question": "What does the availability heuristic involve in human decision making?",
        "options": [
            "Judging the frequency of an event by how easily examples come to mind",
            "Allowing initial information to disproportionately influence estimates",
            "Completely eliminating all mental shortcuts and cognitive biases",
            "Making complex choices without relying on any memory recall"
        ],
        "answer": 1,
        "explanation": "文章指出 availability heuristic is where people judge the frequency of an event by how easily examples come to mind，故选A。"
    },
    {
        "id": "toefl-r-185",
        "exam": "toefl",
        "section": "reading",
        "part": 1,
        "passage": "Invasive species represent a major threat to global biodiversity and ecosystem stability when introduced to new environments outside their native ranges. Lacking natural predators or diseases in their introduced habitats, invasive species can multiply rapidly and outcompete native flora and fauna for vital resources such as food, water, and space. For example, the introduction of the brown tree snake to Guam decimated native forest bird populations, while zebra mussels in North American waterways clog industrial infrastructure and disrupt aquatic food webs. Management strategies involve early detection, rapid eradication, and biological control using specialized natural enemies, though prevention remains the most cost-effective approach.",
        "question": "Why do invasive species often multiply rapidly in newly introduced environments?",
        "options": [
            "They lack natural predators or diseases in their new habitats",
            "They instantly adapt to become native flora and fauna",
            "They rely exclusively on industrial infrastructure for survival",
            "They intentionally cooperate with native species for shared resources"
        ],
        "answer": 1,
        "explanation": "文章指出 lacking natural predators or diseases in their introduced habitats, invasive species can multiply rapidly，故选A。"
    }
]

# Fix answer distribution to be balanced (8-9 each for 0,1,2,3)
# Currently: 28 with answer 0, 5 with answer 1
# Target: ~8 each

# Questions to change (indices 0-27 currently have answer 0)
# We'll change some to 1, 2, 3
changes = {
    0: 0,   # toefl-r-153: keep 0
    1: 1,   # toefl-r-154: 0->1
    2: 2,   # toefl-r-155: 0->2
    3: 3,   # toefl-r-156: 0->3
    4: 0,   # toefl-r-157: keep 0
    5: 1,   # toefl-r-158: 0->1
    6: 2,   # toefl-r-159: 0->2
    7: 3,   # toefl-r-160: 0->3
    8: 0,   # toefl-r-161: keep 0
    9: 1,   # toefl-r-162: 0->1
    10: 2,  # toefl-r-163: 0->2
    11: 3,  # toefl-r-164: 0->3
    12: 0,  # toefl-r-165: keep 0
    13: 1,  # toefl-r-166: 0->1
    14: 2,  # toefl-r-167: 0->2
    15: 3,  # toefl-r-168: 0->3
    16: 0,  # toefl-r-169: keep 0
    17: 1,  # toefl-r-170: 0->1
    18: 2,  # toefl-r-171: 0->2
    19: 3,  # toefl-r-172: 0->3
    20: 0,  # toefl-r-173: keep 0
    21: 1,  # toefl-r-174: 0->1
    22: 2,  # toefl-r-175: 0->2
    23: 3,  # toefl-r-176: 0->3
    24: 0,  # toefl-r-177: keep 0
    25: 1,  # toefl-r-178: 0->1
    26: 2,  # toefl-r-179: 0->2
    27: 3,  # toefl-r-180: 0->3
}

for idx, new_ans in changes.items():
    q = questions[idx]
    # Current correct option is at index q["answer"] (0 for all of these)
    # Swap so the correct option ends up at new_ans
    opts = q["options"]
    correct = opts[q["answer"]]
    opts[q["answer"]], opts[new_ans] = opts[new_ans], opts[q["answer"]]
    q["answer"] = new_ans
    # Update explanation letter
    letters = "ABCD"
    q["explanation"] = q["explanation"].rstrip("。") + f"，故选{letters[new_ans]}。"

# Check current answers
answers = [q["answer"] for q in questions]
from collections import Counter
dist = Counter(answers)
print("Current answer distribution:", dict(dist))
print(f"Total questions: {len(questions)}")

# Verify all passages are 120-180 words
for q in questions:
    wc = len(q["passage"].split())
    if wc < 120 or wc > 180:
        print(f"WARNING: {q['id']} has {wc} words")
    else:
        print(f"OK: {q['id']} has {wc} words")

# Verify IDs are continuous
ids = [q["id"] for q in questions]
expected = [f"toefl-r-{i}" for i in range(153, 186)]
if ids == expected:
    print("IDs are continuous and correct!")
else:
    print("ID mismatch!")
    print("Missing:", set(expected) - set(ids))
    print("Extra:", set(ids) - set(expected))

# Verify 4 distinct options per question
for q in questions:
    opts = q["options"]
    if len(opts) != 4 or len(set(opts)) != 4:
        print(f"WARNING: {q['id']} has invalid options")

# Write final JSON
output_data = {"questions": questions}

with open(r"D:\work\Hermes\testprep-app\data_gen\output\toefl-r_01.json", "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print("File written successfully!")
