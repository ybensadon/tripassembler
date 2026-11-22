"""Bali, the Maldives, Phuket, Tulum, Cancun, Maui, Oahu, Miami, and Singapore."""
from _common import trip, hotel, stay_area, day, sight, route, dish, faq, stop

TRIPS = []


def add(record):
    TRIPS.append(record)


add(trip(
    slug="bali-near-the-beach-under-300",
    title="Sanur beach for under $300 a night",
    location="Bali, Indonesia",
    summary=(
        "Four nights on Sanur beach, where a real hotel on the sand can still land under $300 a night "
        "outside the Christmas rush. The water inside the reef is calm enough for a morning swim, the "
        "beach path is walkable, and Seminyak is a taxi when you want a louder dinner. This is a beach "
        "hotel trip, not a clifftop villa in Uluwatu."
    ),
    who="A couple or two friends who want to walk onto a beach without paying Seminyak club prices for the room.",
    best_time="Late January through June, and September through early November. July, August, and Christmas to New Year's push even Sanur rates up, and Maya Sanur often crosses $300 then.",
    nights=4,
    hook="4 nights · Sanur beach path · Under $300 a night outside peak",
    constraints=["Near the beach", "Under $300 a night", "Hotel on the sand, not a cliff villa"],
    lodging="$110-280",
    daily="$170-280",
    neighborhoods=[
        stay_area("Sanur", "A long beach path, reef-protected water, and hotels that face the sea. Quieter at night than Kuta or Seminyak, which is the point of this budget."),
        stay_area("Seminyak, as a night out", "Beach clubs and restaurants are a 30- to 45-minute taxi north. Sleeping there on this budget usually means a room off the sand. The Legian, the famous beachfront hotel, usually sits over $300."),
    ],
    hotels=[
        hotel("Puri Santrian", "Sanur beach, Jalan Cemara", "A beachfront Sanur hotel at the quieter southern end, with a garden and a reef you can paddle. Deluxe rooms and the family suite stay in range more often than a Seminyak design hotel. The room is a hotel room, not a private-pool villa.", "$140-280", "Sanur, Bali", "https://www.santrian.com/puri-santrian/"),
        hotel("Prama Sanur Beach Bali", "Mertasari beach, Sanur", "The big beachfront hotel on this stretch, with a kids' splash pool and a lagoon pool. Standard rooms are the ones that reliably hold a $300 cap, including many high-season weeks when smaller luxury hotels do not.", "$100-220", "Sanur, Bali", "https://www.pramahotels.com/hotels/detail/prama-sanur-beach"),
        hotel("Maya Sanur Resort & Spa", "Sanur beach, Jalan Danau Tamblingan", "The more polished of the three, with a lagoon pool and direct beach access. It fits under $300 in the rainy season and the shoulder months. In July, August, and Christmas week, book it only if the live rate still clears the cap.", "$200-380", "Sanur, Bali", "https://mayaresorts.com/sanur"),
    ],
    itinerary=[
        day(1, "The beach path, slowly", "Land, take the hotel's stretch of sand, and stop there. Ngurah Rai to Sanur is about 30 to 40 minutes once you are in a car.", "Drop bags. Walk the Sanur beach path south or north until the hotel's own restaurants thin out. The reef makes the water shallow and calm on a normal day.", "Swim, then sit. Rent a hotel bike only if you want the whole promenade. A first afternoon does not need a temple.", "Dinner on the sand in front of the hotel or a five-minute walk along the path. Grilled fish and rice is the meal. Save Jimbaran for a later taxi.", "The path is dark in stretches. Walk back while the beach bars are still lit.", "Sanur, Bali"),
        day(2, "Reef in the morning, Seminyak if you want noise", "One outing off the beach, timed so you are back for sunset on Sanur.", "Paddleboard or snorkel the house reef while the tide is friendly. The hotels keep kayaks; ask which hour the current is easy.", "Taxi to Seminyak for a late lunch and an hour on Double Six or Seminyak beach. Leave before the traffic locks the coast road around sunset.", "Back in Sanur. Eat grilled seafood or a simple nasi campur. Seminyak's beach clubs are a night out, not a reason to miss the last taxi.", "Agree the taxi fare before you get in, both ways. Ride-hailing apps work in South Bali and still surge at sunset.", "Seminyak"),
        day(3, "Ubud, as a day, not a move", "The rice-terrace and monkey-forest day, with a driver, and your bed still on the beach.", "Leave by 8:00. Sacred Monkey Forest first, before the midday tour buses. Hold your bag and do not feed the monkeys.", "Walk the central Ubud lanes, then a rice-terrace lookout. Tegallalang is the crowded one; a driver who skips the main parking lot is worth it. Lunch in town, then the 90-minute return.", "A quiet dinner on the Sanur path. You will be tired of the car. Do not add Tanah Lot on the same day.", "A private driver for the day is the right tool. A series of taxis will cost the same and waste the afternoon.", "Ubud"),
        day(4, "A last swim, then the airport", "Sanur is one of the easier beach hotels to leave from. Keep the morning on the sand.", "Swim and coffee on the path. A short visit to the market streets off Danau Tamblingan if you still want a walk.", "Be at the airport two hours before an international flight. The drive is short until it is not; leave a cushion after lunch.", "Eat before the airport. The terminal is a compromise after four days of grilled fish and nasi campur.", "Tanah Lot looks close on a map and is a half-day from Sanur with traffic. It does not fit a departure morning.", "Tanah Lot"),
    ],
    attractions=[
        sight("Sanur Beach", "A long public path behind a protective reef, which is why the swimming is calmer than Kuta.", "Go out on the sand at low tide and ask the hotel where the current runs.", "Sanur, Bali"),
        sight("Seminyak Beach", "The louder, wider sunset beach. Worth a taxi, not worth blowing the room budget.", "Leave before the coast road clots in the late afternoon.", "Seminyak"),
        sight("Sacred Monkey Forest Sanctuary", "The Ubud forest temple full of long-tailed macaques. It is the one Ubud stop that is actually wild.", "No food in your hands, no loose sunglasses, go early.", "Sacred Monkey Forest Sanctuary"),
        sight("Ubud", "The town around the forest: lanes, a palace courtyard, and rice fields at the edge.", "One day from Sanur is enough. Sleeping there is a different trip.", "Ubud"),
        sight("Tanah Lot", "The sea temple on a rock, best as its own outing if you have a free late afternoon on another visit.", "It does not combine well with a flight or with Ubud.", "Tanah Lot"),
        sight("Jimbaran Bay", "The sunset grilled-fish beach south of the airport. A taxi dinner, not a place to move hotels.", "Pick a warung with a price list and a visible grill, and agree the fish price before it hits the fire."),
    ],
    scenic_routes=[
        route("Sanur beach path", "From the north end of the public path down past the hotel gardens to Mertasari. Banyan trees, fishing boats, and reef.", "About 5 km, an hour if you swim in the middle"),
        route("Driver to Ubud", "Sanur to the Monkey Forest, a short rice-terrace stop, lunch, and back. One direction is 1 to 1.5 hours.", "A full day, about 8 hours door to door"),
        route("Taxi to Jimbaran for fish", "South around the airport to the grill warungs on Jimbaran Bay. Go for sunset and leave before the last tables turn over.", "30 to 50 minutes each way"),
    ],
    transport="Taxis and ride-hailing cars. Sanur is walkable once you are on the beach path, and nowhere else on this itinerary is. A hired driver is the right call for Ubud. Scooters are a local habit and a common injury for visitors; skip one if you do not ride at home. The airport is close, which is a real advantage over Uluwatu.",
    food=[
        dish("Nasi campur", "A warung along Jalan Danau Tamblingan or the beach path", "Rice with a tray of small dishes. Point at what you want. It is the ordinary good lunch."),
        dish("Grilled fish", "Jimbaran Bay warungs, or the hotel beach", "Whole fish, sambal, water spinach. Ask the price per fish before they cook it."),
        dish("Babi guling", "A Ubud stall on the day you go up the hill", "Balinese spit-roasted pig. The well-known spot sells out; go before 1 p.m. Skip it if you do not eat pork."),
        dish("Satay lilit", "Sanur warungs and the night tables on the path", "Minced seafood satay pressed onto lemongrass stalks. Order a stick or two beside the rice, not as a whole cuisine."),
    ],
    tips=[
        "Book Puri Santrian or Prama if the cap is firm. Check Maya Sanur's live rate in July, August, and late December before you assume it qualifies.",
        "The reef is not a swimming pool. Ask about tide and current, and do not walk on coral.",
        "A 'private pool villa' under $300 in this part of Bali is a different search. These three are beach hotels.",
        "Ubud and Tanah Lot are separate days. Putting both on a departure day is how people miss flights.",
    ],
    faqs=[
        faq("Can I actually stay on the beach for under $300?", "Yes in Sanur, for a real room at Puri Santrian or Prama, most weeks of the year. Maya Sanur joins them outside July, August, and Christmas. The famous Seminyak cliff and beach icons, including The Legian, usually do not."),
        faq("Is the water swimmable?", "Inside the reef, on a calm day, yes. It is shallow and gentle compared with Kuta. Low tide leaves a long flat. Ask the hotel that morning."),
        faq("Should I stay in Seminyak instead?", "Only if nightlife matters more than the room rate. A true beachfront room there breaks $300 more often. Visit for an afternoon."),
        faq("Do these rooms have private pools?", "No. They have hotel pools and the sea. A private pool is a villa category and a different budget."),
    ],
    map_places=[
        stop("Sanur Beach", "Sanur", "Indonesia", "Sanur, Bali"),
        stop("Puri Santrian", "Sanur", "Indonesia"),
        stop("Sacred Monkey Forest Sanctuary", "Ubud", "Indonesia", "Sacred Monkey Forest Sanctuary"),
        stop("Ubud", "Ubud", "Indonesia", "Ubud"),
        stop("Jimbaran Bay", "Jimbaran", "Indonesia"),
        stop("Tanah Lot", "Tabanan", "Indonesia", "Tanah Lot"),
    ],
    budget_notes="Lodging at $110-280 is realistic for these three outside Christmas, with Maya the one that spills over in peak weeks. Food stays near $25-45 a day if lunch is a warung and dinner is grilled fish. A driver to Ubud is about $40-60 for the day. The beach path is free. Taxis to Seminyak add $15-25 each way in ordinary traffic.",
))

add(trip(
    slug="bali-2-bedroom-under-400night",
    title="A two-bedroom villa in Seminyak or Canggu, outside the peak weeks",
    location="Bali, Indonesia",
    summary=(
        "Four nights in a two-bedroom villa with a private pool in Seminyak or Canggu. That product exists "
        "under $400 a night in ordinary months. It does not exist at Amankila, and it gets scarce in August "
        "and from about 20 December through early January, when the same villa often jumps past $500. "
        "Book the two-bedroom category by name. A one-bedroom pool suite is a different room."
    ),
    who="Friends or a small family who want two real bedrooms and a pool that is not the hotel's.",
    best_time="February through June, and September through November. Avoid August and Christmas to New Year if $400 is a hard cap.",
    nights=4,
    hook="4 nights · Two bedrooms, private pool · Under $400 outside August and Christmas",
    constraints=["Two bedrooms", "Under $400 a night", "Canggu or Seminyak", "Private pool is the villa, not the hotel pool"],
    lodging="$220-400",
    daily="$300-460",
    neighborhoods=[
        stay_area("Seminyak and Petitenget", "Walkable restaurants and a beach about 10 minutes on foot from the villa lanes. Louder than Sanur, easier than Ubud if you want the sea."),
        stay_area("Canggu and Berawa", "A beach town that grew up around surf and cafés. The two-bedroom pool villa is the local product. Evenings are livelier than a Nusa Dua resort."),
    ],
    hotels=[
        hotel("Peppers Seminyak", "Petitenget, Seminyak", "One- to five-bedroom villas, each with a private pool. The two-bedroom has a kitchen, which is uncommon in a hotel villa. Outside August and Christmas week the two-bedroom often lands under $400; those peak weeks often do not. It is a villa resort with a restaurant and a kids' club, not a house with no staff.", "$280-550", "Seminyak, Bali", "https://www.peppersseminyak.com/"),
        hotel("The Elysian Boutique Villa Hotel", "Seminyak", "A small Seminyak villa hotel. The two-bedroom villa has a private pool and two king bedrooms. The hotel's own description lists tea and coffee, not a full kitchen, so do not book it as a cooking trip. The rate for this villa often sits under $400 outside August and the Christmas holidays.", "$250-480", "Seminyak, Bali", "https://theelysian.com/"),
        hotel("Lv8 Resort Hotel", "Berawa, Canggu", "A beachfront-area hotel in Canggu. Ask for the two-bedroom suite with private pool, about 160 square metres. Other suites share the resort pool or are one-bedroom. A private-pool two-bedroom here can fit under $400 outside peak; confirm the category name on the booking so you are not handed a garden suite.", "$200-420", "Canggu, Bali"),
    ],
    itinerary=[
        day(1, "Villa first, beach second", "The pool is the point of the rate. Use it before you cross town.", "Settle in, check that you actually received two bedrooms and a private pool, and say so at the desk if the category is wrong. That conversation is easy on arrival and miserable on night two.", "Walk or grab a short ride to the nearest beach: Petitenget or Seminyak from Peppers or The Elysian, Berawa or Batu Bolong from Lv8.", "Dinner within a 10-minute ride. If you are at Peppers, one night in is reasonable because the kitchen is real. The other two hotels are restaurant nights.", "Canggu traffic at sunset is slow. Eat near the villa on night one.", "Seminyak"),
        day(2, "A temple, then back to the pool", "One sightseeing block in the morning so the villa does not become a base you never leave, or a base you abandon.", "Tanah Lot in the morning, before the heat and the tour groups. From Canggu or Seminyak it is under an hour. The rock temple is the view; the market around it is skippable.", "Back by early afternoon. Swim in your own pool. A beach hour if the tide is right.", "Dinner out: seafood or a simple Indonesian grill. Sleep at the villa, not in a club.", "Tanah Lot's stair and the wet rocks are slippery. It is a lookout as much as a visit.", "Tanah Lot"),
        day(3, "Ubud for the day", "The same rule as a beach hotel: go up, come back, keep the villa.", "Driver at 8:00. Monkey Forest, a walk through town, lunch.", "A rice-field stop on the way back, then your own pool at 4:00. That order is the whole trick.", "Cook at Peppers if you bought groceries in the morning, or eat near the villa. A second night in Ubud is a different trip.", "Do not ride a scooter over the hills after a long lunch.", "Ubud"),
        day(4, "Pool, beach, airport", "Departure day stays local. The airport is 40 to 70 minutes from Canggu depending on the hour.", "A last swim in the private pool. Coffee on the villa terrace.", "Leave after lunch for an afternoon or evening flight, earlier if the flight is at midday. Berawa to the airport looks short and is not, once the school run starts.", "Eat before you go. Airport food is the letdown after a villa kitchen or a Petitenget grill.", "Photograph the villa on day one. Day four is bags and pool water.", "Kuta, Bali"),
    ],
    attractions=[
        sight("Seminyak Beach", "The sunset beach closest to the Petitenget villas.", "Walk it in the late afternoon and leave the main club strip when you have seen it.", "Seminyak"),
        sight("Berawa and Batu Bolong", "Canggu's beach pair. Surf in the morning, cafés behind the sand.", "Batu Bolong's current is for surfers. Swim only where it is obviously shallow and watched."),
        sight("Tanah Lot", "The sea temple worth the short morning drive from these villas.", "Go early. The sunset crowd is the postcard and the traffic.", "Tanah Lot"),
        sight("Ubud", "A day of town lanes and a forest temple, then back to a pool that is yours.", "Keep the luggage at the villa. Do not try to sleep in both places.", "Ubud"),
        sight("Sacred Monkey Forest Sanctuary", "The one Ubud attraction that is not a shop.", "Zip bags. The macaques know pockets.", "Sacred Monkey Forest Sanctuary"),
        sight("Petitenget Temple", "A neighborhood temple a short walk from the Seminyak villas. A 20-minute stop, not a tour.", "Dress with a sarong if you go inside. The beach just beyond it is the longer outing."),
    ],
    scenic_routes=[
        route("Villa lane to the beach", "From Petitenget or Berawa, a short walk or a five-minute car to the sand. This is the daily route, and it should stay short.", "Under 2 km"),
        route("Morning to Tanah Lot", "Seminyak or Canggu west to the sea temple and straight back, before lunch.", "About 45 to 70 minutes each way"),
        route("Ubud day with a driver", "Monkey Forest, lunch, one rice-terrace viewpoint, villa by late afternoon.", "About 8 hours, with 1 to 1.5 hours of driving each way"),
    ],
    transport="A mix of walking, short ride-hailing trips, and one hired driver for Ubud and Tanah Lot. The villa lane is rarely the beach itself. Canggu scooters are dense; riding one home after dinner is the common mistake. Airport transfers should be booked, not hailed at the last minute, because Berawa's exit roads jam.",
    food=[
        dish("A villa breakfast", "Peppers, if you use the kitchen", "The two-bedroom there has a real kitchen. The Elysian and Lv8 are not the places to plan a grocery dinner unless your confirmation says otherwise."),
        dish("Nasi goreng or mie goreng", "A warung between the villa and the beach", "The cheap good dinner. Eat it on night one before you spend club prices."),
        dish("Grilled seafood", "A beach warung at Berawa or along Seminyak", "Fish, squid, sambal, rice. Check the chalkboard price."),
        dish("Babi guling", "Ubud, on the day-trip lunch", "Roast pig on rice. Go early in the lunch window. Plenty of non-pork plates sit beside it if someone in the group skips it."),
    ],
    tips=[
        "The booking must say two bedrooms and private pool. A 'villa' in the hotel name is not that promise.",
        "August and 20 December to early January are when this search fails. Those weeks, raise the cap or change the dates.",
        "Peppers is the kitchen. Do not expect to cook at The Elysian from the description on its own site.",
        "Amankila, the Four Seasons, and the Uluwatu cliff hotels are the wrong names for a $400 two-bedroom.",
    ],
    faqs=[
        faq("Is a two-bedroom private-pool villa really under $400?", "Often, at these three, outside August and Christmas to New Year. In those weeks the same category commonly runs $500 and up. I am not quoting a live rate; check the category before you pay."),
        faq("Which one has a kitchen?", "Peppers Seminyak's villas do, including the two-bedroom. The Elysian's two-bedroom lists tea and coffee, not a kitchen. Lv8's pool suite is a hotel suite; do not assume a stove."),
        faq("Are the pools private?", "Only in the categories named: Peppers villas, The Elysian's two-bedroom villa, and Lv8's two-bedroom suite with private pool. A stay in a cheaper room at Lv8 uses the resort pool."),
        faq("Is Canggu quiet?", "Quieter than Kuta's bar street, livelier than Sanur or Nusa Dua. If the group wants silence, this is the wrong page."),
    ],
    map_places=[
        stop("Peppers Seminyak", "Seminyak", "Indonesia"),
        stop("Berawa Beach", "Canggu", "Indonesia"),
        stop("Tanah Lot", "Tabanan", "Indonesia", "Tanah Lot"),
        stop("Ubud", "Ubud", "Indonesia", "Ubud"),
        stop("Seminyak Beach", "Seminyak", "Indonesia", "Seminyak"),
    ],
    budget_notes="The two-bedroom pool villa is the whole budget: $220-400 in shoulder months, often more in August and late December. Food drops if you cook at Peppers and rises if you eat on the Seminyak beach. A driver for Ubud is a modest extra beside the room. Do not add a cliff-hotel night to 'balance' the trip; that single night can cost more than the four villa nights.",
))

add(trip(
    slug="bali-family-friendly-with-kitchen",
    title="A family apartment or villa in Bali with a real kitchenette",
    location="Bali, Indonesia",
    summary=(
        "Four nights for a family that wants to make breakfast and keep snacks in a fridge. In Bali that "
        "means an apartment suite or a villa with a kitchen, not a kids' club room with a minibar. Nusa Dua "
        "is the calm version: a gated beach resort area with kitchenette suites. Canggu is the livelier "
        "version, a small villa hotel where the kitchen and the private pool are in the villa. Ubud is "
        "peaceful and a poor place to swim, so it is not the base here."
    ),
    who="Parents with children who will eat cereal at 6:30 a.m. and do not want a different restaurant for every meal.",
    best_time="April to June, or September to early November. School holidays in July, August, and late December fill Nusa Dua and lift villa rates.",
    nights=4,
    hook="4 nights · Kitchenette or villa kitchen · Nusa Dua or Canggu",
    constraints=["Family", "Kitchen in the unit", "Calmer than Kuta"],
    lodging="$160-420",
    daily="$250-420",
    neighborhoods=[
        stay_area("Nusa Dua", "A gated resort coast with a calm beach, a kids' club at the big hotels, and almost no traffic inside the enclave. The most practical family base on this list."),
        stay_area("Canggu", "A real villa kitchen and a private pool, with cafés and surf just outside. Better for older children than for toddlers who need a kids' club and a quiet road."),
    ],
    hotels=[
        hotel("Novotel Bali Nusa Dua Hotel & Residences", "ITDC complex, Nusa Dua", "Book an apartment suite, not a standard room. Accor equips the apartment suites with a kitchenette plus a living and dining area, including two-bedroom layouts. There is a kids' club, a lagoon pool, and a shuttle to the beach club about two minutes away. A kitchenette means a small stove and a fridge, not a chef's kitchen.", "$160-320", "Nusa Dua, Bali", "https://all.accor.com/hotel/6328/index.en.shtml"),
        hotel("Marriott's Bali Nusa Dua Gardens", "Nusa Dua", "Residence-style villas in the same gated area, sold with kitchenettes. Confirm the specific villa includes the kitchenette and ask how many bedrooms it has. The beach and the resort pools are the day; the kitchenette is for breakfast and one simple dinner. This is a family campus, not a private house.", "$180-400", "Nusa Dua, Bali"),
        hotel("The Wina Canggu", "Canggu", "A small villa hotel: one- and two-bedroom villas, each with a private pool, a kitchen, and a living room, a short walk from the beach. Book the two-bedroom if you need the space. It is a better cooking setup than a Nusa Dua kitchenette, and a noisier street. There is no large kids' club.", "$140-280", "Canggu, Bali", "https://thewinaresorts.com/the-wina-canggu/"),
    ],
    itinerary=[
        day(1, "Pool, beach, early dinner", "Arrival day stays inside the resort gate or the villa lane. Children do not need a temple after a flight.", "Check the kitchenette or kitchen before the shops close. Buy milk, fruit, bread, and snacks at the nearest supermarket on the way from the airport if you can face the stop.", "Nusa Dua: shuttle to the beach club and a shallow swim. Canggu: the villa pool first, the beach only if everyone still has patience.", "Dinner in the apartment or a simple hotel meal before 7:30. The first night is not Jimbaran.", "Ask for a crib, a high chair, and where breakfast ingredients actually are. A 'kitchenette' without pans is a fridge.", "Sanur, Bali"),
        day(2, "The calm beach", "One beach, used properly, beats three sights.", "Morning swim. In Nusa Dua the water in front of the resort coast is the easy one. In Canggu, swim only in a guarded shallow stretch; Batu Bolong is a surf break.", "Back to the unit for lunch from the kitchen. This is the meal the kitchen is for. A nap. Then the pool.", "A short dinner out if energy remains: Nusa Dua's Bali Collection for something easy, or a Canggu warung a few minutes away. Otherwise cook again.", "Reef shoes help on the rocky bits of sand. The midday sun is the real hazard; swim before 10:30 and after 3:30.", "Kuta, Bali"),
        day(3, "One outing that ends at the pool", "A half-day, not a cross-island tour. Uluwatu's cliffs are a bad idea with small children late in the day.", "Nusa Dua Waterblow and the beach path, or a Pandawa Beach hour, which is close. Canggu families can do the same and stay local: a morning surf lesson for older kids, then home.", "Groceries if you are thin, then the pool all afternoon. The kids' club at the Novotel is there for a parent to take an hour.", "Cook or eat early. A bedtime at the villa is the luxury.", "Skip the kecak fire dance with overtired children. It starts at sunset and ends in a crowd."),
        day(4, "Breakfast in, airport after lunch", "Use the kitchen one last time. The flight is the only appointment.", "Breakfast in the suite. A last pool swim.", "Leave earlier than the map suggests. Nusa Dua to the airport is often 30 to 50 minutes; Canggu can be an hour.", "Eat the leftovers or an early lunch before you go. Hungry children and an airport queue are a bad pair.", "Confirm the apartment is the category with the kitchenette on the way out, in case you need to tell the next booking what worked."),
    ],
    attractions=[
        sight("Nusa Dua beach", "A managed resort beach with calm water on a normal day. The right swim for small children.", "Use the hotel shuttle and the flags. The enclave is walkable; the roads outside it are not."),
        sight("Pandawa Beach", "A white-sand beach a short drive from Nusa Dua, with a cliff behind it.", "Go in the morning. It is a beach, not a pool, and the sun is direct."),
        sight("Nusa Dua Waterblow", "A short cliff lookout where the swell hits a gap in the rock. Twenty minutes, then ice cream.", "Hold hands near the edge. It is a viewpoint, not a playground."),
        sight("Berawa Beach", "The Canggu option: sand, cafés, and surf.", "Small children stay in the villa pool. Older children can watch the surf lesson before they join one."),
        sight("Bali Collection", "The open-air shopping and food court inside Nusa Dua. Useful, not cultural.", "It solves a rainy afternoon and a picky dinner."),
        sight("Ubud, another trip", "Rice fields and the monkey forest are wonderful and a long day from Nusa Dua with kids.", "Save Ubud for a visit when the drive is the plan, not an add-on.", "Ubud"),
    ],
    scenic_routes=[
        route("Resort gate to the beach club", "The Novotel shuttle or a short walk inside the Nusa Dua enclave to the sand. Do this twice a day rather than touring.", "A few minutes"),
        route("Nusa Dua to Pandawa", "A short local drive for a different beach, then back for lunch in the kitchenette.", "About 20 to 30 minutes each way"),
        route("Airport to the supermarket to the villa", "The arrival route that makes day two easier. Stock the kitchen before you unpack the beach bag.", "40 to 70 minutes depending on base and traffic"),
    ],
    transport="Hotel shuttles inside Nusa Dua, and a prebooked car from the airport. Canggu is ride-hailing and walking. Do not put a family on scooters. A full-day driver is optional here; the kitchen and the beach are the trip, and a long scenic day works against tired children.",
    food=[
        dish("Breakfast from the kitchenette", "The apartment or The Wina villa", "Eggs, fruit, toast, coffee. This is the reason you booked this page instead of a room-only resort."),
        dish("Nasi campur", "A warung at Bali Collection or near the Canggu villa", "A shared tray of rice and small dishes. Easy for children who will eat the chicken and leave the sambal."),
        dish("Grilled fish and rice", "A simple beach lunch, one of the four days", "One restaurant fish meal is plenty. The other lunches belong in the villa."),
        dish("Fruit and snacks", "Supermarket on the way from the airport", "Papaya, banana, yogurt, and something familiar. The kitchen does nothing if you arrive with no food."),
    ],
    tips=[
        "At the Novotel, the kitchenette is in the apartment suites. A standard room will not have one.",
        "The Wina's kitchen is in the villa, and so is the private pool. Nusa Dua's pools are shared, which is what many children actually want.",
        "A minibar is not a kitchen. If the listing does not say kitchen or kitchenette, it is the wrong room.",
        "Kuta's big family resorts have kids' clubs and no place to cook. They answer a different question.",
    ],
    faqs=[
        faq("Will we have a full kitchen?", "At The Wina, the villa is advertised with a kitchen. At the Novotel, book an apartment suite and expect a kitchenette. At Marriott's Bali Nusa Dua Gardens, confirm the villa's kitchenette in writing. None of these is a private chef."),
        faq("Is Nusa Dua better than Ubud with children?", "For swimming and short walks, yes. Ubud is calm and inland. This trip assumes you want the sea and a stove."),
        faq("Is Canggu safe for little kids?", "The villa is. The beach break and the scooters are the hazards. Stay in the pool with small children and use a car at night."),
        faq("What does this cost?", "Apartment suites and these villas often run $160-400 outside school holidays. August and Christmas cost more and sell out of two-bedroom layouts first."),
    ],
    map_places=[
        stop("Nusa Dua", "Nusa Dua", "Indonesia"),
        stop("Pandawa Beach", "Kutuh", "Indonesia"),
        stop("Berawa Beach", "Canggu", "Indonesia"),
        stop("Novotel Bali Nusa Dua", "Nusa Dua", "Indonesia"),
        stop("Ngurah Rai International Airport", "Denpasar", "Indonesia"),
    ],
    budget_notes="Lodging at $160-420 covers a kitchenette apartment in Nusa Dua or a two-bedroom pool villa at The Wina in ordinary months. Cooking breakfast and one dinner pulls food down toward $40-70 for a family, against $100-plus if every meal is a restaurant. The kids' club at the Novotel is included for guests; surf lessons and taxis are not. Peak school-holiday weeks can wipe out the two-bedroom inventory.",
))

