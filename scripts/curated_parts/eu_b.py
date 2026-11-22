from _common import trip, hotel, stay_area, day, sight, route, dish, faq, stop
TRIPS = []

# Uncertainties worth a second look:
# - Citadines Les Halles, Citadines Saint-Germain-des-Prés, and Adagio Paris Opéra
#   do not publish a true two-bedroom. The largest plan at each is one bedroom
#   plus a sofa bed. paris-2-bedroom-under-400night uses three Adagio properties
#   that do list a two-bedroom apartment. Live rates were not rechecked.
# - Hôtel Le Trou Normand (Deauville) was not verified and is not listed.
# - Hotel de Russie's pool is a shared spa hydrotherapy pool, not a lap pool.
# - Anantara Palazzo Naiadi says its rooftop pool is closed from 5 October 2026
#   until summer 2027. Reconfirm before anyone books it in order to swim.
# - No private-pool villa is named. Château d'Esclimont was skipped on purpose.
# - Peninsula Paris and Le Royal Monceau: shared pools; the guest-entry fee was
#   not rechecked. Crillon's indoor pool is about 14 meters and shared.
# - Hôtel Napoléon Fontainebleau has a shared indoor spa pool on a paid time slot.
#   It is not a private pool.
# - Hotel homepages are linked only when they were on the allowed list.


def add(record):
    TRIPS.append(record)


add(trip(
    slug="paris-city-center-walkable",
    title="Walkable Paris: the islands, the Marais, and one museum",
    location="Paris, France",
    summary=(
        "Four nights in the 1st, 4th, 5th, and 6th for people who want the river outside the door. "
        "You walk both islands, sleep in the Marais, on the Panthéon, or in Sentier, and spend one morning "
        "in a single museum. The Eiffel Tower is a different day, in a different arrondissement, and it is not this trip."
    ),
    who="A couple or two friends who would rather cross a bridge than change metro lines.",
    best_time="April to June, or late September through October. August is hot and a lot of small dining rooms close. The Louvre is closed on Tuesdays.",
    nights=4,
    hook="4 nights · Islands and the Marais · $180–350/night",
    constraints=["Walkable center", "No car", "One museum, not a museum pass"],
    lodging="$180–350",
    daily="$270–460",
    neighborhoods=[
        stay_area("Le Marais and the islands", "The 4th puts Notre-Dame, the Place des Vosges, and Île Saint-Louis inside a 20-minute walk. Sunday is busy. Monday morning is quiet."),
        stay_area("Panthéon and Saint-Germain", "The 5th and 6th are the Luxembourg and the dinner streets. Hôtel des Grands Hommes faces the Panthéon; the islands are a walk down the hill."),
    ],
    hotels=[
        hotel("Hôtel Jeanne d'Arc Le Marais", "Le Marais, rue de Jarente", "The long-running Marais hotel on a small 4th-arrondissement street. Rooms are basic and often small. The tiled mirror in the lounge is the flourish. You are here because the islands and the Place des Vosges are a walk.", "$140–230", "Paris"),
        hotel("Hôtel des Grands Hommes", "Place du Panthéon", "A literary hotel on the square, the kind of place André Breton actually stayed. Quieter at night than a Marais crossroads. The 6th, the Luxembourg, and the Petit Pont are all downhill on foot.", "$220–400", "Paris"),
        hotel("The Hoxton Paris", "Sentier, 2nd", "A reliable base just north of the 1st, with a lobby people use. Walk south to the Palais-Royal and the river in about 20 minutes. Ask for a room off the street if you hate noise.", "$230–420", "Paris", "https://thehoxton.com/paris/"),
    ],
    itinerary=[
        day(1, "Both islands, before the museums", "Arrive and learn the river on foot. No ticketed interior yet.", "Drop bags and walk to the Pont Neuf. From the Hoxton that is about 25 minutes; from Jeanne d'Arc, about 15; from the Panthéon, down through the 5th to the Petit Pont. Henri IV's statue is the marker. Step down to Square du Vert-Galant if you want the water at eye level.", "Cross onto Île de la Cité. See Notre-Dame from the parvis, then Sainte-Chapelle if your timed slot is today. Cross the Pont Saint-Louis and walk the full quay circuit of Île Saint-Louis.", "Dinner on rue Saint-Louis-en-l'Île, or walk into the Marais if you want a louder street. Ice cream from Berthillon only when the line is short.", "Book Notre-Dame's free interior slot and Sainte-Chapelle before you book dinner. The outside of the cathedral is the backup.", "Notre-Dame de Paris"),
        day(2, "One museum, then the square", "The Louvre in the morning, and then you are done with museums.", "Louvre, Denon wing, at opening, with a timed ticket. Enter through the Carrousel, not the pyramid queue. Winged Victory, the big Italian rooms, the Mona Lisa because you are already there, and then leave. Two and a half hours.", "Walk out through the Tuileries, not back through the mall. Cross to the Marais by the Hôtel de Ville and sit in the Place des Vosges. The arcades are the sight.", "Dinner in the Marais. Breizh Café on rue Vieille du Temple for a galette if you booked. L'As du Fallafel on rue des Rosiers is the lunch line, not a romantic dinner.", "The Louvre is closed on Tuesdays. If that is your morning, swap in the Musée d'Orsay and skip the Louvre for the trip.", "Louvre"),
        day(3, "The 6th, slowly", "A garden, a church, and a dinner street. No second museum.", "Luxembourg Gardens when the gates open. The Médicis fountain is on the rue de Médicis side, which people miss if they only photograph the palace façade. Take a green chair and stay.", "Saint-Germain-des-Prés: the abbey church, then rue de Seine. Coffee at Café de Flore if you want the room, or a cheaper cup on rue des Canettes. Shakespeare and Company only if you are already on the quay and the line is sane.", "Dinner in the 6th. Le Relais de l'Entrecôte on rue Saint-Benoît if you want steak-frites and nothing else; they do not take bookings and the line moves. Otherwise a bistro on rue de Seine.", "Sunday is lively in the Marais and quiet in parts of the 6th. Flip this day with day 4 if you land on a Sunday.", "Luxembourg Gardens"),
        day(4, "Market, then the station", "A last morning in the Marais, then the train. The Eiffel Tower stays off the list.", "Marché des Enfants Rouges, 39 rue de Bretagne, if you want food instead of a monument. It is the old covered market of the Marais. Go when it opens.", "A last loop of the Place des Vosges and the Seine along the Quai de Bourbon. Do not add the Eiffel Tower. It sits in the 7th and it takes the rest of the day.", "CDG is the RER B from Saint-Michel or Châtelet. Orly is metro 14 from Châtelet. Eat before the station.", "If you still have an unused Notre-Dame interior slot, use it at opening and cut the market.", "Place des Vosges"),
    ],
    attractions=[
        sight("Notre-Dame de Paris", "The island church, which you will walk past more than once.", "The interior is free and timed. The outside is the plan if the slot is gone.", "Notre-Dame de Paris"),
        sight("Sainte-Chapelle", "The upper chapel, which is the reason to queue.", "First slot of the day. The lower chapel is the warmup, not the point.", "Sainte-Chapelle"),
        sight("Louvre", "One wing, in the morning, in a building you will not finish.", "Denon wing. Carrousel entrance. Out through the Tuileries.", "Louvre"),
        sight("Luxembourg Gardens", "The 6th-arrondissement park, with chairs you can move.", "Médicis fountain first, palace façade second.", "Luxembourg Gardens"),
        sight("Place des Vosges", "The square the Marais walk is actually for.", "Sit. The shops in the arcades can wait.", "Place des Vosges"),
        sight("Île Saint-Louis", "The smaller island, which is a residential street with a view.", "Walk the quays once. Berthillon is optional.", "Île Saint-Louis"),
        sight("Musée d'Orsay", "The alternate museum if the Louvre is closed or if you care more about Impressionists.", "It is a single building. Ninety minutes is a real visit. Closed Mondays.", "Musée d'Orsay"),
    ],
    scenic_routes=[
        route("Island circuit", "Pont Neuf, Square du Vert-Galant, Île de la Cité, Pont Saint-Louis, the full quay loop of Île Saint-Louis, back by the Pont de la Tournelle.", "About 4 km, 90 minutes"),
        route("Vosges to the Luxembourg", "Place des Vosges, rue des Francs-Bourgeois, across the river at the Pont Marie or the Petit Pont, up through the 5th to the gardens.", "About 5 km, 2 hours"),
        route("Quai de Bourbon at dusk", "Hôtel de Ville along the right-bank quay, across to the Quai de Bourbon, and into Saint-Germain if your feet still agree.", "About 3 km, 1 hour"),
    ],
    transport="Walk. All three hotels sit inside a half-hour of the islands on foot. Buy a couple of metro tickets for the airport, for rain, or for a bad blister. CDG is the RER B. Orly is metro 14. A taxi at 8 a.m. on a weekday is the expensive way to do the same trip.",
    food=[
        dish("Galette complète", "Breizh Café, rue Vieille du Temple", "Buckwheat, ham, egg, cheese. Book. Cider is the Breton pairing; wine is fine if you insist."),
        dish("Falafel", "L'As du Fallafel, rue des Rosiers", "The famous one, eaten on the street. Go at noon on a weekday or accept the line. Once is enough."),
        dish("Glace", "Berthillon, rue Saint-Louis-en-l'Île", "Two scoops, walking the quay. If the line blocks the sidewalk, buy from the takeaway window or skip it."),
        dish("Steak-frites", "Le Relais de l'Entrecôte, rue Saint-Benoît", "There is no menu to speak of. They do not take reservations. Share a starter or you will not finish the second sitting of meat."),
    ],
    tips=[
        "One museum. Louvre plus Orsay plus Sainte-Chapelle in a single day is how a walking trip turns into a queue.",
        "Notre-Dame's interior and Sainte-Chapelle are separate bookings. Read which one you bought.",
        "Rue de Rivoli rooms are loud. Ask for a courtyard at any of these hotels if you sleep lightly.",
        "Dinner places you have heard of need a reservation before you fly. Wine bars still take walk-ins.",
    ],
    faqs=[
        faq("Can I do this without the metro?", "Yes. The Hoxton to Île Saint-Louis is about half an hour on foot. Jeanne d'Arc and des Grands Hommes are closer to the river."),
        faq("Which single museum?", "The Louvre, Denon wing, at opening. If you want Impressionists more than the palace, do the Musée d'Orsay instead and skip the Louvre entirely."),
        faq("Is the Marais all right at night?", "Yes. Weekend streets are crowded. Keep the phone in a pocket on rue de Rivoli and you will be fine."),
        faq("What does a walkable room cost?", "Jeanne d'Arc can land under $200. A nicer room at des Grands Hommes or the Hoxton is often $250–400. Under $150 in these arrondissements is a very small room."),
    ],
    map_places=[
        stop("Notre-Dame de Paris", "Paris", "France", "Notre-Dame de Paris"),
        stop("Sainte-Chapelle", "Paris", "France", "Sainte-Chapelle"),
        stop("Louvre", "Paris", "France", "Louvre"),
        stop("Luxembourg Gardens", "Paris", "France", "Luxembourg Gardens"),
        stop("Place des Vosges", "Paris", "France", "Place des Vosges"),
        stop("Île Saint-Louis", "Paris", "France", "Île Saint-Louis"),
    ],
    budget_notes="Lodging is $180–350 for a real room in these arrondissements. Jeanne d'Arc is the cheap end; the Hoxton and des Grands Hommes climb on weekends. A sit-down dinner is $50–80 a person. The Louvre is about $25, Sainte-Chapelle about $15, and the walks are free. One museum keeps the daily number honest.",
))


