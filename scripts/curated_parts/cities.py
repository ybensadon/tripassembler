"""Dubai, Marrakech, Japan, Bangkok, Sydney, New York, Los Angeles, Banff, Cape Town."""
from _common import trip, hotel, stay_area, day, sight, route, dish, faq, stop

TRIPS = []


def add(record):
    TRIPS.append(record)


add(trip(
    slug="dubai-luxury-with-ocean-view",
    title="Dubai luxury on the Gulf, not a Downtown fountain view",
    location="Dubai, United Arab Emirates",
    summary=(
        "Four nights on Jumeirah Beach, where the water in front of the hotel is the Arabian Gulf. "
        "Burj Al Arab, Jumeirah Beach Hotel, and Four Seasons Resort Dubai at Jumeirah Beach are beach "
        "hotels. A Downtown tower looking at the fountain is a skyline view, and this trip does not pretend otherwise."
    ),
    who="A couple or two friends who want a real Gulf view and will take a taxi when they want the skyline.",
    best_time="November to March. June through September is brutally hot; the beach is an early-morning idea, and midday belongs indoors.",
    nights=4,
    hook="4 nights · Arabian Gulf from Jumeirah · $500–1,800/night",
    constraints=["Gulf view, not a fountain view", "Beach hotels in Jumeirah", "Taxi or metro for Downtown"],
    lodging="$500–1,800",
    daily="$700–2,200",
    neighborhoods=[
        stay_area("Jumeirah Beach / Umm Suqeim", "The beach in front of these hotels is the Gulf. Burj Al Arab sits on its own island just offshore. This is not Dubai Marina and not Downtown."),
        stay_area("Downtown, as an outing", "Dubai Mall and the fountain are worth one evening. Go there by taxi. Do not move the hotel there and then call the fountain an ocean."),
    ],
    hotels=[
        hotel("Burj Al Arab", "Jumeirah, on its own island", "The sail stands offshore of Jumeirah Beach. Guest rooms look at the Arabian Gulf. It is a landmark hotel, not a subtle one, and it is the clearest 'ocean view' in the city.", "$1,200–3,000", "Dubai", "https://www.jumeirah.com/en/stay/dubai/burj-al-arab-jumeirah"),
        hotel("Jumeirah Beach Hotel", "Umm Suqeim", "The wave-shaped hotel on the sand beside Burj Al Arab. The Gulf is in front of the building. Pools here are shared hotel pools.", "$400–900", "Dubai"),
        hotel("Four Seasons Resort Dubai at Jumeirah Beach", "Jumeirah Beach", "A low-rise resort on a long stretch of Jumeirah Beach. Book a Gulf-facing room; some rooms look back toward the skyline instead of the water.", "$500–1,100", "Dubai"),
    ],
    itinerary=[
        day(1, "The beach you actually booked", "Arrive, stay on the Gulf, and do not start with a mall.", "Transfer to Jumeirah. Walk the beach toward Burj Al Arab and look at the water you came for.", "Swim or sit. If it is summer, make this the early morning and spend the hot hours at the hotel pool.", "Dinner at the hotel or a short taxi along Jumeirah Beach Road. Leave Downtown for tomorrow.", "Ask for a sea-facing room in writing. A 'resort view' can mean the garden.", "Burj Al Arab"),
        day(2, "Old Dubai, then the skyline", "One day off the beach, split between the creek and Downtown.", "Al Fahidi and a ride across Dubai Creek on an abra. The gold and spice souks are on the Deira side.", "Back to the hotel to swim. Do not stack the mall onto a morning that was already outdoors.", "Taxi to Dubai Mall after dark for the fountain. Call it a skyline and a fountain. It is not the Gulf.", "The fountain schedule is posted. You do not need a dinner reservation inside the mall to see it.", "Dubai Creek"),
        day(3, "The Palm, from the water's edge", "A look at the Palm without moving the suitcase.", "Taxi to the Palm for the outer crescent view. Atlantis is a photo stop unless you have already bought a water-park ticket.", "Back to Jumeirah for a long afternoon on the beach. This is the point of the hotel.", "A quiet dinner. Jumeirah Beach Road has restaurants; you do not need a second mall.", "Friday late morning is crowded on the public beaches. The hotel beach is calmer.", "Palm Jumeirah"),
        day(4, "One more swim", "Leave from the beach, not from a theme park.", "A last swim. Jumeirah Mosque is the nearby stop if you want a building that is not a hotel; check the visit hours.", "Taxi to DXB. The drive is often 25 to 40 minutes and longer at rush hour.", "Eat before the airport. Terminal food is a compromise.", "Gulf-facing rooms at the Four Seasons are the ones that match this search. Confirm the category.", "Jumeirah Mosque"),
    ],
    attractions=[
        sight("Burj Al Arab", "The Gulf view, from the hotel that sits in it.", "You do not need afternoon tea to have seen it. The beach walk is enough if you are not staying inside.", "Burj Al Arab"),
        sight("Jumeirah Beach", "The actual Arabian Gulf shoreline these hotels face.", "Public sections get busy on Fridays. Hotel beaches are the calmer swim."),
        sight("Dubai Creek", "The old city's water: abras, dhows, and the souks. A creek, not a coast.", "Cross once by abra and walk Al Fahidi on the Bur Dubai side.", "Dubai Creek"),
        sight("Al Bastakiya", "The wind-tower neighborhood by the creek. Low, old, and walkable.", "Go in the morning. Midday in summer is punishing.", "Al Bastakiya"),
        sight("Dubai Mall", "The skyline outing: the fountain and the mall, one evening.", "Do not spend the whole trip here. One visit is the right amount.", "Dubai Mall"),
        sight("Palm Jumeirah", "The offshore palm, seen as a half-day, not as a reason to change hotels.", "Traffic on and off the trunk is the tax. Go and come back.", "Palm Jumeirah"),
    ],
    scenic_routes=[
        route("Jumeirah shoreline walk", "Along the beach from a Jumeirah hotel toward Burj Al Arab. Gulf on one side the whole way.", "About 3 km, under an hour if you stop to look"),
        route("Creek crossing", "Abra from Bur Dubai to Deira, then back. The ride is a few minutes and costs a few dirhams.", "10 minutes on the water"),
        route("Taxi to the fountain", "Jumeirah to Downtown after dark. Skyline and fountain, then the same taxi back to the beach.", "20–40 minutes each way"),
    ],
    transport="Taxis and ride-hailing are the honest way between Jumeirah, the creek, and Downtown. The metro is useful if you are near a station; these beach hotels are not on top of one. Do not rent a car for four nights unless you like parking at malls. DXB is a taxi.",
    food=[
        dish("Grilled fish", "Bu Qtair, Umm Suqeim", "A casual open-air fish grill near the beach hotels. You point at the fish. It is not a linen-tablecloth restaurant."),
        dish("Shawarma", "Al Mallah on Al Dhiyafah, Satwa", "A late-night Beirut-style shawarma street. A taxi from Jumeirah, and worth it once."),
        dish("Luqaimat", "A creekside cafe or the hotel if you would rather not hunt", "Crisp sweet dumplings with date syrup. Dessert, not dinner."),
        dish("Machboos", "A hotel Arabic restaurant on Jumeirah, or Al Fanar if you want the theatrical version", "Spiced rice and meat or fish. Share one. Portions are large."),
    ],
    tips=[
        "Book the room category that says Gulf or sea. 'Partial sea view' and 'skyline' are different products.",
        "June through September: be outside before 9 a.m. and after 4 p.m. The rest of the day is the pool or indoors.",
        "Downtown is one evening. Sleeping there and calling the fountain an ocean view is how this search goes wrong.",
        "Friday is the local weekend. Brunch is an event, and the public beach is busier.",
    ],
    faqs=[
        faq("Is the fountain an ocean view?", "No. The fountain is a lake in front of the mall. The Gulf is at Jumeirah, the Marina beach, and the Palm."),
        faq("Can I see the sea from Burj Khalifa?", "You can see a long way from the top, including toward the coast. That is a viewpoint, not a hotel on the water. This trip does not stay there."),
        faq("Is Atlantis the same beach?", "Atlantis is on the Palm, with its own beach and a water park. It is a different trip. Do not swap it in and expect a quiet Gulf hotel."),
        faq("What does this cost?", "A real Gulf-facing room at these hotels is often $500 and up. Burj Al Arab is in another bracket. Summer sales exist; holiday weeks do not."),
    ],
    map_places=[
        stop("Burj Al Arab", "Dubai", "United Arab Emirates", "Burj Al Arab"),
        stop("Jumeirah Mosque", "Dubai", "United Arab Emirates", "Jumeirah Mosque"),
        stop("Dubai Creek", "Dubai", "United Arab Emirates", "Dubai Creek"),
        stop("Al Bastakiya", "Dubai", "United Arab Emirates", "Al Bastakiya"),
        stop("Dubai Mall", "Dubai", "United Arab Emirates", "Dubai Mall"),
    ],
    budget_notes="The room is the cost. A Gulf-facing night at Jumeirah Beach Hotel or the Four Seasons is often $400–900, and Burj Al Arab is far above that. Taxis add up if you cross the city twice a day. One mall evening and one good dinner are enough; you do not need a theme-park ticket.",
))

add(trip(
    slug="dubai-2-bedroom-under-400night",
    title="A two-bedroom in Dubai under $400, if you respect the season",
    location="Dubai, United Arab Emirates",
    summary=(
        "Four nights in a real two-bedroom apartment hotel with a kitchen. Under $400 a night is a normal summer "
        "rate at these buildings and a tight one from November through March, and during the big event weeks. "
        "The apartments are in Business Bay, Downtown, and Al Jaddaf, not on the Gulf."
    ),
    who="Two couples, or a family, who need two bedrooms and a kitchen and will trade the beach address for the rate.",
    best_time="June to September if the budget is the point. November to March is better weather and worse rates. Avoid F1 week, New Year, and the major festivals if $400 is a ceiling.",
    nights=4,
    hook="4 nights · Two bedrooms and a kitchen · Often under $400 in summer",
    constraints=["Two bedrooms", "Kitchen", "Under $400 only in the right months"],
    lodging="$220–450",
    daily="$320–520",
    neighborhoods=[
        stay_area("Business Bay", "DAMAC Maison Cour Jardin is here. Canal and tower views, a short hop to Downtown, no beach."),
        stay_area("Al Jaddaf", "The Marriott executive apartments are inland and usually the easiest place to hold the rate. A shuttle covers the mall."),
    ],
    hotels=[
        hotel("DAMAC Maison Cour Jardin", "Business Bay", "Hotel-serviced two-bedroom suites with a kitchen, a second bedroom, and a guest bathroom. Business Bay looks at the canal and the skyline, not the Gulf. Summer weeks can sit under $400; winter often does not.", "$250–500", "Dubai"),
        hotel("DAMAC Maison Mall Street", "Downtown, Dubai Mall Street", "Two-bedroom suites with kitchens, a short walk from Dubai Mall. Some floors see the fountain. That is a skyline view. Same seasonal rule: $400 is realistic in summer and optimistic at New Year.", "$280–550", "Dubai"),
        hotel("Marriott Executive Apartments Al Jaddaf", "Al Jaddaf", "One-, two-, and three-bedroom apartments with full kitchens and a washer-dryer. This is the practical under-$400 address in more months of the year. The beach is a shuttle or a taxi, not a walk.", "$180–400", "Dubai"),
    ],
    itinerary=[
        day(1, "Settle the apartment", "Check in, find the grocery, and cook one meal so the kitchen is real.", "Drop bags. A Carrefour or Waitrose run is the first errand, not a museum.", "A short walk or taxi to see where you are: the canal if you are in Business Bay, the creek side if you are in Al Jaddaf.", "Cook dinner. The two-bedroom only pays off if you are not in a restaurant every night.", "Confirm the booking says two bedrooms. A 'family suite' with a sofa bed is a different room.", "Dubai Creek"),
        day(2, "One Downtown evening", "Use the mall as a half-day, not the identity of the trip.", "Morning at the pool or, in winter, a walk. In summer, stay indoors until late afternoon.", "Dubai Mall. Pick one thing: the aquarium or the fountain, not both plus a theme park.", "Dinner cooked, or a simple meal on the way home. The apartment is the restaurant.", "The fountain is outside and free. You do not need a mall restaurant reservation to see it.", "Dubai Mall"),
        day(3, "A beach that is not your hotel", "The apartment is inland. The Gulf is a planned outing.", "Taxi to Jumeirah Public Beach or Kite Beach in the morning, before the heat.", "Back by early afternoon. Laundry and a rest is a legitimate use of a two-bedroom.", "Cook again, or shawarma nearby. Four restaurant dinners will blow the budget the room just saved.", "Public beaches are crowded on Friday. Go another morning if you can.", "Jumeirah Mosque"),
        day(4, "Old Dubai, then the airport", "A last morning with a point, and a flight.", "Al Fahidi and the Dubai Gold Souk, early. Both are small and better before the heat.", "Back to pack. The apartment kitchen means you can eat leftovers instead of buying an airport lunch.", "Taxi to DXB. From Al Jaddaf it is close. From Business Bay, leave more time.", "Tourism dirhams are charged per bedroom per night at many of these buildings. Ask the total, not just the rate.", "Dubai Gold Souk"),
    ],
    attractions=[
        sight("Dubai Mall", "The one big indoor attraction that suits an apartment stay.", "Go once, with a list. The mall expands to fill any afternoon you give it.", "Dubai Mall"),
        sight("Dubai Fountain", "The skyline show, seen from the mall lake.", "Night is when it looks like the photographs.", "Dubai Fountain"),
        sight("Dubai Creek", "The old waterway. A good morning from an Al Jaddaf base.", "The abra is the crossing. You do not need a cruise.", "Dubai Creek"),
        sight("Dubai Gold Souk", "The Deira market, small and specific.", "Windows are for looking. Agree the making charge before you buy.", "Dubai Gold Souk"),
        sight("Al Bastakiya", "Wind-tower lanes on the Bur Dubai side of the creek.", "Pair it with the creek, not with a beach afternoon.", "Al Bastakiya"),
        sight("Jumeirah Beach", "The Gulf outing, because the apartment is not on it.", "Morning only in summer. Take a taxi both ways.", ""),
    ],
    scenic_routes=[
        route("Canal edge in Business Bay", "A flat walk by the Dubai Canal if you are at Cour Jardin. Towers, not surf.", "2–4 km"),
        route("Abra and the souks", "Bur Dubai to Deira and back. Gold souk, spice market, creek.", "Half a morning"),
        route("Taxi to Kite Beach", "The apartment-to-Gulf trip. Go early, swim, leave before the pavement gets hostile.", "20–35 minutes each way"),
    ],
    transport="Taxis. The metro helps if you are willing to walk to a station in the heat, which in summer you should not do at noon. A car is useful for a beach morning and a nuisance at the mall. Budget the tourism fee per bedroom on top of the room rate.",
    food=[
        dish("Home-cooked rice and grill", "Your kitchen, after a Carrefour shop", "The budget only works if several dinners are cooked. Chicken, rice, salad, done."),
        dish("Shawarma", "A neighborhood counter near Business Bay or Al Jaddaf", "The right not-cooking night. One each, eaten early."),
        dish("Fish and rice", "Bu Qtair if you are already at Jumeirah for the beach morning", "Do it on the beach day so you are not crossing the city for one meal."),
        dish("Luqaimat and karak", "A creek cafe or a mall coffee stop", "Sweet dumplings and strong tea. A snack, not a meal plan."),
    ],
    tips=[
        "Under $400 is a summer statement. In winter, the same two-bedroom is often $400–600. Move to Al Jaddaf or shorten the stay rather than pretending the rate is year-round.",
        "Read the room name. 'Two bedroom' means two rooms with doors. A living room with a sofa bed does not.",
        "Ask about the tourism fee per bedroom. It is small and it is extra.",
        "The kitchen is the point. If you eat out every night, book a smaller hotel and stop optimizing the apartment.",
    ],
    faqs=[
        faq("Can I have a Gulf view and two bedrooms under $400?", "Sometimes in summer at a JBR apartment, almost never in winter. This page keeps the rate and gives up the beach address."),
        faq("Is Business Bay walkable to Dubai Mall?", "It is a longer walk than the ads say, and unpleasant in the heat. Use a taxi."),
        faq("Are these residences or hotels?", "All three are serviced apartment hotels with a front desk, housekeeping, and a kitchen in the two-bedroom."),
        faq("What if my dates are over $400?", "Al Jaddaf moves first. If even that is over, the honest answer is a one-bedroom or different dates, not a fictional winter sale."),
    ],
    map_places=[
        stop("Dubai Mall", "Dubai", "United Arab Emirates", "Dubai Mall"),
        stop("Dubai Fountain", "Dubai", "United Arab Emirates", "Dubai Fountain"),
        stop("Dubai Creek", "Dubai", "United Arab Emirates", "Dubai Creek"),
        stop("Dubai Gold Souk", "Dubai", "United Arab Emirates", "Dubai Gold Souk"),
        stop("Al Bastakiya", "Dubai", "United Arab Emirates", "Al Bastakiya"),
    ],
    budget_notes="A two-bedroom at Al Jaddaf can land around $200–350 in summer and shoulder weeks. Cour Jardin and Mall Street run higher and clear $400 easily in winter. Food stays reasonable if you cook three nights and eat simply the other. Taxis are the swing factor if you cross to the beach every day. Add the per-bedroom tourism fee.",
))

add(trip(
    slug="dubai-family-friendly-with-kitchen",
    title="A family apartment in Dubai Marina, plus one beach morning",
    location="Dubai, United Arab Emirates",
    summary=(
        "Four nights in a Dubai Marina or JBR apartment with a kitchen, so dinner is not a restaurant every night. "
        "The days are a beach morning, a short Dubai Mall visit, and time at the pool. Atlantis is not the hotel. "
        "In summer the heat is the main fact of the trip, and midday outside is a mistake."
    ),
    who="Parents with children who want space, a kitchen, and a beach they can reach without changing hotels.",
    best_time="November to March for the beach. If you must come in June, July, or August, plan indoor middays and early swims, and expect the apartment rate to be the cheap part.",
    nights=4,
    hook="4 nights · Marina kitchen · Beach morning, not a theme park",
    constraints=["Kitchen", "Dubai Marina or JBR", "Atlantis is a day trip at most, not the stay"],
    lodging="$250–600",
    daily="$380–650",
    neighborhoods=[
        stay_area("Dubai Marina", "Apartment hotels with kitchens, a walkway, and a beach you can reach at JBR. This is the family base."),
        stay_area("Jumeirah Beach Residence", "The Walk and the sand. JA Oasis Beach Tower is here, which is an apartment building, not a water park."),
    ],
    hotels=[
        hotel("Jannah Place Dubai Marina", "Dubai Marina", "Serviced studios and two-bedroom apartments with a kitchenette and a washing machine. The modest family pick: enough kitchen to make breakfast and a simple dinner.", "$180–350", "Dubai"),
        hotel("JA Oasis Beach Tower", "Jumeirah Beach Residence", "Large two-, three-, and four-bedroom apartments with full kitchens on The Walk, looking at the Gulf and the Marina. This is the beach apartment. It is not Atlantis, and it is not a hotel room with a minibar.", "$300–700", "Dubai"),
        hotel("Grosvenor House Dubai", "Dubai Marina", "Book an apartment with a kitchen and a living room. A standard hotel room does not meet this search. It costs more than Jannah Place and still keeps you in the Marina.", "$350–750", "Dubai"),
    ],
    itinerary=[
        day(1, "Apartment, grocery, early swim", "Learn the kitchen and the nearest sand before you plan anything else.", "Check in and shop at a Marina grocery. Breakfast tomorrow should already be in the fridge.", "A short evening walk on Marina Walk or The Walk at JBR if the heat has dropped. In summer, make it brief.", "Dinner in the apartment. The first night is not the night to queue for a restaurant with tired children.", "Ask which bedroom has the door that closes. Open-plan sleeping is not two bedrooms.", "Dubai Marina"),
        day(2, "Beach morning, mall later", "One beach, then one indoor attraction. Not five.", "JBR beach or Marina Beach as soon as you are up. Swim, leave before late morning in the hot months.", "Pool at the apartment during the hot hours. Children do not need a schedule at noon.", "A short Dubai Mall trip after 4 p.m. Choose the aquarium or a simple wander, then leave.", "The mall is 20 to 30 minutes by taxi. Do not start the visit at lunchtime in August.", "Dubai Mall"),
        day(3, "A neighborhood day", "Stay near the apartment so the kitchen and the pool get used.", "A slow morning. The Marina promenade is enough if the weather is kind. If it is not, the pool is the morning.", "Nap, laundry, a second grocery run. This is the day the apartment is for.", "If you want one outing, take a taxi to Al Bastakiya and the creek for an hour, then come home to cook.", "Do not add a water park onto this day. Aquaventure is its own full day and its own ticket.", "Al Bastakiya"),
        day(4, "One last swim, then DXB", "Leave from the Marina without a farewell theme park.", "Another early beach hour if the flight allows it. If the flight is midday, swim only if you can still make the taxi.", "Pack food for the ride if security will allow it past the hotel. Otherwise eat in the apartment.", "Taxi to DXB. From the Marina it is a long cross-town ride; leave a full hour and a half before you think you should.", "Friday departures meet weekend traffic. Add time.", "Palm Jumeirah"),
    ],
    attractions=[
        sight("Dubai Marina", "The neighborhood you are staying in: promenade, boats, and a beach nearby.", "Walk it in the morning or after 4 p.m.", "Dubai Marina"),
        sight("Jumeirah Beach", "The family swim, a taxi or a Walk away from a Marina apartment.", "Public beach rules and flags matter. Hotel or residence beaches are simpler with small children.", ""),
        sight("Dubai Mall", "One indoor visit, not the whole trip.", "Pick the aquarium or the fountain. Skip the third mall activity.", "Dubai Mall"),
        sight("Dubai Aquarium and Underwater Zoo", "The mall stop that children actually remember.", "Timed entry helps. It is inside the mall, so you are already indoors.", ""),
        sight("Palm Jumeirah", "A look from the Marina side, or a short taxi onto the Palm.", "Seeing the Palm is not the same as spending the day at Atlantis.", "Palm Jumeirah"),
        sight("Al Bastakiya", "A quiet old-Dubai hour when the Marina starts to feel like one long balcony.", "Go early. Strollers and summer noon do not mix in these lanes.", "Al Bastakiya"),
    ],
    scenic_routes=[
        route("Marina Walk to the beach", "From a Marina apartment along the promenade toward JBR and the sand. Flat, and too hot at midday in summer.", "2–4 km"),
        route("Taxi to Dubai Mall", "One planned indoor afternoon. Aquarium or fountain, then home to cook.", "20–35 minutes each way"),
        route("Creek hour", "A single abra crossing and a walk through Al Bastakiya, used as a change of scene on the rest day.", "Half a morning"),
    ],
    transport="Taxis and ride-hailing. A car seat is the reason some families rent a car; parking at the Marina and the mall is the reason not to. The tram along JBR is useful for the beach hop if you are already on it. DXB is a long taxi from the Marina.",
    food=[
        dish("Apartment breakfast", "Your kitchen", "Eggs, fruit, yogurt, bread. A konbini-style shop run the night before beats a hotel breakfast buffet you will not use."),
        dish("Pasta or rice dinner", "Your kitchen", "One pot, early. The kitchen is why you are not paying for four restaurant dinners."),
        dish("Shawarma", "A counter on The Walk at JBR", "The easy night out. Eat early with children; the Walk gets loud later."),
        dish("Grilled fish", "Bu Qtair, if you are already near Jumeirah", "Casual, messy, and better than a mall food court. Skip it if the children will not sit in the heat."),
    ],
    tips=[
        "Summer heat is the safety issue. Beach before 9 a.m., indoors or in the pool until late afternoon, no midday Marina walk in August.",
        "Atlantis has a kitchen only in the sense that a resort has room service. It is not this stay. If you want the water park, buy a day ticket and come back to the apartment.",
        "Book a two-bedroom or a large one-bedroom with a door. A studio with a kitchenette will feel like a hotel room by night two.",
        "Dubai Mall is one visit. A family trip that is only malls wastes the apartment and the beach.",
    ],
    faqs=[
        faq("Is JA Oasis Beach Tower the same as JA Ocean View?", "No. Oasis Beach Tower is the apartment building with full kitchens. JA Ocean View is a hotel of sea-view rooms, and it is not the kitchen stay."),
        faq("Can we do Atlantis for a day?", "Yes, as a ticketed day, if the children care. It does not replace the apartment, and it should not be added on top of a beach morning."),
        faq("Is the Marina beach swimmable?", "Yes, with the usual flag system. Winter is pleasant. Summer water is warm and the air is the problem."),
        faq("What does a family apartment cost?", "Jannah Place is the budget end. JA Oasis and a Grosvenor House apartment cost more and can clear $400 outside summer. The kitchen still saves meals."),
    ],
    map_places=[
        stop("Dubai Marina", "Dubai", "United Arab Emirates", "Dubai Marina"),
        stop("Palm Jumeirah", "Dubai", "United Arab Emirates", "Palm Jumeirah"),
        stop("Dubai Mall", "Dubai", "United Arab Emirates", "Dubai Mall"),
        stop("Al Bastakiya", "Dubai", "United Arab Emirates", "Al Bastakiya"),
        stop("Dubai Creek", "Dubai", "United Arab Emirates", "Dubai Creek"),
    ],
    budget_notes="Jannah Place two-bedrooms are the ones that can sit near or under $300 in quieter weeks. JA Oasis and Grosvenor House apartments are larger and often $400–700. Groceries for breakfast and two dinners change the trip's cost more than another attraction ticket. Taxis to the mall and the airport are the other line item. A water-park day is optional and not cheap.",
))