add(trip(
    slug="bali-pet-friendly",
    title="Bali without the dog: rabies, villas that say no, and a beach week anyway",
    location="Bali, Indonesia",
    summary=(
        "Four nights on a Sanur or Seminyak beach, or in Ubud, with the dog left at home. Bali has rabies. "
        "Bringing a dog into Indonesia is an import-permit and quarantine project, not a holiday plan, and "
        "the well-known hotels on this page should be treated as no-pets unless you hold a written yes for "
        "the exact room. This is still a full beach and rice-field trip. The pet constraint is unmet."
    ),
    who="Someone who hoped to travel with a dog, and who needs a straight answer before they buy the ticket.",
    best_time="Late April to June, or September. The weather is kind and the hotels are easier to book. The pet answer does not change with the season.",
    nights=4,
    hook="4 nights · Leave the dog at home · Sanur, Seminyak, or Ubud",
    constraints=["Pet-friendly search, unmet", "Do not bring a dog without written permission", "Rabies is present in Bali"],
    lodging="$180-450",
    daily="$260-420",
    neighborhoods=[
        stay_area("Sanur", "The calm beach. Tandjung Sari has been here since the 1960s, in bungalows behind the sand. A good base if the trip goes ahead without a pet."),
        stay_area("Seminyak or Ubud", "The Oberoi is the long-running Seminyak beach hotel. Maya Ubud is the valley alternative, with a river and no sea. Neither is a reason to fly a dog in."),
    ],
    hotels=[
        hotel("Tandjung Sari", "Sanur beach", "A garden of bungalows on Sanur beach, opened in the 1960s. The family bungalow is two bedrooms with a minibar and tea, not a kitchen, and not a pet room. Treat the hotel as no-pets unless you have an email that names the bungalow and the dates.", "$180-400", "Sanur, Bali", "https://www.tandjungsarihotel.com/"),
        hotel("The Oberoi Beach Resort, Bali", "Seminyak beach", "A beachfront hotel that has been on this sand since the late 1970s, with lanai rooms and villas. I have no basis to call it pet-friendly. Book it for the garden and the beach, and leave the dog at home.", "$350-700", "Seminyak, Bali"),
        hotel("Maya Ubud Resort & Spa", "Ubud, Petulu", "A long-running valley resort above a river, with pools and villas. It is the right hotel if the trip becomes an Ubud stay. It is not a documented dog hotel. Confirm any exception in writing, and expect the answer to be no.", "$200-450", "Ubud, Bali"),
    ],
    itinerary=[
        day(1, "Arrive without a kennel", "The day is easier because you are not clearing an animal. Use that.", "Sanur or Seminyak: beach path and a swim. Ubud: the hotel valley and a slow lunch, not the monkey forest on hour one.", "Unpack and walk. In Sanur, the reef beach. In Seminyak, the sand in front of the Oberoi and a short walk toward Petitenget. In Ubud, the hotel's own ridge path.", "Dinner near the hotel. Do not make a pet-friendly-café project out of the evening. Bali cafés that post a dog photo are not a customs clearance.", "If a villa told you a dog might be allowed, and you do not have it in writing, the answer for this trip is still no.", "Sanur, Bali"),
        day(2, "The neighborhood on foot", "One area, done properly.", "Sanur: the full beach path by bike or on foot, plus a warung lunch. Seminyak: Petitenget temple and the beach. Ubud: the town lanes and the market in the morning.", "A single longer stop. Sanur can taxi to Seminyak for a late lunch and come back. Ubud walks to the rice-field edge and stops before the hills.", "Dinner at the hotel or one good table nearby. Tandjung Sari's seaside restaurant is the point of staying there.", "Street dogs are common and some are not healthy. Do not pet them, and do not let children feed them.", "Seminyak"),
        day(3, "Ubud, or the sea temple", "If you are already in Ubud, this is the monkey forest and a terrace view. If you are on the coast, pick one: Ubud or Tanah Lot, not both.", "Coast hotels: a driver at 8:00 for Ubud, Monkey Forest first. Ubud hotel: Monkey Forest at opening, then the town.", "A terrace lunch, then back. Coast hotels should be on the beach path by late afternoon. The Ubud hotel should be at the pool.", "A quiet dinner. You are halfway through a trip that works because the pet stayed home.", "The monkey forest is the wrong place for a pet even if a hotel had agreed. Macaques and a visiting dog are a bad meeting.", "Sacred Monkey Forest Sanctuary"),
        day(4, "Beach or valley, then the flight", "Keep the last morning where you slept.", "Swim or walk. Buy coffee and snacks. No new region.", "Airport from Sanur or Seminyak is the easy version. From Ubud, leave extra time; the hill road and the coast road both jam.", "Eat a proper lunch before the terminal.", "Get any future pet promise by email, naming the animal, the weight, and the dates. A front-desk shrug is not a yes.", "Ubud"),
    ],
    attractions=[
        sight("Sanur Beach", "The reef beach in front of Tandjung Sari. Calm water, a long path, no need for a car once you arrive.", "Walk at dawn if you want it empty.", "Sanur, Bali"),
        sight("Seminyak Beach", "The Oberoi's coast. Wider surf, a proper sunset, more people.", "The hotel's beach is the quiet piece. The club stretch north is optional.", "Seminyak"),
        sight("Ubud", "The town you add as a day from the coast, or the place you stay if Maya Ubud is the hotel.", "One overnight in each is how bags get lost. Pick one base.", "Ubud"),
        sight("Sacred Monkey Forest Sanctuary", "The forest temple in Ubud. Go early and keep food sealed.", "This is not a pet stop under any reading of the signs.", "Sacred Monkey Forest Sanctuary"),
        sight("Tanah Lot", "The sea temple west of Seminyak, a morning drive if you skip Ubud.", "Sunset is crowded. Morning is the visit.", "Tanah Lot"),
        sight("Petitenget Temple", "A living temple at the north end of Seminyak beach, an easy walk from the Oberoi side.", "Sarong if you enter. The beach beside it is the longer pleasure."),
    ],
    scenic_routes=[
        route("Sanur beach path", "The full promenade from the north end to Mertasari, out and back, with a swim in the middle.", "About 5 km"),
        route("Coast to Ubud with a driver", "A morning departure, Monkey Forest, lunch, back to the beach hotel before dark.", "A full day"),
        route("Seminyak to Tanah Lot", "A morning out-and-back if day three is not already Ubud.", "Under an hour each way in light traffic"),
    ],
    transport="Cars and your feet. Sanur's path is the walkable piece. Ubud's lanes are walkable in town and steep in the valleys. Do not plan the trip around moving a dog between a car, a villa, and a temple. The airport transfer is a ordinary car for people and bags.",
    food=[
        dish("Nasi campur", "A Sanur or Ubud warung", "The default lunch. Point at the dishes. Most places will make a mild plate for a child."),
        dish("Grilled fish", "Sanur beach or a Seminyak warung", "Whole fish, rice, sambal on the side. Eat it on the coast night."),
        dish("Babi guling", "Ubud, at lunch on the day you are there", "Roast pig. Arrive before it sells out. Skip it for a vegetarian table without making a scene; the town is full of other plates."),
        dish("Coffee on the hotel terrace", "Tandjung Sari, The Oberoi, or Maya Ubud", "One slow breakfast at the hotel is worth more than a café crawl, and none of those terraces is a dog run."),
    ],
    tips=[
        "Leave the dog at home. A holiday villa that 'loves dogs' on social media is not an Indonesian import permit.",
        "If you still ask a villa, get the yes in writing with dates, the dog's name, and the weight. Do not fly on a maybe.",
        "Do not pet street dogs. Rabies is present in Bali, and the bite is the crisis, not the inconvenience.",
        "These three hotels are excellent without a pet and should be booked as no-pet stays.",
    ],
    faqs=[
        faq("Can I bring my dog to Bali for this trip?", "Do not. Importing a dog into Indonesia means permits and quarantine, and Bali has rabies. None of the hotels listed here is a reason to try."),
        faq("Are any of these hotels pet-friendly?", "Treat all three as no. Tandjung Sari, The Oberoi, and Maya Ubud are here because they are real, long-running places to stay, not because they accept dogs. A written exception would have to come from the hotel, and you should assume it will not."),
        faq("What if a villa says yes?", "Get it in writing for that villa and those dates, and sort the import rules before you buy a plane ticket. A listing checkbox is not enough. This itinerary does not depend on that yes."),
        faq("Is the trip worth doing without the dog?", "Yes. Sanur or Seminyak gives you the beach, and Ubud gives you the hills. The week works as an ordinary Bali trip, which is what it is."),
    ],
    map_places=[
        stop("Sanur Beach", "Sanur", "Indonesia", "Sanur, Bali"),
        stop("Tandjung Sari", "Sanur", "Indonesia"),
        stop("The Oberoi Beach Resort", "Seminyak", "Indonesia"),
        stop("Maya Ubud", "Ubud", "Indonesia"),
        stop("Sacred Monkey Forest Sanctuary", "Ubud", "Indonesia", "Sacred Monkey Forest Sanctuary"),
    ],
    budget_notes="These hotels run about $180-450 at Tandjung Sari and Maya Ubud, and often $350-700 at The Oberoi. The pet you did not bring saves a quarantine bill and a ruined first day. Food is $30-60 a person if you mix warungs and one hotel dinner. There is no honest 'pet fee' to plan, because the right fee is the cost of a sitter at home.",
))

add(trip(
    slug="maldives-with-private-pool",
    title="A Maldives villa with its own pool, and the transfer that gets you there",
    location="Malé, Maldives",
    summary=(
        "Four nights in a villa whose private pool is the category you book, not the resort's main pool. "
        "Soneva Fushi and Four Seasons Landaa Giraavaru are seaplane resorts in Baa Atoll, about 30 minutes "
        "in the air and daylight only. One&Only Reethi Rah is a speedboat or resort yacht of about 45 to "
        "60 minutes in North Malé Atoll. A pool villa at any of the three commonly runs $1,500 to $5,000 "
        "a night before taxes and the transfer. This is not a city-hotel price."
    ),
    who="A couple, or a family using a two-bedroom pool villa, who have already decided the Maldives means one island and a big rate.",
    best_time="January to April for drier weather, which is also when the rate is highest. May to July and November are cheaper and wetter. Seaplanes still fly only in daylight.",
    nights=4,
    hook="4 nights · Private-pool villa · Seaplane or a 45-minute boat",
    constraints=["Private pool inside the villa", "One resort island", "Seaplane daylight rules if you pick Baa Atoll"],
    lodging="$1,500-5,000+",
    daily="$1,800-5,500+",
    neighborhoods=[
        stay_area("Baa Atoll", "Soneva Fushi and Four Seasons Landaa Giraavaru. UNESCO biosphere water, manta season roughly in the southwest monsoon months, and a seaplane that will not fly after dark."),
        stay_area("North Malé Atoll", "One&Only Reethi Rah. A long sand island with many beaches, reached by boat, so a late flight can still make the crossing."),
    ],
    hotels=[
        hotel("Soneva Fushi", "Kunfunadhoo, Baa Atoll", "Large beach villas with private pools, reached by a seaplane of about 30 minutes. A late arrival can use a domestic flight to Dharavandhoo and a short boat instead. The pool is part of the villa, including the one-bedroom categories. Rates sit far above a city suite, and drinks are extra on most plans. The Den is a kids' club if you are not traveling as a couple.", "$2,000-6,000+", "Baa Atoll, Maldives", "https://www.soneva.com/resorts/soneva-fushi"),
        hotel("Four Seasons Resort Maldives at Landaa Giraavaru", "Landaa Giraavaru, Baa Atoll", "A seaplane of about 30 to 35 minutes, daylight only. Book a villa with a private pool; the top residences have long lap pools, and a lower category is not the same product. If you land after the last seaplane you stay the night in Malé. There is a serious spa and a family program for younger children.", "$1,800-5,000+", "Baa Atoll, Maldives", "https://www.fourseasons.com/maldiveslg/"),
        hotel("One&Only Reethi Rah", "North Malé Atoll", "Speedboat or the resort yacht, about 45 to 60 minutes from Malé. No seaplane. Book a villa with a pool in the name, such as a grand beach villa or grand water villa with pool; do not assume every category includes one. The island is huge, with a kids' club and a separate club for teenagers. The boat fare is a large extra.", "$1,500-5,000+", "North Malé Atoll, Maldives", "https://www.oneandonlyresorts.com/reethi-rah"),
    ],
    itinerary=[
        day(1, "The transfer is the day", "You will not see Malé properly, and you should not try. Get to the villa before dinner.", "Clear the airport and the resort desk. Seaplane guests wait for daylight and a weight limit; boat guests to Reethi Rah have a longer wet ride and more flexibility after dark.", "Arrive, shower, and sit by the private pool. Snorkel only if the house reef is steps away and you are not exhausted. Soneva and Landaa both have house reefs; use the resort briefing.", "Dinner at the resort. There is no town to wander to. Half-board or a meal plan matters because the next restaurant is a boat ride away.", "Book the international flight to land before mid-afternoon if you are on a seaplane. Miss it and you have bought a night in Malé.", "Malé"),
        day(2, "House reef, then the pool you paid for", "A full day on the island. Do not add a second island.", "Guided house-reef snorkel in the morning. Listen to the guide about currents. The private pool is the afternoon, not the morning, or you will skip the reef.", "Lunch. A spa hour if you booked it before you arrived; the good times go first. Read a book by the pool.", "Dinner in a different restaurant on the same island. At Soneva the treetop table needs a reservation. At any of the three, barefoot is the dress code and 'smart casual' means a shirt.", "Sunscreen and a rash guard. The pool is easy; the reef at noon is how people get burned."),
        day(3, "One boat, if the resort is running it", "The only excursion worth leaving the pool for.", "If you are in Baa during manta season, take the resort's Hanifaru Bay trip and follow the park rules: no touching, no chasing. Out of season, take the resort's short sandbank picnic and be back for lunch.", "The private pool and a nap. A second snorkel on the house reef at 4:00 is enough adventure.", "A long dinner. You are not going anywhere afterward.", "Reethi Rah guests should not plan a Baa Atoll manta trip. That is a different archipelago. Use the resort's own boat.", "Hanifaru Bay"),
        day(4, "Morning water, then the airport direction", "Seaplane departures start early. Pack the night before.", "Sunrise swim, breakfast, bags. The pool at 7:00 is the goodbye.", "Transfer to Malé. A seaplane connection needs a gap before the international flight; the resort will tell you the latest flight you can make. Reethi Rah's boat is less fragile and still wants a buffer.", "If you have a long connection, eat at the airport. Do not book a city tour between the seaplane and a tight flight.", "The green tax, GST, and the transfer fare are not in the villa's headline number. Look at the total before you compare it with a city hotel.", "Maldives"),
    ],
    attractions=[
        sight("The villa pool", "The reason for the rate. At Soneva it is part of the villa. At Landaa and Reethi Rah it is a named category, so the confirmation has to say pool.", "Swim it in the afternoon, when you would otherwise be looking for a town."),
        sight("House reef", "The free, extraordinary thing. All three islands have reef; the quality depends on the wind that week.", "Go with the resort guide the first time. Currents are the hazard, not boredom."),
        sight("Hanifaru Bay", "The manta gathering place in Baa Atoll, in season, and only with a licensed boat.", "Do not book this from Reethi Rah. Different atoll.", "Hanifaru Bay"),
        sight("Baa Atoll", "A UNESCO biosphere. The water around Soneva and Landaa is the sight, not a museum ashore.", "Binoculars and a patient snorkel beat a packed excursion list."),
        sight("Reethi Rah's beaches", "Twelve beaches on one island. You can walk a long way and still be at the resort.", "Ask for a buggy if the villa is at the far end. The island is bigger than the brochure walk."),
        sight("Malé", "The capital you pass through. A real city, and not the holiday.", "See it only if a missed seaplane forces a night. Otherwise stay on the boat or the plane.", "Malé"),
    ],
    scenic_routes=[
        route("Seaplane to Baa Atoll", "Velana to Soneva Fushi or Landaa Giraavaru. About 30 to 35 minutes, daylight only, a fare per adult and per child. Soneva can also send you via Dharavandhoo on a domestic flight if you land late.", "Half a day once you count the wait"),
        route("Boat to Reethi Rah", "Resort speedboat or yacht from Malé, about 45 to 60 minutes. It can run later than a seaplane. The fare is compulsory and large.", "About an hour on the water"),
        route("Resort boat to a sandbank", "A short picnic boat from whichever island you chose. The right off-island trip when mantas are not in season.", "Two to four hours, back for lunch"),
    ],
    transport="There are no roads between these islands. You use the resort's seaplane or its boat, and you do not island-hop on a four-night trip. Seaplanes stop in the afternoon. A flight into Malé after about 3:30 p.m. often means a hotel night in Malé before a Baa Atoll resort. Reethi Rah's boat is the more forgiving arrival. Baggage on a seaplane is tighter than the international allowance; check the kilos.",
    food=[
        dish("Resort breakfast", "The main restaurant, or a floating breakfast in the private pool if the villa offers it", "Fruit, eggs, and Maldivian mas huni if it is on the buffet: smoked tuna, coconut, onion, and chili."),
        dish("Grilled reef fish", "Any of the island's restaurants", "The cooking is the resort's. Ask what is local and what was flown in. Skip parrotfish even if a menu offers it."),
        dish("Mas huni", "Breakfast buffet", "The national breakfast. Tuna, grated coconut, onion, lime, and chili with roshi flatbread. Milder versions exist for children."),
        dish("A tasting menu, one night", "Soneva's reserved tables, or the main restaurant at Landaa or Reethi Rah", "One ambitious dinner is enough. The other nights, eat simply. The bill for drinks can rival the food."),
    ],
    tips=[
        "The private pool has to be in the room category. A beautiful resort pool is the thing you were trying not to book.",
        "Land in Malé early in the day for a seaplane. Reethi Rah is the choice if your flight arrives at night.",
        "Transfers are often $400-900 per adult round trip, sometimes more, and children over two usually pay. Get the number in the quote.",
        "Four nights is three swims and one excursion. A longer list of islands will spend the holiday in transit.",
    ],
    faqs=[
        faq("Is the pool really private?", "At Soneva Fushi the villas come with their own pools. At Four Seasons Landaa Giraavaru and One&Only Reethi Rah, book a villa that says pool. A beach villa or a water villa without that word may have only the lagoon and the resort pools."),
        faq("What does it cost?", "Commonly $1,500 to $5,000 a night for a pool villa before taxes, service, the green tax, and the transfer. Christmas and New Year go higher. This page will not pretend otherwise."),
        faq("Seaplane or speedboat?", "Soneva Fushi and Landaa Giraavaru: seaplane, about half an hour, daylight only. Reethi Rah: boat, about 45 to 60 minutes, including later in the evening. Pick the hotel around your flight time."),
        faq("Can we leave the island for dinner?", "No, not usefully. Dinner is on the resort. Choose the meal plan with that in mind, and ask whether drinks are included. Often they are not."),
    ],
    map_places=[
        stop("Velana International Airport", "Malé", "Maldives"),
        stop("Soneva Fushi", "Baa Atoll", "Maldives"),
        stop("Four Seasons Landaa Giraavaru", "Baa Atoll", "Maldives"),
        stop("One&Only Reethi Rah", "North Malé Atoll", "Maldives"),
        stop("Hanifaru Bay", "Baa Atoll", "Maldives", "Hanifaru Bay"),
    ],
    budget_notes="Budget the villa at $1,500-5,000+ a night, then add a seaplane or boat that can run several hundred dollars per adult each way, plus taxes and the green tax. A meal plan changes the daily number more than taxis ever could, because there are no taxis. One spa treatment and one photo trip are the extras that surprise people. Four nights is the minimum that survives a transfer day on each end.",
))

add(trip(
    slug="maldives-2-bedroom-under-400night",
    title="The honest Maldives search for a two-bedroom under $400",
    location="Malé, Maldives",
    summary=(
        "Four nights at a well-known mid-range resort, with a straight answer on the price. A two-bedroom "
        "overwater villa under $400 a night is not a real Maldives product. Bandos, Kandima, and Kuramathi "
        "are the closest famous-enough islands: a beach room can sometimes fall near $250 to $450 in the "
        "green season, and a true two-bedroom is usually higher, often well clear of $400 once taxes and "
        "the transfer are counted. Bandos is a short speedboat. Kandima and Kuramathi need a seaplane or, "
        "at Kuramathi, a 90-minute boat."
    ),
    who="Friends or a family trying to split a two-bedroom, who need the real range before they fall for a thumbnail.",
    best_time="May to July and October to November for the lowest room rates, with more rain. December to April is the dry, expensive season, and it will not rescue this budget.",
    nights=4,
    hook="4 nights · Two-bedroom search, mostly unmet · $250-900 real range",
    constraints=["Two bedrooms under $400, unmet for a water villa", "Say the real nightly range", "Speedboat versus seaplane"],
    lodging="$250-900",
    daily="$400-1,100",
    neighborhoods=[
        stay_area("North Malé Atoll, Bandos", "About 10 to 20 minutes by speedboat from the airport. The practical choice if a late flight and a lower rate matter more than a huge island."),
        stay_area("Dhaalu and Rasdhoo", "Kandima is a seaplane of about 40 minutes to Dhaalu Atoll. Kuramathi, in Rasdhoo Atoll, is a 20- to 25-minute seaplane or a shared speedboat of about 90 minutes."),
    ],
    hotels=[
        hotel("Bandos Maldives", "North Malé Atoll", "One of the older resort islands, a short speedboat from Velana. Beach rooms and villas can land in the few-hundred-dollar range in low season. A two-bedroom overwater villa at $350 is not the booking to expect. Ask for the two-bedroom rate in writing and assume it sits higher than the entry room.", "$220-600", "North Malé Atoll, Maldives"),
        hotel("Kandima Maldives", "Dhaalu Atoll", "A large mid-range island with sky studios and family rooms, about 40 minutes by seaplane. A two-bedroom family sky suite has been advertised from just over $400 before taxes and transfers, in the cheapest month, for two adults. That is a floor, not a typical bill. It is not an overwater villa, and most weeks cost more.", "$300-800", "Dhaalu Atoll, Maldives"),
        hotel("Kuramathi Maldives", "Rasdhoo Atoll", "A long-running island with many room types, including two-bedroom beach houses. You can arrive by seaplane in about 25 minutes or by speedboat in about 90 minutes. Seaplanes stop in the afternoon. The two-bedroom house is a family product in the mid to high hundreds and up, not a $400 overwater deal.", "$350-1,000+", "Rasdhoo Atoll, Maldives"),
    ],
    itinerary=[
        day(1, "Boat or plane, then the beach", "The transfer chooses the day. Eat, sleep, swim once.", "Bandos: a short speedboat, sometimes the same evening as a late flight. Kandima: a daylight seaplane, so land in Malé early. Kuramathi: pick the 90-minute boat if you want to avoid the seaplane fare, or the 25-minute flight if you landed in time.", "Check in and ask again what category you received. If you paid entry-room money, you are not in a two-bedroom water villa. Put the bags down accordingly.", "Dinner on the island. A drink package is either worth it or a waste; decide before you are thirsty, because there is no off-island bar.", "If the flight arrives after the last seaplane, book a Malé airport hotel before you leave home. The resort cannot invent daylight.", "Malé"),
        day(2, "House reef", "The reef is why you accepted a small island.", "Morning snorkel with the resort guide. Bandos, Kandima, and Kuramathi all have house reefs. The wind decides which side is calm.", "Lunch, a long sit, a second swim at your own pace. A two-bedroom group can take turns.", "Dinner. If you are in an entry room, enjoy it without spending the evening calculating the villa you did not book.", "Life jackets for weaker swimmers. The drop-off is the attraction and the risk.", "Maldives"),
        day(3, "One short boat, or none", "A sandbank or a nearby reef, run by the resort, back by lunch. No island-hopping tour.", "The excursion if it is under four hours. With children or a nervous snorkeler, trade it for another morning on the house reef and a booked hour in a pool.", "Afternoon on the beach. Kuramathi's island is large enough to bike. Bandos is small enough to walk. Kandima is a big resort with a lot of guests; pick a quiet stretch.", "Dinner. The buffet is the sensible meal; one à la carte night is the treat.", "Dolphins are a bonus, not a guarantee. Anyone promising a whale shark on a clock is selling a boat ride."),
        day(4, "Reef, then back to Malé", "Same transfer rules in reverse.", "Early snorkel if the boat or plane is later. Bandos can leave closer to your flight. Seaplane resorts need the morning departure.", "Cross to the airport with a gap before the international flight. A 90-minute Kuramathi speedboat plus a delay is how connections die.", "Eat at the resort or the airport. There is no honest street-food stop in between unless you built a Malé night on purpose.", "The two-bedroom under $400 was the search. The trip you had is a beach resort. Those can both be true."),
    ],
    attractions=[
        sight("Bandos house reef", "A close-in reef on a short-transfer island. The best use of a mid-range Maldives rate.", "Go at the tide the dive shop names, not at a random noon."),
        sight("Kandima's beaches", "A big island with room to walk away from the main pool.", "The sky studios are inland-feeling compared with a beach villa. Walk to the water on purpose."),
        sight("Kuramathi", "One of the older resort islands, large enough that a bike is useful, with a long house reef.", "Choose the boat or the plane before you choose the excursion."),
        sight("A resort sandbank", "The picnic that replaces a fake 'island hopping' day.", "Book it through the resort and keep it short."),
        sight("Malé", "Useful only as an emergency night before a daylight seaplane.", "An airport hotel is the right booking, not a guesthouse adventure with a 6 a.m. boat.", "Malé"),
        sight("Rasdhoo Atoll water", "The sea around Kuramathi, which is the view you came for if you skipped the water villa.", "Snorkel the house reef before you pay for a boat.", "Maldives"),
    ],
    scenic_routes=[
        route("Speedboat to Bandos", "About 10 to 20 minutes from the airport jetty. The least fragile transfer on this page, and the one that can work after a late landing.", "Under half an hour"),
        route("Seaplane to Kandima", "About 40 minutes to Dhaalu Atoll, daylight only, a fare on top of the room.", "Most of the arrival day"),
        route("Kuramathi, two ways", "Seaplane about 25 minutes, or a shared speedboat about 90 minutes. The boat is cheaper and longer. The plane stops in the afternoon.", "25 minutes, or an hour and a half"),
    ],
    transport="Resort boats and seaplanes only. Bandos is the transfer you barely notice. Kandima is a seaplane commitment. Kuramathi lets you trade money for time. None of the three is a place you leave for dinner. Build a two-hour cushion before an international flight on the way home, more if you chose the 90-minute boat.",
    food=[
        dish("Mas huni and roshi", "Resort breakfast", "Tuna and coconut with flatbread. The local plate on a buffet that is otherwise international."),
        dish("Grilled fish", "The main restaurant", "The sensible dinner. Ask which fish is being caught locally this week."),
        dish("Buffet dinner", "Included if you bought half-board or all-inclusive", "On a mid-range island this is the meal that keeps the budget from breaking. À la carte every night will not."),
        dish("A packed reef snack", "The dive shop or the excursion boat", "Take the fruit and water. You will be hungry when you get out of the sea, and the next restaurant is back at the jetty."),
    ],
    tips=[
        "Do not pay a deposit on a 'two-bedroom water villa' at $350. Ask which building, which atoll, and what the transfer costs.",
        "An entry beach room under $400 in the green season is possible. A two-bedroom usually is not, once taxes and both transfers are in.",
        "Kandima's cheapest published two-bedroom is a sky suite around the low $400s before tax, in a cheap month. That is the honest floor.",
        "If the group needs two bedrooms more than it needs the Maldives, a Bali villa hits the number. If the group needs the reef, book the beach room and split it only if the hotel allows the occupancy.",
    ],
    faqs=[
        faq("Can I get a two-bedroom overwater villa under $400?", "No, not as a plan you should believe. The mid-range islands here sometimes sell beach rooms and, on sale, a two-bedroom sky suite or beach room near or above $400 before tax and transfers. The water villa is a different price."),
        faq("What is the real range?", "Entry rooms at Bandos, Kandima, and Kuramathi often run roughly $250-600 depending on month and meal plan. Two-bedroom houses and pool villas commonly run $500 to well over $1,000, and a pool villa at a family island can reach several thousand on a full-board night."),
        faq("Which transfer should we pick?", "Bandos if you want a short speedboat. Kandima if you accept a 40-minute seaplane. Kuramathi if you want a choice between a 25-minute seaplane and a 90-minute boat. Late arrivals and seaplanes do not mix."),
        faq("Are meals included?", "Sometimes. A room-only rate looks closer to $400 and then fails at dinner, because you cannot leave. Compare half-board totals, not headline room rates."),
    ],
    map_places=[
        stop("Bandos", "North Malé Atoll", "Maldives"),
        stop("Kandima", "Dhaalu Atoll", "Maldives"),
        stop("Kuramathi", "Rasdhoo Atoll", "Maldives"),
        stop("Malé", "Malé", "Maldives", "Malé"),
        stop("Velana International Airport", "Malé", "Maldives"),
    ],
    budget_notes="Plan on $250-600 for a beach room in the green season and more in the dry season. A two-bedroom is usually above $400 before you add tax, the green tax, and a transfer that can cost more than a night in the room. All-inclusive at these resorts can be the cheaper way to eat and the faster way to blow past $400. The search term and the real invoice are different documents.",
))