add(trip(
    slug="paris-2-bedroom-under-400night",
    title="A real second bedroom in Paris, under $400 when the city allows it",
    location="Paris, France",
    summary=(
        "Citadines Les Halles, Citadines Saint-Germain-des-Prés, and Adagio Paris Opéra do not have two bedrooms. "
        "Their biggest apartment is a bedroom plus a sofa bed, sold as sleeping four. If you need two doors that close, "
        "book a two-bedroom at Adagio by the Eiffel Tower, in Bercy, or at Buttes-Chaumont, and expect summer and fashion weeks to push the Eiffel one through $400."
    ),
    who="A family or four adults who have been burned by a 'sleeps 4' listing that was a sofa in the living room.",
    best_time="March outside fashion week, or late October and November, if the $400 cap matters. Late February, late September, and June through August are when the two-bedroom rate jumps.",
    nights=4,
    hook="4 nights · A real second bedroom · $200–380/night",
    constraints=["Two separate bedrooms", "A kitchen you can cook in", "Under about $400 outside peak weeks"],
    lodging="$200–380",
    daily="$270–450",
    neighborhoods=[
        stay_area("Bercy, 12th", "The practical base. Parc de Bercy, a grocery, and metro 14 to Châtelet in about 10 minutes. This is the itinerary below."),
        stay_area("15th by the Tower, or the 19th by the park", "Adagio Tour Eiffel is the postcard and the one that breaks $400. Buttes-Chaumont is quieter, greener, and a commute to the islands."),
    ],
    hotels=[
        hotel("Adagio Paris Bercy Village", "12th, Cour du Minervois", "An established aparthotel beside Bercy Village with a real two-bedroom of about 55 square meters, kitchen included, sleeping up to six only because of a sofa bed. The rate more often stays under $400 than the Eiffel building. Metro 14 is the way into the center.", "$200–360", "Paris"),
        hotel("Adagio Paris Centre Tour Eiffel", "15th, rue du Théâtre", "The two-bedroom here is about 75 square meters: a double room, a twin room, and a sofa bed. Rue du Commerce is the real shopping street. Book this when the address matters, and treat $400 as a shoulder-season number.", "$280–480", "Paris"),
        hotel("Adagio Paris Buttes-Chaumont", "19th, Cours du 7ème Art", "A smaller aparthotel by the park, with a two-bedroom around 50 square meters. The most likely of the three to hold the cap. You are not walking to Notre-Dame. The park is the reason to accept the metro.", "$180–320", "Paris"),
    ],
    itinerary=[
        day(1, "Move in and buy food", "The base is Bercy. The other two hotels are named where the walk changes.", "Check in and find the grocery before you find a monument. Cour Saint-Émilion has enough shops for a first dinner. If you booked the 15th, rue du Commerce is the run. If you booked the 19th, shop on the park edge.", "Parc de Bercy: the vineyard, the lake, and the passerelle Simone-de-Beauvoir. That is the orientation walk. Tour Eiffel guests do the Champ de Mars lawn and do not buy a tower ticket today. Buttes-Chaumont guests do the park's temple and the suspension bridge.", "Cook. A roast chicken, a baguette, a salad. The first night in a restaurant for four people is how a $400 apartment becomes a $600 day.", "Email ahead and keep the reply that says two separate bedrooms. 'Sleeps 6' includes the sofa.", "Parc de Bercy"),
        day(2, "The islands, then home for lunch", "One short trip into the center. The apartment is the midday plan.", "Metro 14 from Cour Saint-Émilion to Châtelet, about 10 minutes. Walk the two islands for two hours. Notre-Dame from the parvis, Île Saint-Louis once around, and stop. This is not the Louvre day.", "Back to the apartment for a late lunch and a rest. The park again in the afternoon, which is the point of having a kitchen. Children get a playground. Adults get a bench.", "Dinner near the apartment. Bercy Village has tables; you do not need to cross the city. One metro home is the rule.", "From the 15th, do this day on the Champ de Mars and save the islands for a morning when everyone slept. From the 19th, the park replaces the second outing.", "Île Saint-Louis"),
        day(3, "A market, then a flat walk", "Buy dinner. Then a path that does not involve a museum.", "Marché d'Aligre in the morning, at Ledru-Rollin, a short metro hop from Bercy. It is closed on Monday. Buy fruit, a comté, and something for the evening. The 15th equivalent is Marché Grenelle on Wednesday or Sunday. The 19th can use a market by Jaurès.", "Coulée verte René-Dumont if you want a lifted railway, entered from the Viaduc des Arts near Bastille. Do an hour, not the whole length. Otherwise the Seine bank at Bercy.", "Cook what you bought. A second restaurant night is optional and should be walking distance.", "Sunday markets pack up in the early afternoon. Go at 9.", "Coulée verte René-Dumont"),
        day(4, "Out from Gare de Lyon", "A short morning, then the station, which is close.", "Breakfast from a bakery on Cour Saint-Émilion. A last turn through Parc de Bercy if the train is after lunch.", "Gare de Lyon is about 15 minutes on foot from this apartment. CDG is a change; Orly is metro 14 without going backwards into town. Do not schedule Versailles on the way to the airport.", "Eat the food still in the fridge before you leave. Apartment check-out is often 11:00, earlier than a hotel.", "If you are in the 15th or the 19th, give yourself a full extra hour to cross town with bags.", ""),
    ],
    attractions=[
        sight("Parc de Bercy", "The local park: vines, a lake, and playgrounds, next to the apartment.", "The vineyard corner is the part that does not feel like a dog run.", "Parc de Bercy"),
        sight("Cour Saint-Émilion", "The old wine warehouses, now the shops and the metro.", "Useful for groceries and a backup dinner. It is not a secret.", ""),
        sight("Marché d'Aligre", "The market morning that makes the kitchen worth it.", "Closed Monday. Go early on Sunday.", ""),
        sight("Coulée verte René-Dumont", "A planted railway viaduct, an hour's walk from Bastille.", "Out and back. The full line to the Bois de Vincennes is a different trip.", "Coulée verte René-Dumont"),
        sight("Île Saint-Louis", "The one center outing, done in a morning.", "Two hours, then the metro home.", "Île Saint-Louis"),
        sight("Notre-Dame de Paris", "Seen from the parvis on the island morning.", "A timed interior only if you already have the slot. Do not build the day around the queue.", "Notre-Dame de Paris"),
        sight("Parc des Buttes-Chaumont", "The reason to book the 19th instead of the center.", "The temple and the suspension bridge. Weekday mornings are the quiet version.", "Parc des Buttes-Chaumont"),
    ],
    scenic_routes=[
        route("Parc de Bercy loop", "Vineyard, lake, and the passerelle Simone-de-Beauvoir to the library side and back.", "About 3 km, 1 hour"),
        route("Line 14 and the islands", "Cour Saint-Émilion to Châtelet, then Notre-Dame and a lap of Île Saint-Louis.", "10 minutes on the metro, then about 3 km on foot"),
        route("Aligre to the Coulée verte", "Market at Ledru-Rollin, then the Viaduc des Arts entrance and an hour on the viaduct.", "About 3 km, 90 minutes with the market"),
    ],
    transport="No car. Parking is paid and the two-bedroom does not need one. Metro 14 from Bercy, line 6 or 8 from the 15th, line 7 or 5 from Buttes-Chaumont. Buy groceries on foot. A Navigo Easy loaded with a few rides is enough for four days.",
    food=[
        dish("Poulet rôti", "A rôtisserie near Cour Saint-Émilion or the Aligre market", "The Sunday lunch of people who live here. Eat it in the apartment with a baguette and a green salad."),
        dish("Comté and a baguette", "Marché d'Aligre", "Buy the cheese in the morning and let it sit. This is dinner if you also bought tomatoes."),
        dish("Jambon-beurre", "A bakery, not a café terrace", "Butter, not mayonnaise. The lunch that keeps the restaurant budget for one real dinner."),
        dish("Banh mi", "Avenue de Choisy, a short hop south into the 13th", "The better cheap lunch if you are bored of bread. Go to the avenue, not to a souvenir café in Bercy Village."),
    ],
    tips=[
        "Get the two-bedroom confirmation in writing. A one-bedroom plus a sofa bed is what the famous central aparthotels actually sell.",
        "Fashion weeks, roughly late February and late September, move prices across the city. June through August does it again, especially at the Tour Eiffel building.",
        "The 19th is a park holiday. It is a dull commute to the Louvre with small children and a stroller.",
        "Kitchens are real and small. Shop daily. A frying pan and a drip coffee maker, not a dining room.",
    ],
    faqs=[
        faq("Do Citadines Les Halles, Citadines Saint-Germain, or Adagio Opéra have two bedrooms?", "No. Each tops out at a one-bedroom apartment with a sofa bed. Sleeps-four is not a second bedroom."),
        faq("Will $400 hold?", "At Bercy and Buttes-Chaumont, often, outside summer and fashion weeks. At the Tour Eiffel two-bedroom, treat $400 as a shoulder-season rate."),
        faq("Are the two-bedrooms one level?", "The Adagio plans used here are apartments, not the duplex townhouses some Citadines buildings use. Ask about stairs anyway if you are bringing a stroller inside the unit."),
        faq("Do we need a car?", "No. A car in the 12th, 15th, or 19th is a parking bill. The metro does the one center day."),
    ],
    map_places=[
        stop("Parc de Bercy", "Paris", "France", "Parc de Bercy"),
        stop("Marché d'Aligre", "Paris", "France", ""),
        stop("Coulée verte René-Dumont", "Paris", "France", "Coulée verte René-Dumont"),
        stop("Notre-Dame de Paris", "Paris", "France", "Notre-Dame de Paris"),
        stop("Parc des Buttes-Chaumont", "Paris", "France", "Parc des Buttes-Chaumont"),
        stop("Champ de Mars", "Paris", "France", "Champ de Mars"),
    ],
    budget_notes="The cap is the apartment, not the whole day. A Bercy or Buttes-Chaumont two-bedroom often lands at $200–360 outside peak weeks. The Tour Eiffel two-bedroom is the one that prints $400-plus in summer. Groceries for four can stay near $40–60 a day if you cook two nights. One island morning adds metro fares and maybe a $25 cathedral-adjacent splurge, not a second hotel.",
))


add(trip(
    slug="paris-mountain-or-nature-view",
    title="Paris has no mountains: sleep in Fontainebleau and walk the forest",
    location="Paris, France",
    summary=(
        "Paris has no mountains, no alpine view, and no honest way to pretend the Bois de Boulogne is wilderness. "
        "This is the nature version of a Paris trip: four nights in Fontainebleau, a train of about 40 minutes from Gare de Lyon, "
        "with the forest and the château as the days. Hôtel Molitor is the in-city alternative if you refuse to leave Paris, and its famous pools are shared and beside the point."
    ),
    who="People who asked for a mountain or a nature view and would rather change towns than be sold a park bench.",
    best_time="May, June, September, and October. The rocks are hot and busy on summer weekends. The château is closed on Tuesdays. Winter walks are good and muddy, and the days are short.",
    nights=4,
    hook="4 nights · Fontainebleau forest · $180–360/night",
    constraints=["Nature, honestly", "No fake mountain view", "Forest base, not a boulevard hotel"],
    lodging="$180–360",
    daily="$260–450",
    neighborhoods=[
        stay_area("Fontainebleau town", "Sleep facing the château or on rue Grande. The forest starts about a kilometer out. This is the base the days assume."),
        stay_area("Porte Molitor, 16th", "Only if you will not take the train. The Bois de Boulogne is a designed park with lakes and roads. Molitor's pools are a shared hotel amenity."),
    ],
    hotels=[
        hotel("Hôtel Aigle Noir", "Fontainebleau, place Napoléon Bonaparte", "A mansion hotel facing the château, in business on this square since the 18th century. No pool. The forest is about a kilometer. This is the room to book for the walk.", "$220–420", "Fontainebleau"),
        hotel("Hôtel Napoléon Fontainebleau", "Fontainebleau, rue Grande", "A four-star at 9 rue Grande, a few minutes from the château gate. There is a shared indoor spa pool on a paid, timed slot. Ignore it. You are here for the trail at the edge of town.", "$180–340", "Fontainebleau"),
        hotel("Hôtel Molitor", "16th, Porte Molitor", "The 1929 pool complex, now a hotel, about 500 meters from the Bois de Boulogne. Book it only if you will not go to Fontainebleau. The indoor and outdoor pools are shared, famous, and not a nature view. The Bois is a park.", "$350–650", "Paris"),
    ],
    itinerary=[
        day(1, "Train, gardens, town", "Get out of Paris before you start sightseeing.", "Transilien from Gare de Lyon to Fontainebleau-Avon, about 40 minutes, then the local bus to the château stop, about 15 minutes. A taxi from the station is the version with bags. Check in and leave the bags.", "The château gardens and the carp pond, not the state apartments. You will do interiors on a later morning when you are not carrying a suitcase in your head. The Jardin de Diane is the quiet piece next to Aigle Noir.", "Dinner on rue Grande. Le Cadran, the brasserie at Hôtel Napoléon, is the easy booking if you do not want to hunt.", "The château building is closed on Tuesdays. Put interiors on another day even if the park is open.", "Palace of Fontainebleau"),
        day(2, "The rocks, which are the view", "Sandstone boulders. That is the mountain this region has.", "Taxi to the Apremont trailhead in the morning. Agree a return time or plan a marked walk back toward town. Follow the Denecourt paint marks. The gorge loop is the sight: boulders, pines, and a view that is a few dozen meters up, which is the honest skyline.", "Stay out through lunch. A jambon-beurre from a rue Grande bakery, eaten on a rock. Back in town by late afternoon. Do not start a new trail at 4 p.m. The marks are clear and the light goes anyway.", "A quiet dinner. You will be tired in the legs, not in the 'we did three museums' way. Drink water before the wine.", "Sneakers with tread. The rock is smooth and people twist ankles here every weekend.", "Forest of Fontainebleau"),
        day(3, "Interiors, then Barbizon", "The palace in the morning, the painters' village after.", "Château interiors with a timed ticket. The horseshoe staircase, the François I gallery, and Napoleon's apartment if it is on the circuit that day. Two hours. The audioguide is worth it because the rooms are a sequence, not a pile.", "Barbizon, about 10 minutes by taxi, on the forest edge. One main street, the inn where the painters stayed, and a walk into the trees they painted. Millet and Rousseau are the names. You do not need a museum ticket to understand the place.", "Back in Fontainebleau for dinner. If Barbizon caught you at lunch, keep the evening simple.", "Barbizon on a Sunday afternoon can be a coach stop. Go on a weekday if your dates allow.", "Barbizon"),
        day(4, "A short forest morning, then Paris", "Leave from the town, not from a trailhead at dusk.", "One more marked path close to town, or a last loop of the carp pond if your train is at noon. Buy food for the ride on rue Grande.", "Train back to Gare de Lyon. If you have three spare hours and a later flight, the Bois de Vincennes is the green space on this side of Paris, at Lac Daumesnil. If you do not, go to the airport. A Louvre dash with forest mud on your shoes is a bad ending.", "CDG and Orly are back in Paris logistics. Give yourself the transfer you would have given yourself from a city hotel, plus the Fontainebleau train.", "Molitor guests, who never came out here, should spend this morning in the Bois de Boulogne and call that the honest version of their booking.", "Bois de Vincennes"),
    ],
    attractions=[
        sight("Palace of Fontainebleau", "The royal and imperial château, with a park you can walk even when the rooms are enough.", "Interiors on a timed ticket, not on the day you arrive with bags. Closed Tuesdays.", "Palace of Fontainebleau"),
        sight("Forest of Fontainebleau", "The actual nature: pines, sand, and sandstone gorges.", "Stay on the marked Denecourt trails. Download a map before the trees eat the signal.", "Forest of Fontainebleau"),
        sight("Gorges d'Apremont", "The boulder field people mean when they imagine a view near Paris.", "Go in the morning with water. The 'summit' is a rock, and that is the point.", ""),
        sight("Barbizon", "The village on the forest edge where the landscape painters worked.", "A weekday. One street, then the trees.", "Barbizon"),
        sight("Bois de Boulogne", "The in-city park next to Molitor. Lakes, roads, and the Pré Catelan.", "A picnic and a loop. It is not a substitute for the forest day.", "Bois de Boulogne"),
        sight("Bois de Vincennes", "The large park on the Gare de Lyon side of Paris.", "Lac Daumesnil if you have a few hours on the way home. Skip it if the flight is tight.", "Bois de Vincennes"),
    ],
    scenic_routes=[
        route("Gorges d'Apremont loop", "A marked Denecourt circuit from the Apremont parking area through the boulders and back. Taxi from town to the start.", "About 6 km, 2.5 hours"),
        route("Château park and the carp pond", "From the gate past the horseshoe staircase, through the gardens to the carp pond and back by the Jardin de Diane.", "About 3 km, 90 minutes"),
        route("Train and bus from Paris", "Gare de Lyon to Fontainebleau-Avon, then the local bus to the château. The scenic part starts when the apartment blocks stop.", "About 40 minutes on the train, 15 on the bus"),
    ],
    transport="Train from Gare de Lyon, then the town bus or a taxi to the hotel. You can do the château and Barbizon without a car. A taxi to the Apremont trailhead makes the forest morning simple; agree the pickup before the driver leaves. A rental car helps only if you want several trailheads in one day.",
    food=[
        dish("Jambon-beurre", "A bakery on rue Grande", "Buy it before the taxi to the rocks. Eat it sitting down on stone, not in a restaurant with sandy shoes."),
        dish("Plat du jour", "Le Cadran, Hôtel Napoléon", "The hotel brasserie. A reasonable dinner when you do not want to explore a small town at 9 p.m."),
        dish("Fromage de Fontainebleau", "A fromager in town", "The local fresh cream cheese, with berries. It has nothing to do with the château except the name."),
        dish("A long lunch in Barbizon", "The village street", "Eat after the walk, not before. The village is one street, so pick a kitchen you can see into."),
    ],
    tips=[
        "The view is a boulder field, not a peak. Anyone selling an alpine panorama from a Paris hotel is describing a poster.",
        "Download the IGN map or a Denecourt overlay in town. Signal in the gorges is a rumor.",
        "The château is closed on Tuesdays. Gardens and forest still work that day.",
        "Molitor is a pool hotel next to a park. Do not book it expecting the Fontainebleau day to magically happen before breakfast.",
    ],
    faqs=[
        faq("Are there mountains near Paris?", "No. Fontainebleau's sandstone is the rugged walk. The Alps are a different country-sized trip."),
        faq("Can I day-trip the forest from a Paris hotel?", "You can, and you will get about two hours on a trail plus the train. Sleep in Fontainebleau if the forest is the reason you came."),
        faq("Is the Bois de Boulogne enough?", "For a lake and a picnic, yes. For the quiet people mean by a nature view, no. It is a park with ring roads."),
        faq("Does Hôtel Napoléon have a private pool?", "No. It has a shared indoor spa pool, booked by the hour, for an extra fee. The forest is the amenity."),
    ],
    map_places=[
        stop("Palace of Fontainebleau", "Fontainebleau", "France", "Palace of Fontainebleau"),
        stop("Forest of Fontainebleau", "Fontainebleau", "France", "Forest of Fontainebleau"),
        stop("Barbizon", "Barbizon", "France", "Barbizon"),
        stop("Bois de Boulogne", "Paris", "France", "Bois de Boulogne"),
        stop("Bois de Vincennes", "Paris", "France", "Bois de Vincennes"),
        stop("Gare de Lyon", "Paris", "France", ""),
    ],
    budget_notes="A Fontainebleau room at the Napoléon or Aigle Noir is often $180–360. Molitor is a 16th-arrondissement five-star and prices like one, $350–650, for a different trip. The château ticket is about $15. Taxis to trailheads add up if you take them twice a day; one out-and-back is the budget. Picnics keep food near $25 a person on the forest day.",
))