add(trip(
    slug="marrakech-with-private-pool",
    title="A pool in Marrakech: private when it is yours, small when it is the riad's",
    location="Marrakech, Morocco",
    summary=(
        "Four nights built around a real pool, with the difference said out loud. Amanjena's pool maisons have a "
        "private heated pool in a walled garden outside the medina. Le Farnatchi's pool is a shared riad pool. "
        "Royal Mansour's big garden pool is shared; a private pool there belongs only to the riads that include one."
    ),
    who="Travelers who care more about the pool than about being steps from the main square, and who will read the room category.",
    best_time="March to May, and October to November. July and August are extremely hot even with a pool. December nights are cold and a heated pool matters.",
    nights=4,
    hook="4 nights · Private pool or a real riad pool · Not a shared resort by accident",
    constraints=["Pool category must match the search", "Medina or Palmeraie, said plainly", "A plunge is small"],
    lodging="$400–2,500",
    daily="$550–2,800",
    neighborhoods=[
        stay_area("Palmeraie / Route de Ouarzazate", "Amanjena is out here, about 15 minutes from the medina. The private pools are in garden courtyards. You will take a taxi to the square."),
        stay_area("The medina", "Le Farnatchi and Royal Mansour are inside the walls. A riad pool is overlooked by the house. A true private pool is a specific suite, not the default room."),
    ],
    hotels=[
        hotel("Amanjena", "Route de Ouarzazate", "Book a Pool Pavilion or a Pool Villa. Those have a private heated pool of about 25 square metres in a walled garden. The plain Pavilion has no pool. The resort is outside the medina, beside a golf course, not in a souk.", "$1,200–3,000", "Marrakech"),
        hotel("Le Farnatchi", "Medina", "A small luxury house in the medina with a swimming pool used by the suites. It is a riad pool, pleasant and not large, and it is not private to your room. Suites look onto it. You share it.", "$400–900", "Marrakech"),
        hotel("Royal Mansour", "Medina, by the walls", "Fifty-three private riads and a large shared garden pool, Le Jardin. A private swimming pool is part of the Grand Riad and is not automatic on a Superior riad. Confirm the words 'private pool' on your category before you count on one.", "$1,500–5,000", "Marrakech"),
    ],
    itinerary=[
        day(1, "The pool, then nothing else", "Arrive and use the water you booked. The medina can wait.", "Transfer in. If you are at Amanjena, the hotel runs an airport transfer. If you are in the medina, agree the riad's meeting point outside the car-free lanes.", "Swim. A riad plunge is not a lap pool. A Pool Pavilion pool is a real swim and still private.", "Dinner at the hotel the first night. You are not going back out.", "Heated matters from November to March. Ask.", "Jemaa el-Fnaa"),
        day(2, "The square, in the morning", "One medina morning, then back to the pool before the afternoon heat.", "Jemaa el-Fnaa, the Koutoubia, and one garden or palace. Two hours in the lanes is enough.", "Return for a long swim and a rest. This is why you paid for the pool.", "Dinner in the riad or a short walk to a nearby table if you are at Le Farnatchi. From Amanjena, eat at the hotel or book a driver both ways.", "Do not plan a sunset in the medina and a swim after dark as if they were next door. From the Palmeraie they are a taxi.", "Kutubiyya Mosque"),
        day(3, "A garden that is not your pool", "One outing that is about plants and color, then your own water again.", "Jardin Majorelle and the Yves Saint Laurent museum beside it, early, with tickets.", "Back to the pool. Read, sleep, swim. A pool trip with an activity every afternoon is just a city trip that cost more.", "A hammam at the hotel if you want it. You do not need a second spa across town.", "Majorelle tickets sell out in the middle of the day. Morning is the visit.", "Majorelle Garden"),
        day(4, "A last swim", "Leave from the pool, not from a rushed souk.", "Swim. Breakfast in the garden if you are at Amanjena, or on the roof if you are at Le Farnatchi.", "A short medina walk only if your flight is late. Otherwise go to the airport.", "Menara airport is close to Amanjena and a longer exit from the deep medina. Leave the time the riad tells you, then add some.", "Cash for taxis if you are not using the hotel car.", "Bahia Palace"),
    ],
    attractions=[
        sight("Jemaa el-Fnaa", "The square. Go once, in the morning, and again at dusk only if you are already in the medina.", "Keep your phone in a pocket. Agree any photo or henna price first.", "Jemaa el-Fnaa"),
        sight("Kutubiyya Mosque", "The minaret that orients the whole city. The prayer hall is not a tourist interior.", "See it from the garden in front. Pair it with the square.", "Kutubiyya Mosque"),
        sight("Majorelle Garden", "The cobalt garden. It is the right second outing, not a second day of shopping.", "Timed tickets. Go when it opens.", "Majorelle Garden"),
        sight("Bahia Palace", "Painted ceilings and a courtyard, in the southern medina.", "A morning visit. The rooms are empty on purpose; the craft is the point.", "Bahia Palace"),
        sight("Ben Youssef Madrasa", "The theological school with the carved stucco. Cooler than the lanes.", "Combine with a short souk walk, then leave.", "Ben Youssef Madrasa"),
        sight("Saadian Tombs", "A small royal burial site beside the Kasbah mosque.", "The line is the drawback. Go early or skip it in favor of the pool.", "Saadian Tombs"),
    ],
    scenic_routes=[
        route("Medina morning loop", "Koutoubia to the edge of Jemaa el-Fnaa and back out. A taste of the lanes without a four-hour commitment.", "About 2 km, plus whatever the souk does to your sense of direction"),
        route("Majorelle by taxi", "Hotel to the garden and straight back. Do not walk it from a deep-medina riad in July.", "15–25 minutes each way"),
        route("Roof at sunset", "If your riad has a roof, that is the scenic route. The Atlas sits on the horizon on a clear day. It is not the sea.", "The stairs"),
    ],
    transport="Taxis and hotel cars. The medina is mostly closed to cars; your riad will meet you at a gate. Amanjena is a transfer every time you want the square. Do not drive yourself in the medina.",
    food=[
        dish("Tagine", "Your riad, or a small restaurant just outside the main square", "Chicken with lemon, or lamb with prune. One tagine feeds two."),
        dish("Breakfast of msemen and orange juice", "The riad roof", "Flat griddled bread, honey, and the orange juice Marrakech actually does well."),
        dish("Couscous", "Friday lunch at the riad if they serve it", "The weekly dish. Eat it at midday, not as a midnight snack."),
        dish("Grilled brochettes", "A simple grill on the way back from the square", "Meat on skewers. A lighter dinner than a banquet on the night you also want to swim."),
    ],
    tips=[
        "The room name is the product. 'Pool Pavilion' has a private pool. 'Pavilion' does not. 'Riad pool' means the house shares it.",
        "A medina plunge pool is small. If you want to swim laps, you want Amanjena's pool category or Royal Mansour's big shared garden pool, and those are different promises.",
        "July and August afternoons are for the water and a dark room. Do not schedule the souks at 3 p.m.",
        "Royal Mansour's Le Jardin pool is beautiful and shared. Do not describe it as private.",
    ],
    faqs=[
        faq("Does every Royal Mansour riad have a private pool?", "No. The estate has a large shared pool. A private pool is a feature of specific riads, including the Grand Riad. Make the confirmation say so."),
        faq("Is Le Farnatchi's pool private?", "No. It is the hotel's pool, shared by the suites. It is still a real riad pool, not a resort lagoon."),
        faq("Can I walk to the souks from Amanjena?", "Not usefully. It is outside the walls, about 15 minutes by car. Budget the transfers or stay in the medina."),
        faq("Is this an ocean trip?", "No. Marrakech is inland. The water is a pool. The Atlantic version of this search is Essaouira."),
    ],
    map_places=[
        stop("Jemaa el-Fnaa", "Marrakech", "Morocco", "Jemaa el-Fnaa"),
        stop("Kutubiyya Mosque", "Marrakech", "Morocco", "Kutubiyya Mosque"),
        stop("Majorelle Garden", "Marrakech", "Morocco", "Majorelle Garden"),
        stop("Bahia Palace", "Marrakech", "Morocco", "Bahia Palace"),
        stop("Ben Youssef Madrasa", "Marrakech", "Morocco", "Ben Youssef Madrasa"),
    ],
    budget_notes="These are not the cheap riads. Le Farnatchi is the lower end of this list and still a luxury medina hotel. Amanjena's pool categories and Royal Mansour are several times a normal riad rate. Taxis are minor next to the room. Eat at the hotel more often than not; the pool is the luxury you came for.",
))

add(trip(
    slug="marrakech-2-bedroom-under-400night",
    title="Two bedrooms in a Marrakech riad, under $400 outside the holidays",
    location="Marrakech, Morocco",
    summary=(
        "Four nights in a real medina riad with two sleeping rooms, at a rate that usually sits under $400. "
        "That price is normal in late spring, summer, and much of the autumn, and it fails at Christmas, New Year, "
        "and Easter. These are not El Fenn's grand suites. A standard double is not a two-bedroom."
    ),
    who="Two couples, or a family, who want two rooms and a courtyard and do not need a palace suite.",
    best_time="March to May and September to early November for weather and a rate that can still fit. Summer is cheaper and very hot. Avoid the last two weeks of December.",
    nights=4,
    hook="4 nights · Two-bedroom riad · Usually under $400 except holidays",
    constraints=["Two bedrooms, not a sofa in the salon", "Under $400 outside peak holidays", "Medina riads, not a Palmeraie villa"],
    lodging="$140–400",
    daily="$220–420",
    neighborhoods=[
        stay_area("Mouassine and the northern medina", "Riad streets with a door on a lane. You walk to the square in 10 to 20 minutes if you know the way, longer if you do not."),
        stay_area("Bab Doukkala side", "Slightly calmer edges of the medina, still walkable to the sights, easier for a taxi drop at a gate."),
    ],
    hotels=[
        hotel("Riad Kniza", "Medina", "A long-running family riad with antiques and suites. Ask for a suite with two sleeping rooms. A double room does not satisfy the search, and Christmas week will not stay under $400.", "$160–380", "Marrakech"),
        hotel("Maison Arabe", "Medina", "A larger riad-hotel with a shared pool and suites. Book the two-room suite if you need two bedrooms. Summer is when this budget is comfortable. Easter and late December are not.", "$180–400", "Marrakech"),
        hotel("Riad L'Orangeraie", "Mouassine", "A smaller medina riad with a shared courtyard pool. Two-room stays often land under $400 outside peak weeks. Confirm the second room is a bedroom with a door, not a sitting alcove.", "$140–320", "Marrakech"),
    ],
    itinerary=[
        day(1, "Find the door", "The arrival is a taxi to a medina gate and a walk, or a porter with a cart.", "Let the riad send someone to the nearest car access. Do not hunt the lane with four suitcases at dusk.", "Settle both rooms, then walk to Jemaa el-Fnaa while it is still light so the way back is familiar.", "Dinner on the roof or a simple grill nearby. The square's food stalls are optional, not required.", "Save the riad's pin and a phone number before you go out.", "Jemaa el-Fnaa"),
        day(2, "Palaces, slowly", "Two historic houses, not six.", "Bahia Palace in the morning.", "El Badi Palace, which is a ruin of a courtyard and storks, then back to the riad for the hot part of the day.", "Cook or eat in. A two-bedroom riad is also a place to have breakfast supplies and fruit.", "Both palaces are in the southern medina. Do them together and then stop.", "Bahia Palace"),
        day(3, "The garden", "Majorelle, then a free afternoon.", "Taxi to Majorelle Garden at opening.", "Back for a swim if your riad has a pool. Maison Arabe and L'Orangeraie do; it is shared and small. Riad Kniza's water is not the point of the stay.", "The spice square and a mint tea, or a quiet night in. You do not need a show.", "The garden is outside the medina walls. Use a taxi both ways.", "Majorelle Garden"),
        day(4, "A last lane, then the airport", "One more walk, then leave on time.", "Ben Youssef Madrasa if you want one more interior. Otherwise the roof and a slow pack.", "Head for the gate your driver names. Menara is not far, and medina exits still take longer than the map.", "Eat before you go. The airport is not the meal.", "Friday departure meets more medina foot traffic. Add time.", "Ben Youssef Madrasa"),
    ],
    attractions=[
        sight("Jemaa el-Fnaa", "The orientation point. See it once by day and once at dusk.", "Agree prices. The stalls are a circus and a food market at the same time.", "Jemaa el-Fnaa"),
        sight("Bahia Palace", "The 19th-century palace with the painted ceilings.", "Morning light is kinder, and the rooms are cooler then.", "Bahia Palace"),
        sight("El Badi Palace", "A ruined palace. The scale is the sight.", "There is little shade. Do not linger at noon in summer.", "El Badi Palace"),
        sight("Majorelle Garden", "The blue garden, a taxi from the riad.", "Tickets are timed. Buy them before you get in the taxi.", "Majorelle Garden"),
        sight("Ben Youssef Madrasa", "Carved cedar and stucco around a courtyard.", "It pairs with a short walk in the souk, then home.", "Ben Youssef Madrasa"),
        sight("Kutubiyya Mosque", "The city's landmark minaret, seen from the plaza in front.", "You are not going inside for a tour.", "Kutubiyya Mosque"),
    ],
    scenic_routes=[
        route("Riad to the square", "The walk you will repeat. Do it in daylight the first time and learn two landmarks on the way.", "10–20 minutes once you know it"),
        route("Bahia to El Badi", "A short southern-medina link between the two palaces. Do both, then leave.", "About 15 minutes on foot"),
        route("Taxi to Majorelle", "Out through a medina gate and across to the garden. The scenic part is the garden, not the ride.", "15–25 minutes"),
    ],
    transport="Walk in the medina, taxi outside it. Have the riad book airport cars. A rental car is a burden. Petite taxis outside the walls should use the meter; agree a price only if the meter will not be used.",
    food=[
        dish("Tagine", "The riad, or a neighborhood restaurant your host names", "Lemon chicken or kefta. Eat on the roof when it is not too hot to sit there."),
        dish("Msemen", "Breakfast at the riad", "The right breakfast. You do not need a cafe pilgrimage for it."),
        dish("Brochettes and salad", "A grill within a short walk", "The inexpensive dinner that keeps the $400 room honest."),
        dish("Orange juice and dates", "A stall at Jemaa el-Fnaa", "Buy the juice from the row of stalls and watch it being squeezed. One glass."),
    ],
    tips=[
        "Write 'two bedrooms' into the confirmation. A suite with a salon and one bed is not the room.",
        "Under $400 is common except Christmas, New Year, and Easter. If your dates are those weeks, change dates or change cities. Do not expect El Fenn's best suite at this number.",
        "Summer is the bargain and the heat. A pool helps, and a pool at these riads is shared and small.",
        "Both bedrooms should have a fan or air-conditioning that you have asked about. Some beautiful rooms are hotter than the listing photos.",
    ],
    faqs=[
        faq("Is a whole riad under $400 realistic?", "A small two-bedroom house, yes, outside holidays. A staffed palace with a private pool, no."),
        faq("Do these riads have private pools?", "No. If there is a pool, the house shares it. The private-pool trip is a different page and a different budget."),
        faq("Can four adults sleep comfortably?", "Only in a true two-bedroom. Ask who sleeps in which room and whether the second room has a window."),
        faq("How do we find the door at night?", "You do not. The riad meets you at a gate. Arrange it before the flight lands."),
    ],
    map_places=[
        stop("Jemaa el-Fnaa", "Marrakech", "Morocco", "Jemaa el-Fnaa"),
        stop("Bahia Palace", "Marrakech", "Morocco", "Bahia Palace"),
        stop("El Badi Palace", "Marrakech", "Morocco", "El Badi Palace"),
        stop("Majorelle Garden", "Marrakech", "Morocco", "Majorelle Garden"),
        stop("Ben Youssef Madrasa", "Marrakech", "Morocco", "Ben Youssef Madrasa"),
    ],
    budget_notes="A real two-bedroom riad is often $150–300 a night in summer and shoulder season, and $350–500 or more at Christmas. Food can stay at $40–70 a day if you eat breakfast at the riad and alternate tagines with simple grills. Majorelle and the palaces are small ticket prices next to the room. Airport transfers are worth booking through the riad.",
))

add(trip(
    slug="marrakech-near-the-beach-under-300",
    title="Marrakech has no beach: stay in Essaouira under $300",
    location="Essaouira, Morocco",
    summary=(
        "Marrakech is inland. The beach Moroccans pair with it is Essaouira, about three hours west on the Atlantic. "
        "This is four nights on that coast for under $300 a night, with a real stop in Marrakech on the way in. "
        "Heure Bleue is the palace that usually breaks the cap, so it is not one of the hotels."
    ),
    who="People who searched for a Marrakech beach and would rather have the Atlantic than a story about one.",
    best_time="May to October for swimming weather, with wind most afternoons. Essaouira is cooler than Marrakech in summer, which is the point. Winter is bright, windy, and not a swim.",
    nights=4,
    hook="4 nights · Essaouira on purpose · Under $300, plus a Marrakech stop",
    constraints=["The beach is Essaouira", "Under $300 for the coast hotel", "One Marrakech day, not a fake ocean in the medina"],
    lodging="$90–280",
    daily="$160–320",
    neighborhoods=[
        stay_area("Essaouira medina", "Ryad Watier and Villa Maroc are inside the walls, a short walk to the ramparts and the town beach. You hear gulls and wind, not Jemaa el-Fnaa."),
        stay_area("The beach south of the medina", "Sofitel Essaouira Beach & Spa is on the sand. The medina is a walk or a short taxi. This is the Atlantic, and it is often windy after lunch."),
    ],
    hotels=[
        hotel("Ryad Watier", "Essaouira medina", "A small medina riad. The family suite is the two-bedroom, recently offered from about €150 with breakfast, under $300. Doubles start lower. The beach is a walk, not a private strand.", "$80–220", "Essaouira"),
        hotel("Villa Maroc", "Essaouira kasbah", "The long-running kasbah hotel by the ramparts. A double room is the under-$300 product. A sea-view suite on a package rate can cross $300, so book the room that matches the cap. There is no pool.", "$100–280", "Essaouira"),
        hotel("Sofitel Essaouira Beach & Spa", "Essaouira beach", "On the Atlantic, reopened in November 2026 after a renovation. A superior room was listed near €170 on a December night, which is under $300. August and holidays will not match that sample. Heure Bleue usually sits over this budget.", "$160–320", "Essaouira"),
    ],
    itinerary=[
        day(1, "Land in Marrakech, sleep on the coast", "The Marrakech airport is the gateway. The beach is not in that city.", "Land at Marrakech Menara. If the flight is early, walk Jemaa el-Fnaa and the Koutoubia for two hours with your bag in a car, then leave.", "Drive to Essaouira, about three hours. Stop only if you need to. The road is the trip.", "Arrive to the ramparts at dusk. Eat grilled fish. You are done.", "A private car is the calm version. The bus is cheaper and eats the afternoon. Do not try to day-trip this.", "Jemaa el-Fnaa"),
        day(2, "The medina and the port", "Essaouira is a walkable town. Use that.", "Skala de la Ville and the port. Watch the boats and the gulls. The blue boats are the sight.", "The town beach if the wind allows. Afternoon wind is normal. A walk on the sand can be a lean into the breeze, not a sunbath.", "Dinner in the medina. Sardines, not a tagine banquet, unless you want one.", "Shoes matter on the rampart stones. The wind makes hats a comic exercise.", "Essaouira"),
        day(3, "A beach day that is actually a beach", "Stay on the water. Marrakech is not today's problem.", "Morning swim or a long walk south along the beach. The water is the Atlantic and it is cool.", "A quiet afternoon. If you are at the Sofitel, the pool is the windbreak. If you are in the medina, a courtyard is.", "Sunset on the ramparts, then dinner. One seafood meal is enough for the day if lunch was a picnic.", "Sunscreen and a layer. The light is strong and the air is not Marrakech-hot.", "Essaouira"),
        day(4, "Back via Marrakech airport", "Leave time for the three-hour return. A second medina visit only fits an evening flight.", "Breakfast, a last walk to the port, checkout.", "Drive to Menara. If the flight is late, you may have an hour for the Majorelle Garden with a taxi from the airport road. If it is not, go straight to the terminal.", "Eat before security. Do not depend on a connection that assumes Marrakech traffic will behave.", "Friday and Sunday roads are busier. Tell the driver your flight time, not a vibe.", "Majorelle Garden"),
    ],
    attractions=[
        sight("Essaouira medina", "The walled town, a UNESCO site you can walk across in a morning.", "The main square, the fish grills, and the ramparts are the whole idea.", "Essaouira"),
        sight("Essaouira port", "Working boats, blue paint, and the gulls. The honest coastal scene.", "Mornings are when the catch is in. Afternoons are windier.", ""),
        sight("The Atlantic beach", "The answer to the Marrakech beach search.", "Swim in the morning. The wind usually rises after lunch.", ""),
        sight("Jemaa el-Fnaa", "The Marrakech stop on the way in, not the base.", "Two hours is a visit. A week is a different trip.", "Jemaa el-Fnaa"),
        sight("Kutubiyya Mosque", "What you can see in that same short Marrakech window.", "From the square in front. Then get in the car.", "Kutubiyya Mosque"),
        sight("Majorelle Garden", "Only if the return flight is late enough for a taxi from the airport road.", "Do not miss a flight for a garden. Skip it cleanly if the timing is tight.", "Majorelle Garden"),
    ],
    scenic_routes=[
        route("Marrakech to Essaouira", "The three-hour drive west. Atlas foothills, then argan country, then the Atlantic. This is the scenic route that makes the search true.", "About 2.5–3.5 hours by car"),
        route("Ramparts walk", "From the Skala along the sea wall to the port. Wind, cannons, and the color of the doors.", "About 2 km"),
        route("Beach walk south", "From the town beach toward the bigger sand in front of the resort strip. Turn around when you have had enough wind.", "An hour out and back"),
    ],
    transport="A private car or a shared transfer between Marrakech airport and Essaouira is the spine of the trip. Inside Essaouira, walk. The medina is small. A taxi is for the beach hotel if you do not want the wind in your face with luggage. Do not rent a car unless you want it for the drive itself.",
    food=[
        dish("Grilled sardines", "The port stalls in Essaouira", "The meal the town is for. A plate of fish, bread, and salad, eaten near the boats."),
        dish("Seafood pastilla", "A medina restaurant, one night", "A sweet-savory pie. Share it. It is richer than the grilled fish."),
        dish("Mint tea and a pastry", "A rampart cafe", "The windy-afternoon version of a meal. Sit inside the glass if the sand is blowing."),
        dish("Tagine, once", "The Marrakech stop, or your first Essaouira night", "You can eat a tagine by the ocean. You do not need one at every meal just because you landed in Morocco."),
    ],
    tips=[
        "Marrakech is not on the sea. Anyone selling a medina room as an ocean view is wrong. Essaouira is the correction.",
        "Under $300 holds at Ryad Watier and at a Villa Maroc double. It holds at the Sofitel on ordinary dates and fails in peak August and on holiday weeks. Heure Bleue is the one to stop expecting.",
        "The wind is part of the place. A calm postcard morning can be a difficult beach afternoon. Bring a layer.",
        "The Marrakech piece is a stop, not a second base. Sleeping in both cities for one night each wastes the beach.",
    ],
    faqs=[
        faq("Can I day-trip Essaouira from Marrakech?", "You can, and you will spend six hours in a car for a short walk. This trip stays on the coast instead."),
        faq("Is the Sofitel under $300?", "A published December night was about €170. That is under $300. Do not treat it as the August rate. Check your dates."),
        faq("Where do I sleep in Marrakech?", "You mostly do not. Day one uses the airport and, if the clock allows, the square, then continues to Essaouira. The hotels on this page are the coast."),
        faq("Is the water warm?", "It is the Atlantic. Cool in summer, cold in winter. The pool at the Sofitel is the warm swim. The medina riads on this list do not have one."),
    ],
    map_places=[
        stop("Essaouira", "Essaouira", "Morocco", "Essaouira"),
        stop("Jemaa el-Fnaa", "Marrakech", "Morocco", "Jemaa el-Fnaa"),
        stop("Kutubiyya Mosque", "Marrakech", "Morocco", "Kutubiyya Mosque"),
        stop("Majorelle Garden", "Marrakech", "Morocco", "Majorelle Garden"),
        stop("Bahia Palace", "Marrakech", "Morocco", "Bahia Palace"),
    ],
    budget_notes="A medina double in Essaouira is often $90–180. The Sofitel can sit under $300 outside peak and over it in August. The private transfer each way is the extra cost that makes the trip work, often more than a night in a cheap riad. Fish dinners are inexpensive. Heure Bleue is omitted because it usually misses the cap.",
))

add(trip(
    slug="marrakech-luxury-with-ocean-view",
    title="Marrakech luxury, honestly: gardens and the Atlas, not the ocean",
    location="Marrakech, Morocco",
    summary=(
        "Four nights of real Marrakech luxury at La Mamounia, Royal Mansour, and El Fenn. The city is inland. "
        "The famous water is a pool, and the horizon on a clear day is the Atlas, not the Atlantic. "
        "If the search was for the ocean, the honest version is Essaouira, three hours west, and this is not that trip."
    ),
    who="Travelers who want the best of Marrakech and will not be talked into calling a fountain the sea.",
    best_time="March to May, and late September to November. Summer is too hot for a garden city to feel luxurious at midday. Winter nights are cold and the hotels are at their best indoors.",
    nights=4,
    hook="4 nights · Medina luxury · Atlas on the horizon, no ocean",
    constraints=["No ocean claim", "The pools are pools", "Essaouira is the other trip"],
    lodging="$500–2,500",
    daily="$700–2,800",
    neighborhoods=[
        stay_area("The medina and its edge", "La Mamounia sits by the walls, Royal Mansour just inside them, El Fenn deeper in the lanes. All three are Marrakech, none of them is a coast."),
        stay_area("Essaouira, if you actually wanted the sea", "A different hotel and a three-hour drive. Do that trip on its own page. Do not spend a luxury Marrakech night chasing a rumor of a beach."),
    ],
    hotels=[
        hotel("La Mamounia", "Beside the medina walls", "Gardens, a celebrated pool that is shared by the hotel, and the Atlas in the distance on a clear day. There is no ocean view because there is no ocean. Book it for the garden and the building.", "$600–1,500", "Marrakech"),
        hotel("Royal Mansour", "Medina", "Private riads, extraordinary craft, and a large shared garden pool. Some top riads have a private pool. None of them faces the sea. The light at the end of the view is the mountains.", "$1,500–5,000", "Marrakech"),
        hotel("El Fenn", "Medina", "Rooftops over the lanes and three shared pools, with the Atlas behind them on a clear afternoon. The pools are the hotel's, for guests, and they are not the Atlantic.", "$400–900", "Marrakech"),
    ],
    itinerary=[
        day(1, "Arrive and look at the right horizon", "See what the view actually is, from the roof or the garden.", "Transfer in and have the hotel meet you at the medina gate if needed.", "A swim in the hotel pool, which is the water this trip has.", "Dinner at the hotel. Look south. If the air is clear, that line of mountains is the High Atlas.", "Haze hides the Atlas on many afternoons. You may get the mountains at dawn and not at tea time.", "Atlas Mountains"),
        day(2, "The medina, edited", "Three stops, then back to the garden.", "Koutoubia and a controlled walk to Jemaa el-Fnaa. You are allowed to leave when it gets tiring.", "Ben Youssef Madrasa, then the hotel pool.", "A reserved dinner, either in the hotel or somewhere your concierge will send a car for.", "Luxury in the medina is also knowing when to stop walking.", "Ben Youssef Madrasa"),
        day(3, "Palaces and a garden", "The historic interiors, and Majorelle, without turning it into a march.", "Bahia Palace early.", "Majorelle Garden with tickets already in hand. The museum next door is small and worth it if you care about Saint Laurent. Then stop.", "Rooftop or garden at your hotel for the evening. You have already been out.", "Do not add the souks as a third full event. Buy one thing or buy nothing.", "Bahia Palace"),
        day(4, "The garden, then the plane", "A last morning in the hotel's own grounds.", "Breakfast in the garden at La Mamounia, in the riad at Royal Mansour, or on the roof at El Fenn. Swim if there is time.", "Leave for Menara. The airport is close to the city and the medina exit is the part that takes time.", "You are not detouring to Essaouira today. That is a different itinerary.", "If the Atlas is clear at breakfast, that is the view to remember. It still is not the sea.", "Jemaa el-Fnaa"),
    ],
    attractions=[
        sight("Jemaa el-Fnaa", "The square, seen once with a plan to leave.", "Dusk is the spectacle. You do not have to eat there.", "Jemaa el-Fnaa"),
        sight("Kutubiyya Mosque", "The minaret beside the hotel belt.", "The plaza in front is the view. The interior is a mosque, not a museum.", "Kutubiyya Mosque"),
        sight("Bahia Palace", "The finest painted palace interior most visitors will enter.", "Go at opening. The courtyards are the rooms that matter.", "Bahia Palace"),
        sight("Majorelle Garden", "A designed garden, a useful contrast to the medina dust.", "Timed entry. Pair it with the small museum or with nothing else.", "Majorelle Garden"),
        sight("Ben Youssef Madrasa", "The carved courtyard in the northern medina.", "It is quiet compared with the souk around it. Use that.", "Ben Youssef Madrasa"),
        sight("Atlas Mountains", "The real horizon. Snow in winter, haze in summer, never a bay.", "You see them from a roof. You do not need a day trip unless you want one.", "Atlas Mountains"),
    ],
    scenic_routes=[
        route("Roof line toward the Atlas", "From El Fenn's roof, La Mamounia's garden edge, or a Royal Mansour terrace, looking south. Mountains, palm, and ochre walls.", "Stay put"),
        route("Koutoubia to the square", "A short, straight walk that shows you the medina's front door without a souk spiral.", "20 minutes"),
        route("The road you are not taking", "Essaouira is three hours west if the ocean is non-negotiable. It does not fit beside this hotel stay. Know that, and stay.", "About 3 hours, another trip"),
    ],
    transport="Hotel cars and taxis to the gates. Walk only the walks you mean to walk. A rental car spends its time parked outside the medina. Menara airport is the flight.",
    food=[
        dish("Hotel breakfast", "La Mamounia, Royal Mansour, or El Fenn", "You are paying for it. Eat the fruit, the bread, and the coffee before you go anywhere."),
        dish("Couscous or tagine", "The hotel, one lunch", "Have the formal version once. It will be better than a random square stall and you can sit down."),
        dish("A serious dinner", "The hotel restaurant, booked", "This is a luxury stay. One reserved dinner beats four indecisive nights in the medina."),
        dish("Orange juice", "Jemaa el-Fnaa, on the single visit", "The thing worth buying in the square. Drink it there."),
    ],
    tips=[
        "There is no ocean view in the Marrakech medina. The Atlas is the view. Pools are pools.",
        "La Mamounia's famous pool is shared. El Fenn's three pools are shared. Say that, and they are still wonderful.",
        "Essaouira is the Atlantic trip. Combining it with four luxury nights in Marrakech means a lot of driving and a weaker version of both.",
        "Book dinner and the Majorelle time before you book a souk guide. The guide is optional. The timing is not.",
    ],
    faqs=[
        faq("Which room faces the ocean?", "None. Anyone who offers one is describing a pool, a fountain, or a picture."),
        faq("Can I see the sea from a balloon?", "A balloon ride, if you take one, looks at the desert edge and the Atlas. It does not create a coastline."),
        faq("Is Royal Mansour in the medina?", "Yes, in a walled estate by the medina. You are in Marrakech. You are not at the beach."),
        faq("What should I book if I need the Atlantic?", "Essaouira, on the beach page. Heure Bleue if money is no object, or the under-$300 hotels if it is."),
    ],
    map_places=[
        stop("Jemaa el-Fnaa", "Marrakech", "Morocco", "Jemaa el-Fnaa"),
        stop("Kutubiyya Mosque", "Marrakech", "Morocco", "Kutubiyya Mosque"),
        stop("Bahia Palace", "Marrakech", "Morocco", "Bahia Palace"),
        stop("Majorelle Garden", "Marrakech", "Morocco", "Majorelle Garden"),
        stop("Atlas Mountains", "Morocco", "Morocco", "Atlas Mountains"),
    ],
    budget_notes="The room is a luxury purchase: several hundred dollars at El Fenn, more at La Mamounia, and much more at Royal Mansour. Meals in-house are the next cost and are worth it on a short stay. Taxis are trivial. There is no beach club to buy because there is no beach.",
))