add(trip(
    slug="maldives-family-friendly-with-kitchen",
    title="A family island in the Maldives, with a short boat and almost no kitchen",
    location="Malé, Maldives",
    summary=(
        "Four nights at a resort that actually runs a kids' club, on an island with a house reef, reached "
        "by speedboat if you choose Kuda Huraa or Meeru. Kitchens barely exist. A minibar is not a kitchen, "
        "and a family villa kitchenette is something you confirm for that villa rather than assume. "
        "Kuramathi can take 90 minutes by boat or 25 by seaplane, which is a long first day with a toddler. "
        "The useful family trip is the short boat, the reef, and an early bedtime."
    ),
    who="Parents with children roughly four and up, who want a kids' club and a reef and can accept eating every meal at the resort.",
    best_time="December to April for calmer seas and a kinder house reef. Avoid promising toddlers a long crossing in rough weather. Seaplane resorts still require a daylight landing.",
    nights=4,
    hook="4 nights · Kids' club and house reef · Kitchen mostly unmet",
    constraints=["Family", "Kitchen is rare; confirm a kitchenette or eat at the resort", "Name the transfer time"],
    lodging="$400-2,500+",
    daily="$600-2,800+",
    neighborhoods=[
        stay_area("North Malé Atoll", "Four Seasons Kuda Huraa is a speedboat of about half an hour. Meeru is a speedboat of about 55 minutes. Both are more sensible with children than a seaplane connection on the same day as a long-haul flight."),
        stay_area("Rasdhoo Atoll", "Kuramathi is the big, long-running family island. The 90-minute shared speedboat is the tiring option; the seaplane is shorter and stops in the afternoon."),
    ],
    hotels=[
        hotel("Four Seasons Resort Maldives at Kuda Huraa", "North Malé Atoll", "A speedboat of about 30 minutes from the airport. Family villas exist, and some categories have a private pool. A kitchenette is not a standard feature; ask whether the specific family villa has one, and expect a minibar if the answer is vague. The kids' club is real, and the rate is a luxury rate, often $1,000 to $2,500 and well beyond for a family villa.", "$1,000-3,000+", "North Malé Atoll, Maldives", "https://www.fourseasons.com/maldives/"),
        hotel("Meeru Maldives Resort Island", "North Malé Atoll", "A large family island about 55 minutes by speedboat. Kids, a wide reef, and a lot of room categories. An ordinary room does not have a kitchen. A two-bedroom beach pool villa is a high, meal-plan price, not an apartment. This is the practical mid-to-upper family resort on a boat you can explain to a tired child.", "$300-1,200", "North Malé Atoll, Maldives"),
        hotel("Kuramathi Maldives", "Rasdhoo Atoll", "A classic family island with two-bedroom beach houses and a kids' club. No guest kitchen in a normal room. Choose the 25-minute seaplane or the 90-minute speedboat on purpose. The long boat plus a toddler plus a late arrival is the combination to avoid. If you miss the seaplane, you are overnighting in Malé.", "$350-1,000+", "Rasdhoo Atoll, Maldives"),
    ],
    itinerary=[
        day(1, "The boat, then nothing else", "Children get one transfer. They do not get a welcome excursion.", "Kuda Huraa is the short, expensive boat. Meeru is about 55 minutes. Kuramathi is the one you only choose in daylight, and you pack snacks and a change of clothes for the 90-minute boat.", "Arrive, find the kids' club hours, and swim in the lagoon in front of the room if the resort says it is calm. Skip the house reef until the morning.", "Early dinner, the children's menu or the plain end of the buffet, bed. The resort is the whole town.", "A kitchenette you were promised and did not receive should be raised on night one, while they can still move you.", "Malé"),
        day(2, "Kids' club and the house reef", "The shape of a good family day here.", "Reef snorkel for anyone old enough, with life jackets, on the resort's time. Smaller children stay on the sand with a parent or at the club if the age rule allows. Clubs often start around age four; ask.", "Lunch. Pool or lagoon. A nap. The afternoon is not a second boat.", "Dinner early. Trade a sunset cruise for a bedtime. You can watch the sunset from the beach in front of dinner.", "Write the club's age cutoff and hours on the first morning. 'Kids' club' sometimes means two hours, not all day."),
        day(3, "A short boat only if the ages work", "Toddlers do not do a long snorkel safari. Older children might.", "If everyone swims, book the resort's shortest guided snorkel, under a couple of hours, and be back for lunch. If anyone is little, repeat day two: reef in front of the beach, club, pool.", "Afternoon in the room. This is when a kitchenette would matter, and when a minibar does not. Order fruit and sandwiches from room service instead of pretending to cook.", "One nicer family dinner if the resort has an early seating. Otherwise the buffet, again, without apology.", "Do not schedule Hanifaru Bay. These hotels are not in Baa, and the ride is the opposite of a toddler day.", "Maldives"),
        day(4, "Breakfast and the boat back", "Same transfer you survived on the way in, with wet swimsuits in a separate bag.", "Breakfast, a last paddle, bags packed before the children scatter.", "Leave on the resort's instruction. A 55- or 90-minute boat needs a longer gap before the flight than Kuda Huraa's half hour.", "Airport snacks. The meal plan ends at the jetty.", "Thank the club staff by name. On a small island that is the whole childcare system."),
    ],
    attractions=[
        sight("House reef", "The daily snorkel. Meeru and Kuramathi are known for wide reefs; Kuda Huraa's reef is part of a polished resort rather than a wilderness.", "First swim with the guide. Life jackets for children."),
        sight("The kids' club", "The other half of the resort. Age rules differ, and teenagers are not the same booking as four-year-olds.", "Ask what happens in the rain. A plastic slide is not a program."),
        sight("Kuda Huraa lagoon", "A close North Malé island, which is the luxury version of 'easy with children.'", "The family villa is the category. A garden room with a minibar is not a kitchen stay."),
        sight("Meeru's beaches", "Room to walk, a long sand edge, and enough space that the island does not feel like a single pool deck.", "Rent the bike if the room is far from dinner."),
        sight("Kuramathi", "The old-style large island: several clusters of rooms, a reef, and a bike path.", "Only if the transfer length is acceptable in writing.", "Maldives"),
        sight("Malé, as a buffer night", "The honest backup when a seaplane day fails.", "Book the airport hotel in advance if your inbound flight is late and you chose Kuramathi.", "Malé"),
    ],
    scenic_routes=[
        route("Speedboat to Kuda Huraa", "About 30 minutes from the airport. The best transfer on this page with young children. It costs resort money, and it does not depend on a seaplane.", "Half an hour"),
        route("Speedboat to Meeru", "About 55 minutes. Long enough for snacks and a toilet plan, short enough to do on arrival day.", "About an hour"),
        route("Kuramathi boat or plane", "Ninety minutes by shared speedboat, or about 25 minutes by seaplane in daylight. Pick one before you buy the flights.", "25 minutes, or an hour and a half"),
    ],
    transport="Resort speedboats, or a seaplane only if you chose Kuramathi and a daylight landing. Do not plan a domestic-flight adventure with children on a four-night trip. Buggies and bikes matter on Meeru and Kuramathi because dinner can be a long walk in the dark. Kuda Huraa is smaller and more managed. There is no hop to another resort for a meal.",
    food=[
        dish("Children's buffet", "The main restaurant", "Plain pasta, rice, fruit, and grilled fish exist on every one of these islands. Look at the buffet before you order a special meal."),
        dish("Mas huni", "Breakfast", "A mild plate of tuna and coconut for any child who eats fish. Chili on the side."),
        dish("Room-service sandwiches", "The villa or room, day three afternoon", "The substitute for the kitchen you do not have. Order before the club ends, when everyone is hungry at once."),
        dish("One booked family dinner", "Kuda Huraa, if you are there, or the best à la carte room on Meeru or Kuramathi", "One night that feels like a holiday for the adults, at an early time. The other nights are the buffet, on purpose."),
    ],
    tips=[
        "Say the transfer time out loud before you book: 30 minutes, 55 minutes, or 90. Toddlers feel all three differently.",
        "Ask 'kitchenette or minibar?' and wait for a noun. A family villa can still be a minibar and a kettle.",
        "Kids' clubs have age floors. Under-fours are usually your job, on the beach, in a life jacket.",
        "A two-bedroom with a private pool at these resorts is a luxury booking. Meeru has published pool-villa rates in the thousands on a meal plan. Do not budget it as an apartment.",
    ],
    faqs=[
        faq("Is there a kitchen?", "Usually no. Four Seasons family villas sometimes include more than a minibar; confirm the exact villa. Meeru and Kuramathi rooms are hotel rooms. Plan to eat at the resort, and use room service for the messy afternoon snack."),
        faq("Which transfer is fair to a toddler?", "Kuda Huraa's half-hour speedboat, then Meeru's 55 minutes. Kuramathi's 90-minute boat is the one to avoid if anyone gets carsick, and its seaplane requires a daylight landing in Malé."),
        faq("Is a kids' club all day?", "No. Get the hours and the ages on day one. Parents still own the early morning, the late afternoon, and every meal the club does not cover."),
        faq("Can we do a long snorkel trip?", "Only with children who already snorkel, and only on the resort's short boat. A full-day safari is the wrong third day. The house reef is the trip."),
    ],
    map_places=[
        stop("Four Seasons Kuda Huraa", "North Malé Atoll", "Maldives"),
        stop("Meeru", "North Malé Atoll", "Maldives"),
        stop("Kuramathi", "Rasdhoo Atoll", "Maldives"),
        stop("Malé", "Malé", "Maldives", "Malé"),
        stop("Velana International Airport", "Malé", "Maldives"),
    ],
    budget_notes="Kuda Huraa is a luxury rate, often $1,000-3,000 a night for a family villa before the boat. Meeru and Kuramathi can start a few hundred dollars for an entry room and climb fast for a two-bedroom or a pool villa on full board. Food is a meal plan, not a grocery run. Add the boat or seaplane per person, including children over two. The kitchen you do not have is the reason half-board matters.",
))

add(trip(
    slug="maldives-pet-friendly",
    title="A short-boat Maldives week, with the dog left at home",
    location="Malé, Maldives",
    summary=(
        "Four nights on a classic resort island a short speedboat from Malé. Importing a dog into the "
        "Maldives is prohibited. No resort on this page accepts a guest's dog, and this list is not a "
        "set of pet-friendly villas. Leave the dog at home. Kurumba, Baros, and Taj Exotica are ordinary "
        "famous islands with house reefs, reached by boat in well under an hour, which makes a four-night "
        "trip actually usable. The pet constraint is unmet."
    ),
    who="Anyone who searched for a pet-friendly Maldives and needs the policy before the fantasy.",
    best_time="January to April for weather. The pet rule does not have a season. It is the law, every month.",
    nights=4,
    hook="4 nights · Leave the dog at home · Speedboat under an hour",
    constraints=["Dogs prohibited", "Leave the dog at home", "Pet-friendly villas are not a category here"],
    lodging="$400-1,500",
    daily="$550-1,800",
    neighborhoods=[
        stay_area("North Malé Atoll", "Kurumba and Baros. The first resort in the country and a small luxury island, both a short speedboat from the airport. You can arrive in the evening."),
        stay_area("South Malé Atoll", "Taj Exotica, on Emboodhoo, also a short speedboat. Same rule about animals. A lagoon hotel, not a kennel with a beach."),
    ],
    hotels=[
        hotel("Kurumba Maldives", "North Malé Atoll", "Opened in 1972 as the first resort in the Maldives, about 15 minutes by speedboat from the airport. House reef, beach, and restaurants. Dogs are not accepted. The short boat is why it is the right island for a brief trip, not because anyone can bring a pet.", "$350-900", "North Malé Atoll, Maldives"),
        hotel("Baros Maldives", "North Malé Atoll", "A small luxury island about 20 to 25 minutes by speedboat, long-running and quiet. Villas, a house reef, no dog policy that a guest can use. Book it as a no-pet resort and enjoy how small the island is.", "$500-1,400", "North Malé Atoll, Maldives"),
        hotel("Taj Exotica Resort & Spa, Maldives", "Emboodhoo, South Malé Atoll", "A speedboat of about 15 to 20 minutes to a long, thin island with a proper spa and a house reef. The Taj name does not create a pet exception. Leave the dog at home and take the short boat.", "$450-1,200", "South Malé Atoll, Maldives"),
    ],
    itinerary=[
        day(1, "A short boat and a reef view", "Because the crossing is under half an hour, arrival day can still include a swim.", "Clear the airport and board the resort boat. Fifteen to twenty-five minutes is the range. There is no seaplane on this itinerary.", "Check in, walk the island once. It will not take long. Snorkel only if the desk says the visibility is fine and you are awake enough.", "Dinner at the resort. You will do that every night. Choose the meal plan accordingly.", "Do not ask the boat handlers if the dog can come on the next trip. The answer is no at the border, not at the jetty.", "Malé"),
        day(2, "House reef, properly", "The whole point of picking a near island is that you are rested enough to use the reef.", "Morning snorkel with the guide. Kurumba, Baros, and Taj Exotica all sit on reefs. Let the guide pick the entry.", "Lunch, a book, a second swim later. A spa appointment if the island is Taj Exotica and you booked it.", "Dinner. Walk the beach after, which on Baros is a very short loop and on Kurumba a slightly longer one.", "Rinse the gear. Salt ruins a mask by day four if you do not.", "Maldives"),
        day(3, "Sandbank or a longer snorkel", "One planned outing, still home for lunch or just after.", "The resort's short boat. A sandbank picnic is the right shape. A 'find whale sharks' promise is not a plan.", "Back on the island for the hot hours. Sleep. Repeat the house reef at 4:00 if you liked the morning.", "A better bottle of wine or a set menu, since you cannot go into Malé for a change of scene without giving up the evening.", "Malé is 20 minutes away and still the wrong dinner plan. The boat schedule will not match a restaurant reservation."),
        day(4, "Swim, boat, flight", "The short transfer makes a late morning possible. Use it.", "Breakfast and a last snorkel.", "Boat to the airport with the gap the resort recommends. Even a 20-minute crossing deserves an hour of slack.", "Eat before you leave the island if the flight is long. The airport is fine and unremarkable.", "The dog is at home. That is the successful version of this search."),
    ],
    attractions=[
        sight("Kurumba house reef", "A reef you can be on within an hour of landing, which is rare in this country.", "Use the guide's entry point. The easy boat is not an easy current."),
        sight("Baros", "A small island you can understand in one walk. The luxury is the lack of a crowd.", "Circumnavigate it once in the evening.", "Maldives"),
        sight("Taj Exotica lagoon", "A long sand spit and a spa day if you want one unstructured afternoon.", "Book the spa before you fly. Walk-ins disappoint."),
        sight("A sandbank picnic", "The one off-island hour that suits a four-night, short-boat trip.", "Take the resort boat. A private charter doubles the cost for the same sand."),
        sight("Malé", "The capital across a short stretch of water, which you will see from the boat and do not need to tour.", "A city walk only if a flight delay gives you half a day on the way home.", "Malé"),
        sight("The arrival boat", "Twenty minutes over the atoll is the scenery other trips spend a seaplane fare to get.", "Sit outside if the spray allows. The photos are on the way in, when you are still curious."),
    ],
    scenic_routes=[
        route("Speedboat to Kurumba", "About 15 minutes from Velana. The shortest famous crossing in the country.", "A quarter of an hour"),
        route("Speedboat to Baros", "About 20 to 25 minutes. Still an evening-friendly arrival.", "Under half an hour"),
        route("Speedboat to Taj Exotica", "About 15 to 20 minutes to South Malé Atoll. Same planning rules, opposite side of the airport.", "Under half an hour"),
    ],
    transport="Speedboats only. No seaplane, which is the advantage: you can land late and still sleep on the island. There is no car, no street, and no inter-island dinner. The airport boat on the last day is the only timetable that matters. Give it a cushion even though the ride is short.",
    food=[
        dish("Mas huni", "Breakfast buffet", "Tuna, coconut, onion, and chili. Eat it once even if the rest of breakfast is familiar."),
        dish("Grilled fish", "The main restaurant", "The standing dinner. Ask for the catch and skip endangered reef species if a menu is careless."),
        dish("A set menu, one night", "Baros or Taj Exotica", "The small-island version of a fancy night. Reserve it. Kurumba has more restaurants if your group disagrees."),
        dish("Reef-trip fruit and water", "The picnic boat", "You will want both the minute you are back on the sand. Do not count on a snack shack on a sandbank."),
    ],
    tips=[
        "Leave the dog at home. Importing dogs into the Maldives is prohibited. A resort cannot waive that.",
        "Do not search for a pet-friendly water villa. That category is a misunderstanding of the law.",
        "Pick these islands because the boat is short. A four-night trip dies on a daylight-only seaplane.",
        "Buy the meal plan with your eyes open. You cannot walk out to a cheaper dinner.",
    ],
    faqs=[
        faq("Can any Maldives resort take my dog?", "No. Leave the dog at home. Importing a dog is prohibited, and this page does not list pet-friendly villas. Kurumba, Baros, and Taj Exotica are normal resorts."),
        faq("What if the dog is small, or a service animal?", "Do not plan on an exception from a blog or a front desk. The import ban is the constraint. Sort any service-animal question with the Maldives authorities and the airline before you consider a booking, and assume a holiday stay is not possible."),
        faq("Why these three hotels?", "They are famous, they are a short speedboat from Malé, and they have reefs worth four nights. They are not a workaround for the pet rule."),
        faq("Is the trip worth it without the dog?", "Yes, if you wanted the water. A near-Malé island gives you a reef on night one. That is a better holiday than a seaplane connection with an animal you were never going to be allowed to land."),
    ],
    map_places=[
        stop("Kurumba Maldives", "North Malé Atoll", "Maldives"),
        stop("Baros Maldives", "North Malé Atoll", "Maldives"),
        stop("Taj Exotica Maldives", "South Malé Atoll", "Maldives"),
        stop("Malé", "Malé", "Maldives", "Malé"),
        stop("Velana International Airport", "Malé", "Maldives"),
    ],
    budget_notes="Rooms often run $400-1,500 a night depending on the island and the month, plus a short boat that is cheaper than a seaplane and still not free, plus taxes and the green tax. Food is the meal plan. There is no pet fee to budget, because the dog is not coming. A sitter at home is the real pet line on this invoice.",
))

add(trip(
    slug="phuket-budget-under-200night",
    title="Patong or Kata for under $200 a night",
    location="Phuket, Thailand",
    summary=(
        "Four nights on the west coast of Phuket in a real hotel under $200 a night, which is an easy rate "
        "outside Christmas and New Year. The Kee sits in Patong, Orchidacea is on the Kata hillside with a "
        "beach shuttle, and Katathani is the beachfront Kata resort whose classic rooms fit this cap from "
        "about May through October. A beachfront at Katathani in January often does not. Amanpuri is a "
        "different budget entirely."
    ),
    who="Friends or a couple who want a swim and a plate of seafood without a private-pool villa.",
    best_time="May to October for the rate, with more rain and fewer people. November to March is the dry season and the expensive one. Christmas week will not stay under $200 at a beachfront hotel.",
    nights=4,
    hook="4 nights · Patong or Kata · Under $200 off peak",
    constraints=["Under $200 a night", "Beach hotel, not a cape villa", "Christmas week is excluded"],
    lodging="$70-190",
    daily="$120-220",
    neighborhoods=[
        stay_area("Patong", "The town with the beach, the shops, and Bangla Road. Convenient and loud after dark. Ask for a room that does not face the bar street."),
        stay_area("Kata", "A shorter beach south of Patong, with a small town behind it. Orchidacea is on the hill; Katathani is on the sand. The better sleep if you do not need nightlife."),
    ],
    hotels=[
        hotel("The Kee Resort & Spa", "Patong", "A modern Patong hotel, central, with a pool and a spa. Ordinary weeks often land between $80 and $180. It is a town hotel with beach access nearby, not a quiet cove. Request a room away from Bangla Road.", "$80-180", "Patong, Phuket"),
        hotel("Orchidacea Resort", "Khoktanod Road, Kata", "A hillside resort between Kata and Kata Noi, on a site that has taken guests for decades. The beach is a short walk or the hotel shuttle, not a private sand strip. Rooms often sit well under $200, including a lot of the high season. There is a pool and a separate children's pool.", "$70-160", "Kata, Phuket", "https://www.orchidacearesort.com/"),
        hotel("Katathani Phuket Beach Resort", "Kata Beach", "The large beachfront hotel on Kata, with a long pool and a real frontage on the sand. A classic or garden room from May through October is often under $200. A beachfront room in December, January, or Christmas week often is not, so check the category before you count it against the cap.", "$120-280", "Kata, Phuket"),
    ],
    itinerary=[
        day(1, "The beach you slept near", "Patong if you are at The Kee, Kata if you are at the other two. Do not start with a tour.", "Drop bags and swim. Kata Noi, just south of Kata, is the quieter sand if Katathani's beach feels busy. Patong's beach is wide and used; swim between the flags.", "Walk the town long enough to find dinner. In Kata that is a small grid. In Patong it is a long beach road. Buy sunscreen in a pharmacy if you packed none; hotel shops overcharge.", "Seafood with a price-per-kilo board. Eat early. Bangla Road after 10 p.m. is a choice, not a requirement.", "Agree taxi fares before you sit down. The meter is not the local habit.", "Patong Beach"),
        day(2, "The other beach", "If you slept in Patong, spend the day in Kata. If you slept in Kata, you already live there; use Kata Noi and Karon instead of a pointless Patong night.", "Morning swim at Kata Noi. The south end is calmer and the walk from Kata beach is short.", "Lunch in Kata town. A one-hour taxi to Patong only if someone in the group wants to see it, and then come back before dinner.", "Dinner in the town where your bed is. A second seafood grill is allowed. So is a cheap Thai curry shop on the main road.", "The Kata-Karon-Patong road jams from 4 p.m. Do the far beach in the morning.", "Kata Beach"),
        day(3, "Old Town, or a cape view", "One day off the beach towel. Phuket Town is the more interesting choice. A Phi Phi boat is a ten-hour commitment and a rough ride.", "Taxi to Phuket Town by 9:30. Walk Thalang Road, Soi Romanee, and the Sino-Portuguese shophouses. Coffee, a museum if it is open, lunch.", "Promthep Cape for the viewpoint on the way home if the light is good, then Kata or Patong by late afternoon. Skip the cape if the sky has already closed in; it is a sunset place.", "A quiet dinner. You have been in a car. Night three is not the night for a 5 a.m. island boat.", "Phi Phi can be added by deleting this day, not by stacking it on top. The boat is an all-day project.", "Phuket"),
        day(4, "Swim, Wat Chalong if you want it, airport", "The airport is at the north end of the island. Kata to the airport can take 90 minutes.", "Morning swim. Return the rental car if you were unwise enough to hire one for one day.", "Leave after an early lunch for an afternoon flight. Wat Chalong is a reasonable stop only if it is actually on the way and you are not late.", "Eat the seafood lunch, not the airport pad thai, if you can help it.", "A private car to the airport, booked by the hotel, beats a last-minute negotiation with wet hair.", "Wat Chalong"),
    ],
    attractions=[
        sight("Patong Beach", "The long, busy beach with the town behind it. Swim here if you are at The Kee.", "Morning is the decent hour. The beach bars are not the swim.", "Patong Beach"),
        sight("Kata Beach", "A bay you can see the ends of. The better default if the hotel is Orchidacea or Katathani.", "The shuttle from Orchidacea is the point of that booking. Use it.", "Kata Beach"),
        sight("Kata Noi", "The smaller beach just south. Fewer hotels, the same water.", "Walk from Kata in the morning before the sand fills."),
        sight("Phuket Old Town", "Sino-Portuguese streets, a real town, and lunch that is not a beach menu.", "Go in the morning. Sunday evening is the walking street, if your dates include it."),
        sight("Promthep Cape", "The southern viewpoint. Worth twenty minutes on the way back from town.", "Sunset is the crowd. A cloudy afternoon is just a parking lot."),
        sight("Wat Chalong", "The island's best-known temple, inland, with a tall chedi.", "Cover shoulders and knees. It is a working temple, not a set.", "Wat Chalong"),
    ],
    scenic_routes=[
        route("Kata to Kata Noi on foot", "The beach path and the headland between the two bays. The best free hour of the trip.", "About 2 km"),
        route("Taxi to Phuket Old Town", "From Kata or Patong up and across to the old streets, then back via Promthep if the light is good.", "45 to 70 minutes each way"),
        route("Phi Phi by day boat", "A speedboat or ferry that leaves early and returns late. Maya Bay has had visitor limits; check that week. Do this only by giving it the whole day.", "8 to 10 hours, and rough if the sea is up"),
    ],
    transport="Hotel shuttles, agreed taxis, and your feet on the beach. A rental car is extra stress on the coast road for a four-night swim trip. Patong to Kata is 20 to 40 minutes depending on traffic. The airport is far from both; budget 60 to 90 minutes from Kata and a bit less from Patong. Songthaews exist and are confusing for a first visitor with luggage.",
    food=[
        dish("Grilled seafood by the kilo", "A Kata or Patong beach-road restaurant with prices on a board", "Prawns, snapper, rice, a Thai salad. Photograph the price list. The expensive surprise is the prawns."),
        dish("Massaman curry", "A Thai shop away from the beach road", "Potato, peanut, and a mild curry. The reliable dinner when nobody wants to negotiate a fish."),
        dish("Moo hong", "Phuket Town, on the Old Town day", "The local braised pork, dark and sweet, with rice. Order it at a Sino-Portuguese café, not at a beach club."),
        dish("Morning noodle soup", "A shop near the hotel", "Rice noodles, broth, and a cold drink before the beach. Cheaper and better than the hotel breakfast if your rate excludes it."),
    ],
    tips=[
        "Christmas week and the first week of January break the $200 cap at Katathani's beachfront rooms. Orchidacea is the safer hold.",
        "Bangla Road is a block from a lot of Patong hotels. Ask for a quiet room or stay in Kata.",
        "Amanpuri, on a northwestern cape, is not a budget substitute. Do not stretch this search until it becomes that hotel.",
        "Agree every taxi fare first. The phrase to practice is the price, the destination, and a nod before you open the door.",
    ],
    faqs=[
        faq("Will $200 actually get a beach hotel?", "Yes at The Kee and Orchidacea for most of the year, and at Katathani for a classic room in the rainy season. A beachfront Katathani room in high season, and anything decent at Christmas, usually will not."),
        faq("Patong or Kata?", "Kata if you want to sleep. Patong if you want to walk to dinner and do not mind noise. The beaches are 30 minutes apart and the days can mix."),
        faq("Is Phi Phi worth it?", "Once, if you give it the entire day and the forecast is calm. It is a crowded boat, not a hidden bay. Maya Bay's access rules change; check before you pay."),
        faq("Do I need a car?", "No. Taxis and the Orchidacea shuttle cover this itinerary. A car helps only if you already like driving on the left in traffic."),
    ],
    map_places=[
        stop("Patong Beach", "Patong", "Thailand", "Patong Beach"),
        stop("Kata Beach", "Kata", "Thailand", "Kata Beach"),
        stop("Kata Noi", "Kata", "Thailand"),
        stop("Phuket Old Town", "Phuket", "Thailand"),
        stop("Wat Chalong", "Phuket", "Thailand", "Wat Chalong"),
    ],
    budget_notes="Rooms at $70-190 are realistic at The Kee and Orchidacea, and at Katathani outside high season. Food can stay near $20-35 a day on noodles and one seafood dinner, or twice that if every meal is a beach club. Taxis add up: budget $15-30 for a one-way coast hop. A Phi Phi boat is often $80-120 and is the optional splurge, not the daily plan. Christmas week is a different price list.",
))

add(trip(
    slug="phuket-city-center-walkable",
    title="Walkable Phuket Town, with one beach day by taxi",
    location="Phuket, Thailand",
    summary=(
        "Three nights in Phuket Old Town, in the Sino-Portuguese streets, not in Patong. The Memory at On On "
        "Hotel has stood on Phang Nga Road since 1927, Casa Blanca is a small restored house on Phuket Road, "
        "and Sino House is another heritage-street hotel in the same grid. Sunday evening is the walking "
        "street. The beach is a taxi to Kata, about 45 minutes, and then you come back to town for dinner."
    ),
    who="A couple or a friend who would rather walk to dinner than sleep above a beach bar.",
    best_time="November to April if you want a dry beach day. The town walk works in the rain too. Sunday is the night the streets fill, so arrive by Sunday if you can choose.",
    nights=3,
    hook="3 nights · Old Town on foot · One taxi to Kata",
    constraints=["Walkable town center", "Phuket Town, not Patong", "No car"],
    lodging="$70-160",
    daily="$120-200",
    neighborhoods=[
        stay_area("Phuket Old Town", "Thalang, Phang Nga, and Phuket Roads. Shophouses, cafés, a Sunday walking street, and hotels you can leave on foot. This is the city center the search asked for."),
        stay_area("Kata, as a day", "The beach. A pre-agreed taxi, a swim, and a return before dinner. Sleeping there is the other Phuket page."),
    ],
    hotels=[
        hotel("The Memory at On On Hotel", "Phang Nga Road, Old Town", "The island's oldest hotel, built in 1927 and later a location in The Beach. Restored Sino-Portuguese rooms, a courtyard, no pool, and the Sunday walking street at the front door. Rooms are often $70-150. Street noise on weekend nights is the trade for being in the middle.", "$70-150", "Phuket Town", "https://www.thememoryhotel.com/en/"),
        hotel("Casa Blanca Boutique Hotel", "Phuket Road, Old Town", "A small restored shophouse, about 17 rooms, with a modest pool. You can walk to Soi Romanee and the Sunday market. Street-facing rooms hear the bar opposite; ask for the courtyard if you sleep lightly. Often under $120.", "$60-140", "Phuket Town"),
        hotel("Sino House Phuket Hotel", "Old Town", "A heritage-street hotel in the same walkable grid, smaller and quieter than a beach resort. Use it as a town base: Thalang Road for food, the weekend market when it is on, and a taxi to the sea. Confirm the room is on an upper floor if the ground floor faces a café.", "$70-150", "Phuket Town"),
    ],
    itinerary=[
        day(1, "The streets, then dinner", "Arrive and stay in the grid. The beach can wait.", "Check in and walk Phang Nga Road, Thalang Road, and Soi Romanee. The architecture is the sight: tiled floors, five-foot ways, and shophouses still in use.", "Thai Hua Museum if it is open, then a coffee and a slow loop until you can find the hotel without a map.", "Dinner within a ten-minute walk. Moo hong or a seafood dish in a room with a fan, not a show. If you landed on a Sunday, the walking street is the evening.", "The Memory has no pool. Casa Blanca's pool is a dip, not a day. Plan the swim for tomorrow.", "Phuket"),
        day(2, "Taxi to Kata, back for dinner", "One beach day, booked as a there-and-back, not a move.", "Leave by 9:00. Agree a round-trip price or use a ride-hailing car. Swim at Kata or Kata Noi. Rent a chair only if you need shade; the trees and a shirt will do for two hours.", "Lunch in Kata town, one more swim, and the car back by 3:30 so you are in Old Town before the coast road and the town streets both slow down.", "Dinner on Thalang Road. You are a town guest who went swimming, which is the right shape for this search.", "Do not check out and 'just see' Patong at sunset. You will lose the walk home.", "Kata Beach"),
        day(3, "A last loop, then the airport", "The morning is still a walk. The airport is an hour north in ordinary traffic.", "Coffee and the streets you liked, in the light. Buy snacks. The standard market mornings are useful if one falls on your date; the Sunday night market will already have happened or not.", "Leave after lunch for an afternoon flight. Add time on a Friday. There is no beach on the way that is worth missing the plane.", "Eat a real lunch in town. The airport is a food court.", "A hotel car is the calm exit. Haggling with luggage on Phang Nga Road is not.", "Phuket"),
    ],
    attractions=[
        sight("Phuket Old Town", "The Sino-Portuguese center. Walk it without a list and you will still have a good day.", "Sunday evening is the walking street. Other days the buildings are easier to see.", "Phuket"),
        sight("Soi Romanee", "A short lane of restored shophouses and cafés. The postcard street.", "Go once in the morning and once after dark. They are different streets."),
        sight("Thai Hua Museum", "The Chinese-school building that explains the town's tin and trade history.", "An hour, then back outside. The streets are the larger exhibit."),
        sight("Kata Beach", "The swim. A taxi from the hotel, a public beach, and a return the same day.", "Kata Noi if you want fewer people and do not mind a slightly longer drop-off.", "Kata Beach"),
        sight("Promthep Cape", "The southern headland, possible on the way back from Kata if the driver agrees.", "Ten minutes at the viewpoint is enough. The stalls are optional."),
        sight("Wat Chalong", "The large temple inland, if you want one religious building before the airport.", "It is not in the old town. Do it as a stop with a driver, not as a walk.", "Wat Chalong"),
    ],
    scenic_routes=[
        route("Old Town loop", "Phang Nga Road to Thalang to Soi Romanee to Phuket Road and back. Shophouses the whole way.", "About 2 km, and you will walk it three times"),
        route("Taxi to Kata and back", "Old Town to Kata Beach for a swim and lunch, then the same road home in the early afternoon.", "About 45 to 70 minutes each way"),
        route("Sunday walking street", "The Lard Yai stalls along the old streets, usually Sunday evening. Eat as you walk.", "An hour, or the whole evening"),
    ],
    transport="Walk in town. A taxi or ride-hailing car for Kata, the airport, and Wat Chalong. You do not need a car, and a car in these streets is a burden. The airport transfer is the one booking to make in advance. Patong is not on the way to anything in this itinerary.",
    food=[
        dish("Moo hong", "A Thalang Road or Dibuk Road shop", "Phuket braised pork. The town dish. Eat it with rice, not as a tasting flight."),
        dish("O-tao", "An Old Town street stall or a simple shop", "A crisp mussel omelette. Snack, not dinner, unless you order a second."),
        dish("Kopitiam toast and coffee", "A Sino-Portuguese café on the morning loop", "Thick toast, butter, and strong coffee. Breakfast before the heat."),
        dish("Seafood lunch in Kata", "A board-price restaurant off the sand", "The one beach meal. Check the prawn price. Dinner happens back in town."),
    ],
    tips=[
        "Stay in the old grid. A hotel 'near Phuket Town' on the bypass is a different trip and you will not walk anywhere.",
        "The Memory has no pool. If a pool is essential, Casa Blanca's is small and real; the sea is the Kata day.",
        "Sunday night is loud and wonderful. Light sleepers should ask for a back room or visit Sunday as a day-trip from a quieter date.",
        "The beach day is one day. Two beach days means you wanted the Kata page.",
    ],
    faqs=[
        faq("Is Phuket Town actually walkable?", "The old center is. Thalang, Phang Nga, Soi Romanee, and the restaurants are a few minutes apart. The beaches, the airport, and Wat Chalong are not."),
        faq("Can I see a beach?", "Yes. Kata is a taxi of about 45 to 70 minutes. Swim and come back. Patong is the noisier alternative and not an improvement for this itinerary."),
        faq("Which night is the market?", "The big Old Town walking street is Sunday evening. If you are there on another night the streets are still the sight; they are just quieter."),
        faq("Are these hotels beach resorts?", "No. They are town hotels in old buildings. That is the category that makes the center walkable. The sand is a day trip."),
    ],
    map_places=[
        stop("The Memory at On On Hotel", "Phuket", "Thailand"),
        stop("Thalang Road", "Phuket", "Thailand"),
        stop("Soi Romanee", "Phuket", "Thailand"),
        stop("Kata Beach", "Kata", "Thailand", "Kata Beach"),
        stop("Wat Chalong", "Phuket", "Thailand", "Wat Chalong"),
    ],
    budget_notes="Old Town rooms often run $70-160, which is the easy part. Food stays near $15-30 a day if lunch is a shop and dinner is moo hong. The Kata taxi is the extra, often $25-40 round trip if you agree it first. There is no resort fee and no beach club minimum. The Sunday stalls will still take cash for snacks.",
))