add(trip(
    slug="paris-near-the-beach-under-300",
    title="The beach Parisians use: three nights in Deauville",
    location="Deauville, France",
    summary=(
        "Paris is inland. The coast its residents actually take the train to is Deauville–Trouville, about two hours from Saint-Lazare, and that is where this trip sleeps. "
        "Under $300 is realistic at the Mercure and the two ibis hotels for much of the year. August, sunny weekends, and the American Film Festival push even those rates over the cap. "
        "Hôtel Barrière Le Normandy is the famous boardwalk hotel, and it is usually well over $300, so it is not one of the beds."
    ),
    who="People who searched for a Paris beach and are willing to stay on the Channel instead of the Seine.",
    best_time="June and September, when the beach is open and the town is not in August form. Early September is the American Film Festival, which fills the hotels. Winter is a boardwalk walk.",
    nights=3,
    hook="3 nights · Deauville, train from Paris · $130–260/night",
    constraints=["On the coast", "Under $300 when the calendar allows", "A Paris train, not a Paris hotel"],
    lodging="$130–260",
    daily="$210–380",
    neighborhoods=[
        stay_area("Deauville center", "The Mercure and both ibis hotels are in town, a 10-minute walk from the Planches or the marina. You do not need a sea-view room to be at the beach after breakfast."),
        stay_area("Trouville, across the Touques", "The older town, the fish market, and the better ordinary dinner. Sleep in Deauville, eat over the bridge."),
    ],
    hotels=[
        hotel("Mercure Deauville Centre", "Rue Breney", "An Anglo-Norman building in the center, about 700 meters from the Planches and 400 meters from the station. The right 'nice enough' room when Le Normandy is out of the budget. Summer weekends can still clear $300.", "$150–280", "Deauville"),
        hotel("ibis Deauville Centre", "Quai de la Marine", "On the marina, about 200 meters from the station and a 10-minute walk to the sand. Duplex family rooms exist if you need a sofa. This is the practical bed, and the harbor view is of boats, not open ocean.", "$110–210", "Deauville"),
        hotel("ibis Styles Deauville Centre", "Rue Robert Fossorier", "About 300 meters from the beach and the casino, with breakfast included. The design is horse-racing kitsch and the location is the point. The rate that most often stays under $300, until August weekends.", "$130–240", "Deauville"),
    ],
    itinerary=[
        day(1, "Saint-Lazare to the Planches", "Leave Paris on purpose. The beach is the destination.", "Train from Paris Saint-Lazare to Trouville-Deauville, about two hours. Walk to the hotel, drop bags, and go straight to the Planches, the boardwalk with the named bathing huts.", "The beach is wide and sandy. The water is the Channel, which means cold outside high summer. Walk west until the umbrellas thin out. The casino end is the postcard; the far end is the swim.", "Cross the Pont des Belges into Trouville for dinner. The quay, not the casino. Les Vapeurs for mussels if you want the room everyone knows.", "Le Normandy is on this boardwalk and it is not your hotel. Walk past it.", "Deauville"),
        day(2, "A real beach day, then the fish town", "Sand in the morning, Trouville when you are tired of the wind.", "Be on the beach before the day-trippers from Paris feel thick. Swim if you meant to. Otherwise walk the full front. The light is better before lunch.", "Trouville's fish market if it is open, then the streets behind the front, which are a working town rather than a resort brochure. The market is the lunch: grilled fish, eaten simply.", "A booked seafood dinner. A plateau de fruits de mer only if two people are sharing it. One sole each is the saner order. Back across the bridge.", "Wind is the weather here, even in July. A jacket for the evening quay.", "Trouville-sur-Mer"),
        day(3, "Honfleur or the train", "One extra town, or a clean departure. Not a two-hour Louvre.", "Honfleur by bus, about half an hour, if you want the old harbor. Walk the Vieux Bassin, look at the slate houses, and leave. A taxi is the backup if the bus times are rude.", "Back to Deauville for a last hour on the sand if the train allows. Buy camembert for the ride, from a shop, ripe enough to smell.", "Train to Saint-Lazare. A Paris evening can be added before a flight the next day. Do not schedule the Musée d'Orsay between the beach and a departure.", "August weekends and film-festival dates sell out of the cheap rooms first. If your return is a Sunday, book the train when you book the hotel.", "Honfleur"),
    ],
    attractions=[
        sight("Les Planches", "Deauville's boardwalk, with the named beach huts and the flags.", "Walk it once for the architecture of the resort, then get down on the sand.", ""),
        sight("Deauville beach", "A wide sandy Channel beach, which is the whole reason to leave Paris.", "The water is cold. The far end of the beach is quieter than the casino end.", ""),
        sight("Trouville-sur-Mer", "The fishing town across the river, older than the resort.", "Dinner here. The front is the walk; the back streets are the town.", "Trouville-sur-Mer"),
        sight("Trouville fish market", "The morning market that makes day 2 a place rather than a sunbed.", "Go to eat, not to photograph the stalls and leave.", ""),
        sight("Honfleur", "The harbor town half an hour along the coast, for one morning.", "The Vieux Bassin, then the bus back. It is not a second base.", "Honfleur"),
        sight("Deauville-La Touques racecourse", "The track at the edge of town. Races run much of the year.", "Check the card. On a big Sunday the town is full and the hotels know it.", ""),
    ],
    scenic_routes=[
        route("The Planches", "From the casino end of the boardwalk along the named huts to the quieter sand.", "About 2 km, 40 minutes"),
        route("Across to Trouville", "Pont des Belges, the Trouville quay, and the streets behind the fish market.", "About 3 km, 1 hour"),
        route("Paris to the coast", "Saint-Lazare to Trouville-Deauville, direct. Sit on the left or the right; the arrival is the point.", "About 2 hours"),
    ],
    transport="Train from Paris Saint-Lazare to Trouville-Deauville. Walk from the station to all three hotels. Trouville is a bridge away. Honfleur is a bus of about 30 minutes or a taxi. A car is for Cabourg, the farther beaches, or a pile of luggage, not for this three-night version.",
    food=[
        dish("Moules-frites", "Les Vapeurs, Trouville quay", "The brasserie everyone means. Book in August. Mussels and fries, not a tour of the menu."),
        dish("Grilled fish", "Trouville market, lunchtime", "Buy it and eat it while you are there. A sole or whatever was landed. This beats a resort restaurant at 1 p.m."),
        dish("Camembert", "A fromager in Deauville or the Trouville market", "Pays d'Auge cheese, ripe. Eat it with a baguette on a bench, not as a sad supermarket wedge."),
        dish("Tarte aux pommes", "A bakery on the way back to the hotel", "Apple tart, then a calvados after dinner if you want the regional closer. One glass."),
    ],
    tips=[
        "The Channel is a decision in June and a pleasure in August. Pack for wind either way.",
        "Le Normandy and Le Royal will break a $300 cap on an ordinary summer week. Walk to the beach from the Mercure or an ibis.",
        "Deauville is sand. Do not arrive with Brighton expectations of pebbles, and do not arrive expecting Biarritz.",
        "Race Sundays and the early-September film festival are when 'under $300' quietly stops being true. Check the calendar before you celebrate a rate.",
    ],
    faqs=[
        faq("Is this a Paris trip?", "It is the beach trip that starts and ends at Saint-Lazare. You do not sleep in Paris. Add a Paris night before or after if you need the city."),
        faq("Can I stay under $300?", "Often, at these three, outside August weekends and the film festival. A sea-view room at the Barrière hotels is a different budget."),
        faq("Do I need a car?", "No for Deauville, Trouville, and the train. A car helps for Honfleur only if the bus times are wrong for your departure."),
        faq("Which side of the river?", "Sleep in Deauville, near the station and the Planches. Eat in Trouville. The resort is the beach; the port is the dinner."),
    ],
    map_places=[
        stop("Les Planches", "Deauville", "France", ""),
        stop("Deauville beach", "Deauville", "France", ""),
        stop("Trouville-sur-Mer", "Trouville-sur-Mer", "France", "Trouville-sur-Mer"),
        stop("Honfleur", "Honfleur", "France", "Honfleur"),
        stop("Trouville-Deauville station", "Deauville", "France", ""),
        stop("Deauville-La Touques racecourse", "Deauville", "France", ""),
    ],
    budget_notes="Off-peak, the ibis and the Mercure often land at $130–260, breakfast included at the ibis Styles. August weekends and the American Film Festival can push a ordinary double through $300, which is why the cap is 'where possible.' A seafood dinner is $40–70 a person. The beach is free. Le Normandy is the hotel you walk past, not the one you book, on this budget.",
))