add(trip(
    slug="tokyo-family-friendly-with-kitchen",
    title="Tokyo with a kitchen: apartments, teamLab, and a real neighborhood",
    location="Tokyo, Japan",
    summary=(
        "Four nights in a Tokyo apartment hotel with a kitchen, so breakfast can be a convenience-store run and dinner "
        "does not have to be a restaurant every night. The days include teamLab and a neighborhood walk in Yanaka or "
        "Shimokitazawa, not a loop that only crosses Shibuya scramble. IC cards and konbini meals are part of the plan."
    ),
    who="Parents with children who want a hob, a table, and a city plan that is not four malls.",
    best_time="Late March to May for blossom, and October to November for clear days. Summer is humid. New Year week is a different city, with many shops closed.",
    nights=4,
    hook="4 nights · Apartment kitchen · Yanaka or Shimokitazawa, not only Shibuya",
    constraints=["Kitchen in the room", "One neighborhood day", "Trains, not a car"],
    lodging="$180–450",
    daily="$280–480",
    neighborhoods=[
        stay_area("Nishi-Shinjuku", "MIMARU and the Shinjuku apartments put you on the west side, with trains everywhere and a kitchen when the children are done."),
        stay_area("Roppongi / Tokyo Midtown", "Oakwood Premier is the pricier, fuller kitchen, attached to a station and a complex. Useful, not cute."),
    ],
    hotels=[
        hotel("MIMARU Tokyo Shinjuku West", "Nishi-Shinjuku", "Apartment rooms with a real kitchen: hob, pots, fridge, microwave. Family rooms with bunks. Laundry is a coin machine in the building, not a washer in every room.", "$160–320", "Tokyo"),
        hotel("Citadines Shinjuku Tokyo", "Shinjuku", "Serviced apartments with kitchens, a short walk from Shinjuku-gyoemmae Station. Book a larger layout if you are four. The small rooms are a poor fit for a family.", "$180–360", "Tokyo"),
        hotel("Oakwood Premier Tokyo Midtown", "Roppongi, Tokyo Midtown", "Full kitchens and a washer-dryer in the apartment. The expensive one, and the easiest if you want Midtown, Roppongi Station, and space for a longer stay.", "$280–550", "Tokyo"),
    ],
    itinerary=[
        day(1, "Cards, konbini, kitchen", "Learn the train and the grocery before you learn a skyline.", "Get a Suica or Pasmo, including a child's card if you need one. The airport train is the first use.", "Check in, then a konbini or a small supermarket. Eggs, rice, fruit, yogurt. Breakfast tomorrow is solved.", "A short walk near the hotel. Shinjuku at night is a lot. The apartment is the right dinner.", "7-Eleven, Lawson, and FamilyMart are legitimate meals. Rice balls, sandwiches, and bananas are fine with children.", "Shinjuku Gyo-en"),
        day(2, "teamLab, with tickets", "One immersive museum, booked ahead, then a normal afternoon.", "teamLab Planets in Toyosu, at your timed entry. It is wet in places. Bring clothes you can roll up.", "Back to the apartment to change and eat something you bought on the way. Do not add a second museum.", "If everyone still has energy, an early ramen near the hotel. If not, cook noodles in the room. Both count.", "Planets tickets go. Without them, do Ueno Park and skip the scramble to a box office.", ""),
        day(3, "A neighborhood that is not a crossing", "Yanaka or Shimokitazawa. Pick one.", "Yanaka Cemetery and the shopping street, or Shimokitazawa's lanes and record shops. Let the children set the pace.", "A park stop and a bakery. This day has no skyline assignment.", "Cook a real dinner. The kitchen is the luxury on a day you walked.", "Shibuya Crossing can be a ten-minute look on the way home. It is not the day.", "Yanaka, Tokyo"),
        day(4, "Meiji Shrine, then the train", "A last green morning and a departure that is not a panic.", "Meiji Shrine and the gravel paths. It is free, and it is the right scale for a last morning.", "A konbini lunch for the train. Pack the kitchen things you bought and leave the rest.", "Narita or Haneda. The IC card still works on the airport train. Leave more time than the timetable's best case.", "Do not plan Shinjuku Gyoen and Meiji and a shopping street on the morning you fly.", "Meiji Shrine"),
    ],
    attractions=[
        sight("Meiji Shrine", "A forest in the city. Free, gravel underfoot, and calm if you go early.", "The inner garden is the paid part. The main shrine walk is enough.", "Meiji Shrine"),
        sight("Shinjuku Gyo-en", "The other great garden, a separate morning from the shrine.", "It closes earlier than you think. Check the day before.", "Shinjuku Gyo-en"),
        sight("Yanaka", "A low neighborhood of temples, a cemetery, and a shopping street.", "This is the day that is not Shibuya. Stay for a snack and leave.", "Yanaka, Tokyo"),
        sight("Shimokitazawa", "Small streets, shops, and a scale children can handle.", "Pick this or Yanaka, not both, unless you enjoy trains more than the places.", "Shimokitazawa"),
        sight("teamLab Planets", "The booked, barefoot, sometimes-wet museum in Toyosu.", "Timed tickets. Bring a change of socks.", ""),
        sight("Ueno Park", "The backup green space and museum park if teamLab is sold out.", "You do not have to enter a museum to use the park.", "Ueno Park"),
    ],
    scenic_routes=[
        route("Meiji forest walk", "From Harajuku into the shrine grounds and back out a different gate. Gravel, trees, and a break from intersections.", "About 2 km"),
        route("Yanaka Ginza stroll", "The shopping street and the cemetery edge. No viewpoint, which is the appeal.", "A slow hour"),
        route("Yamanote to Toyosu", "The train sequence to teamLab Planets. It is a route with a purpose, and the IC card is how you pay.", "About 40 minutes from Shinjuku"),
    ],
    transport="Trains and the subway. Buy IC cards at the airport and use them for trains, subways, and convenience stores. Children old enough to walk a ticket gate need to know the drill; small children ride with you. A car is the wrong tool. Narita and Haneda both have direct trains.",
    food=[
        dish("Onigiri and an egg sandwich", "Any konbini", "A real breakfast with children. Eat some of it in the apartment so you are not picnicking on a train floor."),
        dish("Instant or fresh noodles at home", "The apartment kitchen", "Boil water. Add what you bought at the supermarket. This is allowed."),
        dish("Ramen", "A neighborhood shop near Shinjuku or Roppongi, early", "One restaurant meal. Go at 6 p.m., not at 8, if you are with children."),
        dish("Tonkatsu", "A simple set-meal restaurant, one night", "A cutlet and rice is the dinner everyone will finish. Chain or independent, both are fine."),
    ],
    tips=[
        "A konbini breakfast is legitimate. Do not force a hotel buffet onto a trip that has a kitchen.",
        "Get IC cards before you need them. Cash still matters for some small restaurants.",
        "teamLab is one outing with tickets. A neighborhood is the other. Shibuya Crossing is optional scenery.",
        "Apartment kitchens in Tokyo are small. A hob and a pot are enough. Do not expect an oven.",
    ],
    faqs=[
        faq("Do all the rooms have a kitchen?", "MIMARU's rooms do. Citadines Shinjuku's apartments do. Oakwood's apartments do. A standard hotel room elsewhere does not. Book the apartment category."),
        faq("Is teamLab Borderless the same as Planets?", "No. This plan uses Planets in Toyosu because the visit is concrete. Check which one is open and which you actually hold tickets for."),
        faq("Can we do Disneyland too?", "Not on these four days without deleting the neighborhood and exhausting everyone. That is a separate trip."),
        faq("What does the apartment cost?", "MIMARU and Citadines are often $180–350 for a family layout. Oakwood Midtown is more. The kitchen saves a breakfast and at least one dinner a day."),
    ],
    map_places=[
        stop("Meiji Shrine", "Tokyo", "Japan", "Meiji Shrine"),
        stop("Shinjuku Gyo-en", "Tokyo", "Japan", "Shinjuku Gyo-en"),
        stop("Yanaka", "Tokyo", "Japan", "Yanaka, Tokyo"),
        stop("Shimokitazawa", "Tokyo", "Japan", "Shimokitazawa"),
        stop("Ueno Park", "Tokyo", "Japan", "Ueno Park"),
    ],
    budget_notes="Budget the apartment first. A family room with a kitchen is often $200–400, more at Oakwood. Konbini breakfasts and one cooked dinner keep food near $40–70 a person a day if you are careful, more if every meal is a restaurant. teamLab tickets are the planned extra. Trains are cheap next to a taxi habit.",
))

add(trip(
    slug="tokyo-mountain-or-nature-view",
    title="Tokyo nature, honestly: a garden in the city and a night in Hakone",
    location="Tokyo, Japan",
    summary=(
        "Four nights that do not pretend a Shinjuku hotel faces Mount Fuji. Two or three nights are in Tokyo, at a "
        "hotel by the Imperial Palace moat or in the Chinzanso garden, and one night is at Gora Kadan in Hakone. "
        "Fuji is often in cloud. Hakone's view is the hills, and the city's nature is Meiji Shrine and Shinjuku Gyo-en."
    ),
    who="Travelers who want trees, water, and a ryokan night, and who will not pay extra for a Fuji view that is not there.",
    best_time="Late October to November for clear air, and late March to April for blossom. Fuji is a winter-morning rumor even then. June is rain. August is humid.",
    nights=4,
    hook="4 nights · Hakone ryokan plus Tokyo gardens · Fuji not promised",
    constraints=["No fake Fuji-view Shinjuku room", "One Hakone night", "Clouds are the normal Fuji forecast"],
    lodging="$300–900",
    daily="$450–1,100",
    neighborhoods=[
        stay_area("Marunouchi", "Palace Hotel Tokyo faces the palace moat and gardens. That is a real green view in the city, and it is not a mountain."),
        stay_area("Gora, Hakone", "Gora Kadan is a hillside ryokan a few minutes from Gora Station. You are here for one night, for the bath and the hills, not for a guaranteed volcano."),
    ],
    hotels=[
        hotel("Gora Kadan", "Gora, Hakone", "A real Hakone ryokan on the former grounds of an imperial villa. Kaiseki, a shared grand bath, and private open-air baths only in select rooms. The view is Hakone's hills. Fuji is not the product. Rates are per person and include meals.", "$500–1,200 per person", "Hakone"),
        hotel("Palace Hotel Tokyo", "Marunouchi", "Beside the Imperial Palace moat. Many rooms look at water and pine, which is the honest city version of a nature view. Use it for the Tokyo nights of this split stay.", "$400–800", "Tokyo"),
        hotel("Hotel Chinzanso Tokyo", "Mejiro", "A large historic garden in the city, with the hotel set in it. Choose this instead of Hakone only if you do not want to change hotels. It is a garden, not a Fuji lookout.", "$300–700", "Tokyo"),
    ],
    itinerary=[
        day(1, "The city's own forest", "Stay in Tokyo and use the parks, which do not depend on the weather over Fuji.", "Meiji Shrine in the morning, before the wedding groups fill the path.", "Shinjuku Gyo-en in the afternoon. Two gardens in one day is the right amount of nature without a train to the mountains.", "Dinner near the hotel. If you are at the Palace Hotel, the lights on the moat are the evening view.", "Gyo-en has opening hours and a closing time. Do not arrive at 4 p.m. and expect a long wander.", "Meiji Shrine"),
        day(2, "To Hakone, without a Fuji promise", "One smooth train to the hills, and a ryokan night.", "Odakyu Romancecar from Shinjuku to Hakone-Yumoto, then the mountain railway toward Gora. It takes the morning.", "A lake loop only if the timing is kind: a short look at Lake Ashi, then check in. Do not stack the pirate ship, the ropeway, and a hike before a kaiseki dinner.", "Dinner and the bath at Gora Kadan. Private outdoor baths are not in every room. Book that category if you need it, or use the shared bath.", "Luggage can go ahead with a delivery service if you do not want it on the mountain train. Ask the Tokyo hotel the day before.", "Hakone"),
        day(3, "Hakone morning, Tokyo evening", "Leave the ryokan after breakfast and be back in the city for the night.", "A short walk near Gora or the Hakone Open-Air Museum if the weather is decent. Skip it if you would be rushing the bath you paid for.", "Train back to Tokyo. Check into Palace Hotel or Chinzanso.", "A simple dinner. You ate a large ryokan meal last night. Noodles are the right correction.", "Cloud on the ropeway is common. If you cannot see across the valley, you still had the ryokan. Do not wait all day for Fuji.", "Lake Ashi"),
        day(4, "Palace garden, or the Chinzanso trees", "A last nature morning that is in Tokyo on purpose.", "If you are at the Palace Hotel, walk the outer gardens of the Imperial Palace. If you are at Chinzanso, use the hotel garden and do not add a crossing of the city.", "A konbini or hotel lunch and the airport train.", "Haneda is the easier airport from central Tokyo. Narita needs more margin.", "There is no Fuji stop on the way to the airport that is worth missing a flight for.", "Tokyo Imperial Palace"),
    ],
    attractions=[
        sight("Meiji Shrine", "The city forest. It does not require a clear view of anything distant.", "Early morning. The iris garden is seasonal and separate.", "Meiji Shrine"),
        sight("Shinjuku Gyo-en", "Lawn, greenhouse, and a planned landscape. The city's best easy nature after the shrine.", "A ticket and a closing time. Go after the shrine, not after dark.", "Shinjuku Gyo-en"),
        sight("Hakone", "The mountain night. Hills, baths, and a lake if you have the hours.", "One night is the shape of this trip. A day trip from Tokyo is the backup.", "Hakone"),
        sight("Lake Ashi", "The lake in Hakone, with a chance of Fuji and a better chance of cloud.", "If the peak is hidden, look at the lake and leave. Do not reorganize the trip around a rumor.", "Lake Ashi"),
        sight("Tokyo Imperial Palace outer gardens", "Moat, pine, and a flat walk beside the Palace Hotel.", "You are walking the public edge, not touring the private palace.", "Tokyo Imperial Palace"),
        sight("Mount Fuji", "The mountain you may not see. Named here so the trip can be honest about it.", "Clear winter mornings are the best odds. Most days, something is in the way.", "Mount Fuji"),
    ],
    scenic_routes=[
        route("Romancecar to Hakone", "Shinjuku to Hakone-Yumoto, then the Tozan line up to Gora. The scenic part is the climb after Yumoto.", "About 2 hours to Gora"),
        route("Meiji to the station", "A walk out of the shrine grounds toward Harajuku or Sendagaya. Trees, then the city again.", "20–30 minutes"),
        route("Palace moat loop", "A flat walk along the Imperial Palace's east gardens and moat. The nature view from the Tokyo hotel, at ground level.", "About 3 km"),
    ],
    transport="Trains. The Romancecar needs a limited-express ticket plus the fare; buy it in the Odakyu app or at Shinjuku. A Hakone Freepass can be worth it if you will ride the mountain line, a bus, and a boat. A car is unnecessary and parking in both places is a chore. Luggage forwarding between the Tokyo hotel and the ryokan is the calm way to do the split night.",
    food=[
        dish("Kaiseki", "Gora Kadan, in the room or a private dining room", "This is the Hakone dinner, included in the ryokan rate. Show up hungry and do not book a second dinner."),
        dish("Ryokan breakfast", "Gora Kadan", "Fish, rice, pickles. It is a meal. Eat it before the train back."),
        dish("Noodles in Tokyo", "A soba or ramen shop near Tokyo Station or Mejiro", "The night you return from Hakone. Small, quick, and not another banquet."),
        dish("Konbini breakfast", "The Tokyo mornings", "On the days you are not at the ryokan, rice balls and coffee are enough before a garden."),
    ],
    tips=[
        "Do not buy a Shinjuku 'Fuji view' room unless the hotel will put the direction in writing. Even then, cloud hides the mountain most days, and summer haze hides it more.",
        "Gora Kadan's private open-air bath is a room category, not a promise on every door. The shared bath is still the ryokan.",
        "Ryokan rates are per person and include dinner and breakfast. Compare them with a hotel room plus two meals, not with a bare room rate.",
        "One Hakone night is enough inside four nights. Two nights is a Hakone trip. Zero nights is a Tokyo park trip, which is the Chinzanso version.",
    ],
    faqs=[
        faq("Will I see Mount Fuji?", "Maybe, from the Hakone side, on a clear day. Plan as if you will not. The ryokan and the Tokyo gardens still work in cloud."),
        faq("Can I do Kawaguchiko instead?", "Yes, as a different long day from Tokyo, about two hours each way. This itinerary chooses Hakone because the ryokan night fits. Doing both is too much."),
        faq("Is Hakone Kowakien the same idea?", "No. Kowakien is the large onsen and theme-park side of Hakone. Gora Kadan is the quiet ryokan."),
        faq("What if I do not want to change hotels?", "Stay at Chinzanso or the Palace Hotel all four nights, keep Meiji and Gyo-en, and treat Hakone as a day trip. You will have less of the bath and none of the rush."),
    ],
    map_places=[
        stop("Meiji Shrine", "Tokyo", "Japan", "Meiji Shrine"),
        stop("Shinjuku Gyo-en", "Tokyo", "Japan", "Shinjuku Gyo-en"),
        stop("Hakone", "Hakone", "Japan", "Hakone"),
        stop("Lake Ashi", "Hakone", "Japan", "Lake Ashi"),
        stop("Tokyo Imperial Palace", "Tokyo", "Japan", "Tokyo Imperial Palace"),
    ],
    budget_notes="The Hakone night is the expensive one, often priced per person with two meals, so a couple can spend as much as a serious Tokyo hotel or more. Palace Hotel and Chinzanso are luxury city rates. Trains are cheap. The Hakone Freepass and a kaiseki that is already in the rate are the budget. Do not add a Fuji sightseeing ticket on top and expect the mountain to cooperate.",
))

add(trip(
    slug="kyoto-luxury-with-ocean-view",
    title="Kyoto luxury: a garden and the Kamogawa, not an ocean",
    location="Kyoto, Japan",
    summary=(
        "Kyoto is inland. Four nights of the city's real luxury, at the Four Seasons in Higashiyama, at Aman Kyoto "
        "in the northern hills, and at Hiiragiya, the old ryokan by the river. The water in town is the Kamogawa. "
        "There is no sea view to upgrade into, and a transfer to Aman is part of staying there."
    ),
    who="Travelers who want the best garden or ryokan stay in Kyoto and do not need a coastline invented for them.",
    best_time="Late March to April for blossom, and November for color. Both are crowded and expensive. June is rainy. August is hot. Winter is quiet and cold and suits a ryokan.",
    nights=4,
    hook="4 nights · Garden and ryokan luxury · The river is the Kamogawa",
    constraints=["No ocean", "Aman is in the hills", "Hiiragiya is formal"],
    lodging="$700–2,000",
    daily="$900–2,400",
    neighborhoods=[
        stay_area("Southern Higashiyama", "The Four Seasons is here, beside a historic pond garden, walkable to the temples if you like walking and a taxi if you do not."),
        stay_area("The northern hills", "Aman Kyoto is in Kita ward, in the forest, not in Gion. A car from Kyoto Station is on the order of 30 to 40 minutes. You are choosing the setting over the stroll to dinner."),
    ],
    hotels=[
        hotel("Four Seasons Hotel Kyoto", "Higashiyama", "Built around a centuries-old pond garden in southern Higashiyama. The water is that pond, and the walks are to Kiyomizu and the lanes. There is no ocean.", "$700–1,400", "Kyoto", "https://www.fourseasons.com/kyoto/"),
        hotel("Aman Kyoto", "Northern hills, Kita ward", "A hotel in the forest above the city, not a base in Gion. Budget a 30- to 40-minute transfer from Kyoto Station each time you go in. The view is trees and a garden.", "$1,200–2,500", "Kyoto", "https://www.aman.com/resorts/aman-kyoto"),
        hotel("Hiiragiya", "Nakagyo, by the Kamogawa", "A ryokan operating since 1818, a short walk from the river and Pontocho. Kaiseki is in the rate, priced per person. It is formal. It is not a family resort, and it does not face the sea.", "$900–1,800 for two, with meals", "Kyoto"),
    ],
    itinerary=[
        day(1, "The garden you are sleeping beside", "Arrive and learn which water is actually outside.", "Transfer. If you chose Aman, the ride from the station is part of the stay, not a surprise.", "Walk the hotel garden. At the Four Seasons, that is the pond. At Aman, it is the forest path. At Hiiragiya, walk to the Kamogawa.", "Dinner in the hotel. Hiiragiya's kaiseki is the reason to be there. Do not book a second dinner.", "Tell Aman in advance which hours you want a car. The hills are not a casual subway hop.", "Kamo River"),
        day(2, "One temple district", "Higashiyama, edited.", "Kiyomizu-dera early, then the walk down Sannen-zaka. Leave before the lane becomes a queue.", "Back to the hotel. If you are at Aman, this day is a car in and a car out, and that is fine.", "A quiet evening. Gion is a walk from Hiiragiya and a plan from Aman. See it once, without a performance unless you booked one.", "The temple sits on a hill. The street back down is the pretty one and the crowded one.", "Kiyomizu-dera"),
        day(3, "The north, or the bamboo", "A second landscape, not a checklist of every temple.", "If you are at Aman, stay on the north side: a walk, the hotel, and maybe Kamigamo. If you are at the Four Seasons or Hiiragiya, take a taxi or train to Arashiyama in the morning only.", "The bamboo grove is a short walk and a crowd. See it, then the river, then leave. Do not add the monkey park unless you want a hike.", "Dinner at the hotel again if you are at the ryokan. One restaurant night is plenty on this trip.", "Arashiyama at opening is a different place from Arashiyama at 11 a.m.", "Arashiyama"),
        day(4, "The river, then the station", "A last flat walk and a train.", "Along the Kamogawa if you are central, or one more garden path if you are at Aman.", "Transfer to Kyoto Station. The Aman car needs to be booked. The Four Seasons and Hiiragiya are ordinary taxis.", "The shinkansen or the Haruka to the airport. Eat before you go if dinner was your habit; station food is a backup.", "Do not schedule Fushimi Inari on the way to a train. The mountain of gates takes longer than a cab detour.", "Fushimi Inari-taisha"),
    ],
    attractions=[
        sight("Kiyomizu-dera", "The wooden stage over the hillside. The Higashiyama temple to see if you see one.", "Early. The lane below it is the crowd.", "Kiyomizu-dera"),
        sight("Kamo River", "The city's water. Couples sit on the banks in season. It is a river, and it is the correct answer to 'what water is in Kyoto?'", "Walk a section near Pontocho rather than trying to follow it for miles.", "Kamo River"),
        sight("Arashiyama", "The western edge: bamboo, a river, and hills.", "A morning, not a full day added to a temple list.", "Arashiyama"),
        sight("Bamboo Forest (Kyoto)", "The grove everyone means when they say Arashiyama.", "It is short. Go early and then do something else nearby or leave.", "Bamboo Forest (Kyoto)"),
        sight("Fushimi Inari-taisha", "The torii gates. Worth it on a day you can give it, not on a transfer day.", "Walk uphill until the crowd thins. You do not have to reach the summit.", "Fushimi Inari-taisha"),
        sight("Philosopher's Walk", "A canal path in the northern east of the city. Best in blossom or autumn, ordinary and still pleasant otherwise.", "Pair it with nothing huge. It is a walk.", "Philosopher's Walk"),
    ],
    scenic_routes=[
        route("Kamogawa bank", "From the Shijo bridges north or south along the river path. The water in this trip, named correctly.", "2–4 km"),
        route("Sannen-zaka down from Kiyomizu", "The stone lane of shops from the temple toward the city. Pretty, and crowded after mid-morning.", "About 1 km"),
        route("Arashiyama morning", "Bamboo grove to the river and back to the taxi or the train. A half-day from a central hotel, a planned car day from Aman.", "A morning"),
    ],
    transport="Taxis and hotel cars in Kyoto, trains for the city if you are staying centrally and like the bus and subway. Aman Kyoto is a car stay. Hiiragiya and the Four Seasons can be on foot for some meals and some temples. Kyoto Station is the shinkansen. The airport is the Haruka express if you are leaving Japan from Kansai.",
    food=[
        dish("Kyo-kaiseki", "Hiiragiya, in the room", "The meal the ryokan is for. It is included, it is long, and you should not add dinner elsewhere that night."),
        dish("Yudofu", "A tofu restaurant near Nanzen-ji, on a day you are already east", "Hot tofu in broth. A Kyoto lunch, light enough to walk after."),
        dish("Nishiki Market snacks", "Nishiki, one midday", "Pickles, grilled fish on a stick, tamagoyaki. Eat as you go, then sit down somewhere else for a real meal.", ),
        dish("Breakfast at the hotel", "Four Seasons, Aman, or the ryokan", "You are in the price band where breakfast is part of the stay. Use it."),
    ],
    tips=[
        "Kyoto has no ocean. The Kamogawa is the river. The Four Seasons pond is a pond. Aman's water is a garden.",
        "Aman is not a walk to Gion. Every dinner in town is a transfer. Stay in and eat there on at least one night.",
        "Hiiragiya is formal, and the rate is per person with meals. Ask before bringing children. This is not a family hotel.",
        "Blossom weeks and the November leaves are when these hotels are hardest to book and easiest to overpay. The gardens are still there in early December.",
    ],
    faqs=[
        faq("Can I get an ocean-view room in Kyoto?", "No. You can get a garden, a pond, a forest, or a river. The sea is in other cities."),
        faq("How long is the transfer to Aman Kyoto?", "About 30 to 40 minutes from Kyoto Station by car, longer in traffic. Plan the day around that, or pick the Four Seasons or Hiiragiya."),
        faq("Is Tawaraya the same as Hiiragiya?", "They are the two famous old ryokan, a lane apart. Tawaraya is real and extremely hard to book. Hiiragiya is the one listed here because it is operating and reachable."),
        faq("Is the bamboo grove worth it?", "Once, early, as a short walk. It is not a half-day of content. The river beside it is the better linger."),
    ],
    map_places=[
        stop("Kiyomizu-dera", "Kyoto", "Japan", "Kiyomizu-dera"),
        stop("Kamo River", "Kyoto", "Japan", "Kamo River"),
        stop("Arashiyama", "Kyoto", "Japan", "Arashiyama"),
        stop("Fushimi Inari-taisha", "Kyoto", "Japan", "Fushimi Inari-taisha"),
        stop("Philosopher's Walk", "Kyoto", "Japan", "Philosopher's Walk"),
    ],
    budget_notes="All three hotels are luxury, and Aman and Hiiragiya's per-person meal rates can put a couple well above $1,000 a night. The Four Seasons is often the most straightforward room rate of the three. Taxis and the Aman car are the transport cost. Temple tickets are minor. Eating kaiseki out on top of a ryokan plan is how the budget doubles for no reason.",
))