add(trip(
    slug="tulum-with-private-pool",
    title="A Tulum suite with a plunge pool, on a road with no addresses",
    location="Tulum, Mexico",
    summary=(
        "Four nights on Tulum's beach road, where the hotels people mean by a private pool are Be Tulum, "
        "a ground-floor room at Mi Amor, and a plunge-pool suite at Nômade. Be Tulum sells its suites with "
        "private plunge pools; confirm the suite. At Mi Amor the plunge pools are on the ground floor, and "
        "the upstairs rooms have balconies instead. Nômade has plunge pools on many suites and a social "
        "beach club, so it is the least quiet of the three. The road is unmarked, rutted, and slow. There "
        "are no street addresses a driver can trust. Azulik is famous and is not the private-pool promise."
    ),
    who="A couple who want a plunge pool and can tolerate a buggy ride, cash, and a soft schedule.",
    best_time="November to April, outside the Christmas and New Year weeks, when the sea is clearer and the sargassum is usually lighter. Summer seaweed can erase the beach; the pool is what you still have.",
    nights=4,
    hook="4 nights · Plunge-pool suite · Beach road, no addresses",
    constraints=["Private plunge pool", "Beach road, not the town", "Confirm the room category"],
    lodging="$350-900",
    daily="$450-1,000",
    neighborhoods=[
        stay_area("Tulum beach road", "The hotel zone on the Boca Paila road. Kilometer markers, not street numbers. Buggies, potholes, and a 20-minute crawl that looks like five on a map."),
        stay_area("Tulum pueblo", "The town inland, where dinner and tacos cost less and the ruins road begins. You sleep on the beach and eat here once."),
    ],
    hotels=[
        hotel("Be Tulum", "Beach road, hotel zone", "Suites on the beach and in the jungle, sold with private plunge pools. It is adults-oriented. The hotel is on the beach road, so your confirmation is a kilometer marker and a WhatsApp pin, not a street address. Rates often run $400-900. Confirm the suite has a plunge pool rather than only a shared infinity pool.", "$400-900", "Tulum, Mexico"),
        hotel("Mi Amor", "Beach road, rocky point", "A small hotel on a rock over the water. Ground-floor rooms have plunge pools; upper rooms have balconies and do not. Book the ground floor in writing if the pool is the reason for the stay. The shared infinity pool is real and is not the same thing.", "$350-800", "Tulum, Mexico"),
        hotel("Nômade Tulum", "Beach road", "Many of the suites have a private plunge pool, and the beach club is a social place with music. Book a plunge-pool suite by name. This is the wrong hotel if you wanted silence. It is the right one if you wanted the pool and do not mind other people at dinner.", "$300-700", "Tulum, Mexico"),
    ],
    itinerary=[
        day(1, "The road, then the pool", "Getting there is the work. The pool is the reward. Do not plan a ruin at 4 p.m.", "Land at Cancún or Tulum airport. The Cancún airport is the common one and then a two-hour car. Tulum airport is closer and has fewer flights. Either way, the last kilometers on the beach road are slow.", "Check the room against the booking before the driver leaves. Ground floor at Mi Amor. A named plunge-pool suite at Be Tulum or Nômade. Swim in it.", "Dinner at the hotel. You will not want another buggy ride. The restaurant prices are part of sleeping on this road.", "Save the hotel's location pin offline. Cell service drops, and 'the white arch' is not a direction."),
        day(2, "Ruins at opening, pool after", "The archaeological site opens in the morning and closes mid-afternoon. Go first.", "Be at the ruins when they open. The cliff and the sea are the view. Two hours is enough. The site is north of the hotel zone; your buggy or taxi has to come back down the same bad road.", "Lunch in town if you are already inland, then the plunge pool for the hot hours. A beach swim only if the sargassum is light. In summer it often is not.", "Dinner in the pueblo if you can face the ride: tacos, a walk, an early return. Otherwise the hotel again.", "Bring cash for the ruins and for tips. Cards fail in more places than the hotels admit."),
        day(3, "A cenote, then nothing", "One freshwater swim. Not three.", "Gran Cenote or a quieter cenote your hotel actually knows. Go at opening. Many ban ordinary sunscreen; follow the sign at the stairs.", "Back by lunch. The afternoon is the plunge pool and a book. This is the day the room earns the rate.", "A long dinner at the hotel. Nômade will be the liveliest. Be Tulum and Mi Amor are the quieter tables.", "Do not add a Sian Ka'an boat today. That is a full, rough day and it deletes the pool.", "Cobá"),
        day(4, "Pool, then the long road out", "Leaving is another slow hour before the highway even starts.", "Sunrise swim in the plunge pool. Breakfast. Bags.", "The car back to Cancún airport needs a two-hour cushion plus the beach-road crawl. Tulum airport is the shorter version if your flight uses it.", "Eat breakfast properly. The highway food is a petrol station.", "Photograph the room number and the pin. You may need to explain the pickup point to a driver who has never been down the road.", "Playa del Carmen"),
    ],
    attractions=[
        sight("Your plunge pool", "The private one in the suite or the ground-floor room. Shared infinity pools are what the cheaper category gets.", "Confirm it on arrival while the driver is still there."),
        sight("Tulum ruins", "The cliff city. Go at opening, before the heat and the tour groups from Cancún.", "Tickets and the rules change. Check the week you travel, and carry cash."),
        sight("Gran Cenote", "The easiest famous cenote near town. Clear water, a short swim, a crowd by 11:00.", "Go early. No regular sunscreen if the sign says so."),
        sight("Tulum beach", "The sand in front of the hotels. Beautiful when the seaweed is gone, and buried when it is not.", "Ask the hotel that morning. A brown line of sargassum is not a failure of your booking."),
        sight("Tulum pueblo", "The inland town with the tacos and the hardware stores. A useful dinner, not a resort.", "Go once. The beach road does not have ordinary shops."),
        sight("Sian Ka'an", "The biosphere south of the hotels. Worth a different trip's whole day.", "Do not bolt it onto a plunge-pool afternoon.", "Sian Ka'an Biosphere Reserve"),
    ],
    scenic_routes=[
        route("Beach road crawl", "From the highway arch down the Boca Paila road to the hotel. Ruts, bikes, buggies, no useful street numbers.", "20 to 40 minutes for a few kilometers"),
        route("Ruins at opening", "Hotel to the archaeological site when the gate opens, then back before lunch.", "A morning, plus the slow road twice"),
        route("Cenote and back", "An early ride to one cenote, a swim, and the pool by early afternoon.", "Half a day"),
    ],
    transport="A pre-booked car from the airport, then hotel buggies and taxis that know the kilometer markers. Do not rent a scooter on this road unless you already ride rough tracks. There is no walking between most hotels after dark in a useful way; distances are short and the road is not lit. Cash and an offline pin matter more than a bus map.",
    food=[
        dish("Tacos in the pueblo", "A standing taquería in Tulum town", "Al pastor and a agua fresca. The meal that costs a fraction of the hotel dinner. Go on the ruins day."),
        dish("Hotel ceviche", "Be Tulum, Mi Amor, or Nômade", "You will eat it because leaving is a production. One good ceviche is enough; the second night, order fish a simpler way."),
        dish("Fruit and coffee at the room", "The suite, breakfast", "Many of these hotels include breakfast. Eat it. The road is a bad place to go hunting for a café at 8 a.m."),
        dish("Marquesitas or a street snack", "Town, after the ruins", "A sweet crepe from a stand. Dessert, so dinner can stay a taco."),
    ],
    tips=[
        "The booking line has to say plunge pool. At Mi Amor that means the ground floor. At Nômade it means the suite category, not the entry tent.",
        "Azulik is the famous hotel on this road. Some villas have a plunge or a tub, many do not, and there is no main pool. It is not the hotel for this search.",
        "Save the location pin. Drivers get lost, and the hotels do not have ordinary addresses.",
        "Summer sargassum can wipe out the swim. The private pool is the insurance. November to April is the kinder window.",
    ],
    faqs=[
        faq("Which rooms actually have a private pool?", "Be Tulum markets private plunge pools with its suites; still match the suite name on the confirmation. Mi Amor's plunge pools are the ground-floor rooms. Nômade has them on many suites, not as a promise for every bed."),
        faq("Is Azulik the private-pool hotel?", "No. Do not book it for that reason. It is a remarkable building with limited electricity, and a pool is not the reliable feature."),
        faq("How bad is the road?", "Slow, potholed, and shared with buggies. A short distance takes a long time. Tell your airport driver the hotel pin, not a street number."),
        faq("Can we do the ruins, a cenote, and Sian Ka'an?", "The ruins and one cenote, yes. Sian Ka'an is a separate full day on a boat and does not fit beside a pool afternoon."),
    ],
    map_places=[
        stop("Be Tulum", "Tulum", "Mexico"),
        stop("Mi Amor", "Tulum", "Mexico"),
        stop("Tulum ruins", "Tulum", "Mexico"),
        stop("Gran Cenote", "Tulum", "Mexico"),
        stop("Tulum pueblo", "Tulum", "Mexico"),
    ],
    budget_notes="Plunge-pool suites on this road often run $350-900 a night, more at Christmas. Hotel meals are the painful line: budget $40-80 a person if you eat on site, or mix in one pueblo taco night. The airport car is $80-150 from Cancún. Cash for the ruins, tips, and the cenote. The road itself is free and still the most expensive-feeling part of the day.",
))

add(trip(
    slug="tulum-quiet-romantic-getaway",
    title="A quiet Tulum week: the far end of the coast, ruins at opening, one cenote",
    location="Tulum, Mexico",
    summary=(
        "Four nights aimed at the quiet end of this coast, not the beach-road bars. Hotel Esencia is in "
        "Xpu-Há, about half an hour north of the Tulum ruins, on its own beach. Azulik is the famous "
        "jungle-and-candle hotel on the Tulum road, adults only, with little electricity in the rooms. "
        "Coqui Coqui is the small scented hotel. None of this is a party plan. You go to the ruins when "
        "they open, swim one cenote, and eat a long dinner."
    ),
    who="A couple who want a quiet room, an early ruin, and dinner that does not come with a DJ.",
    best_time="Late November to April. Summer is hotter, wetter, and more likely to put sargassum on the sand. Christmas week is crowded even at the quiet hotels.",
    nights=4,
    hook="4 nights · Quiet coast · Ruins at opening, one cenote",
    constraints=["Quiet and romantic", "Away from the party end of the beach road", "Concrete hotels"],
    lodging="$400-1,200",
    daily="$500-1,300",
    neighborhoods=[
        stay_area("Xpu-Há", "Hotel Esencia's beach, between Playa del Carmen and Tulum. You give up the walkable hotel zone and gain a quiet shore. The ruins are a short drive."),
        stay_area("The quieter Tulum beach road", "Azulik and Coqui Coqui sit on the hotel road, which is still bumpy and address-less. Pick them for the room, and decline the loudest dinners."),
    ],
    hotels=[
        hotel("Hotel Esencia", "Xpu-Há", "A long-running estate hotel on its own beach, originally a private house. Jungle rooms and suites include private plunge pools; the pool villas are a further step up. It is the quietest hotel on this list because it is not on the Tulum hotel strip. Often $700-1,500. The ruins are about 25 to 40 minutes south.", "$700-1,500", "Tulum, Mexico"),
        hotel("Azulik", "Tulum beach road", "The famous wood-and-vine hotel over the jungle and the water. Rooms are mostly candlelit, with little or no electricity, no television, and no ordinary hotel pool. Some villas have a small plunge or a tub; do not book it for a guaranteed private pool. Adults, and the beach is clothing-optional. Often $600-1,400.", "$600-1,400", "Tulum, Mexico"),
        hotel("Coqui Coqui Tulum", "Tulum", "A small perfumed hotel from the Yucatán brand that also has houses in Valladolid and Mérida. It is a romantic, low-key room rather than a scene. Confirm what is included, because the property is tiny and dinner may be a plan you make in town.", "$300-700", "Tulum, Mexico"),
    ],
    itinerary=[
        day(1, "Arrive and stop", "The romantic version of this coast is the night you do not go out.", "Car from Cancún or Tulum airport. Esencia is off the highway at Xpu-Há. Azulik and Coqui Coqui are down the beach road; add the slow kilometers.", "Swim, then sit. At Azulik, learn the candles and the lack of outlets before you need a phone charger. The hotel has charging spots in public areas.", "Dinner at the hotel. At Esencia this is the estate's restaurant. At Azulik it is the hotel's own tables. At Coqui Coqui, ask that morning where dinner actually happens.", "Tell the front desk you are not interested in a beach-club crawl. The good hotels will plan a smaller evening."),
        day(2, "Ruins at opening", "Be there when the gate opens. The site is small and the cliff is the picture.", "Early departure. Tickets, water, and a hat. Two hours among the structures, then leave as the tour buses arrive.", "Back to the hotel for lunch and a long afternoon. A beach swim if the sand is clear. A pool swim at Esencia. At Azulik, the tub or the shade.", "Dinner again at the hotel, or one reservation in town if you are at Coqui Coqui and want a table that takes a card and a clock.", "The ruins close in the afternoon. A 2 p.m. arrival is the wrong romance."),
        day(3, "One cenote", "Fresh water, then a quiet afternoon. Sian Ka'an only if you have agreed it is a bumpy full day and you still want it.", "A cenote at opening. Gran Cenote is the known one. A hotel car to a less famous cenote is the quieter version; ask Esencia or Azulik which one they trust this month.", "Lunch, then nothing. Read. Sleep. A couple's massage if you booked it yesterday.", "Dinner on the property. This is the night a party hotel would ruin. You are not at that hotel.", "If you choose Sian Ka'an instead, cancel the massage and the cenote. It is a boat, a biosphere, and a long dirt road. It replaces the day.", "Sian Ka'an Biosphere Reserve"),
        day(4, "A slow morning, then the highway", "The last swim is the point. The airport is a scheduled interruption.", "Breakfast and a walk on the beach. Esencia's beach is the easy walk. The Tulum road hotels have a smaller strip of sand.", "Car to the airport with a cushion. From Xpu-Há to Cancún airport, allow two hours. From the beach road, allow more.", "Eat before you leave. A roadside taco is fine; a hungry arrival at the terminal is not the ending.", "Charge everything the night before if you are at Azulik. The room will not help you in the morning.", "Playa del Carmen"),
    ],
    attractions=[
        sight("Tulum ruins", "The walled city on the cliff. The right hour is the first hour.", "Go with a hat and without a plan to see Cobá the same day."),
        sight("Hotel Esencia's beach", "A quieter shore than the Tulum hotel zone, which is the reason to sleep at Xpu-Há.", "Walk it in the morning. The afternoon is for shade."),
        sight("Azulik", "A building more than a checklist. Candlelight, wood, and the sound of the sea under the floors.", "It is adults-only and inconvenient on purpose. Pack a power bank."),
        sight("A cenote", "One sinkhole swim in clear water. The contrast with the salt is the pleasure.", "Early, and follow the sunscreen rule on the sign."),
        sight("Sian Ka'an Biosphere Reserve", "Mangrove, lagoon, and a boat, south of the beach road.", "A full day or not at all. The entrance road is rough.", "Sian Ka'an Biosphere Reserve"),
        sight("Cobá", "The tall pyramid in the jungle, about 45 minutes inland. A different day from the cliff ruins.", "Only if you care more about a climb than about a quiet afternoon.", "Cobá"),
    ],
    scenic_routes=[
        route("Opening hour at the ruins", "Hotel to the Tulum site at the gate, two hours, back to a quiet lunch.", "A morning"),
        route("One cenote", "An early car to a single cenote and straight back. The romantic version has one swim, not a circuit.", "Half a day"),
        route("Sian Ka'an by boat", "A licensed boat into the biosphere. Bumpy road, long day, no shops. Replace day three if you want it.", "A full day"),
    ],
    transport="Private car from the airport and for the ruins and the cenote. Esencia can arrange this without the beach-road chaos. Azulik and Coqui Coqui still require the rutted hotel road. Walking at night between beach clubs is how the quiet trip turns into the loud one; stay at the hotel after dinner. Scooters are a poor idea on this surface.",
    food=[
        dish("A long hotel dinner", "Esencia or Azulik", "The meal you booked the silence for. Reserve it. At Esencia the cooking is part of the estate; at Azulik it is part of the scene you already accepted."),
        dish("Tacos in Tulum pueblo", "A simple taquería, once", "Al pastor, a salsa that you taste before you commit, and a bottle of water. The human-scale meal."),
        dish("Ceviche", "The hotel, lunch after the ruins", "Citrus and fish after a hot morning. Share one and order a cooked plate if you want something gentle."),
        dish("Breakfast at the room", "Included, or the hotel terrace", "Eat it slowly. There is no better café plan at Azulik before the staff are set up, and Esencia's breakfast is the reason you are there."),
    ],
    tips=[
        "Esencia is the quiet hotel because it is not on the Tulum party road. Azulik is quiet inside the room and theatrical everywhere else.",
        "Azulik does not reliably give you a private pool or a charged phone. Pack for candles.",
        "Ruins at opening, one cenote, one long dinner. That is the trip. A third activity makes it a tour.",
        "Sargassum in summer is a real spoiler of the beach walk. The season for this trip is the dry months.",
    ],
    faqs=[
        faq("Which hotel is actually quiet?", "Hotel Esencia, at Xpu-Há. Azulik is hushed in the room and famous enough to be a destination. Coqui Coqui is small. None of them is the central beach-club strip, and Nômade's music nights are a different page."),
        faq("Does Azulik have a private pool?", "Not as a promise. Some villas have a plunge or a hot tub. There is no main pool. Book it for the rooms, not for a swim."),
        faq("Can we see the ruins and still have a romantic day?", "Yes, if you go when they open and you are back for a late lunch. A midday visit in a tour group is the unromantic version."),
        faq("Is Sian Ka'an worth it?", "Yes, as the whole of day three, on a small boat with a licensed guide. It is not a sunset add-on after a cenote."),
    ],
    map_places=[
        stop("Hotel Esencia", "Xpu-Há", "Mexico"),
        stop("Azulik", "Tulum", "Mexico"),
        stop("Tulum ruins", "Tulum", "Mexico"),
        stop("Sian Ka'an", "Tulum", "Mexico", "Sian Ka'an Biosphere Reserve"),
        stop("Cobá", "Cobá", "Mexico", "Cobá"),
    ],
    budget_notes="Esencia and Azulik are often $600-1,500 a night. Coqui Coqui can sit lower and still well above a town hotel. Meals at the quiet hotels are a significant daily cost; one pueblo lunch keeps it human. Cars from Cancún airport are the other line. The ruins and a cenote are modest next to the room. Christmas week is a poor time to insist on quiet.",
))

add(trip(
    slug="tulum-pet-friendly",
    title="Tulum with the dog left at home",
    location="Tulum, Mexico",
    summary=(
        "Four nights in Tulum without a dog. Most of the beach-road eco-hotels refuse pets: thatch, "
        "wildlife, cenotes, and house rules all point the same way. Mexico may allow a dog across the "
        "border with the right papers, and that is not the same as Azulik, Habitas, or Papaya Playa "
        "Project letting the dog into a room. This itinerary assumes the dog stays home. The pet "
        "constraint is unmet. The ruins, one cenote, and the beach still work."
    ),
    who="A traveler who hoped a jungle hotel would say yes to a dog, and who should hear no before booking the flight.",
    best_time="December to April for the beach. The hotels' pet answers do not soften in low season.",
    nights=4,
    hook="4 nights · Leave the dog at home · Ruins, cenote, beach",
    constraints=["Pet-friendly search, unmet", "Beach-road hotels usually say no", "Get any exception in writing"],
    lodging="$250-700",
    daily="$320-800",
    neighborhoods=[
        stay_area("Tulum beach road", "Where Azulik, Habitas, and Papaya Playa Project actually are. Beautiful, and a bad place to arrive with a dog and a hope."),
        stay_area("Tulum pueblo and Aldea Zama", "The town side, where a private house might someday say yes. This itinerary does not depend on that house. Eat here, sleep on the coast without a pet."),
    ],
    hotels=[
        hotel("Azulik", "Beach road", "Open villas, wildlife, candles, and a clothing-optional beach. It is a poor fit for a dog and should be treated as no-pets. Stay for the building if the dog is at home. Do not claim a private pool; some villas have a plunge or a tub and there is no main pool.", "$600-1,400", "Tulum, Mexico"),
        hotel("Habitas Tulum", "Beach road", "A well-known beach hotel with a social side. I have no basis to call it pet-friendly, and the safe assumption is no. Book the room for the beach, and ask only if you enjoy collecting a written refusal.", "$300-700", "Tulum, Mexico"),
        hotel("Papaya Playa Project", "Beach road", "A long-running, simpler beach hotel on the same road. Rooms are closer to cabanas than to sealed apartments. Treat it as no-pets. It is the more relaxed, less precious stay if you are coming without an animal.", "$200-500", "Tulum, Mexico"),
    ],
    itinerary=[
        day(1, "The road, without a kennel", "Arrival is a bad road and a good swim. It is easier with ordinary luggage.", "Car to the beach road. Check in. Walk the sand in front of the hotel and stop at the edge of the property. These are not endless public esplanades.", "Swim, rinse, sit. Read the house rules you already expected: no pets, and often a fragile ecosystem pitch that is doing real work.", "Dinner at the hotel or a taco run to town if the buggy is easy. Come back early.", "If a listing showed a dog on a bed, and you do not have an email from this hotel for these dates, you are still at no."),
        day(2, "Ruins at opening", "The same good plan as every other Tulum week.", "The archaeological site at opening. Cliff, temple, sea. Two hours.", "Town lunch, tacos or a sit-down meal, then the beach when the sun drops a little.", "A hotel dinner. You are not touring pet patios.", "The ruins are not a dog stop. Neither is a cenote. That alone should end the debate."),
        day(3, "One cenote", "Fresh water, a rule sheet, and a reminder that a dog does not belong on those stairs.", "An early cenote. Follow the sunscreen ban. Swim and leave before the tour vans.", "Afternoon at the hotel beach. Habitas may feel social by dusk; Papaya can too. Azulik stays stranger and quieter in the room.", "Dinner. One nice meal, then sleep. The beach road after midnight is the party version of Tulum, and it is optional.", "Do not put a dog in a cenote, a taxi, or a thatched room that said no.", "Cobá"),
        day(4, "Beach morning, airport afternoon", "A last swim is the whole morning.", "Walk and swim. Pack the sand out of the bag.", "Car to Cancún or Tulum airport with the usual cushion for the beach road.", "Eat first. The rest of the day is a highway.", "A future pet exception has to name the hotel, the dates, and the dog. A brand-new villa with a stock photo is not that email.", "Playa del Carmen"),
    ],
    attractions=[
        sight("Tulum ruins", "The cliff site. Go early, before the heat.", "Carry cash and a hat. Leave any fantasy of a dog outside with the car."),
        sight("The hotel beach", "A short piece of sand in front of where you slept. Swim in the morning.", "Check the sargassum. Summer can be a brown line of weed."),
        sight("A cenote", "One sinkhole. Clear, cool, and rule-bound.", "No ordinary sunscreen. No pets, which the signs will also tell you."),
        sight("Tulum pueblo", "Tacos, a pharmacy, and a reminder that most of Tulum is a town, not a hotel lobby.", "Eat here once so the hotel bill is not the whole story."),
        sight("Sian Ka'an Biosphere Reserve", "The protected coast south of the hotels. A boat day if you want a fifth reason the dog was a bad idea.", "License, bumpy road, full day.", "Sian Ka'an Biosphere Reserve"),
        sight("Cobá", "Jungle pyramids inland, if the beach day is rained out.", "A half-day with a car, not a pet outing.", "Cobá"),
    ],
    scenic_routes=[
        route("Beach road to the ruins", "Slow kilometers out to the highway, then the short hop to the site at opening, then the same ruts home.", "A morning"),
        route("One cenote", "Hotel to a single cenote early, and back to the sand.", "Half a day"),
        route("Airport car", "Cancún airport is about two hours plus the beach road. Tulum airport is the shorter flight option when it exists for your route.", "Half a day on departure"),
    ],
    transport="Private cars and hotel buggies. The beach road is the whole transport story: slow, shared with bikes, and hostile to a pet you are trying to hide. Do not rent a scooter to solve it. Taxis know hotel names better than addresses, and they still get lost; keep the pin.",
    food=[
        dish("Tacos al pastor", "A pueblo taquería", "The correct cheap dinner. Eat them standing up on the ruins day."),
        dish("Ceviche", "The hotel, once", "A lime-cured lunch. Split it. Order a cooked dish beside it if you want something warm."),
        dish("Grilled fish", "Papaya Playa or Habitas, if that is where you are", "The straightforward dinner. Azulik's menus are more of a production and more of a bill."),
        dish("Fruit water and a marquesita", "Town", "A cold agua fresca and a sweet crepe. The snack between the ruins and the car."),
    ],
    tips=[
        "Assume Azulik, Habitas, and Papaya Playa Project will say no. Do not arrive to negotiate.",
        "A Mexican import paper is not a hotel permission. They are different yeses, and you need both, and you have neither on this itinerary.",
        "Cenotes, ruins, and thatched beach rooms are each a reason to leave the dog at home.",
        "If a private house in Aldea Zama ever says yes, get it in writing. This trip does not name that house, because I will not invent one.",
    ],
    faqs=[
        faq("Can I bring my dog to a Tulum eco-hotel?", "Almost certainly not. Azulik, Habitas, and Papaya Playa Project should be treated as no-pets. Get any exception in writing before you fly, and expect not to receive one."),
        faq("Does Mexico allow dogs?", "Travelers do enter Mexico with dogs when the paperwork is in order. That is a border question. It does not open a cenote, a ruin, or these hotels."),
        faq("Is there a pet-friendly villa you recommend?", "No. I am not going to invent one. A listing with a dog photo is not a confirmation. The town side is where a yes would have to come from, in writing, and this itinerary stands without it."),
        faq("Is the trip good without the dog?", "Yes. Ruins at opening, one cenote, and a morning swim are the whole Tulum week. They work better without a pet in the car."),
    ],
    map_places=[
        stop("Tulum ruins", "Tulum", "Mexico"),
        stop("Azulik", "Tulum", "Mexico"),
        stop("Habitas Tulum", "Tulum", "Mexico"),
        stop("Papaya Playa Project", "Tulum", "Mexico"),
        stop("Gran Cenote", "Tulum", "Mexico"),
    ],
    budget_notes="These hotels run roughly $200-700 at Papaya and Habitas and more at Azulik, before food. Eating on the beach road is the expensive habit; one town meal a day cuts it. There is no pet fee in the budget because the correct cost is a sitter at home. A car from Cancún is the other unavoidable line. Do not add a 'pet cleaning deposit' you have not seen in writing.",
))