add(trip(
    slug="paris-with-private-pool",
    title="A private pool in Paris: the honest answer is a shared one",
    location="Paris, France",
    summary=(
        "In-room private pools basically do not exist in central Paris, and this page will not invent a villa to paper over that. "
        "Hôtel de Crillon, Peninsula Paris, and Le Royal Monceau each have a beautiful hotel pool, and every one of them is shared with other guests. "
        "Stay in one if you want a real swim between museum mornings. A house in the countryside is the private-pool trip, and it is not inside the boulevards."
    ),
    who="People who asked for a private pool and deserve a straight answer before they wire a deposit.",
    best_time="Any season. All three pools are indoors. Weekday mornings are the quiet water. August is easier to reserve and duller in the dining rooms around them.",
    nights=3,
    hook="3 nights · A shared palace pool · $800–1,600/night",
    constraints=["No fake private pool", "One palace hotel", "A swim, then the city"],
    lodging="$800–1,600",
    daily="$980–1,900",
    neighborhoods=[
        stay_area("Place de la Concorde", "Crillon's door is the square. The Tuileries start across the traffic. This is the most central of the three pools."),
        stay_area("Étoile and Parc Monceau", "Peninsula is on avenue Kléber, a walk from the Trocadéro. Royal Monceau is on avenue Hoche, next to Parc Monceau. Both are the 16th/8th version of quiet."),
    ],
    hotels=[
        hotel("Hôtel de Crillon", "Place de la Concorde", "A palace on the square. Sense, the spa, has a heated indoor pool of about 14 meters in pale stone. Hotel guests can swim from early morning; outside spa guests use it later in the day. It is shared. It is not in the suite.", "$900–1,800", "Paris"),
        hotel("Peninsula Paris", "Avenue Kléber, 16th", "The indoor pool, under a glass roof, is one of the best swims in the city and it is shared with other guests. You are a short walk from the Palais de Chaillot and the river. Ask whether pool access is included before you count it as free.", "$800–1,700", "Paris"),
        hotel("Le Royal Monceau Raffles Paris", "Avenue Hoche, 8th", "The Starck pool is a set piece, and it is a shared guest pool, not a pool in the room. Parc Monceau is the morning walk. The 8th is calm and it is not the Marais; plan the days around the park and one taxi to a museum.", "$800–1,600", "Paris"),
    ],
    itinerary=[
        day(1, "See the pool you actually bought", "One hotel for the stay. You do not tour three spas.", "Check in and swim before you do anything else, so the shared pool is a fact and not a brochure. At Crillon the guest hours start early. At the other two, use the afternoon window the spa gives you.", "Then the walk that belongs to the hotel. Crillon: the Tuileries until they feel like a park and not a corridor. Peninsula: Palais de Chaillot and the view of the tower from across the river, without climbing it. Royal Monceau: Parc Monceau before the gates close.", "Dinner outside the hotel. One palace meal in three nights is a choice; three of them will double the trip. A bistro near Madeleine, in the 16th, or off Parc Monceau.", "Ask at booking whether the pool is included, billed as spa entry, or reserved by the hour. A photo of water is not an access policy.", "Place de la Concorde"),
        day(2, "One museum, then back to the water", "The same rule as a normal Paris trip: one ticket.", "Musée d'Orsay if you want a building you can finish, or the Louvre's Denon wing if you want the palace. Timed entry, morning, out within two and a half hours. Take a taxi back. This is not the day you also do the Marais.", "The pool when it is calmer than a Saturday at noon. These are short hotel pools. Crillon's is about 14 meters. You are floating, not training. Then a book, or the Tuileries again if you are at Crillon.", "A simple dinner. Angelina on rue de Rivoli is the hot chocolate if you are near Concorde and you go at opening or late, not at 3 p.m. It is not dinner.", "Orsay is closed Monday. The Louvre is closed Tuesday. Pick the morning that is actually open.", "Musée d'Orsay"),
        day(3, "An early swim, then leave", "Do not add Versailles to a checkout day.", "Swim if the pool opens early. Crillon's pool has been opening for hotel guests around 6:30 a.m. Confirm the night before. Peninsula and Royal Monceau: use whatever morning slot the spa still honors on departure day.", "A last walk with no new neighborhood. Concorde to the Louvre courtyard and back, or Parc Monceau once more, or the Trocadéro terrace. Then the airport.", "CDG and Orly from these hotels are a taxi or the RER from a nearby station. Eat a jambon-beurre from a bakery so the last meal is not a $90 club sandwich.", "A buyout of the pool, if you inquire, is an event contract. It is not included in the room.", "Tuileries Garden"),
    ],
    attractions=[
        sight("Place de la Concorde", "The square outside Crillon, which is the view the address is selling.", "Cross it carefully. The Tuileries gate is the walk.", "Place de la Concorde"),
        sight("Tuileries Garden", "The park between Concorde and the Louvre.", "Chairs by the fountains, not a march to the pyramid unless you are going in.", "Tuileries Garden"),
        sight("Palais de Chaillot", "The terrace across the river from the Eiffel Tower.", "The view is the visit. The tower ticket is a different trip.", "Palais de Chaillot"),
        sight("Parc Monceau", "The 8th-arrondissement park next to Royal Monceau.", "A morning loop. The gates close in the evening.", "Parc Monceau"),
        sight("Musée d'Orsay", "The one museum that fits a three-night pool stay.", "Morning, timed, then back to the hotel. Closed Mondays.", "Musée d'Orsay"),
        sight("Arc de Triomphe", "A short walk from the Peninsula if you want one monument.", "The roof is optional and it is a queue. The avenue itself is the evening walk.", "Arc de Triomphe"),
    ],
    scenic_routes=[
        route("Concorde and the Tuileries", "From Crillon's door through the Tuileries to the Louvre courtyard and back by rue de Rivoli.", "About 3 km, 90 minutes"),
        route("Kléber to the river", "Peninsula to the Palais de Chaillot terrace, down to the Pont d'Iéna, and back. The tower stays where it is.", "About 2.5 km, 1 hour"),
        route("Parc Monceau loop", "From avenue Hoche around the colonnade and the pond.", "About 2 km, 40 minutes"),
    ],
    transport="Taxis are part of this budget. Use one to the museum and one to the airport. The walks above are the point of the neighborhood you picked. The metro still works if you would rather not sit in traffic on the way to Orsay.",
    food=[
        dish("Chocolat chaud", "Angelina, rue de Rivoli", "Go at opening. The afternoon line is the story people tell afterward, and it is not a good story."),
        dish("Steak tartare", "A booked bistro near Madeleine or in the 8th", "Dinner outside the hotel on night one. Frites, not a tasting menu."),
        dish("Jambon-beurre", "A bakery, eaten in the Tuileries or Parc Monceau", "One cheap lunch keeps the palace from eating the whole budget."),
        dish("Breakfast", "The hotel once, a bakery after that", "The palace croissant is not automatically better. Pay for it on the morning you will sit still."),
    ],
    tips=[
        "These pools are short and shared. Crillon's is about 14 meters. You are floating, not training for a race.",
        "Get the access rule in writing: included, spa fee, or timed slot. Do not discover it in a robe.",
        "A listing that says 'private pool' in central Paris is usually a hotel pool with a hire hour, or a picture of someone else's courtyard.",
        "Molitor, by the Bois de Boulogne, is another famous shared pool and it is not a private one either. It sits on the nature page because of the park.",
    ],
    faqs=[
        faq("Is there a central hotel with a pool in the room?", "Not among established hotels I would book. Treat a suite 'plunge pool' as unverified until you have the current floor plan, and assume it is a bathtub with a view."),
        faq("Can we book the pool just for us?", "Some of these spas hire the water for events. That is a buyout with a price to match. It is not a feature of the room."),
        faq("Which pool is the real swim?", "All three are shared. Crillon is the most central. Peninsula is the one people mean when they say the pool is worth the hotel. Royal Monceau is the design piece next to a quiet park."),
        faq("What if it has to be private?", "Leave the arrondissements. A rented house in the Île-de-France or on the Normandy coast is the honest next step. I am not naming a villa from a listing photo."),
    ],
    map_places=[
        stop("Place de la Concorde", "Paris", "France", "Place de la Concorde"),
        stop("Tuileries Garden", "Paris", "France", "Tuileries Garden"),
        stop("Palais de Chaillot", "Paris", "France", "Palais de Chaillot"),
        stop("Parc Monceau", "Paris", "France", "Parc Monceau"),
        stop("Musée d'Orsay", "Paris", "France", "Musée d'Orsay"),
        stop("Arc de Triomphe", "Paris", "France", "Arc de Triomphe"),
    ],
    budget_notes="These are palace rates: $800–1,600 a night is the band, and a park-facing or square-facing suite goes higher. A hotel dinner is $150-plus a person, which is why two of the three dinners should be a bistro or a bakery. The pool may be included or it may be a spa charge. Ask. The museum is about $25. The privacy you originally wanted is not for sale in these buildings.",
))


add(trip(
    slug="london-budget-under-200night",
    title="London under $200 a night: three Premier Inns, and the weeks they fail",
    location="London, United Kingdom",
    summary=(
        "$200 a night buys a real Premier Inn room in the center on a weeknight in the shoulder season, and it is a wish in June, July, and on Saturdays. "
        "County Hall and Leicester Square are the branches people want, and both clear $200 when the city is full. "
        "King's Cross is the full-size Premier Inn that still sometimes holds the cap. This plan spends money on almost nothing except the bed and one paid ticket."
    ),
    who="Two people who want to be central, sleep properly, and not pretend a hostel dorm is a hotel.",
    best_time="November through March if the rate is the point. A Tuesday is cheaper than a Saturday in every month. June through August at County Hall is often a different budget.",
    nights=4,
    hook="4 nights · Central Premier Inns · $150–240/night",
    constraints=["Central-ish chain hotel", "Under $200 when the date allows", "Free museums and walks"],
    lodging="$150–240",
    daily="$210–320",
    neighborhoods=[
        stay_area("South Bank and the Square", "County Hall puts Westminster Bridge outside. Leicester Square puts you in the noise. Both are the center, and both price like it in summer."),
        stay_area("King's Cross", "The full-size Premier Inn by the station, not a tiny Hub room. Bloomsbury and the British Museum are a walk. This is the branch that fits the cap most often."),
    ],
    hotels=[
        hotel("Premier Inn London County Hall", "Belvedere Road, South Bank", "The postcard Premier Inn, next to Westminster Bridge. The room is the standard Premier Inn room, clean and generic. The location is why it sells out of the budget first. Summer and Saturdays often clear $200.", "$170–280", "London"),
        hotel("Premier Inn London Leicester Square", "Swiss Court", "A few steps from the square, which means theaters, Chinatown, and noise. Ask for a higher floor away from the square. Same summer warning as County Hall. Earplugs are a packing item, not a joke.", "$170–280", "London"),
        hotel("Premier Inn London King's Cross", "King's Cross", "The full-size King's Cross Premier Inn, not the Hub capsules nearby. A walk to the British Museum through Bloomsbury. The branch that most often still lands near $200 on a weeknight.", "$140–230", "London"),
    ],
    itinerary=[
        day(1, "The river, which is free", "Arrive and spend nothing except the bed and a pint.", "If you are at County Hall, walk out and along the South Bank toward the Tate Modern chimney. Do not go in unless you want to. Westminster Bridge at dusk is the picture.", "If you are at King's Cross or Leicester Square, one Tube to Westminster and the same walk. St James's Park if you would rather have grass than skateboarders. Stop before you feel obliged to buy a London Eye ticket.", "A pub dinner near the hotel. The George Inn, off Borough High Street, is the galleried old one if you are on the South Bank side. Eat at 6:30. The West End pre-theatre markup starts at 7.", "The London Eye, a river cruise, and the Tower are the paid traps of day one. Skip all three.", "River Thames"),
        day(2, "The British Museum, then get out", "Free entry. The building is the risk, because it is too big.", "Be there at opening. The Egyptian sculpture gallery and the Rosetta Stone, then one upstairs room you actually care about. Leave before noon. From King's Cross this is a 20-minute walk. From the other two hotels it is one Tube.", "Bloomsbury's squares to Covent Garden on foot. Look at the market, do not start shopping. Covent Garden is a through-route, not a destination.", "Chinatown if you are at Leicester Square: a roast-meat rice at 5:30, before the theater crowd. Otherwise the same pub logic as last night, in a different pub.", "The National Gallery is the free backup if the British Museum feels like a school trip. Do not do both.", "British Museum"),
        day(3, "Parks and the one paid door", "Westminster from the outside, unless you have chosen your one ticket.", "St James's Park from Trafalgar Square to the palace gates. Pelicans, the lake, Buckingham Palace from the mall. Free. The palace tour is not the budget version.", "Westminster Abbey if it is your one paid sight, booked for the afternoon, about the price of a serious dinner. If it is not, walk the bridge, look at Parliament, and keep the money. The Tower of London is the other paid option and it takes half a day. Pick one or neither.", "Borough Market is mostly shut by evening. Dinner is a Borough pub, not a second lunch at the market. If this day is a Saturday, Maltby Street is the alternative food street.", "Abbey tickets are timed. The outside is the plan if you did not buy one.", "Westminster Abbey"),
        day(4, "A market or a train", "Leave on a cheap breakfast, not a new neighborhood.", "Sunday: Brick Lane and a salt-beef bagel at Beigel Bake, early, if you want one cheap famous thing. Any other morning: Borough Market when it opens, one sandwich, then the station.", "If there is no market, a last hour on the South Bank and the train. King's Cross and St Pancras are the useful stations if you slept there. Waterloo and Charing Cross serve the other two hotels.", "Do not add a show on departure day because the tickets looked cheap at noon. Eat before the platform.", "Contactless on the Tube has a daily cap. Do not buy a paper Travelcard for four rides.", "Borough Market"),
    ],
    attractions=[
        sight("British Museum", "The one free museum morning.", "Egyptian sculpture, then out. The whole building is a week.", "British Museum"),
        sight("River Thames", "The South Bank walk, which costs nothing.", "Westminster to the Tate Modern chimney and back.", "River Thames"),
        sight("St James's Park", "The green walk from Trafalgar Square to the palace.", "Morning, before the mall is a procession of tours.", "St James's Park"),
        sight("Westminster Abbey", "The one building worth paying for, if you pay for anything.", "A timed ticket, or the outside from Parliament Square.", "Westminster Abbey"),
        sight("Borough Market", "Lunch, not a lifestyle.", "One thing to eat. The rest of the stalls are how $40 disappears.", "Borough Market"),
        sight("National Gallery", "The free alternate to the British Museum.", "One wing. Trafalgar Square is the front door.", "National Gallery"),
        sight("Covent Garden", "A through-walk, useful because two of the hotels are near it.", "Pass the piazza. Do not sit down for a show you did not plan.", "Covent Garden"),
    ],
    scenic_routes=[
        route("South Bank", "Westminster Bridge to the Tate Modern, along the river, and back if your hotel is County Hall.", "About 3 km, 1 hour"),
        route("St James's Park", "Trafalgar Square, the lake, Buckingham Palace gates.", "About 2.5 km, 45 minutes"),
        route("Bloomsbury to Covent Garden", "From the British Museum through the squares to the piazza.", "About 2 km, 40 minutes"),
    ],
    transport="Walk, plus one or two Tube rides a day. Contactless bank card, daily cap, no paper pass. King's Cross walks to the museum. County Hall walks to the river. Leicester Square walks to almost everything and sleeps badly if you face the square. Heathrow is the Elizabeth line. Gatwick is a train from a main station, not a taxi.",
    food=[
        dish("Pie and a pint", "The George Inn, Borough High Street", "The galleried coaching inn. A pie is dinner. You do not need a starter in a room this old."),
        dish("Salt beef bagel", "Beigel Bake, Brick Lane", "Early or late. Mustard. The Sunday morning version of a cheap landmark."),
        dish("One market sandwich", "Borough Market", "Roast pork or a grilled cheese, then leave. Three stalls is a $30 accident."),
        dish("Roast meat and rice", "Chinatown, near Leicester Square", "Order at 5:30. Duck or char siu. The 8 p.m. pre-theatre room is the same food with a wait."),
    ],
    tips=[
        "$200 is about £155. County Hall and Leicester Square are often above that from June through August and on Friday and Saturday. King's Cross is the first place to look.",
        "Premier Inn rooms fit a suitcase. They do not fit two large suitcases fully open. Travel lighter than a palace trip.",
        "The British Museum and the National Gallery are free. The Tower and the Abbey are not. One paid door for the whole trip.",
        "Leicester Square is loud until late. Ask for a room off the square, and mean it.",
    ],
    faqs=[
        faq("Can I really sleep in the center under $200?", "On a Tuesday in November, often. On a Saturday in July, not at County Hall or Leicester Square. Check King's Cross first."),
        faq("Are these rooms boring?", "Yes. That is the product. You are paying for a clean bed and an address, not a story about the wallpaper."),
        faq("Is Leicester Square a mistake?", "For getting around, no. For sleeping, only if the room faces the square. Earplugs help. A courtyard request helps more."),
        faq("What should I skip?", "The Eye, a Thames cruise, and any walking tour that ends in a shop. The South Bank is the same walk and it is free."),
    ],
    map_places=[
        stop("British Museum", "London", "United Kingdom", "British Museum"),
        stop("Borough Market", "London", "United Kingdom", "Borough Market"),
        stop("Westminster Abbey", "London", "United Kingdom", "Westminster Abbey"),
        stop("St James's Park", "London", "United Kingdom", "St James's Park"),
        stop("Trafalgar Square", "London", "United Kingdom", "Trafalgar Square"),
        stop("King's Cross station", "London", "United Kingdom", ""),
    ],
    budget_notes="Budget $150–240 for the room and assume the top of that range is County Hall in a busy month, which can also jump past $280. Food can stay at $40–60 a day on pub meals, a market lunch, and a Chinatown plate. The British Museum is free. If you buy the Abbey or the Tower, add $30–40 that day and do not also eat a 'nice dinner.'",
))