add(trip(
    slug="osaka-family-friendly-with-kitchen",
    title="Osaka with a kitchen: Namba apartments, and Dotonbori only once",
    location="Osaka, Japan",
    summary=(
        "Four nights in a Namba apartment hotel with a kitchen, for a family that wants okonomiyaki once and breakfast "
        "at home the other mornings. Dotonbori is one night, not the whole trip. A train to Kyoto takes about half an "
        "hour and can be one day; the rest stays in Osaka and is about food you can also cook."
    ),
    who="Families who want two rooms or a real kitchen near Namba or Umeda and do not want a different restaurant for every meal.",
    best_time="March to May, and October to November. Summer is hot and festival-busy. New Year closes a surprising number of small kitchens.",
    nights=4,
    hook="4 nights · Namba kitchen · One Dotonbori night",
    constraints=["Kitchen", "Near Namba", "Dotonbori is not every evening"],
    lodging="$160–380",
    daily="$260–450",
    neighborhoods=[
        stay_area("Namba", "Fraser, Citadines, and MIMARU are all a short walk from Namba Station. Kuromon, Dotonbori, and the Nankai line are the reasons to be here."),
        stay_area("Umeda, as a day", "The north side is a train ride, useful for a department-store food floor, not where these apartments are."),
    ],
    hotels=[
        hotel("MIMARU Osaka Namba Station", "Namba", "Kitchens in the rooms and family apartments with bunks, a few minutes from Nankai Namba. A two-bedroom layout was announced for December 2026; before that, book the family apartment and ask how the beds are divided.", "$150–320", "Osaka"),
        hotel("Citadines Namba Osaka", "Namba", "Apartments in the old Takashimaya annex, studios through two-bedrooms. Book a one- or two-bedroom so you get a proper kitchen and a door. A studio is a weaker family fit.", "$170–360", "Osaka"),
        hotel("Fraser Residence Nankai Osaka", "Namba", "One- and two-bedroom apartments with kitchenettes, about three minutes from Nankai Namba Station. The washer-dryer is in the apartment. Dotonbori is a walk you can choose not to repeat.", "$180–380", "Osaka"),
    ],
    itinerary=[
        day(1, "Grocery, then one neon street", "Get the kitchen running, and see Dotonbori once.", "IC card if you do not already have one from the airport. Check in and find a supermarket.", "Rest. The kitchen gets a test run of rice or noodles.", "Dotonbori after dark for takoyaki, eaten standing up, then home. You have now done the famous street.", "Go early with children. The canal side gets packed later.", "Dōtonbori"),
        day(2, "Osaka, not a slogan", "Castle or market, not both plus a theme park.", "Kuromon Market in the morning for fruit and grilled seafood, eaten there, not hauled back as a project.", "Osaka Castle park for an hour outdoors. The keep is optional.", "Cook dinner. You already ate street food last night.", "The castle grounds are the part that works with children. The interior is a museum you can skip.", "Osaka Castle"),
        day(3, "Kyoto, if you want it, by train", "A half-hour train and one Kyoto neighborhood, then back to your own kitchen.", "JR Special Rapid from Osaka to Kyoto. Pick one: Fushimi Inari's lower gates, or Arashiyama's bamboo and the river. Not both.", "Back in Osaka by late afternoon. The apartment is the reward.", "Dinner in. Or okonomiyaki at a local counter near Namba, which is a better Osaka meal than a second night of tourist takoyaki.", "The Kyoto day is optional. If everyone is tired, Umeda's food floor and the apartment are a valid day three.", "Fushimi Inari-taisha"),
        day(4, "A market breakfast and the airport", "Leave from Namba, which is convenient for Kansai Airport.", "Use the kitchen, then a short walk if the flight is late.", "Nankai limited express from Namba to Kansai Airport, or the Haruka if your routing prefers it. Buy the airport train before you are in a hurry.", "Eat what is left in the fridge. A last konbini run covers the rest.", "The Nankai rapi:t is the simple Namba-to-KIX train. It costs more than the ordinary express and saves the stress.", "Namba"),
    ],
    attractions=[
        sight("Dōtonbori", "The canal, the signs, and one night of street food.", "Once. The apartment is a five- to fifteen-minute walk, which is close enough.", "Dōtonbori"),
        sight("Osaka Castle", "The park and the moat. The tower is a museum if you want the stairs.", "Weekends are crowded. The grounds are the family part.", "Osaka Castle"),
        sight("Namba", "The station neighborhood you are living in, including shops that are not on the canal.", "Use it for groceries and trains, not as a thing to 'do' for four hours.", "Namba"),
        sight("Shinsaibashi", "The covered shopping street. Useful in rain, skippable in good weather.", "Walk through on the way to Dotonbori rather than making it an event.", "Shinsaibashi"),
        sight("Umeda", "A north-Osaka afternoon: department stores and a food floor.", "One visit for a depachika picnic you bring home. Not a second base.", "Umeda"),
        sight("Fushimi Inari-taisha", "The optional Kyoto morning, half an hour away by train.", "Climb only as far as the group is happy. The lower gates are the photograph.", "Fushimi Inari-taisha"),
    ],
    scenic_routes=[
        route("Namba to Dotonbori on foot", "The walk from the apartment to the canal. Do it once at night and once, if you must, by day, and then stop.", "10–15 minutes"),
        route("Special Rapid to Kyoto", "Osaka Station or a central JR station to Kyoto in about 30 minutes. The scenic part is Kyoto, not the train.", "About 30 minutes"),
        route("Castle park loop", "Around the outer moat and up to the plaza. Flat enough with a pause, and a real outdoor hour.", "About 3 km"),
    ],
    transport="Trains and walking. Get an IC card. Nankai Namba is the airport station for Kansai. JR is the Kyoto day. A car in central Osaka is a mistake. Taxis are for rain and for a child who is done walking, not for every hop.",
    food=[
        dish("Takoyaki", "A stand on Dotonbori, night one only", "Octopus balls, eaten hot, standing up. One tray. Then you are finished with this street."),
        dish("Okonomiyaki", "A counter near Namba, not a tourist stage", "Savory pancake. Cook-it-yourself shops are fun with older children and messy with very small ones."),
        dish("Kushikatsu", "A local Shinsekai or Namba counter, one lunch", "Breaded skewers. The rule is not to double-dip the sauce. Go early."),
        dish("Breakfast from the grocery", "The apartment", "Eggs, bread, fruit, yogurt. The kitchen is why this is not a hotel buffet you will not get to."),
    ],
    tips=[
        "Dotonbori on night one, and not again, unless someone specifically asks. It does not get better on the fourth visit.",
        "Book the apartment with a kitchen and a closed bedroom. Fraser's two-bedrooms and Citadines' larger apartments are the clear versions. MIMARU's family rooms have kitchens and bunks; confirm the layout.",
        "Kyoto is optional and close. It is not an Osaka trip if you sleep there. Come back to the kitchen.",
        "Kuromon is a market, not a grocery. Buy the snack there and the breakfast ingredients at a supermarket.",
    ],
    faqs=[
        faq("Is Universal Studios on this trip?", "No. It is a full day and a separate ticket, and it deletes the kitchen-and-neighborhood idea. Go another time."),
        faq("Can we walk to Umeda?", "You should not. It is a short subway ride. Save the walking for Namba."),
        faq("Do the kitchens have ovens?", "Assume a hob, a rice cooker or a pot, and a microwave. Plan dinners that match that."),
        faq("How close is Kyoto?", "About 30 minutes by JR Special Rapid from Osaka to Kyoto Station, plus the time to reach the JR station. It is a day, not a commute to do twice."),
    ],
    map_places=[
        stop("Dōtonbori", "Osaka", "Japan", "Dōtonbori"),
        stop("Osaka Castle", "Osaka", "Japan", "Osaka Castle"),
        stop("Namba", "Osaka", "Japan", "Namba"),
        stop("Shinsaibashi", "Osaka", "Japan", "Shinsaibashi"),
        stop("Umeda", "Osaka", "Japan", "Umeda"),
    ],
    budget_notes="A family apartment near Namba is often $160–350. Food drops sharply if breakfast and two dinners are cooked and the street-food nights are snacks rather than kaiseki. The Kyoto train is inexpensive. The airport express is the transport splurge worth making. Skip Universal and the budget stays recognizable.",
))

add(trip(
    slug="osaka-luxury-with-ocean-view",
    title="Osaka's water is a bay: city towers, and one hotel that is actually on it",
    location="Osaka, Japan",
    summary=(
        "Osaka has a bay and does not have a Pacific beach. Four nights that say so. Conrad and InterContinental are "
        "high city hotels whose upper floors look toward the bay in the distance. Grand Prince Hotel Osaka Bay, in "
        "Nanko, is the one standing on the water. None of them shows an open-ocean horizon from Kita."
    ),
    who="Travelers who want a luxury Osaka stay and a true description of the water they will see.",
    best_time="March to May, and October to November, when the air is clearer and a distant bay is actually visible. Summer haze makes every 'bay view' into a city view.",
    nights=4,
    hook="4 nights · Bay, not Pacific · One hotel on the water, two towers inland",
    constraints=["No Pacific claim", "Name the water correctly", "Nanko is not Namba"],
    lodging="$350–900",
    daily="$500–1,050",
    neighborhoods=[
        stay_area("Nakanoshima and Umeda", "Conrad is on the river island of Nakanoshima. InterContinental is in Grand Front by Osaka Station. Both are city hotels. The bay is a direction, not a beach at the door."),
        stay_area("Nanko, on Osaka Bay", "Grand Prince Hotel Osaka Bay is in Suminoe, on the bay, with harbor and skyline views. Downtown is a shuttle or a train."),
    ],
    hotels=[
        hotel("Conrad Osaka", "Nakanoshima", "A high tower on Nakanoshima Festival Tower West. Upper floors look across the city and south toward the bay. The water below the building is the river. There is a shared indoor pool on the 38th floor. This is not a beach resort.", "$450–900", "Osaka"),
        hotel("InterContinental Osaka", "Umeda, Grand Front", "Next to Osaka Station. High floors look over the city, and on a clear day the bay is in the distance. The lap pool is shared and indoors. You are in Kita, not on a Pacific headland.", "$400–800", "Osaka"),
        hotel("Grand Prince Hotel Osaka Bay", "Nanko, Suminoe", "The hotel that is actually on Osaka Bay, with harbor and skyline views. The water is a bay of the inland sea, not the open Pacific. You will use a shuttle or the New Tram to reach Umeda or Namba.", "$250–550", "Osaka"),
    ],
    itinerary=[
        day(1, "See which water you got", "Check the view against the booking before you build a fantasy around it.", "Arrive and go up. At Conrad, the river and the city are the foreground. At the Grand Prince, the bay is the foreground. At InterContinental, it is skyline first.", "A walk on Nakanoshima if you are central, or the harbor edge if you are in Nanko.", "Dinner in the hotel or a short ride to a single good restaurant. You do not need Dotonbori tonight.", "If the haze is thick, the 'bay view' from Umeda becomes a city view. That is normal.", "Osaka Bay"),
        day(2, "The bay, on purpose", "Go to the water even if your hotel is already there, and name it correctly.", "Osaka Aquarium Kaiyukan and the Tempozan area. This is the waterfront people mean, on the bay.", "If you are staying in Nanko, you are already on this side of the city. If you are in Umeda, it is a subway and a tram, not a stroll.", "Back before you are tired of trains. One waterfront day is enough.", "The aquarium is a full morning with children and a long visit without them. Do not add Universal.", "Osaka Aquarium Kaiyukan"),
        day(3, "The city that is not a view", "A day in Osaka proper, because a bay hotel is still a city trip.", "Osaka Castle park in the morning.", "Umeda or Namba for one meal and one walk. If you are at the Grand Prince, this is the day the shuttle earns its place.", "A reserved dinner. Conrad and InterContinental are in the restaurant belt. From Nanko, eat at the hotel or accept the ride.", "Do not describe the castle moat as the ocean either. It is a moat.", "Osaka Castle"),
        day(4, "A clear morning, then the airport", "Look once more, then leave.", "If the air is clear, the bay view is at its best in the morning. If it is not, you have already had the trip.", "Train to Kansai Airport. From Nanko the New Tram and a connection take longer than the Umeda hotels' direct options. Leave the extra time.", "Eat before the platform. Airport food is the backup.", "Haze, again, is not a failed holiday. The bay is still where the map says it is.", "Ōsaka Station"),
    ],
    attractions=[
        sight("Osaka Bay", "The body of water this search can honestly claim. An inland-sea bay, with a port, not a Pacific beach.", "You see it properly from Nanko and Tempozan. From Umeda you see toward it.", "Osaka Bay"),
        sight("Osaka Aquarium Kaiyukan", "The serious waterfront attraction, next to the harbor.", "Buy a time. It is popular, and it is enough for a morning.", "Osaka Aquarium Kaiyukan"),
        sight("Osaka Castle", "The city landmark, inland, with a park.", "The grounds first. The tower if you like museums.", "Osaka Castle"),
        sight("Nakanoshima", "The river island under Conrad. A real walk, and a river.", "Evening is pleasant. It is not a beach.", ""),
        sight("Umeda", "The north station city: InterContinental, department stores, and the skyline view.", "One evening. The restaurants are the point.", "Umeda"),
        sight("Dōtonbori", "Optional, one night, if you want the noisy version of Osaka.", "It is a canal in Minami, not a bay.", "Dōtonbori"),
    ],
    scenic_routes=[
        route("Nakanoshima river walk", "Along the island under the Conrad. Bridges, office lights, and the river. The accurate water for that hotel.", "2–4 km"),
        route("Tempozan harbor edge", "Aquarium to the waterfront promenade. This is the bay, with cranes and a ferris wheel, not a tropical beach.", "An hour"),
        route("Umeda to Nanko", "Subway and New Tram, or the hotel shuttle, from a Kita hotel to the bay. Do it once so the view category is not theoretical.", "About 40 minutes"),
    ],
    transport="Trains for the city, the hotel shuttle if you are at the Grand Prince, and a taxi at night when the connection is annoying. Kansai Airport is the Nankai or JR Haruka depending on your station. A car does not improve this trip. From Kita you cannot walk to the Pacific because the Pacific is not there.",
    food=[
        dish("Hotel breakfast with the real view", "Conrad, InterContinental, or the Grand Prince", "Eat it by the window once. City, river, or bay: you will know which you bought."),
        dish("Okonomiyaki", "A serious counter in Umeda or Fukushima, not a novelty show", "One Osaka meal that is not room service."),
        dish("Sushi or grilled fish", "A reserved dinner near the hotel", "You are in a port city. Order the fish and skip the skyline restaurant with a weak kitchen."),
        dish("Kushikatsu", "A simple counter, one lunch", "Skewers and a beer or tea. The opposite of the hotel, on purpose."),
    ],
    tips=[
        "From Kita, a bay view means a high floor looking south on a clear day. It does not mean waves.",
        "Grand Prince Hotel Osaka Bay is the waterfront hotel. It is in Nanko, and the trade is the shuttle.",
        "Conrad's pool is a shared indoor pool on the 38th floor. It looks at the city. It is not a private ocean pool.",
        "Summer haze and winter smog both flatten the distant view. Book the Nanko hotel if seeing water up close matters more than being in Umeda.",
    ],
    faqs=[
        faq("Is Osaka on the Pacific?", "No. Osaka Bay connects to the Seto Inland Sea. The open Pacific is on the other side of the Kii Peninsula and is not what these windows face."),
        faq("Which hotel is actually on the water?", "Grand Prince Hotel Osaka Bay, in Nanko. Conrad is on the river in Nakanoshima. InterContinental is in Umeda."),
        faq("Can I see the sea from the castle?", "You see the city. Do not go to the castle for a maritime view."),
        faq("Is the aquarium worth it?", "Yes, once, as the bay day. It is a large aquarium beside the harbor, not a substitute for a beach."),
    ],
    map_places=[
        stop("Osaka Bay", "Osaka", "Japan", "Osaka Bay"),
        stop("Osaka Aquarium Kaiyukan", "Osaka", "Japan", "Osaka Aquarium Kaiyukan"),
        stop("Osaka Castle", "Osaka", "Japan", "Osaka Castle"),
        stop("Umeda", "Osaka", "Japan", "Umeda"),
        stop("Ōsaka Station", "Osaka", "Japan", "Ōsaka Station"),
    ],
    budget_notes="Conrad and InterContinental are the expensive city towers. The Grand Prince is often less and spends its money on the bay location instead of a Kita address. Meals in-house push the daily cost up; one serious dinner and one local lunch is the saner split. The aquarium ticket is the planned extra. Shuttles are free and taxis from Nanko are not.",
))

add(trip(
    slug="osaka-with-private-pool",
    title="Osaka does not do private pools: three excellent hotels anyway",
    location="Osaka, Japan",
    summary=(
        "A private pool is a poor fit for Osaka. Onsen baths and shared hotel pools are real, and they are not a pool "
        "that belongs to your room. These four nights stay at the St. Regis, the Ritz-Carlton, or the Imperial, and "
        "do not pretend any of them is a villa with a plunge. If a private pool is the whole point, this is the wrong city."
    ),
    who="Travelers who asked for a private pool, can hear that Osaka is the wrong inventory, and still want a very good hotel.",
    best_time="March to May, and October to November. The advice does not change with the season: the pool you want is still not a standard room feature.",
    nights=4,
    hook="4 nights · Luxury Osaka · No private pool, said plainly",
    constraints=["Do not call a shared pool private", "No fake villa", "The city is still worth staying in"],
    lodging="$350–800",
    daily="$500–950",
    neighborhoods=[
        stay_area("Midosuji", "The St. Regis is on this boulevard, between Umeda and Namba, which is a useful and quiet-enough luxury address. It is not a resort coast."),
        stay_area("Umeda and Temmabashi", "Ritz-Carlton and the Imperial are north, near trains and the river. Gardens and lobbies, not private decks over the Pacific."),
    ],
    hotels=[
        hotel("The St. Regis Osaka", "Midosuji, Hommachi", "A strong city hotel with a butler service, on the main boulevard, connected to Hommachi Station. It is not a pool hotel. Book it for the room and the service. There is no private pool to request.", "$400–800", "Osaka"),
        hotel("The Ritz-Carlton, Osaka", "Umeda", "A long-running luxury hotel in Umeda. If you find a pool on the property, it is a shared hotel pool. That does not meet a private-pool search. The reason to stay is the hotel, the station, and the restaurants.", "$400–850", "Osaka"),
        hotel("Imperial Hotel Osaka", "Temmabashi", "The city's classic grand hotel, by the Okawa River, with a garden. It is a wonderful stay and a bad answer to 'private pool.' Listed so the trip has three real hotels and zero invented plunges.", "$300–650", "Osaka"),
    ],
    itinerary=[
        day(1, "A good hotel, and the truth", "Check in and retire the pool request before it ruins the stay.", "Arrive, look at the room you actually booked, and go for a walk. Midosuji if you are at the St. Regis, the river if you are at the Imperial.", "A coffee and an early evening. You are in a city hotel.", "Dinner in the hotel the first night. It will be better than a search for a pool deck that is not there.", "Ask the concierge about a public bath or a spa appointment if you want water. Call it a bath or a spa.", "Umeda"),
        day(2, "The river and the castle", "Osaka outdoors, which is parks and a river, not a villa pool.", "Osaka Castle park in the morning.", "Nakanoshima and a walk by the river in the afternoon. This is the city's elegant water.", "A teppanyaki or a sushi counter, reserved. One expensive meal, eaten because the hotel is already expensive.", "The castle park is busy on weekends. Go anyway, and leave when you are done.", "Osaka Castle"),
        day(3, "A bath, accurately named", "If you want to soak, book a real bath, not a fictional pool.", "A morning in Umeda or a department store, unhurried.", "Book a spa treatment at the hotel, or a sento or super-sento the concierge respects. Shared water, clear rules, tattoos often restricted.", "Dinner anywhere but a revolving skyline restaurant. Kita has better options than the view category suggests.", "Tattoo policies at baths are strict in Osaka. Ask before you go.", "Namba"),
        day(4, "Leave without a grievance", "The city was the trip. The missing pool was never coming.", "A last walk on Midosuji or along the Okawa. Buy nothing you have to carry onto a train.", "Kansai Airport by train. From Hommachi or Umeda this is straightforward. From Temmabashi, give it one extra connection's worth of time.", "Eat first.", "Four nights was enough to enjoy Osaka and not enough to conjure a private pool. Both things are true.", "Ōsaka Station"),
    ],
    attractions=[
        sight("Osaka Castle", "The park that gives the trip an outdoor morning.", "Walk the grounds. The tower is optional.", "Osaka Castle"),
        sight("Midosuji", "The boulevard the St. Regis sits on. Ginkgo in season, a city street the rest of the year.", "It is a walk, not a viewpoint.", ""),
        sight("Umeda", "Stations, food, and the practical north side.", "Use it for a meal and a train, not a pool.", "Umeda"),
        sight("Nakanoshima", "The river island. The nicest central walk that is actually about water.", "Evening, when the offices empty and the bridges are lit.", ""),
        sight("Namba", "South Osaka, if you want one louder evening.", "Go for dinner and come back. You do not need to stay there.", "Namba"),
        sight("Okawa River", "The river by the Imperial Hotel. A walk, not a swim.", "Morning is calm. This is not a beach.", ""),
    ],
    scenic_routes=[
        route("Midosuji walk", "Along the boulevard from Hommachi toward Umeda or Namba. The city's formal street, at ground level.", "2–4 km"),
        route("Okawa to the castle", "A taxi or a walk from the Imperial's river to the castle park. Green, then the moat.", "A morning"),
        route("Nakanoshima loop", "Bridges and the riverside, which is the water you can have. It is public and it is enough.", "About 3 km"),
    ],
    transport="Subway and walking. All three hotels are connected to the city in a way a villa with a private pool would not be, which is the consolation. Kansai Airport by Nankai or JR. Taxis at night are reasonable and not a lifestyle.",
    food=[
        dish("Teppanyaki", "A reserved counter, or the hotel if it has a good one", "One meal where the theater is the cooking and you can sit still."),
        dish("Sushi", "A serious counter in Kita", "Osaka's sushi is not a consolation prize. Book it and be on time."),
        dish("Okonomiyaki", "A local counter, one lunch", "The meal that keeps the trip from being only hotel dining rooms."),
        dish("Hotel breakfast", "Whichever of the three you chose", "Included or not, eat it. You are not walking out to a pool cafe."),
    ],
    tips=[
        "A shared indoor pool, a sento, and a private onsen bath are three different things. None of the three hotels is being sold here as a private pool.",
        "If a private pool is non-negotiable, do not take this trip. Look at a villa city. Forcing the word onto a Osaka suite will not put water on the terrace.",
        "The St. Regis is the no-pool version of luxury. That can be a relief if you came for sleep and a boulevard.",
        "Bathhouses often refuse tattoos. Ask. A hotel spa is the simpler soak.",
    ],
    faqs=[
        faq("Is there any Osaka hotel with a private pool?", "Not as a normal product. A rare suite might market a soaking tub. A tub is not a pool. I am not going to rename one."),
        faq("What about a ryokan with a private bath?", "Those exist in Arima or in Kyoto more honestly than in central Osaka. A private bath is still not a pool, and it is a different booking."),
        faq("Does the Ritz-Carlton have a pool?", "Treat anything watery there as shared, or as absent, until the hotel tells you otherwise in writing. It is not a private-pool hotel."),
        faq("Why stay four nights then?", "Because Osaka is a very good food city and these are very good hotels. The mistake is only the pool part of the search."),
    ],
    map_places=[
        stop("Osaka Castle", "Osaka", "Japan", "Osaka Castle"),
        stop("Umeda", "Osaka", "Japan", "Umeda"),
        stop("Namba", "Osaka", "Japan", "Namba"),
        stop("Ōsaka Station", "Osaka", "Japan", "Ōsaka Station"),
        stop("Dōtonbori", "Osaka", "Japan", "Dōtonbori"),
    ],
    budget_notes="You are paying luxury hotel rates, roughly $350–800 a night, for rooms and service, not for a pool. One serious dinner is the other big cost. Spa treatments are optional. There is no pool-cabana minimum spend because there is no pool cabana. Four nights is plenty.",
))