add(trip(
    slug="cancun-budget-under-200night",
    title="Cancún under $200 a night, if you skip Christmas week",
    location="Cancun, Mexico",
    summary=(
        "Four nights in Cancún on a budget that the Hotel Zone breaks in winter and especially at Christmas. "
        "Hotel Krystal Cancún, on the beach in the Zone, has listed standard rooms from about $150 in an "
        "ordinary week. Fiesta Inn Cancún Las Américas, on Avenida Bonampak downtown, stays under $200 "
        "even when the beach does not, and it is not on the sand. Fiesta Americana Condesa is beachfront, "
        "and a room-only rate can fit under $200 from late spring through fall. Christmas week will not qualify."
    ),
    who="A couple or friends who want the Caribbean water and will change neighborhoods when the Zone price jumps.",
    best_time="May to early November for a Hotel Zone room under $200, accepting heat, rain, and hurricane season. Christmas week and much of January to March will not make the cap at a beach hotel.",
    nights=4,
    hook="4 nights · Under $200 · Zone in summer, downtown if not",
    constraints=["Under $200 a night", "Christmas week does not qualify", "Downtown is the reliable version"],
    lodging="$80-190",
    daily="$140-250",
    neighborhoods=[
        stay_area("Hotel Zone", "The beach strip on Boulevard Kukulcán. Krystal and, in the cheap months, Fiesta Americana Condesa put you on the water. Winter rates step over this budget."),
        stay_area("Downtown Cancún, Bonampak", "Fiesta Inn Las Américas is the year-round under-$200 hotel. A taxi of 15 to 25 minutes reaches the public beaches. You are sleeping in the city."),
    ],
    hotels=[
        hotel("Hotel Krystal Cancún", "Kukulcán Km 9, Hotel Zone", "A long-running Zone hotel with its own beach. Standard rooms have been listed from about $150, taxes included, in an ordinary week; ocean-view categories sit higher and Christmas week will not stay under $200. It is not all-inclusive. You pay for meals.", "$150-250", "Cancun, Mexico", "https://en.krystal-cancun.com/"),
        hotel("Fiesta Inn Cancún Las Américas", "Avenida Bonampak", "A downtown hotel near Bonampak, a short ride from the airport and a taxi from the beach. Published room rates often start under $100. This is the hotel that still qualifies when the Zone does not. There is a pool, not a reef outside the door.", "$75-140", "Cancun, Mexico"),
        hotel("Fiesta Americana Condesa Cancún", "Hotel Zone", "A well-known beachfront Zone hotel. A room-only rate in summer and early fall can fall under $200. Christmas week, much of the winter, and any all-inclusive package should be assumed over the cap until the live total says otherwise. Confirm you are not buying a meal plan by accident.", "$140-280", "Cancun, Mexico"),
    ],
    itinerary=[
        day(1, "The beach that matches the rate", "If the hotel is in the Zone, you are already there. If it is downtown, the first job is a taxi to a public beach, not a resort tour.", "Check in. Zone hotels: swim before dinner. Downtown: drop bags and taxi to Playa Delfines or the public end of the strip for a late swim, then back.", "Walk only the piece of Kukulcán you need. The Zone is a highway with hotels, not a strolling town.", "Dinner downtown at Parque de las Palapas if you are already in the city, or a simple Zone meal if you are not crossing back. Keep it cheap on night one.", "The Zone sidewalk is incomplete. At night, use a taxi even for a 'short' hop.", "Cancún"),
        day(2, "Isla Mujeres, early", "A ferry day, not a catamaran party unless you want one.", "Taxi to Puerto Juárez and the passenger ferry to Isla Mujeres. About 45 minutes on the water. Go north to Playa Norte and swim there; it is the gentle beach.", "Golf-cart the island only if you want the loop. The southern end is rocks and a lighthouse. Lunch on the island, then a return ferry before late afternoon.", "Back in Cancún for a taco dinner. Downtown is the better taco neighborhood. Zone guests can taxi in and out.", "Buy the ferry tickets in the morning. The last convenient boat back is earlier than the sunset you imagine.", "Isla Mujeres"),
        day(3, "Reef or ruins, not both", "Pick one. Chichén Itzá is about 2.5 hours each way and deletes the beach. A nearer snorkel keeps the $200 trip honest.", "A morning snorkel trip to a near reef, booked locally, or a taxi to the El Rey ruins in the Zone if you want archaeology without a bus. El Rey is small and close.", "Afternoon swim at the hotel beach or the public beach. A nap. This is a beach trip that spent its culture on day two.", "Dinner downtown again: Parque de las Palapas for tacos and a walk. It is the city's living room.", "A Chichén tour is a 14-hour day and a separate budget. Do it only by sacrificing Isla Mujeres.", "Chichén Itzá"),
        day(4, "Swim, then the airport", "The airport is closer to downtown than to the far end of the Zone. Leave accordingly.", "Morning swim. Return any snorkel gear. Buy water.", "A taxi with a gap before the flight. Zone traffic on Kukulcán can turn 20 minutes into 50.", "Eat a late breakfast or an early lunch. Airport food is the usual compromise.", "Christmas week is when this page's Zone hotels stop being under $200. If that is your date, you are at the Fiesta Inn and you already swam by taxi.", "Cancún"),
    ],
    attractions=[
        sight("Hotel Zone beach", "The reason to be in Cancún. Krystal and Condesa have beach frontage; the Fiesta Inn does not.", "Swim in the morning. Afternoon thunderstorms are common in the cheap season."),
        sight("Isla Mujeres", "A ferry ride to a smaller island and a calm north beach.", "Passenger ferry from Puerto Juárez. Skip the all-day booze boat.", "Isla Mujeres"),
        sight("Playa Norte", "The shallow beach on the north end of Isla Mujeres. The best swim of the trip.", "Rent a chair only if you need shade. The water is the point.", "Isla Mujeres"),
        sight("Parque de las Palapas", "The downtown park where the city eats tacos at night.", "Go hungry. The stalls are the meal."),
        sight("El Rey", "A small Maya site inside the Hotel Zone. A short visit, not Chichén.", "Combine it with a beach day, not with the ferry."),
        sight("Chichén Itzá", "The great inland site, and a very long day from this hotel.", "Worth it on a longer trip. On these four nights it replaces the island.", "Chichén Itzá"),
    ],
    scenic_routes=[
        route("Ferry to Isla Mujeres", "Taxi to Puerto Juárez, passenger ferry, Playa Norte, ferry back. The right day trip.", "About 45 minutes each way on the boat"),
        route("Downtown to the public beach", "From Bonampak to Playa Delfines or a Zone public access. The daily pattern if you slept at the Fiesta Inn.", "15 to 25 minutes by taxi"),
        route("Chichén Itzá by bus", "A full-day highway trip inland. Do it instead of Isla Mujeres, not as well as.", "About 2.5 hours each way"),
    ],
    transport="Taxis, the Isla Mujeres ferry, and your feet on the beach. The Hotel Zone bus runs the strip and is the cheap way to move between Kukulcán kilometers. Downtown to the Zone is a taxi. Rental cars sit in traffic and in parking lots; skip one unless you are driving to a cenote on your own. The airport is a short taxi from Bonampak and a longer one from the south end of the Zone.",
    food=[
        dish("Tacos at Parque de las Palapas", "Downtown, at night", "Several small portions, salsas on the side. The best cheap meal in the city."),
        dish("Cochinita pibil", "A downtown counter or a market stall", "Yucatecan slow-cooked pork. Eat it at lunch, when it is freshest."),
        dish("Grilled fish", "A simple Zone or island restaurant", "Once, on Isla Mujeres or after a swim. Check the price. The budget dies in beachfront seafood if you do it twice."),
        dish("Huevos motuleños", "Breakfast, downtown or the hotel", "Eggs on tortilla with beans, ham, peas, and salsa. A large breakfast makes the beach lunch optional."),
    ],
    tips=[
        "Christmas week will not be under $200 at Krystal's better rooms or at Condesa. Book the Fiesta Inn or move the date.",
        "All-inclusive prices are a different product. A $180 room-only rate that becomes a $320 package is no longer this page.",
        "The Zone is a poor walking city. Budget taxis rather than trying to stroll Kukulcán at noon.",
        "Hurricane season is the cheap season. Buy the travel insurance you would skip in March.",
    ],
    faqs=[
        faq("Can I stay on the beach for under $200?", "In summer and early fall, often yes at Hotel Krystal and sometimes at Fiesta Americana Condesa on a room-only rate. At Christmas, no. Fiesta Inn Las Américas is the hotel that stays under the cap, and it is downtown."),
        faq("Is the Fiesta Inn a beach hotel?", "No. It is on Bonampak, with a pool. The beach is a taxi. That is the honest way to hold the budget in winter."),
        faq("Are these all-inclusive?", "Krystal's standard rate is not. Condesa is often sold both ways; the room-only number is the one that can fit. An all-inclusive Christmas package will not."),
        faq("Is Isla Mujeres worth a day?", "Yes. Playa Norte is a better swim than most of the Zone, and the ferry is simple. Go early and come back under your own power."),
    ],
    map_places=[
        stop("Hotel Krystal Cancún", "Cancún", "Mexico"),
        stop("Parque de las Palapas", "Cancún", "Mexico"),
        stop("Isla Mujeres", "Isla Mujeres", "Mexico", "Isla Mujeres"),
        stop("Playa Delfines", "Cancún", "Mexico"),
        stop("Chichén Itzá", "Pisté", "Mexico", "Chichén Itzá"),
    ],
    budget_notes="Downtown rooms can sit under $120 for much of the year. Zone beach rooms under $200 are a May-to-November hope, not a Christmas one. Food stays near $25-40 a day on tacos and one fish lunch, and doubles if you eat at the hotel. Ferries and taxis are the other daily cost. An all-inclusive upgrade usually ends the under-$200 claim, which is fine if you change the claim on purpose.",
))

add(trip(
    slug="cancun-near-the-beach-under-300",
    title="A Hotel Zone beach hotel under $300, and not the all-inclusive giant",
    location="Cancun, Mexico",
    summary=(
        "Four nights in a beachfront Hotel Zone hotel that can sit under $300 a night for much of the year. "
        "InterContinental Presidente and the Marriott Cancun Resort are not all-inclusive; you pay for food. "
        "Fiesta Americana Condesa is beachfront and often sold both as a room and as a package, so read the "
        "rate plan. Hyatt Ziva is usually over this cap and is all-inclusive, so it is the wrong name for "
        "the search. Christmas week and spring break can push all three over $300."
    ),
    who="Travelers who want to walk out to the sand and still choose where they eat.",
    best_time="Most of the year except Christmas to New Year, spring break, and other holiday spikes. Summer is cheapest and stormier. January to March is when you have to check the live rate.",
    nights=4,
    hook="4 nights · Hotel Zone beach · Under $300 most weeks",
    constraints=["Near the beach", "Under $300 a night", "Know whether the rate includes meals"],
    lodging="$180-300",
    daily="$260-420",
    neighborhoods=[
        stay_area("Hotel Zone, mid-strip", "Presidente, the Marriott, and Condesa sit on Boulevard Kukulcán with beach frontage. The water is the neighborhood. The street is a highway."),
        stay_area("Downtown, for dinner", "Parque de las Palapas and the taco streets. A taxi away, and the right place for one meal that is not a resort price."),
    ],
    hotels=[
        hotel("InterContinental Presidente Cancun Resort", "Kukulcán Km 7.5", "A beachfront Zone hotel with a long, relatively calm beach and a pool. The rate is not all-inclusive. It often falls under $300 outside holiday weeks and can cross it at Christmas and in peak winter. You are paying for the sand and eating where you like.", "$180-340", "Cancun, Mexico"),
        hotel("Marriott Cancun Resort", "Hotel Zone", "Beachfront, with a pool and the usual resort machinery, and not an all-inclusive by default. A standard beach-side room often fits under $300 outside Christmas, New Year, and spring break. An ocean-front suite will not. Meal plans are optional; the room-only rate is the one this page means.", "$200-380", "Cancun, Mexico"),
        hotel("Fiesta Americana Condesa Cancún", "Hotel Zone", "A long-running beachfront hotel. Room-only rates often sit under $300 for a large part of the year. An all-inclusive package is a different and usually higher number. If the booking says meals and drinks for a headline that looks too low, read the dates and the occupancy again.", "$160-320", "Cancun, Mexico"),
    ],
    itinerary=[
        day(1, "The hotel beach", "You paid to be on the sand. Use it before you leave the Zone.", "Check in and swim. The Presidente's beach is one of the calmer stretches. The Marriott and Condesa have real frontage too; follow their flags.", "Walk the beach rather than Kukulcán. The road is loud and the sidewalk comes and goes.", "Dinner at the hotel or one Zone restaurant you have already picked. Night one is not the night to hunt downtown.", "Resort chairs at your own hotel are the free version. A beach club next door is how a $300 cap disappears.", "Cancún"),
        day(2, "Isla Mujeres", "The same good day trip as the cheaper page, from a more comfortable bed.", "Morning ferry from Puerto Juárez. Swim at Playa Norte. Eat lunch on the island.", "A short loop if you want it, then the ferry back in daylight. The Zone beach is still there tomorrow.", "Dinner downtown: Parque de las Palapas. Taxi both ways. Tacos are the point of leaving a beach hotel.", "Do not buy a sunset booze cruise as the island day. You can stand on a ferry.", "Isla Mujeres"),
        day(3, "Reef, then the pool", "A morning in the water and an afternoon under an umbrella you already paid for.", "A local snorkel trip or a morning at the El Rey site if you want stones instead of fish. Do not do Chichén today unless you have dropped the beach from the plan.", "Back for a late lunch and the hotel pool. The under-$300 beach trip includes resting on the beach.", "One nicer dinner, either at the hotel or a reserved Zone restaurant. This is the meal the room-only rate left you free to choose.", "Spring break weeks change the noise on this strip. If that is your date, Presidente's end is calmer than the club hotels and the rate may still be over $300.", "Cancún"),
        day(4, "Swim and leave", "The airport run is a taxi on Kukulcán. It is unpredictable in the afternoon.", "A last swim. Pack the sand.", "Leave with a margin. South Zone to the airport can be 40 minutes or it can be traffic.", "Eat at the hotel or downtown on the way only if the timing is obvious. Missing the flight is the expensive version of saving lunch.", "Keep the rate plan on your phone. A front desk upsell to all-inclusive on the last morning is not a bargain.", "Cancún"),
    ],
    attractions=[
        sight("Hotel Zone beach", "The Caribbean in front of the hotel. This is the attraction the rate is buying.", "Morning swim, shade at noon, another swim at 4:00."),
        sight("Isla Mujeres", "A ferry and a smaller island with a better swimming beach.", "Go on your own from Puerto Juárez.", "Isla Mujeres"),
        sight("Playa Norte", "Shallow, clear water on Isla Mujeres. Spend the middle of the day here.", "Bring cash and a hat.", "Isla Mujeres"),
        sight("El Rey", "A compact Maya site in the Hotel Zone, useful if you want ruins without a bus to Chichén.", "An hour, then back to the pool."),
        sight("Parque de las Palapas", "Downtown's evening taco park. The city's actual neighborhood life.", "One night is enough to understand you could have slept here for less and swum by taxi."),
        sight("Chichén Itzá", "The inland capital of this coastline's day trips, and too far to combine with a beach afternoon.", "Save it for a day you are willing to write off.", "Chichén Itzá"),
    ],
    scenic_routes=[
        route("The beach in front of the hotel", "Walk the sand until the next hotel's boundary, then turn around. Closer and better than walking the boulevard.", "An hour"),
        route("Ferry to Isla Mujeres", "Zone or downtown taxi to Puerto Juárez, ferry, Playa Norte, ferry back.", "A full day, with 45 minutes on the water each way"),
        route("Taxi to Parque de las Palapas", "An evening out of the Zone for tacos, then a taxi home. The antidote to a third hotel dinner.", "15 to 25 minutes each way"),
    ],
    transport="Taxis, the Zone bus, and the ferry. You can walk the beach and not much else. Kukulcán is dangerous to stroll at night in the badly lit parts. A rental car spends the day in a hotel garage. Airport taxis are a fixed habit; ask the price before you get in and compare it with a pre-booked transfer.",
    food=[
        dish("Tacos at Parque de las Palapas", "Downtown", "The one dinner that should not be at the hotel. Share a tour of the stalls."),
        dish("Breakfast at the hotel", "Presidente, Marriott, or Condesa", "If it is included, eat it. If it is $30 extra, compare it with a downtown breakfast and usually just pay, because the beach is the morning."),
        dish("Grilled fish on Isla Mujeres", "A beach restaurant at Playa Norte", "The trip's seafood meal. One order of fish, not the lobster special, keeps the day inside the budget."),
        dish("Cochinita or panuchos", "Downtown, lunch before the ferry or the day after", "Yucatecan pork and stuffed tortillas. Eat downtown at least once so the Zone does not set every price."),
    ],
    tips=[
        "Hyatt Ziva is the famous all-inclusive that usually sits over $300. It is a different search.",
        "Read the rate. Presidente and the Marriott are room-only unless you add a plan. Condesa may be packaged.",
        "Christmas week and spring break are when 'under $300' becomes a wish. Check the total, not a blog's memory.",
        "The beach in front of your hotel is the luxury. A second beach club is how people double the daily spend.",
    ],
    faqs=[
        faq("Will a beachfront room really be under $300?", "Often, at these three, outside Christmas, New Year, and spring break. In those weeks, assume it will not until you see the live total."),
        faq("Are they all-inclusive?", "Presidente and the Marriott Cancun Resort are not, unless you buy a package. Fiesta Americana Condesa is frequently sold both ways. The room-only rate is the one that fits this page."),
        faq("Why not Hyatt Ziva?", "It is a well-known all-inclusive on the beach, and the rate is usually above this cap. Book it if you want the meal plan and a higher number, not if you want this budget."),
        faq("Is the Zone walkable?", "Along the sand, yes. Along the road, poorly. Use taxis after dark and the bus in the daytime if you are hopping kilometers."),
    ],
    map_places=[
        stop("InterContinental Presidente Cancun", "Cancún", "Mexico"),
        stop("Marriott Cancun Resort", "Cancún", "Mexico"),
        stop("Isla Mujeres", "Isla Mujeres", "Mexico", "Isla Mujeres"),
        stop("Parque de las Palapas", "Cancún", "Mexico"),
        stop("El Rey", "Cancún", "Mexico"),
    ],
    budget_notes="Rooms at $180-300 are plausible for much of the year and unreliable at Christmas. Because two of these hotels are not all-inclusive, budget $50-90 a person for food if you mix the hotel and one downtown night. Taxis and the ferry add $20-40 on an outing day. A hidden all-inclusive supplement is the thing to find before you pay, not after.",
))

add(trip(
    slug="cancun-luxury-with-ocean-view",
    title="Oceanfront Cancún: Nizuc, Le Blanc, or the JW Marriott",
    location="Cancun, Mexico",
    summary=(
        "Four nights in a true oceanfront luxury hotel in Cancún. Nizuc sits at the quiet Punta Nizuc end "
        "and is not all-inclusive. Le Blanc is adults-only and all-inclusive, on the sand. The JW Marriott "
        "is beachfront and you book an ocean-view room, not a garden view, if the sea is the point. All "
        "three face the Caribbean. A 'Zone luxury hotel' with a lagoon view is a different window."
    ),
    who="A couple, or a family at Nizuc or the JW, who want the ocean outside and are willing to pay the winter rate.",
    best_time="December to April for calm, clear water, at the high rate. Late spring is cheaper and still swimmable. Hurricane season is a real trade at this price.",
    nights=4,
    hook="4 nights · Oceanfront luxury · Nizuc, Le Blanc, or the JW",
    constraints=["Ocean view", "Luxury beachfront", "Book the ocean category, not the garden"],
    lodging="$450-1,200",
    daily="$600-1,400",
    neighborhoods=[
        stay_area("Punta Nizuc", "The southern point, where Nizuc has its own beach away from the club strip. Quieter water and a longer ride to town."),
        stay_area("The Hotel Zone beach", "Le Blanc and the JW Marriott face the open Caribbean on Kukulcán. You are in the Zone, on the sand, not on a side street."),
    ],
    hotels=[
        hotel("NIZUC Resort & Spa", "Punta Nizuc", "A luxury resort on the point, with oceanfront rooms and a beach that is not the party Zone. It is not all-inclusive. Book an ocean-view room or suite; the property is large enough to have lesser views. Often $500-1,200. The spa and the beach are the day.", "$500-1,200", "Cancun, Mexico"),
        hotel("Le Blanc Spa Resort Cancún", "Hotel Zone", "An adults-only all-inclusive on the beach. The rate is high and it includes food and drinks, which changes the comparison with Nizuc and the JW. Book an oceanfront room if you want the sea rather than the pool deck. Often $600-1,500. Children are not the guest this hotel wants.", "$600-1,500", "Cancun, Mexico"),
        hotel("JW Marriott Cancun Resort & Spa", "Hotel Zone", "A beachfront luxury hotel with a serious spa and a pool, not an all-inclusive by default. An ocean-view or oceanfront room is the booking. A garden or resort-view room fails the search even at a luxury rate. Often $400-900 outside the steepest holiday weeks.", "$400-900", "Cancun, Mexico"),
    ],
    itinerary=[
        day(1, "The ocean you booked", "Check the window. If it faces a garden, this is the hour to ask for the category you paid for.", "Arrive and go to the beach. Nizuc's beach is the quiet one. Le Blanc and the JW give you the Zone's turquoise water with a better chair.", "Swim, then the spa only if you already have a booking. Walk-in spa hours at these hotels disappoint.", "Dinner at the hotel. At Le Blanc it is included; reserve the restaurant anyway. At Nizuc and the JW you are paying, so choose one table and stay there.", "Adults-only means adults-only. Do not arrive at Le Blanc with a child and a theory.", "Cancún"),
        day(2, "Isla Mujeres, done gently", "Even a luxury week is better with one morning off the property.", "A private boat or the ordinary ferry. The ferry is more honest and less 'package.' Swim at Playa Norte.", "Lunch on the island, back by mid-afternoon, and the hotel beach for the second swim of the day.", "A reserved dinner. Le Blanc guests should book the quieter restaurant. Nizuc and JW guests can stay on site or take a car to one serious table.", "The ocean-view room is wasted if you only see it in the dark. Leave the curtains open at 7 a.m.", "Isla Mujeres"),
        day(3, "Reef, or El Rey and the pool", "A soft day. Luxury here is an empty afternoon.", "A private or small-group snorkel if the sea is calm. Otherwise El Rey for an hour, which is inside the Zone and does not steal the day.", "Spa or pool. At Nizuc, stay on the property. The point of Punta Nizuc is that you do not go looking for entertainment.", "Dinner. If you are not all-inclusive, this is the expensive meal, and it should be one meal, not three.", "Chichén Itzá is a 14-hour day. It fights this hotel. Save the ruins for a different kind of week.", "Cancún"),
        day(4, "Morning water, afternoon flight", "The last swim is in front of the room.", "Breakfast on a terrace that faces the sea, then a swim.", "A car to the airport with a margin. Nizuc is at the far southern end, so it needs the most time.", "Eat at the hotel. You have already paid, either in the rate or in the plan.", "Check the folio for a resort fee and a spa gratuity before you are in the car.", "Cancún"),
    ],
    attractions=[
        sight("The oceanfront beach", "Nizuc's point, or the Zone beach at Le Blanc and the JW. The view you came to buy.", "Swim in the morning. The hotels will set up chairs; you do not need a club."),
        sight("Isla Mujeres", "A smaller island and a shallow beach, a good contrast to a large resort.", "Ferry or a small boat. Be back for a late swim at the hotel.", "Isla Mujeres"),
        sight("Playa Norte", "The swimming beach on Isla Mujeres.", "Spend two hours in the water, then leave. The island does not need a checklist.", "Isla Mujeres"),
        sight("Nizuc's pools and beach", "A quieter luxury campus at the end of the Zone.", "Stay on the property for one full afternoon. That is the use of this hotel."),
        sight("El Rey", "A small ruin in the Zone for a morning that is not a spa.", "Pair it with the pool, not with a second tour."),
        sight("Chichén Itzá", "The famous inland site. Too far for this four-night ocean plan.", "Come back when the hotel is not the point.", "Chichén Itzá"),
    ],
    scenic_routes=[
        route("Beach walk at dawn", "The sand in front of the room before the chairs multiply. The best half hour of a luxury beach trip.", "Under 2 km"),
        route("To Isla Mujeres", "A morning boat, Playa Norte, and back to the hotel beach.", "Most of the day, lightly used"),
        route("Punta Nizuc to the airport", "The long way out from Nizuc. Leave earlier than a central Zone hotel would.", "40 to 70 minutes"),
    ],
    transport="Hotel cars and taxis. You are not walking Kukulcán for fun. Le Blanc and the JW are simpler airport runs than Nizuc, which sits at the south end. A rental car is useless beside an oceanfront lobby. If you book a fishing or snorkel boat, use the hotel's desk and ask who operates it.",
    food=[
        dish("Breakfast facing the water", "The hotel terrace", "Fruit, eggs, and coffee with the actual view. At Le Blanc this is included. At the others it is a fair use of the rate."),
        dish("Dinner at the hotel restaurant", "Nizuc, the JW, or a reserved Le Blanc room", "One serious dinner. Le Blanc's inclusions still require a reservation at the good rooms. The others will be a real bill."),
        dish("Fish on Isla Mujeres", "Playa Norte", "Lunch, simply grilled. You are not hunting a celebrity table."),
        dish("A downtown taco stop, optional", "Parque de las Palapas", "Worth it if someone in the couple wants one meal that is not a resort. Skip it if the point of the spend was never to leave."),
    ],
    tips=[
        "The room category must say ocean or oceanfront. Resort view, garden view, and lagoon view are the ways this search fails politely.",
        "Le Blanc includes meals and drinks and excludes children. Nizuc and the JW do not include your dinner.",
        "Comparing a $700 all-inclusive with a $500 room-only rate is a false comparison. Add the food.",
        "Winter is when these hotels feel like what they cost. August can look cheaper for a reason.",
    ],
    faqs=[
        faq("Which one is the quiet luxury?", "Nizuc, at Punta Nizuc. Le Blanc is polished and social in an adults-only way. The JW is a large beachfront hotel with a better spa than a party scene."),
        faq("Is Le Blanc all-inclusive?", "Yes, and adults-only. The rate looks higher because food and drinks are inside it. Reserve the restaurants; 'included' does not mean walk-in at 8 p.m."),
        faq("Do all rooms face the ocean?", "No. Ask for oceanfront or ocean view in the confirmation. A luxury room that faces the garden fails this page."),
        faq("Should we add Chichén Itzá?", "Not on a four-night trip built around the water. The road eats the day. El Rey is the ruin that fits."),
    ],
    map_places=[
        stop("NIZUC Resort & Spa", "Cancún", "Mexico"),
        stop("Le Blanc Spa Resort", "Cancún", "Mexico"),
        stop("JW Marriott Cancun", "Cancún", "Mexico"),
        stop("Isla Mujeres", "Isla Mujeres", "Mexico", "Isla Mujeres"),
        stop("Punta Nizuc", "Cancún", "Mexico"),
    ],
    budget_notes="Expect $450-1,200 a night, with Le Blanc often higher because it is all-inclusive and Nizuc higher when you insist on the best ocean category. At the JW and Nizuc, add $80-150 a person per day for food and drinks. Spa treatments and a private boat sit outside all of those numbers. Christmas and New Year are a further step up, not a small surcharge.",
))