add(trip(
    slug="london-family-friendly-with-kitchen",
    title="London with a kitchen: two real bedrooms, not a sofa bed",
    location="London, United Kingdom",
    summary=(
        "A family stay in London works when the apartment has two bedrooms with doors and a kitchen you will actually cook in. "
        "Citadines Trafalgar Square has a small number of two-bedroom duplexes on Northumberland Avenue. SACO Holborn, on Lamb's Conduit Street, is the practical Bloomsbury version. "
        "Cheval Three Quays, by the Tower, is the Thames apartment, and it will not pretend to be a normal family rate."
    ),
    who="Parents with children who have done the hotel-room version and do not want to do it again.",
    best_time="Late May or September, when the museums are open and the school-holiday premium is not the whole story. Kitchens matter more in winter, when a picnic is a bad plan.",
    nights=4,
    hook="4 nights · Two bedrooms and a kitchen · $300–650/night",
    constraints=["Two bedrooms with doors", "A real kitchen", "One museum a day"],
    lodging="$300–650",
    daily="$380–760",
    neighborhoods=[
        stay_area("Bloomsbury", "SACO Holborn is the base the days assume. The British Museum is a 15-minute walk. Russell Square and Coram's Fields are the outdoor hours."),
        stay_area("Trafalgar Square or the Tower", "Citadines puts you on Northumberland Avenue, useful and busy. Cheval Three Quays puts you on the Thames by Tower Bridge, which is the splurge."),
    ],
    hotels=[
        hotel("SACO Holborn", "Lamb's Conduit Street, Bloomsbury", "Serviced apartments in Spens House, including real two-bedrooms around 47 to 60 square meters, most with two bathrooms, an oven, a dishwasher, and a washing machine. Some have a roof terrace. This is the family booking.", "$280–480", "London"),
        hotel("Citadines Trafalgar Square", "Northumberland Avenue", "An aparthotel with studios, one-bedrooms, and a limited run of two-bedroom duplexes, on the order of a dozen. Living space downstairs, bedrooms up a stair. Book the duplex by name. A sofa bed is how some listings get to six sleepers.", "$350–600", "London"),
        hotel("Cheval Three Quays", "Lower Thames Street", "Serviced apartments beside Tower Bridge, with real two-bedroom units and a full kitchen. Some look at the river. This is the one that blows a family budget and earns the address. Confirm the floor plan so you are not in a one-bedroom with a view.", "$500–900", "London"),
    ],
    itinerary=[
        day(1, "Groceries, then the square", "The days assume SACO Holborn. The other addresses are noted where the walk changes.", "Check in and walk to the Waitrose at the Brunswick Centre before you walk to a museum. Buy pasta, fruit, milk, and breakfast for tomorrow. Coram's Fields is the garden nearby, and adults are admitted only with a child.", "Russell Square if the Fields are enough. Let the children run. Trafalgar guests can use St James's Park for this hour. Cheval guests can walk the river path to Tower Bridge and stop.", "Cook. The first restaurant night with tired children is the expensive way to learn the Tube map.", "Citadines duplexes have an internal stair. Ask before you arrive with a stroller you planned to park inside the apartment.", "Russell Square"),
        day(2, "The British Museum, briefly", "Ninety minutes, then home for lunch. That is a successful museum day.", "Opening time. The Egyptian gallery, the mummies if that is the child's request, and out. The Great Court is the meeting point if someone wanders. From Lamb's Conduit Street the walk is about 15 minutes.", "Back to the apartment. Lunch you bought yesterday. Quiet hour. Then a playground, not a second museum. Coram's Fields again, or a bus toward Hyde Park if everyone still has legs. The Diana Memorial Playground in Kensington Gardens is the farther version and it queues on weekends.", "Pizza one night only. A neighborhood oven, or the walk toward a Covent Garden Franco Manca if you want a known name. Eat early. Bedtime is the amenity.", "Do not add the Natural History Museum to this day. It is a separate morning in South Kensington.", "British Museum"),
        day(3, "The river, with a return plan", "Out for the morning, home before anyone melts.", "Tube to Tower Hill. The Tower of London if you bought tickets and the children are old enough to last. If you did not, the outside, Tower Bridge, and a walk west along the river is the free version. Cheval guests skip the Tube and start at the door.", "Borough Market for one shared snack if it is open, then the Tube home. Lunch in the apartment. The afternoon is laundry, the washing machine, and a park. This is why you rented a kitchen.", "Cook again. A roast chicken from a supermarket is a better family dinner than a 7:30 table in Soho.", "The London Eye is a queue and a fare. The river walk is the same water.", "Tower of London"),
        day(4, "A park, then the train", "A park in the morning and the train after. No new ticket.", "From Holborn, Hyde Park and the Diana playground if you did not go yesterday, or a last hour in Russell Square if the bags are already by the door. From Trafalgar, St James's Park is the easy one. From the Tower, the river path one last time.", "Elizabeth line from Farringdon or Tottenham Court Road if you are going to Heathrow and you slept in Holborn. Give a Cheval checkout extra time; Lower Thames Street is not next to that line. Eat the food left in the fridge.", "Airport. A restaurant meal on the way is how you miss the train.", "Check-out at apartments is often 10 or 11. Ask the night before and book the late bag drop if you have an evening flight.", "Hyde Park, London"),
    ],
    attractions=[
        sight("British Museum", "The one museum that is walkable from the Bloomsbury apartment.", "Ninety minutes at opening. Egyptian rooms, then leave.", "British Museum"),
        sight("Coram's Fields", "The children's garden near Lamb's Conduit Street.", "Adults go in only with a child. That is the rule, and it is why the place works.", ""),
        sight("Russell Square", "The outdoor hour that does not require a plan.", "A lawn between the apartment and the museum.", "Russell Square"),
        sight("Tower of London", "The one paid morning, if you buy it.", "Tickets timed. The outside and the bridge are the free substitute.", "Tower of London"),
        sight("Borough Market", "A snack on the river day, not a second destination.", "One thing to share. Then the Tube home.", "Borough Market"),
        sight("Hyde Park, London", "The larger park for the last morning, with the Diana playground on the Kensington Gardens side.", "Go early on a weekend. The playground can queue.", "Hyde Park, London"),
        sight("Tower Bridge", "The walk outside Cheval, and the photo that does not need a ticket.", "Cross it and come back. The exhibition inside is optional.", "Tower Bridge"),
    ],
    scenic_routes=[
        route("Holborn to the museum", "Lamb's Conduit Street, Great Ormond Street, Russell Square, the British Museum door.", "About 1.2 km, 15 minutes"),
        route("Tower Bridge to the Tate ramp", "A flat river walk west from the bridge, good with a stroller, turning around when legs fade.", "About 3 km, 70 minutes"),
        route("Hyde Park to the playground", "Marble Arch or Lancaster Gate to the Serpentine and the Diana Memorial Playground.", "About 3 km, 1 hour"),
    ],
    transport="Walk from SACO to the museum. Tube for the Tower day. Contactless cards for adults; children under 11 travel free on the Tube with an adult, which is worth using. Heathrow is the Elizabeth line from Farringdon. Do not rent a car.",
    food=[
        dish("Pasta at the apartment", "Waitrose, Brunswick Centre", "The first and third nights. Sauce, pasta, fruit. This is the budget tool."),
        dish("One Borough Market snack", "Borough Market", "A sausage roll or a grilled cheese to share. Not a grazing tour with hungry children."),
        dish("Pizza, once", "A neighborhood oven, or Franco Manca toward Covent Garden", "Early seating. One night out is the rule, or the kitchen was pointless."),
        dish("Caff breakfast", "A café near Holborn or Lamb's Conduit Street", "Once, a bacon sandwich. The other mornings are cereal you bought."),
    ],
    tips=[
        "Say 'two-bedroom duplex' at Citadines and 'two-bedroom' at SACO and Cheval. A one-bedroom with a sofa bed will come back as available and it is the wrong booking.",
        "Cheval over $600 is a view. SACO is the same holiday. Pick before you fall for the river photo.",
        "Confirm the washing machine at SACO if you are traveling with small children. Most two-beds have one.",
        "One museum a day. The British Museum plus the Tower plus the Eye is a taxi at 3 p.m. and a ruined dinner.",
    ],
    faqs=[
        faq("Are these actually two bedrooms?", "Yes, if you book the right category. Citadines has few duplexes and they go first. SACO Holborn and Cheval Three Quays both have proper two-bedroom stock. Read the floor plan."),
        faq("Can we cook every night?", "Yes, and you should cook at least two. A family table in central London is $80–150 before anyone has enjoyed it."),
        faq("Which address is easiest with small children?", "SACO Holborn. The museum is a short walk, the squares are outside, and you are not on a nightclub street."),
        faq("Is there a pool?", "No. This is a kitchen trip. A shared hotel pool is a different page, and it is not a backyard."),
    ],
    map_places=[
        stop("British Museum", "London", "United Kingdom", "British Museum"),
        stop("Russell Square", "London", "United Kingdom", "Russell Square"),
        stop("Tower of London", "London", "United Kingdom", "Tower of London"),
        stop("Borough Market", "London", "United Kingdom", "Borough Market"),
        stop("Hyde Park", "London", "United Kingdom", "Hyde Park, London"),
        stop("Tower Bridge", "London", "United Kingdom", "Tower Bridge"),
    ],
    budget_notes="The two-bedroom is the cost: about $300–480 at SACO, often $350–600 for a Citadines duplex, and $500–900 at Cheval when you are paying for the river. Groceries cut food to $40–70 a day for a family if you cook twice. The British Museum is free. The Tower is the optional $40-class ticket. Budget the washing powder; the machine is the reason the apartment beats a hotel on day three.",
))