add(trip(
    slug="bangkok-pet-friendly",
    title="Bangkok with a dog: three hotels that publish a pet policy",
    location="Bangkok, Thailand",
    summary=(
        "Four nights in Bangkok only at hotels that publish a pet rule. Kimpton Maa-Lai welcomes pets that fit in the "
        "elevator. Capella takes one small dog and charges for it. Siam Kempinski takes small pets in specific Garden "
        "Wing rooms and does not let them into the restaurants or the gardens. The Peninsula's current listings say no pets."
    ),
    who="People traveling with a dog who need the policy in writing before they fly, not a vague promise that Thailand is easy.",
    best_time="November to February is the kinder weather. March to May is dangerously hot for a walk. The rainy season shortens every outing. Dogs feel the heat before you do.",
    nights=4,
    hook="4 nights · A written pet policy · Heat, sidewalks, and temples",
    constraints=["Published pet rules only", "No invented pet resort", "Temples are not dog attractions"],
    lodging="$250–700",
    daily="$350–800",
    neighborhoods=[
        stay_area("Langsuan and Siam", "Kimpton Maa-Lai and Siam Kempinski are on this side of the city, near malls and the BTS. Useful with a dog you may need to take back upstairs often."),
        stay_area("Charoen Krung", "Capella is on the river. The hotel grounds are the walk. The old-road sidewalks outside are not a reliable dog route."),
    ],
    hotels=[
        hotel("Kimpton Maa-Lai Bangkok", "Langsuan", "The clearest yes. The hotel's own policy welcomes pets that fit in the elevator, with no nightly stay fee, a leash or a stroller, and diapers encouraged. Pets are not allowed in the bars. A cleaning fee applies if there is an accident.", "$220–450", "Bangkok"),
        hotel("Capella Bangkok", "Charoen Krung, by the river", "Dogs only, one dog up to 10 kg, and a fee on the order of THB 3,000++ a night. Not at the pool, the spa, or most restaurants. The hotel names Phra Nakhon as the dining exception. Confirm the fee for your dates.", "$500–1,100", "Bangkok"),
        hotel("Siam Kempinski Hotel Bangkok", "Siam", "Up to two pets around 11 kg, only in named Garden Wing room types, for a fee around THB 1,500++ a night. Pets are not permitted in the restaurants, the public areas, or the gardens. This is a room-and-walk policy, not a resort where the dog joins lunch.", "$280–600", "Bangkok"),
    ],
    itinerary=[
        day(1, "The room, the grass, and an early walk", "Arrive, confirm the pet rules at the desk, and do not overwalk a jet-lagged dog.", "Check in and sign whatever pet form they hand you. Ask again where the dog can relieve itself.", "A short walk at the coolest hour you have left. In Langsuan that may be a small patch and a sidewalk. Do not march to a temple.", "Dinner. At Capella, a small dog may be welcome at Phra Nakhon and not elsewhere. At the Kempinski, plan on in-room dining if the dog cannot be left.", "Pavement gets hot enough to burn paws. If you cannot hold the back of your hand on it, do not walk the dog.", "Lumphini Park"),
        day(2, "The city without the dog", "One big sight, done by the humans, while the dog stays in a planned way.", "Grand Palace and Wat Phra Kaew, or Wat Pho. Dogs do not go in. Shoes come off. A dog on a leash at the gate is not a workaround.", "Only go if someone can stay with the dog in the room, or you have a sitter the hotel trusts. Do not tie a dog outside a temple.", "A cool evening walk, short, near the hotel. Then in-room or a pet-allowed corner for dinner.", "Many taxis and some boats will refuse a dog. Ask before you get in, or use a car the hotel books.", "Grand Palace"),
        day(3, "A park morning", "The best legal, practical outdoor hour for a dog in this city.", "Lumphini Park early, if your hotel can reach it without a miserable transfer, or the hotel's own designated pet area if the park is a production.", "Back before the heat. The middle of the day is air-conditioning, water, and sleep.", "A mall can be a human errand. Most malls are not dog venues. One person goes, one stays, or you go dogless.", "Bring water. A dog from a temperate climate will overheat here faster than the itinerary expects.", ""),
        day(4, "Leave without a midday hike", "The departure is a car and a crate plan, not a last temple.", "A very early walk if the flight allows it. Skip it if you would be on hot concrete.", "Hotel car to the airport. Confirm the airline's crate, breed, and embargo rules before you ever reach this morning. Bangkok heat embargoes are real.", "Papers, water, and the pet fee receipt. Eat.", "Do not switch hotels on the last night because a rooftop looked fun. The policy is why you are here.", "Wat Pho"),
    ],
    attractions=[
        sight("Grand Palace", "The royal and temple complex. People only.", "Shoes off, covered shoulders, no dog in the courtyard, no dog parked at the entrance.", "Grand Palace"),
        sight("Wat Pho", "The reclining Buddha. A better single temple if you only do one.", "Same rule: the dog is not coming in.", "Wat Pho"),
        sight("Wat Arun", "The river temple, worth seeing from the boat or the opposite bank.", "A dog on a boat is a negotiation. See it without the dog.", "Wat Arun"),
        sight("Lumphini Park", "The central park most likely to be a practical dog walk.", "Early morning. The loop is the walk. Midday is not.", ""),
        sight("Jim Thompson House", "A human hour in a teak house and a garden. Leave the dog at the hotel.", "It is small and air-conditioned in parts. Do not combine it with two temples.", "Jim Thompson House"),
        sight("Chatuchak Weekend Market", "A weekend market. Crowded, hot, and a bad place for a dog.", "Skip it on this trip, or go alone while the dog stays in.", "Chatuchak Weekend Market"),
    ],
    scenic_routes=[
        route("Early hotel loop", "Whatever short circuit the concierge will draw for a dog: a soi, a patch of grass, back inside. The scenic part is surviving it.", "15–25 minutes"),
        route("Lumphini outer path", "A morning lap, if you can get there without a refused taxi. Leave as the sun gets serious.", "About 2.5 km"),
        route("River look, without the dog", "A hotel boat or a hired boat for the humans to see Wat Arun from the water. The dog sits this one out.", "An hour"),
    ],
    transport="A hotel car, booked in advance, that has agreed to carry a dog. Taxis and tuk-tuks can refuse. The BTS is a poor tool with a pet. Boats are a human outing. The airport transfer is a private car, and the airline crate rules matter more than the hotel.",
    food=[
        dish("In-room dinner", "Whichever hotel will not allow the dog in the restaurant", "At the Kempinski this is the normal plan. Order early. The dog is why."),
        dish("Boat noodles", "A shop you visit while the dog is settled", "The Bangkok lunch worth leaving the room for. One person stays with the dog if needed."),
        dish("Som tam and grilled chicken", "A simple shop, dogless", "Papaya salad and chicken. The right casual meal when you have a sitter hour."),
        dish("Mango and sticky rice", "Anywhere it looks fresh, including room service", "Dessert. Do this once. It does not require a view."),
    ],
    tips=[
        "Heat is the welfare issue. Walk at dawn or after sunset, test the pavement, carry water, and do not be proud.",
        "Sidewalks are broken, blocked, and sometimes absent. A stroller for a small dog is not a joke.",
        "Temples mean shoes off and no dogs. The Grand Palace is not a pet destination. Do not invent one.",
        "Get the pet policy by email: weight, count, fee, rooms, and where the dog may walk. Listings go stale. The Peninsula currently reads as no pets, whatever older guides say.",
    ],
    faqs=[
        faq("Does the Peninsula Bangkok take dogs?", "Current published listings say no. Do not book it for a pet unless you have a written yes for your dates. This trip uses hotels whose own pages say yes."),
        faq("Can my dog come to the Grand Palace?", "No. Plan a person to stay with the dog, or a sitter. Outside the gate is not a solution."),
        faq("Are the fees per night?", "Capella and Siam Kempinski charge a nightly pet fee. Kimpton Maa-Lai's published policy does not charge a stay fee and does charge for accidents and some supplies. Confirm the number."),
        faq("Is a big dog possible?", "Kimpton is the one that does not set a kilogram cap, as long as the dog fits in the elevator and follows the rules. Capella is 10 kg. The Kempinski is about 11 kg and only in certain rooms."),
    ],
    map_places=[
        stop("Grand Palace", "Bangkok", "Thailand", "Grand Palace"),
        stop("Wat Pho", "Bangkok", "Thailand", "Wat Pho"),
        stop("Wat Arun", "Bangkok", "Thailand", "Wat Arun"),
        stop("Jim Thompson House", "Bangkok", "Thailand", "Jim Thompson House"),
        stop("Chatuchak Weekend Market", "Bangkok", "Thailand", "Chatuchak Weekend Market"),
    ],
    budget_notes="The room is a luxury or upper-mid rate, and the pet fee can add $40–100 a night at Capella and the Kempinski. A sitter, if you want to see a temple properly, is another cost. Cars instead of the BTS add up. Food can stay moderate if some dinners are in the room. Do not budget a 'pet resort' activity. It is not a thing you need, and the comic version of one does not exist.",
))

add(trip(
    slug="sydney-family-friendly-with-kitchen",
    title="Sydney family apartments with kitchens, and Bondi as a day out",
    location="Sydney, Australia",
    summary=(
        "Four nights in a real apartment hotel in The Rocks, Darling Harbour, or the CBD, with a kitchen so dinner is "
        "not a restaurant every night. A ferry day is the trip's best hour. Bondi is an outing by bus, not the base, "
        "because the apartments are in the city where the ferries leave."
    ),
    who="Families who want a kitchen, a washing machine, and the harbor, and who do not need to sleep next to the surf.",
    best_time="October to November, and March to April. December to February is summer, school holidays, and higher rates. June to August is cool and fine for ferries, less so for the beach.",
    nights=4,
    hook="4 nights · City apartment kitchen · Ferry day, Bondi as an outing",
    constraints=["Full kitchen, not a kettle", "City base", "Bondi is not the hotel"],
    lodging="$220–480",
    daily="$340–560",
    neighborhoods=[
        stay_area("The Rocks and Circular Quay", "Quay West puts the ferry wharves at the bottom of the hill. The Opera House and the bridge are walks, not transfers."),
        stay_area("Darling Harbour and Kent Street", "Adina is on King Street Wharf. Meriton Kent Street is a 10-minute walk to Darling Harbour. Both are city apartments, not beach houses."),
    ],
    hotels=[
        hotel("The Sebel Quay West Suites Sydney", "The Rocks", "One- and two-bedroom apartments with full kitchens, above Circular Quay. This is the ferry base. Bondi is a bus you take on purpose.", "$280–520", "Sydney"),
        hotel("Adina Sydney Darling Harbour", "King Street Wharf", "Apartments have full kitchens, with a cooktop and an oven. Studios have a microwave and a fridge, which is not the same. Book the apartment. Darling Harbour is outside.", "$240–460", "Sydney"),
        hotel("Meriton Suites Kent Street", "CBD, Kent Street", "The local serviced-apartment operator. Suites have full kitchens; studios have kitchenettes. An indoor pool, and a walk to Darling Harbour rather than a walk to the sand.", "$200–400", "Sydney"),
    ],
    itinerary=[
        day(1, "Keys, groceries, a harbor look", "Arrive and make the apartment function before you sightsee.", "Check in and shop at a supermarket. Breakfast for tomorrow, and something easy for dinner.", "Walk to Circular Quay even if you are staying at Kent Street. See the bridge and the Opera House from the promenade and then go home.", "Cook. The first night is not the night to queue for a view restaurant with tired children.", "The Rocks is hilly. A two-bedroom with a stroller is still a walk, just a slower one.", "Sydney Opera House"),
        day(2, "The ferry is the activity", "A full ferry day beats a list of neighborhoods.", "Ferry from Circular Quay to Manly. The ride is the view. Swim at Manly only if the flags and the season say yes.", "The return ferry in the afternoon. If energy remains, a short walk in the Royal Botanic Garden.", "Dinner in the apartment, or fish and chips you carry home. You do not need a third location today.", "Ferries use an Opal card. Get one before you are at the wharf with a group.", "Manly, New South Wales"),
        day(3, "Bondi, as a guest", "One beach trip, then back to the city apartment.", "Bus to Bondi in the morning. Swim or walk the coastal path for as long as the group enjoys it, not as a forced march to Coogee.", "Back to the apartment by mid-afternoon. Pool, laundry, a rest. This is what the kitchen and the extra room are for.", "Cook a proper dinner. One night of this, at least, should be pasta or a roast chicken and not a reservation.", "Bondi in summer school holidays is crowded and the bus is slow. Go early.", "Bondi Beach"),
        day(4, "A garden morning, then the airport", "Leave from the harbor, not from a theme park.", "Royal Botanic Garden, or a last ferry to the Zoo side if you already hold Taronga tickets. Do not invent a zoo morning on a flight day.", "Pack the fridge into a last meal or give the food away. Apartment checkout is easier if you are not also hunting lunch.", "Airport train or a booked car. The train is the simple version from the city.", "Do not add Darling Harbour rides and the beach and the garden on the day you fly.", "Royal Botanic Garden, Sydney"),
    ],
    attractions=[
        sight("Sydney Opera House", "The building on the harbor, a walk from The Rocks.", "See it from the outside for certain. A tour only if you care about the halls.", "Sydney Opera House"),
        sight("Sydney Harbour Bridge", "The other half of the same view. Walk across if the group is up for it.", "The pedestrian path is the southeast side. It is a walk, not the bridge climb, which is a separate paid production.", "Sydney Harbour Bridge"),
        sight("Darling Harbour", "The waterfront next to Adina and near Meriton. Easy with children, and not the harbor's finest view.", "Use it for a playground hour, then go to Circular Quay for the real prospect.", "Darling Harbour"),
        sight("Manly, New South Wales", "The ferry destination: a beach at the other end of a beautiful ride.", "Check the surf flags. The ferry back is the plan, not a bus saga.", "Manly, New South Wales"),
        sight("Bondi Beach", "The famous sand, visited and left.", "Morning. The coastal walk south is optional and can be turned around.", "Bondi Beach"),
        sight("Royal Botanic Garden, Sydney", "The green edge between the Quay and the Domain.", "Free, and the right last morning.", "Royal Botanic Garden, Sydney"),
    ],
    scenic_routes=[
        route("Ferry to Manly", "Circular Quay to Manly Wharf. The Opera House, the heads, and the Pacific at the end of the ride.", "About 30 minutes each way"),
        route("Bridge walk", "From The Rocks, across the Harbour Bridge pedestrian path and back, or on to Milsons Point and a train.", "About 2 km one way"),
        route("Bus to Bondi", "From the city to Bondi Beach. This is the outing that proves the apartment did not need to be on the sand.", "About 40 minutes, longer in traffic"),
    ],
    transport="Walk, ferry, bus, and train. An Opal card covers all of them. A car in The Rocks and Darling Harbour is a parking problem. The airport train is the sane arrival and departure if you can handle the luggage. With small children and a lot of bags, a car transfer is the exception.",
    food=[
        dish("Apartment breakfast", "Your kitchen", "Eggs, toast, fruit. Buy them the first afternoon. A hotel breakfast buffet is not the reason you booked a kitchen."),
        dish("Fish and chips", "Manly, or Doyle's at Watson's Bay if you ferry there instead one day", "Eat it by the water. One harbor lunch is the ceremonial meal."),
        dish("A roast chicken dinner", "The apartment, from a supermarket rotisserie", "The family night. Salad, bread, done. This is allowed."),
        dish("Meat pie", "A bakery in The Rocks or the CBD", "Lunch on the walk day. One each. It is a snack with a crust, not a restaurant."),
    ],
    tips=[
        "Book an apartment, not a studio, if you need a real kitchen. Adina and Meriton both draw that line in the room type.",
        "Bondi is a good morning and a bad base for this search. You would give up the ferry and the kitchen-to-Quay walk.",
        "The harbor swim and the ocean swim are different. Manly and Bondi have surf and flags. Darling Harbour is not a beach.",
        "School holidays and New Year change both the rates and the ferries. Book the apartment before you promise the children a date.",
    ],
    faqs=[
        faq("Can we stay in Bondi and still have a kitchen?", "Yes, in a flat, and you will spend the trip on the bus. This page keeps the apartment in the city and sends you to Bondi once."),
        faq("Is the Opera House walkable from Darling Harbour?", "It is a meaningful walk, fine for adults and a lot for small children. The ferry or a short bus from the Quay side is easier if you are at Kent Street."),
        faq("Do we need a car?", "No. A car seat is the only good argument, and parking is the rebuttal. Ferries are the point."),
        faq("What does the apartment cost?", "Often $220–450 a night for a one- or two-bedroom, more in school holidays and December. The kitchen saves breakfast and at least one dinner a day."),
    ],
    map_places=[
        stop("Sydney Opera House", "Sydney", "Australia", "Sydney Opera House"),
        stop("Sydney Harbour Bridge", "Sydney", "Australia", "Sydney Harbour Bridge"),
        stop("Darling Harbour", "Sydney", "Australia", "Darling Harbour"),
        stop("Bondi Beach", "Sydney", "Australia", "Bondi Beach"),
        stop("Manly", "Sydney", "Australia", "Manly, New South Wales"),
    ],
    budget_notes="A city apartment with a kitchen is often $220–450, higher in December and January. Groceries and one takeaway dinner keep food in a family range. Ferries and the airport train are small next to a week of taxis. The bridge climb and Taronga Zoo are optional tickets, not required for the harbor to work.",
))

add(trip(
    slug="new-york-family-friendly-with-kitchen",
    title="New York with a kitchen, one borough day, and one museum",
    location="New York, United States",
    summary=(
        "Four nights in a Manhattan apartment hotel with a kitchen, so dinner is not a restaurant every night and "
        "breakfast is not a $40 mistake. The days are a neighborhood, one museum, a park, and a single borough outing "
        "in Brooklyn. Four museums is not a family plan. Times Square is not the base."
    ),
    who="Parents who want a real kitchen or a kitchenette suite and a schedule children can survive.",
    best_time="April to June, and September to early November. Summer is hot and crowded. Late December is a different, more expensive city.",
    nights=4,
    hook="4 nights · Kitchen suite · One museum, one Brooklyn day",
    constraints=["Kitchen or real kitchenette", "Not four museums", "Not a Times Square base"],
    lodging="$280–550",
    daily="$420–700",
    neighborhoods=[
        stay_area("Upper West Side", "Hotel Beacon is at 75th and Broadway, a walk to Central Park and one museum if you want it. Groceries are on the avenue."),
        stay_area("Murray Hill or downtown", "The Marmara is a Park Avenue extended stay. A downtown Residence Inn puts you near the subway to Brooklyn. Either beats a room over Times Square."),
    ],
    hotels=[
        hotel("Hotel Beacon", "Upper West Side, Broadway at 75th", "Two-room suites with kitchenettes on the Upper West Side. A bedroom and a separate sitting room is the family layout. You can walk to the park. You do not need a second museum to justify the address.", "$250–480", "New York"),
        hotel("The Marmara Park Avenue", "Murray Hill", "Extended-stay apartments with full kitchens. This is the true cook-in option: a stove, not just a microwave. A practical block of Park Avenue, not a view of a billboard.", "$300–600", "New York"),
        hotel("Residence Inn by Marriott New York Downtown Manhattan/World Trade Center Area", "Financial District", "Suites at 170 Broadway with full kitchenettes: a stovetop, a microwave, and a fridge. Downtown is quiet at night and an easy subway to Brooklyn. Book a suite large enough that someone is not sleeping in the kitchen.", "$280–520", "New York"),
    ],
    itinerary=[
        day(1, "The apartment works", "Groceries first, skyline second.", "Check in and find the nearest grocery. Milk, fruit, bread, something for dinner.", "A short walk. From the Beacon, that is a piece of Central Park. From downtown, it is the water at Battery Park and then home.", "Cook, or a slice of pizza you carry back. The first night is not a tasting menu.", "Ask how the kitchen is equipped. A kitchenette without a pot is a surprise you can fix on hour one.", "Central Park"),
        day(2, "One museum", "A single ticketed morning, then nothing else with a line.", "American Museum of Natural History if you are on the Upper West Side. If you are downtown, pick that museum and take the subway, or skip it and do the Statue of Liberty ferry only if you already have tickets.", "Playground or the park. Children need the unscheduled part.", "Dinner in. Pasta is a complete New York evening when you have a kitchen.", "Do not add the Met after the Natural History. That is how family trips go sour.", "American Museum of Natural History"),
        day(3, "One borough: Brooklyn", "Leave Manhattan for a day and come back to the same kitchen.", "Subway to Brooklyn Heights. Walk the promenade.", "A pizza in Brooklyn, then Prospect Park or a bookstore and home. You do not need DUMBO and Coney Island and a third neighborhood.", "Cook again, or eat the leftovers. The subway home is the evening.", "The promenade is windy. It is still the right Brooklyn hour.", "Brooklyn Heights"),
        day(4, "A slow morning and a train", "Leave without a farewell museum.", "A park hour or a diner breakfast near the apartment. Use up the groceries.", "Subway to the airport or a car if the luggage and the children require it. LaGuardia and JFK are not the same trip.", "Eat before security from what you already bought.", "Sunday subway changes are real. Check the route that morning.", "Brooklyn Bridge"),
    ],
    attractions=[
        sight("Central Park", "The backyard, especially from the Upper West Side.", "Enter at 72nd or 77th and do not try to see the whole park.", "Central Park"),
        sight("American Museum of Natural History", "The one museum. Dinosaurs are enough.", "Timed tickets. Two hours. Then leave.", "American Museum of Natural History"),
        sight("Brooklyn Heights", "The one borough outing: a promenade and a neighborhood.", "Walk the height, eat, return. Do not add a checklist.", "Brooklyn Heights"),
        sight("Brooklyn Bridge", "Best as a view from the promenade, or a walk if the group is fresh on a different day.", "Midday in summer on the bridge itself is a crowd. The promenade view is the family version.", "Brooklyn Bridge"),
        sight("Prospect Park (Brooklyn)", "The optional green hour after pizza, if Brooklyn Heights was not enough.", "Use the playground near the entrance you came from. Do not cross the whole park out of duty.", "Prospect Park (Brooklyn)"),
        sight("Statue of Liberty", "Only with ferry tickets you already hold. Otherwise see the skyline from Battery Park and move on.", "The crown and the pedestal are separate, timed, and a long half-day.", "Statue of Liberty"),
    ],
    scenic_routes=[
        route("Central Park, one loop", "From the Upper West Side into the park, south toward the lake or north toward the reservoir, and back. One direction.", "About 3 km"),
        route("Brooklyn Heights Promenade", "Subway to the Heights, along the promenade toward the bridge view, pizza, subway home.", "A walkable afternoon"),
        route("Downtown to the park", "If you are at the Residence Inn, the subway up to the museum and the park is the route. Do it once.", "About 30 minutes on the train"),
    ],
    transport="Subway, and walking. Buy a MetroCard or use OMNY. A car is for the airport if luggage demands it, not for Manhattan. Taxis with children are a tool when the subway stairs are impossible, not the default. Do not drive to Brooklyn Heights.",
    food=[
        dish("Pasta at the apartment", "Your kitchen", "The dinner that makes the hotel category worth it. One pot, early bedtime."),
        dish("Pizza slice", "A neighborhood slice shop, or one sit-down pie in Brooklyn", "One slice each is a snack. A pie is dinner. Do not do both plus a restaurant."),
        dish("Bagels", "A local shop in the morning", "The breakfast that is better than the groceries, one day. Eat it at the apartment if the shop has no seats."),
        dish("Halal cart or a simple chicken dinner", "A cart if you are already out, or roast chicken from a grocery", "The not-cooking backup. Not every night."),
    ],
    tips=[
        "One museum. The Natural History, or the ferry, or the Met. Not the set.",
        "A kitchenette with two pans is enough. A room with a mini-fridge is not this search.",
        "Brooklyn is one day. You still sleep in Manhattan, where the groceries are.",
        "Times Square is a place you might change trains. It is not a hotel choice for a family that wants to sleep.",
    ],
    faqs=[
        faq("Is the Beacon a full kitchen?", "It is a kitchenette suite: enough to make breakfast and a simple dinner. The Marmara's apartments are the fuller kitchen. Both beat a standard hotel room."),
        faq("Can we do the Statue of Liberty and a museum?", "Only by deleting the park time. Pick one ticketed thing on this trip."),
        faq("Which airport is easier?", "From the Upper West Side, neither is pleasant. A car service is reasonable on departure day. The subway is cheaper and harder with suitcases."),
        faq("What does this cost?", "A family suite with a kitchen in Manhattan is often $300–550. Cooking two dinners and breakfast is how it stays cheaper than four nights of restaurants."),
    ],
    map_places=[
        stop("Central Park", "New York", "United States", "Central Park"),
        stop("American Museum of Natural History", "New York", "United States", "American Museum of Natural History"),
        stop("Brooklyn Heights", "New York", "United States", "Brooklyn Heights"),
        stop("Brooklyn Bridge", "New York", "United States", "Brooklyn Bridge"),
        stop("Prospect Park", "New York", "United States", "Prospect Park (Brooklyn)"),
    ],
    budget_notes="The suite is the cost, often $300–550 in ordinary weeks and more in December and school holidays. Groceries for breakfast and two dinners matter more than another attraction. One museum ticket per person is the planned extra. Subway fares are small. A car to the airport is the right place to spend, if you spend on transport at all.",
))

add(trip(
    slug="new-york-pet-friendly",
    title="New York with a dog: three hotels that actually allow one",
    location="New York, United States",
    summary=(
        "Four nights at hotels that publish a dog policy, in a city where many apartment buildings do not allow dogs "
        "at all. Loews Regency takes two pets for a flat stay fee. The Pierre takes small dogs and charges by the night. "
        "Archer takes one small dog and a cleaning deposit. The walks are park edges and dog runs, not a march up Fifth Avenue."
    ),
    who="People bringing a dog who need a hotel that will say yes in writing, and a plan that does not depend on restaurant patios.",
    best_time="April to June, and September to October, when the pavement is not brutal and the parks are pleasant. July heat and January salt are both hard on paws.",
    nights=4,
    hook="4 nights · Hotels that allow dogs · Dog runs, not building bans",
    constraints=["Published pet policy", "Weight and fee confirmed", "Many buildings say no; these hotels do not"],
    lodging="$300–800",
    daily="$450–950",
    neighborhoods=[
        stay_area("Upper East Side at 61st", "Loews Regency and The Pierre are next to Central Park. This is the easiest serious walk in the city."),
        stay_area("West 38th Street", "Archer is in the Garment District, which is not romantic and is practical. The Madison Square dog run is about a mile south."),
    ],
    hotels=[
        hotel("Loews Regency New York", "Park Avenue at 61st", "A famous pet hotel. Up to two pets, a one-time fee of $150 per stay, and no weight limit on the hotel's own policy page. Bowls and a pet menu. You are across from Central Park.", "$400–800", "New York"),
        hotel("The Pierre", "Fifth Avenue at 61st", "Dogs only, up to 15 pounds, no more than two, at $75 per dog per night. Not in the restaurants or the fitness center. Dogs cannot be left alone in the room. You sign a waiver. Central Park is the walk.", "$500–1,000", "New York"),
        hotel("Archer Hotel New York", "45 West 38th Street", "One dog up to 15 pounds and a $250 nonrefundable cleaning deposit per stay. The house policy allows an emotional-support dog up to 50 pounds and another page says 15. Confirm which limit they will honor. Service animals are not charged.", "$250–500", "New York"),
    ],
    itinerary=[
        day(1, "A short walk and the rules", "Confirm the fee, the weight, and where the dog can go, then keep the first walk easy.", "Check in. Ask which elevator and which door. At the Pierre, remember the dog cannot be left alone.", "A first walk on the park edge if you are at 61st, or a short block loop if you are at Archer. Do not aim for a skyline.", "Dinner. Most of these dining rooms do not allow dogs. One person stays, or you use room service, or you eat at an outdoor table that has said yes.", "Pavement in summer: test it with your hand. Paw burns are the stupid injury.", "Central Park"),
        day(2, "The park, properly", "The best walk in the city is Central Park, on a leash, with water.", "Enter near 61st or subway up from 38th Street. Walk the drive or a path along the south end. The Ramble is tangled and not the best first dog walk.", "A rest in the room during the hottest or coldest part of the day. Dogs need the off-hours too.", "Madison Square's dog run if you want an off-leash hour and your dog is a dog-run dog. Otherwise repeat a calmer park edge.", "Dog runs have their own rules and busy times. A leash walk is the default.", "Madison Square and Madison Square Park"),
        day(3, "Downtown, with an exit", "A neighborhood walk that includes a plan for when the dog has had enough.", "Tompkins Square Park has a historic dog run. Go if a downtown hour sounds good, by subway only if the dog is subway-calm. Many dogs should take a car.", "Leave before it becomes an endurance event. A bookstore or a coffee for the human, then home.", "Night walk near the hotel only. New York at night is fine on a known block and pointless as a tour with a tired dog.", "Not every taxi will take a dog cheerfully. A car service you have already told is kinder.", "Tompkins Square Park"),
        day(4, "One last park edge", "Departure is a car, not a subway with a crate and a suitcase.", "A morning walk. If you are flying, this walk is short.", "Car to the airport. Tell them there is a dog when you book it.", "Papers, water, and a towel. Eat.", "Do not plan the Statue of Liberty. The ferry is not a dog plan.", "Hudson River"),
    ],
    attractions=[
        sight("Central Park", "The walk. South end from 61st is enough; the whole park is not the assignment.", "Leash laws apply. Carry water and bags.", "Central Park"),
        sight("Madison Square and Madison Square Park", "A smaller park, and a dog run nearby, useful from Archer.", "The run is for dogs that already like dog runs.", "Madison Square and Madison Square Park"),
        sight("Tompkins Square Park", "The downtown dog-run outing.", "Go and leave. The East Village is a lot of stimulation for one hour.", "Tompkins Square Park"),
        sight("Hudson River", "The west-side path, a calmer alternative walk if the park is packed.", "Enter at the nearest access and do an out-and-back, not a pilgrimage to the tip of the island.", "Hudson River"),
        sight("Brooklyn Bridge", "A human view you can skip with a dog. The crowds and the stairs are a poor match.", "See it from a distance or on a different, dogless trip.", "Brooklyn Bridge"),
        sight("The High Line", "Not a reliable dog plan. Skip it rather than discover the rule at the entrance.", "Use the park and the runs instead.", "High Line"),
    ],
    scenic_routes=[
        route("61st into Central Park", "From the Regency or the Pierre, across Fifth or up Park, into the south end of the park and back.", "1–3 km"),
        route("Archer to Madison Square", "Down toward 23rd for the dog run, then straight back to 38th. A mile is enough.", "About 2 km each way"),
        route("Hudson River out-and-back", "A car or a crosstown walk to the river path, a short north or south, and home.", "An hour"),
    ],
    transport="Walk the walks. Use a car service for the airport, for Tompkins if the dog hates the subway, and for anywhere with a lot of stairs. The subway can be fine for a calm dog at off-peak and miserable otherwise. Do not plan on taxis as a system; some drivers dislike dogs. Tell the car company in advance.",
    food=[
        dish("Room service or takeout", "The hotel, or a place that will pack the meal", "The Pierre's restaurants are not dog dining rooms. Plan the meal as if the dog is eating in the room, because the dog is."),
        dish("A slice, carried out", "A pizza counter on the walk home", "Eat it in the room. A crowded slice shop is not a dog cafe."),
        dish("Bagel breakfast", "A shop, then the room", "One person can run down for bagels. This is the easy morning."),
        dish("A reserved dinner for the humans", "A restaurant, only with a dog plan", "Either a sitter, a person who stays, or an outdoor table that confirmed the dog. Do not improvise this at 8 p.m."),
    ],
    tips=[
        "Get the policy in writing: weight, number of pets, fee, and whether the dog can be left in the room. The Pierre says no. Loews is built for the opposite.",
        "Archer's two official pages do not match on emotional-support weight. Confirm before you fly a 40-pound dog into a 15-pound rule.",
        "Many residential buildings ban dogs. That is why this is a hotel trip. Do not switch to a random walk-up because the photos were nice.",
        "Summer pavement and winter salt both hurt paws. Walk early, wipe feet, carry water.",
    ],
    faqs=[
        faq("Can I leave the dog in the room?", "At the Pierre, no. At the others, ask and assume you need a walker if you will be gone long. Housekeeping and a dog alone is the conflict."),
        faq("Are restaurants an option?", "Usually not inside. Outdoor seating is a case-by-case yes. Room service is the dependable dinner."),
        faq("Is Central Park off-leash?", "Only in specific hours and places, and those rules change. A leash is the plan. Dog runs are the off-leash option."),
        faq("What does the fee add?", "About $150 per stay at the Regency, $75 per dog per night at the Pierre, and a $250 deposit at Archer. Small next to the room, and mandatory."),
    ],
    map_places=[
        stop("Central Park", "New York", "United States", "Central Park"),
        stop("Madison Square Park", "New York", "United States", "Madison Square and Madison Square Park"),
        stop("Tompkins Square Park", "New York", "United States", "Tompkins Square Park"),
        stop("Hudson River", "New York", "United States", "Hudson River"),
        stop("High Line", "New York", "United States", "High Line"),
    ],
    budget_notes="These are expensive Manhattan hotels, often $300–800, plus a pet fee that is annoying and not the main cost. A dog walker is the extra if you want a museum or a real dinner. Budget for a car to the airport. Meals can be takeout. Do not add a boarding kennel unless you actually want one; the point was to bring the dog.",
))