add(trip(
    slug="maui-with-private-pool",
    title="A private plunge in Wailea, which means a villa and a high rate",
    location="Maui, United States",
    summary=(
        "Four nights in Wailea, where a private pool means a villa category and usually $1,200 a night and up. "
        "Fairmont Kea Lani's two-story villas have a private plunge and a kitchen; the suites do not. Andaz "
        "Maui's villas offer a private hot tub or a plunge pool, so the confirmation has to say pool. Four "
        "Seasons Maui at Wailea has excellent shared pools and is not a private-pool booking. Lahaina's "
        "Front Street is still rebuilding after the 2023 fire; this trip stays in Wailea."
    ),
    who="A couple, or a family splitting a Kea Lani villa, who want the pool to themselves and have the rate.",
    best_time="April to June, or September to November, for a slightly softer rate. December holidays and winter whale season are when these villas are hardest to get and most expensive.",
    nights=4,
    hook="4 nights · Private plunge means the villa · Often $1,200+",
    constraints=["Private pool only in the villa category", "Wailea", "Honest luxury prices"],
    lodging="$800-2,500+",
    daily="$950-2,800+",
    neighborhoods=[
        stay_area("Wailea", "The resort coast. Beaches are public, the path between them is walkable, and the villas with their own pools are a specific, expensive inventory."),
        stay_area("Kihei, for a meal", "Just north, with grocery stores and plate-lunch shops. Useful because the Kea Lani villa has a kitchen. Not a reason to tour Lahaina."),
    ],
    hotels=[
        hotel("Fairmont Kea Lani", "Wailea", "All-suite hotel, and the private plunge is not in a standard suite. It is in the two-story villas: a gated courtyard, a plunge pool, a kitchen, and a walk toward Polo Beach. Those villas often run $1,200 to $2,500 and up. Book the villa by name. The hotel pools are shared and do not count.", "$1,200-2,500+", "Wailea, Maui", "https://www.fairmont-kea-lani.com/"),
        hotel("Andaz Maui at Wailea", "Mokapu Beach, Wailea", "Resort rooms use the shared infinity pools. Villas are the private-water category, and the hotel's own descriptions mix a private hot tub and a plunge pool. Ask which one the villa has, in writing. A hot tub is not the pool this search means. Villa rates are often $2,000 and up.", "$900-2,500+", "Wailea, Maui"),
        hotel("Four Seasons Resort Maui at Wailea", "Wailea", "The famous beach hotel, with some of the best shared pools on the island and a path to Wailea Beach. A garden or ocean room does not have a private pool. Treat it as the luxury hotel you book when a shared oceanfront pool is actually what you want. Rooms often run $800 to $2,000.", "$800-2,000", "Wailea, Maui", "https://www.fourseasons.com/maui/"),
    ],
    itinerary=[
        day(1, "The pool you paid for", "Confirm the category before you unpack the snorkel.", "If the Kea Lani booking is a suite, you are at the shared pools. If it is the two-story villa, the plunge is in the courtyard. At Andaz, read the villa line again: hot tub or pool. At the Four Seasons, enjoy the shared pool without renaming it.", "Wailea Beach path, a short walk, and a swim if the shore break is small. Polo Beach is the Kea Lani end.", "Dinner at the resort or Monkeypod Kitchen in the Shops at Wailea. Do not drive to Lahaina for a Front Street restaurant. The town is still rebuilding after the August 2023 fire.", "The villa kitchen at Kea Lani needs a grocery stop. The other two hotels are restaurant nights."),
        day(2, "Beach path, no summit", "A gentle day. Haleakala sunrise is a 3 a.m. project and it is not this itinerary.", "Walk the Wailea coastal path from Ulua toward Keawakapu or the other way, depending on the hotel. Swim where the lifeguard or the hotel says the shore break is kind.", "Afternoon in the private plunge if you have one, or in the Four Seasons pool if that is the hotel. A spa hour only if it was booked.", "A quiet dinner. The Shops at Wailea are enough geography. Kihei has plate lunch if you want to spend less than a resort menu.", "The path is public and the beaches are public. The chair service is the hotel's.", "Haleakalā National Park"),
        day(3, "Snorkel in the morning, pool after", "One boat, or none if the wind is up. Molokini is a real trip and a real cancellation risk.", "A morning Molokini or South Maui snorkel if the operator is going and you do not get seasick. It starts early. Back by lunch.", "The private pool, a nap, a book. This is the day the villa is for. Four Seasons guests do the same thing in a beautiful shared pool.", "Dinner in. Or a second night at a Wailea restaurant you already liked. No luau is required for this trip.", "Whale season is roughly December to April. A boat that promises a whale is still a boat, and the channel can be rough.", "Molokini"),
        day(4, "Plunge, then the airport", "Kahului is about 45 minutes from Wailea if the road is kind. It is not always kind.", "A last swim in the villa pool or the hotel pool. Coffee on the lanai.", "Leave after a late breakfast for an afternoon flight, earlier for a midday one. Return the rental car with a fuel stop that is not at the airport exit.", "Eat before the terminal. Maui's airport food is a short menu.", "If the plunge pool was the reason for the rate and you did not get one, say so on the morning of day one, not on the way to the airport."),
    ],
    attractions=[
        sight("Kea Lani villa plunge", "A private pool in a courtyard, attached to a two-bedroom villa with a kitchen. The suite product is a different hotel experience.", "Book the two-story villa. Ask to see 'plunge pool' on the confirmation."),
        sight("Wailea Beach path", "A paved walk linking the resort beaches. The public, free part of a very expensive stay.", "Go in the morning. Midday on the sand is a burn."),
        sight("Polo Beach", "The beach at the Kea Lani end of Wailea. Smaller and useful.", "The path reaches it. You do not need a tour."),
        sight("Ulua Beach", "A Wailea swim, sometimes with a little reef near the rocks when the sea is calm.", "Skip it if the shore break is dumping. The pool is the backup."),
        sight("Molokini", "The offshore crater. A half-day boat from Maalaea or Kihei when the wind allows.", "If you are a poor sailor, do not trade a sure pool for a maybe crater.", "Molokini"),
        sight("The Four Seasons pools", "Shared, landscaped, and excellent. They are the honest alternative when a private plunge is over the line.", "They do not become private because the rate is high."),
    ],
    scenic_routes=[
        route("Wailea coastal path", "Ulua, Wailea, and Polo, on foot, with swims. The daily walk.", "About 1.5 miles of path, as far as you like"),
        route("Molokini morning boat", "A booked boat, early, back before the trade winds fill in. Optional.", "A half day"),
        route("Wailea to Kahului", "The airport run. Piilani Highway to Kuihelani or the upper road, depending on traffic.", "About 45 minutes, longer at rush"),
    ],
    transport="A rental car. Wailea is walkable once you are on the path, and nowhere else is. The airport is Kahului, not next door. Do not plan dinner in Lahaina; the drive is long and Front Street is not the restaurant row it was before the fire. Parking at the hotels is part of the resort machine; the villa guests still need the car for groceries.",
    food=[
        dish("Villa breakfast", "Fairmont Kea Lani villa kitchen", "Eggs and fruit after a grocery run. This is the one hotel on the list where cooking is a real option, and only in the villa."),
        dish("Fish at Monkeypod Kitchen", "The Shops at Wailea", "A practical, good Wailea dinner that is not inside the hotel. Book it. It is not a Lahaina restaurant."),
        dish("Poke", "Foodland or a Kihei counter", "A pound of fresh poke and rice, eaten at the villa or on a bench. The luxury lunch that costs like an ordinary lunch."),
        dish("Resort dinner, one night", "Four Seasons, Andaz, or Kea Lani", "One hotel dinner is the occasion. The other nights, Monkeypod or the kitchen, or the bill will climb past the pool."),
    ],
    tips=[
        "Say the category out loud: Kea Lani two-story villa, or an Andaz villa whose note says plunge pool. A suite and a hot tub are different products.",
        "Four Seasons Maui is the wrong booking if a private pool is non-negotiable. It is the right booking if you want the best shared pool.",
        "Expect $1,200 or more for the private water. An $800 room at these hotels is still a shared pool.",
        "Leave Lahaina's restaurant list alone unless you have current local advice. The fire was in August 2023 and Front Street is not a casual night out.",
    ],
    faqs=[
        faq("Which booking has its own pool?", "The two-story villas at Fairmont Kea Lani. At Andaz, only a villa that specifies a plunge pool, not a hot tub and not a resort room. The Four Seasons pools are shared."),
        faq("What does it cost?", "Often $1,200 to $2,500 a night for a Kea Lani villa, and around $2,000 or more for an Andaz villa. Four Seasons rooms often start nearer $800 and still do not include a private pool. Holiday weeks go higher."),
        faq("Is Hotel Wailea the private-pool hotel?", "No. It is an adults-only hillside hotel with lanais and a shuttle to the beach. It is on the quiet-romantic page, not this one."),
        faq("Can we do Haleakala sunrise?", "Not as part of this four-night pool trip. Summit sunrise means a reservation and a middle-of-the-night drive. Do it on a trip that expects to be tired the next day."),
    ],
    map_places=[
        stop("Fairmont Kea Lani", "Wailea", "United States"),
        stop("Andaz Maui", "Wailea", "United States"),
        stop("Four Seasons Resort Maui", "Wailea", "United States"),
        stop("Wailea Beach", "Wailea", "United States"),
        stop("Molokini", "Maui", "United States", "Molokini"),
    ],
    budget_notes="The private pool is the splurge: plan $1,200-2,500+ for the villa, against $800-2,000 for a Four Seasons room with a shared pool. Food drops if you cook in the Kea Lani villa and rises fast at resort restaurants. A snorkel boat is often $150-250 a person. The car is mandatory. None of this gets cheaper by calling a lanai a pool.",
))

add(trip(
    slug="maui-2-bedroom-under-400night",
    title="A two-bedroom Kihei condo under $400, outside Christmas",
    location="Maui, United States",
    summary=(
        "Four nights in a two-bedroom condo in Kihei, which is a real category under $400 a night outside "
        "Christmas and New Year. Kamaole Sands, Mana Kai Maui, and Maui Kamaole are condo resorts with "
        "kitchens, across the road or on the beach at the Kamaole parks. Honua Kai, up in Kaanapali, is "
        "often over this cap. The same two-bedroom at Christmas commonly jumps to $500-900. The beaches "
        "are public and the kitchens are the point."
    ),
    who="A family or two couples who want two bedrooms, a kitchen, and a beach park rather than a resort wristband.",
    best_time="April, May, September, October, and early November. Summer can still fit. Christmas through New Year usually will not, and January stays firmer than people expect.",
    nights=4,
    hook="4 nights · Kihei two-bedroom · Under $400 outside Christmas",
    constraints=["Two bedrooms", "Under $400 a night", "Condo kitchen", "Christmas week excluded"],
    lodging="$220-400",
    daily="$320-480",
    neighborhoods=[
        stay_area("Kihei", "The condo coast. Kamaole Beach Parks I, II, and III are the swimming beaches. Grocery stores are close, which matters because you have a kitchen."),
        stay_area("Wailea, as a walk", "Ten to fifteen minutes south by car. The resort path is a morning outing, not a place you need to sleep in order to swim."),
    ],
    hotels=[
        hotel("Kamaole Sands", "Kihei, by Kamaole Beach Park II", "A large, long-running condo complex across from the beach park. Two-bedroom units with kitchens are the standard family booking and often fall under $400 outside holiday weeks. Pools are shared. Furnishings vary because owners rent them; read the specific unit.", "$220-400", "Kihei, Maui"),
        hotel("Mana Kai Maui", "Kihei, Kamaole Beach Park I", "A beachfront condo-hotel at the north end of the Kamaole parks. Two-bedroom units exist and often price under $400 in shoulder months; Christmas does not. You are on the sand side of the road, with a kitchen. Book the two-bedroom, not a studio, if that is the search.", "$250-450", "Kihei, Maui"),
        hotel("Maui Kamaole", "Kihei, near Kamaole Beach Park III", "Another established Kihei condo, often the more affordable two-bedroom of the three. Kitchens, shared pools, and a short walk to the beach park. Outside Christmas and New Year this is a credible under-$400 stay. In those weeks, do not force it.", "$200-380", "Kihei, Maui"),
    ],
    itinerary=[
        day(1, "Grocery, then the beach park", "The condo works after the fridge is full.", "Pick up the car, stop at Foodland or Safeway in Kihei, check in. Confirm you have two bedrooms and a kitchen, not a studio with a murphy bed.", "Swim at the nearest Kamaole park if the shore break allows. The parks are public, with showers.", "Cook the first dinner. That is the budget and the point. Grilled fish or a salad and rice is enough after a flight.", "Kihei's afternoon wind can make the beach less pleasant. Swim earlier tomorrow.", "Kihei, Hawaii"),
        day(2, "Kamaole in the morning, Wailea path after", "One beach day that does not require a boat ticket.", "Morning at Kamaole I, II, or III, whichever is calmest. Snorkel only inside the rocks if the sea is flat. If it is not, stay on the sand.", "Drive ten minutes to the Wailea path and walk an hour. You are visiting, not relocating. Gelato or a coffee, then back.", "Cook again, or take poke back to the condo. A restaurant night can wait.", "Do not leave valuables in the car at the beach parks. Break-ins are the local crime."),
        day(3, "A boat, or Makena", "Choose based on your stomach and the forecast.", "If you want a snorkel boat, this is the morning, from Kihei or Maalaea, back by early afternoon. If you do not, drive to Makena or Big Beach for a walk and a careful swim. The shore break at Big Beach is famous for being unkind.", "Afternoon at the condo pool. Laundry if you are in a unit that has it. The kitchen makes a late lunch.", "One dinner out in Kihei. A fish restaurant, reserved, then home. No luau-every-night plan, and no Lahaina reservation unless a local has confirmed the restaurant is open.", "Molokini trips cancel for wind. Have the Makena version ready.", "Molokini"),
        day(4, "Beach park, clean the kitchen, fly", "Condos charge for a kitchen left dirty. Clean it.", "A last morning swim. Run the dishwasher. Photograph the unit only if you would come back; the check-out list is the actual task.", "Car to Kahului. Kihei is closer than Wailea and still wants a margin. Fuel up in town.", "Eat the groceries. The airport is not the place for a last special meal.", "Christmas week is when this exact condo is often $600. If that is your date, this page told you so.", "Kihei, Hawaii"),
    ],
    attractions=[
        sight("Kamaole Beach Parks", "Three public parks in a row, which is why these condos exist. Grass, showers, and a swim.", "Morning, before the wind. Change parks if one has a shore break."),
        sight("Mana Kai's beach edge", "The sand in front of Mana Kai, continuous with Kamaole I.", "You still follow the ocean, not the brochure. A calm day is a swimming day."),
        sight("Wailea coastal path", "The resort walk, free, a short drive from the condo.", "Go once. The rest of the swims are in Kihei."),
        sight("Makena and Big Beach", "A wilder south shore beach. Beautiful and occasionally dangerous.", "Stay out of the water if the break is high. People get hurt here every year."),
        sight("Molokini", "The optional crater trip. Easy to board from this part of the island.", "Cancel without pride if you do not like boats.", "Molokini"),
        sight("The condo pool", "Shared, and perfectly good at 4 p.m. when the beach is windy.", "It is not a private plunge. That search is the Wailea villa page."),
    ],
    scenic_routes=[
        route("Morning loop of the three Kamaoles", "Park I to III along the road and the sand, and back to the unit.", "About 2 miles"),
        route("Kihei to the Wailea path", "A short drive south, a walk, a drive home for a kitchen lunch.", "15 minutes each way"),
        route("Kihei to Kahului airport", "North on Piilani, then across. The departure.", "About 30 to 40 minutes"),
    ],
    transport="A rental car. The beaches are walkable from these specific condos; the grocery store, Wailea, and the airport are not a pleasant walk with bags. Kihei has buses and you will not use them with beach chairs and a cooler. Park in the unit's assigned spot and at the public beach lots without leaving a bag in sight.",
    food=[
        dish("Cooked dinner", "The condo kitchen", "Fish, rice, a salad. Two dinners in will do more for the budget than any coupon."),
        dish("Poke", "Foodland Farms or a Kihei poke counter", "The no-cooking lunch. Buy it early; the good flavors sell out."),
        dish("Plate lunch", "A Kihei shop", "Two scoops of rice, mac salad, and a protein. One of these, not one every day."),
        dish("A Kihei fish dinner, once", "A reserved local restaurant in Kihei, not a Front Street name", "The night you do not cook. Keep Lahaina off the list unless you have checked that the specific restaurant survived and reopened."),
    ],
    tips=[
        "The under-$400 two-bedroom is a shoulder-season fact. Christmas to New Year is often $500-900 for the same unit.",
        "Honua Kai is the handsome Kaanapali condo that usually misses this cap. It is not the third name here for that reason.",
        "Read the unit, not just the building. Condo kitchens and sofas vary by owner.",
        "Big Beach looks calm in photos and is not always calm. When in doubt, use Kamaole.",
    ],
    faqs=[
        faq("Is a two-bedroom under $400 real?", "Yes in Kihei, outside Christmas, New Year, and some winter weeks. Kamaole Sands, Mana Kai, and Maui Kamaole are the buildings. The rate is for a specific owner unit, so check the dates."),
        faq("Do they have kitchens?", "Yes. That is the condo product. Use them. A hotel room in Wailea under $400 often does not have a kitchen and often is not two bedrooms."),
        faq("Are the pools private?", "No. They are shared condo pools. A private plunge is a Wailea villa at a much higher rate."),
        faq("What about Honua Kai?", "It is a real luxury condo resort in Kaanapali, and a two-bedroom there is often above $400. Leave it for a different budget."),
    ],
    map_places=[
        stop("Kamaole Sands", "Kihei", "United States"),
        stop("Mana Kai Maui", "Kihei", "United States"),
        stop("Kamaole Beach Park", "Kihei", "United States"),
        stop("Wailea Beach Path", "Wailea", "United States"),
        stop("Kahului Airport", "Kahului", "United States"),
    ],
    budget_notes="A two-bedroom at $220-400 is realistic in the shoulder months and a bad promise from about 20 December through early January. Groceries for breakfast and two dinners can hold food near $40-70 a day for two people. One restaurant night and a snorkel boat are the extras. Cleaning fees on condo bookings can add $150-300 to the stay, so put them in the nightly math before you celebrate the rate.",
))

add(trip(
    slug="maui-quiet-romantic-getaway",
    title="A quiet Maui: Napili Bay or Wailea, not a luau schedule",
    location="Maui, United States",
    summary=(
        "Four nights that stay quiet on purpose. Napili Kai is a low-rise hotel on Napili Bay, open since "
        "the 1960s. Hotel Wailea is adults-only on the hillside above Wailea, with a shuttle down to the "
        "beach and no claim here of a private pool. The Inn at Mama's Fish House is the small set of "
        "cottages beside the restaurant in Kuau, which is not Lahaina. Haleakala at sunrise means a "
        "reservation and a start around 2:30 or 3:00 a.m. Hana is a full day on a slow road. Neither is "
        "an evening plan."
    ),
    who="A couple who want one good dinner and a beach that does not come with a show.",
    best_time="May, June, September, and October. Winter is whale season and also peak rates. Avoid expecting Lahaina to entertain you; Front Street is still recovering from the 2023 fire.",
    nights=4,
    hook="4 nights · Napili or Wailea · One dinner, no luau circuit",
    constraints=["Quiet", "Romantic", "No nightly luau", "Haleakala only with a 3 a.m. start"],
    lodging="$350-900",
    daily="$480-1,050",
    neighborhoods=[
        stay_area("Napili", "A small bay and a low hotel. You walk to the sand. Evenings are the sound of the water, not a strip."),
        stay_area("Wailea hillside or Kuau", "Hotel Wailea if you want a polished adults-only suite and a shuttle to the resort beach. Mama's cottages if the dinner is the center of the trip and you like Paia better than a resort."),
    ],
    hotels=[
        hotel("Napili Kai Beach Resort", "Napili Bay", "Low-rise buildings on a small bay, a classic Maui hotel rather than a new tower. Studios and suites, a reefy little beach when the sea is calm, and evenings that end early. Often $400-700. It is not a private-pool resort and it is not a luau resort.", "$400-700", "Napili, Maui"),
        hotel("Hotel Wailea", "Wailea hillside", "Adults-only, Relais & Châteaux, about 72 suites on a garden hillside, with a shuttle to Wailea Beach. The suites have lanais and deep tubs. This page does not claim private plunge pools. Often $700-1,400. It is quiet because there are no children and no lobby scene.", "$700-1,400", "Wailea, Maui"),
        hotel("The Inn at Mama's Fish House", "Kuau, near Paia", "Cottages beside Mama's Fish House, the long-running restaurant that was not part of the Lahaina fire. You are here to book dinner and sleep within walking distance of it. The north shore is windier and more local than Wailea. Confirm the cottage and the dinner reservation together.", "$400-800", "Paia, Maui"),
    ],
    itinerary=[
        day(1, "The bay or the hillside, and stop", "Pick one hotel and let the first night be small.", "Napili: check in and swim in the bay if it is calm. Wailea: take the shuttle down, swim, and ride back up. Mama's: check into the cottage and walk the Paia road only as far as you feel like.", "No excursion. A shower and a chair.", "Dinner at the hotel, or the booked table at Mama's if that is the inn. One dinner. Do not add a luau because a brochure suggested it.", "If you want Haleakala sunrise later in the trip, the reservation has to exist already, and you will lose this night's sleep to it. Choose."),
        day(2, "A short coast, not the summit", "The romantic day is a swim and a drive that ends before dark.", "Napili guests can drive to Kapalua's beach and the coastal lookouts, then back. Wailea guests walk the path. Mama's guests go to Ho'okipa as a lookout, not as a swimming plan when the surf is up, then Paia for a coffee.", "Afternoon in the room. This is the trip.", "A simple dinner. Paia Fish Market is the unfussy north-shore meal. Wailea has Monkeypod. Napili can eat at the hotel.", "Do not continue from Paia around to Hana today. That is tomorrow's entire job, or it is not happening.", "Paia, Hawaii"),
        day(3, "Hana, or a long nothing", "Hana is 2.5 to 3.5 hours each way on a narrow road with one-lane bridges. It is a full day. The alternative is to stay at the bay and be happier.", "If you go, leave by 7:00, skip half the waterfalls, and turn around when you are tired rather than forcing the full loop back the south way. Buy banana bread at a roadside stand you can see is open. Do not pair this day with a summit sunrise.", "Be off the bad part of the road before dark. Dinner is late and simple.", "If you stayed, this was a beach day and a better dinner. Both versions are allowed. Only one is quiet.", "There is no gas station you should gamble on. Start with a full tank.", "Hana, Hawaii"),
        day(4, "Morning water, then Kahului", "The airport is closer to Paia than to Napili or Wailea. All three still want a margin.", "A last swim. Napili Bay in the morning is the nicest version. Hotel Wailea guests take the shuttle once more.", "Drive to Kahului. Return the car. If you did Hana yesterday, you are tired, so the flight should not be an early one.", "Eat a real lunch before the airport. Paia is the easy version if you slept at Mama's.", "A sunrise summit on departure day is how people miss flights. Do not.", "Haleakalā National Park"),
    ],
    attractions=[
        sight("Napili Bay", "A small crescent and a reefy swim when the swell is down. The quiet beach.", "If the surf is up, the hotel pool is the swim. Do not fight the shore break."),
        sight("Kapalua coast", "A few lookouts and a beach just north of Napili. A morning, not a tour.", "Then go back. The rest of West Maui is not required."),
        sight("Wailea Beach path", "The walk Hotel Wailea will shuttle you toward. Public sand, resort backdrop.", "Go once in the morning and once before dinner."),
        sight("Ho'okipa", "The north-shore lookout for wind and surf, near Paia. A viewing place.", "Stay out of the water unless you already know this break."),
        sight("Hana", "The village at the end of a long beautiful road. The road is the visit.", "A full day, or skip it. There is no quick version.", "Hana, Hawaii"),
        sight("Haleakala summit", "A volcanic crater above the clouds, if the clouds allow. Sunrise requires a reservation.", "Departure around 2:30 or 3:00 a.m. from Napili or Wailea, cold air, and a tired next day. Sunset is the kinder hour and you still drive down in the dark.", "Haleakalā National Park"),
    ],
    scenic_routes=[
        route("Napili to Kapalua and back", "A short coastal morning: one beach, one lookout, the hotel for lunch.", "Under an hour of driving"),
        route("Road to Hana", "Paia to Hana on the Hana Highway. Waterfalls, bridges, and a full day. Do not start after a summit sunrise.", "2.5 to 3.5 hours each way, plus stops"),
        route("Haleakala, if you insist", "A reserved summit sunrise. Middle of the night, a picnic, a descent, and a lost afternoon.", "About 1.5 hours from Wailea, longer from Napili, in the dark"),
    ],
    transport="A rental car, even if you barely use it at Napili. Hotel Wailea's shuttle covers the beach and not the rest of the island. The Hana road is slow and daylight-only for visitors who have not driven it. Kahului airport is the way in and out. Lahaina is not a stop for dinner on the way to anything.",
    food=[
        dish("Dinner at Mama's Fish House", "Kuau", "The special meal. Book it when you book the cottage, or weeks ahead if you are staying elsewhere and driving up. It is expensive and it is not in Lahaina."),
        dish("Paia Fish Market", "Paia", "Fish tacos or a plate, fast, good, and the right lunch before or after Hana. The town itself was not the fire zone."),
        dish("Breakfast at Napili Kai", "The hotel", "Eat it and go to the bay. A restaurant hunt is the opposite of this trip."),
        dish("Monkeypod Kitchen", "Wailea", "The easy good dinner if you are at Hotel Wailea and do not want the dining room. Still book."),
    ],
    tips=[
        "One dinner out, not a luau circuit. The bay at night is the entertainment.",
        "Haleakala sunrise is a reservation plus a 3 a.m. departure. If that sounds grim, go at sunset or do not go.",
        "Hana deletes whatever else you put on that date. Leave at 7:00 and turn around before dark.",
        "Hotel Wailea is quiet and adults-only. It is not, on this page, a private-pool villa.",
    ],
    faqs=[
        faq("Is this a luau trip?", "No. One dinner, a beach, and an optional long drive. A luau is a different evening in a different kind of week."),
        faq("Can we do sunrise at Haleakala?", "Yes, if you already have the reservation and you accept leaving around 2:30 or 3:00 a.m., in the cold, with a real chance of cloud. The next day should be empty."),
        faq("Is Hana a side trip?", "It is a whole day. The drive is 2.5 to 3.5 hours each way, with one-lane bridges. Do not plan it the morning after a summit sunrise."),
        faq("What about Lahaina?", "The August 2023 fire destroyed much of Front Street, and rebuilding is ongoing. This itinerary does not send you there for dinner. Eat in Napili, Wailea, or Paia."),
    ],
    map_places=[
        stop("Napili Kai Beach Resort", "Napili", "United States"),
        stop("Hotel Wailea", "Wailea", "United States"),
        stop("Mama's Fish House", "Paia", "United States"),
        stop("Hana", "Hana", "United States", "Hana, Hawaii"),
        stop("Haleakala", "Maui", "United States", "Haleakalā National Park"),
    ],
    budget_notes="Napili Kai often runs $400-700. Hotel Wailea is often $700-1,400. The Mama's cottages depend on the week and only make sense with the dinner, which is a serious bill for two. A Hana day is mostly free once you have the car and the fuel. There is no luau ticket in this budget on purpose. Summit reservations are a small fee and a large sleep debt.",
))

add(trip(
    slug="maui-pet-friendly",
    title="Maui with a dog only if Hawaii already said yes",
    location="Maui, United States",
    summary=(
        "Four nights in Wailea at hotels that publish a pet rule, after you have already cleared Hawaii's "
        "rabies quarantine. A casual 'bring the dog' is the wrong plan. The state is rabies-free and the "
        "5-Day-or-Less program wants vaccines, a blood test, a waiting period that is often months, and "
        "approval before you fly. Fairmont Kea Lani takes dogs 20 pounds and under. Grand Wailea takes "
        "dogs under 50 pounds for a large nightly fee. Andaz allows pets on request and may charge. Many "
        "beaches still prohibit dogs. If the paperwork is not finished, leave the dog at home."
    ),
    who="Someone whose dog already has Hawaii quarantine approval, or who needs to hear that approval is not a same-week project.",
    best_time="The paperwork sets the date, not the weather. For the island itself, May, June, September, and October are kinder rates. Do not book the flight and then start the blood test.",
    nights=4,
    hook="4 nights · Quarantine first · Then a Wailea hotel that actually takes dogs",
    constraints=["Hawaii rabies rules before any hotel", "Named hotels with published pet policies", "Beaches are not automatically open to dogs"],
    lodging="$400-1,200",
    daily="$520-1,400",
    neighborhoods=[
        stay_area("Wailea", "Where these three pet policies actually apply. A resort path, a car, and hotels that have written the rules down."),
        stay_area("Kihei condos, only unit by unit", "Some owners allow dogs and some do not. This page does not name a condo as pet-friendly, because the association is not the owner."),
    ],
    hotels=[
        hotel("Fairmont Kea Lani", "Wailea", "The hotel publishes a pet policy: dogs 20 pounds or under, from Hawaii or from out of state if the quarantine rules are met, about $40 a day, on a leash, not in the pools, crated if alone. A 40-pound dog does not become allowed because the room is a villa. The two-story villas are also the private-plunge category, which is a separate fact.", "$500-2,000", "Wailea, Maui", "https://www.fairmont-kea-lani.com/"),
        hotel("Grand Wailea", "Wailea", "A large resort with a published policy: pets under 50 pounds, one pet, about $200 per night, on a leash, not in restaurants or pools, and only after you have complied with state quarantine. The fee for four nights is $800 before the room. The pools are shared and elaborate. This is a yes with a real price, not a cozy inn.", "$500-1,200", "Wailea, Maui"),
        hotel("Andaz Maui at Wailea", "Mokapu Beach", "Listed by the hotel's booking channels as pet-friendly on request, with charges that may apply. Get the current weight limit and fee in writing before you fly. Rooms use shared pools. A villa is a different, much higher rate. The dog does not get the beach just because the hotel said yes.", "$700-1,600", "Wailea, Maui"),
    ],
    itinerary=[
        day(1, "A legal arrival, then a short walk", "The day's success is an animal that was allowed off the plane. The beach is secondary.", "Land with the paperwork the state already approved. Kahului is not the place to discover a missing blood test. Most animals clear through the state's process via Honolulu even when Maui is the destination; follow the current instruction, not a blog.", "Hotel check-in, the pet fee, the relief area the hotel names. A short leashed walk in the area the hotel allows. Do not head for the sand because it looks empty.", "Dinner at the hotel or Monkeypod, with the dog in the room only if the policy allows the dog to be unattended in a crate. Read that line twice.", "Heat is a medical problem for a dog in a parked car. The car is not a kennel, not for five minutes."),
        day(2, "Hotel grounds and a morning hour", "The good day is early and shady.", "Walk the dog at dawn in the space the hotel permits. People walk the Wailea path; dogs may not be allowed on it or on the beach. Ask the hotel that morning and follow the sign in front of you.", "The human swim happens in turns, or the dog stays in a crate in the room if the hotel permits that, while one person is on the beach. A dog does not go in the pool.", "A quiet dinner. Grand Wailea's fee is high enough that you should use the room and the grounds you paid for, not spend the day hunting a dog beach that is not there.", "Midday asphalt burns paws. Dawn and after 5:00 are the walking hours."),
        day(3, "One human outing", "The snorkel or the Wailea path is for people. The dog's day is the room and the relief area.", "One person, or both if a sitter or the crate plan is real, does a morning swim or a short Wailea walk. Do not leave the dog in the car at a trailhead.", "Afternoon in the room with the air conditioning. This is a resort afternoon, not a ridge hike.", "Dinner. If both of you go, the hotel's rule on unattended pets decides whether the dog is crated in the room or you order in.", "I am not sending you to a waterfall with a dog. The car would be hot and the trail is a bad idea.", "Kihei, Hawaii"),
        day(4, "Paperwork home, too", "Departure has a health-certificate direction as well. Ask your vet before you are at the airport.", "Dawn walk. Pack. The same heat rules.", "Car to Kahului with time for an animal that cannot sit in a hot parking lot. Follow the airline's crate rules on the way out.", "Eat before the airport. A long security line is worse with a thirsty dog.", "The 20-pound and 50-pound limits are not suggestions. A bigger dog needed a different plan months ago."),
    ],
    attractions=[
        sight("The hotel's pet relief area", "The place you will actually use. Ask where it is before you need it at 10 p.m.", "Bag it. The fee does not include someone else doing this."),
        sight("Wailea path, if dogs are allowed that week", "A flat walk. Often a human walk, not a dog walk. The sign wins.", "Go at dawn. If the sign says no dogs, turn around."),
        sight("Kamaole parks, for people", "The Kihei beaches. A human swim on day three while the dog is legally and safely parked in the room, if the hotel allows.", "Do not tie a dog in the sun beside a beach shower."),
        sight("Grand Wailea's grounds", "A lot of landscaping for a leashed morning walk if the hotel confirms the route.", "The pool is not the dog's. The published rule says so."),
        sight("Polo Beach", "A smaller Wailea beach at the Kea Lani end. A people swim.", "Same beach rule: dogs stay off unless a current county sign says otherwise."),
        sight("Kahului", "The airport town. Not a destination. The place the paperwork meets the flight.", "Build slack into the drive."),
    ],
    scenic_routes=[
        route("Dawn loop on hotel grounds", "The daily dog walk, short, leashed, before the heat. The route the front desk describes.", "15 to 30 minutes"),
        route("Wailea path, humans", "A morning walk for the people, dog left only under the hotel's crate rule.", "About a mile"),
        route("Wailea to Kahului", "The airport, with the dog, in a cooled car, with extra time.", "About 45 minutes"),
    ],
    transport="A rental car with the air conditioning already proven, and no plan that leaves the dog in it. Hotel shuttles may refuse the dog; ask. The beach path is not your guaranteed walk. If the quarantine routing requires Honolulu, that connection is part of the trip and it is the state's design, not an airline quirk you can talk your way through.",
    food=[
        dish("Breakfast in the room", "The suite or villa", "Easier with a dog than a dining room. Grand Wailea and the others are not inviting the dog to the restaurant."),
        dish("Monkeypod Kitchen", "The Shops at Wailea", "A human dinner. Go only with a legal plan for the dog during that hour."),
        dish("Poke from a Kihei shop", "Foodland or a counter, eaten at the hotel", "The flexible lunch. You can take turns leaving the room."),
        dish("Room service, one night", "Whichever of the three hotels you booked", "The night nobody wants to solve the crate question. Pay it."),
    ],
    tips=[
        "Start with the Hawaii Department of Agriculture rules, not the hotel. A FAVN blood test and the waiting period are often a months-long project. Five days or less is the name of the program, not the time it takes to qualify.",
        "Fairmont's limit is 20 pounds. Grand Wailea's is 50 pounds and about $200 a night. Andaz is on request. A condo listing is not a fourth hotel.",
        "Many Maui beaches prohibit dogs. A pet-friendly room is not a pet-friendly swim.",
        "Never leave the dog in the car. The trade winds do not make a closed car safe.",
    ],
    faqs=[
        faq("Can I bring a dog to Maui on a whim?", "No. Hawaii is rabies-free. The 5-Day-or-Less program requires rabies vaccines, a passing FAVN antibody test, a waiting period after that test that is often 120 days, a health certificate, and approval before arrival. If that process is not finished, leave the dog at home."),
        faq("Which hotels allow dogs?", "Fairmont Kea Lani, for dogs 20 pounds and under, about $40 a day, including out-of-state dogs that already meet quarantine. Grand Wailea, for dogs under 50 pounds, about $200 a night. Andaz Maui, on request, with a fee you must confirm. All three still require the state rules."),
        faq("Can the dog come to the beach?", "Do not assume so. County beaches commonly prohibit dogs, and these hotels prohibit them in the pools. Ask about the path and the relief area. The morning walk may be the hotel grounds and nothing else."),
        faq("What about a Kihei condo?", "Some owners allow dogs and the next unit does not. I am not naming a complex as pet-friendly. If you go that way, the yes has to be for that unit, in writing, and the quarantine still applies."),
    ],
    map_places=[
        stop("Fairmont Kea Lani", "Wailea", "United States"),
        stop("Grand Wailea", "Wailea", "United States"),
        stop("Andaz Maui", "Wailea", "United States"),
        stop("Kahului Airport", "Kahului", "United States"),
        stop("Kamaole Beach Park", "Kihei", "United States"),
    ],
    budget_notes="Rooms are ordinary Wailea rates, roughly $400-1,200 and much more for a villa, plus a pet fee: about $40 a night at Kea Lani or about $200 a night at Grand Wailea. Four nights at Grand Wailea is $800 in pet fees before tax. Budget the quarantine process as its own cost, paid months earlier. If you do not have approval, the correct pet budget is a sitter at home and a different trip.",
))