add(trip(
    slug="london-luxury-with-ocean-view",
    title="London luxury without an ocean: the river, the park, or Mayfair",
    location="London, United Kingdom",
    summary=(
        "No London hotel has an ocean view. The Thames is a river, and a river suite is barges, the South Bank, and brown water, which can be wonderful and is not the Atlantic. "
        "Book The Savoy if you want that water from the room, and ask for a river-facing room in writing. Book Four Seasons London at Park Lane if you want Hyde Park. "
        "Book Claridge's if you want Mayfair and no water at all. The sea is the Brighton trip, an hour south."
    ),
    who="Travelers who searched for an ocean-view suite and should hear the geography before they pay for the wrong window.",
    best_time="May, June, and September, when the park is worth crossing. The hotels cost the same in January. The river looks better at dusk in any month.",
    nights=3,
    hook="3 nights · River or park, never the ocean · $800–1,600/night",
    constraints=["No invented ocean view", "One grand hotel", "A walk at dusk"],
    lodging="$800–1,600",
    daily="$950–1,900",
    neighborhoods=[
        stay_area("The Strand and the Embankment", "The Savoy is the only one of the three with a real river room. The walk is the Victoria Embankment, not a beach."),
        stay_area("Mayfair and Park Lane", "Four Seasons faces Hyde Park. Claridge's faces Brook Street. Both are a taxi from the water, which is the correct relationship."),
    ],
    hotels=[
        hotel("The Savoy", "Strand", "The river hotel. A river-facing room looks at the Thames and the South Bank. A Strand room looks at traffic. Those are different purchases. Email the words 'river-facing' and keep the reply. The Embankment walk starts at the door.", "$800–1,800", "London", "https://www.thesavoy.com/"),
        hotel("Four Seasons Hotel London at Park Lane", "Park Lane", "A grand hotel on the park, with Hyde Park as the view. It does not face the river and it does not face the sea. Book it for the park and for Mayfair, and take a taxi when you want the Embankment.", "$900–1,800", "London", "https://www.fourseasons.com/london/"),
        hotel("Claridge's", "Brook Street, Mayfair", "The Mayfair hotel. The windows look at the neighborhood, not at water of any kind. Afternoon tea is a separate reservation and it sells out. The evening dress code is real enough that you should not arrive in train clothes.", "$900–1,800", "London", "https://www.claridges.co.uk/"),
    ],
    itinerary=[
        day(1, "The water you actually get", "The Thames at dusk, from a room or from the pavement.", "Check in. If you are at The Savoy, confirm the room faces the river before you unpack. If it does not, ask to move while the desk still has options. Park Lane and Claridge's guests should not expect this conversation to produce water.", "Walk the Victoria Embankment from the Savoy toward Westminster as the light goes, or start at Westminster if you took a taxi from Mayfair. This is the view. Barges, the London Eye in the distance, the South Bank lights. Call it a river.", "Dinner at Rules, on Maiden Lane, if you booked. It is older than these hotels and it is a short walk from the Savoy. Mayfair guests can eat nearer Brook Street and do the river tomorrow instead.", "A Strand-facing Savoy room is a fine hotel and the wrong answer to this search.", "River Thames"),
        day(2, "One gallery, then the park", "Hyde Park is the Four Seasons reason to exist. Everyone else can still walk it.", "National Gallery at opening. The Sainsbury Wing, then one set of rooms you care about. Ninety minutes. The building is free and it will still exhaust you if you try to be complete.", "Hyde Park from Park Lane to the Serpentine and back. Sit. Claridge's is a 15-minute walk from the park gate. The Savoy is a taxi or a long Embankment-plus-Mall walk; take the taxi and keep the energy for the park.", "If you booked afternoon tea, it is today, and it was booked weeks ago. Claridge's is the room people mean. One sitting. Then a light dinner, because tea is dinner.", "Tea without a reservation is a lobby and a refusal. Have a backup restaurant.", "National Gallery"),
        day(3, "Mayfair in the morning, then the station", "A short Mayfair walk, then the station. A second museum does not fit a checkout.", "Brook Street, Burlington Arcade, and a coffee. The arcade is a straight roofed street of shops. You do not need to buy anything. St James's Park if you would rather have trees than windows.", "Leave from Green Park if you are in Mayfair, or from Charing Cross if you are at the Savoy. Heathrow is the Elizabeth line from a central station, not a romantic taxi across the city at 4 p.m. unless the fare is already in the budget.", "Eat before the platform. The hotel breakfast is the one to pay for on the morning you are not rushing.", "Brighton is an hour by train and it is not a morning add-on. The sea is a separate trip.", "Burlington Arcade"),
    ],
    attractions=[
        sight("River Thames", "The only water in this booking. Brown, tidal, and worth a dusk walk.", "A Savoy river room, or the Embankment on foot. Not the Atlantic.", "River Thames"),
        sight("Hyde Park, London", "The view from Park Lane, and the walk for the other two hotels.", "Serpentine, then back. A festival weekend is not a quiet luxury morning.", "Hyde Park, London"),
        sight("National Gallery", "The one museum, because it is free and it is near the Savoy.", "Opening time. One wing.", "National Gallery"),
        sight("St James's Park", "The green piece between Mayfair and the river.", "A morning walk if Hyde Park was yesterday.", "St James's Park"),
        sight("Waterloo Bridge", "The best ordinary viewpoint, a few minutes from the Savoy.", "Stand in the middle. The City one way, Westminster the other.", "Waterloo Bridge"),
        sight("Burlington Arcade", "A short, covered Mayfair walk on the last morning.", "Look, then coffee. It is not a duty-free itinerary.", "Burlington Arcade"),
    ],
    scenic_routes=[
        route("Victoria Embankment", "From The Savoy to Westminster Bridge along the river.", "About 2 km, 40 minutes"),
        route("South Bank return", "Across Waterloo Bridge and back on the South Bank to the bridge you came from.", "About 3 km, 1 hour"),
        route("Park Lane to the Serpentine", "From the Four Seasons side of Hyde Park to the water and back by Albert Gate.", "About 4 km, 90 minutes"),
    ],
    transport="Taxis are reasonable on this budget for the park-to-river hop and the airport. Walk the Embankment and Mayfair. The Elizabeth line is the adult way to Heathrow even from a palace, because a Friday taxi is a queue with leather seats.",
    food=[
        dish("Afternoon tea", "Claridge's, if you booked it", "One sitting, planned before the trip. It replaces dinner. The unbooked version is a disappointment in a nice lobby."),
        dish("Dinner at Rules", "Rules, Maiden Lane", "Game, pudding, a short walk from the Savoy. Book. It is a London restaurant, not a hotel restaurant."),
        dish("Lunch at The Wolseley", "The Wolseley, Piccadilly", "Breakfast or a late lunch. The grand café, useful when you want the room without a tasting menu."),
        dish("A normal breakfast", "A coffee on Brook Street or the Strand", "Pay for the hotel breakfast once. The other mornings, walk."),
    ],
    tips=[
        "Write 'river-facing room' to The Savoy. A courtyard or a Strand room will not become the Thames because you asked at 9 p.m.",
        "Four Seasons Park Lane faces the park. Claridge's faces Mayfair. Neither is a consolation ocean.",
        "Corinthia London, on Whitehall Place, is the other grand hotel near the river. Most of its rooms are not river-front. Treat it as a spa hotel with a short walk to the Embankment.",
        "Do not bolt Brighton onto this stay as a 'morning by the sea.' The train is an hour each way and the day disappears.",
    ],
    faqs=[
        faq("Which room actually sees water?", "A river-facing room at The Savoy. Ask for that phrase. Many Savoy rooms look at the courtyard or the Strand."),
        faq("Is the Thames worth the rate?", "At dusk, from the Embankment or from a river room, yes. The water is brown. The sea is in Brighton."),
        faq("Can I see the ocean from anywhere in these hotels?", "No. Not from the roof, not from a suite, not on a clear day."),
        faq("What if The Savoy is full?", "Stay at Claridge's or the Four Seasons and walk the Embankment for the water. Do not rebrand a park view as a sea view."),
    ],
    map_places=[
        stop("River Thames", "London", "United Kingdom", "River Thames"),
        stop("The Savoy", "London", "United Kingdom", ""),
        stop("Hyde Park", "London", "United Kingdom", "Hyde Park, London"),
        stop("National Gallery", "London", "United Kingdom", "National Gallery"),
        stop("Waterloo Bridge", "London", "United Kingdom", "Waterloo Bridge"),
        stop("Burlington Arcade", "London", "United Kingdom", "Burlington Arcade"),
    ],
    budget_notes="A room at these three is often $800–1,600, and a confirmed river room or a park suite goes above that. Afternoon tea and a Rules dinner are the two meals to plan; the rest can be a Wolseley lunch and a bakery. The National Gallery is free. The ocean you searched for is a Brighton hotel, not a line item on this bill.",
))


add(trip(
    slug="london-near-the-beach-under-300",
    title="London's beach trip: sleep in Brighton, an hour down the line",
    location="Brighton, United Kingdom",
    summary=(
        "The honest 'London near the beach' trip sleeps in Brighton, on shingle, with the Channel in front of the Grand. "
        "Under $300 is realistic at Hotel du Vin and the Premier Inn for most of the year, and at The Grand outside summer weekends. "
        "London Victoria is about an hour by train if you want one city day. It is not where you stay."
    ),
    who="People who want a beach within reach of London and are done pretending the Thames Embankment is a shore.",
    best_time="May, June, and September. August weekends push The Grand through $300. Winter is a seafront walk in a coat, not a swim.",
    nights=3,
    hook="3 nights · Brighton beach, London by train · $140–280/night",
    constraints=["Sleep by the sea", "Under $300 off peak", "London by train, not as the base"],
    lodging="$140–280",
    daily="$210–380",
    neighborhoods=[
        stay_area("King's Road seafront", "The Grand is on the front. You hear the road and you see the water. This is the hotel that breaks the cap in August."),
        stay_area("The Lanes", "Hotel du Vin and the North Street Premier Inn are a short walk inland. Quieter nights, same beach after breakfast."),
    ],
    hotels=[
        hotel("The Grand Brighton", "King's Road", "The Victorian hotel on the seafront, opened in the 1860s. Ask for a sea-view room and expect that room to clear $300 on a summer weekend. The building is the landmark; the A259 is the noise.", "$180–400", "Brighton"),
        hotel("Hotel du Vin Brighton", "Ship Street, the Lanes", "A townhouse hotel in the Lanes, about ten minutes downhill to the shingle. Often the better under-$300 bed if you do not need to see the water from the pillow.", "$160–300", "Brighton"),
        hotel("Premier Inn Brighton City Centre", "North Street", "The reliable room that usually stays under $300, a short walk to the front. Generic in the way Premier Inns are, and the correct booking when the Grand is priced for a wedding.", "$100–200", "Brighton"),
    ],
    itinerary=[
        day(1, "Down from London, onto the shingle", "The London train drops you in town, and the beach is a walk from the station.", "London Victoria or London Bridge to Brighton, about an hour. Drop bags. Walk the front from the Palace Pier toward the West Pier's iron skeleton. Do not climb on it.", "The beach is stones, not sand. Swim only if you meant to. The water is the Channel. Sit if you brought a thick layer between you and the pebbles. Seagulls will try for anything fried.", "Dinner in the Lanes, early. The Cricketers is the old pub if you want a pint and a pie. Book a proper table only if you already know you want one long evening.", "Buy the return train when you buy the outbound. Sunday evenings fill.", "Brighton Palace Pier"),
        day(2, "Beach in the morning, one building after", "The sea before the museum, or the museum will become the day.", "On the beach while it is still a local morning. Walk east toward Kemp Town and the beach huts. That stretch is the quiet version of the front.", "The Royal Pavilion if you want the one indoor sight. The building is the exhibit. Book a time in season. If you would rather not, North Laine is the shop streets and it does not require a ticket.", "Seafood at English's, in the Lanes, if you booked. Oysters or a sole when the price is sane. Fish and chips on the front is the other dinner, eaten outside, once.", "Seagulls are serious. Eat under a roof or guard the chips.", "Royal Pavilion"),
        day(3, "London for a few hours, or the train home", "A city day only if you are not also flying.", "If you want London: one train up, the National Gallery or the British Museum, not both, and a train back. An hour each way. Be honest about the clock.", "If you do not want London, swim or walk the front again and leave in the afternoon. Gatwick is about 30 minutes by train if that is the airport. Heathrow is a longer connection and should not be combined with a London museum.", "Dinner in Brighton only if the flight is tomorrow. Otherwise eat before the platform.", "A London day on a departure day is how people miss trains. Pick one.", "The Lanes"),
    ],
    attractions=[
        sight("Brighton Palace Pier", "The working pier at the center of the front.", "Walk it once. The amusements are optional and loud.", "Brighton Palace Pier"),
        sight("Royal Pavilion", "The indoor sight, a palace that looks like nothing else on this coast.", "Book in season. The outside is free if the inside is sold out.", "Royal Pavilion"),
        sight("The Lanes", "The old streets just inland, where two of the hotels are.", "Dinner here. The beach is a ten-minute walk downhill.", "The Lanes"),
        sight("West Pier", "The ruined iron pier west of the Grand. A silhouette, not an attraction you enter.", "Look from the promenade. Stay off the structure.", "West Pier"),
        sight("Brighton beach", "Shingle and cold water. The reason the trip exists.", "Shoes you can take off. A towel thick enough for stones.", ""),
        sight("North Laine", "The parallel shopping streets, for the afternoon you skip the Pavilion.", "A coffee and a wander. It is not a second town.", ""),
    ],
    scenic_routes=[
        route("Pier to the West Pier", "Along the promenade from Brighton Palace Pier to the West Pier remains.", "About 1.5 km, 30 minutes"),
        route("Kemp Town huts", "East along the seafront to the beach huts and back.", "About 3 km out and back, 70 minutes"),
        route("London to Brighton", "Victoria or London Bridge to Brighton, direct. The last ten minutes are the approach to the sea.", "About 1 hour"),
    ],
    transport="Train from London, then walk. All three hotels are in the center. The seafront bus is for rain or for Kemp Town if you are done walking. Gatwick is the nearby airport, about 30 minutes by train. A car in Brighton is a parking problem.",
    food=[
        dish("Fish and chips", "A fryer on the front", "Once, eaten with attention to the gulls. Not the every-meal plan."),
        dish("Oysters or a sole", "English's, the Lanes", "The old seafood room. Book. A dozen oysters or one proper fish, not both unless you mean it."),
        dish("Pie and a pint", "The Cricketers, the Lanes", "The first night, without a reservation strategy. A pie is enough."),
        dish("Bacon sandwich", "A café in North Laine", "Before the beach, on the morning you want something hot. Then you are outside."),
    ],
    tips=[
        "The beach is stones. A fashionable towel is not enough. Bring something thick, and shoes you can carry.",
        "The Grand's sea view is the room that breaks $300 in July and August. Hotel du Vin and the Premier Inn are how the cap survives.",
        "Gulls take food from hands. It stops being funny immediately.",
        "Trains back to London on Sunday evenings are the ones that strand people. Buy the seat earlier.",
    ],
    faqs=[
        faq("Is Brighton near London?", "About an hour, station to station, when the trains are behaving. It is a beach trip with a London door, not a London neighborhood."),
        faq("Can I swim?", "Yes, from the public beach, at your own judgment. There is no hotel private beach in this plan. The water is cold outside high summer."),
        faq("Which hotel is on the water?", "The Grand. Hotel du Vin and the Premier Inn are a short walk inland. You lose the sound of the road at night and you still reach the sea after breakfast."),
        faq("What if I only have one beach day?", "Come anyway, and do not add a London museum. Brighton as a lunch stop is a train and a photograph."),
    ],
    map_places=[
        stop("Brighton Palace Pier", "Brighton", "United Kingdom", "Brighton Palace Pier"),
        stop("Royal Pavilion", "Brighton", "United Kingdom", "Royal Pavilion"),
        stop("The Lanes", "Brighton", "United Kingdom", "The Lanes"),
        stop("West Pier", "Brighton", "United Kingdom", "West Pier"),
        stop("Brighton station", "Brighton", "United Kingdom", ""),
        stop("London Victoria", "London", "United Kingdom", ""),
    ],
    budget_notes="Hotel du Vin often sits at $160–300, the Premier Inn under $200, and The Grand at $180–400 with the sea view as the part that exceeds $300 on summer weekends. A seafood dinner is $40–70. Fish and chips and a pub pie keep a day cheaper. The train from London is the other real cost; buy it with the hotel. The beach is free and uncomfortable, which is the local deal.",
))