add(trip(
    slug="new-york-quiet-romantic-getaway",
    title="A quiet New York weekend: the Village, a reservation, an empty bridge",
    location="New York, United States",
    summary=(
        "Three nights that stay out of Times Square. The Greenwich Hotel and The Marlton are the quiet choices, in "
        "Tribeca and the Village. The Ludlow is the stylish one on a louder street, so ask for a high room off the "
        "avenue. The plan is a walk, one reserved dinner, and the Brooklyn Bridge at a sane hour."
    ),
    who="A couple who want New York at conversation volume and will book dinner before they book anything cute.",
    best_time="April to June, and September to October. A winter weekend can be quiet and beautiful if you like coats. New Year's Eve is the opposite of this trip.",
    nights=3,
    hook="3 nights · Village and Tribeca · Dinner booked, bridge at a sane hour",
    constraints=["Not Times Square", "One reservation", "The bridge is not a midnight dare"],
    lodging="$350–900",
    daily="$500–1,100",
    neighborhoods=[
        stay_area("Tribeca and the West Village", "The Greenwich Hotel and The Marlton put you in walkable, low-rise streets. This is the getaway version of Manhattan."),
        stay_area("Lower East Side", "The Ludlow is here. The hotel is good and the sidewalk on a Saturday is not quiet. A high floor is the request."),
    ],
    hotels=[
        hotel("The Greenwich Hotel", "Tribeca", "A courtyard hotel in Tribeca. Quiet, residential, and the right first choice if the word getaway is serious. You can walk to the Village and to the river.", "$600–1,100", "New York"),
        hotel("The Marlton Hotel", "Greenwich Village", "A small historic hotel on West 8th Street. Rooms are small. The Village outside is the point, and it is much quieter than midtown without being asleep.", "$280–500", "New York"),
        hotel("The Ludlow", "Lower East Side", "A design hotel on a street that stays up later. Ask for a high floor away from the avenue if you want the room to match the rest of this trip. The neighborhood is the trade.", "$300–600", "New York"),
    ],
    itinerary=[
        day(1, "Drop the bags and walk until dinner", "No itinerary with a logo. Just the neighborhood.", "Check in. If you are at the Marlton, walk Washington Square and the small streets west of it. If you are in Tribeca, walk the river and then up into the Village.", "A long, aimless hour. Bookshops, a coffee, a bench. This is the trip.", "The dinner you reserved. One sitting, somewhere you chose weeks ago, close enough to walk home.", "If you did not reserve, you are now in the wrong city for spontaneity at 8 p.m. Fix it before you land.", "Greenwich Village"),
        day(2, "The bridge in daylight", "Cross the Brooklyn Bridge when it is a walk, not a crowd event.", "Late morning on the bridge, from the Brooklyn side if you want the classic approach toward Manhattan, or from City Hall if you are already downtown. Weekday hours are kinder than Saturday noon.", "Brooklyn Heights Promenade for a few blocks, then a late lunch, then back.", "A drink near the hotel, not a second neighborhood. The night is for the room and an early morning.", "Sunset can be lovely and it can be a crush. If the path looks packed, look from the promenade instead.", "Brooklyn Bridge"),
        day(3, "A last Village morning", "Leave from downtown without a midtown errand.", "Coffee and a final walk. The West Village in the morning is the picture you wanted.", "Train, car, or subway to the airport with more time than the map says. Do not add a museum.", "You are done. A quiet trip ends quietly.", "Penn Station and Times Square are not required to leave New York. Keep it that way.", "Hudson River"),
    ],
    attractions=[
        sight("Greenwich Village", "The walkable point of the stay. Streets, not a single building.", "Morning and late afternoon. Saturday night is busier and still not Times Square.", "Greenwich Village"),
        sight("Brooklyn Bridge", "The one monument, walked at a sane hour.", "Weekday late morning, or the promenade view if the path is a parade.", "Brooklyn Bridge"),
        sight("Brooklyn Heights", "The quiet continuation of the bridge walk.", "A few blocks of the promenade and a lunch. Then go home.", "Brooklyn Heights"),
        sight("Hudson River", "The Tribeca and West Village waterfront, a flat walk with a wide sky.", "Sunset from a pier, then dinner. Do not turn it into a run to Midtown.", "Hudson River"),
        sight("The High Line", "Optional, and a little more planned than this trip needs.", "If you go, go early, walk a short section, and get off. It is not the romantic core.", "High Line"),
        sight("Washington Square Park", "The Village's living room. A half hour on a bench is a complete visit.", "You do not need a reason. The arch is right there.", ""),
    ],
    scenic_routes=[
        route("Village loops", "From The Marlton, west to Bedford and Grove, down to the river, back by a different street. Get lost on purpose.", "About 4 km"),
        route("Bridge and promenade", "Downtown to the Brooklyn Bridge, Brooklyn Heights Promenade, and a train or a walk back. The daylight version.", "About 4 km plus the crossing"),
        route("Tribeca river walk", "From The Greenwich Hotel to the Hudson piers and back through the side streets. The quiet romantic route that never sees a billboard.", "About 3 km"),
    ],
    transport="Walk. Downtown Manhattan is the rare place where a romantic weekend does not need a taxi except in the rain or with luggage. The subway is for the airport and for coming back from Brooklyn if you do not want to re-cross the bridge. A car service is for the flight.",
    food=[
        dish("The reserved dinner", "A Village or Tribeca restaurant you booked", "This is the meal the trip is built around. Tasting menu or a simple room, as long as the reservation is real."),
        dish("Coffee and a pastry", "A Village bakery in the morning", "Breakfast does not need a plan. Sit down only if you find seats."),
        dish("Lunch in Brooklyn Heights", "A small restaurant off the promenade", "Soup, a sandwich, a glass of wine. Then the train."),
        dish("A last breakfast", "Near the hotel", "Eggs and coffee. Do not try to fit a famous brunch line before a flight."),
    ],
    tips=[
        "Reserve dinner before you reserve anything whimsical. New York romance fails in a doorway with a two-hour wait.",
        "The Ludlow is the compromise hotel. If quiet is the actual goal, take the Greenwich or the Marlton and let the Lower East Side be a walk, not a bedroom.",
        "The bridge at 10 a.m. on a Tuesday is the romantic version. The bridge at midnight on a Saturday is a crowd with a view.",
        "Rooms at The Marlton are small. Fall in love with the street, not the square footage.",
    ],
    faqs=[
        faq("Is Times Square romantic at night?", "No. It is bright and crowded. This trip does not go there to check."),
        faq("Can we add a Broadway show?", "A matinee, maybe, if the dinner and the walk still fit. A show plus a club plus the bridge is a different weekend."),
        faq("Which hotel is actually quiet?", "The Greenwich Hotel. The Marlton is quiet for the Village. The Ludlow depends on the room and the night."),
        faq("How expensive is dinner?", "A serious reservation for two is often $200–400 before wine. Budget it. The rest of the day can be coffee and walking."),
    ],
    map_places=[
        stop("Greenwich Village", "New York", "United States", "Greenwich Village"),
        stop("Brooklyn Bridge", "New York", "United States", "Brooklyn Bridge"),
        stop("Brooklyn Heights", "New York", "United States", "Brooklyn Heights"),
        stop("Hudson River", "New York", "United States", "Hudson River"),
        stop("High Line", "New York", "United States", "High Line"),
    ],
    budget_notes="The hotel sets the range: The Marlton can be the relative deal, and The Greenwich Hotel is a splurge. The dinner reservation is the other planned cost. Walking is free. A car to the airport and a long lunch in Brooklyn are the rest. Three nights is the right length; a fourth becomes a city break with errands.",
))

add(trip(
    slug="new-york-luxury-with-ocean-view",
    title="Manhattan luxury looks at the park or the river, not the ocean",
    location="New York, United States",
    summary=(
        "Three nights at The Carlyle, The Mark, or Pendry Manhattan West. These are the correct luxury hotels, and "
        "none of them faces the Atlantic. Upper East Side rooms look at a street or toward the park. Pendry, if it "
        "sees water, sees the Hudson River. The ocean is a long subway ride to Rockaway, and it is not this hotel stay."
    ),
    who="Travelers who want a classic New York luxury hotel and will not be sold the Hudson as an ocean.",
    best_time="April to June, and September to November. December is festive and expensive. August is when a beach day is least miserable, and still a separate project from the hotel.",
    nights=3,
    hook="3 nights · Upper East Side or Hudson Yards · No ocean, on purpose",
    constraints=["Do not call the Hudson the ocean", "Park or river, named correctly", "A beach day is optional and long"],
    lodging="$600–1,400",
    daily="$800–1,700",
    neighborhoods=[
        stay_area("Upper East Side", "The Carlyle and The Mark are Madison Avenue hotels. The park is the landscape. The Atlantic is not on this map."),
        stay_area("Manhattan West", "Pendry is at Hudson Yards. The river to the west is the Hudson. It is wide, and it is a river."),
    ],
    hotels=[
        hotel("The Carlyle", "Upper East Side, Madison Avenue", "The classic. A Madison Avenue address with the park a block away. Rooms look at the street and the block. There is no ocean view to upsell, and the hotel does not need one.", "$700–1,500", "New York"),
        hotel("The Mark", "Upper East Side, Madison Avenue", "A luxury hotel on the same stretch of the Upper East Side. Park, galleries, and a quiet avenue. Book it for the hotel. If a listing says 'view,' ask view of what. It will not be the Atlantic.", "$650–1,400", "New York"),
        hotel("Pendry Manhattan West", "Hudson Yards", "A newer luxury hotel on the west side. Some rooms look toward the Hudson River and the city. A river view is worth having. It is not an ocean view, and the hotel should not be described as one.", "$500–1,100", "New York"),
    ],
    itinerary=[
        day(1, "The park, which is the view", "Arrive and use the landscape the hotel actually has.", "Check in. If you are on the Upper East Side, walk into Central Park at 72nd or 79th. If you are at Pendry, walk to the river and look at it honestly.", "A slow afternoon. One gallery or one shop, not a list.", "Dinner near the hotel, reserved. The Upper East Side has the restaurants. Hudson Yards has them too, and they are indoors.", "Ask for a park-side or river-side room only if you care about that specific thing. Do not ask for the ocean.", "Central Park"),
        day(2, "A civilized day", "One cultural stop and a long lunch. This is a luxury stay, not a borough survey.", "The Met, if you want a museum, for two hours. Or the Frick's neighborhood and no museum at all.", "Lunch, then back to the hotel. A nap is a valid use of a good room.", "A second reservation, or the hotel bar. You do not need to see Times Square to complete New York.", "The Met will expand to fill the day if you let it. Leave while you are still enjoying it.", "Metropolitan Museum of Art"),
        day(3, "Leave, or admit the beach is a project", "The ocean is the A train to Rockaway, more than an hour, and it does not fit a flight day.", "A last walk in the park or along the river. Coffee.", "Car or subway to the airport. If you have a whole extra day and a bathing suit, Rockaway is the honest Atlantic. It is not a cab from The Carlyle.", "You came for the hotel. The hotel delivered. The ocean was never in the borough in the way the search implied.", "Do not call a Hudson sunset an ocean sunset in the caption. The light is real. The geography is a river.", "Hudson River"),
    ],
    attractions=[
        sight("Central Park", "The view that belongs with The Carlyle and The Mark.", "Enter and wander. The Mall, the lake, the reservoir. You do not need a program.", "Central Park"),
        sight("Metropolitan Museum of Art", "The one museum that matches an Upper East Side hotel.", "Two hours, a single wing, then out. The building will still be there.", "Metropolitan Museum of Art"),
        sight("Hudson River", "The water Pendry can see. Wide, tidal, and a river.", "Walk the riverside path. Do not upgrade the noun.", "Hudson River"),
        sight("High Line", "A short walk from Hudson Yards, useful if you are at Pendry.", "Go early or accept the crowd. It is a park on a viaduct, not a coast.", "High Line"),
        sight("Madison Avenue", "The actual front door of the Upper East Side hotels.", "A walk from 60th toward the 70s is the neighborhood. You do not need to shop.", ""),
        sight("Rockaway Beach", "The real Atlantic, if you insist, on a day with no flight.", "The A train, more than an hour each way. A project, not an amenity.", "Rockaway Beach"),
    ],
    scenic_routes=[
        route("Park from Madison", "From The Carlyle or The Mark into Central Park and back by a different path. The luxury walk.", "About 3 km"),
        route("Hudson from Manhattan West", "From Pendry to the river path, north or south for half an hour, and back. Look at the river.", "About 3 km"),
        route("The A train, if you must", "Penn Station or a west-side A train to Rockaway. Only on a free day, with a plan to come back sandy and tired.", "More than an hour each way"),
    ],
    transport="Taxis and walking on the Upper East Side, walking and the subway from Hudson Yards. A car service to the airport is the luxury version of leaving. Do not rent a car to stare at a river. The beach, if attempted, is the subway, not a limousine fantasy of a nearby shore.",
    food=[
        dish("A reserved dinner", "An Upper East Side dining room, or a serious restaurant near Hudson Yards", "Book it. This hotel bracket does not pair well with wandering until you are hungry."),
        dish("Hotel breakfast", "The Carlyle, The Mark, or Pendry", "Eat it at least once. You are paying for the room to be pleasant in the morning."),
        dish("A long lunch", "Near the museum or the park", "The meal that replaces a second attraction. Sit down."),
        dish("A slice, if you want one", "Anywhere that is not trying too hard", "Even this trip can include a slice. Eat it on the way back to the hotel."),
    ],
    tips=[
        "The Atlantic does not touch Manhattan. The Hudson is a river. The East River is a river. The harbor is a harbor.",
        "A park view at The Carlyle or The Mark is the luxury view. Ask for it plainly.",
        "Rockaway is a real beach day and a poor add-on. Give it a full day or skip it without guilt.",
        "If you wanted a famous ocean hotel, this is the wrong search. The Hamptons are a different trip with a different train.",
    ],
    faqs=[
        faq("Which room faces the ocean?", "None. A west-facing Pendry room can face the Hudson. An Upper East Side room can face the park or Madison Avenue."),
        faq("Is the harbor close enough to count?", "Battery Park looks at the harbor, and these hotels are not there. You can visit. You should not rebrand the visit as an ocean-view stay."),
        faq("Can we do Rockaway from The Carlyle?", "Yes, badly. It is a cross-town trip plus a long subway, and then you do it again in reverse. Only if the day is empty."),
        faq("Why these hotels, then?", "Because they are the right luxury hotels. The search term was wrong about the water, not about the city."),
    ],
    map_places=[
        stop("Central Park", "New York", "United States", "Central Park"),
        stop("Metropolitan Museum of Art", "New York", "United States", "Metropolitan Museum of Art"),
        stop("Hudson River", "New York", "United States", "Hudson River"),
        stop("High Line", "New York", "United States", "High Line"),
        stop("Rockaway Beach", "New York", "United States", "Rockaway Beach"),
    ],
    budget_notes="These rooms are often $600–1,400 a night. Dinner for two at this level is easy to take past $300. Breakfast in the hotel is not cheap and is part of the stay. The park is free. A Rockaway day adds subway fares and a beach dinner, and it is optional. The mistake to avoid is paying a premium for a view that was mislabeled.",
))

add(trip(
    slug="new-york-mountain-or-nature-view",
    title="Nature from New York: the Ramble, then a train to Dia Beacon",
    location="New York, United States",
    summary=(
        "Four nights in Manhattan with nature treated as a real plan, not a cabin that does not exist. Central Park "
        "and the Ramble are the city half. One day is a Metro-North train to Dia Beacon. Storm King is only if you "
        "add a taxi from Beacon, because it is not next door. This is not the Adirondacks, and it is not a fake Catskills loft."
    ),
    who="Travelers who want trees, sculpture, and a river valley without pretending they slept in a mountain lodge.",
    best_time="May to June, and September to October, when the Hudson Valley is green or turning and the park is at its best. Winter is handsome and stark. August in the city is the weak version.",
    nights=4,
    hook="4 nights · Central Park and a train to Beacon · Not a fake cabin",
    constraints=["Stay in the city", "Dia Beacon is the train day", "Storm King needs a car or a taxi"],
    lodging="$250–550",
    daily="$380–650",
    neighborhoods=[
        stay_area("Central Park South and the Upper East Side", "1 Hotel Central Park and The Surrey put the park outside. The Ramble is a walk, not a transfer."),
        stay_area("Chelsea", "The High Line Hotel is a former seminary with a courtyard, useful if you want quieter streets and do not mind a subway to the park."),
    ],
    hotels=[
        hotel("1 Hotel Central Park", "Central Park South", "Across the street from the park, with a nature-minded building rather than a nature fantasy. The view is the park and the city. You are not in the mountains. You are next to them in the only sense Manhattan allows.", "$400–800", "New York"),
        hotel("The Surrey", "Upper East Side", "A quiet hotel a short walk from the park. The right choice if you want the Ramble before breakfast-time crowds and a calm block at night.", "$350–700", "New York"),
        hotel("The High Line Hotel", "Chelsea", "A former seminary with a garden courtyard. Quiet, a little apart from midtown, and an easy walk to the High Line. The nature day still requires a train north.", "$250–500", "New York"),
    ],
    itinerary=[
        day(1, "The Ramble, slowly", "Use the park as a place, not a backdrop on the way to a museum.", "Drop bags. Enter the park and walk to the Ramble. Stay on paths. It is a woodland in the middle of the island, and it is enough for the afternoon.", "The Lake, or the reservoir if you want a bigger sky. One loop.", "Dinner near the hotel. You do not need to go downtown to complete the day.", "The Ramble is confusing on purpose. Note your exit before you wander.", "Central Park"),
        day(2, "Metro-North to Dia Beacon", "The nature day that leaves the city by train.", "Grand Central to Beacon on Metro-North. It is about an hour and a half. Sit on the river side.", "Dia Beacon, the contemporary art museum in a former box factory. Give it the unhurried afternoon it wants.", "Train back. Dinner late, near the hotel, simple.", "Storm King Art Center is not in Beacon. It is a taxi or a car away, in Cornwall. Do not promise yourself both unless you have that ride booked.", "Dia Beacon"),
        day(3, "The Cloisters, which is a park with a museum", "Fort Tryon is the other nature hour inside the city limits.", "Subway and bus, or a car, to The Cloisters. The gardens and Fort Tryon Park are half the point.", "A slow visit. Then back. Do not add the Met on the same day.", "A walk on the High Line only if you are staying in Chelsea and still feel like walking. Otherwise the evening is done.", "The Cloisters is a half-day. Treat the trip uptown as part of the visit, not a nuisance.", "The Cloisters"),
        day(4, "One more morning in the trees", "Leave from the park, not from a store.", "A last short walk: the Ramble again, or Conservatory Garden if you are on the Upper East Side.", "Airport. A car is reasonable with luggage. The subway is reasonable without it.", "You did not need a cabin. The park and the river valley were the trip.", "If you want Storm King, it replaces Dia or the Cloisters. It does not get added on the flight morning.", "Storm King Art Center"),
    ],
    attractions=[
        sight("Central Park", "The nature in the city. The Ramble is the part that feels like woods.", "Weekday morning. Stay on paths and leave with daylight if you do not know the trails.", "Central Park"),
        sight("Dia Beacon", "The reason to take the train. Art in a vast old factory by the river.", "Check the closed days. Mondays and some holidays will wreck this plan.", "Dia Beacon"),
        sight("Storm King Art Center", "Sculpture in a huge meadow, near Beacon and not in it.", "A taxi from the Beacon station, or a car. Walking from the station is not the plan.", "Storm King Art Center"),
        sight("The Cloisters", "Medieval rooms and gardens at the top of Manhattan, inside Fort Tryon Park.", "Combine with the park, not with a second museum.", "The Cloisters"),
        sight("High Line", "A raised park, best as a short walk from the Chelsea hotel.", "It is urban planting, not a wilderness. Enjoy it for what it is.", "High Line"),
        sight("Hudson River", "The river you see from the train window on the way to Beacon.", "The river side of the carriage is the scenic side going north.", "Hudson River"),
    ],
    scenic_routes=[
        route("The Ramble", "Enter from the west or east at the 70s and wander the paths around the Lake. Out the way you came if you get turned around.", "About 2–3 km"),
        route("Hudson Line to Beacon", "Grand Central to Beacon. The river appears and stays with you for much of the ride.", "About 90 minutes"),
        route("Fort Tryon to The Cloisters", "From the subway and bus end, through the park to the museum. The approach is part of the visit.", "A slow half hour on foot at the end"),
    ],
    transport="Subway in the city, Metro-North for Beacon. Buy the train ticket before you board. A taxi from Beacon to Storm King is a real cost; budget it or do not go. The High Line is a walk. A car in Manhattan is unnecessary. A car service to the airport is the one road transfer worth paying for.",
    food=[
        dish("A diner or a cafe near the park", "Upper East Side or Central Park South", "Breakfast before the Ramble. Keep it ordinary."),
        dish("Lunch in Beacon", "A place in the town after Dia, or the museum cafe if you are deep in the building", "You have time. The train back can be the early evening one."),
        dish("Pizza or a simple dinner", "Near the hotel, after the train", "You will be tired. Do not book a fragile reservation for 8:30."),
        dish("A packed snack", "For the train", "Coffee and something portable. The Hudson Line is not a dining car you should count on."),
    ],
    tips=[
        "Dia Beacon is often closed on Monday. Check before you lock the day.",
        "Storm King and Dia are a car day, or two separate days. They are not a stroll from one ticket to the other.",
        "This is not Mohonk and not a Catskills cabin. Those are real trips if you leave the city and stay there. This one stays in New York and uses the train.",
        "The Ramble after dark is not a romantic idea. Walk it by day.",
    ],
    faqs=[
        faq("Is this the Adirondacks?", "No. The Adirondacks are many hours north. This is Central Park plus the Hudson Valley by train."),
        faq("Can I see mountains from the hotel?", "You can see the park, and from some west-side points the river and the Palisades. You cannot see a summit range from a Manhattan room in any way that matters."),
        faq("Is Bear Mountain instead of Beacon all right?", "Yes, as a different day, usually by bus or car. Do not try to add it to Dia. Pick one outing north."),
        faq("What if I wanted a lodge?", "Mohonk Mountain House, about two hours north, is a real mountain hotel. It is a different trip. This page does not pretend a Chelsea courtyard is that."),
    ],
    map_places=[
        stop("Central Park", "New York", "United States", "Central Park"),
        stop("Dia Beacon", "Beacon", "United States", "Dia Beacon"),
        stop("Storm King Art Center", "New Windsor", "United States", "Storm King Art Center"),
        stop("The Cloisters", "New York", "United States", "The Cloisters"),
        stop("High Line", "New York", "United States", "High Line"),
    ],
    budget_notes="Hotels near the park at this level are often $250–700. Metro-North is the bargain of the trip. Dia tickets and, if you add it, a taxi to Storm King are the extras. Food can stay moderate because several meals are ordinary. The Cloisters has an entrance fee. You do not need a rental car unless Storm King becomes the point.",
))