add(trip(
    slug="oahu-with-private-pool",
    title="Oahu, where Waikiki pools are shared and a private pool is a house",
    location="Oahu, United States",
    summary=(
        "Four nights in Waikiki with a plain statement about the water. Halekulani's pool is shared. The "
        "Royal Hawaiian's pool is shared. The Moana Surfrider's pool is shared. None of these towers has "
        "a private plunge in the room. A private pool means a house, usually outside Waikiki, in Kailua, "
        "Kaneohe, Hawaii Kai, or the hills above Kahala, and the listings change. I am not naming a rental "
        "brand. Four Seasons Resort Oahu at Ko Olina has been sold with a Pacific Suite plunge pool; confirm "
        "that category on the hotel's current sheet before you treat it as private. The rest of that resort "
        "uses shared pools."
    ),
    who="A couple who searched for a private pool and should hear what Waikiki actually is, then have a good four nights anyway.",
    best_time="April to June, or September to November. Winter surf on the North Shore is a lookout, not a swim. Waikiki's shared pools are pleasant in every season and they are still shared.",
    nights=4,
    hook="4 nights · Waikiki shared pools · A private pool is a house",
    constraints=["Private pool is unmet in Waikiki towers", "Shared pools described honestly", "A house is the real private-pool product"],
    lodging="$300-700",
    daily="$420-850",
    neighborhoods=[
        stay_area("Waikiki", "Walkable, swimmable, and full of famous hotels whose pools are for all the guests. This is the base of the itinerary."),
        stay_area("Kailua or Kahala, if you need the pool", "A house with a fenced pool is the product the search was after. Confirm the pool is private and in the rental, then decide if you are willing to leave Waikiki to have it."),
    ],
    hotels=[
        hotel("Halekulani", "Waikiki", "The calm beachfront hotel with the orchid pool. The pool is shared. The rooms do not have private pools. You are paying for the beach, the service, and a quieter lobby than the rest of the strip. Often $500-900.", "$500-900", "Honolulu", "https://www.halekulani.com/"),
        hotel("The Royal Hawaiian", "Waikiki", "The pink hotel, opened in 1927, with a courtyard pool and a beach. The pool is shared. A tower room with a lanai is still a tower room. Do not book it expecting a plunge pool. Often $350-700.", "$350-700", "Honolulu", "https://www.royal-hawaiian.com/"),
        hotel("Moana Surfrider", "Waikiki", "The oldest of the beach hotels, with a banyan courtyard and a shared pool. Ocean-wing rooms look at the water. They do not contain a pool. Often $300-650. It is the right hotel if you want the historic beach and you have dropped the private-pool requirement.", "$300-650", "Honolulu"),
    ],
    itinerary=[
        day(1, "The shared pool, used properly", "Arrive and enjoy the thing the hotel actually has.", "Check in. Swim in the hotel pool, then in Waikiki where the flags say to. The water in front of these three hotels is the easy swim.", "Walk the beach as far as Fort DeRussy and back. Diamond Head is a tomorrow-or-later project and it needs a reservation.", "Dinner near the hotel or a short walk into the neighborhood behind Kalakaua. The first night is not a North Shore drive.", "The pool is crowded in the middle of the day and pleasant at 8 a.m. Go then.", "Waikiki"),
        day(2, "Diamond Head or the long pool morning", "One reservation, early, then you are done with logistics.", "Diamond Head State Monument if you have the timed entry. It is a hot walk, not a private-pool substitute. Without a reservation, repeat the beach and the pool.", "Lunch, then a shaded afternoon. The hotel pool at 3 p.m. is enough.", "A proper dinner. Halekulani's restaurant is the expensive version. A simpler grill is a valid choice.", "Start the crater walk with water. Turning around in the sun is common and fine.", "Diamond Head, Hawaii"),
        day(3, "North Shore or Kailua, as a look", "A day trip, not a move. Winter surf is for watching.", "Drive over the pali to Kailua Beach in the morning, or continue to the North Shore if the group wants the big winter waves from a safe lookout. Swim in Kailua or Lanikai only when it is calm. In winter, Waimea Bay is not your swimming lesson.", "Shrimp or a plate lunch on the way back, then the hotel pool before dinner. You did not find a secret private pool on this drive. You found a coast.", "Dinner in Waikiki. Leonard's malasadas in Kapahulu can be the stop on the way home if you still have room.", "The pali road is beautiful and windy. People get carsick. Drive it in daylight."),
        day(4, "Beach, then the airport", "Honolulu airport is not far, and traffic makes it far.", "A last swim in the shared pool and a last walk on the sand.", "Leave with a cushion. Waikiki to the airport can be 25 minutes or it can be an hour.", "Eat before you go. A malasada is not lunch.", "If a Ko Olina suite was supposed to solve the private pool, that booking had to be confirmed before this morning. A Waikiki checkout is too late.", "Honolulu"),
    ],
    attractions=[
        sight("Halekulani's pool", "A shared orchid pool on the beach. It is beautiful and it is not private.", "Go early. The chairs are the competition."),
        sight("Royal Hawaiian courtyard", "The pink hotel's lawn and shared pool, which is the postcard.", "Walk through even if you are staying next door.", "Waikiki"),
        sight("Moana Surfrider courtyard", "The banyan tree and a shared pool at the old beach hotel.", "An evening drink under the tree is the use of it. The rooms upstairs still have no pools."),
        sight("Diamond Head", "The crater walk above Waikiki. A reservation, a hot path, a view.", "Timed entry. Without it, do not drive up and hope.", "Diamond Head, Hawaii"),
        sight("Kailua Beach", "The windward beach with pale sand and, on a calm day, a better swim than the postcard suggests.", "A day trip. A house here is how you would actually get a private pool, and I am not naming the house."),
        sight("USS Arizona Memorial", "The Pearl Harbor memorial. A separate morning, and a reservation.", "It does not combine with Diamond Head. Choose.", "USS Arizona Memorial"),
    ],
    scenic_routes=[
        route("Waikiki beach walk", "From the hotels through the sand to Fort DeRussy and back on Kalakaua if you need shade.", "About 2 miles"),
        route("Over the pali to Kailua", "H-1 to the Pali Highway and down to Kailua Beach. The island's other side, in the morning.", "About 30 to 40 minutes"),
        route("North Shore lookout day", "Up the center or the east side to the North Shore, a look at the winter surf, and back before dark.", "A full day, 1.5 to 2 hours each way with traffic"),
    ],
    transport="Walk in Waikiki. A rental car for Kailua or the North Shore, and only on that day if you hate parking; Waikiki garages are expensive. The airport is a taxi or a car return. TheBus works for Diamond Head and for some beach trips if you enjoy the scheduling. A private pool does not appear if you drive far enough without a reservation for a house that has one.",
    food=[
        dish("Malasadas", "Leonard's Bakery, Kapahulu", "The Portuguese doughnut that became a Honolulu habit. Buy them on the way back from the windward side, and eat them warm."),
        dish("Poke", "A Waikiki or Kapahulu counter", "Ahi and rice for lunch. The beach meal that is not a hotel club sandwich."),
        dish("Plate lunch", "Rainbow Drive-In or a similar long-running counter", "Two scoops, mac salad, and a protein. Once. It is a large meal."),
        dish("Hotel dinner, one night", "Halekulani if you are there, or a serious Waikiki restaurant", "One expensive dinner. The other nights, poke and a walk, or the pool will not be the only shared thing about the bill."),
    ],
    tips=[
        "The three famous pools are shared. Booking a suite does not change that.",
        "A private pool is a house outside Waikiki. Read the listing for a fenced pool that belongs to the rental, and expect to give up the walkable beach.",
        "If a hotel offers the Four Seasons Ko Olina Pacific Suite as a private plunge, make the hotel put that sentence on the confirmation. I am not treating a roundup article as a guarantee.",
        "Diamond Head and the Arizona Memorial both use reservations. Pick one.",
    ],
    faqs=[
        faq("Does the Royal Hawaiian have private pools?", "No. The pool is shared, in the courtyard. Halekulani and the Moana Surfrider are the same story. A lanai is not a pool."),
        faq("Where is a real private pool?", "A house in Kailua, Kaneohe, Hawaii Kai, or the Kahala hills, with the pool in that rental. I am not endorsing a management brand because the inventory turns over. Confirm the pool is private, fenced, and heated or unheated on purpose."),
        faq("What about Four Seasons at Ko Olina?", "The resort pools and lagoon are shared. A Pacific Suite has been described as having a private plunge. Confirm it on the current rate sheet. It is about 40 minutes from Waikiki and it is a very high rate."),
        faq("Is Waikiki still worth it?", "Yes, for the swim and the walking. Come for the shared pool and the beach. The private-pool search is a different map."),
    ],
    map_places=[
        stop("Halekulani", "Honolulu", "United States"),
        stop("The Royal Hawaiian", "Honolulu", "United States"),
        stop("Moana Surfrider", "Honolulu", "United States"),
        stop("Diamond Head", "Honolulu", "United States", "Diamond Head, Hawaii"),
        stop("Kailua Beach", "Kailua", "United States"),
    ],
    budget_notes="These Waikiki hotels often run $300-900 a night for a beach room, and the pool in that rate is shared. A house with a private pool can cost the same or more and will not be on the sand in Waikiki. Food can stay moderate on poke and plate lunch, or jump with one hotel dinner. The car is only essential on the day you leave town. There is no honest $400 add-on that puts a private pool inside the Royal Hawaiian.",
))

add(trip(
    slug="miami-near-the-beach-under-300",
    title="South Beach under $300, except when Miami decides otherwise",
    location="Miami, United States",
    summary=(
        "Four nights in South Beach at a real hotel that can land under $300 a night in summer, early fall, "
        "and ordinary weekdays. Catalina Hotel & Beach Club, Gale South Beach, and The National Hotel are "
        "the three. Winter weekends and Art Basel week, in early December, often jump over $300, sometimes "
        "by a lot. The National's pool is the famous one and it is shared. You are on Collins, a short walk "
        "from the sand, not in a private-pool villa."
    ),
    who="Friends or a couple who want the beach and will move the dates if the weekend price is silly.",
    best_time="May to June and September to early November. Avoid Art Basel week and holiday weekends in winter if the cap is firm. August is hot, cheap, and stormy.",
    nights=4,
    hook="4 nights · South Beach · Under $300 off the winter weekends",
    constraints=["Under $300 a night", "Near the beach", "Winter weekends often fail the cap"],
    lodging="$160-300",
    daily="$250-420",
    neighborhoods=[
        stay_area("South Beach, Collins Avenue", "Catalina, Gale, and The National are on or just off the beach grid. Ocean Drive is the noisy edge. Collins is the slightly more useful one."),
        stay_area("Mid-Beach, if the rate escapes", "A little quieter and not automatically cheaper. This itinerary stays south unless the live rate says otherwise."),
    ],
    hotels=[
        hotel("Catalina Hotel & Beach Club", "Collins Avenue, South Beach", "A straightforward South Beach hotel with a pool and a short walk to the sand. Ordinary non-winter weeks often fall under $300, and a Saturday in January often does not. Book a quieter room, not the one over the bar, if you want to sleep.", "$150-320", "Miami Beach"),
        hotel("Gale South Beach", "Collins Avenue", "A Collins Avenue hotel with a pool, in the same walk-to-the-beach category. It can sit under $300 in summer and early fall. Winter weekends and Art Basel week should be checked before you count them. You are here for the location, not a giant resort.", "$180-360", "Miami Beach"),
        hotel("The National Hotel", "Collins Avenue, South Beach", "The long-running hotel with the long blue pool. The pool is shared and it is the reason to pick this one when the rate cooperates. Under $300 is realistic in the soft months and unreliable on winter weekends. Ocean Drive noise is a block away; ask for a pool-side room if you want the postcard.", "$180-400", "Miami Beach"),
    ],
    itinerary=[
        day(1, "Swim before the scene", "The beach is best before it is a backdrop.", "Check in, or drop bags if the room is not ready, and swim. The public beach at the end of your street is the point.", "Walk north or south on the sand, then once down Ocean Drive so you have seen it. Stay on Collins after that.", "Dinner off Ocean Drive. A normal restaurant on a side street will be better than the front-row pasta.", "The under-$300 rate and a quiet room can be the same booking if you ask. They are not the same room by accident.", "South Beach"),
        day(2, "The pool, then a neighborhood", "One outing inland, while you can still face a car.", "Morning at The National's pool if you are staying there, or the beach if you are at the other two. The pool is the hotel's whole personality.", "Afternoon in Wynwood or the Design District for an hour of walking around, or Vizcaya if you want a garden instead of a mural. Do not try to do both.", "Dinner back on the beach side, early enough that Ocean Drive is still a choice rather than a crowd.", "Rideshares surge when the beach empties and when it fills. Walk when the distance is under 20 minutes.", "Miami Beach, Florida"),
        day(3, "Key Biscayne for the day", "A calmer beach and a lighthouse, which resets a South Beach trip.", "Car or rideshare over the Rickenbacker Causeway, which has a toll, to Bill Baggs. Swim, walk to the Cape Florida lighthouse, eat a picnic or a simple lunch.", "Back by late afternoon. The National's pool, or your own hotel's, is the second swim.", "A slightly better dinner. You have one night left and the rate you saved can go here.", "Bill Baggs is the nature hour. It is also the proof that Miami Beach is not the only sand.", "Key Biscayne, Florida"),
        day(4, "South Pointe, then leave", "The south end of the island is a park and a jetty. Use it in the morning.", "Walk to South Pointe Park, watch the ships, swim if the flags are kind.", "Airport or a train depending on how you arrived. Miami International is a rideshare of 30 to 50 minutes from South Beach, more in the afternoon.", "Eat a late breakfast. Cuban coffee and a pastry is the right last meal.", "If your dates are Art Basel week, this whole page may have been over $300. That is the week to stay home or pay the higher number on purpose.", "South Beach"),
    ],
    attractions=[
        sight("South Beach", "The sand in front of Collins. Wide, public, and enough of a beach for four mornings.", "Go early. The day gets hot and the chairs get rented.", "South Beach"),
        sight("The National's pool", "A long, famous hotel pool. Shared, photogenic, and a fair use of an afternoon.", "Stay in the chair you were given. It is not a private pool."),
        sight("Ocean Drive", "The Art Deco front. Walk it once.", "Eat somewhere else. The view is the product, and you have already looked."),
        sight("South Pointe Park", "Grass, a jetty, and the ship channel at the bottom of the island.", "Morning. Bring the dog only on the Miami pet page's rules; this page is people."),
        sight("Bill Baggs Cape Florida State Park", "A state park on Key Biscayne with a beach and a lighthouse.", "The causeway toll is part of the trip. Swim, walk, leave.", "Bill Baggs Cape Florida State Park"),
        sight("Vizcaya Museum and Gardens", "A bayfront villa and garden in Coconut Grove. The indoor-outdoor hour if you are tired of sand.", "Go on day two or not at all. It does not fit a departure morning.", "Vizcaya Museum and Gardens"),
    ],
    scenic_routes=[
        route("Collins to the sand and back", "The daily walk. Two blocks and you are wet.", "Ten minutes"),
        route("South Pointe and back", "Down the beach or the path to the park and the jetty.", "About 1.5 miles from the central hotels"),
        route("Rickenbacker to Bill Baggs", "A causeway with a view, a toll, and a quieter beach. Half a day.", "20 to 30 minutes each way"),
    ],
    transport="Walk. South Beach at this hotel tier does not need a car, and parking will cost more than the rides you actually take. Use a rideshare for Key Biscayne, Vizcaya, and the airport. The causeway is the one drive worth doing. At night, walk the lit streets and ride when the group is tired; Ocean Drive's chaos is not a scenic route after midnight unless that is the plan.",
    food=[
        dish("Cuban coffee and a pastelito", "A ventanita within walking distance", "The breakfast. Stand at the counter. It is cheaper than the hotel and faster."),
        dish("A Cuban sandwich", "A casual South Beach or mainland counter, not a club", "Ham, roast pork, cheese, pickles, and the press. One is a meal."),
        dish("Ceviche or grilled fish", "A side-street restaurant", "The one proper dinner. Share the ceviche and order a cooked entrée."),
        dish("Picnic at Bill Baggs", "Bought before you cross the causeway", "Fruit, a sandwich, water. The park is the point, not a restaurant hunt in a wet bathing suit."),
    ],
    tips=[
        "Check the date against Art Basel week and winter Saturdays before you believe $300.",
        "The National is the pool hotel. Catalina and Gale are the simpler Collins hotels. All three can break the cap on the wrong Friday.",
        "Ocean Drive is a walk, not a dinner strategy.",
        "A shared hotel pool is what these rates buy. A private pool in South Beach is a different and much higher search.",
    ],
    faqs=[
        faq("Will it really be under $300?", "In May, June, September, and early November, often yes. On winter weekends and during Art Basel week, often no. The live rate is the answer, and Christmas and New Year are not this page."),
        faq("Are we on the beach?", "A short walk, yes. These are South Beach hotels, not inland highway hotels. The sand is public."),
        faq("Is The National quiet?", "The pool is calm for South Beach. Ocean Drive is not. Ask for a pool-facing room and keep the expectations at 'hotel,' not 'spa retreat.'"),
        faq("Do we need a car?", "No, until Bill Baggs or the airport. Parking in South Beach is a second hotel rate."),
    ],
    map_places=[
        stop("The National Hotel", "Miami Beach", "United States"),
        stop("South Beach", "Miami Beach", "United States", "South Beach"),
        stop("South Pointe Park", "Miami Beach", "United States"),
        stop("Bill Baggs Cape Florida State Park", "Key Biscayne", "United States", "Bill Baggs Cape Florida State Park"),
        stop("Ocean Drive", "Miami Beach", "United States"),
    ],
    budget_notes="Rooms at $160-300 fit the soft months and fail a lot of winter Saturdays. Food is $40-70 a person if breakfast is a ventanita and one dinner is a real restaurant. Key Biscayne is a rideshare and a toll, not a tour price. Art Basel week can double the room. If the rate is $450, you are on a different trip and you should admit it before you arrive.",
))

add(trip(
    slug="miami-luxury-with-ocean-view",
    title="Oceanfront Miami Beach: Faena, The Setai, or Fontainebleau",
    location="Miami, United States",
    summary=(
        "Four nights in a hotel where the ocean-view category is the booking, not a hope. Faena and The "
        "Setai are the smaller luxury ends of Miami Beach. Fontainebleau is the famous oceanfront campus, "
        "and a pool-view or bay-view room is the wrong room even when the hotel is right. All three face "
        "the Atlantic if you buy the room that says so. Winter and Art Basel week are when the rates feel "
        "like the architecture."
    ),
    who="A couple, or a small group at Fontainebleau, who want the Atlantic outside the glass and will pay for that line on the reservation.",
    best_time="Late November to April if you want clear, social Miami, at the high rate. Summer is cheaper, hotter, and more humid, and the ocean is still there.",
    nights=4,
    hook="4 nights · Oceanfront category · Faena, Setai, or Fontainebleau",
    constraints=["Ocean view", "Luxury", "Book oceanfront, not pool view"],
    lodging="$500-1,500",
    daily="$700-1,800",
    neighborhoods=[
        stay_area("Mid-Beach", "Faena and Fontainebleau. A slightly wider beach and a short ride to South Beach when you want the noise."),
        stay_area("South Beach", "The Setai, on Collins, for people who want to walk out into the Art Deco grid and still sleep in a quiet luxury hotel."),
    ],
    hotels=[
        hotel("Faena Hotel Miami Beach", "Mid-Beach", "A theatrical oceanfront hotel with a gilded lobby and a real beach. Book an ocean-view room. Garden and courtyard categories miss the point. Often $700-1,800 in season. The pool is shared and very much a scene; the ocean is the morning.", "$700-1,800", "Miami Beach"),
        hotel("The Setai", "South Beach", "A quieter luxury hotel on Collins with an oceanfront position and a restrained pool deck. Ocean-view rooms are the ones that answer this search. Often $800-2,000 in winter. It is the choice if Fontainebleau feels too large.", "$800-2,000", "Miami Beach"),
        hotel("Fontainebleau Miami Beach", "Mid-Beach", "The oceanfront landmark. The campus is huge, the pools are a city, and only some rooms face the Atlantic. Book oceanfront or ocean view in the confirmation. A pool-view room looks at umbrellas. Often $400-1,200, with the ocean category at the top of that and well beyond on big weekends.", "$450-1,400", "Miami Beach"),
    ],
    itinerary=[
        day(1, "Confirm the window, then swim", "The view is either there or it is a front-desk conversation.", "Arrive and look out. Ocean, good. Pool deck or a wall, call while the bellman is still holding the bags. Then swim.", "The beach in front of the hotel, morning light or late light. Fontainebleau's grounds are large; give yourself time to find the sand.", "Dinner in the hotel the first night. Faena and The Setai are built for that. Fontainebleau has many tables; reserve the one you actually want.", "A luxury room that faces the wrong way is a completed mistake. Fix it on hour one.", "Miami Beach, Florida"),
        day(2, "The beach, then one cultural hour", "A soft day with one destination.", "Swim and breakfast on a terrace that faces the water. This is the meal the rate is for.", "The Bass Museum if you want art without a long ride, or the Pérez if you are willing to cross to the mainland. One museum.", "A reserved dinner, not a walk-in on Collins. The Setai and Faena reward staying in. Fontainebleau guests can do the same or go south for the evening.", "Chairs on the public beach are a few steps from a very expensive room. Use the hotel's setup.", "South Beach"),
        day(3, "Key Biscayne, because the room will still be there", "Even an oceanfront week needs one hour that is not a cabana.", "Morning car to Bill Baggs. Swim, walk to the lighthouse, come back after lunch.", "The hotel pool in the afternoon. At Fontainebleau this is a scene. At The Setai it is quieter. At Faena it is a costume. Choose with your eyes open.", "The expensive dinner. One of them. Stone crab at Joe's if it is October through May and you booked ahead. Out of season, do not invent a crab.", "Joe's is a South Beach institution and a wait. It is not a secret.", "Bill Baggs Cape Florida State Park"),
        day(4, "Ocean morning, airport afternoon", "The last swim is the itinerary.", "Breakfast, a swim, a slow pack.", "Rideshare to Miami International with a margin. Mid-Beach is not farther in a way that saves you from traffic.", "Eat at the hotel. You are past the point of optimizing.", "Check the folio for a resort fee. It will be there.", "Miami"),
    ],
    attractions=[
        sight("The Atlantic from the room", "The category you paid for. If you cannot see it, the rest of the list is a distraction.", "Settle it at check-in."),
        sight("Faena's beach", "Mid-Beach sand in front of a maximalist hotel.", "Morning swim, before the deck party."),
        sight("The Setai's oceanfront", "A calmer luxury frontage on South Beach.", "Use it twice a day. The neighborhood walk is optional."),
        sight("Fontainebleau oceanfront", "The big beach and the big pool. Specify which one your room sees.", "Pool-view is a fun room and the wrong booking."),
        sight("Bill Baggs and Cape Florida Light", "A lighthouse and a public beach on Key Biscayne. The hour away from the cabana.", "Go in the morning and be back for the pool.", "Cape Florida Light"),
        sight("The Bass Museum", "A small museum at the edge of the beach grid. The right size for this trip.", "An hour, then the ocean again."),
    ],
    scenic_routes=[
        route("Hotel beach at morning", "From the room to the sand and back before breakfast is over. Do it every day.", "Five minutes"),
        route("Collins walk", "A stretch of the avenue to see the scale of the beach hotels, then back to yours.", "A mile or two"),
        route("To Bill Baggs", "Rickenbacker Causeway to the park and the lighthouse.", "About half an hour from Mid-Beach"),
    ],
    transport="The hotel's door, your feet, and rideshares. A rental car in this part of Miami Beach is a parking problem. The causeway day is a round-trip ride. Airport transfers should be ordered, not hailed in a rainstorm under the porte-cochère with the rest of the checkout line.",
    food=[
        dish("Breakfast with the ocean in front of you", "The hotel", "Order it once without looking at the price, then decide if you want it every morning. Often the answer is yes."),
        dish("Stone crab", "Joe's Stone Crab, in season, roughly October to May", "The Miami Beach meal. It is expensive, it is a scene, and it is closed in summer. Book or go at an off hour."),
        dish("A simpler grilled fish", "The Setai, Faena, or a Fontainebleau restaurant", "The dinner when crab is out of season or you want to stay on the property."),
        dish("Cuban coffee", "A ventanita, once", "Walk to one so the trip includes one ordinary Miami habit. Then go back to the good breakfast."),
    ],
    tips=[
        "Oceanfront, ocean view, and partial ocean view are three prices. Read the verb on the confirmation.",
        "Fontainebleau's pool is not the ocean. If you wanted the pool party, book the pool view and stop calling it an ocean trip.",
        "Faena is a mood. The Setai is the quiet one. Choose before you are standing in a lobby that embarrasses you or bores you.",
        "Art Basel week and New Year's Eve rewrite the rates. The hotel will still be on the ocean. The invoice will not look like October.",
    ],
    faqs=[
        faq("Do all the rooms face the ocean?", "No. Each of these hotels has rooms that face the pool, the city, or a courtyard. The ocean category is a specific booking."),
        faq("Which hotel is the quiet one?", "The Setai. Faena is grander and louder in spirit. Fontainebleau is a city with a beach attached."),
        faq("Is Fontainebleau still the right luxury hotel?", "Yes, if you book the ocean and you do not mind the scale. A pool-view room at a famous name is a miss."),
        faq("What does it cost?", "Often $500-1,500 a night, with ocean categories and holiday weeks above that. Breakfast and one serious dinner can add $100-200 a person. Stone crab is not the budget valve."),
    ],
    map_places=[
        stop("Faena Hotel Miami Beach", "Miami Beach", "United States"),
        stop("The Setai", "Miami Beach", "United States"),
        stop("Fontainebleau Miami Beach", "Miami Beach", "United States"),
        stop("Bill Baggs Cape Florida State Park", "Key Biscayne", "United States", "Bill Baggs Cape Florida State Park"),
        stop("Joe's Stone Crab", "Miami Beach", "United States"),
    ],
    budget_notes="Budget $500-1,500 a night and then look again at the oceanfront column, which is the top of the range. Food and drinks at this tier are a daily $100-200 a person if you stay on property. A resort fee will appear. Key Biscayne is the cheap day. The expensive mistake is a non-ocean room at an ocean price because the photo was cropped.",
))