add(trip(
    slug="london-quiet-romantic-getaway",
    title="A quiet London weekend: Marylebone, the park, and no Leicester Square",
    location="London, United Kingdom",
    summary=(
        "A romantic weekend in London fails when the hotel is on a taxi rank. Stay on Dorset Square or Seymour Street, or on a stucco street in Notting Hill at The Laslett. "
        "The plan is a long breakfast, Regent's Park or Hyde Park when it is not a festival, one dinner you booked weeks ago, and the Thames at dusk. "
        "No clubs, and no show unless you already love the play."
    ),
    who="A couple who want London and also want to hear each other at 10 p.m.",
    best_time="April to June, or September. Check Hyde Park for festival weekends before you promise a quiet morning. A winter weekend works if the Wallace Collection replaces the park.",
    nights=3,
    hook="3 nights · Marylebone, quietly · $250–450/night",
    constraints=["Quiet streets", "One good dinner", "No West End crawl"],
    lodging="$250–450",
    daily="$360–600",
    neighborhoods=[
        stay_area("Marylebone", "Dorset Square and Seymour Street are the brief. Regent's Park to the north, Hyde Park to the south, and almost nothing open at 1 a.m. that you will regret."),
        stay_area("Notting Hill, if you want it quieter still", "The Laslett is a townhouse on Pembridge Gardens. Portobello on a Saturday morning is a visit, not a reason to sleep on the market."),
    ],
    hotels=[
        hotel("Dorset Square Hotel", "Dorset Square, Marylebone", "A Firmdale townhouse on the garden square where Thomas Lord's first cricket ground stood. English rooms, a quiet night, a short walk to Regent's Park. This is the hotel that matches the brief most closely.", "$280–480", "London"),
        hotel("The Zetter Townhouse Marylebone", "Seymour Street", "A townhouse with a cocktail lounge that is a room, not a club. One drink downstairs and you can still be asleep by eleven. Edgware Road is nearby; the hotel is the calm part of that map.", "$250–420", "London"),
        hotel("The Laslett", "Pembridge Gardens, Notting Hill", "A townhouse hotel on a white-stucco street. You are a walk from the Hill and a bus from Kensington Gardens. Choose it if you want evenings even quieter than Marylebone, and do not come on a Saturday expecting Portobello to be empty.", "$220–400", "London"),
    ],
    itinerary=[
        day(1, "The square, then an early dinner", "Arrive, walk the square, and keep the evening for one early dinner.", "Drop bags. Walk Dorset Square and north into Regent's Park. The rose garden if it is late spring or summer. If you booked The Laslett, do this hour in Kensington Gardens instead and save Regent's Park.", "A long lunch or a late breakfast you did not rush. Then the hotel. The rest is the point of three nights. Read, nap, change for dinner.", "Dinner on Marylebone High Street, booked. Fischer's if you want a wood-paneled room and a proper plate. Be seated by 7:30. The Zetter's lounge is one drink before, not the evening.", "Saturday night in Marylebone still needs a reservation. The streets are quiet and the small rooms are full.", "Regent's Park"),
        day(2, "Hyde Park, then the river at dusk", "Daylight in the park. The Thames after, when the lights are on.", "Hyde Park from Marble Arch toward the Serpentine, in the morning, before the shops. Sit. Skip Kensington Palace unless you already wanted it. Festival weekends are the exception: if the park is a stage, go to the Wallace Collection instead.", "Rest after lunch. A couple of hours in the room is a successful afternoon on this trip.", "Tube or a taxi to Westminster. Walk the Embankment toward Blackfriars as it gets dark, then a taxi home. Do not turn the South Bank into a bar crawl. One drink with the view is the shape of it.", "Hyde Park in July can be a concert site. Check the dates when you book the hotel.", "Hyde Park, London"),
        day(3, "One small museum, then the train", "The Wallace Collection, which is the right size for a departure morning.", "Wallace Collection at opening, Manchester Square, a short walk from both Marylebone hotels. Free. A house of paintings, armor, and furniture. An hour. If it is closed, the morning is another loop of Regent's Park.", "Coffee on Marylebone High Street. Laslett guests can do a short Portobello walk only if it is not late on a Saturday, then the station.", "Paddington, Marylebone, or a taxi to the airport. Eat before you go. There is no evening plan, and that is correct.", "A play is a good night if you already wanted that play. It is a bad default for this trip.", "Wallace Collection"),
    ],
    attractions=[
        sight("Regent's Park", "The morning walk from Dorset Square.", "Roses in season. A weekday if you can.", "Regent's Park"),
        sight("Hyde Park, London", "The long green morning, done before lunch.", "Serpentine, a bench, then leave. Avoid festival build days.", "Hyde Park, London"),
        sight("Wallace Collection", "A free house-museum that fits a quiet trip.", "Opening time. An hour. Manchester Square.", "Wallace Collection"),
        sight("Marylebone", "The neighborhood itself: the square, the High Street, the scale of the streets.", "Stay here. Visit the West End; do not sleep there.", "Marylebone"),
        sight("River Thames", "Dusk on the Embankment, then home.", "Westminster to Blackfriars. A taxi back.", "River Thames"),
        sight("Kensington Gardens", "The park walk if you slept at The Laslett.", "Morning, then back to Pembridge Gardens. Portobello is separate and busier.", "Kensington Gardens"),
    ],
    scenic_routes=[
        route("Dorset Square to the roses", "Out of the square, north to Regent's Park and the rose garden.", "About 1.5 km, 25 minutes"),
        route("Marble Arch to the Serpentine", "Across Hyde Park to the bridge and back on a parallel path.", "About 3 km, 50 minutes"),
        route("Embankment at dusk", "Westminster Bridge toward Blackfriars, lights coming on, then a taxi.", "About 2.5 km, 40 minutes"),
    ],
    transport="Walk Marylebone. A taxi or one Tube ride for the river evening, so you are not on the South Bank looking for a bus at 10. The Laslett is a bus or a short Tube from the parks. Heathrow is the Elizabeth line from Paddington, which is close to all three hotels.",
    food=[
        dish("A booked dinner", "Fischer's, Marylebone High Street", "The Austrian room. Book it before the hotel if your dates are a weekend. Eat early."),
        dish("Pastry on the High Street", "A Marylebone bakery", "Breakfast in the square or walking. Not room service every morning."),
        dish("One cocktail", "The Zetter Townhouse lounge, if you are staying there", "One round, then the table you booked. The lounge is a room, and it is easy to stay too long."),
        dish("A Sunday roast", "A Marylebone pub, only if you booked it", "Skip the hunt if you did not reserve. A roast is not a walk-in plan at 1 p.m."),
    ],
    tips=[
        "Leicester Square, Soho after 10 p.m., and any hotel 'a minute from the theaters' is the other trip.",
        "Book dinner before you book the smaller restaurant. Marylebone on a Saturday is quiet in the street and full at the tables.",
        "Ask for a room off a busy pub garden. Squares are quiet until someone sits under the window.",
        "Portobello on Saturday is a crowd. If that is your weekend, sleep in Marylebone and visit in the morning.",
    ],
    faqs=[
        faq("Is Notting Hill quieter than Marylebone?", "The Laslett's street is. Portobello on a Saturday is not. Sleep in Marylebone if your dates include that morning and you want it only as a visit."),
        faq("Do we need a show?", "No. Add a play only when there is a specific play. Otherwise the evening is dinner and the river."),
        faq("Can we add a night in the countryside?", "That is a different booking. Three nights is enough to be quiet inside London if the hotel is off the West End."),
        faq("What does it cost?", "These townhouses are often $250–450 a night, more on a Saturday at Dorset Square. Under $200 puts you in a Premier Inn, which is a fine bed and the wrong atmosphere."),
    ],
    map_places=[
        stop("Regent's Park", "London", "United Kingdom", "Regent's Park"),
        stop("Hyde Park", "London", "United Kingdom", "Hyde Park, London"),
        stop("Wallace Collection", "London", "United Kingdom", "Wallace Collection"),
        stop("Marylebone High Street", "London", "United Kingdom", "Marylebone"),
        stop("River Thames", "London", "United Kingdom", "River Thames"),
        stop("Kensington Gardens", "London", "United Kingdom", "Kensington Gardens"),
    ],
    budget_notes="Budget $250–450 for the room. Dorset Square on a Saturday can sit above that. One booked dinner is $70–120 a person if you order properly. Breakfast from a bakery and a free morning at the Wallace Collection keep the other day closer to $40–60 of spending on top of the hotel. The park and the Embankment are free.",
))


add(trip(
    slug="rome-city-center-walkable",
    title="Walkable Rome: the centro on foot, and one real night in Trastevere",
    location="Rome, Italy",
    summary=(
        "Four nights inside the centro storico, sleeping between Campo de' Fiori and the Pantheon, for people who will walk to the river and not tour Rome by taxi. "
        "One morning is the Forum and the Colosseum, with tickets already in hand. One evening is Trastevere, which means crossing the Tiber and staying for dinner. "
        "The Vatican is a half day of its own. It is not something you pass on the way to lunch."
    ),
    who="A couple or two friends who want the old center on foot and will book the two timed tickets before they book the trattoria.",
    best_time="April, May, and October. August is hot and a lot of family trattorie close. The Vatican Museums are closed most Sundays. The Forum is a morning place in every season.",
    nights=4,
    hook="4 nights · Centro on foot · $180–360/night",
    constraints=["Walkable centro", "Timed tickets bought first", "Vatican as a half day"],
    lodging="$180–360",
    daily="$270–460",
    neighborhoods=[
        stay_area("Campo de' Fiori and the Pantheon", "All three hotels are in this knot of streets. The square is a market in the morning and a bar scene at night. Ask for a room off the fountain if you sleep lightly."),
        stay_area("Trastevere, for dinner only", "Cross at the Isola Tiberina, eat, and come back. Staying over there is a different trip. You want to wake up by the Pantheon."),
    ],
    hotels=[
        hotel("Hotel Campo de' Fiori", "Campo de' Fiori", "Just off the square, in the middle of the walk. The location is the argument. The square gets loud after 10 p.m., so take a room that does not face it if you can.", "$200–380", "Rome"),
        hotel("Albergo del Senato", "Piazza della Rotonda", "On the square in front of the Pantheon. You open the door and the building is there. Rooms are not large. You are paying for that door.", "$250–450", "Rome"),
        hotel("Hotel Teatro di Pompeo", "Largo del Pallaro", "A small hotel built into what remains of Pompey's theatre, a few quiet minutes from Campo de' Fiori. Calmer than a square-facing room. The old wall in the breakfast room is the real one.", "$160–280", "Rome"),
    ],
    itinerary=[
        day(1, "The small center, at dusk", "Arrive and walk the streets you will use all week. No ancient campus yet.", "Drop bags. Pantheon outside, and inside if the timed entry you booked is this afternoon. If it is not, leave the interior for a morning and keep walking. Piazza Navona next, one loop, no second gelato yet.", "Trevi Fountain at dusk, when it is crowded rather than impossible. Then back toward the hotel through the side streets, not along the souvenir spine of Via del Corso.", "Dinner near the hotel, booked. Cacio e pepe at Armando al Pantheon if you planned ahead. A glass of wine on Campo de' Fiori is fine at 6 and a mistake at midnight.", "The Pantheon is timed. Have the slot or enjoy the portico.", "Pantheon, Rome"),
        day(2, "Colosseum and Forum, then stop", "One ancient morning. Lunch is the end of the ruins.", "Be at the Colosseum at opening with the combined ticket, then walk into the Forum. Do them in that order while you are fresh. The Palatine is the add-on only if you are not already done. You should be out by early afternoon.", "The Capitoline terrace overlooking the Forum is free and it is the right last view. Then a taxi or a slow walk back to the centro. Rest. Do not add a church interior out of guilt.", "Trastevere at night. Cross at the Isola Tiberina, walk to Piazza Santa Maria in Trastevere, and eat on a street one block off the square, where you booked. A short taxi home if your feet are finished.", "Buy the Colosseum and Forum ticket before the trip. The walk-up line is the failure mode.", "Colosseum"),
        day(3, "The Vatican, and nothing else important", "A half day, protected from the rest of the city.", "Vatican Museums at the first entry you can get. Raphael rooms, the Sistine, and out. It is already a lot. St. Peter's if you still have attention; the dome is a lot of stairs and it is optional. The museums are closed most Sundays.", "Lunch in Prati or back in the centro. Then sit. A second museum this afternoon is how the week sours. A nap and a nasoni refill is the correct program.", "A simple dinner near Campo de' Fiori. Pizza al taglio from Antico Forno Roscioli if you want bread and tomato instead of another seated meal. Gelato from Gelateria del Teatro after, not before.", "From the Pantheon, the Vatican is a 30- to 40-minute walk or a short taxi. Do not walk it at the end of a Forum morning. That was yesterday.", "Vatican Museums"),
        day(4, "Market, Ghetto, airport", "The neighborhood morning you did not have time for, then the airport.", "Campo de' Fiori market in the morning if it is running. It is a produce market, not a craft fair, and it is a morning thing. Buy fruit for the train.", "The Ghetto: the turtle fountain, the Portico d'Ottavia, and carciofo alla giudia if artichokes are in season, which is the cooler months. One plate, fried, with a lemon.", "Termini for the Leonardo Express, or a taxi to Fiumicino. The taxi from inside the walls is a fixed fare; ask the driver to confirm it before the bags go in.", "Leave the Vatican off this day. A half-done museum and a missed flight is a bad trade.", "Campo de' Fiori"),
    ],
    attractions=[
        sight("Pantheon, Rome", "The building outside the hotel door, if you stayed at the Senato.", "A timed interior, or the portico and the square.", "Pantheon, Rome"),
        sight("Piazza Navona", "The Baroque square on the first-evening loop.", "One walk through. Eat one street away, where the menus are calmer.", "Piazza Navona"),
        sight("Trevi Fountain", "Seen at dusk on day one, when you are already out.", "Stand, look, leave. It does not get better at midnight.", "Trevi Fountain"),
        sight("Colosseum", "The ancient morning, paired with the Forum on one ticket.", "Opening slot. Do this before the Forum, not after a long lunch.", "Colosseum"),
        sight("Roman Forum", "The ruins you walk after the Colosseum, while the ticket still makes sense.", "Leave before you are angry at the gravel. The Capitoline view is the coda.", "Roman Forum"),
        sight("Trastevere", "One neighborhood evening across the river.", "Isola Tiberina, a booked table off the main square, then home.", "Trastevere"),
        sight("Vatican Museums", "A half day with a morning entry. The Sistine is the end, not the start.", "First slot you can get. Closed most Sundays. Do not pair it with the Forum.", "Vatican Museums"),
    ],
    scenic_routes=[
        route("Pantheon, Navona, Trevi", "From the Rotonda to Piazza Navona and across to the Trevi Fountain in the side streets.", "About 2 km, 1 hour with the crowds"),
        route("Into Trastevere", "From Campo de' Fiori across the Isola Tiberina to Piazza Santa Maria in Trastevere.", "About 2 km, 35 minutes"),
        route("Colosseum to the Capitoline view", "Out of the Forum and up to the terrace that looks back over it. The ticketed half is the morning; this is the last kilometer.", "About 2 km inside the sites, half a day all in"),
    ],
    transport="Walk the centro. A taxi for the Vatican if you do not want the 40-minute walk, and a taxi home from Trastevere if dinner ran long. Fiumicino is the Leonardo Express from Termini or a fixed-fare taxi from inside the walls. Confirm the fare before you sit. Do not rent a car.",
    food=[
        dish("Cacio e pepe", "Armando al Pantheon", "Book it. Pecorino and pepper, not a cream sauce. This is the dinner to plan, not the one you find at 9."),
        dish("Carciofo alla giudia", "A trattoria in the Ghetto", "Fried artichoke, in season, roughly the cooler months. One each. Squeeze the lemon."),
        dish("Pizza al taglio", "Antico Forno Roscioli, Via dei Giubbonari", "Lunch, standing or walking. One or two pieces. The sit-down Roscioli restaurant is a different reservation."),
        dish("Gelato", "Gelateria del Teatro", "After dinner, a short walk from Campo de' Fiori. Two flavors. The first gelato of the day at 11 a.m. ruins the pace."),
    ],
    tips=[
        "Book the Colosseum-Forum ticket and the Vatican Museums before you book dinner. Everything else on this trip can be walked without a slot, except the Pantheon interior.",
        "The Vatican is a half day. An hour is enough for the square outside St. Peter's and a decision to come back another year.",
        "Campo de' Fiori at night is a drinking square. Pretty at 6. Loud at midnight. Interior rooms exist for a reason.",
        "Water from the nasoni is safe. Carry a bottle. August heat is not a surprise you should meet empty-handed.",
    ],
    faqs=[
        faq("Can we walk the whole trip?", "Yes, except the Vatican, which is a real walk or a short taxi from the Pantheon. Do not add that walk to the end of a Forum morning."),
        faq("Is Trastevere worth leaving the centro for?", "Yes, once, for dinner. Sleeping there is a different plan. You want to wake up by the Pantheon."),
        faq("How many ancient sites in one day?", "The Colosseum and the Forum. The Palatine only if you are not tired. The Vatican is the next day, alone."),
        faq("What does a walkable room cost?", "Teatro di Pompeo and Campo de' Fiori often land at $180–350. A Pantheon-facing room at Albergo del Senato costs more and is smaller than the photograph."),
    ],
    map_places=[
        stop("Pantheon", "Rome", "Italy", "Pantheon, Rome"),
        stop("Trevi Fountain", "Rome", "Italy", "Trevi Fountain"),
        stop("Colosseum", "Rome", "Italy", "Colosseum"),
        stop("Roman Forum", "Rome", "Italy", "Roman Forum"),
        stop("Trastevere", "Rome", "Italy", "Trastevere"),
        stop("Vatican Museums", "Rome", "Italy", "Vatican Museums"),
    ],
    budget_notes="A centro room is often $180–360, more at the Senato when you face the Pantheon. A trattoria dinner is $30–50 a person if you do not start ordering the English menu's specials. Pizza al taglio is lunch for $8. The combined Colosseum and Forum ticket and the Vatican ticket are about $20–30 each. Taxis to Fiumicino are a fixed fare; the walk itself is free.",
))