add(trip(
    slug="los-angeles-2-bedroom-under-400night",
    title="A two-bedroom in Los Angeles under $400, with a car or a rideshare",
    location="Los Angeles, United States",
    summary=(
        "Four nights in a real two-bedroom with a kitchen, at a rate that can sit under $400 outside summer weekends "
        "and awards season. One option is downtown, one is a Marina del Rey apartment, and one is Pasadena. Santa Monica "
        "on a July weekend is not this budget. None of these is a Bel-Air villa. You will drive or call a car."
    ),
    who="Two couples, or a family, who need two bedrooms and will trade a beach address for a rate that holds.",
    best_time="January to March, outside holiday weekends, is when the rate is most believable. Summer weekends and any week a major award or convention lands will break $400, especially near the sand.",
    nights=4,
    hook="4 nights · Two bedrooms · Under $400 off-peak, and you need a car",
    constraints=["Actual two bedrooms", "Under $400 only on the right dates", "Not a Bel-Air house"],
    lodging="$180–400",
    daily="$280–480",
    neighborhoods=[
        stay_area("Downtown", "The Residence Inn at L.A. LIVE is the reliable two-bedroom suite. You are next to an arena, not a beach. Rideshare to everything else."),
        stay_area("Pasadena", "The other Residence Inn holds the budget more often. Griffith is a drive. Santa Monica is a longer drive. Say that when you book it."),
    ],
    hotels=[
        hotel("Residence Inn by Marriott Los Angeles L.A. LIVE", "Downtown, Olympic Boulevard", "A real two-bedroom suite with a full kitchen, next to the convention center and the arena. Under $400 is realistic when nothing big is in town, and it disappears on event nights. This is not Santa Monica.", "$180–400", "Los Angeles"),
        hotel("Oakwood Marina del Rey", "Marina del Rey", "Furnished apartments, including two-bedrooms with full kitchens, a short hop from the marina beach. Older published rates sat under $400. Confirm the building is still taking short stays under this name before you depend on it.", "$200–450", "Los Angeles"),
        hotel("Residence Inn by Marriott Los Angeles Pasadena/Old Town", "Pasadena", "Book the two-bedroom suite, not the studio. Pasadena is where this budget survives more often. The beach is a car trip. A Santa Monica two-bedroom under $400 is a winter weekday, not a plan.", "$170–380", "Los Angeles"),
    ],
    itinerary=[
        day(1, "The apartment, then one neighborhood", "Do not start with a freeway tour.", "Check in, confirm you have two doors that close and a kitchen that has pans.", "A grocery run. In Los Angeles this is a car or a rideshare, not a stroll, unless you are lucky.", "Cook. The two-bedroom only makes financial sense if you are not also buying four restaurant dinners.", "Parking fees at downtown hotels can wreck a rate that looked under $400. Ask.", "Griffith Observatory"),
        day(2, "The beach, as a drive", "You do not sleep on the sand. You go there in the morning.", "Santa Monica in the morning, before the lot situation gets ugly. A walk on the pier or the sand, then leave.", "Back to the apartment for the middle of the day. Work, or do nothing. The second bedroom is for this.", "Dinner in, or tacos nearby. A rideshare both ways is the transport.", "Summer weekends: if the rate broke $400, you are in the wrong week, not the wrong mood.", "Santa Monica Pier"),
        day(3, "One sight, by car", "Griffith, or a museum, not both plus a studio tour.", "Griffith Observatory in the morning for the view. The hike is optional and exposed.", "A supermarket and a quiet afternoon. Los Angeles rewards the apartment more than it rewards a third attraction.", "Cook something larger. Invite the second bedroom's occupants to do the dishes.", "Observatory parking is a bottleneck. Rideshare or go early.", "Griffith Park"),
        day(4, "Leave on the freeway you already respect", "The airport is not 'nearby' in the way a map suggests at rush hour.", "A calm morning. Eat the remaining groceries.", "To LAX with more time than the mileage implies. A rideshare is the right tool. A rental car return adds its own line.", "You did not need a villa. You needed two bedrooms, and you had them if you booked the suite and not the studio.", "Check the suite type in the confirmation one more time before you arrive, not after.", "Getty Center"),
    ],
    attractions=[
        sight("Santa Monica Pier", "The beach outing, reached by car.", "Morning. Do not build the day around staying for sunset unless the apartment is truly close.", "Santa Monica Pier"),
        sight("Santa Monica State Beach", "The sand in front of the pier. A few hours, not a residence.", "Weekends are crowded. The water is cold.", "Santa Monica State Beach"),
        sight("Griffith Observatory", "The view over the basin. The one scenic drive of the trip.", "Early. A sunset visit is pretty and operationally worse.", "Griffith Observatory"),
        sight("Griffith Park", "The open space around the observatory, if you want a walk.", "Bring water. There is not much shade on the popular trails.", "Griffith Park"),
        sight("The Grove", "A useful downtown-of-the-west-side errand if you are driving past. Not a sight.", "Go only if you need something. It is a mall.", ""),
        sight("Getty Center", "The optional art-and-view morning, if you skipped Griffith. Not in addition, on a four-night trip with a kitchen to justify.", "The tram up is part of the visit. It takes a half day.", "Getty Center"),
    ],
    scenic_routes=[
        route("To the pier and back", "Apartment to Santa Monica in the morning and home before you are stuck in the return peak. The scenic part is the last mile.", "30–70 minutes, depending on the base and the hour"),
        route("To Griffith", "From downtown, Pasadena, or the marina, the drive is the route. The view is the reward. Do not chain it to a beach hour.", "30–60 minutes"),
        route("A non-freeway errand", "If you are in Pasadena, walk Old Town and do not get in the car until the beach day. The best mile of the trip may be the one you do not drive.", "A walkable hour"),
    ],
    transport="A car or a rideshare, every day you leave the block. Los Angeles distances are honest about this. Parking at the downtown Residence Inn and at the beach is part of the cost. A rental car makes Griffith and Santa Monica possible and makes the hotel parking fee hurt. Rideshare is saner if you will only go out once a day. Do not plan to walk between these neighborhoods.",
    food=[
        dish("Tacos", "A taqueria near wherever you actually are", "The right dinner on a night you do not cook. Order at the counter."),
        dish("Groceries and a cooked dinner", "The suite kitchen", "Two nights of this is the budget. Chicken, tortillas, salad, fruit."),
        dish("A beach snack", "Santa Monica, on the beach morning", "Eat something simple and leave. A long lunch on the sand is how the drive home gets worse."),
        dish("Breakfast in the suite", "Your kitchen", "Coffee you made. The under-$400 story collapses if every morning is a restaurant."),
    ],
    tips=[
        "The confirmation must say two bedrooms. A sofa bed in the living room is the trick this search falls for.",
        "Under $400 fails on summer weekends, award weeks, and big convention dates. Move the date or move to Pasadena.",
        "Santa Monica is the outing. Sleeping there in a true two-bedroom, in season, is a different budget.",
        "Ask about parking. A $50 nightly fee is part of the rate even when the website displays it separately.",
    ],
    faqs=[
        faq("Can I walk to the beach from these hotels?", "From Oakwood Marina del Rey, you are close to a marina beach and a rideshare from the ocean beach. From downtown and Pasadena, no."),
        faq("Is Oakwood still the name on the door?", "It has been a real two-bedroom apartment property. Confirm a current short-stay listing before you treat it as bookable. The Residence Inn suites are the safer contracts."),
        faq("Why not a Bel-Air house?", "Because a house in the hills is not under $400, and it is not a hotel with a front desk. This page is the apartment-hotel version."),
        faq("Do we need a car if we stay in Pasadena?", "For the beach and Griffith, yes. Old Town itself is walkable, which is the one relief."),
    ],
    map_places=[
        stop("Santa Monica Pier", "Los Angeles", "United States", "Santa Monica Pier"),
        stop("Griffith Observatory", "Los Angeles", "United States", "Griffith Observatory"),
        stop("Griffith Park", "Los Angeles", "United States", "Griffith Park"),
        stop("Santa Monica State Beach", "Los Angeles", "United States", "Santa Monica State Beach"),
        stop("Getty Center", "Los Angeles", "United States", "Getty Center"),
    ],
    budget_notes="A two-bedroom suite can be $180–350 when the city is quiet and over $400 the week you actually wanted. Parking and rideshares are the hidden daily cost, easily $40–80. Groceries keep food down. A rental car plus parking can erase the savings versus a smaller hotel in Santa Monica, so do the arithmetic before you commit to downtown.",
))

add(trip(
    slug="los-angeles-family-friendly-with-kitchen",
    title="Los Angeles with kids: a kitchen, Griffith, and a Santa Monica morning",
    location="Los Angeles, United States",
    summary=(
        "Four nights built for a family that wants to cook. Cal Mar has kitchen suites a walk from Santa Monica beach. "
        "Homewood Suites at the airport has full kitchens and a rideshare to the sand. A Residence Inn in Burbank is the "
        "kitchen nearer Griffith. Different buildings from the two-bedroom page. One beach morning, one observatory, and dinners at home."
    ),
    who="Parents who will drive or rideshare, want a kitchen, and would like the children to have both a beach and a view without a theme park.",
    best_time="March to May, and October to November. Summer is the beach season and the traffic season. Mornings are the only calm part of a July day.",
    nights=4,
    hook="4 nights · Family kitchen · Beach morning, Griffith once",
    constraints=["A kitchen you can cook dinner in", "Not the two-bedroom page's hotels", "Car or rideshare"],
    lodging="$180–420",
    daily="$300–520",
    neighborhoods=[
        stay_area("Santa Monica", "Cal Mar is the walk-to-the-beach version. The suites are bedrooms plus sofa beds, not two closed bedrooms, and the kitchen is real."),
        stay_area("Burbank or the airport", "The Burbank Residence Inn makes Griffith a shorter drive and the beach a real commute. Homewood at LAX splits the difference and feels like an airport until you leave it."),
    ],
    hotels=[
        hotel("Cal Mar Hotel Suites", "Santa Monica", "Suites with full kitchens, a pool, and a walk to the beach. The layout is a bedroom plus a sofa bed, which is why it is not on the two-bedroom page. For a family that mostly needs cooking and the sand, it fits.", "$200–400", "Los Angeles"),
        hotel("Homewood Suites by Hilton Los Angeles International Airport", "LAX / El Segundo side", "Homewood suites come with full kitchens. You are near the airport, not on the sand. A morning rideshare to Santa Monica is the beach plan, and Griffith is a longer ride. Useful, not glamorous.", "$160–320", "Los Angeles"),
        hotel("Residence Inn by Marriott Los Angeles Burbank/Downtown", "Burbank", "Residence Inn suites have full kitchens. Burbank puts Griffith on a shorter drive than Santa Monica does, and the beach becomes the morning you schedule. Not a walk to either. A different building from the Pasadena Residence Inn on the two-bedroom page.", "$170–340", "Los Angeles"),
    ],
    itinerary=[
        day(1, "Pool, grocery, early bedtime", "Make the suite function. The sights start tomorrow.", "Check in and confirm the kitchen has a stove, pots, and enough plates.", "Grocery store by car or rideshare. Breakfast food, a first dinner, snacks.", "Cook, swim if the pool is open, sleep. Santa Monica at night can wait.", "If you are at Homewood, the first evening is not the moment to 'just pop' to the beach. That is a morning.", "Santa Monica State Beach"),
        day(2, "Beach morning", "Sand early, home before everyone is sunburned and hungry.", "Santa Monica beach in the morning. If you are at Cal Mar, walk. If you are anywhere else, rideshare and arrive as it opens into the day.", "Back for lunch you make yourselves. The afternoon is the pool or a nap. This is the point of the kitchen.", "A simple dinner in the suite. Tacos only if cooking failed.", "Parking at the beach is the enemy. Walking from Cal Mar is the luxury.", "Santa Monica Pier"),
        day(3, "Griffith, once", "The view, not a hike competition.", "Drive or rideshare to Griffith Observatory in the morning. Look at the city, the sign from a distance, and the sky.", "A short walk in Griffith Park only if there is shade and patience. Then home.", "Cook the bigger dinner. The children have had their two outings.", "Do not add a studio tour. You will lose the afternoon the kitchen was meant to save.", "Griffith Observatory"),
        day(4, "One playground morning, then LAX", "Leave without a new neighborhood.", "A last swim or a last walk on the sand if the flight is late and you are in Santa Monica. Otherwise pack.", "To the airport. From Homewood this is the one easy transfer. From Burbank or Santa Monica, leave an honest margin.", "Eat the leftovers before you go.", "Sunday traffic toward LAX is not a theory. Look at the clock.", "Griffith Park"),
    ],
    attractions=[
        sight("Santa Monica State Beach", "The family swim and sand, in the morning.", "Flags, cool water, and a plan to leave for lunch at the suite.", "Santa Monica State Beach"),
        sight("Santa Monica Pier", "The amusement edge of the same morning, if the children ask.", "It is optional. The beach does not require the rides.", "Santa Monica Pier"),
        sight("Griffith Observatory", "The one view that makes the driving feel worthwhile.", "Morning. Bring layers. It is cooler and windier than the beach.", "Griffith Observatory"),
        sight("Griffith Park", "Open space around the observatory.", "A short walk, water, and no ambition to reach a summit with tired children.", "Griffith Park"),
        sight("La Brea Tar Pits", "The indoor-outdoor museum to add only if you are skipping something else. One extra, not a third day of attractions.", "It sits in Mid-Wilshire, a separate drive. Do not bolt it onto Griffith.", "La Brea Tar Pits"),
        sight("Venice Beach", "The nearer sand to some airport hotels, louder and less useful than Santa Monica for families.", "Prefer Santa Monica unless Venice is simply closer that morning.", "Venice Beach"),
    ],
    scenic_routes=[
        route("Walk to the sand", "From Cal Mar to Santa Monica beach in the morning and back when the children are done. The best route in the trip because it is not a freeway.", "Under 20 minutes each way"),
        route("Rideshare to Griffith", "From whichever hotel you chose. The view at the top is the scenery. The freeway is the cost.", "30–70 minutes"),
        route("A Burbank block", "If you stayed at the Burbank Residence Inn, walk the neighborhood once before anyone gets in a car. A family trip needs one hour that is not a back seat.", "An hour"),
    ],
    transport="Rideshare or a rental car. Santa Monica is the only base where the beach is a walk. Griffith is a drive from all three, shortest from Burbank. A car seat is the argument for renting. Hotel parking fees are the argument against it. LAX transfers from Burbank need a cushion. From Homewood they do not.",
    food=[
        dish("Suite breakfast", "Your kitchen", "Cereal, fruit, eggs. Buy it the first day. This is the meal that keeps the trip kind."),
        dish("Picnic lunch after the beach", "Back at the suite, not on a windy towel unless you love sand in the sandwiches", "The kitchen earns its keep at lunch."),
        dish("Tacos", "One night, from a shop you can walk to or briefly drive to", "The dinner you do not cook. Enough for everyone, eaten early."),
        dish("Pasta or rice dinner", "The suite, the Griffith night", "A normal dinner. The observatory was the event."),
    ],
    tips=[
        "Beach in the morning, Griffith on its own day, dinners at home. That is the whole structure. Resist a third signature outing.",
        "Cal Mar's sofa bed is fine for many families and wrong for people who needed a door that locks between bedrooms. Read this page and the two-bedroom page as different products.",
        "Heat, sun, and a long car ride are the fatigue. The pool afternoon is not laziness.",
        "Ask Homewood and the Burbank Residence Inn to confirm a full kitchen, not a microwave and a fridge only, on the room you are sent.",
    ],
    faqs=[
        faq("Why aren't these the same hotels as the two-bedroom list?", "Because a family kitchen trip and a strict two-bedroom budget trip are different stays. Cal Mar, Homewood, and the Burbank Residence Inn are this one."),
        faq("Can we do Disneyland?", "Not inside these four days without deleting the beach or Griffith. It is a separate trip."),
        faq("Is the Pacific warm?", "Not really. Children will still swim. Bring a towel they can actually get warm in."),
        faq("Which base is least annoying?", "Cal Mar if the beach is the priority and you accept the sofa-bed layout. Burbank if Griffith and a calmer evening matter more. Homewood if you want the airport easy and will rideshare out."),
    ],
    map_places=[
        stop("Santa Monica State Beach", "Los Angeles", "United States", "Santa Monica State Beach"),
        stop("Santa Monica Pier", "Los Angeles", "United States", "Santa Monica Pier"),
        stop("Griffith Observatory", "Los Angeles", "United States", "Griffith Observatory"),
        stop("Griffith Park", "Los Angeles", "United States", "Griffith Park"),
        stop("La Brea Tar Pits", "Los Angeles", "United States", "La Brea Tar Pits"),
    ],
    budget_notes="These kitchens are often $170–350 a night, more on summer weekends in Santa Monica. Groceries for breakfast and two dinners are the savings. Rideshares to the beach and Griffith can run $30–70 a round trip each. A rental car changes the math if parking is free at the hotel and brutal at the beach. Theme-park tickets are not in this budget because they are not in this trip.",
))

add(trip(
    slug="banff-city-center-walkable",
    title="Walkable Banff: sleep in town, and take the bus to Lake Louise",
    location="Banff, Canada",
    summary=(
        "Four nights in the town of Banff, which is small enough to walk. Moose Hotel, the Fox, and the Banff Inn are "
        "on the street grid. Fairmont Banff Springs is the famous castle up the hill, a shuttle or a long walk, so it "
        "is not the hotel for this page. One day goes to Lake Louise by bus, because the parking lot is not a plan."
    ),
    who="Travelers who want to step out to dinner and do not want a car sitting in a parkade.",
    best_time="June to September for the lakes and the long days, with the crowds that implies. Late September is calmer. Winter is a ski trip and a different walk, icy and early-dark.",
    nights=4,
    hook="4 nights · In town on foot · Lake Louise by bus",
    constraints=["Sleep in town", "No car required", "Lake Louise parking is not the plan"],
    lodging="$180–400",
    daily="$280–460",
    neighborhoods=[
        stay_area("Banff Avenue", "The whole walkable town: restaurants, the river, and the shops. Moose, Fox, and Banff Inn are here. You can be at dinner in five or fifteen minutes."),
        stay_area("The hill, which this page does not sleep on", "Banff Springs sits above the Bow. Go up for a look if you want. Sleeping there means a Roam bus back to dinner or a walk you will do once."),
    ],
    hotels=[
        hotel("Moose Hotel & Suites", "Banff Avenue", "At the edge of downtown, so the town is a walk. Rooftop hot pools look at the mountains and are shared. Suites exist if you need more than a room. This is the walkable luxury pick.", "$250–450", "Banff"),
        hotel("Fox Hotel & Suites", "Banff Avenue", "On the main street, with a grotto-style pool that is shared. You can do the whole trip from the door without a car.", "$200–400", "Banff"),
        hotel("Banff Inn", "Banff Avenue", "A simpler in-town hotel. Less famous than the castle, and much more walkable than the castle. The right room if the other two are priced like a weekend and you still want the street.", "$140–280", "Banff"),
    ],
    itinerary=[
        day(1, "Learn a town you can cross", "Arrive and walk until the map is in your feet.", "Check in. Walk Banff Avenue to the Bow River and back by a side street.", "Tunnel Mountain if you still have daylight and energy. The summit trail is short and steep, and the view is the town in its hole.", "Dinner on the avenue. You can walk home. That is the product.", "The Tunnel Mountain trail is a workout, not a stroll in sandals.", "Tunnel Mountain"),
        day(2, "Lake Louise, by bus", "The famous lake, without the fantasy of an empty parking lot.", "Roam transit, or the Parks Canada shuttle in peak season, from Banff to Lake Louise. Go early.", "Walk the lakeshore. Do not start the big hike unless you meant to. The rockpile view is the short version.", "Bus back in time for a normal dinner in town. The lake after 5 p.m. is lovely and the bus schedule is the constraint.", "In summer the Lake Louise lot reserves and then fills. A car does not solve a full lot. The bus is the honest ticket.", "Lake Louise, Alberta"),
        day(3, "A canyon, early", "Johnston Canyon before the tour buses, then a quiet afternoon.", "Early Roam or a short taxi to Johnston Canyon. Walk the lower falls. The upper falls are farther and worth it if the catwalk is not already jammed.", "Back to town for a late lunch and a free afternoon. The hot pools at the hotel, a nap, a bookshop.", "Dinner somewhere you have already walked past and liked. No itinerary for the evening.", "The canyon is ice in winter and a crowd in July. Early is the only fix you control.", "Johnston Creek (Alberta)"),
        day(4, "The river, then the castle as a visit", "Leave from town. Look at the famous hotel without sleeping in it.", "A morning walk on the Bow River trail.", "If you want the castle, take the Roam bus up to Fairmont Banff Springs, walk the public view, and come back down. Then the airport or the train city.", "Calgary is about an hour and a half by the Banff Airporter or a similar bus. Do not miss it because you were still on Tunnel Mountain.", "The walk from town up to the castle is longer and steeper than it looks on a postcard.", "Banff Springs Hotel"),
    ],
    attractions=[
        sight("Tunnel Mountain", "The short steep walk above town. The view is Banff itself.", "Go up in the morning. Come down the same way.", "Tunnel Mountain"),
        sight("Lake Louise, Alberta", "The turquoise lake. The day trip, not the bedroom.", "Bus or shuttle. The lakeshore path is the visit. Agnes is a hike you opt into.", "Lake Louise, Alberta"),
        sight("Johnston Creek (Alberta)", "The canyon with the catwalk and the falls.", "Early. The lower falls are enough if the upper trail is a queue.", "Johnston Creek (Alberta)"),
        sight("Bow River", "The river at the bottom of town. The easiest beautiful walk.", "Evening light is kind. You can be back at dinner in minutes.", "Bow River"),
        sight("Banff Springs Hotel", "The castle, visited by bus from a hotel that is actually in town.", "See the view. Do not move your luggage up the hill for one photo.", "Banff Springs Hotel"),
        sight("Banff Upper Hot Springs", "A public soak on Sulphur Mountain, if you want a bath that is not your hotel pool.", "It is a bus or a taxi. The water is a soak, not a swim.", "Banff Upper Hot Springs"),
    ],
    scenic_routes=[
        route("Bow River trail", "From downtown along the river toward the falls or just out and back. Flat, and the reason a car is unnecessary.", "2–6 km"),
        route("Tunnel Mountain Summit", "The switchback trail above the east end of town. Short, steep, and the local view.", "About 4 km round trip"),
        route("Roam to Lake Louise", "The bus from Banff town to the lake and back. The scenic part starts when the road climbs out of the valley.", "About an hour each way, plus waiting"),
    ],
    transport="Walk in town. Roam transit for Lake Louise, the canyon, the cave-and-basin side, and the castle. The Parks Canada shuttle is the peak-season tool for Lake Louise and, separately, for Moraine Lake, which this page does not promise. A car is optional and often worse because of parking. Calgary Airport is a booked bus, about ninety minutes.",
    food=[
        dish("A proper dinner on Banff Avenue", "A restaurant you can walk to", "Alberta beef or a simple pasta. Book the popular rooms. Walk home."),
        dish("Bakery breakfast", "A bakery in town, early", "Coffee and something substantial before the Louise bus. Hotel breakfast is the backup."),
        dish("A packed lunch", "For Lake Louise", "The lakeside kiosks are limited and priced like a viewpoint. Carry a sandwich."),
        dish("A casual second dinner", "Anywhere you liked the look of, on the canyon day", "You do not need a tasting menu after a morning on a catwalk."),
    ],
    tips=[
        "Fairmont Banff Springs is a sight on this trip, not the bed. The walk up from town is a hike in disguise.",
        "Lake Louise in summer is a reservation problem. Use the bus. Arriving in a rental car at 11 a.m. is how people miss the lake.",
        "This page does not schedule Moraine Lake. The road is closed to private cars and the shuttle books out. Do not add it the night before.",
        "Town is walkable and dinner is close. That is true. It is still a mountain town: a jacket, even in July, belongs in the bag.",
    ],
    faqs=[
        faq("Can I walk to the Banff Springs Hotel?", "You can, and it is uphill the whole way back. The Roam bus is the intended version. Sleep in town instead."),
        faq("Do I need a car?", "No. Roam and your feet cover this itinerary. A car helps only if you are leaving the town-and-Louise pattern."),
        faq("Is Moraine Lake on the way to Louise?", "It is a separate road, and you cannot just drive up it. It is not part of this four-night walk."),
        faq("Are the hotel pools private?", "No. Moose's rooftop pools and the Fox's grotto pool are shared. They are still a good end to a cold walk."),
    ],
    map_places=[
        stop("Tunnel Mountain", "Banff", "Canada", "Tunnel Mountain"),
        stop("Lake Louise", "Lake Louise", "Canada", "Lake Louise, Alberta"),
        stop("Johnston Canyon", "Banff", "Canada", "Johnston Creek (Alberta)"),
        stop("Bow River", "Banff", "Canada", "Bow River"),
        stop("Banff Springs Hotel", "Banff", "Canada", "Banff Springs Hotel"),
    ],
    budget_notes="An in-town room is often $180–400, more on July and August weekends. The bus is cheap next to a rental car and a parkade. Lake Louise itself is a park pass plus the transit. Dinners on the avenue add up; one booked meal and one casual meal is the sane split. The castle is free to look at from the public side.",
))

add(trip(
    slug="banff-mountain-or-nature-view",
    title="Banff for the view: the castle, the Rimrock, or Tunnel Mountain",
    location="Banff, Canada",
    summary=(
        "Four nights where the view is the reason to book. Fairmont Banff Springs looks over the Bow and Mount Rundle. "
        "Rimrock Banff sits on Sulphur Mountain above town. Buffalo Mountain Lodge is in the trees on Tunnel Mountain. "
        "Moraine Lake is included only as a shuttle you reserve. You cannot drive up whenever you feel like it."
    ),
    who="Travelers who want a mountain outside the window and will take a bus or a shuttle to dinner if that is the trade.",
    best_time="June to September for the lakes. The view hotels are also the point in winter, when the town is quieter and the days are short. Smoke in late summer can flatten every view; it is a real risk.",
    nights=4,
    hook="4 nights · A real mountain view · Moraine only by shuttle",
    constraints=["The room faces the valley or the trees", "Town is a ride, not a step", "No drive-up promise for Moraine"],
    lodging="$280–700",
    daily="$400–850",
    neighborhoods=[
        stay_area("Above the Bow", "Banff Springs is the castle on the hill. The view is the river and the mass of Rundle. Dinner in town is a Roam bus or a taxi back up."),
        stay_area("Sulphur Mountain and Tunnel Mountain", "Rimrock is on the gondola road. Buffalo Mountain Lodge is on Tunnel Mountain Road, about five minutes by car from the avenue and not a walk to it."),
    ],
    hotels=[
        hotel("Fairmont Banff Springs", "Above the Bow River", "The castle view: the river, the valley, and Mount Rundle. It is not in town. A Roam bus or a long walk connects you to dinner. Book a valley-facing room if the view is why you came.", "$400–900", "Banff", "https://www.fairmont.com/banff-springs/"),
        hotel("Rimrock Banff, Emblems Collection", "Sulphur Mountain Road", "Above town, near the gondola and the Upper Hot Springs, with the valley in front of the windows. After a renovation it trades as Rimrock Banff, Emblems Collection. You are up the hill on purpose.", "$300–650", "Banff"),
        hotel("Buffalo Mountain Lodge", "Tunnel Mountain", "In the forest on Tunnel Mountain Road, with a real outlook and fireplaces in many rooms. About five minutes by car to town. A view lodge, not a Banff Avenue address.", "$250–500", "Banff"),
    ],
    itinerary=[
        day(1, "Look at the thing you paid for", "Arrive, find the view, and do not immediately go downtown.", "Check in and spend the first hour on the side of the building that faces the valley or the trees.", "A short walk from the hotel: the Bow if you are at the Springs, the Sulphur road if you are at the Rimrock, the lodge grounds if you are on Tunnel Mountain.", "Dinner at the hotel the first night. You did not book a view in order to leave it at 6 p.m.", "Valley-facing and forest-facing are different. Confirm the category.", "Banff Springs Hotel"),
        day(2, "Sulphur Mountain, from above town", "The gondola, which is easiest if you are already on this side of the river.", "Banff Gondola. On a clear day the summit boardwalk is the view of views. On a smoky day it is an expensive cloud. Check before you buy.", "Upper Hot Springs if you want to soak, then back.", "Hotel dinner or a taxi down to town and back up. Do not pretend the walk down is casual after a full day.", "The gondola and the Rimrock are neighbors. From Banff Springs or Tunnel Mountain you still need a ride.", "Sulphur Mountain (Alberta)"),
        day(3, "A lake you planned for", "Either Lake Louise or Moraine, not both unless a reserved shuttle says so.", "If you hold a Moraine Lake shuttle reservation, use it and do not also promise yourself Louise. If you do not, take the bus to Lake Louise and walk the shore.", "Back before you are stranded at a trailhead. The shuttle is the schedule.", "A quiet dinner. The view at dusk from the hotel is the second half of the day.", "Moraine Lake Road is closed to private cars. A reservation or a tour seat is the only way up. 'We will just drive' is the plan that fails.", "Moraine Lake"),
        day(4, "One canyon or one river, then Calgary", "A last outdoor hour that does not depend on a new reservation.", "Johnston Canyon early, if you can face the catwalk, or a Bow River walk if you would rather stay near the hotel.", "Down to town only if you need to, then the bus to Calgary.", "Leave the mountains in daylight if you can. The park is the memory, not the airport mall.", "Smoke, snow, and a full shuttle are all ordinary. The hotel view still counts.", "Bow River"),
    ],
    attractions=[
        sight("Banff Springs Hotel", "The view hotel and, if you are staying elsewhere, the castle to look at.", "A valley-facing room is the point. A parking-lot room is a waste of the rate.", "Banff Springs Hotel"),
        sight("Sulphur Mountain (Alberta)", "The gondola summit. Peaks in every direction when the air is clear.", "Buy the ticket when you can see the top. Cloud and smoke make it a short, pricey ride.", "Sulphur Mountain (Alberta)"),
        sight("Moraine Lake", "The other famous turquoise, and the one you cannot casually drive to.", "Shuttle reservation, or do not go. The lakeshore is the visit.", "Moraine Lake"),
        sight("Lake Louise, Alberta", "The backup famous lake, served by a bus from town.", "Go early. The shore path, not necessarily the teahouse hike.", "Lake Louise, Alberta"),
        sight("Johnston Creek (Alberta)", "The canyon walk, a good last morning.", "Lower falls if you are short on time. The catwalk is slick when it is cold.", "Johnston Creek (Alberta)"),
        sight("Bow River", "The water in the valley the castle looks at.", "A flat walk, useful when the shuttle days are done.", "Bow River"),
    ],
    scenic_routes=[
        route("From the room", "The view you booked: Rundle and the Bow from the Springs, the valley from the Rimrock, the trees and the town below from Tunnel Mountain. Start here.", "Stay"),
        route("Gondola and the boardwalk", "Sulphur Mountain summit boardwalk. Short, high, and pointless in a whiteout.", "A couple of hours including the ride"),
        route("Reserved Moraine shuttle", "The only dependable way onto Moraine Lake Road in season. The scenic part is the last stretch of that road, and you are a passenger.", "A booked seat, not a whim"),
    ],
    transport="You want a car or a taxi more than the walkable-town page does, because these hotels are up a hill. Roam still helps for Louise and for getting down to dinner. Moraine is a Parks Canada or hotel shuttle with a reservation, not your rental car. Calgary is a bus or a very expensive taxi. In winter, add ice and an early sunset to every plan.",
    food=[
        dish("Dinner at the hotel", "Banff Springs, the Rimrock, or Buffalo Mountain Lodge", "One night, at least, eat where you are staying. The view is the table."),
        dish("A town dinner", "Banff Avenue, by bus or taxi", "The night you want a different room. Book, and book the return ride if you are on the hill."),
        dish("A packed lunch", "For the lake day", "Carry it. The shoreline is not a restaurant row."),
        dish("Coffee before the shuttle", "The hotel, early", "Moraine and Louise days start before a leisurely brunch. Eat first."),
    ],
    tips=[
        "Say the view category out loud when you book: valley, not courtyard, not the parking side.",
        "Moraine Lake is a shuttle system. If the reservation is gone, go to Louise or stay on Sulphur. Do not drive the closed road.",
        "Wildfire smoke in August can erase the view you paid for. It is not the hotel's fault, and it is not rare.",
        "Getting to dinner in town is a ride. Factor that in, or eat at the hotel and enjoy the reason you are up there.",
    ],
    faqs=[
        faq("Can I drive to Moraine Lake?", "Not in the season when you want to see it. The road is closed to private vehicles. A shuttle reservation is the visit."),
        faq("Is the Rimrock open?", "It reopened after a renovation as Rimrock Banff, Emblems Collection. It is the Sulphur Mountain view hotel, above town."),
        faq("Is Banff Springs walkable to town?", "Down, eventually. Back up, it feels like a trail. Use the bus if you are sleeping there and eating on the avenue."),
        faq("Which hotel is actually in the trees?", "Buffalo Mountain Lodge, on Tunnel Mountain. The Springs is a castle over the valley. The Rimrock is on the Sulphur road."),
    ],
    map_places=[
        stop("Banff Springs Hotel", "Banff", "Canada", "Banff Springs Hotel"),
        stop("Sulphur Mountain", "Banff", "Canada", "Sulphur Mountain (Alberta)"),
        stop("Moraine Lake", "Lake Louise", "Canada", "Moraine Lake"),
        stop("Lake Louise", "Lake Louise", "Canada", "Lake Louise, Alberta"),
        stop("Bow River", "Banff", "Canada", "Bow River"),
    ],
    budget_notes="A view room at the Springs is often $400–900. The Rimrock and Buffalo Mountain Lodge can be less and still face the right direction. Shuttles are modest until a private taxi up and down the hill every night becomes the plan. One hotel dinner is worth it. A missed Moraine reservation is free to replace with Louise. Do not buy a tour on top of a shuttle you already hold.",
))