add(trip(
    slug="miami-pet-friendly",
    title="South Beach with a dog: three hotels that actually say yes",
    location="Miami, United States",
    summary=(
        "Four nights with a dog at a South Beach hotel that publishes a yes. 1 Hotel South Beach welcomes "
        "up to two dogs, each under 50 pounds, and does not add a pet fee. The Betsy allows dogs and cats, "
        "with no fee on a direct booking and a fee on third-party bookings. Kimpton Surfcomber does not "
        "charge a pet fee and does not set a weight limit. The swimming beach is not the dog's. Walk South "
        "Pointe Park in the morning, before the heat, and ask where dogs are actually allowed that week."
    ),
    who="A person and a dog who already travel together, and who will pay a cleaning fee if they break a rule.",
    best_time="November to April if the dog handles heat poorly, accepting higher hotel rates. Summer mornings are still usable if you walk at dawn and you are indoors by 10:30. Hurricane season is an animal-logistics problem as well as a weather one.",
    nights=4,
    hook="4 nights · Dogs welcome at three hotels · Not on the swimming beach",
    constraints=["Pet-friendly hotels with published rules", "Dogs off the swimming beach", "Morning walks before the heat"],
    lodging="$250-800",
    daily="$340-950",
    neighborhoods=[
        stay_area("South Beach", "1 Hotel, The Betsy, and the Surfcomber are all on Collins, a short walk from grass at South Pointe or from a sidewalk relief spot. The sand is the human swim."),
        stay_area("South Pointe Park", "The morning walk. Grass, a path, the ship channel. Confirm the current leash and dog rules; they are not the same as the hotel's."),
    ],
    hotels=[
        hotel("1 Hotel South Beach", "Collins Avenue", "A known dog hotel: up to two dogs, each under 50 pounds, no pet fee on the hotel's published policy, with beds and bowls. Dogs stay leashed, do not sit by the pool, and are not left loose in the room. The hotel itself says pets are not allowed on the beach. Often $400-900.", "$400-900", "Miami Beach", "https://www.1hotels.com/south-beach"),
        hotel("The Betsy", "Ocean Drive", "Dogs and cats are allowed. The hotel's own FAQ says there is no pet fee on a direct booking, and a fee of about $150 on a third-party booking. Book direct if the dog is coming. Ocean Drive is lively. Often $300-700, and higher in winter.", "$300-750", "Miami Beach", "https://www.thebetsyhotel.com/"),
        hotel("Kimpton Surfcomber Hotel", "Collins Avenue", "The Kimpton pet welcome, in the hotel's own words: no pet fee, no weight or breed limit, beds and bowls, a backyard relief area. It is between Collins and the beach. Often $250-550 outside peak weekends. The beach rule is still the city's, not the brand's.", "$250-600", "Miami Beach", "https://www.surfcomber.com/"),
    ],
    itinerary=[
        day(1, "Check the paws, then the park", "Arrive, drink water, walk before the pavement heats up.", "Hotel first. Collect the bowl and the rules. Walk South Pointe Park if the current rules allow dogs on the path you are on. If a sign says no, use the hotel's relief area and do not argue with the sign.", "The human swim is a handoff: one person on the beach, the dog in the room only if the hotel allows it, and not unattended unless crated. 1 Hotel's rule is strict about unattended pets.", "Dinner you can reach on foot, early. Patio seating is a question to ask, not a right.", "A 50-pound limit at 1 Hotel means 50 pounds. Weigh the dog before you fly.", "South Beach"),
        day(2, "Dawn walk, hot day indoors", "Miami heat is the constraint that is not in the pet fee.", "Walk at sunrise. Carry water. Paw-test the pavement with your hand.", "Midday in the room with the air on. A human can go to the beach. The dog cannot go to the pool or, under these hotels' guidance and local rules, onto the swimming beach.", "An early dinner. The Betsy's Ocean Drive block is busier; Surfcomber and 1 Hotel are a slightly easier exit.", "Do not leave the dog on a balcony. It is an old-hotel temptation and a bad idea.", "Miami Beach, Florida"),
        day(3, "A people outing with a plan", "The dog needs a legal hour, not a parked-car hour.", "If both of you want Bill Baggs or a museum, use a sitter or a daycare you have booked, or go one at a time. A dog does not wait in the car, and a dog does not enter the lighthouse.", "The other half of the day is the park walk and the room. That is a full dog day. It does not need a second attraction.", "Dinner with a patio if the restaurant confirms dogs, or room service if it does not. Many places will say no.", "South Pointe in the morning is the outing that does not require a strategy. Repeat it."),
        day(4, "One more dawn, then the airport", "The flight home has crate rules and a temperature embargo. Check them.", "Walk. Pack the bowl. Ask the hotel if anything was damaged before you discover it on the folio in the car.", "Rideshare or a car that you know accepts the dog. Not every driver does. The airport is 30 to 50 minutes.", "Eat. Give the dog water. The rest is a terminal.", "A third-party booking at The Betsy may have added the pet fee you thought you had avoided. Direct means direct.", "Miami"),
    ],
    attractions=[
        sight("South Pointe Park", "The grassy south tip of Miami Beach. The morning dog walk if the posted rules allow it.", "Dawn. Water. A leash. Leave if the sign says to."),
        sight("1 Hotel's dog setup", "Beds, bowls, and a staff that expects dogs. The most deliberate of the three welcomes.", "Under 50 pounds, two dogs maximum, no beach, no pool."),
        sight("The Betsy", "An Ocean Drive hotel that will take the dog, especially if you booked with the hotel.", "Direct booking is how you avoid the pet fee."),
        sight("Surfcomber's backyard relief area", "An actual patch of the hotel for the dog, which solves the 11 p.m. problem.", "Use it. The beach is not the backup."),
        sight("The swimming beach", "For people. The hotels and local rules keep dogs off the sand.", "Take turns. Do not try to be the exception at 8 a.m."),
        sight("A human hour at the Bass or a café", "The part of the trip that is still a trip.", "Only with a crate plan or a second person."),
    ],
    scenic_routes=[
        route("Dawn loop to South Pointe", "Hotel to the park and back before the pavement is hot. The daily route.", "15 to 30 minutes"),
        route("Collins in the early morning", "A longer sidewalk walk if the park is closed to dogs that day.", "Under a mile"),
        route("To the airport with the dog", "A pre-booked car, water, and a crate if the airline wants one.", "30 to 50 minutes"),
    ],
    transport="Walk. Rideshares are inconsistent about dogs; a booked car or a pet-friendly taxi is the airport plan. Do not rent a car and then wonder what to do with the dog at a garage. The beach is close enough that one person can swim while the other stays in reach of the room.",
    food=[
        dish("Breakfast from a ventanita, eaten outside or back in the room", "A walkable Cuban counter", "Coffee for you, water for the dog, something bread-based. The easiest morning."),
        dish("An early patio dinner", "A restaurant that confirms dogs on the patio", "Call. A bowl of water and a seat outside is the meal. If they say no, believe them."),
        dish("Room service", "1 Hotel, The Betsy, or the Surfcomber", "The no-strategy dinner. Use it once without guilt."),
        dish("Picnic after the dawn walk", "Bought the evening before", "Fruit and a sandwich in the park, if food is allowed where you are sitting. Then go inside."),
    ],
    tips=[
        "1 Hotel: under 50 pounds, two dogs, no fee, no beach. The Betsy: book direct to avoid the pet fee. Surfcomber: no fee and no weight cap on the hotel's own page.",
        "The swimming beach is not a dog beach. South Pointe's paths are the walk, if signs allow.",
        "Walk at dawn. Midday sidewalks burn paws and the humidity is the other hazard.",
        "A pet fee you were not told about is still cheaper than a ruined trip. Read the booking channel. Third-party rates are where The Betsy's fee appears.",
    ],
    faqs=[
        faq("Which hotels take dogs?", "1 Hotel South Beach, up to two dogs under 50 pounds each, no pet fee. The Betsy, dogs and cats, no fee if you book direct. Kimpton Surfcomber, no fee and no published weight limit. Policies change; re-read them when you book."),
        faq("Can the dog go on the beach?", "No. 1 Hotel cites the rule against pets on the beach, and the safe plan at all three is to keep the dog off the swimming sand. Use South Pointe Park in the morning if dogs are allowed there, and the hotel relief area if they are not."),
        faq("Is there a fee?", "Not at 1 Hotel or the Surfcomber on their published policies. At The Betsy, not on a direct booking; about $150 if you booked through a third party. Damage and deep cleaning can still be charged."),
        faq("What about the heat?", "Walk before it is hot, carry water, and never leave the dog in a car or on a balcony. Summer is an early-morning trip with a long air-conditioned middle."),
    ],
    map_places=[
        stop("1 Hotel South Beach", "Miami Beach", "United States"),
        stop("The Betsy Hotel", "Miami Beach", "United States"),
        stop("Kimpton Surfcomber", "Miami Beach", "United States"),
        stop("South Pointe Park", "Miami Beach", "United States"),
        stop("South Beach", "Miami Beach", "United States", "South Beach"),
    ],
    budget_notes="Rooms often run $250-800, more at 1 Hotel in winter. The pet fee is $0 at 1 Hotel and the Surfcomber on their current published rules, and $0 at The Betsy only when you book direct. Food is ordinary South Beach pricing plus the occasional room-service night. A dog daycare, if you want a full human day, is the extra line. The beach chair is the one thing you are not buying for the dog.",
))

add(trip(
    slug="miami-mountain-or-nature-view",
    title="Miami has no mountains: the Everglades, Cape Florida, and a Coconut Grove bed",
    location="Miami, United States",
    summary=(
        "Four nights based in Coconut Grove, because Miami does not have a mountain view and will not grow "
        "one for the search. The nature is the Everglades' Anhinga Trail, the lighthouse and beach at Bill "
        "Baggs on Key Biscayne, and a kayak morning at Oleta River. Mayfair House and Mr. C are in the Grove, "
        "which shortens the drive to the causeway and to Vizcaya. Four Seasons Hotel Miami is a Brickell "
        "tower with a bay and a skyline, included so nobody pretends a high floor is a ridge. Sleep here, "
        "and go to the wetland in the morning."
    ),
    who="Someone who asked for a mountain or a nature view in Miami and deserves the real landscape instead of a fake vista.",
    best_time="December to April, when mosquitoes and afternoon storms are lighter and the glades are drier. Summer nature days start at dawn and end by noon. There is no season in which a mountain appears.",
    nights=4,
    hook="4 nights · No mountains · Everglades, Cape Florida, Oleta",
    constraints=["No mountain view", "Nature days from Coconut Grove", "Honest hotels"],
    lodging="$220-550",
    daily="$320-650",
    neighborhoods=[
        stay_area("Coconut Grove", "Old trees, a bay, Vizcaya, and a short ride to the Rickenbacker Causeway. The right base for Key Biscayne and a tolerable drive toward the Everglades."),
        stay_area("Brickell", "Four Seasons Hotel Miami, if you want a famous tower. The view is water and buildings. The national park is still a drive."),
    ],
    hotels=[
        hotel("Mayfair House Hotel & Garden", "Coconut Grove", "A Grove hotel built around a garden courtyard. You can walk to dinner and reach Bill Baggs in about 20 minutes. The view is leaves and the neighborhood, not a peak. Often $250-500. Useful, and on the correct side of the bay for the nature days.", "$250-500", "Miami", "https://www.mayfairhousemiami.com/"),
        hotel("Mr. C Miami Coconut Grove", "Coconut Grove", "A smaller luxury hotel in the Grove, with bay-side energy rather than a wilderness lodge. It puts Vizcaya, the causeway, and dinner in the same evening. Often $300-600. Book it for the location, then leave it in the morning for the park.", "$300-600", "Miami"),
        hotel("Four Seasons Hotel Miami", "Brickell", "A high-rise downtown hotel. Upper floors look at the bay and the city. They do not look at mountains, because there are none. It is the famous hotel on this list, and it adds ten or fifteen minutes to the nature drives. Often $400-800.", "$400-800", "Miami"),
    ],
    itinerary=[
        day(1, "The Grove, and a garden", "Arrive and do the nearest nature, which is Vizcaya's garden, not a summit.", "Check in. Walk the Grove's sidewalks so you know where dinner is.", "Vizcaya Museum and Gardens, an hour or two. Bay, villa, and trees. This is the closest thing to a view, and it is a garden.", "Dinner in the Grove. Coconut Grove is a neighborhood; use it. Brickell guests can come over or stay by the river.", "There is no scenic overlook to reschedule. The itinerary does not contain one."),
        day(2, "Everglades, early", "Anhinga Trail at Royal Palm, inside Everglades National Park, via the Ernest Coe entrance near Homestead. About 45 to 75 minutes from the Grove.", "Leave by 7:30. Tram or walk the Anhinga Trail and see alligators from the boardwalk without approaching them. Mosquitoes are part of the park. Bring repellent and more water than you think.", "Be out of the main walking by lunch. A short extra trail if you are fine, then the drive back. An airboat ride on the park's edge is a loud, separate product; the boardwalk is the quieter one.", "An early dinner. You got up early. The city at night is optional.", "Do not bring a dog on the Anhinga boardwalk. This is not the pet page, and the wildlife is the point.", "Everglades National Park"),
        day(3, "Bill Baggs and the lighthouse", "Key Biscayne is the easy nature day, and the Grove is the right hotel for it.", "Over the Rickenbacker Causeway to Bill Baggs Cape Florida State Park. Swim, then walk to the Cape Florida lighthouse. The beach is a barrier-island beach, not a mountain lake.", "Back after lunch. A second swim or a hammock hour. Oleta can be tomorrow's morning if you still want mangroves; do not stack it today.", "Dinner in the Grove again, or a casual place on Key Biscayne before you recross the causeway.", "The toll and the parking are the logistics. The lighthouse is the picture.", "Bill Baggs Cape Florida State Park"),
        day(4, "Oleta, or a last bay walk, then the airport", "Oleta River State Park is in North Miami Beach: mangroves and a kayak, about 30 to 45 minutes north. If the flight is early, replace it with a Grove waterfront walk.", "A morning kayak or a shoreline walk at Oleta if the flight allows. Rent from the park concession and stay in the marked water. If you fly at midday, skip it and walk the Grove.", "Airport with a margin. Brickell and the Grove are both straightforward and both capable of traffic.", "Eat first. A nature morning without lunch is how the airport becomes dinner.", "You will not see the trip's best hour from the Four Seasons window. You will see a handsome bay. Both things can be true.", "Oleta River State Park"),
    ],
    attractions=[
        sight("Anhinga Trail", "A boardwalk over the sawgrass and the slough, with alligators and wading birds at close range.", "Go early. Do not feed or approach anything. The animals are not a show.", "Everglades National Park"),
        sight("Everglades National Park", "The river of grass at the edge of the metro area. The nature this city actually has.", "Ernest Coe entrance, Royal Palm, then leave before the thunderstorm or the boredom, whichever comes first.", "Everglades National Park"),
        sight("Bill Baggs Cape Florida State Park", "Beach, shade, and a lighthouse at the end of Key Biscayne.", "Swim in the morning. The causeway is the approach.", "Bill Baggs Cape Florida State Park"),
        sight("Cape Florida Light", "The old lighthouse at the park. Climb only if it is open that day.", "If the tower is closed, the ground and the beach still count.", "Cape Florida Light"),
        sight("Oleta River State Park", "Mangrove kayaking on the north side of the bay. A different ecosystem from the glades boardwalk.", "A morning rental. Do not plan it after a late Everglades return.", "Oleta River State Park"),
        sight("Vizcaya Museum and Gardens", "The formal version of Miami nature: a garden on the bay.", "The first afternoon, so the park days stay wilder.", "Vizcaya Museum and Gardens"),
    ],
    scenic_routes=[
        route("Grove to the Anhinga Trail", "South to Homestead and the Ernest Coe entrance, early, then the boardwalk.", "45 to 75 minutes each way"),
        route("Rickenbacker to Cape Florida", "The causeway to Bill Baggs. Water on both sides, a toll, a lighthouse at the end.", "About 20 minutes from the Grove"),
        route("Up to Oleta River", "A morning drive north to the mangrove park and a kayak loop.", "30 to 45 minutes"),
    ],
    transport="A rental car. The Grove is walkable at night and useless for the Everglades without a car. Key Biscayne is a rideshare if you only do that one day, and a car if you are doing the glades too. Four Seasons guests in Brickell add a little time and lose the ability to walk to Vizcaya as easily. Start the Everglades day with a full tank and offline directions; the park does not care about your map app.",
    food=[
        dish("Cuban coffee and eggs in the Grove", "A Grove café or bakery", "The breakfast before a park day. Eat more than a pastry if you are going to the glades."),
        dish("A packed Everglades lunch", "Bought the night before", "Sandwiches, fruit, and more water than a city walk requires. The Coe entrance is not a food hall."),
        dish("Key Biscayne lunch", "A casual place after Bill Baggs, or the picnic you brought", "Eat near the park so the drive home is not hungry and traffic-bound."),
        dish("Grove dinner", "A neighborhood restaurant you can walk to from Mayfair House or Mr. C", "The reward for a 7:30 a.m. alligator walk. Brickell has the flashier version and the worse drive home."),
    ],
    tips=[
        "There is no mountain view. A high hotel floor is a bay view. Book the floor if you want the bay, and book the parks if you want nature.",
        "Anhinga Trail in the middle of a summer day is mosquitoes and glare. Go early all year, and go in the dry season if you can.",
        "Alligators on the boardwalk are normal. They are not an invitation. Stay on the path.",
        "Coconut Grove is the base because Key Biscayne and Vizcaya are close. The Everglades are still a drive. That is the geography.",
    ],
    faqs=[
        faq("Where is the mountain view?", "There isn't one. Miami's nature is the Everglades, the mangrove coast at Oleta, and the barrier island at Cape Florida. The hotels look at gardens, the bay, or the skyline."),
        faq("Why Coconut Grove?", "It sits next to Vizcaya and the causeway to Key Biscayne, and the drive to the main Everglades entrance is straightforward. A South Beach hotel makes every one of those days longer."),
        faq("Is an airboat the Everglades?", "It is a loud ride, usually outside the quiet part of the national park. The Anhinga Trail is the version that belongs in this trip. Take an airboat only if you know you want the noise."),
        faq("Does the Four Seasons fix the view?", "It fixes nothing about mountains. It is a fine Brickell hotel with a bay and city outlook, and a slightly worse starting point for the parks."),
    ],
    map_places=[
        stop("Anhinga Trail", "Homestead", "United States", "Everglades National Park"),
        stop("Bill Baggs Cape Florida State Park", "Key Biscayne", "United States", "Bill Baggs Cape Florida State Park"),
        stop("Oleta River State Park", "North Miami Beach", "United States", "Oleta River State Park"),
        stop("Vizcaya Museum and Gardens", "Miami", "United States", "Vizcaya Museum and Gardens"),
        stop("Mayfair House Hotel & Garden", "Coconut Grove", "United States"),
    ],
    budget_notes="Grove hotels often run $250-600. The Four Seasons runs higher for a view of the bay. Park entries are modest next to the room: budget the car, the causeway toll, and a kayak rental. Food stays reasonable if the Everglades lunch is packed and dinner is in the Grove. No tour needs to sell you a mountain overlook. If someone does, they are describing a different state.",
))

add(trip(
    slug="singapore-near-the-beach-under-300",
    title="A Singapore beach day under $300, on a coast the city built",
    location="Singapore",
    summary=(
        "Four nights in Singapore with one real aim: a swim that does not require pretending Marina Bay "
        "is a beach. Sentosa's Siloso, Palawan, and Tanjong beaches are constructed and groomed, with sand "
        "brought in and a lagoon kept for swimming. Shangri-La Rasa Sentosa is the hotel on that sand, and "
        "early-bird weekdays have been advertised around $230-270, so under $300 is possible and a weekend "
        "or the Formula 1 period often is not. Village Hotel Sentosa and Village Hotel Changi are the "
        "more reliable under-$300 beds. Marina Bay Sands will not fit this cap."
    ),
    who="A couple or a small family who want a beach hour inside a city trip, and who know the beach was built.",
    best_time="Weekdays outside the June and December school holidays and outside the Formula 1 race, usually in September. Those weeks push even the mid-range hotels over $300. The sea is warm all year. Rain is a daily possibility, not a season you can fully dodge.",
    nights=4,
    hook="4 nights · Built beach, real swim · Under $300 if you avoid race week",
    constraints=["Under $300 a night", "A beach day", "Sentosa is a constructed beach", "Marina Bay Sands does not fit"],
    lodging="$140-300",
    daily="$220-380",
    neighborhoods=[
        stay_area("Sentosa", "The island with the constructed beaches. Rasa Sentosa is on Siloso. Village Hotel Sentosa is a walk of about ten minutes from Palawan, not on the sand. You pay a train or cable-car fare to get on and off."),
        stay_area("Changi and the East Coast", "Village Hotel Changi is the practical under-$300 base near Changi Beach and the airport. East Coast Park is the city's long reclaimed shoreline: bikes, hawker food, and a swim that feels like a park."),
    ],
    hotels=[
        hotel("Shangri-La Rasa Sentosa, Singapore", "Siloso Beach, Sentosa", "The city's actual beachfront resort, on the western end of Siloso. The beach in front of it is a maintained public beach, not a wild coast. Early-bird rates have been listed around $230-270 before taxes. Weekends, school holidays, and the F1 period often clear $300, so this hotel fits the cap only on the right dates. Ask for a sea-facing room if the sand is the reason.", "$230-450", "Singapore", "https://www.shangri-la.com/singapore/rasasentosaresort/"),
        hotel("Village Hotel Sentosa", "Sentosa", "A mid-range hotel on the island, about ten minutes on foot from Palawan Beach. This is the Sentosa stay that more often remains under $300 when Rasa's sea-view room does not. You are near a constructed beach, not in a tower on the sand. Useful for families and for anyone who wants the island without the resort rate.", "$160-280", "Singapore"),
        hotel("Village Hotel Changi", "Changi", "Near the airport and a short ride from Changi Beach, which is a quieter, less staged shore than Sentosa. Rates often sit under $200. The city is a train ride, not a walk. Book it if the cap is firm and you are willing to swim at a neighborhood beach instead of a resort one.", "$120-220", "Singapore"),
    ],
    itinerary=[
        day(1, "The constructed beach, on purpose", "Arrive and go to the sand you came for. Name it honestly when you get there.", "If you are on Sentosa, check in and walk to Siloso or Palawan. The sand is soft because it is maintained. The swim is real. If you are in Changi, drop bags and go to Changi Beach or, if you still want the postcard, take the train and the Sentosa Express across.", "Swim, then a walk along the beach you picked. Siloso is the busiest, Tanjong the quietest, Palawan the family middle. They connect.", "Dinner at East Coast Lagoon Food Village if you can face the ride, or a simpler meal on Sentosa if you cannot. The hawker centre is the better plate.", "Sentosa's beaches can close for weather or events. Have the East Coast as the backup swim.", "Sentosa"),
        day(2, "The city, with the bay as a view and not a beach", "Marina Bay is a reservoir edge. Look at it. Do not pack a towel for it.", "Gardens by the Bay in the morning, before the heat. The domes cost money; the outdoor gardens are already a lot.", "A look at Marina Bay Sands from the promenade. You are not staying there on this budget, and the rooftop is a separate ticket if you want the view. Chinatown or Kampong Glam for a walk afterward.", "Hawker dinner: Maxwell or a Chinatown centre. Chicken rice, a vegetable dish, and something spicy if you want it.", "The MRT is the tool. A taxi to every sight will spend the money you saved on the room.", "Gardens by the Bay"),
        day(3, "East Coast or a rougher island", "Choose a second kind of shore.", "East Coast Park: rent a bike, ride, swim if the water looks decent to you, and eat at the hawker centre on the lagoon. This shoreline is reclaimed parkland. It is the city's everyday beach.", "Or, if you want something less groomed, a bumboat from Changi Point to Pulau Ubin for a few hours of village paths and bikes. This is the better add-on if you slept in Changi.", "Dinner in Katong or at the East Coast stalls. Chili crab is a special meal, messy and priced like one, for two people sharing.", "Pulau Ubin's last boats are a real constraint. Leave the island in daylight.", "East Coast Park"),
        day(4, "A garden morning, then the airport", "Changi is an easy airport if you are already in the east, and a planned ride if you are on Sentosa.", "Singapore Botanic Gardens for a walk if the flight is later. The garden is free outdoors and it is the calmest nature in the center.", "Sentosa guests should leave longer than the map suggests. The island exit plus traffic can eat an hour you thought was twenty minutes. Changi hotel guests have the rare luxury of a short airport run.", "Eat a last hawker meal or a proper breakfast. The airport is good and you do not have to save your appetite for it.", "A sea-view room at Rasa that came in over $300 was the signal to switch to Village or to Changi, not to ignore the cap.", "Singapore Botanic Gardens"),
    ],
    attractions=[
        sight("Siloso Beach", "The lively constructed beach on Sentosa, with Rasa Sentosa at the western end.", "Swim in the roped area. The sand is maintained, and the water is a lagoon edge, not an open wild coast.", "Sentosa"),
        sight("Palawan and Tanjong Beaches", "The other two Sentosa beaches. Palawan is the family one; Tanjong is quieter.", "Walk or take the beach tram between them rather than booking three experiences.", "Sentosa"),
        sight("East Coast Park", "A long reclaimed park with a beach, a bike path, and a hawker centre. The local version of a beach day.", "Go on a weekday if you can. Weekends are a city outing.", "East Coast Park"),
        sight("Changi Beach", "The quieter northeast beach near the airport hotel. Less famous, more neighborhood.", "A morning swim if you stayed at Village Hotel Changi."),
        sight("Gardens by the Bay", "The city garden. Worth a morning, and not a substitute for the beach.", "Outdoor portions first. The domes if you still have curiosity and money.", "Gardens by the Bay"),
        sight("Pulau Ubin", "A small island with a village, bikes, and mangrove. The least polished nature on this list.", "Bumboat from Changi Point, and back before the last boat.", "Pulau Ubin"),
    ],
    scenic_routes=[
        route("The three Sentosa beaches", "Siloso to Palawan to Tanjong on foot or the free beach connection. Constructed shoreline the whole way.", "About 2 km of beach"),
        route("East Coast Park by bike", "A rented bike on the park path, a swim, and a stop at the hawker centre.", "As far as you feel like, for an hour or three"),
        route("Bumboat to Pulau Ubin", "From Changi Point, a short boat, a bike on the island, and the same boat back.", "A half day"),
    ],
    transport="The MRT, the Sentosa Express or cable car, and a taxi when you are sandy and tired. You do not need a car. Sentosa charges a way on and off; budget the train or the cable car rather than being surprised. Changi Airport to Village Hotel Changi is the easy arrival. Sentosa to the airport on the last day needs a longer margin than people who live downtown expect. East Coast Park is a bus or a short taxi from the city, and a longer ride from Sentosa.",
    food=[
        dish("Chicken rice", "Maxwell Food Centre or another hawker centre", "The plate to eat once, at a busy stall. Go at lunch, when the chicken is at its best."),
        dish("Chili crab or black pepper crab", "A seafood restaurant, shared by two", "The special meal. One crab, buns to wipe the sauce, and a bill that looks like a hotel extra. Worth doing, not worth doing twice."),
        dish("East Coast hawker food", "East Coast Lagoon Food Village", "Satay, barbecue, and a cold drink after the bike. The correct lunch for that beach."),
        dish("Kaya toast and coffee", "A kopitiam or a Ya Kun", "Breakfast. Coconut jam, butter, and strong coffee. Then go to the beach before the heat."),
    ],
    tips=[
        "Say the sentence: Sentosa's beach is constructed. It is still a pleasant swim. East Coast Park is reclaimed park shoreline. Changi Beach is the quieter local option.",
        "Marina Bay Sands is the famous hotel that does not fit under $300. Look at it from the promenade.",
        "Rasa Sentosa fits the cap on early-bird weekdays and often misses it on weekends, school holidays, and race week.",
        "A beach-only Singapore trip is thin. The beach day works because the other days are hawker food, a garden, and a neighborhood.",
    ],
    faqs=[
        faq("Is there a real beach?", "Yes, with a caveat. Sentosa's three beaches are built and groomed for swimming. East Coast Park is a reclaimed city shoreline. Changi Beach is a simpler neighborhood beach. None of them is a deserted cape."),
        faq("Can the hotel be under $300?", "Village Hotel Changi usually, Village Hotel Sentosa often, and Shangri-La Rasa Sentosa on the right weekday with an early rate. Marina Bay Sands no. The F1 period and school holidays are when the cap fails."),
        faq("Do I stay on Sentosa the whole time?", "You can, and you will want one day off it for hawker food and the central city. Sentosa is a playground attached to a city, not the whole city."),
        faq("Is the water swimmable?", "In the designated areas, yes. It is warm, it is not a clear tropical bay in the postcard sense, and it is monitored. If a beach is closed, use the other one."),
    ],
    map_places=[
        stop("Siloso Beach", "Sentosa", "Singapore", "Sentosa"),
        stop("East Coast Park", "Singapore", "Singapore", "East Coast Park"),
        stop("Gardens by the Bay", "Singapore", "Singapore", "Gardens by the Bay"),
        stop("Pulau Ubin", "Singapore", "Singapore", "Pulau Ubin"),
        stop("Changi Beach", "Singapore", "Singapore"),
    ],
    budget_notes="Village Hotel Changi often holds $120-220. Village Hotel Sentosa often holds $160-280. Rasa Sentosa can dip under $300 on early-bird weekdays and will not on a race weekend or a holiday. Hawker meals keep food near $25-40 a day; chili crab is the $60-100 exception for two. Add the Sentosa train or cable car and the MRT. Marina Bay Sands is the reminder that the famous waterfront hotel is a different budget.",
))