add(trip(
    slug="rome-with-private-pool",
    title="A private pool in Rome: shared, seasonal, or up on Monte Mario",
    location="Rome, Italy",
    summary=(
        "A private pool inside the Aurelian walls is not a real category, and this page will not invent a villa to fill one. "
        "Hotel de Russie has a shared saltwater hydrotherapy pool in the spa, which is a soak, not a lap pool in the suite. "
        "Anantara Palazzo Naiadi has a shared rooftop pool in warm months, and the hotel has said it is closed from 5 October 2026 until summer 2027. Rome Cavalieri, on Monte Mario, has the full-size outdoor pools, shared, in a park, about 20 minutes by taxi from the centro, and closed in the cold months."
    ),
    who="People who asked for a private pool in Rome and need the three real options described without the brochure.",
    best_time="June to early September if swimming is the reason, and then only at Cavalieri. November through March, book de Russie for the garden and treat any pool as a spa. Do not book Palazzo Naiadi in order to swim until the hotel confirms the roof has reopened.",
    nights=3,
    hook="3 nights · A shared pool, not a private one · $450–1,200/night",
    constraints=["No invented villa", "Shared water only", "Summer if you want to swim laps"],
    lodging="$450–1,200",
    daily="$600–1,450",
    neighborhoods=[
        stay_area("Via del Babuino", "Hotel de Russie sits between the Spanish Steps and Piazza del Popolo. The secret garden is the reason to stay. The spa pool is a small shared extra."),
        stay_area("Monte Mario", "Rome Cavalieri is outside the centro, in its own park. The outdoor pools are why you accept the taxi. You are not walking home from dinner in Trastevere."),
    ],
    hotels=[
        hotel("Hotel de Russie", "Via del Babuino", "The Rocco Forte hotel with the secret garden. The spa has a shared saltwater hydrotherapy pool, a sauna, and a hammam. It is a soak under the city, not a pool you swim. The location, between Popolo and the Steps, is the reason the room is worth it.", "$700–1,400", "Rome"),
        hotel("Anantara Palazzo Naiadi", "Piazza della Repubblica", "A grand hotel on the square of the naiads, with a shared rooftop pool overlooking the piazza in the warm season. The hotel's own notice says that roof pool is closed from 5 October 2026 until summer 2027. Reconfirm before you book it in order to swim. The spa and the square remain.", "$400–800", "Rome"),
        hotel("Rome Cavalieri, A Waldorf Astoria Hotel", "Monte Mario", "Outdoor pools in the hotel park, shared with guests, plus a family pool. About 20 minutes by taxi from Piazza del Popolo, and not a walk. Outdoor water runs in the warm months and closes in late fall and winter. There is a separate indoor pool in the spa, and spa access is not automatically free. This is the closest thing to a real swim in Rome. It is not private.", "$400–900", "Rome"),
    ],
    itinerary=[
        day(1, "The pool, then one neighborhood", "De Russie is the central plan. Cavalieri and Naiadi are written into the same day.", "If you are at de Russie, walk Piazza del Popolo and up to the Pincio terrace, then back down Via del Babuino. Use the hydro-pool late in the day and do not expect exercise. If you are at Cavalieri, swim first, then one taxi to Piazza del Popolo for that same walk, then back. If you are at Naiadi, look at the fountain on the square and treat the roof as closed unless the desk says otherwise.", "The Spanish Steps from above, early enough that the staircase is not a seat. Antico Caffè Greco on Via dei Condotti for one coffee, standing or at a table, because it is the historic room and once is enough.", "Dinner off Via del Babuino, not on the Piazza del Popolo terrace. A carbonara at a booked trattoria two streets away. Cavalieri guests who do not want a second taxi should eat at the hotel tonight and save the centro dinner for lunch tomorrow.", "Ask what the pool is before you pack swim goggles. A hydrotherapy pool and a  park pool are different objects.", "Piazza del Popolo"),
        day(2, "A short centro morning, then the water", "One set of streets. The afternoon belongs to the hotel.", "Pantheon at opening if you have the slot, or the Trevi Fountain early, and then stop. You are not doing the Forum on a pool trip unless you have given up the pool. Taxi or walk back depending on the hotel.", "Swim, soak, or sit in the de Russie garden. At Cavalieri this is the long outdoor afternoon, in season, with the city below the hill. At Naiadi, if the roof is still closed, the afternoon is the spa you confirmed or a book on the square. Do not go find another hotel's pool.", "A simple dinner. Supplì or a slice if you are in the centro and full from lunch. Cavalieri guests can stay on the hill; leaving at 9 p.m. is a taxi and a decision.", "The Vatican does not fit this day. It does not fit this trip unless you drop the pool.", "Pantheon, Rome"),
        day(3, "A last soak, then the airport", "A last swim or a short walk, then Fiumicino. The Colosseum does not fit a flight day.", "A morning swim if the pool is open. De Russie guests can walk to the Spanish Steps early, when the square is only people with coffee. Cavalieri guests should get in the water and then into a taxi, not into a ruin.", "Fiumicino. From Monte Mario a taxi is the honest transfer. From Via del Babuino, a taxi or a ride to Termini for the Leonardo Express. From Repubblica you are already near Termini, which is the one convenience of Naiadi.", "Eat before you leave the hotel area. The airport is the meal you did not plan.", "Reconfirm Naiadi's roof if your dates are inside the published closure. A closed pool with a nice view is a terrace.", "Spanish Steps"),
    ],
    attractions=[
        sight("Piazza del Popolo", "The square at the end of Via del Babuino, and the right first walk from de Russie.", "The churches, the obelisk, and the gate. Eat off the square.", "Piazza del Popolo"),
        sight("Pincian Hill", "The terrace above the square, which is the view you can have without a ruin.", "Go up in the late afternoon. Come down before you are late for dinner.", "Pincian Hill"),
        sight("Spanish Steps", "A short walk from de Russie, best early.", "Look from the top or the bottom. Sitting on them in a crowd is the other experience.", "Spanish Steps"),
        sight("Pantheon, Rome", "The one centro interior, on the morning you are not swimming.", "A timed slot at opening, then back to the hotel.", "Pantheon, Rome"),
        sight("Trevi Fountain", "The other option for that same short morning.", "Early. Then stop. It pairs badly with a second monument.", "Trevi Fountain"),
        sight("Fountain of the Naiads", "The fountain in front of Palazzo Naiadi, which you can see even when the roof pool is shut.", "The square is the visit. The pool is a separate question for the front desk.", "Fountain of the Naiads"),
        sight("Monte Mario", "The hill the Cavalieri sits on, outside the old walls.", "A taxi, not a walk, from the centro. The park paths are inside the hotel grounds.", "Monte Mario"),
    ],
    scenic_routes=[
        route("Babuino and the Pincio", "Piazza del Popolo, up to the Pincian terrace, down and along Via del Babuino to the Spanish Steps.", "About 2 km, 45 minutes"),
        route("Pantheon to the Trevi", "A short morning link between the two, done at opening, then a taxi back to the pool.", "About 1 km, 20 minutes"),
        route("Cavalieri to Popolo", "A taxi from the hotel gate to Piazza del Popolo. The scenic part is the hill road, and you are not walking it with a towel.", "About 20 minutes by taxi"),
    ],
    transport="Taxis are the design of the Cavalieri version: one in the morning, one back, one to the airport. De Russie and Naiadi can walk their neighborhoods. Fiumicino from Monte Mario should be a taxi you book the night before. From Repubblica, Termini and the Leonardo Express are close.",
    food=[
        dish("One coffee", "Antico Caffè Greco, Via dei Condotti", "The historic caffè near the Steps. Once. It is a stop, not your everyday breakfast."),
        dish("Carbonara", "A booked trattoria off Via del Babuino", "Skip the Piazza del Popolo terraces. Two streets away, at lunch, so dinner can be lighter."),
        dish("Supplì", "A forno between Popolo and the Steps", "The afternoon you refuse another restaurant. Eat it outside. One is a snack, three is lunch."),
        dish("Dinner on the hill", "Rome Cavalieri, one night", "If you are staying up there, one hotel dinner is rational because the alternative is a taxi. Do not pay it three times."),
    ],
    tips=[
        "Match the packing to the pool: a soak at de Russie, a seasonal rooftop at Naiadi, a real outdoor swim at Cavalieri in summer. The photos are not interchangeable.",
        "Palazzo Naiadi's rooftop closure through summer 2027 is a published notice. A terrace with the cover on is not a pool.",
        "Cavalieri in winter is a grand hotel on a hill. The outdoor pools are shut. The indoor spa pool may cost extra. It is not a swim holiday in January.",
        "None of these pools is private. A buyout, where it exists, is an event contract with an event price.",
    ],
    faqs=[
        faq("Can I swim laps in the centro?", "Not at de Russie. The hydro-pool is a soak. For laps, you want Cavalieri's outdoor pool, in season, as a guest. Day passes exist and they are limited."),
        faq("Is there a villa with a private pool nearby?", "There are rentals outside the walls, toward the Appia Antica and the countryside. I am not naming one. Ask for a current dated photo of that pool, and assume you will want a car."),
        faq("Is de Russie worth it without a real pool?", "Yes. The garden and the location are the hotel. The hydro-pool is a spa extra, and it is shared."),
        faq("How awkward is the taxi from Cavalieri?", "About 20 minutes to Piazza del Popolo in ordinary traffic, longer at rush hour. Count a taxi each way if you eat in the centro. That fare is part of choosing the swim."),
    ],
    map_places=[
        stop("Piazza del Popolo", "Rome", "Italy", "Piazza del Popolo"),
        stop("Spanish Steps", "Rome", "Italy", "Spanish Steps"),
        stop("Pantheon", "Rome", "Italy", "Pantheon, Rome"),
        stop("Trevi Fountain", "Rome", "Italy", "Trevi Fountain"),
        stop("Fountain of the Naiads", "Rome", "Italy", "Fountain of the Naiads"),
        stop("Monte Mario", "Rome", "Italy", "Monte Mario"),
    ],
    budget_notes="De Russie is the expensive central bed, often $700–1,400. Naiadi and Cavalieri can land nearer $400–800, and Cavalieri's park is what that money is for in summer. A taxi each way from Monte Mario is part of the daily cost. Spa entry is not always included; ask. A centro lunch can stay at $30–50. The private pool in the original request is a house outside the walls, not a line on these bills.",
))