add(trip(
    slug="banff-quiet-romantic-getaway",
    title="A quiet Banff getaway: Lake Louise at dinner, not Banff Avenue at midnight",
    location="Banff, Canada",
    summary=(
        "Three nights away from the Saturday-night bar on Banff Avenue. The base is Lake Louise village, at the Post "
        "Hotel, with Deer Lodge if you want to be nearer the lake and Juniper if you would rather sit at the edge of "
        "Banff town. One big view, a long dinner, and an early morning before the buses arrive."
    ),
    who="A couple who want mountains, a serious dinner, and a hotel that is not on the main street.",
    best_time="Late September, when the larches may be turning and the lake is calmer, or January if you want snow and do not need a long evening outside. July is beautiful and the least quiet.",
    nights=3,
    hook="3 nights · Lake Louise, not Banff Avenue · One view, one dinner",
    constraints=["Not the Banff Avenue bar", "Lake Louise is the base", "Early morning, before the buses"],
    lodging="$250–600",
    daily="$400–750",
    neighborhoods=[
        stay_area("Lake Louise village", "The Post Hotel is here, in the village, not on the lakeshore. It is about 45 minutes from Banff town and a short hop to the lake if you go before the crowds."),
        stay_area("The edge of Banff", "Juniper is the alternative if you want a valley view and a bistro without sleeping on the avenue. It is not the Lake Louise trip. Pick one base."),
    ],
    hotels=[
        hotel("Post Hotel & Spa", "Lake Louise village", "A quiet hotel in the village, about 45 minutes from Banff town, with a serious dining room and a serious wine cellar. You are not on the lakeshore. You are also not on Banff Avenue. This is the base.", "$350–700", "Lake Louise"),
        hotel("Deer Lodge", "Lake Louise", "An older lodge above the lake, quieter and plainer than the Fairmont Chateau, which is a summer crowd and not this trip. You trade polish for being near the water.", "$250–500", "Lake Louise"),
        hotel("Juniper Hotel & Bistro", "Edge of Banff", "Off the highway at the edge of town, with a valley view and a bistro. Choose it only if you want Banff nearby and still refuse the bar street. The itinerary below assumes Lake Louise.", "$220–450", "Banff"),
    ],
    itinerary=[
        day(1, "Arrive, and do not go out again", "The getaway starts by stopping.", "Transfer from Calgary. The drive is an hour and a half to Banff and longer to Lake Louise. Watch the light and do not add a canyon.", "Check in at the Post or Deer Lodge. A short walk in the village or the lodge grounds.", "The long dinner. At the Post, this is the dining room you booked. Dress like a person who made a reservation, then stay in.", "If the dining room is full, you waited too long. Book it with the room.", "Lake Louise, Alberta"),
        day(2, "The lake before the buses", "One view, early, and then nothing ambitious.", "Be at Lake Louise as it gets light, or as soon as the shore path is open. Walk until you are cold or content, and leave as the first full parking wave arrives.", "Back to the hotel. Spa, book, nap. A romantic trip that hikes Agnes and then wants a calm dinner has planned two days in one.", "A second dinner, simpler if last night was the production. Or the same dining room if that is the whole idea.", "Chateau Lake Louise is on the shore and is the building you will see. You do not need to be staying in it to stand there at dawn.", "Moraine Lake"),
        day(3, "A slow leave", "One more quiet hour, then Calgary.", "Coffee and a last look if the morning is clear. Do not start a new trail.", "Drive or bus toward Calgary. If you leave Lake Louise late, you will be in the park after dark in a way that is pretty and tiring.", "The airport. Eat before you are in the terminal.", "Banff Avenue is not a required stop on the way out. Skip it.", "Bow River"),
    ],
    attractions=[
        sight("Lake Louise, Alberta", "The one big view. Early, almost empty, and then left alone.", "Dawn or opening. The later you arrive in July, the less this is a getaway.", "Lake Louise, Alberta"),
        sight("Moraine Lake", "Only if you already hold a shuttle seat and are willing to spend the quiet day there instead of at Louise.", "It is not an add-on. It replaces the Louise morning.", "Moraine Lake"),
        sight("Bow River", "What you see on the drive, and the water in the valley.", "A pullout is enough. Do not invent a third hike.", "Bow River"),
        sight("Banff National Park", "The park itself is the attraction. The town is a service center you can mostly skip.", "Stay in the village or at the lake. Use town for a grocery if you must.", "Banff National Park"),
        sight("Tunnel Mountain", "Not on this itinerary. Named so it stays in town, where the walkable page uses it.", "If you are at Juniper, a short view walk is the local version. Do not drive to Louise and also up Tunnel in one afternoon.", "Tunnel Mountain"),
        sight("Banff Springs Hotel", "A castle you may pass and do not need to enter.", "The quiet trip does not require a tour of someone else's lobby.", "Banff Springs Hotel"),
    ],
    scenic_routes=[
        route("Village to the lake at dawn", "The short trip from the Post Hotel up to the lakeshore before the buses. The whole romantic route.", "About 10 minutes by car or shuttle, then a walk"),
        route("Lakeshore and back", "Along the water until the crowd thickens, then return. Do not continue to the teahouse unless you came to hike.", "1–3 km"),
        route("Calgary to Lake Louise", "The arrival drive through the park. Stop once for the view and then finish the trip. More stops become a tour.", "About 2 hours"),
    ],
    transport="A car is the calm way to be at the lake early and to leave Calgary. The Park and Ride and Roam buses work from Banff town and are less romantic at dawn. If you do not want to drive, book a transfer and a hotel that can get you to the shore early. Banff Avenue is easy to avoid: do not go there for dinner.",
    food=[
        dish("The long dinner", "Post Hotel dining room", "The meal to reserve with the room. Game, wine, and enough time. This is the night."),
        dish("A simple second dinner", "The hotel again, or a quiet table in the village", "You do not need a new concept. You need to be fed without a bar."),
        dish("Breakfast before the lake", "The hotel, early", "Eat enough. A viewpoint is cold and there is no charming cafe at dawn on the shore."),
        dish("A packed apple and a chocolate bar", "Your bag", "The unglamorous part of a romantic morning. Take them."),
    ],
    tips=[
        "Saturday night on Banff Avenue is the thing this trip refuses. Do not 'just go in for one drink' and lose the plot.",
        "Fairmont Chateau Lake Louise is on the lake and is busy. Deer Lodge and the Post are the quieter beds. The shore at dawn is how you still get the view.",
        "Book the Post dining room. A romantic hotel with a walk-in dinner plan is a gamble.",
        "Three nights is right. A fourth starts to want activities, and activities are how it stops being quiet.",
    ],
    faqs=[
        faq("Is the Post Hotel on the lake?", "No. It is in Lake Louise village. The lake is a short ride. The hotel is the dinner and the quiet."),
        faq("Can we stay in Banff town and still be quiet?", "Only at the edge, which is why Juniper is listed. The avenue itself is not the getaway, especially on a weekend."),
        faq("Is Moraine Lake more romantic?", "At opening, yes, and only with a shuttle reservation. It replaces Lake Louise. It does not join it."),
        faq("Do we have to hike?", "No. The shore, the dinner, and an early night are the trip. The teahouse is a different holiday."),
    ],
    map_places=[
        stop("Lake Louise", "Lake Louise", "Canada", "Lake Louise, Alberta"),
        stop("Moraine Lake", "Lake Louise", "Canada", "Moraine Lake"),
        stop("Banff National Park", "Banff", "Canada", "Banff National Park"),
        stop("Bow River", "Banff", "Canada", "Bow River"),
        stop("Tunnel Mountain", "Banff", "Canada", "Tunnel Mountain"),
    ],
    budget_notes="The Post is the expensive quiet choice and includes the dinner you should actually eat. Deer Lodge is the simpler near-lake room. Juniper is the Banff-edge alternative and a different base. A car or a private transfer from Calgary is the other real cost. Park passes matter. You save by not doing a list of tours.",
))

add(trip(
    slug="cape-town-luxury-with-ocean-view",
    title="Cape Town luxury on the Atlantic, and a harbor hotel that is not the ocean",
    location="Cape Town, South Africa",
    summary=(
        "Four nights with the water named correctly. Twelve Apostles and Pod Camps Bay face the Atlantic, which is "
        "cold. Cape Grace is on a quay in the V&A, looking at the marina and the working harbor, with Table Mountain "
        "behind it. That harbor view is beautiful and it is not an ocean horizon. Book the room that faces the water you mean."
    ),
    who="Travelers who want a real water view and will choose between the Atlantic seaboard and the harbor on purpose.",
    best_time="November to March for long evenings and a chance of swimming, though the Atlantic stays cold. April and May are softer. June to August is winter: dramatic, windy, and green, with short days.",
    nights=4,
    hook="4 nights · Atlantic or the V&A harbor · Named separately",
    constraints=["Say which water", "Atlantic is cold", "The V&A basin is a harbor"],
    lodging="$350–900",
    daily="$500–1,100",
    neighborhoods=[
        stay_area("Camps Bay and the Atlantic seaboard", "Twelve Apostles sits under the mountain facing the ocean. Pod is on the Camps Bay beachfront. Both are the Atlantic. The water is the Benguela current and it is cold."),
        stay_area("V&A Waterfront", "Cape Grace is on a private quay. You look at masts, working boats, and Table Mountain. Stay here for the harbor and the walk to restaurants, not for a beach."),
    ],
    hotels=[
        hotel("Twelve Apostles Hotel & Spa", "Atlantic seaboard, Camps Bay side", "Faces the Atlantic, with the Twelve Apostles range behind the hotel. Book an ocean-facing room; some rooms face the mountain instead. The swim, if you insist, is cold.", "$400–900", "Cape Town"),
        hotel("Pod Camps Bay", "Camps Bay beachfront", "On the sand at Camps Bay, so the Atlantic really is the view. Louder and younger than the Twelve Apostles, with the beach promenade at the door. Still cold water.", "$250–550", "Cape Town"),
        hotel("Cape Grace", "V&A Waterfront", "On a quay in the V&A. The view is the marina and the working harbor, with Table Mountain behind. It is one of the city's best luxury hotels and it is not an Atlantic-horizon hotel. Book it for the harbor.", "$400–850", "Cape Town"),
    ],
    itinerary=[
        day(1, "The water you actually face", "Arrive and settle the difference between a beach and a basin.", "Transfer. Camps Bay and the Twelve Apostles are a ride from the airport around the mountain. The V&A is more direct.", "If you are on the Atlantic, walk the beach or the hotel terrace and feel the water temperature. If you are at Cape Grace, walk the quay and look at the mountain.", "Dinner at the hotel the first night. The wind comes up in the evening more often than the brochures suggest.", "Ocean-facing means ocean-facing. A mountain-facing room at the Twelve Apostles is a different, also beautiful, product.", "Camps Bay"),
        day(2, "Table Mountain, if the cableway is open", "The city's other view, which depends on wind.", "Check the cableway. If it is running, go in the morning. If it is not, Kirstenbosch is the garden version of the same mountain and does not close for a breeze.", "Down before you are cold. Back to the hotel water.", "A reserved dinner. Camps Bay has a strip; the better meal may be the hotel. The V&A has too many choices and a few good ones.", "Do not hike the mountain in the afternoon wind as a casual idea. Use the cableway or do not go up.", "Table Mountain"),
        day(3, "The other water, as a visit", "See the one you did not book.", "If you slept on the Atlantic, spend a few hours at the V&A and look at the harbor so you know what the other hotels mean. If you slept at Cape Grace, go to Camps Bay for the beach hour and a sunset.", "Back. A spa hour or a do-nothing hour is the luxury.", "Dinner. One serious meal is enough.", "Camps Bay sunset is a crowd and a parking problem. A rideshare both ways.", "V&A Waterfront"),
        day(4, "A last swim or a last look at the mountain", "Leave without a new region.", "A morning swim if you can stand the Atlantic, or a walk on the Waterfront if you cannot.", "Airport. The Atlantic seaboard needs more time than the V&A. Wind and the hospital bend are not theoretical.", "You saw the ocean, or you saw the harbor. You know which.", "Do not add the Cape of Good Hope on a flight day. It is a separate drive.", "Table Mountain"),
    ],
    attractions=[
        sight("Camps Bay", "The Atlantic beach and the row of palms. The true ocean of this search.", "Swim if you like cold water. Walk it if you do not.", "Camps Bay"),
        sight("Table Mountain", "The backdrop, from the beach or from the cableway.", "The cableway closes in wind. Have Kirstenbosch as the other plan.", "Table Mountain"),
        sight("V&A Waterfront", "The harbor the Cape Grace looks at. Shops, boats, and the mountain.", "A few hours. It is not a beach.", "V&A Waterfront"),
        sight("Kirstenbosch National Botanical Garden", "The garden on the mountain's eastern side. The windproof outdoor day.", "Go in the morning. It is large enough to be a half-day and small enough to leave.", "Kirstenbosch National Botanical Garden"),
        sight("Clifton, Cape Town", "The next set of beaches up the coast, colder and more sheltered by giant rocks.", "A sunset look, not a reason to relocate.", "Clifton, Cape Town"),
        sight("Robben Island", "A harbor boat and a history tour, not a beach day.", "Book ahead. It leaves from the Waterfront. It is a sober visit, not a cruise.", "Robben Island"),
    ],
    scenic_routes=[
        route("Camps Bay front", "Along the beach with the Twelve Apostles behind you and the Atlantic in front. The ocean walk.", "About 2 km"),
        route("Waterfront to the quay", "A loop of the V&A basin. Harbor water, cranes, and the mountain. Name it correctly while you walk.", "An hour"),
        route("To Kirstenbosch", "A rideshare from either base to the garden and back. The mountain without the cableway gamble.", "20–40 minutes each way"),
    ],
    transport="Rideshare or a hotel car. A rental car is useful for the peninsula and annoying at the Waterfront and in Camps Bay parking. The Atlantic seaboard to the V&A is a short, spectacular, traffic-prone drive. The airport is on the other side of the city. Do not walk between Camps Bay and town. At night, use a car, not a long walk on a quiet coastal road.",
    food=[
        dish("A reserved dinner", "The hotel, or one Camps Bay room that is not just a view", "Book it. Sunset tables go. The view is not a substitute for the kitchen, so choose a place that can do both or drop the view."),
        dish("Fish and chips or a grill", "A simple lunch, not on the most photographed corner", "The Cape's ordinary fish meal. Eat it once."),
        dish("Breakfast with the water", "Twelve Apostles, Pod, or Cape Grace", "The morning you are paying for. Ocean, or harbor, as booked."),
        dish("A Malay curry", "Bo-Kaap or a serious Cape Malay table, one lunch", "A city meal with a history. Do it on the day you are already on the city side."),
    ],
    tips=[
        "The Atlantic is cold. A heated pool is the swim for many guests, and that is a reasonable choice, not a failure.",
        "Cape Grace is a harbor hotel. Twelve Apostles and Pod are ocean hotels. Do not let a booking site call all three the same view.",
        "The cableway is a wind decision made that morning. Kirstenbosch is the adult backup.",
        "Use rideshare at night. A walk from a beach bar back along a dark road is not the luxury version.",
    ],
    faqs=[
        faq("Is the V&A the ocean?", "No. It is a harbor basin. You can see the mountain and the boats. The Atlantic is at Camps Bay, Clifton, and the Twelve Apostles."),
        faq("Can I swim at Camps Bay?", "Yes, if you like cold water and you obey the flags. Many people walk and then swim in the hotel pool."),
        faq("Which room at the Twelve Apostles?", "The one that says ocean, if the ocean is the search. Mountain-facing rooms look at the range, which is a different luxury."),
        faq("Is Pod as quiet as the Twelve Apostles?", "No. It is on the beachfront strip. The view is more immediate and the night is louder."),
    ],
    map_places=[
        stop("Camps Bay", "Cape Town", "South Africa", "Camps Bay"),
        stop("Table Mountain", "Cape Town", "South Africa", "Table Mountain"),
        stop("V&A Waterfront", "Cape Town", "South Africa", "V&A Waterfront"),
        stop("Kirstenbosch", "Cape Town", "South Africa", "Kirstenbosch National Botanical Garden"),
        stop("Clifton", "Cape Town", "South Africa", "Clifton, Cape Town"),
    ],
    budget_notes="Ocean-facing luxury here is often $400–900 at the Twelve Apostles and Cape Grace, sometimes less at Pod and more in December and January. Rideshares add up if you cross the city daily. One serious dinner is the other large line. The cableway and Robben Island are optional tickets. The cold swim is free.",
))

add(trip(
    slug="cape-town-quiet-romantic-getaway",
    title="A quiet Cape Town: Bantry Bay, Chapman's Peak, and no Long Street",
    location="Cape Town, South Africa",
    summary=(
        "Four nights on the quieter Atlantic side. Ellerman House is a small hotel above Bantry Bay. The President "
        "is the simpler bay hotel with the ocean in front. Tintswalo Atlantic is the small lodge at Hout Bay, which "
        "puts Chapman's Peak at the door. Sunset is Clifton or Camps Bay. Long Street is not on the itinerary. At night, take a car."
    ),
    who="A couple who want the ocean, a long dinner, and a coast drive, and who do not want a nightlife strip.",
    best_time="November to March for long light, with wind. April and May are quieter. December holidays are beautiful and not quiet on the beaches. Winter is for storms and fireplaces, which can be the romantic version.",
    nights=4,
    hook="4 nights · Bantry Bay or Hout Bay · Chapman's Peak, not Long Street",
    constraints=["No Long Street night", "Rideshare after dark", "Do not walk the mountain alone at night"],
    lodging="$250–900",
    daily="$400–1,100",
    neighborhoods=[
        stay_area("Bantry Bay", "Residential, on the Atlantic, between Sea Point and Clifton. Ellerman House and The President are here. You hear water, not a bar street."),
        stay_area("Hout Bay", "Tintswalo sits at the water under Chapman's Peak. Quieter and more remote. The sunset drive starts at your door, and town is a ride."),
    ],
    hotels=[
        hotel("Ellerman House", "Bantry Bay", "A small house above the Atlantic. Sea-facing rooms look over Bantry Bay, and the hotel is quiet because it is a house, not a scene. Book a room that faces the water. The art and the wine gallery are indoors if the wind is up.", "$500–1,200", "Cape Town"),
        hotel("The President Hotel", "Bantry Bay", "A straightforward hotel in the same residential bay, with no nightlife strip at the door. Ask for an Atlantic-facing room. Other rooms look at the mountain or the city. Less rarefied than Ellerman, and still the quiet side.", "$180–350", "Cape Town"),
        hotel("Tintswalo Atlantic", "Hout Bay", "A small lodge on a pebble beach under Chapman's Peak, looking at the Atlantic and Hout Bay. Not a Waterfront walk. Children under 10 are not the standard policy. Confirm the transfer. The road is the scenery and the logistics.", "$400–900", "Cape Town"),
    ],
    itinerary=[
        day(1, "Arrive and stay in", "The getaway is the bay, not a city orientation.", "Transfer to Bantry Bay or Hout Bay. The airport is on the far side of town. Let someone else drive.", "A terrace, a swim in the pool, a look at the ocean. The water is cold. The pool is allowed.", "Dinner at the hotel. Ellerman and Tintswalo are places you eat in. Do not go looking for a scene.", "Wind can make a balcony unpleasant by evening. Have the indoor table as the plan.", "Camps Bay"),
        day(2, "Chapman's Peak, by day", "The coast drive, done in daylight, and ended before you are on a dark mountain road.", "Late morning along Chapman's Peak Drive toward Hout Bay and back, or onward to a winery only if you still feel like sitting in a car. The cliffs and the ocean are the point.", "A late lunch, then back to the hotel for a long nothing.", "Sunset at Clifton or a quiet Camps Bay lookout, by rideshare, and back for the night. You are not staying out.", "Do not drive Chapman's Peak in the fog or at night for the romance of it. The romance is the daylight.", "Chapman's Peak"),
        day(3, "A garden, not a bar", "The quiet daytime Cape Town.", "Kirstenbosch in the morning. Walk, sit, leave before you are overheated or windblown.", "Back along the coast. If you want a beach hour, Clifton's coves are the stop. They are rocky and cold and beautiful.", "A second hotel dinner, or one reserved table that is not on Long Street. Home early.", "Long Street, Bree Street binges, and a club are a different trip. They are easy to decline.", "Kirstenbosch National Botanical Garden"),
        day(4, "One more ocean morning", "Leave from the bay.", "Breakfast with the Atlantic in the window, if your room has it. A short walk on the Sea Point promenade only if you are in Bantry Bay and the weather is kind.", "Airport with a margin. The coast road plus the city can take longer than a maps estimate at noon.", "You never needed the nightclub version.", "If the cableway is open and you are tempted, only go if the flight is late. Otherwise the mountain from below was enough.", "Clifton, Cape Town"),
    ],
    attractions=[
        sight("Camps Bay", "The sunset look, visited and left. Not the hotel, unless you chose a louder base on the other page.", "Go for the light, by car, and leave.", "Camps Bay"),
        sight("Clifton, Cape Town", "Four coves under the mountain. The quiet swim, if the cold does not put you off.", "The beaches are down steep steps. A sunset from the road is the easier version.", "Clifton, Cape Town"),
        sight("Chapman's Peak", "The coast drive between Hout Bay and Noordhoek. Cliffs and the Atlantic.", "Daylight, good weather, a sober driver. It is a toll road and a serious piece of road.", "Chapman's Peak"),
        sight("Kirstenbosch National Botanical Garden", "The garden morning. Shade, fynbos, and a mountain slope.", "It is the right scale for a quiet day. Do not rush it into an hour.", "Kirstenbosch National Botanical Garden"),
        sight("Table Mountain", "Seen from the bay all day. Going up is optional and weather-dependent.", "If the cableway is closed, you have not missed the mountain. You are looking at it.", "Table Mountain"),
        sight("Signal Hill (Cape Town)", "A viewpoint over the city. Pretty, and not a place to walk after dark.", "Daytime only, and not alone on the paths. Use a car.", "Signal Hill (Cape Town)"),
    ],
    scenic_routes=[
        route("Chapman's Peak Drive", "Hout Bay to Noordhoek along the cliffs. Stop at the pullouts. Turn around when you have had the view.", "About 9 km of the dramatic section"),
        route("Bantry Bay to Clifton", "A short coastal hop for sunset, by car. The beaches are below the road.", "10–15 minutes plus the time you stay"),
        route("To Kirstenbosch", "Across the city in the morning and back to the coast before the wind makes everyone tired. One garden, then home.", "20–40 minutes each way"),
    ],
    transport="Rideshare or a hotel driver, including at night. A rental car helps on Chapman's Peak and is one more thing to park in Bantry Bay. Do not walk the mountain, Lion's Head, or Signal Hill after dark, and do not walk a long stretch of the coast road at night. The airport transfer should be booked, not invented in the lobby twenty minutes before you need it.",
    food=[
        dish("Dinner at the hotel", "Ellerman House or Tintswalo", "The romantic meal is the one on the property. Reserve it. Leaving to find a trendier room breaks the trip."),
        dish("A simple lunch in Hout Bay", "After Chapman's Peak", "Fish, eaten because you are there, not because it is famous. Then go back."),
        dish("Breakfast overlooking the bay", "Your hotel", "The meal the room category is for. Sea-facing, or you are looking at a wall and calling it romance."),
        dish("One city lunch", "A quiet dining room, not a Long Street bar", "If you want a kitchen outside the hotel, make it lunch, in daylight, with a car home."),
    ],
    tips=[
        "Use a rideshare or a driver at night. This is a safety instruction, not a mood.",
        "Do not hike the mountain alone, and do not start a trail in the late afternoon. People are robbed on the paths after dark.",
        "The Atlantic is cold. A sunset with a coat is more honest than a swim you will not enjoy.",
        "Ellerman is the quiet house. The President is the simpler bay hotel. Tintswalo is the remote one. Pick the logistics you actually want.",
    ],
    faqs=[
        faq("Is Long Street part of a romantic Cape Town?", "Not this one. It is a night out. The quiet version is the bay, the garden, and an early dinner."),
        faq("Can we walk up Lion's Head for sunrise?", "Only if you know the route, start with enough light to come down, and are not alone. It is not a spontaneous midnight idea."),
        faq("Is Tintswalo hard to get in and out of?", "It sits under Chapman's Peak at Hout Bay. Beautiful, and every dinner in the city is a drive. Eat there."),
        faq("What if the wind is howling?", "Stay in. The hotels on this page are the point. A windy Chapman's Peak day can be moved or cancelled without ruining the trip."),
    ],
    map_places=[
        stop("Camps Bay", "Cape Town", "South Africa", "Camps Bay"),
        stop("Clifton", "Cape Town", "South Africa", "Clifton, Cape Town"),
        stop("Chapman's Peak", "Cape Town", "South Africa", "Chapman's Peak"),
        stop("Kirstenbosch", "Cape Town", "South Africa", "Kirstenbosch National Botanical Garden"),
        stop("Table Mountain", "Cape Town", "South Africa", "Table Mountain"),
    ],
    budget_notes="Ellerman and Tintswalo are the expensive quiet. The President is the bay hotel that can be a few hundred dollars instead. Dinners on property are part of the point and should be budgeted as such. Rideshares and a possible driver for Chapman's Peak are the transport. You save nothing by wandering Long Street, so do not. A cableway ticket is optional and weather-dependent.",
))
