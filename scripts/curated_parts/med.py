"""Amsterdam nature and pools, the Adriatic, the Cyclades, and Reykjavík."""
from _common import trip, hotel, stay_area, day, sight, route, dish, faq, stop

# Uncertainties worth a second look:
# - Pillows Maurits at the Park is Mauritskade 61 by Oosterpark, not Vondelpark.
# - No second private pool in Amsterdam. Conservatorium and the Waldorf Guerlain
#   pool are shared. Only Hotel Akersloot's suite pool is described as private.
# - City Walls Hostel may now be dorms only. The copy says to confirm a private room.
# - Celenga's low published from-price is not an August rate.
# - Villa Renos lists a 100 m2 Grand Suite, not two closed bedrooms. Confirm the plan.
# - Astivi is a Pyrgos apartment listing, thinner than Kastro Mansion's own site.
# - Antonia and Kavalari were not used as two-bedrooms.
# - Ethos and Cally say pets are allowed and print no weight or fee. NOŪS states
#   one pet, 10 kg, about €50. All three still need a written yes.
# - Kivotos and Mykonos Ammos show "pets on request" on Booking.com only.
#   Santa Marina's 10 kg cap is on the Marriott page. No Chora hotel was given a yes.
# - Mykonian Breeze's two-bedroom size comes from a listing, not a rate card.
# - Narkissos teaser rates were ignored. Daedalus's booking engine showed a 2027
#   season window; the hotel is treated as a normal spring-to-autumn operation.
# - Red Beach access and any dog beach were left unnamed on purpose.
# - Ion Adventure Hotel and the Retreat are mentioned and are not the three hotels.
# - Zorzis was skipped; its site said the Mykonos hotel had paused.

TRIPS = []


def add(record):
    TRIPS.append(record)


add(trip(
    slug="amsterdam-mountain-or-nature-view",
    title="Amsterdam has no mountain: a park, a polder, and one dune day",
    location="Amsterdam, Netherlands",
    summary=(
        "There is no mountain in Amsterdam, and no hotel balcony fixes that. The honest nature from the city is "
        "Vondelpark, the Amsterdamse Bos with its small man-made hill, a bike through the Waterland polders, and "
        "one day either at Zaanse Schans or in the Kennemer dunes above Bloemendaal. Keukenhof is a bulb garden "
        "and only open for about eight weeks in spring."
    ),
    who="Walkers and moderate cyclists who searched for a view and will take grass, water, and a wide sky instead.",
    best_time="May, June, and September. The dunes and the Bos are pleasant in July. Keukenhof runs roughly mid-March to mid-May and is closed the rest of the year.",
    nights=4,
    hook="4 nights · Parks and polders · $150–320/night",
    constraints=["No mountains", "One bike day outside the canal belt", "Keukenhof only if it is open"],
    lodging="$150–320",
    daily="$220–340",
    neighborhoods=[
        stay_area("Vondelpark edge", "The park is the reason to be on this side of the city. Museumplein is a short walk. The canal ring is a tram, not the point of the stay."),
        stay_area("Oosterpark, if you book the wrong 'park' hotel", "Pillows Maurits at the Park faces Oosterpark on the Mauritskade. It is green, and it is not Vondelpark."),
    ],
    hotels=[
        hotel("Hotel Vondel", "Vondelstraat", "A long-running hotel on Vondelstraat, actually beside Vondelpark. This is the straightforward base for the park mornings.", "$170–320", "Amsterdam"),
        hotel("Conscious Hotel Vondelpark", "Overtoom", "On the Overtoom, along the west side of Vondelpark. Smaller and plainer than a palace hotel, and the location matches the trip.", "$140–260", "Amsterdam"),
        hotel("Pillows Maurits at the Park", "Mauritskade, Oosterpark", "The hotel's own site puts Pillows Grand Boutique Hotel Maurits at the Park at Mauritskade 61, beside Oosterpark, not Vondelpark. Book it for a quiet east-side stay and a tram to the Bos. Do not book it expecting to step into Vondelpark.", "$280–520", "Amsterdam"),
    ],
    itinerary=[
        day(1, "Vondelpark, and that is the view", "Arrive and use the park as the city, not as a shortcut between museums.", "Drop bags at a Vondelpark hotel. Walk the park from the Van Baerlestraat end toward the rose garden, away from the loudest entrance.", "The open grass and the ponds are the sight. One museum on Museumplein only if you still want a building after the flight. Skip stacking the Rijksmuseum and the Van Gogh.", "Dinner on the Overtoom or a short tram south. The evening is a park loop in the last light, not a canal-belt crawl.", "The park is busy on the first warm Saturday. A weekday morning is the better version.", "Vondelpark"),
        day(2, "The Amsterdamse Bos, including the only hill", "A large planted forest south of the city. The hill in it is man-made and small, and it is still the summit.", "Rent a bike, or take the bus, to the Amsterdamse Bos. Ride as far as the Bosbaan rowing course so you see water and trees, not only the entrance.", "Climb the little hill. Visit the goat farm if you like animals. Eat pancakes at Boerderij Meerzicht, which is the honest lunch in this park.", "Back to Vondelpark before dark. Your legs will notice the Bos more than a museum day.", "Wind across the Bos is the weather. A city bike with a basket is enough. A racing bike is not required.", "Amsterdamse Bos"),
        day(3, "Waterland on a bike", "Flat polder north of the IJ: ditches, cows, and church villages. This is the right place for a visitor to ride. The inner canal belt is not.", "Take the free ferry behind Centraal to Buiksloterweg and rent a bike on the north side, or bring the bike across. Ride toward Nieuwendam and out through the polder.", "Broek in Waterland, then Holysloot or Ransdorp. Wooden houses, a small church, and a horizon. Turn around while you still like the saddle.", "Dinner back in the city. You will not find a mountain restaurant out there, and you should not try to invent one.", "About 30 km is a half day for someone who rides at home. If you do not, take an e-bike or the bus to Broek in Waterland and walk the village.", ""),
        day(4, "Dunes, or windmills if the sky is low", "One trip out of town. The dunes are the nature. Zaanse Schans is the backup when you want wooden houses instead of sand.", "Train toward Overveen, then walk or take the bus into the Kennemer dunes. The national park behind Bloemendaal aan Zee is heath, pine, and sand, with the North Sea at the bottom.", "Walk to the beach if the wind is kind, then back. If the forecast is rain, swap the whole day for Zaanse Schans: train to Koog-Zaandijk, early, and leave before it becomes a queue of photos.", "Train back to Centraal and on to Schiphol when you are done. Eat before the airport.", "Do not try to add Keukenhof unless your dates fall in its short spring season. Lisse is a third direction.", ""),
    ],
    attractions=[
        sight("Vondelpark", "The city's everyday park, large enough to spend a morning without a ticket.", "Enter away from Leidseplein if you want the quieter paths and the rose garden.", "Vondelpark"),
        sight("Amsterdamse Bos", "A thousand-hectare planted forest with a rowing lake, a goat farm, and one small hill.", "The hill is the mountain joke. Go up it, then keep riding. The forest is the point.", "Amsterdamse Bos"),
        sight("Zaanse Schans", "Windmills and wooden houses northwest of the city. A sight, not a wilderness.", "Go at opening. Midday is tour buses. It is a fair substitute for the dunes in bad weather, not a second mountain.", "Zaanse Schans"),
        sight("Kennemerduinen", "Coastal dunes at Bloemendaal, in Zuid-Kennemerland. Pine, sand, and a real beach below.", "Wear shoes you can get sand in. The paths are soft and the last stretch to the sea is open wind.", ""),
        sight("Waterland", "Polder villages north of Amsterdam: Broek in Waterland, Holysloot, Ransdorp.", "This is a bike ride or a bus, not a stroll from Dam Square. The horizon is the view.", ""),
        sight("Keukenhof", "A designed bulb garden in Lisse, not a peak. Extraordinary when it is open, and shut for most of the year.", "Check the year's dates before you promise anyone tulips. Outside those weeks, do not go.", "Keukenhof"),
    ],
    scenic_routes=[
        route("Waterland polder loop", "Free ferry to Buiksloterweg, then bike lanes through the polder to Broek in Waterland and Holysloot or Ransdorp, and back. Ditches and villages the whole way.", "About 30 km, half a day"),
        route("Overveen to the Kennemer dunes", "Train from Centraal toward Overveen, then on foot into the dunes and down to Bloemendaal aan Zee if you want the sea. Return the same way.", "30–40 minutes by train, then 8–12 km of walking"),
        route("Train to Zaanse Schans", "Centraal to Koog-Zaandijk, then a short walk to the mills. Use this instead of the dunes, not on top of them, if the day is wet.", "About 20 minutes by train, plus the walk"),
    ],
    transport="Trains and bikes do this trip. A car is a burden in the center and only mildly useful for the dunes. The Waterland ride starts with the free IJ ferry, not with a bike on the Singel. Schiphol is a direct train from Centraal. Keukenhof, when open, is a train toward Leiden or Haarlem and a shuttle, a separate half day.",
    food=[
        dish("Pannenkoeken", "Boerderij Meerzicht in the Amsterdamse Bos", "The pancake farm in the park. Lunch, not a gastronomic evening. Go after the hill, not instead of the ride."),
        dish("Broodjes and cheese", "A market or a supermarket, eaten in Vondelpark", "The park lunch that works: bread, young cheese, fruit. The cafés on the main path are for coffee when it rains."),
        dish("Apple pie and coffee", "A café in Broek in Waterland", "You earn it by riding there. It is a village stop, not a tasting menu."),
        dish("Kibbeling", "A stall at Bloemendaal aan Zee, if you do the dune day", "Fried fish pieces by the beach. Fine when you are sandy. Skip it if you swapped the day for windmills."),
    ],
    tips=[
        "The Bos hill is the only summit. Anyone selling an Amsterdam mountain view is selling a metaphor.",
        "Ride in Waterland. Leave the rental bike off the inner canal ring, where you will be in everyone's way.",
        "Keukenhof dates are short. If the garden is closed, the dunes are still there.",
        "Pillows Maurits at the Park is a real hotel by a real park. The park is Oosterpark.",
    ],
    faqs=[
        faq("Is there a viewpoint that feels like a mountain?", "No. The Amsterdamse Bos hill is a short climb over trees. The dunes at Bloemendaal are higher than the city and still not alpine. Go for the horizon."),
        faq("Can I do this without a bike?", "The parks and the dunes, yes. Waterland without a bike is one village by bus, which is pleasant and much smaller than the ride."),
        faq("Is Zaanse Schans nature?", "It is historic mills in a landscape. Worth a morning. It is not a national park, and it is crowded from late morning."),
        faq("Which hotel is actually next to Vondelpark?", "Hotel Vondel on Vondelstraat, and Conscious Hotel Vondelpark on the Overtoom. Pillows Maurits at the Park is by Oosterpark."),
    ],
    map_places=[
        stop("Vondelpark", "Amsterdam", "Netherlands", "Vondelpark"),
        stop("Amsterdamse Bos", "Amstelveen", "Netherlands", "Amsterdamse Bos"),
        stop("Broek in Waterland", "Waterland", "Netherlands", ""),
        stop("Zaanse Schans", "Zaandam", "Netherlands", "Zaanse Schans"),
        stop("Bloemendaal aan Zee", "Bloemendaal", "Netherlands", ""),
    ],
    budget_notes="A Vondelpark hotel runs about $150–320. Pillows, once you accept that it faces Oosterpark, is a more expensive hotel. Bikes are a day rental. The Bos and the dunes are cheap. Keukenhof is a paid ticket and only in its season. Trains to Overveen or Zaandam are ordinary Dutch fares, not a tour price.",
))


add(trip(
    slug="amsterdam-with-private-pool",
    title="The private pool is in Akersloot, not on a canal",
    location="Akersloot, Netherlands",
    summary=(
        "A private swimming pool in a canal-house hotel is not a real Amsterdam product. Hotel Akersloot, about "
        "thirty minutes north by car, does rent suites with an in-room pool of about 1.5 by 3 meters, and from "
        "there you day-trip into the city. Conservatorium Hotel and Waldorf Astoria Amsterdam have real pools, "
        "and both pools are shared spas. Booking either of them does not get you a private pool."
    ),
    who="People who want to swim in their own room and will trade a canal address for that, or who will accept a shared spa pool in the city instead.",
    best_time="May to September if you also want the Castricum beach. The pool suite works in colder months. July weekends in Amsterdam are crowded, which matters less when you sleep in Akersloot.",
    nights=4,
    hook="4 nights · In-room pool in Akersloot · City by day",
    constraints=["Private pool means Akersloot", "City pools on this list are shared", "Car or a train-and-taxi, not a tram to the hotel"],
    lodging="$280–700",
    daily="$360–520",
    neighborhoods=[
        stay_area("Akersloot", "A village between Castricum and Alkmaar. The pool suite is the lodging. Amsterdam is a day trip, about half an hour by car and longer by train and taxi."),
        stay_area("Museumplein or the Herengracht, if you give up the private pool", "Conservatorium and the Waldorf Astoria put you in the city. You swim in a hotel spa with other guests."),
    ],
    hotels=[
        hotel("Hotel Akersloot", "Akersloot", "Suites here have a private indoor pool of about 1.5 by 3 meters. That is a real in-room pool, and it is not a villa lagoon. A standard room in the same hotel does not answer this search. The village is about thirty minutes from Amsterdam by car.", "$280–520", "Akersloot", "https://www.hotelakersloot.nl/en/"),
        hotel("Conservatorium Hotel", "Museumplein", "A converted conservatory facing Museumplein, with a shared spa pool. You can walk to the park and the museums. You cannot claim the pool as your own.", "$450–800", "Amsterdam"),
        hotel("Waldorf Astoria Amsterdam", "Herengracht", "A canal palace with the Guerlain Spa. The pool is real and it is shared. Staying here buys the canal belt and a spa appointment, not a private pool.", "$550–950", "Amsterdam"),
    ],
    itinerary=[
        day(1, "The pool, first", "Arrive in Akersloot and use the thing you booked. The city can wait until tomorrow.", "Pick up a car at Schiphol, or take the train to Castricum and a taxi for the last stretch. Check that your booking says pool suite.", "Swim. The pool is about the size of a small room, 1.5 by 3 meters. It is private. It is not a place to do laps for an hour.", "Dinner in Akersloot or a short drive to Alkmaar if you want a town square. Do not commute into Amsterdam on the arrival night.", "If the confirmation does not name the pool suite, you have a countryside room and a misunderstanding.", ""),
        day(2, "Amsterdam for the animals and the harbor, then back", "One city day that is not a canal-belt walking tour. Sleep in Akersloot again.", "Drive or train in. Artis, in the Plantage, is a compact zoo and a better use of a day-trip morning than a museum sprint.", "The Hortus next door if you like plants, or the free ferry behind Centraal for a look at the IJ and a walk back. Leave the center by late afternoon.", "Pool in the evening. That is the point of sleeping this far out.", "Park once, at the edge, or use the train. Do not drive the canal ring looking for a space.", "Artis (zoo)"),
        day(3, "The local beach", "Castricum aan Zee is the swim that is not a hotel pool. The dunes behind it are the nature.", "Morning in the pool if you like it empty. Then Castricum aan Zee, a few minutes away. Sand, a promenade, and the same dune country as Kennemerland, closer to your bed.", "Walk the beach and stop. You are not trying to cover the whole coast.", "Back to the suite. Alkmaar is the dinner alternative if Castricum feels too much like a beach café.", "Wind off the North Sea is normal. A sunny forecast still means a jacket.", ""),
        day(4, "A short city morning, or Alkmaar", "Use the last day for one thing, then the airport.", "If it is a Friday in cheese-market season, Alkmaar's Waag square is the local sight. Otherwise a second, shorter Amsterdam trip: a neighborhood you missed, then out.", "Pool, pack, and drive to Schiphol. The airport is not in Akersloot, so leave the margin.", "Eat before the terminal. The suite checkout and a flight are enough logistics.", "The cheese market is a seasonal Friday event, not a daily show. On other days Alkmaar is still a walkable old town.", ""),
    ],
    attractions=[
        sight("Hotel Akersloot pool suite", "The private pool, about 1.5 by 3 meters, in the room. This is the attraction you cannot get on the Herengracht.", "Book the suite by name. Ask what the pool hours are in your room, and whether the water is heated the week you come.", ""),
        sight("Artis", "Amsterdam's zoo in the Plantage, easy to reach on a day trip and easy to leave.", "Go at opening. It is a city zoo, not a safari park. Two or three hours is a full visit.", "Artis (zoo)"),
        sight("Castricum aan Zee", "The beach nearest Akersloot, with dunes behind the sand.", "Swim in the sea if you want a swim that is not the hotel pool. The pool is warmer and private. The sea is neither.", ""),
        sight("Alkmaar", "A small North Holland city with a cheese market on Fridays in season and a real center the other days.", "Do not plan the trip around the market unless your Friday is inside the season.", ""),
        sight("De Rijp", "A compact old village near Akersloot, useful on an evening when you do not want Amsterdam.", "It is a walk and a drink, not a sight that needs a guide.", ""),
        sight("The IJ ferry", "The free ride behind Centraal, so a day trip includes the working harbor and not only a museum street.", "Walk on, walk off. It is not a cruise and it does not need a ticket.", ""),
    ],
    scenic_routes=[
        route("Akersloot to Amsterdam by car", "About thirty minutes outside rush hour, into the city and straight to a parking garage. This is the commute your pool costs you.", "About 30 minutes by car"),
        route("Akersloot to Castricum aan Zee", "A short local hop to the beach and the dunes. Do it without going through Amsterdam.", "About 10–15 minutes by car"),
        route("Train via Castricum", "The version without a car: train from Castricum to Amsterdam Centraal, and a taxi or bus between the hotel and Castricum station. Slower than the advertised half hour.", "Often 60–75 minutes door to door"),
    ],
    transport="A car is the honest way to stay in Akersloot and still see Amsterdam. Schiphol pickup works. Without a car, budget a taxi from Castricum station and a train each way, and do not describe it as thirty minutes. In the city, park and walk or use the tram. The Conservatorium and the Waldorf only make sense if you skip the car and accept a shared pool.",
    food=[
        dish("Alkmaar cheese", "A shop by the Waag, eaten the same day", "Buy a piece and eat it. The Friday market is a spectacle. The cheese is the lunch."),
        dish("North Sea fish", "A beach place at Castricum aan Zee", "Fried fish or shrimp croquettes after the sand. It is a café, priced like a beach."),
        dish("Broodje pom", "A Surinamese takeaway on the Amsterdam day", "Chicken and root-vegetable sandwich. One is lunch. Sit on a bench, then get the train or the car."),
        dish("Poffertjes", "A stall in Alkmaar or at a winter market", "Small pancakes, butter, sugar. A snack between the pool and dinner, not a meal."),
    ],
    tips=[
        "The private pool is a suite at Hotel Akersloot. If the room name does not mention a pool, you do not have one.",
        "1.5 by 3 meters is the size. Plan a soak, not a workout.",
        "Conservatorium's pool and the Waldorf's Guerlain pool are shared. They are good city hotels and the wrong answer to 'private'.",
        "Thirty minutes is the drive. The train version has a taxi at the Akersloot end.",
    ],
    faqs=[
        faq("Can I have a private pool on a canal?", "Not in any hotel I am willing to name. The canal houses do not have in-room pools. The suite that does is in Akersloot."),
        faq("Is the Waldorf Astoria pool private?", "No. It is the Guerlain Spa pool, shared by guests. The same is true of the pool at Conservatorium Hotel."),
        faq("Is the Akersloot pool big enough to swim?", "You can swim a few strokes. It is a private indoor pool the size of a small bedroom, not a lap pool and not an infinity edge over the sea."),
        faq("What if I would rather walk to dinner?", "Stay at Conservatorium or the Waldorf, use their shared pool, and drop the word private. The evenings are better. The pool is no longer yours."),
    ],
    map_places=[
        stop("Hotel Akersloot", "Akersloot", "Netherlands", ""),
        stop("Artis", "Amsterdam", "Netherlands", "Artis (zoo)"),
        stop("Castricum aan Zee", "Castricum", "Netherlands", ""),
        stop("Alkmaar", "Alkmaar", "Netherlands", ""),
        stop("Amsterdam Centraal station", "Amsterdam", "Netherlands", ""),
    ],
    budget_notes="The pool suite is the expensive object, often well above a normal Amsterdam room, and a standard room at the same hotel does not count. Conservatorium and the Waldorf are luxury city rates for a shared pool. Add a rental car, or trains plus taxis. Beach food is ordinary. You are paying for the pool and the commute, not for a canal view.",
))


add(trip(
    slug="dubrovnik-budget-under-200night",
    title="Dubrovnik under $200 a night, which means May or October",
    location="Dubrovnik, Croatia",
    summary=(
        "Old Town Dubrovnik in July and August is not a $200 hotel. The rate works in May and October, usually in "
        "Lapad: Hotel Lero is the dependable one, Hotel Kompas sits on the bay and sometimes crosses the line, "
        "and a private room at City Walls Hostel is the only version of that hostel that belongs here. Walk the "
        "walls at opening and take the ferry to Lokrum. A dorm bed is a different, cheaper trip."
    ),
    who="Travelers who will sleep a bus ride from the walls in exchange for a rate that survives the trip.",
    best_time="May and October. Early June and late September can still land near $200 at Hotel Lero if you book ahead. July and August usually will not, even in Lapad.",
    nights=4,
    hook="4 nights · Shoulder season · Lapad under $200",
    constraints=["$200 room in May or October", "Not an Old Town palace in August", "Walls at opening, Lokrum by ferry"],
    lodging="$110–200",
    daily="$180–260",
    neighborhoods=[
        stay_area("Lapad", "The western peninsula: a beach, larger rooms, and a bus of about fifteen minutes to Pile Gate. This is where $200 is a hotel rather than a bunk."),
        stay_area("Inside the walls, only if the room is private and the month is quiet", "City Walls Hostel backs onto the ramparts. Confirm a private room. The lanes are still full of day-trippers at noon."),
    ],
    hotels=[
        hotel("Hotel Lero", "Iva Vojnovića 14, Montovjerna", "A practical hotel with a pool, about a fifteen to twenty minute walk up from Pile, or bus 4 back up the hill. Family rooms exist. In May and October a standard room can sit under $200. In August, do not count on it.", "$120–220", "Dubrovnik"),
        hotel("Hotel Kompas", "Šetalište kralja Zvonimira, Lapad", "On Lapad Bay, with a beach at the door and both an indoor and an outdoor pool. More hotel than Lero, and more likely to price over $200 even in the shoulder. Use it when the beach matters and the rate still fits.", "$160–280", "Dubrovnik"),
        hotel("City Walls Hostel", "Old Town", "Inside the walls, which is the location the budget usually cannot buy. Ask for a private room and get it in writing. A recent city guide described the place as dorms. If the answer is a dorm only, it does not belong on this list.", "$90–180", "Dubrovnik"),
    ],
    itinerary=[
        day(1, "Lapad first, the walls if you still have light", "Arrive, learn the bus, and do not start with a paid walk in the heat of a cruise-ship afternoon.", "Bus or taxi to the hotel. Walk Lapad Bay so you know where the swim is. The Old Town is a bus, not a stroll, from most of these rooms.", "Bus to Pile. Walk the Stradun once, slowly, and stop. You will walk the walls tomorrow when they open.", "Dinner in Lapad. A terrace on the Stradun is the expensive version of an ordinary meal.", "Buy the bus ticket properly. Walking back up the hill from Pile to Lero feels longer than the map.", "Stradun"),
        day(2, "Walls at opening", "The wall walk is about two kilometers of stone and stairs. Morning is the whole trick.", "Be at the gate when the walls open. Go up before the groups. Take water. There is little shade.", "Down into the city for the Stradun, Onofrio's Fountain, and one church or the Rector's Palace if you want an interior. Then the bus back for a swim at Lapad or a walk down to Banje if you are still in town.", "A simple dinner. You already spent the money on the wall ticket.", "The wall ticket is the day's main cost. Do not also buy a cable-car ticket out of habit.", "Dubrovnik City Walls"),
        day(3, "Lokrum", "A short ferry from the old port to a wooded island with a swim and a monastery garden.", "Ferry from the Old Port. Check the last return before you go. You cannot sleep on Lokrum.", "Walk the paths, swim, and sit. Peacocks will try to take your food. Bring water. Leave on a boat you have already identified.", "Evening in Lapad or Gruž. The Old Town at night is prettier than it is cheap.", "The last ferry is not a suggestion. Missing it is how a cheap day becomes a water taxi.", "Lokrum"),
        day(4, "A viewpoint or a slow exit", "One last look, then the airport road, which takes longer than the kilometer count.", "If you want height, the Srđ cable car is a paid view over the roofs and the islands. Skip it if you would rather swim at Lapad and save the fare.", "Be at the airport with a margin. Buses and taxis both slow down when a ship is in.", "Eat a bakery lunch before you go. The terminal is not the meal.", "Walls and Lokrum already did the work. Do not add a last-minute boat to an Elafiti island on a flight day.", ""),
    ],
    attractions=[
        sight("Dubrovnik City Walls", "The walk that justifies the trip. Stone, sea, and roofs, and a lot of steps.", "Enter at opening. Afternoon in July is a shuffle, and this budget trip should not be in July anyway.", "Dubrovnik City Walls"),
        sight("Stradun", "The polished main street. Beautiful, and a poor place to eat or shop.", "Walk it early or after the last excursion boat. At noon it is a corridor.", "Stradun"),
        sight("Lokrum", "The island ferry from the old port: pines, a ruined monastery, rocks to swim from.", "The last boat back is the fact that matters. Peacocks are thieves.", "Lokrum"),
        sight("Fort Lovrijenac", "The fort outside the walls, above the sea on the west side.", "Go if the wall walk left you wanting one more viewpoint. It is a separate ticket.", ""),
        sight("Banje Beach", "The pebble beach just east of the Old Town, under the walls.", "Crowded, and the loungers cost money. Swim and leave, or swim at Lapad for less theater.", ""),
        sight("Lapad Bay", "The neighborhood beach that makes a cheaper hotel feel like a seaside trip.", "The promenade is the walk. The Old Town is the bus.", ""),
    ],
    scenic_routes=[
        route("Pile to the walls at opening", "Bus to Pile Gate, up onto the walls as they open, around the circuit, down to the Stradun.", "About 2 km on the walls, plus the bus"),
        route("Old Port to Lokrum", "Passenger ferry from the old harbor. Walk the island and swim. Return on a boat you chose in advance.", "About 15 minutes each way"),
        route("Lapad Bay promenade", "A flat walk along the bay from the Kompas side, with swims and cafés, no monuments required.", "About 2 km, an hour with a swim"),
    ],
    transport="Libertas city buses connect Lapad, Gruž, and Pile. No cars in the Old Town, and a car is a parking problem you do not need. The airport is a shuttle or a taxi and a slow road when ships are in. Lokrum is a ferry from the Old Port, not a swim. Taxis from the port to Lapad are fine once. Doing it three times a day will eat the hotel savings.",
    food=[
        dish("Crni rižot", "A konoba in Lapad", "Black cuttlefish risotto. One plate is rich. Order it for two to share if you also want grilled squid."),
        dish("Grilled squid", "The same Lapad konoba, not a Stradun terrace", "The ordinary good dinner. A view of the bay is enough. A view of the cathedral is a markup."),
        dish("Burek", "A bakery before the wall walk", "Cheese or meat pie, eaten early. Cheaper and better than a sit-down breakfast in the Old Town."),
        dish("Rožata", "A neighborhood restaurant after the walls", "The local custard. Share one. Do not hunt it on the main street."),
    ],
    tips=[
        "May and October are how $200 works. August is how it doesn't, even before you add the wall ticket.",
        "Walk the walls at opening and carry water. The circuit is exposed.",
        "Confirm a private room at City Walls Hostel. A dorm is not this hotel list.",
        "Lokrum's last ferry is the constraint. Look at it before you look at the peacocks.",
    ],
    faqs=[
        faq("Can I stay inside the walls for $200?", "In July and August, no, not in a hotel room. In May or October a private room at a hostel might. Hotel Lero in Lapad is the booking that actually fits."),
        faq("Is Hotel Kompas always under $200?", "No. It is on the beach and it crosses the line often. Check the date. If it is over, Lero is the one to keep."),
        faq("Do I need a car?", "No. A car cannot enter the Old Town and it will not make Lapad cheaper. Use the bus and the Lokrum ferry."),
        faq("What does the budget not include?", "A sea-view suite in the Old Town, a Stradun dinner, the cable car, and the walls, all on the same day. Pick the walls and one swim."),
    ],
    map_places=[
        stop("Dubrovnik City Walls", "Dubrovnik", "Croatia", "Dubrovnik City Walls"),
        stop("Stradun", "Dubrovnik", "Croatia", "Stradun"),
        stop("Lokrum", "Lokrum", "Croatia", "Lokrum"),
        stop("Pile Gate", "Dubrovnik", "Croatia", ""),
        stop("Lapad Bay", "Dubrovnik", "Croatia", ""),
    ],
    budget_notes="Lodging at $110–200 is a shoulder-season Lapad hotel or a confirmed private room. August can double the bed and blow the premise. The wall ticket is the big extra. Lokrum is a ferry fare. Eat in Lapad and use the bus. A taxi every time you leave the Old Town will cost more than the difference between Lero and a fancier hotel.",
))


add(trip(
    slug="dubrovnik-2-bedroom-under-400night",
    title="A two-bedroom in Dubrovnik under $400, except in August",
    location="Dubrovnik, Croatia",
    summary=(
        "A real two-bedroom under $400 exists in Dubrovnik outside August: a penthouse at Celenga Apartments inside "
        "the walls, the Amarin apartment in Ploče, or Villa Marini Dvori in Lapad. Studios and hotel doubles do not "
        "count, and an August sea view in Ploče or the Old Town often clears $400 even when a listing's 'from' price "
        "looks cheap. Cook some dinners. The walls and Lokrum are still the days."
    ),
    who="Two couples, or a family, who want two closed bedrooms and a kitchen and will travel in the shoulder.",
    best_time="May, June, late September, and October. August is when a true two-bedroom in Ploče or the Old Town leaves this budget. Lapad lasts longer, and even Lapad can fail in the first two weeks of August.",
    nights=4,
    hook="4 nights · Two bedrooms · Under $400 outside August",
    constraints=["Two closed bedrooms", "Under $400 outside August", "Kitchen, so skip the Stradun markup"],
    lodging="$180–400",
    daily="$280–400",
    neighborhoods=[
        stay_area("Old Town or Ploče", "Celenga is inside the walls. Amarin is in Ploče, a short walk from Banje and the old port. You give up a beach at the door and gain the morning city."),
        stay_area("Lapad", "Villa Marini Dvori is the two-bedroom that stays nearer the cap. The beach is a walk. The walls are a bus."),
    ],
    hotels=[
        hotel("Celenga Apartments", "Svetoga Josipa 13, Old Town", "An apartment house in the walls. The two-bedroom is the Minčeta penthouse, about 56 square meters with a kitchen, not the studios. A published from-price near €100 is not an August rate. In August this unit can leave $400.", "$180–450", "Dubrovnik"),
        hotel("Luxury Amarin Apartment", "Lukše Beritića 6, Ploče", "One apartment, not a hotel: two bedrooms, two bathrooms, a kitchen, and a sea-view terrace, an eight-minute walk from Banje. If those dates are taken, you need another Ploče apartment, not a double room renamed as a suite.", "$200–480", "Dubrovnik"),
        hotel("Villa Marini Dvori", "Između ribnjaka 1, Lapad", "A two-bedroom apartment with a terrace in Lapad, a walk from the bay and a bus from the Old Town. This is the one most likely to stay under $400. The listing has said pets are not allowed.", "$160–380", "Dubrovnik"),
    ],
    itinerary=[
        day(1, "Groceries, then the lane", "Settle the apartment and buy food. The two-bedroom only pays off if you use the kitchen.", "Check in and confirm you have two bedrooms and a working stove. A sofa bed in the living room is not the booking.", "If you are inside the walls or in Ploče, shop at Gundulić Square's morning market if it is still open, or at a Konzum in Lapad. Fruit, cheese, bread, coffee.", "Cook. Walk the Stradun after dinner, when the day boats have gone.", "Stairs are part of every Old Town address. Ask about them before you arrive with luggage.", "Stradun"),
        day(2, "Walls, early, and a home dinner", "Same wall walk as everyone else, at a time when it is worth the ticket.", "Walls at opening, with water. Two kilometers, lots of steps, little shade.", "A swim at Banje if you are in Ploče, or the bus to Lapad Bay if that is where the apartment is. Do not do both plus a boat.", "Cook again, or one konoba in the neighborhood. Not both, and not on the Stradun.", "The wall circuit is enough walking. Save Lokrum for tomorrow so the days stay distinct.", "Dubrovnik City Walls"),
        day(3, "Lokrum from the old port", "The island day. The ferry is short. The last boat is the schedule.", "Ferry from the Old Port. Picnic from the apartment. The peacocks are not shy.", "Swim, walk the paths, and leave on a return you already chose.", "A simple dinner. If you are in Lapad, eat near the bay. If you are in Ploče, you are close enough to walk home.", "Sunscreen and water. The island is rock and pine, and the café prices are island prices.", "Lokrum"),
        day(4, "One neighborhood, then the airport", "A last morning in the place you actually stayed, not a new island.", "Ploče guests can walk the old port and look at the cable car without riding it. Lapad guests should swim and then allow a long airport transfer.", "Checkout, a bakery lunch, and the road to the airport. Ships in the port make the road slow.", "Eat before you go.", "A two-bedroom checkout in the Old Town means carrying bags down stairs. Leave time.", ""),
    ],
    attractions=[
        sight("Dubrovnik City Walls", "Still the walk. A bigger apartment does not make noon on the walls more comfortable.", "Opening time. The ticket is per person, so a family of four should want the morning.", "Dubrovnik City Walls"),
        sight("Stradun", "The evening walk after you have cooked, when you are not paying terrace prices to sit on it.", "Shop elsewhere. The street is the sight.", "Stradun"),
        sight("Lokrum", "The easy island. A picnic from your kitchen beats the island café.", "Last ferry. Do not miss it with a car full of people waiting at the apartment.", "Lokrum"),
        sight("Gundulić Square market", "The morning market for fruit, cheese, and the reason the kitchen was worth booking.", "Go in the morning. By afternoon it is over.", ""),
        sight("Banje Beach", "The swim for a Ploče or Old Town apartment. Pebbles, a view of the island, loungers that cost extra.", "You can swim without a lounger. The walk back up to Ploče is short and uphill.", ""),
        sight("Lapad Bay", "The swim and the promenade if the two-bedroom is at Marini Dvori.", "The bus to Pile is the link to the walls. Build it into the morning, not the minute before closing.", ""),
    ],
    scenic_routes=[
        route("Wall circuit at opening", "Up from Pile or the internal gates, around the walls, down before the worst of the heat.", "About 2 km"),
        route("Old Port to Lokrum with a picnic", "Ferry across, swim, back on a chosen boat. The picnic comes from the apartment.", "About 15 minutes each way"),
        route("Ploče to Banje to the old port", "A short coastal walk from a Ploče apartment to the beach and the ferry dock, without crossing the whole city.", "Under 2 km"),
    ],
    transport="On foot inside the walls and in Ploče. A bus from Lapad to Pile. No car in the Old Town, and a car is awkward for a Ploče apartment too. Airport transfers need a margin. The Lokrum ferry is the only boat this itinerary requires. A private water taxi will erase the difference between a $300 apartment and a $500 hotel.",
    food=[
        dish("Market breakfast", "Gundulić Square, or a Lapad supermarket", "Peaches, cheese, yogurt, bread. This is the meal the kitchen is for. Do it more than once."),
        dish("Octopus salad", "A konoba in Ploče or Lapad, one night", "The eat-out night. One seafood plate and a simple pasta, not a tasting menu."),
        dish("Gregada", "A family konoba, if it is on the menu", "Fish stew. Ask what the fish is. If the answer is vague, order the grilled catch of the day instead."),
        dish("Grilled fish at Lapad", "A konoba on the bay, for the Marini Dvori stay", "The dinner you walk to. Split one fish and a salad. The apartment covers the other nights."),
    ],
    tips=[
        "Book the unit that has two bedrooms. Celenga's studios and a hotel double do not satisfy the search.",
        "Ignore a 'from' price until you see your dates. August in the walls and in Ploče is the month that breaks $400.",
        "Cook at least two dinners. Otherwise you have paid for a kitchen and eaten on the Stradun.",
        "Amarin is a single apartment. If it is taken, look for another Ploče two-bedroom, not a rebranded hotel room.",
    ],
    faqs=[
        faq("Will $400 get a two-bedroom in August?", "Often no, not in the Old Town or Ploče with a view. Lapad is the better chance, and even there the first half of August can fail. May and October are the reliable months."),
        faq("Is a family room in a hotel the same thing?", "No. Hotel Lero has family rooms, and they are not automatically two bedrooms. This list is apartments with two rooms and a kitchen."),
        faq("Which base is easiest with luggage?", "Lapad, at Marini Dvori. The Old Town and Ploče mean stairs and limited taxis at the gate."),
        faq("Are pets welcome at these apartments?", "Do not assume it. A Marini Dvori listing has said no pets. Ask each host before you travel with an animal."),
    ],
    map_places=[
        stop("Celenga Apartments", "Dubrovnik", "Croatia", ""),
        stop("Ploče", "Dubrovnik", "Croatia", ""),
        stop("Lapad Bay", "Dubrovnik", "Croatia", ""),
        stop("Lokrum", "Lokrum", "Croatia", "Lokrum"),
        stop("Dubrovnik City Walls", "Dubrovnik", "Croatia", "Dubrovnik City Walls"),
    ],
    budget_notes="A true two-bedroom under $400 is a shoulder-season rate. Celenga's penthouse and the Amarin apartment can clear it in August even if a teaser price says otherwise. Groceries keep the daily spend down. The walls are a per-person ticket. Budget a taxi or shuttle to the airport on the last day, especially from Lapad.",
))


add(trip(
    slug="split-family-friendly-with-kitchen",
    title="Split with a kitchen, the palace in the morning, and a beach after lunch",
    location="Split, Croatia",
    summary=(
        "A family week in Split works when the apartment has a stove and the days stay short. Riva Apartments sit on "
        "the palace wall above the promenade. Residence by Vestibul Palace, a ten-minute walk away, has real kitchens "
        "and two actual two-bedroom suites. Hotel Park is the fallback on Bačvice, and it does not have a guest kitchen. "
        "The palace is the walk. The easy beach is Bačvice. The easy island with children is Supetar on Brač, not a "
        "full-day dash to Bol."
    ),
    who="Parents who will cook breakfast and want a shallow beach and one ferry that still gets everyone home for bedtime.",
    best_time="June and September. The sea is warm enough, the palace is not yet or no longer at peak cruise chaos, and the ferry is frequent. July and August are hotter, busier, and more expensive. May can be lovely and too cold to swim.",
    nights=4,
    hook="4 nights · Kitchen near the Riva · One easy Brač day",
    constraints=["A kitchen, except the Hotel Park fallback", "Bačvice, not a Hvar villa", "Supetar with kids, Bol only if you commit the day"],
    lodging="$140–360",
    daily="$220–340",
    neighborhoods=[
        stay_area("Riva and the south wall of the palace", "Riva Apartments are on this edge. You walk out to the promenade and the port. Cruise passengers do the same at midday, so mornings belong to you."),
        stay_area("Gripe, ten minutes from the palace", "Residence by Vestibul is the quieter family base, with a garage. The beach is a longer walk, about twenty minutes toward Bačvice."),
    ],
    hotels=[
        hotel("Riva Apartments", "Alješijeva 6", "Apartments on the south wall of Diocletian's Palace, by the Riva, about a ten-minute walk from Bačvice. Units have a kitchen or a kitchenette. Confirm a stove and an oven, not only a kettle, before you call it a family kitchen.", "$140–280", "Split"),
        hotel("Residence by Vestibul Palace", "Istarska 25", "Five suites beside Gripe Fortress, each with a full kitchen. Two are two-bedroom luxury suites. The other three are one-bedroom juniors. About eight to ten minutes on foot to the palace, twenty to Bačvice. Quieter than the Riva at night.", "$180–420", "Split"),
        hotel("Hotel Park Split", "Hatzeov perivoj 3, Bačvice", "The graceful hotel beside Bačvice, with family rooms and a pool, and no guest kitchen. Use it when the apartments are gone and you accept eating out. In August the beach bars in front are not a quiet night.", "$160–340", "Split"),
    ],
    itinerary=[
        day(1, "The palace before the ships, then the apartment kitchen", "A short first day. Children get one wonder, not three.", "Walk into Diocletian's Palace through the basement halls and the Peristyle. Early. The stone is the sight. You do not need a long guided route.", "Gelato on the Riva, then groceries: bread, fruit, cheese, yogurt, something easy for dinner. Back to the apartment.", "Cook. The Riva at night is a promenade, fine for a short walk, loud if you were hoping for sleep with the windows open.", "Apartments on the palace wall hear the Riva. Residence by Vestibul is the quieter sleep.", "Diocletian's Palace"),
        day(2, "Bačvice", "The city beach. Shallow for a long way, which is why families use it. Not a secret cove.", "Morning swim at Bačvice. The water is shallow and the shore is concrete and pebble, with a sandy patch. Picigin, the local ball game, happens in the shallows when locals are playing. Watch before you join.", "Back to the apartment for lunch from the kitchen. A hot afternoon is for the room, not another monument.", "A simple dinner out if you want a break from cooking, in Lučac or Varoš rather than the first Riva terrace.", "Sun on the Riva is serious. Hats, and an afternoon indoors, will save the next day.", ""),
        day(3, "Supetar, and home for bed", "Brač is the island day that fits children. Supetar is the near port. Bol is a second journey.", "Passenger ferry from Split's port to Supetar, about fifty to sixty minutes. Buy tickets ahead in summer. No car required.", "The Supetar waterfront and a swim. Ice cream. The last return you can take without a meltdown is the one you already circled.", "Dinner at the apartment. Everyone is tired. That is a successful island day.", "Zlatni Rat at Bol is a beautiful beach and a full day: a catamaran or a bus across the island. Do it only if the children still like long trips. Otherwise stay in Supetar.", ""),
        day(4, "Marjan if the legs work, or another swim", "A green hill on the west side of town. Forest paths, views, no ticket.", "If energy is good, walk up Marjan from the Varoš side and stop at the first real viewpoint. If not, go back to Bačvice.", "Pack, swim if the checkout allows, and use the kitchen for a last lunch so you are not hunting food at the port.", "Bus, ferry, or airport. Split airport is a long transfer. Leave the margin.", "Marjan is shade and pine, still uphill. A stroller is the wrong tool on the paths.", "Marjan, Split"),
    ],
    attractions=[
        sight("Diocletian's Palace", "The Roman palace the old town is built into. Basement halls, the Peristyle, and streets that are still streets.", "Go before the cruise groups. With children, an hour in the cellars and the square is enough.", "Diocletian's Palace"),
        sight("Bačvice", "The neighborhood beach, shallow, close, and ordinary in the best way.", "Morning is calmer. The beach bars get louder toward evening in summer.", ""),
        sight("Supetar", "The Brač port closest to Split. A waterfront, a swim, and a ferry home the same day.", "This is the child-friendly island day. Bol is optional and longer.", ""),
        sight("Marjan", "The wooded hill west of the center. Viewpoints over the harbor and the islands.", "Take the easy viewpoint, not a summit march, if you are with small children.", "Marjan, Split"),
        sight("The Riva", "The palm promenade. The walk between the palace, the port, and ice cream.", "It is a walk, not a beach. Swim at Bačvice.", ""),
        sight("Green market", "Fruit and picnic food for the apartment, just outside the palace.", "Morning. Buy fruit you will actually eat that day.", ""),
    ],
    scenic_routes=[
        route("Palace to Bačvice", "Out of the south gate, along the Riva, then around to Bačvice. A ten to fifteen minute walk from the palace wall.", "About 1 km"),
        route("Split port to Supetar", "Passenger ferry, about an hour, then the Supetar waterfront on foot. Back on a boat you chose in the morning.", "50–60 minutes each way"),
        route("Varoš to the first Marjan viewpoint", "Up through Varoš into the pines, stop at the first wide view, and come down. Shade, stairs, and no ticket.", "About 3 km with the return"),
    ],
    transport="Walk the center. Ferries to Supetar leave from the city port, a short walk from the Riva. Buy tickets ahead on summer weekends. A car is useless inside the palace and a nuisance at Bačvice. The airport bus or a prebooked transfer needs more time than the map suggests. Taxis are for luggage and late boats, not for every beach trip.",
    food=[
        dish("Burek", "A bakery near the market", "The breakfast that children will eat. Cheese or meat. Carry it to the apartment or eat it on the Riva early."),
        dish("Pašticada", "A konoba in Varoš", "Beef stewed in wine and prunes, with gnocchi. The one restaurant meal. Share a plate with a plain pasta for smaller appetites."),
        dish("Gradele", "The same kind of konoba, if the table wants fish", "Tiny fried fish. Order a portion to share before you commit a hungry table to a whole grill."),
        dish("Peka", "A konoba that will start it if you ask the day before", "Meat or octopus under the iron bell. It is not a walk-in lunch. Skip it if the timing is fussy."),
    ],
    tips=[
        "Confirm a real stove. A kitchenette can mean a fridge and a kettle, which will not feed a family for four nights.",
        "Residence by Vestibul has two two-bedroom suites and three one-bedrooms. Book the two-bedroom if you need two rooms.",
        "Hotel Park is the beach hotel without a kitchen. The nights in front of it are lively in August.",
        "With children, ferry to Supetar and swim. Add Bol only if everyone is happy on boats.",
    ],
    faqs=[
        faq("Is the palace all right with kids?", "Yes, early, for the underground halls and the square. It is not a full-day museum. Leave when the groups arrive."),
        faq("Which beach is realistic?", "Bačvice. It is shallow and close. Žnjan is bigger and a longer trip. A Hvar villa is a different island and a different budget."),
        faq("Can we cook every night?", "Yes at Riva Apartments, if your unit has a stove, and yes at Residence by Vestibul. No at Hotel Park."),
        faq("What if the ferry to Brač is rough or sold out?", "Stay at Bačvice. The island day is a bonus, not the only swim."),
    ],
    map_places=[
        stop("Diocletian's Palace", "Split", "Croatia", "Diocletian's Palace"),
        stop("Bačvice Beach", "Split", "Croatia", ""),
        stop("Riva", "Split", "Croatia", ""),
        stop("Marjan", "Split", "Croatia", "Marjan, Split"),
        stop("Supetar", "Supetar", "Croatia", ""),
    ],
    budget_notes="Apartments with kitchens run about $140–300 in June and September and more in August, especially the two-bedroom suites at Residence by Vestibul. Groceries cut meals sharply. The palace walk is free. The Supetar ferry is the main ticket, per person. Hotel Park looks simpler and then charges you for every breakfast and dinner.",
))


add(trip(
    slug="split-near-the-beach-under-300",
    title="Split under $300, on a beach that is actually in Split",
    location="Split, Croatia",
    summary=(
        "The beach stay under $300 is Bačvice or Žnjan, not a villa on Hvar. Hotel Park and Hotel Villa Harmony are "
        "at Bačvice. Radisson Blu Resort & Spa faces the Žnjan coast on Put Trstenika, and in August it often crosses "
        "$300. Stobreč is the quieter bay just beyond, and this list does not invent a hotel there. You can still "
        "walk the palace for one morning. The rest is swimming."
    ),
    who="People who want to swim from the hotel side of Split and will not quietly upgrade themselves to Hvar.",
    best_time="June and September for warm water and a rate under $300. July can still fit at Hotel Park or Villa Harmony if you book early. August at the Radisson often does not.",
    nights=3,
    hook="3 nights · Bačvice or Žnjan · Under $300",
    constraints=["A real Split beach", "Under $300, with an August caveat at the Radisson", "Not Hvar"],
    lodging="$150–300",
    daily="$230–340",
    neighborhoods=[
        stay_area("Bačvice", "The city beach east of the Riva. Hotel Park is on the garden above it. Villa Harmony is on the shore path. You can walk to the palace."),
        stay_area("Žnjan and the Trstenik shore", "Radisson Blu is the big resort on this coast. The beach is longer and the center is a bus or a taxi. Stobreč sits just south, quieter, without a hotel I will name at this price."),
    ],
    hotels=[
        hotel("Hotel Park Split", "Hatzeov perivoj 3, Bačvice", "A 1920s hotel rebuilt beside Bačvice, with a pool and family rooms. A standard room in June or September often fits under $300. A sea view in August may not. You hear the beach.", "$160–340", "Split"),
        hotel("Radisson Blu Resort & Spa, Split", "Put Trstenika 19", "The resort hotel on the Žnjan side, with a real pool and a beach across the road. This is the proper beach hotel, and it is the one that most often prices over $300 in July and August. Shoulder season is when the cap holds.", "$180–420", "Split"),
        hotel("Hotel Villa Harmony", "Preradovićevo šetalište 1a, Bačvice", "A smaller hotel on the Bačvice shore path, with a pool. You are at the beach without the Radisson's size. Check the August rate. The location is the point.", "$150–300", "Split"),
    ],
    itinerary=[
        day(1, "Swim first", "The hotel is at the beach. Use it before you use the palace.", "Check in and swim at Bačvice or at the Radisson's stretch of Žnjan, depending on the bed. The water is clear and the shore is not a Caribbean beach.", "Walk the promenade. If you are at Bačvice, you can reach the Riva on foot. If you are at Žnjan, stay on the coast for the first afternoon.", "Dinner within walking distance of the hotel. The first night is not a taxi to a famous terrace.", "Loungers are a paid extra at some stretches. The swim is not.", ""),
        day(2, "The other beach, or the palace if the wind is up", "One full day that is still about the water, with the city as the backup.", "If you slept at Bačvice, bus or taxi to Žnjan for a longer shore, or walk the coast as far as you feel like. If you slept at the Radisson, spend the morning on Žnjan and the late afternoon in the palace so you see the city once.", "Diocletian's Palace for an hour if you have not gone, early enough that it is not a cruise corridor. Then back to the water.", "Dinner near the hotel again. Three nights is too short to commute for every meal.", "Do not add Hvar. The catamaran is a new trip, and a luxury villa there is the booking this page is refusing.", "Diocletian's Palace"),
        day(3, "A last swim, then leave", "Checkout days still get a morning in the sea if the flight is later.", "Swim, return the towels, and eat something simple. The airport transfer from Žnjan is longer than from Bačvice. Start earlier than the flight number suggests.", "If the flight is late, the palace or Marjan is the dry-land option. If it is early, the swim was yesterday.", "Be at the airport with the bag you already packed wet.", "Split airport transfers are the delay. The beach is not on the way to the terminal.", ""),
    ],
    attractions=[
        sight("Bačvice", "Split's city beach. Shallow water, a promenade, and the hotels that make this budget real.", "Morning swim. In August the bars stay loud after you are ready for bed.", ""),
        sight("Žnjan", "A longer beach east of the center, where the Radisson sits.", "It is a beach, with cafés and not much shade. Bring sandals. The stones and concrete are hot.", ""),
        sight("Stobreč", "The next bay south, residential and quieter. A swim if you are already on the Žnjan side.", "I am not naming a hotel here. Go for the water, then sleep at one of the three hotels above.", ""),
        sight("Diocletian's Palace", "The one city walk. Roman cellars and a living old town.", "An hour, not a second itinerary. You came for the beach.", "Diocletian's Palace"),
        sight("The Riva", "The promenade between Bačvice and the palace.", "Walk it once in the evening. Eat closer to the hotel if the Riva tables look like a performance.", ""),
        sight("Marjan", "The hill you climb only if you want shade and a view on a hot afternoon.", "The first viewpoint is enough. The pine paths are the cooler part of the day.", "Marjan, Split"),
    ],
    scenic_routes=[
        route("Bačvice to the Riva", "Along the shore and around the point to the promenade and the palace. Flat, and the reason a Bačvice hotel still counts as Split.", "About 15–20 minutes"),
        route("Žnjan shore", "A walk along the beach in front of the resort coast, swimming where you feel like it. Stobreč is the far end if you keep going by bus.", "A few kilometers of coast"),
        route("One hour in the palace", "From the Riva into the cellars and the Peristyle, then back to the beach. A loop, not a treasure hunt.", "About 2 km with the walk from Bačvice"),
    ],
    transport="From Bačvice you can walk to the Riva and the port. From the Radisson at Žnjan, use a taxi or a local bus to the center and do not plan on walking it in the heat with children or luggage. The airport is a transfer from either. You do not want a car at these beaches. A Hvar catamaran is how this short trip loses a day.",
    food=[
        dish("Grilled fish", "A restaurant on the Žnjan or Bačvice side, one night", "One proper fish, shared, with salad. Ask the price before it is cooked. Beach fish is where the budget slips."),
        dish("Soparnik", "A bakery or a simple konoba", "A chard pie from the Split coast. Buy a piece. It is lunch with tomatoes."),
        dish("Ćevapi or a plain grill", "A casual place off the Riva", "The dinner that stays under control. The Riva is for a drink you can see the sea with, not for the meal."),
        dish("Gelato", "On the walk back from Bačvice", "The daily extra that is worth it. Skip the tourist cocktail lists."),
    ],
    tips=[
        "Under $300 is a June or September rate at these hotels. Check August at the Radisson before you assume it fits.",
        "Hvar is a different island and, for a villa, a different budget. This page will not send you there.",
        "Hotel Park is on Bačvice. The beach in front of it is social at night in high summer.",
        "Stobreč is a real quieter swim. It is not, on this list, a hotel recommendation.",
    ],
    faqs=[
        faq("Is Žnjan in Split?", "Yes. It is the eastern beach, a bus or taxi from the palace. The Radisson is the hotel there. Bačvice is closer to the center."),
        faq("Can I do this on Hvar for the same money?", "A luxury villa on Hvar is not this trip. A basic Hvar room in August is its own search, and it is not a Split beach hotel."),
        faq("Will $300 hold in August?", "At the Radisson, often no. At Hotel Park or Villa Harmony, sometimes, for a standard room. Read the date, not the brochure rate."),
        faq("Do I need to see the palace?", "Once, for an hour. Three nights of only the palace would be the wrong hotel. Three nights of only the lounger is allowed."),
    ],
    map_places=[
        stop("Bačvice Beach", "Split", "Croatia", ""),
        stop("Žnjan Beach", "Split", "Croatia", ""),
        stop("Hotel Park Split", "Split", "Croatia", ""),
        stop("Diocletian's Palace", "Split", "Croatia", "Diocletian's Palace"),
        stop("Stobreč", "Stobreč", "Croatia", ""),
    ],
    budget_notes="Plan on $150–300 a night in June and September. August at Radisson Blu is the rate that breaks the cap. Beach restaurants can cost more than the hotel savings, so keep one fish dinner and eat simply otherwise. Loungers, taxis from Žnjan, and the airport transfer are the extras. There is no villa fee because there is no villa.",
))


add(trip(
    slug="split-quiet-romantic-getaway",
    title="Quiet Split: Marjan at sunset, Varoš for dinner, Šolta if you want water",
    location="Split, Croatia",
    summary=(
        "The quiet version of Split is not the Riva at midnight in August. Stay in a small palace hotel or a garden "
        "house on the Marjan side, walk the hill at sunset, and eat in Varoš. Hotel Vestibul Palace is tiny and "
        "inside the walls, which are calm at breakfast and not calm late on an August Saturday. Villa Diana is the "
        "more residential sleep. Hotel Park is lovely and faces Bačvice, where the beach bars are the opposite of a "
        "retreat in high summer. A day boat to Šolta fits four nights. Vis is a beautiful island and a long ferry."
    ),
    who="A couple who want stone, a viewpoint, and a dinner they can hear each other over.",
    best_time="Late May, June, and September. The sea is warm and the lanes empty earlier. August midnight on the Riva and at Bačvice is a party. Marjan at sunset still works in August. The streets below it do not get quiet.",
    nights=4,
    hook="4 nights · Marjan and Varoš · Šolta, not the midnight Riva",
    constraints=["Quiet evenings", "Not the Riva in August", "Šolta as the day boat, Vis only if you accept the ferry"],
    lodging="$160–450",
    daily="$260–400",
    neighborhoods=[
        stay_area("Inside the palace, at breakfast", "Hotel Vestibul Palace is on Iza Vestibula, a few rooms in the Roman core. Beautiful at 8 a.m. In August the lanes outside are busy until late."),
        stay_area("The Marjan side", "Villa Diana on Kuzmanićeva is a house with a garden, west of the noise. Hotel Park is farther around at Bačvice and only quiet if your dates are."),
    ],
    hotels=[
        hotel("Hotel Vestibul Palace", "Iza Vestibula 4", "A small hotel in Diocletian's Palace. The rooms are the quiet object. The street outside is not, late, in August. Book it for the stone and the courtyard, and keep August expectations modest.", "$220–480", "Split"),
        hotel("Villa Diana", "Kuzmanićeva 3", "A villa hotel with a garden on the Marjan side of town. This is the more convincing quiet base: residential, not on the Riva, and a walk from the hill paths.", "$150–280", "Split"),
        hotel("Hotel Park Split", "Hatzeov perivoj 3, Bačvice", "A handsome hotel with a terrace and a pool above Bačvice. The building is calm. The beach in front, in July and August, is not a romantic secret after dark. Choose it for the sea view in June or September.", "$180–360", "Split"),
    ],
    itinerary=[
        day(1, "Sunset on Marjan, nothing else ambitious", "Arrive and go up the hill while the city is still in the sun.", "Check in. If you are at Villa Diana you are already on the right side. From Vestibul or the Park, walk to Varoš and up.", "Stop at the first wide viewpoint over the harbor and the islands. The pines are the point. You do not need the far end of the park.", "Dinner in Varoš, a konoba on a side street. Then bed. The Riva can wait until a morning.", "Marjan paths are uneven. Ordinary shoes are fine. Heels are not.", "Marjan, Split"),
        day(2, "The palace when it is empty", "A morning in the stone, before the ships, and a long lunch nowhere famous.", "Peristyle and the cellars early, while Vestibul's neighborhood still belongs to people who slept there. Coffee. Leave when the groups fill the square.", "A slow afternoon. The beach at Kašjuni, on the Marjan shore, is quieter than Bačvice if you want a swim without the promenade.", "Dinner in Varoš again, or one serious table if you booked it. Not a club, and not the Riva after ten if quiet was the request.", "Kašjuni is a local swim with a view of the islands. It is still a city beach, just a calmer one.", "Diocletian's Palace"),
        day(3, "Šolta for the day", "The quieter island that fits a four-night stay. Vis is the one people name, and the ferry eats the day.", "Morning passenger ferry from Split to Rogač on Šolta, about an hour. Check the last return before you board.", "From Rogač you still need a bus, a taxi, or a bike to a cove such as Nečujam or Stomorska. The dock itself is not the beach. Swim, eat simply, and make the boat.", "A late, light dinner near the hotel. You will not want a scene.", "Vis is more than two hours each way. On this trip it is an overnight you do not have. Do not turn it into a frantic day.", ""),
        day(4, "A quiet morning, then the airport", "The last morning should feel like the hotel you chose.", "Coffee in the garden at Villa Diana, or the palace courtyards at Vestibul before the day begins, or a short swim at Bačvice only if you stayed at the Park and the beach is still asleep.", "Checkout and the airport road. Split transfers are slow.", "Eat before the terminal.", "If you wanted silence and booked the Park in August, use this morning as the swim and accept that the night was the compromise.", ""),
    ],
    attractions=[
        sight("Marjan", "The wooded hill over the city. Sunset here is the romantic sight, and it is free.", "Go up in the late afternoon. Come down before the paths feel dark. The first viewpoint is enough.", "Marjan, Split"),
        sight("Varoš", "The neighborhood of stone houses inland from the palace, with the konobas that are not performing for the Riva.", "Book dinner. The good rooms are small.", ""),
        sight("Diocletian's Palace", "The morning version: empty squares, the cellars, a coffee. Not a midnight wander in August.", "Be there early. Leave when the cruise groups take the Peristyle.", "Diocletian's Palace"),
        sight("Kašjuni", "A smaller beach on the Marjan shore, facing the channel. Quieter than Bačvice.", "It is a swim and a view. There is not a resort behind it.", ""),
        sight("Šolta", "The island day. Rogač is the port. The coves are a second hop.", "Last ferry first. Then a taxi or bus to the water you actually want.", ""),
        sight("Hotel Vestibul's quarter", "The palace street itself, worth seeing at breakfast, from the hotel that is actually in it.", "The hotel is small. The romance is the building. The street noise in August is separate and real.", ""),
    ],
    scenic_routes=[
        route("Varoš to the Marjan viewpoint", "Through the upper lanes into the pines, out to a harbor view, back the same way as the light goes.", "About 3 km"),
        route("Split to Rogač", "Morning ferry to Šolta, onward to a cove, back on a return you checked before leaving the hotel.", "About 1 hour each way, plus the cove"),
        route("Early palace loop", "Vestibul to the Peristyle and the cellars and back, before 9 a.m. A short walk that only works early.", "Under 2 km"),
    ],
    transport="Walk. The ferry to Rogač leaves from the city port. A taxi is reasonable for a late return or for luggage to Villa Diana. A car is the wrong tool for Vestibul and only mildly useful for the villa. Do not rent a scooter to chase a quiet trip. Vis ferries exist and take too much of a four-night stay.",
    food=[
        dish("Konoba dinner in Varoš", "A small dining room in Varoš", "Grilled fish or pašticada, a salad, a bottle you can finish. Book it. Ask for a table inside if the lane is loud."),
        dish("Coffee and a pastry", "A square near Vestibul, early", "The romantic breakfast is 8 a.m., not a champagne brunch on the Riva."),
        dish("Picnic on Marjan", "Bought at the market, eaten at the viewpoint", "Bread, tomatoes, cheese, and fruit. Better than a sunset restaurant with speakers."),
        dish("Simple lunch on Šolta", "Whatever is open by the cove you reached", "Grilled fish if they have it. Do not miss the ferry for a second course."),
    ],
    tips=[
        "August on the Riva is not this trip. If your dates are August, sleep at Villa Diana and stay off Bačvice at night.",
        "Vestibul is quiet inside and only as quiet as the palace lane outside. That lane is not quiet late in summer.",
        "Hotel Park's terrace is romantic. The beach clubs in front of it in July are not.",
        "Šolta fits. Vis is a long ferry each way and wants a night you are not spending there.",
    ],
    faqs=[
        faq("Which hotel is actually quiet?", "Villa Diana, on the Marjan side. Vestibul is quiet in the building and lively in the street in August. Hotel Park depends on the month, and August is the loud month."),
        faq("Can we do Vis in a day?", "You can, on a very early ferry and a late return, and you will spend most of the romance on the boat. Šolta is the day that leaves you an evening."),
        faq("Is Hvar the more romantic island?", "Hvar town in August is a nightclub with stone streets. It is not the quiet getaway. This itinerary stays in Split and adds Šolta."),
        faq("Do we need dinner reservations?", "Yes, for the one Varoš table you care about. The trip is four nights. One booked dinner is enough."),
    ],
    map_places=[
        stop("Marjan", "Split", "Croatia", "Marjan, Split"),
        stop("Varoš", "Split", "Croatia", ""),
        stop("Diocletian's Palace", "Split", "Croatia", "Diocletian's Palace"),
        stop("Rogač", "Šolta", "Croatia", ""),
        stop("Villa Diana", "Split", "Croatia", ""),
    ],
    budget_notes="Villa Diana is the rate that stays reasonable. Vestibul and a sea view at Hotel Park cost more and still do not buy silence in August. The Šolta ferry is the excursion. Dinners in Varoš are normal konoba prices if you avoid the Riva. A taxi on the island is a fair extra. Do not add a private boat.",
))


add(trip(
    slug="santorini-2-bedroom-under-400night",
    title="A two-bedroom on Santorini under $400 means a village, not Oia",
    location="Santorini, Greece",
    summary=(
        "A caldera cave in Oia with two bedrooms will not cost $400 a night in any month people want to be there, "
        "and July and August will not produce that rate for a two-bedroom caldera view in Fira either. The honest "
        "booking is a village: Kastro Mansion in Pyrgos has a real two-bedroom suite and may still clear the cap, "
        "Astivi lists two-bedroom apartments in Pyrgos, and Villa Renos in Fira has a 100-square-meter Grand Suite "
        "on the cliff whose floor plan you must confirm. May and October are the months. The kitchen is in the village."
    ),
    who="Friends or a family who need two bedrooms and will give up the Oia postcard to stay under the cap.",
    best_time="May and October. Early June and late September are a maybe. July and August will not hit $400 for a two-bedroom with a caldera view.",
    nights=4,
    hook="4 nights · Two bedrooms in a village · Not an Oia cave",
    constraints=["Two bedrooms under $400", "Shoulder season", "Pyrgos or a confirmed large Fira suite, not Oia"],
    lodging="$180–400",
    daily="$260–380",
    neighborhoods=[
        stay_area("Pyrgos", "A hill village inland from the caldera cliff. Kastro Mansion and Astivi are here. You look at the island from a castle lane, then take the bus to the rim when you want the drop."),
        stay_area("Fira, only for the large suite", "Villa Renos is on the caldera in Fira. The Grand Suite is the only unit big enough to pretend to this search, and it is the unit that leaves $400 in season."),
    ],
    hotels=[
        hotel("Kastro Mansion", "Pyrgos", "A mansion in Pyrgos with a deluxe two-bedroom suite, so the bedroom count is real. It is also the stylish one, and a caldera-minded suite here can clear $400 in a busy week even outside August. Read the dates.", "$250–650", "Pyrgos Kallistis, Santorini"),
        hotel("Astivi Santorini Apartments", "Pyrgos Kallistis", "Village apartments, not caves over the cliff. Book the two-bedroom by that name and ignore any studio in the same listing. May and October are when a rate under $400 is believable.", "$160–400", "Pyrgos Kallistis, Santorini"),
        hotel("Villa Renos", "Fira caldera", "A long-running Fira hotel on the rim. The Grand Suite is about 100 square meters and sleeps five. The site does not say those are two closed bedrooms, so ask for the plan. Smaller rooms do not count. July and August will not be a $400 stay.", "$300–800", "Fira, Santorini"),
    ],
    itinerary=[
        day(1, "The village, not the postcard", "Arrive in Pyrgos or, if you insisted on Renos, accept that you are on the rim and over the spirit of the cap.", "Settle and count bedrooms. Shop in the village or in Fira for breakfast things. The apartment is the point of the booking.", "Walk Pyrgos: the lanes up to the castle ruin and the view over the island's center. This is a village view, not a cliff edge.", "Cook, or eat at a taverna in the village. Skip the Oia sunset on night one. You will only be annoyed at what you did not rent.", "Many village lanes are steps. Ask before you arrive with a stroller or a bad knee.", ""),
        day(2, "Fira's public sunset, then home", "See the caldera without pretending the hotel is in Oia.", "Bus to Fira. Walk the rim path, look at the cliff, and do not tour cave hotels you cannot afford.", "Stay for the sunset from a public terrace, then the bus back. Taxis disappear at sunset. Do not plan on one.", "Dinner in Pyrgos. The two-bedroom is a place to eat, not only to sleep.", "The Fira bus station is the system. Learn it on this day.", ""),
        day(3, "A beach that matches the budget", "Kamari or Perissa. Black sand, a bus, tavernas that are not cliff-edge pricing.", "Bus down to Kamari or across to Perissa. Swim. The beach is the nature you get without a hike.", "Lunch at a beach taverna. One grilled dish, not a seafood tower.", "Back to the village before you are stranded at the bus station.", "Kamari is also where a truly cheap room lives. You are visiting, unless the Pyrgos suite missed the budget and you switched.", ""),
        day(4, "Oia as a visitor, for an hour", "Look at the village you did not book. Leave before you start recalculating the mortgage.", "Bus to Oia in the morning, walk the lanes, and bus back. Do not stay for the famous sunset unless you enjoy the crowd and the return.", "Pack, confirm the airport or the ferry, and use the kitchen so the last meal is not a tourist square.", "Out. The Athinios ferry port is a timed descent with a bus. The airport is closer and still a transfer.", "A two-bedroom checkout in Pyrgos is easy. A Grand Suite checkout in Fira still does not make the rate $400.", ""),
    ],
    attractions=[
        sight("Pyrgos", "The inland hill village. Castle lanes and a wide view over the island's middle.", "Stay here if the budget is the rule. Visit the rim. Do not reverse that.", ""),
        sight("Fira rim", "The public caldera walk in the main town. The view is real and it is not attached to your room unless you paid for Renos.", "Sunset buses and taxis are the bottleneck. Go back on a bus you have seen on the schedule.", ""),
        sight("Oia", "The postcard. Worth a morning visit. The wrong place to sleep on this budget.", "Morning, then leave. The sunset crowd is the expensive version of a view you can see from Fira.", ""),
        sight("Kamari beach", "Black sand on the east coast, a bus from Fira or a short ride from Pyrgos.", "The beach day. Umbrellas cost money. The sea does not.", ""),
        sight("Akrotiri", "The buried town on the south coast, if you would rather have archaeology than another sunset.", "Check that the site is open. It is a half day with the bus, not a stop on the way to the airport.", ""),
        sight("Villa Renos Grand Suite", "The Fira exception: a very large caldera suite that might be two rooms and will not be cheap in season.", "Ask them to describe the doors. A loft and a sofa are not two bedrooms.", ""),
    ],
    scenic_routes=[
        route("Pyrgos castle walk", "Up through the village lanes to the old castle and the view, down past a taverna.", "About 2 km of steps and lanes"),
        route("Bus from the village to the Fira rim", "The public bus to Fira, the pedestrian rim, and a bus home that is not the last hopeful taxi.", "20–40 minutes depending on the village stop"),
        route("Bus to Kamari", "Down to the east-coast beach for the swim day, and back in the afternoon.", "About 20–30 minutes"),
    ],
    transport="Buses are the system, and they jam at sunset. A rental car helps a Pyrgos stay and is a burden in Fira. ATVs are a common injury, not a romantic solution. The airport is in the island's middle, closer to Pyrgos than a map of Oia suggests. Ferry arrivals at Athinios need a prebooked ride if you will not carry bags onto a bus.",
    food=[
        dish("Fava", "A taverna in Pyrgos", "Yellow split-pea puree, onion, oil. The island staple. Order it where the menu is not priced for a cliff."),
        dish("Tomato keftedes", "The same village taverna", "Tomato fritters. One plate with the fava is lunch."),
        dish("Apartment tomatoes and cheese", "A grocery in Pyrgos or Messaria", "Chloro cheese, bread, and the tomatoes Santorini actually grows. Two of your four nights should look like this."),
        dish("Grilled octopus", "A taverna at Kamari, on the beach day", "One seafood plate by the sand. It will still cost more than the village. It should not cost Oia sunset prices."),
    ],
    tips=[
        "July and August will not give you a two-bedroom caldera view for $400. Do not book Oia and hope.",
        "Kastro Mansion's two-bedroom is real and can still miss the cap. Astivi is the plainer Pyrgos ask.",
        "Villa Renos counts only if the Grand Suite is two bedrooms on the plan they send you.",
        "Antonia Hotel and Kavalari are real Fira names. They are not, on the evidence, the two-bedroom answer.",
    ],
    faqs=[
        faq("Can we do Oia for $400 with two bedrooms?", "No. Not with a caldera cave, and not in July or August. Visit Oia. Sleep in Pyrgos."),
        faq("Does Villa Renos have two bedrooms?", "It has a Grand Suite of about 100 square meters for up to five people. Confirm two closed bedrooms. The doubles and the junior suite are not this search."),
        faq("Is May really cheaper?", "Yes, relative to July. It can still exceed $400 at a mansion suite. Get the price for your dates in writing."),
        faq("What if every two-bedroom in Pyrgos is taken?", "Move the dates. A Fira double with a sofa is a different product. So is an Oia cave at twice the money."),
    ],
    map_places=[
        stop("Pyrgos", "Pyrgos Kallistis", "Greece", ""),
        stop("Fira", "Fira", "Greece", ""),
        stop("Oia", "Oia", "Greece", ""),
        stop("Kamari", "Kamari", "Greece", ""),
        stop("Villa Renos", "Fira", "Greece", ""),
    ],
    budget_notes="Under $400 is a May or October village apartment, and even then Kastro Mansion or the Renos Grand Suite can overshoot. July and August caldera two-bedrooms are a different budget, often far past the cap. Cook. Buses are cheap. A sunset dinner in Oia is how the daily spend breaks even when the room did not.",
))


add(trip(
    slug="santorini-budget-under-200night",
    title="Santorini under $200: inland Fira, or Kamari if it is actually July",
    location="Santorini, Greece",
    summary=(
        "Two hundred dollars will not buy a private plunge pool in Oia, a cave on the caldera, or a July sunset suite. "
        "In May and October it can buy a plain room in Fira set back from the rim: Golden Star looks east, not into "
        "the crater, and Hotel Daedalus is central with a shared pool and a walk to the view. In July and August the "
        "honest cheap bed is somewhere like Narkissos Hotel in Kamari, a basic beach hotel with no caldera at all. "
        "You visit the rim. You do not sleep on it."
    ),
    who="Travelers who want to see the island once and will not finance the postcard with the room rate.",
    best_time="May and October for a Fira room near this budget. Late April if the hotels are open. July and August in Fira usually break $200. That is when Kamari is the truthful search.",
    nights=3,
    hook="3 nights · Under $200 · No Oia plunge pool",
    constraints=["Under $200", "Fira inland from the rim, or Kamari in July", "No private caldera pool"],
    lodging="$90–200",
    daily="$160–240",
    neighborhoods=[
        stay_area("Fira, east of the rim", "Golden Star faces east, a short walk from the center and a longer walk from the cliff. Daedalus is central, with its own pool, and the caldera is a walk. You go to the view. It is not outside the window."),
        stay_area("Kamari", "The east-coast beach town. Narkissos is a basic hotel a few minutes from the sand. This is the July answer, and it is not a volcano view."),
    ],
    hotels=[
        hotel("Golden Star Hotel", "Fira, east side", "A family hotel a short walk from Fira's center, with a pool and a view to the east, not into the caldera. Shoulder season is when $200 is plausible. A July room with any comfort often is not.", "$100–240", "Fira, Santorini"),
        hotel("Hotel Daedalus", "Central Fira", "A central hotel a few minutes from the rim, the bus station, and the shops, with a shared pool. The website aims higher than the room. You are paying for location, not a cave. Seasonal, roughly spring to autumn.", "$110–260", "Fira, Santorini"),
        hotel("Narkissos Hotel", "Kamari", "Eighteen basic rooms near Kamari beach. This is the hotel that can still behave like a $200 night in summer, because you are not looking at the crater. Use it when Fira has left the budget. Do not expect a caldera breakfast.", "$80–180", "Kamari, Santorini"),
    ],
    itinerary=[
        day(1, "A room without a view, and a walk to the view", "Sleep inland. Watch the sunset on foot.", "Check in at Golden Star or Daedalus. See the east-facing balcony or the pool courtyard so you are not disappointed later.", "Walk to the Fira rim in the late afternoon. The cliff, the cruise ships, the volcano. It is all there, and it is public.", "A souvlaki dinner in town. Back on foot. You are close enough.", "If you are at Narkissos because it is July, this sunset is a bus to Fira and a bus back. Do that once, not three times.", ""),
        day(2, "One real sight, then a beach", "Akrotiri if you want a place, Kamari if you want water. Not both plus Oia.", "Bus to Akrotiri and see the excavated town. It is the ancient city, under a roof, and it is worth the fare.", "Then the beach at Kamari if the timing works, or straight back if the site was enough. Swim where you are.", "Dinner from a counter or a non-view taverna. The caldera restaurants are the splurge this budget does not include.", "Akrotiri's hours change. Check the day before. A closed site is a beach day, and that is fine.", ""),
        day(3, "Oia in the morning, then leave", "See the famous village without paying to sleep in it.", "Bus to Oia early. Walk to the windmill end and back. Buy nothing important.", "Bus back, collect bags, and transfer to the airport or the port. Do not schedule this around the Oia sunset.", "Eat a bakery lunch. The port road is slow.", "What $200 did not buy: a private plunge, a cave, a caldera breakfast, and a reserved sunset table.", ""),
    ],
    attractions=[
        sight("Fira rim", "The free caldera view in the main town. The budget version of the postcard.", "Walk it near sunset once. Eating there is optional and usually a bad use of $200.", ""),
        sight("Oia", "The village you visit for an hour. White lanes, the blue domes, a crowd.", "Go in the morning. The sunset return is when buses and taxis fail.", ""),
        sight("Akrotiri", "The prehistoric town under a modern roof. The substantial sight on the island.", "Half a day with the bus. Confirm it is open.", ""),
        sight("Kamari beach", "Black sand, tavernas, and the reason a July budget still has a swim.", "If you are sleeping in Fira, this is a bus. If you are sleeping at Narkissos, it is the neighborhood.", ""),
        sight("Golden Star's east view", "Sunrise side of Fira, toward the outer island, not the crater. Honest, and sometimes quite nice.", "Walk ten or fifteen minutes for the famous direction. Do not demand it from the pillow.", ""),
        sight("The old port path", "The staircase from Fira down toward the water, if your knees are willing. A walk, not a tour.", "The cable car has a line and a fee. Walking down is easier than walking up.", ""),
    ],
    scenic_routes=[
        route("Fira center to the rim", "From an inland hotel, on foot, to the pedestrian cliff path and back. The entire luxury view, at the price of a walk.", "About 1–2 km"),
        route("Bus to Oia and back", "Morning bus, a walk through the village, an earlier bus home. Not the sunset departure.", "About 30–40 minutes each way"),
        route("Bus to Akrotiri or Kamari", "South to the site or east to the beach. One of these is day two, not both and Oia.", "About 20–30 minutes"),
    ],
    transport="The Fira bus station is the hub. Use it. Taxis at sunset are not a plan. A rental car blows a $200 room rate very quickly and is unnecessary for three nights. The airport transfer is the one taxi worth paying. If you stay in Kamari, every Fira sunset is a bus.",
    food=[
        dish("Souvlaki", "A counter in Fira", "The dinner that keeps the day under control. Pork or chicken, eaten walking, or sitting nowhere with a view."),
        dish("Tyropita", "A bakery on the way to the bus", "Cheese pie for breakfast. Better than a hotel breakfast you paid extra for."),
        dish("Greek salad and a beer", "A taverna off the rim", "Tomatoes, cucumber, feta, oregano. Ask for a table with no view if the view has a cover charge."),
        dish("Beach watermelon", "A shop in Kamari", "The afternoon. Cold, cheap, and more refreshing than a caldera cocktail."),
    ],
    tips=[
        "$200 does not buy a private plunge in Oia. It does not buy a July cave in Fira either.",
        "Golden Star faces east. That is a feature of the price, not a booking error.",
        "Narkissos in Kamari is the summer fallback. You get the beach and lose the crater.",
        "Bus back from Oia before sunset unless you are prepared to wait.",
    ],
    faqs=[
        faq("What does $200 not buy?", "A private pool, an Oia cave, a reserved caldera breakfast, and most Fira rooms in July and August."),
        faq("Is Hotel Daedalus a luxury hotel?", "Its marketing says so. The stay you want is a central room and a shared pool, a walk from the rim. Judge it by the rate on your dates."),
        faq("Can I see the sunset without a view room?", "Yes. Walk to the Fira rim. It is the same sun."),
        faq("Is Kamari a downgrade?", "It is a different trip: a beach town, basic rooms, and a bus to the view. In July it is often the only way the budget is real."),
    ],
    map_places=[
        stop("Fira", "Fira", "Greece", ""),
        stop("Kamari", "Kamari", "Greece", ""),
        stop("Oia", "Oia", "Greece", ""),
        stop("Akrotiri", "Akrotiri", "Greece", ""),
        stop("Fira bus station", "Fira", "Greece", ""),
    ],
    budget_notes="Shoulder-season Fira rooms can sit under $200 if they do not face the caldera. July and August often do not, which is why Narkissos in Kamari is on the list. Food is the other leak: one rim dinner can cost as much as the room you were proud of saving on. Buses are the cheap part. Add the airport taxi.",
))


add(trip(
    slug="santorini-mountain-or-nature-view",
    title="Santorini's view is a volcanic cliff, not a green mountain",
    location="Santorini, Greece",
    summary=(
        "Santorini is a flooded volcanic crater. The 'mountain' is the caldera wall: dark rock, a drop to the water, "
        "and almost no forest. Stay where that wall is real. Kavalari is a cave hotel on the Fira rim, Hotel Galini "
        "is in Firostefani on the same rim, and Astra Suites sits higher at Imerovigli with a shared infinity pool "
        "over the drop. Hike Fira to Oia only if you like sun and no shade. Akrotiri is the ancient town. A boat "
        "to the volcanic islet is cinders and sulfur, not a nature reserve."
    ),
    who="People who want the cliff, the hike, and the volcano, and will not pretend the island is alpine or lush.",
    best_time="Late April to June, or September into early October. The hike is punishing in July and August. Many rim hotels close in winter. The crater looks like itself in every open month.",
    nights=4,
    hook="4 nights · Caldera rim · Hike, ruins, volcanic islet",
    constraints=["A real caldera or village view", "The Fira–Oia hike is exposed", "Red Beach only if the path is actually open"],
    lodging="$200–700",
    daily="$320–480",
    neighborhoods=[
        stay_area("Fira and Firostefani", "Kavalari is on the Fira cliff. Galini is in Firostefani, about a kilometer along the rim. You can walk the path between them."),
        stay_area("Imerovigli", "The highest part of the caldera rim. Astra Suites is here, with the view and a shared cliff pool. Skaros rock sits below the village."),
    ],
    hotels=[
        hotel("Kavalari Hotel", "Fira caldera", "A former captain's house cut into the Fira cliff, with terraces over the old port and the volcano. The view is the product. The rooms are cave rooms, not a green-mountain lodge. Book the caldera side.", "$220–520", "Fira, Santorini"),
        hotel("Hotel Galini", "Firostefani", "A smaller hotel on the rim in Firostefani, between Fira and Imerovigli. You are on the cliff path. It is a simpler stay than Astra, with the same direction of view.", "$160–360", "Firostefani, Santorini"),
        hotel("Astra Suites", "Imerovigli", "Suites high on the Imerovigli cliff, looking at the caldera and the volcanic islets. The infinity pool is shared, not a private plunge, and the path is stepped. This is the view hotel, at a view price.", "$400–900", "Imerovigli, Santorini"),
    ],
    itinerary=[
        day(1, "Learn the rim you are sleeping on", "Arrive and walk only as far as the next village. The long hike is tomorrow.", "Settle at Kavalari, Galini, or Astra. Walk the rim path until you understand the drop. Imerovigli is the high point.", "Skaros, the rock below Imerovigli, is the short hike if you want one before dinner. It is a path down and up, not a casual stroll in sandals.", "Dinner with the view once, because that is why you paid. The rest of the nights can be plainer.", "The rim path has steps and no guardrail in places. After dark, watch your feet.", ""),
        day(2, "Fira to Oia on foot", "The island's famous walk. About ten kilometers, three to four hours, in full sun, with no shade and no forest.", "Start early from Fira. Water, a hat, and shoes. The path follows the rim through Firostefani and Imerovigli and then gets lonelier and hotter.", "Arrive in Oia, look around, and take the bus back. Do not walk back.", "A quiet dinner at the hotel end. You will be tired and sunburned if you treated this like a garden path.", "July and August add heat and other hikers. There is no water on the middle of the path unless a café happens to be open.", ""),
        day(3, "Akrotiri, not the unstable red cliff", "The ancient city is the sure thing. The red beach has been closed and reopened as the cliff allows.", "Bus to Akrotiri and see the site properly. It is covered, which matters on a hot day.", "If, that week, the path to Red Beach is officially open and not running under a fresh collapse, you may look. If it is closed, do not improvise. Perissa or a quiet south-coast swim is the alternative.", "Back to the rim for sunset from your own village.", "Check the beach closure the same morning. A photograph is not worth a rockfall.", ""),
        day(4, "The volcanic islet", "A boat from the old port or from Ammoudi. Nea Kameni is a cinder cone in the middle of the caldera. Palea Kameni has a hot-water swim.", "Book a small boat that says where it lands. Walk the path on Nea Kameni if you want the crater floor. It is hot, exposed, and smells of sulfur.", "Swim at Palea Kameni if the boat includes it. Then back. The climb from Fira's old port up to the town is the hard part. Use the cable car if your legs are gone.", "Departure transfer. A boat morning plus a flight needs a margin.", "This is the volcano. It is not a green mountain and it is not a surprise you can add after a late breakfast.", ""),
    ],
    attractions=[
        sight("Imerovigli rim", "The highest cliff of the caldera. Rock, sea, and the islands in the crater.", "Astra's shared pool looks at it. The public path does too. The pool is not private.", ""),
        sight("Fira to Oia path", "The rim hike. White villages, then open hillside, then Oia.", "Start early. Bus back. Ten kilometers, no shade.", ""),
        sight("Kavalari's cliff", "The Fira view from a real cave hotel: old port below, volcano ahead.", "Book a caldera room. A back room in the same hotel is a different stay.", ""),
        sight("Skaros", "The rock and ruined Venetian fort below Imerovigli.", "A short, steep path. Good on the arrival day. Not instead of water on the long hike.", ""),
        sight("Akrotiri", "The Bronze Age town under a roof. The human history of the volcano.", "Give it a real visit. It is not a photo stop on the way to a beach.", ""),
        sight("Nea Kameni", "The volcanic islet in the caldera. Black rock, a crater path, sulfur.", "Boat there. Do not expect trees. Palea Kameni's warm swim is the softer part of the same trip.", ""),
    ],
    scenic_routes=[
        route("Fira to Oia on the rim", "The caldera path through Firostefani and Imerovigli to Oia. Bus back from Oia. Water and an early start.", "About 10 km, 3–4 hours"),
        route("Imerovigli to Skaros", "Down from the village to the rock and back up. The short version of the island's terrain.", "About 2–3 km, steep"),
        route("Boat to the volcanic islets", "From Fira's old port or Ammoudi to Nea Kameni and, if the ticket says so, Palea Kameni. Cable car back up to Fira if you need it.", "A half day on the water"),
    ],
    transport="Walk the rim between Fira, Firostefani, and Imerovigli. Buses for Akrotiri, Oia after the hike, and the airport. The old port is a cable car, a steep walk, or a donkey you do not have to use. A car is optional if you sleep on the rim and only leave for Akrotiri and the boat. Book the boat the day before in busy months.",
    food=[
        dish("Fava and tomatoes", "A taverna in Imerovigli or Firostefani", "The local plate after you have looked at the view long enough. Eat it once with the cliff and once without, and compare the bill."),
        dish("Assyrtiko", "A village taverna, not a flight of expensive pours", "The island's white wine. One glass with lunch. A caldera tasting menu is a different budget."),
        dish("Grilled fish", "The dinner you book on night one", "Because you came for the rim, have one meal on it. Ask the price. Then eat more simply."),
        dish("Fruit and water for the hike", "A shop in Fira, the night before", "Buy it before the morning. There is no forest kiosk on the path."),
    ],
    tips=[
        "The landscape is a volcanic cliff. If you wanted pines and a summit meadow, this is the wrong island.",
        "Astra's pool is a shared infinity pool. It is a fine way to see the caldera. It is not your private pool.",
        "The Fira–Oia hike is sun, wind, and other people. Start early and take the bus back.",
        "Red Beach's path has been closed after rockfalls. If it is closed, Akrotiri is still the day.",
    ],
    faqs=[
        faq("Is there a green mountain to climb?", "No. The high ground is the caldera rim at Imerovigli, and the hike to Oia is along that rim. The center of the island is volcanic farmland and villages."),
        faq("Is the boat to the volcano worth it?", "Yes, once, if you want to stand on the crater that made the view. It is hot and bare. The swim at Palea Kameni is the pleasant half."),
        faq("Which hotel is actually on the cliff?", "Kavalari in Fira, Galini in Firostefani, and Astra Suites in Imerovigli. A hotel in Kamari or the middle of the island is a beach or village stay."),
        faq("Can I hike in July?", "You can, at sunrise, with more water than you think. The path does not grow shade in summer."),
    ],
    map_places=[
        stop("Imerovigli", "Imerovigli", "Greece", ""),
        stop("Fira", "Fira", "Greece", ""),
        stop("Oia", "Oia", "Greece", ""),
        stop("Akrotiri", "Akrotiri", "Greece", ""),
        stop("Nea Kameni", "Nea Kameni", "Greece", ""),
    ],
    budget_notes="Rim hotels span a wide range. Galini can be a moderate cliff stay. Kavalari is a caldera cave and prices like one in season. Astra is the expensive view, with a shared pool. The hike is free. Akrotiri and the boat are the tickets. One dinner on the rim is justified. Four of them will cost more than upgrading the room.",
))


add(trip(
    slug="santorini-pet-friendly",
    title="Santorini with a dog: three published yeses, and the caves that say no",
    location="Santorini, Greece",
    summary=(
        "Most caldera cave hotels on Santorini refuse pets, and a booking-site filter is not a policy. Three places "
        "publish a yes. NOŪS in Mesaria, on its Marriott page, allows one pet up to 10 kg and charges about €50 to "
        "clean. Ethos Vegan Suites in Fira lists pets allowed and prints no weight limit. Cally Cave House in Mesa "
        "Katikies says on its own site that pets are allowed, and guests describe a shared pool with no caldera view. "
        "None of that replaces a written yes for your dates, your animal, and the fee. The rim path is a bad place "
        "to discover a no."
    ),
    who="People traveling with a dog who would rather sleep inland than be turned away from a cave hotel.",
    best_time="May, early June, and late September or October, after the hotel has confirmed the pet in writing. Midsummer heat on black stone is hard on a dog, and August cave hotels are the least likely to make an exception.",
    nights=4,
    hook="4 nights · A written pet yes · Not a caldera cave",
    constraints=["Confirm the pet policy in writing", "One published yes is not a guarantee", "Most rim hotels are a no"],
    lodging="$160–500",
    daily="$250–380",
    neighborhoods=[
        stay_area("Mesaria", "Inland, near the airport road. NOŪS is here: gardens, a hotel pool, and no cliff. This is the practical base with a dog."),
        stay_area("Fira, off the rim", "Ethos and Cally are in Fira, not on the postcard edge. Cally's guests mention a walk of about ten or fifteen minutes to the square and no view from the pool."),
    ],
    hotels=[
        hotel("NOŪS Santorini", "Mesaria", "A Design Hotels property on the road through Mesaria. Marriott's page says one pet up to 10 kg, with an extra cleaning fee of about €50. It advertises pools and gardens. Assume a shared pool unless your confirmation names a private one. This is not a caldera cave.", "$280–600", "Mesaria, Santorini"),
        hotel("Ethos Vegan Suites", "Fira", "Suites in Fira with jacuzzis, and a booking page that lists pets allowed. No weight and no fee are printed there. Get both in writing, plus whether the dog can be on the balcony. Vegan breakfast is their other actual policy.", "$180–420", "Fira, Santorini"),
        hotel("Cally Cave House", "Mesa Katikies, Fira", "Four suites in a cave house, a shared pool, about a ten to fifteen minute walk from Fira square. The house site says pets are allowed. Guests describe it as quiet and without a caldera view. Email them the size of the dog before you pay.", "$150–360", "Fira, Santorini"),
    ],
    itinerary=[
        day(1, "Confirm the dog, then leave the rim alone", "The first job is the hotel's yes, already in your email, and a plan that does not depend on cliff restaurants.", "Arrive by a transfer you have told about the animal. Settle. Walk the dog in the village or the hotel grounds, not on the caldera edge at sunset.", "A short outing to a shop for water, food for the dog, and your own dinner supplies. Many terraces will say no.", "Eat at the hotel if they confirmed the dog can be there, or eat what you bought. Do not march a dog through Fira's sunset crowd hoping for a table.", "Carry water. The ground holds heat. Midday walks in July are a bad idea even if the hotel said yes.", ""),
        day(2, "A beach only if someone local says yes", "I will not invent a dog beach. Ask the hotel that already accepted the animal.", "Use the morning, when the ground is cooler. If the hotel names a cove or a stretch that allows dogs, go there. If they do not, a shady village walk is the day.", "The archaeological site and the rim path are poor bets with a dog. Skip Akrotiri unless you have written permission, which you probably will not.", "Back before the stones are at their hottest. Dinner as on night one.", "If the answer on the beach is vague, treat it as a no. A confrontation on a beach is how the trip sours.", ""),
        day(3, "One caldera look, without a reservation you cannot use", "See the view the way a person without a dog does, briefly, and have a plan for the animal.", "Early walk to a viewpoint if the dog can come, or one person goes to the Fira rim while the other stays in the shade. Do not leave a dog in a hot room or a hot car.", "A drive or a taxi to a quiet inland spot the hotel suggests. Pyrgos is pleasant and not automatically welcoming to dogs in its tavernas.", "Repeat the dinner arrangement you already know works.", "Never assume a church, a cave shop, or a sunset bar is fine with a dog because the street is public.", ""),
        day(4, "The flight rules, then the airport", "The hotel yes does not govern the airline.", "A last cool walk. Pack the papers the airline asked for. Confirm the transfer will take the dog.", "Airport with time. Mesaria is close to the airport, which is a reason NOŪS is the easy base.", "You are done. If any hotel along the way tried to renegotiate the pet, that email thread is why you kept it.", "Read the airline's crate and weight rules before you are at the counter.", ""),
    ],
    attractions=[
        sight("Mesaria", "An inland village that can be a base. NOŪS is the hotel here with a published pet rule.", "You are not on the crater. That is why the stay is possible.", ""),
        sight("Fira, off the rim", "The town, reached on foot from Ethos or Cally, without assuming the famous path wants a dog.", "Go early. Shade and water. Leave before the sunset crush.", ""),
        sight("A hotel-confirmed cove", "The only beach I will recommend is the one your hotel names, in writing, for a dog.", "If they have no name, do not crowdsource it from a terrace.", ""),
        sight("Pyrgos", "A hill village you can visit if the dog is welcome in the car and you do not need a taverna table.", "Lanes are steps. Many dining rooms will refuse you. Look, and leave.", ""),
        sight("The caldera rim", "The view, seen briefly, by one person if the dog cannot come.", "Do not make the dog walk the Fira–Oia path. It is long, hot, and waterless.", ""),
        sight("Santorini airport", "Close to Mesaria. The practical advantage of the inland yes.", "Tell the transfer company about the animal when you book it, not at the curb.", ""),
    ],
    scenic_routes=[
        route("Cool morning walk from the hotel", "A short loop the hotel says is all right, with water, before the ground heats. The route is local and boring and that is correct.", "Under 3 km"),
        route("One early look at the Fira rim", "From Cally or Ethos toward the cliff, early, and back. Skip it if the dog is unwelcome or the day is hot.", "About 2 km"),
        route("Airport transfer with the dog already declared", "Mesaria to the airport is a short ride. The paperwork is the longer job.", "A few minutes from Mesaria"),
    ],
    transport="A hotel transfer that knows about the dog, or a rental car if the company allows the animal. Buses are a poor bet with a dog and not something to gamble on. Taxis may refuse. Do not plan the Fira–Oia hike. The airport is the easy part if you stay in Mesaria.",
    food=[
        dish("Hotel terrace meal", "Only if the written confirmation includes the dog", "This is the reliable dinner. A cave restaurant in Oia is not."),
        dish("Takeaway gyros", "A Fira shop, eaten back at the room", "The backup when the terrace is for people only. Buy it, do not negotiate it."),
        dish("Tomato, bread, and cheese", "A grocery", "Lunch that does not require a restaurant policy. You will use this more than once."),
        dish("Water and the dog's usual food", "Bought on day one", "Do not assume a shop in Oia stocks the right food. Bring the staple from home and refill water constantly."),
    ],
    tips=[
        "Get the pet policy in writing: weight, number, fee, where the animal may walk, and what happens if they refuse on the day.",
        "NOŪS states 10 kg and a cleaning fee. Ethos and Cally say yes without those details. Ask.",
        "Most caldera hotels are a no. Do not book one and write 'small dog' in the comments.",
        "Do not leave a dog in a parked car, on a balcony in full sun, or on the Fira–Oia path.",
    ],
    faqs=[
        faq("Will you confirm the pet policy for me?", "No. You must confirm it in writing with the hotel for your dates. A website line and this page can both go stale."),
        faq("Can I stay in an Oia cave with a dog?", "Assume no. The hotels on this list are in Mesaria and in Fira off the rim. If an Oia hotel tells you yes in writing, you have something I did not find."),
        faq("Is the NOŪS rule the whole policy?", "Marriott's page says one pet, up to 10 kg, and a cleaning charge of about €50. Confirm it still applies to your rate plan."),
        faq("What if the hotel reneges?", "That is why the email matters, and why you should not fly on a filter checkbox. Have a second inland option before you travel."),
    ],
    map_places=[
        stop("NOŪS Santorini", "Mesaria", "Greece", ""),
        stop("Ethos Vegan Suites", "Fira", "Greece", ""),
        stop("Cally Cave House", "Fira", "Greece", ""),
        stop("Fira", "Fira", "Greece", ""),
        stop("Pyrgos", "Pyrgos Kallistis", "Greece", ""),
    ],
    budget_notes="NOŪS is a design hotel, not a budget kennel, and the pet fee is extra. Ethos and Cally can be less. None of the rates include a surprise no at the door, which is an expensive problem. Budget taxis that will take a dog, or a rental car that allows one. Restaurant choice is limited, so groceries are part of the plan.",
))


add(trip(
    slug="mykonos-city-center-walkable",
    title="Mykonos Town on foot: Little Venice, the windmills, and the noise",
    location="Mykonos, Greece",
    summary=(
        "Mykonos Town, Chora, is genuinely walkable: Little Venice, the windmills, and Matogianni street are minutes "
        "apart, and the lanes are for people, not cars. It is also loud at night in season. Hotel Leto faces the old "
        "harbor. Hotel Matogianni is on the shopping street itself. Belvedere is the pricier hotel just above town, "
        "a walk down into the lanes rather than a step onto them. Sleep here if you want the town. Do not expect quiet."
    ),
    who="A couple or two friends who want to walk out at night and do not need a beach at the door.",
    best_time="May, early June, and September. You can walk, eat, and sleep. July and August the same streets are a party until late, and the hotels on them are priced for that.",
    nights=3,
    hook="3 nights · Chora on foot · Loud after dark",
    constraints=["Walkable town", "Noise included", "No car in the lanes"],
    lodging="$200–600",
    daily="$300–450",
    neighborhoods=[
        stay_area("Chora, on the harbor and Matogianni", "Leto is by the old harbor. Matogianni Hotel is on Matogianni street. Little Venice and the windmills are a short walk. So are the bars."),
        stay_area("Just above town", "Belvedere sits up the hill, near the School of Fine Arts side, with a view over Chora. You walk down. You are not in the middle of the shout."),
    ],
    hotels=[
        hotel("Hotel Leto", "Old harbor, Chora", "A classic town hotel by the old harbor, with a pool and balconies toward the water, a few minutes from Little Venice. Central, and therefore not quiet in July.", "$200–480", "Mykonos Town"),
        hotel("Hotel Matogianni", "Matogianni street", "On the street the town walks and shops. You are in the middle of Chora, which is the walkable point and the reason earplugs exist in August.", "$220–520", "Mykonos Town"),
        hotel("Belvedere Hotel", "Above Chora", "The famous hotel just above town. Pricier than Leto or Matogianni, with a view over the roofs, and a walk down into the lanes. Choose it if you want the town without sleeping on Matogianni.", "$400–900", "Mykonos Town"),
    ],
    itinerary=[
        day(1, "The three pictures, on foot", "Little Venice, the windmills, and one street. That is the town.", "Drop bags. Walk to Little Venice in the afternoon light, then along the water to the windmills. The distance is minutes.", "Matogianni and the lanes behind it. Get lost once, on purpose. The town is small enough that the harbor puts you right.", "Dinner in town, early enough to get a table, then a walk. If it is July, the volume rises after ten. That is the place, not a surprise.", "Scooters in the lanes are a hazard. Walking is the correct speed.", ""),
        day(2, "Delos in the morning, town again at night", "The serious day trip is the island of Delos, if the boats are running. The town is still your bed.", "A morning boat to Delos. The site needs a couple of hours. The sea has to cooperate. If the boat is cancelled, Megali Ammos is a beach you can walk to from town.", "Back in the afternoon. A swim if you skipped Delos, or a long coffee if you went.", "Night in Chora again. You already know the way home.", "Delos tickets and the boat are a pair. Do not plan it for the last morning before a flight.", ""),
        day(3, "Paraportiani, a walkable swim, and the boat out", "A last morning that is still in town.", "The church of Paraportiani in the Kastro quarter, early, before the poseurs and after the cleaners. Whitewash and a square.", "Walk to Megali Ammos for a swim if you want water without a bus. It is the closest beach. Ornos is a bus and a longer commitment.", "Collect bags and leave from the old port or a taxi to the new port or airport. Walking with luggage through Matogianni at noon is the bad version.", "The airport is close to town and the traffic is not. Leave a margin.", ""),
    ],
    attractions=[
        sight("Little Venice", "The row of houses over the water on the west edge of Chora. The town's postcard, and a five-minute walk from a town hotel.", "Go in the afternoon. The bars want you to stay for sunset. A walk does not require a drink.", ""),
        sight("Kato Mili windmills", "The windmills on the ridge above Little Venice.", "They are a viewpoint over town and the sea. The walk up is short.", ""),
        sight("Matogianni street", "The main walk of shops and people. Staying on it means you are never lost and never quite asleep.", "Useful by day. Loud by night in season.", ""),
        sight("Paraportiani", "The whitewashed church cluster in the Kastro, the quietest famous corner in the early morning.", "Go early. Midday it is a photo queue.", ""),
        sight("Delos", "The archaeological island in the strait. The one outing that is not a beach club.", "Morning boat, a real visit, back. Check the sea.", ""),
        sight("Megali Ammos", "The beach you can walk to from Chora. Not the famous club beach. Enough for a swim.", "Afternoon, then walk back for dinner. Ornos and Psarou are bus beaches.", ""),
    ],
    scenic_routes=[
        route("Harbor, Little Venice, windmills", "From the old harbor along the water, through Little Venice, up to the windmills, and back by Matogianni.", "About 2 km, an hour if you stop"),
        route("Boat to Delos", "A morning excursion from the old harbor, time on the site, and the boat home. Weather can cancel it.", "A half day"),
        route("Chora to Megali Ammos", "A walk south from town to the first beach and back. The swim that does not need the bus station.", "About 20–30 minutes each way"),
    ],
    transport="Your feet. The lanes of Chora are pedestrian, with the occasional scooter you should not imitate. Buses to Ornos and the rest leave from the Fabrika station at the edge of town. The old port is for Delos and some ferries. The new port at Tourlos is for many big ferries, and it is a taxi, not a romantic walk with bags. The airport is close and the road is busy.",
    food=[
        dish("Kopanisti and bread", "A taverna in Chora, not a beach club", "The spicy local cheese. Order it first, with tomatoes, before you order a grilled fish you do not need."),
        dish("Louza", "The same table", "Cured pork from the island. A plate of kopanisti, louza, and salad is a meal."),
        dish("Tyropita", "A bakery on the morning walk", "Cheese pie, warm. Breakfast, eaten outside, before the shops open fully."),
        dish("A plain taverna dinner", "A lane behind Matogianni", "Grill or a baked dish and a salad. Little Venice at sunset is a drink, if you want one, not the best dinner."),
    ],
    tips=[
        "The town is walkable and loud. If you need sleep, Belvedere is up the hill. Matogianni is the noise.",
        "July and August prices at Leto and Matogianni are not the May prices, and the music does not end at eleven.",
        "Delos is the worthwhile boat. A beach club is optional and expensive.",
        "Do not drive into Chora. You will not park, and you do not need to.",
    ],
    faqs=[
        faq("Is Mykonos Town actually walkable?", "Yes. Little Venice, the windmills, Matogianni, the old harbor, and Paraportiani are all on foot. Beaches beyond Megali Ammos are a bus."),
        faq("Will it be quiet?", "Not in July or August, and not on Matogianni. May and September are kinder. Belvedere is quieter than a room over the main street and still not a rural hotel."),
        faq("Is Belvedere in the center?", "It is just above Chora, a walk down. You can do the whole itinerary without a taxi. You are not on the harbor."),
        faq("Do I need a beach hotel instead?", "Only if the beach is the point. This page is the town. Ornos and Psarou are a different stay."),
    ],
    map_places=[
        stop("Little Venice", "Mykonos", "Greece", ""),
        stop("Kato Mili", "Mykonos", "Greece", ""),
        stop("Matogianni street", "Mykonos", "Greece", ""),
        stop("Paraportiani", "Mykonos", "Greece", ""),
        stop("Delos", "Delos", "Greece", ""),
    ],
    budget_notes="A town hotel in May or September might sit around $200–350. In July and August, Leto and Matogianni often leave that behind, and Belvedere was never the cheap choice. Walking saves taxis. Delos is a paid boat. A cocktail in Little Venice is optional. Dinner in a plain taverna keeps the day from doubling.",
))


add(trip(
    slug="mykonos-budget-under-200night",
    title="Mykonos under $200: a plain town room, and not in July",
    location="Mykonos, Greece",
    summary=(
        "A private room in Mykonos under $200 is a shoulder-season fact, not a July one. Hotel Philippi, on Kalogera "
        "since the 1960s, and Carbonaki, on Panachradou since 1961, are the modest town hotels. Even a 2020 rate "
        "card at Carbonaki already had peak doubles near €170, so 2026 in July is not this budget. Hotel Leto, on "
        "the old harbor, is the real town hotel that shows what $200 does not buy once the season starts: a sea-view "
        "balcony and a pool. You still walk to Little Venice. You skip the beach clubs."
    ),
    who="Travelers who want Chora without a beach-club bill and will come in May or late September.",
    best_time="May, early June, late September, and October if the hotels are open. From mid-June through early September, a private room in town usually leaves $200. A dorm might not. This list is not a dorm.",
    nights=3,
    hook="3 nights · Under $200 · Shoulder, or it fails",
    constraints=["Under $200", "A room in town without a famous view", "July prices told plainly"],
    lodging="$100–200",
    daily="$170–250",
    neighborhoods=[
        stay_area("Chora, off the harbor view", "Kalogera and Panachradou are in town and not on the water. You walk to everything. You do not pay for the windmill outside the window."),
        stay_area("The old harbor, if you abandon the cap", "Hotel Leto is the prettier town address. Use it when the date is cheap enough, and do not pretend July still is."),
    ],
    hotels=[
        hotel("Philippi Hotel", "25 Kalogera, Chora", "A family hotel in the lanes since 1964, with a garden and ordinary double rooms. This is the modest town stay. In May it can fit. In July it often will not, even without a view.", "$110–260", "Mykonos Town"),
        hotel("Carbonaki Hotel", "Panachradou 23, Chora", "A small hotel in town since 1961, with a little pool and no famous vista. A 2020 official list already put peak doubles near €170. Treat that as evidence, not as today's price. July now is over $200.", "$120–280", "Mykonos Town"),
        hotel("Hotel Leto", "Old harbor, Chora", "The harbor hotel with a pool and sea-facing balconies, a short walk from Little Venice. It is the honest comparison: a better room, and the one that leaves this budget as soon as the island is busy.", "$200–480", "Mykonos Town"),
    ],
    itinerary=[
        day(1, "The town, from a back street", "You are in Chora. The room is plain. The walk is the same one richer people take.", "Check in on Kalogera or Panachradou. Walk to Little Venice and the windmills in the afternoon. The route does not charge admission.", "Matogianni for the orientation, then out of it. A bakery breakfast you missed can be a late lunch.", "Dinner at a taverna without a view. Sleep will depend on the month. In May the lanes calm down. In July they do not, even at a budget hotel.", "If Leto was the only room left under the cap, you got lucky on the date. Do not expect that in August.", ""),
        day(2, "A bus beach, not a club", "Ornos or Agios Stefanos. Sand, a bus from the Fabrika station, and no reserved daybed.", "Bus to Ornos. Swim from the free part of the beach. The clubs at Psarou and Paraga are a different economy. You can see them and not enter.", "Back to town in the afternoon, before you are paying for shade you did not need.", "Souvlaki or a salad. The money you did not spend on a sunbed is the point.", "Buses get crowded when the beach day ends. Go a little earlier than everyone else.", ""),
        day(3, "One more walk, then a realistic exit", "You have seen the town. Do not add a boat you cannot afford.", "Paraportiani in the morning, a coffee, and the bags.", "If the flight is late, repeat the windmill walk. Skip Delos unless the boat is already paid and cheap on that date.", "Airport or port with a margin. Taxis cost more when you are late.", "Three nights under $200 only works if the room was booked in the shoulder. The last day cannot fix a July rate.", ""),
    ],
    attractions=[
        sight("Little Venice", "Still worth walking to. The budget version is a walk, not a reserved lounger in front of it.", "Go once, late afternoon. You do not need a cocktail to have been there.", ""),
        sight("Kato Mili", "The windmills. A free viewpoint over town.", "Combine with Little Venice. It is one walk.", ""),
        sight("Philippi's garden", "The modest pleasure of the cheap hotel: a planted courtyard in town, not a caldera.", "Use it in the afternoon if the beach bus was enough.", ""),
        sight("Ornos beach", "A sandy bay on the bus. The swim that does not require a club minimum.", "Sit on a towel. The front row of sunbeds is the upsell.", ""),
        sight("Paraportiani", "The white church, best early, and free.", "A last morning. It photographs better before the tour groups.", ""),
        sight("Fabrika bus station", "The unglamorous hub that makes a town hotel able to reach a beach.", "Learn the Ornos bus on day one.", ""),
    ],
    scenic_routes=[
        route("Kalogera to Little Venice and the windmills", "Through the lanes to the water and up to the mills. The same walk as the expensive hotels, from a cheaper door.", "About 2 km"),
        route("Fabrika bus to Ornos", "The public bus to a sandy beach and back. No scooter required.", "About 15 minutes"),
        route("Early loop to Paraportiani", "A short morning walk in the Kastro before departure.", "Under 2 km"),
    ],
    transport="Walk in town. The bus to the beach. One taxi for the airport if the bus timing is wrong. A rental car or an ATV will erase the hotel savings and is unnecessary for three nights. Do not take a cab to Little Venice.",
    food=[
        dish("Tyropita", "A bakery in Chora", "Breakfast for a few euros. The hotel breakfast is often extra and not worth it at this budget."),
        dish("Souvlaki", "A counter off Matogianni", "Dinner at least once. Pork, bread, tomato. Sit somewhere without a minimum."),
        dish("Greek salad", "A taverna with no sea view", "The sit-down meal. One, not every night. Tomatoes and feta are enough."),
        dish("Fruit from a mini-market", "Near Kalogera", "The afternoon. Cheaper than a beach bar and better in a hot room."),
    ],
    tips=[
        "July is not $200 for a private room in town. Carbonaki's own old price list was already near the cap at the peak.",
        "Hotel Leto is on the list so you can see the next step up. It is not the budget default in season.",
        "Beach clubs are how a cheap room becomes an expensive day. Swim at Ornos and leave.",
        "The town is still loud in summer even when the room was cheap.",
    ],
    faqs=[
        faq("Can I do Mykonos in July for $200 a night?", "A private room in Chora, usually no. A shoulder-season room at Philippi or Carbonaki, sometimes yes. A sea view at Leto in August, no."),
        faq("What does the budget not include?", "Nammos, a daybed, a pool suite, and a July harbor view. It includes the walk to Little Venice."),
        faq("Is a hostel the real answer?", "A dorm bed can be under $200 in summer and it is a different trip. These three are hotels with private rooms."),
        faq("Where should I swim?", "Ornos by bus, or Megali Ammos on foot. Not a club beach."),
    ],
    map_places=[
        stop("Kalogera", "Mykonos", "Greece", ""),
        stop("Little Venice", "Mykonos", "Greece", ""),
        stop("Ornos", "Ornos", "Greece", ""),
        stop("Paraportiani", "Mykonos", "Greece", ""),
        stop("Fabrika bus station", "Mykonos", "Greece", ""),
    ],
    budget_notes="The cap holds in May and late September at a plain town room, if you book it. July and August break it, which a pre-pandemic peak rate near €170 already hinted at. Keep food at bakeries and one taverna. A single beach-club afternoon can cost more than the three nights you saved. Airport taxis are the fair extra.",
))


add(trip(
    slug="mykonos-2-bedroom-under-400night",
    title="A two-bedroom on Mykonos under $400 is Ano Mera, not a beach villa",
    location="Mykonos, Greece",
    summary=(
        "A two-bedroom villa on a Mykonos beach under $400 is an August fantasy. The booking that can exist is inland, "
        "in Ano Mera, in May or October. Sofos Suites has a two-level family suite with two bedrooms, about 45 square "
        "meters, which is tight. Mykonian Breeze lists a two-bedroom apartment around 60 square meters, about 7 km "
        "from Chora, plus studios that do not count. Santa Marina on Ornos Bay has real multi-room villas and they "
        "are far above this cap in every month you want the beach. You will want a car or taxis."
    ),
    who="Families or two couples who need two rooms and will stay in a village instead of on Ornos.",
    best_time="May and October. June and September can work at Ano Mera and fail at the beach. July and August villas at Ornos, Psarou, or Agios Ioannis are a different budget.",
    nights=4,
    hook="4 nights · Two bedrooms in Ano Mera · Not an August villa",
    constraints=["Two bedrooms", "Under $400 in the shoulder", "Inland village, car or taxis"],
    lodging="$180–400",
    daily="$280–400",
    neighborhoods=[
        stay_area("Ano Mera", "The inland village, about 7 km from Chora. A square, tavernas, and the monastery of Panagia Tourliani. This is the two-bedroom product. It is not walkable to Little Venice."),
        stay_area("Ornos, as the warning", "Santa Marina's villas are the famous two-bedroom-and-more on the beach. They explain the search, and they do not fit the price."),
    ],
    hotels=[
        hotel("Sofos Suites", "Ano Mera", "Suites and maisonettes a walk from Ano Mera square. The Two Levels Family Suite is the one with two separate bedrooms, about 45 square meters. Their site calls the place luxury. Shoulder season is when $400 is plausible. The size is modest. Studios and one-bedroom suites are not the booking.", "$180–450", "Ano Mera, Mykonos"),
        hotel("Mykonian Breeze", "Ano Mera", "Apartment hotel about 7 km from Chora. Listings include a two-bedroom of about 60 square meters as well as smaller studios. Book the two-bedroom and confirm it on the hotel's own paper. A cheap 'from' price in winter is not an August rate. The property has said it does not take pets.", "$170–420", "Ano Mera, Mykonos"),
        hotel("Santa Marina Mykonos", "Ornos Bay", "A Luxury Collection resort with villas on Ornos Bay. A two-bedroom here is real and it is not a $400 night in May, July, or any other month you actually want a beach club nearby. Named so it is not confused with an Ano Mera apartment.", "$700–1600", "Ornos, Mykonos"),
    ],
    itinerary=[
        day(1, "Count the bedrooms, then the square", "Arrive in Ano Mera and make sure you rented two rooms.", "Check in. Open both bedroom doors. A sofa in the living room is a failed booking. Shop for breakfast at the village.", "Walk to Ano Mera square and the monastery courtyard if it is open. This is the neighborhood.", "Cook, or eat at a taverna on the square. Chora can wait. You are not walking there after dark.", "Taxis from the airport to Ano Mera should be booked, not assumed, when you land with luggage.", ""),
        day(2, "A beach by bus or car, and back", "One swim, from a village base. Not a relocation to the beach.", "Drive or bus toward Agia Anna, Ornos, or Kalafati. Swim where you do not have to buy a bed. Look at Santa Marina from the sand if you are curious. Do not go in and rebook.", "Lunch at a beach taverna that is not a club. One plate.", "Back to Ano Mera for the evening. The two-bedroom is useless if you stay in town until 2 a.m. without a way home.", "Parking in Chora is not the plan. If you have a car, leave it in the village and taxi in on the town night.", ""),
        day(3, "Chora for the evening, with a ride home", "The town walk, done from a village.", "A slow morning at the apartment. Little Venice does not need your whole day.", "Afternoon taxi or bus to Chora. Windmills, Little Venice, a walk. Leave before you are stranded.", "Dinner in Ano Mera, not a second dinner in town. You already know the kitchen.", "The last bus is a fact. Learn it before you go in.", ""),
        day(4, "Delos only if the timing is easy, otherwise the village", "A four-night stay can take a morning boat. It does not have to.", "If you want Delos, it is a morning from the old port, which means an early taxi from Ano Mera. If that sounds like too much, repeat a beach or stay in the village.", "Pack both bedrooms. A two-bedroom checkout has twice the chargers.", "Airport. Ano Mera is not far. Traffic still exists.", "Do not finish at a beach club. It will not retroactively make the apartment a villa.", ""),
    ],
    attractions=[
        sight("Ano Mera square", "The village you are sleeping in. Tavernas, a bakery, and ordinary island life.", "This is the base, not a side trip. Use it.", ""),
        sight("Panagia Tourliani", "The monastery on the square. The architectural sight of the village.", "Step in if it is open. A courtyard and a church, not a museum day.", ""),
        sight("Ornos beach", "The sandy bay you visit. Also the place you do not rent a villa.", "Swim, look up at the hotels, leave.", ""),
        sight("Little Venice", "The town postcard, on the one evening you go in.", "Go by bus or taxi. Do not plan to walk from Ano Mera.", ""),
        sight("Kato Mili", "The windmills, paired with Little Venice on the town evening.", "Same outing. Then go home.", ""),
        sight("Delos", "Optional archaeology. Worth it if the early taxi is acceptable.", "A morning boat. Not on the day you fly.", ""),
    ],
    scenic_routes=[
        route("Ano Mera to a beach and back", "By car or bus to Ornos, Agia Anna, or Kalafati for a swim, and home for dinner. The route is the point of having two bedrooms inland.", "About 15–25 minutes"),
        route("Ano Mera to Chora for the evening", "Bus or taxi in, walk the harbor and the windmills, and a confirmed ride back.", "About 15 minutes, plus the walk"),
        route("Early taxi to the Delos boat", "From the village to the old port for the morning boat, and back to Ano Mera after.", "A half day, if you choose it"),
    ],
    transport="A car, or a patient use of buses and taxis. Ano Mera is on the bus network and it is not a walk to town. Parking in Chora is a reason to leave the car at the apartment. The airport is closer to the village than the glamour is. Santa Marina's driveway is not your transfer.",
    food=[
        dish("Village breakfast", "A bakery on Ano Mera square", "Pies and coffee. The apartment does the rest of breakfast if you bought yogurt and fruit."),
        dish("Cooked dinner", "Your kitchen", "Two nights. Salad, grilled meat or a tray of vegetables from the village shop. This is why the two-bedroom has a stove."),
        dish("Taverna on the square", "Ano Mera", "The eat-out night at home. Cheaper and calmer than Chora."),
        dish("One beach grill", "A non-club taverna at whichever bay you swam", "Fish or pork, a salad, and the bus or the car. Not a bottle service."),
    ],
    tips=[
        "Book the two-bedroom, not the studio hiding in the same property.",
        "Sofos's family suite is about 45 square meters. That is two rooms and not much else.",
        "Santa Marina is the villa people mean. It is not under $400.",
        "August at a beach club is out. May and October in Ano Mera are the product.",
    ],
    faqs=[
        faq("Can I get a two-bedroom on the beach for $400?", "Not at Santa Marina, and not at the famous villas in August. Ano Mera in the shoulder is the honest yes."),
        faq("Is 45 square meters enough?", "It is what Sofos lists for the two-level family suite. If you need two real rooms and a table, ask them to confirm the layout, or take the larger Mykonian Breeze unit."),
        faq("Do we need a car?", "It is the comfortable answer. Buses exist. Taxis should be arranged at night, not waved at."),
        faq("Are these pet-friendly?", "Mykonian Breeze has been listed as not accepting pets. Do not assume Sofos does either. This is the bedroom search, not the dog search."),
    ],
    map_places=[
        stop("Ano Mera", "Ano Mera", "Greece", ""),
        stop("Panagia Tourliani", "Ano Mera", "Greece", ""),
        stop("Ornos", "Ornos", "Greece", ""),
        stop("Little Venice", "Mykonos", "Greece", ""),
        stop("Delos", "Delos", "Greece", ""),
    ],
    budget_notes="A two-bedroom under $400 is a shoulder-season Ano Mera rate, and only if you booked the right unit. Santa Marina is on the page as the counterexample, not as a suggestion. Add a car or several taxis. Cooking is what keeps four nights inside a sensible daily spend. One beach-club lunch will not.",
))


add(trip(
    slug="mykonos-luxury-with-ocean-view",
    title="Mykonos luxury that faces the water: Ornos, Agios Ioannis, and the port side",
    location="Mykonos, Greece",
    summary=(
        "This one is real. Santa Marina sits on a private stretch of Ornos Bay. Bill & Coo Coast is on Agios Ioannis, "
        "which is the sea-facing half of that hotel's two Mykonos addresses. The other Bill & Coo is on Megali Ammos. "
        "Kalesma is on the Aleomandra hillside of Agios Ioannis, looking toward Delos. Tourlos is the new-port bay "
        "just north of town, and the ridge above it is Tagoo, where Cavo Tagoo has the famous pool. You do not need "
        "that fourth hotel to have an ocean view. You do need to book the room that faces the water."
    ),
    who="Travelers who want a famous hotel, an actual sea view, and no pretense that this is a bargain.",
    best_time="Late May through early October. July and August are the scene and the price. The meltemi blows in summer. September keeps the water and loses some of the noise.",
    nights=4,
    hook="4 nights · Ornos or Agios Ioannis · A real sea view",
    constraints=["Ocean view at a famous hotel", "Not a town room with a roof terrace", "Book the sea-facing unit"],
    lodging="$500–1600",
    daily="$700–1100",
    neighborhoods=[
        stay_area("Ornos", "A sandy bay on the south coast, close to town by bus or car. Santa Marina has its own beach on the bay. The public sand is next door and busier."),
        stay_area("Agios Ioannis and Tourlos", "Agios Ioannis is the rocky, quieter cove where Bill & Coo Coast and Kalesma look at the sea and, from Kalesma, toward Delos. Tourlos, to the north, is the new port. Tagoo is the hillside above it."),
    ],
    hotels=[
        hotel("Santa Marina, a Luxury Collection Resort", "Ornos Bay", "On a peninsula of Ornos Bay, with a sandy beach and a village of rooms stepping down to the water. Book a room that faces the bay. A garden room in the same resort is a weaker version of the search.", "$600–1600", "Ornos, Mykonos"),
        hotel("Bill & Coo Coast", "Agios Ioannis", "The Coast hotel, on Agios Ioannis, with the sea in front of the suites. Bill & Coo also runs a hotel on Megali Ammos. The Agios Ioannis one is the ocean address for this trip.", "$600–1500", "Agios Ioannis, Mykonos"),
        hotel("Kalesma Mykonos", "Aleomandra, Agios Ioannis", "A luxury hotel on the Aleomandra hill above Agios Ioannis, with views toward Delos and both the sunrise and sunset sides of that coast. It is quiet on purpose. The beach is below you, not a club in the lobby.", "$700–1800", "Agios Ioannis, Mykonos"),
    ],
    itinerary=[
        day(1, "The bay you paid for", "Arrive and stay on the water. Town can happen tomorrow.", "Settle and confirm the balcony faces the sea. At Santa Marina, go down to the beach. At Bill & Coo Coast or Kalesma, learn the path to the water.", "Swim, or sit and look at Delos if you are at Kalesma. The first afternoon is not a tour.", "Dinner at the hotel. You booked the view. Use it once before you go hunting for a famous table.", "Meltemi days make some coves choppy. The pool is the backup, and at these hotels the pool also faces the right direction.", ""),
        day(2, "Chora, then back to the water", "The town is a short ride, not a place to relocate.", "A late morning in Chora: Little Venice and the windmills, before the evening volume.", "Back for a long swim. If you are at Ornos, the public beach is the lively comparison and the hotel beach is the quiet one.", "A dinner you reserved. On this island, a famous table without a booking is a bar snack.", "The drive to town is short and the parking is not. Use the hotel car or a taxi.", ""),
        day(3, "Delos, or Tourlos if the wind is up", "One outing that is about the sea rather than another pool.", "If the boats run, go to Delos for the morning. It is the island in the view from Kalesma.", "If the wind cancels Delos, ride to Tourlos and look at the new port from the Tagoo ridge. Cavo Tagoo is the hotel on that ridge. You are visiting the view, not checking in.", "A quiet dinner. Four nights of tasting menus is too many. Make this one simpler.", "Book Delos through the hotel if you want the timing handled. The site itself is still a walk in the sun.", ""),
        day(4, "A last swim in the right bay", "Leave from the water, not from a duty-free dash.", "Morning swim. The airport is close to Ornos and still a timed transfer. Agios Ioannis needs the same margin.", "Checkout with salt in your hair is the correct ending.", "Eat before the airport. There is no meal on the way that improves the trip.", "A sea-view room that you only saw at night was the wrong booking. This morning is the correction.", ""),
    ],
    attractions=[
        sight("Ornos Bay", "A sandy bay and the home of Santa Marina. The luxury version has a private beach on the same water the buses reach.", "Swim at the hotel beach. Walk the public sand once so you know the difference.", ""),
        sight("Agios Ioannis", "A smaller, rockier cove. Bill & Coo Coast is on it. Kalesma is on the hill above, toward Aleomandra.", "The water is the view. It is not a party beach.", ""),
        sight("Delos", "The archaeological island in the strait, and the thing Kalesma's view is aimed at.", "A morning boat. Heat, ruins, and a return for a late swim.", ""),
        sight("Tourlos and Tagoo", "The new-port bay and the ridge above it. Cavo Tagoo's pool is the landmark on that hill.", "Go for the outlook over the ferries and the north coast. Your room is still at Ornos or Agios Ioannis.", ""),
        sight("Little Venice", "The town edge over the water, worth one afternoon.", "Go and leave. The hotels on this page have a better morning swim than a sunset bar.", ""),
        sight("Kato Mili", "The windmills above town, on the same short visit.", "Pair them with Little Venice and go back to the bay.", ""),
    ],
    scenic_routes=[
        route("Hotel path to the water", "Down through Santa Marina to its beach, or down from Kalesma and Bill & Coo Coast to Agios Ioannis. The walk you repeat.", "A few minutes, steep in places"),
        route("Taxi to Chora and back", "Little Venice and the windmills, then the bay again before dinner.", "About 10–20 minutes each way"),
        route("Tourlos ridge if Delos is cancelled", "A ride to the new port and the Tagoo hillside to see the north water, then home.", "About 15 minutes from Agios Ioannis"),
    ],
    transport="Hotel cars and taxis. Ornos is on the bus, and you will not use it much at these rates. The airport is a short transfer that still needs a buffer. Delos leaves from the old port. Tourlos is where the big ferries come in. A rental car is optional and a nuisance in Chora.",
    food=[
        dish("First-night dinner at the hotel", "Santa Marina, Bill & Coo Coast, or Kalesma", "Eat once where you sleep, facing the water. You can chase famous tables after that."),
        dish("Kiki's at Agios Sostis", "The taverna with no electricity, if you go", "No reservations, often a wait, cash. Go early or do not go. It is a lunch, not a beach club."),
        dish("Fish, cooked simply", "A reserved table in Chora or at the hotel", "Ask what came in. A whole fish and a salad is the luxurious meal. A foam menu is optional."),
        dish("Kopanisti", "Before the fish", "The local cheese, so the expensive dinner still tastes like the island."),
    ],
    tips=[
        "Book the unit that faces the sea. These hotels also have rooms that do not.",
        "Bill & Coo Coast is Agios Ioannis. The Megali Ammos Bill & Coo is the other hotel.",
        "Kalesma looks toward Delos from Aleomandra. It is not in Chora and not in Tourlos.",
        "Cavo Tagoo, above Tourlos, is a real ocean-view hotel. It is not required once you have one of these three.",
    ],
    faqs=[
        faq("Which bay is which?", "Santa Marina is Ornos. Bill & Coo Coast and Kalesma are Agios Ioannis, Kalesma up on Aleomandra. Tourlos is the new-port bay, a different shore."),
        faq("Is Belvedere this trip?", "Belvedere looks over Chora and is a fine expensive town hotel. It is not a beach hotel on Ornos or Agios Ioannis."),
        faq("Do we have to eat at the hotel?", "Once, yes, so the view is part of a meal. After that, book wherever you actually want to eat."),
        faq("What if we wanted a bargain luxury room?", "These are not bargains. A May stay costs less than August and is still a luxury rate."),
    ],
    map_places=[
        stop("Ornos Bay", "Ornos", "Greece", ""),
        stop("Agios Ioannis", "Agios Ioannis", "Greece", ""),
        stop("Kalesma Mykonos", "Agios Ioannis", "Greece", ""),
        stop("Tourlos", "Tourlos", "Greece", ""),
        stop("Delos", "Delos", "Greece", ""),
    ],
    budget_notes="Rooms at these hotels are a luxury spend, commonly several hundred dollars a night and well past that in August for a true sea view. Food and transfers match the room. Kiki's is the rare lunch that is famous without being a club. Delos is cheap beside the hotel. Do not add a second hotel on Tourlos unless you have a reason to move.",
))


add(trip(
    slug="mykonos-pet-friendly",
    title="Mykonos with a dog: Ornos publishes a yes, Chora mostly does not",
    location="Mykonos, Greece",
    summary=(
        "Many boutiques in Mykonos Town say no to pets, and I will not invent a yes for Leto, Matogianni, or Belvedere. "
        "Santa Marina on Ornos Bay states on its Marriott page that pets are welcome up to 10 kg. Kivotos and Mykonos "
        "Ammos, also on Ornos, show 'pets on request' on Booking.com, with no fee listed there. An agency flag is not "
        "a letter from the hotel. Confirm the animal, the weight, and the fee in writing before you fly. This is a "
        "beach-resort plan, not a cave in Little Venice."
    ),
    who="People with a small dog who can stay on Ornos and will get the policy in writing.",
    best_time="May, June, or September, after a written yes. July and August add heat, meltemi, and hotels that are full enough to stop making exceptions. Do not travel on a checkbox.",
    nights=3,
    hook="3 nights · Ornos · Pet yes in writing",
    constraints=["Written pet confirmation", "Ornos resorts, not a Chora boutique", "OTA flags are not policy"],
    lodging="$400–1200",
    daily="$550–900",
    neighborhoods=[
        stay_area("Ornos Bay", "The beach where a published pet rule exists, at Santa Marina, and where two neighboring hotels show an on-request flag. You can walk the sand. Town is a short ride."),
        stay_area("Chora, only as a visit", "Little Venice is a walk you might do without the dog, or with the dog only if the hotel has told you the town is realistic. Assume restaurants will say no."),
    ],
    hotels=[
        hotel("Santa Marina, a Luxury Collection Resort", "Ornos Bay", "Marriott's page says the hotel welcomes pets up to 10 kg. That is a real published yes, and it is a luxury price on a private beach. Confirm the weight, the number of animals, and any fee against your dates. A 12 kg dog is a different question.", "$600–1600", "Ornos, Mykonos"),
        hotel("Kivotos Mykonos", "Ornos Beach", "A beach hotel on Ornos. Booking.com has said pets are allowed on request at no extra charge. That is an OTA flag. Email the hotel and keep the reply. Do not arrive on the strength of the filter.", "$450–1100", "Ornos, Mykonos"),
        hotel("Mykonos Ammos Hotel", "Ornos", "Also on the Ornos sand, and also showing pets on request with no fee on Booking.com. Same rule: the written yes from the hotel is the booking. The page is only a reason to ask.", "$400–1000", "Ornos, Mykonos"),
    ],
    itinerary=[
        day(1, "The yes, the beach, and no experiments", "You are on Ornos because someone wrote that the dog can come.", "Transfer that already knows about the animal. Check in and re-read the pet note with the front desk. Walk the dog on the hotel beach only if they said the beach is included.", "A quiet afternoon. Heat and meltemi matter. Water, shade, and a short walk.", "Dinner at the hotel if the confirmation includes the restaurant or the terrace. If it does not, eat in the room from food you bought.", "Do not test a Chora taverna on the first night.", ""),
        day(2, "Town without a gamble", "One person can see Little Venice. The dog needs a plan that is not 'we'll ask when we get there.'", "Morning walk while the ground is cooler. If the hotel will mind the dog, the other person can taxi to Chora for an hour.", "Back to Ornos. The public beach and the hotel beach are not the same rule. Follow the one you were given.", "Repeat the dinner that worked last night.", "A parked car in the sun is not a kennel. Neither is a balcony at midday.", ""),
        day(3, "Papers, then the airport", "The hotel yes ends at the airport door.", "A last early walk. Pack the airline documents. Confirm the transfer.", "Checkout. Ornos to the airport is short and still needs time for an animal.", "You are finished. If a restaurant refused you, that was normal. If the hotel refused you, that is why the email was the whole trip.", "Read the crate and weight rules before you are at the counter.", ""),
    ],
    attractions=[
        sight("Ornos Bay", "The beach neighborhood where the pet-friendly evidence actually is.", "Stay on the sand you were invited to. Do not roam the club beaches with a dog.", ""),
        sight("Santa Marina's beach", "A private beach with a published pet weight limit of 10 kg.", "The limit is the policy. Confirm it. Then use the beach.", ""),
        sight("Little Venice", "The town view, optional, and easier without the dog.", "Go if the animal is settled. Do not make the dog the attraction.", ""),
        sight("Kato Mili", "The windmills, on the same optional town hour.", "Short visit. Back to Ornos before the heat.", ""),
        sight("Ano Mera", "A village you might drive through. Not automatically a dog-friendly lunch stop.", "Do not count on a taverna table. Carry water.", ""),
        sight("Mykonos airport", "Close to Ornos. The paperwork is the attraction.", "Declare the dog to the transfer when you book it.", ""),
    ],
    scenic_routes=[
        route("Hotel beach walk, early", "A short loop on the sand the hotel approved, with water, before the day heats up.", "Under 2 km"),
        route("Optional taxi to Chora without the dog", "One person, Little Venice and the windmills, and straight back. The dog stays in a cool room only if that is safe and allowed.", "About 15 minutes each way"),
        route("Ornos to the airport with the dog declared", "A short transfer. The airline rules are the longer preparation.", "About 10 minutes"),
    ],
    transport="A transfer or a rental company that accepts dogs. Do not rely on the town bus. Taxis may refuse an animal, so book one that has agreed. Chora is optional. The airport is close to Ornos.",
    food=[
        dish("Hotel dinner with the dog, if confirmed", "Santa Marina, Kivotos, or Ammos", "Only if the written note includes the dining area. Otherwise this meal does not exist."),
        dish("Groceries for the room", "A shop in Ornos", "Bread, cheese, fruit, and something cooked you can carry back. The reliable dinner."),
        dish("Takeaway", "A grill that will hand you a bag", "Eat it at the hotel. Do not unwrap it in a doorway and hope."),
        dish("Water and the dog's food", "Bought on arrival", "More water than you packed. The island wind is drying."),
    ],
    tips=[
        "Confirm the pet policy in writing: weight, fee, dining, and which beach. A Booking.com flag is not that email.",
        "Santa Marina's published cap is 10 kg. Do not round your dog down.",
        "I have no yes for the famous Chora hotels. They are not on this list.",
        "Mykonian Breeze, inland, has been described as not accepting pets. Do not use it as a backup without asking.",
    ],
    faqs=[
        faq("Do I still have to confirm the pet policy in writing?", "Yes. Even Santa Marina's Marriott page can change, and the Booking.com flags for Kivotos and Mykonos Ammos were never a letter from the front desk. Email, and keep the answer."),
        faq("Can my dog come to Little Venice?", "Only if you are prepared to leave. Restaurants do not have to seat you. The safer town visit is one person, without the dog."),
        faq("Is this a budget trip?", "No. The hotel with the clearest yes is a luxury resort. A cheap town room that says no is not a bargain."),
        faq("What if they say no at the door?", "Then the written confirmation is your argument, and you should have had a second Ornos option ready. Do not drive around Chora asking cave hotels."),
    ],
    map_places=[
        stop("Ornos Bay", "Ornos", "Greece", ""),
        stop("Santa Marina Mykonos", "Ornos", "Greece", ""),
        stop("Kivotos Mykonos", "Ornos", "Greece", ""),
        stop("Mykonos Ammos", "Ornos", "Greece", ""),
        stop("Little Venice", "Mykonos", "Greece", ""),
    ],
    budget_notes="The clear yes is a luxury hotel, so the nights are expensive, and a pet fee may still appear even when an OTA says none. Kivotos and Ammos are not budget either. Budget the transfer that accepts a dog, groceries, and the chance you eat in the room. A refused boutique in town is not a savings.",
))


add(trip(
    slug="iceland-luxury-with-ocean-view",
    title="Reykjavík harbor first, then one long day on the coast",
    location="Reykjavik, Iceland",
    summary=(
        "The luxury base is the Reykjavík harbor, not a lava hotel and not the Retreat. The Reykjavik EDITION, "
        "Tower Suites Reykjavik, and Canopy by Hilton Reykjavik Marina all sit on the working waterfront. From there "
        "you get Harpa, a Golden Circle day, and, on a four-night trip, one south-coast day to Vík and Reynisfjara. "
        "Snæfellsnes is the other coast and it does not fit beside the south on this length. The Blue Lagoon is a "
        "timed booking near the airport. The Retreat, on the same lagoon, is a real hotel and a much larger bill. "
        "Ion Adventure Hotel is a beautiful place in the moss and it is not an ocean view."
    ),
    who="Travelers who want a serious hotel on the harbor and will drive, or be driven, for one inland day and one coast day.",
    best_time="Late May through September, when the south-coast day is a long drive rather than a weather gamble. Winter suits the lagoon and the harbor lights. It does not suit this coast day.",
    nights=4,
    hook="4 nights · Reykjavík harbor · Golden Circle and one coast",
    constraints=["Harbor hotel, ocean-adjacent", "Blue Lagoon booked ahead", "One coast, not two"],
    lodging="$350–800",
    daily="$500–750",
    neighborhoods=[
        stay_area("Reykjavík harbor", "EDITION, Tower Suites, and Canopy by Hilton Reykjavik Marina are on this water. Harpa is the walk. The ocean here is a working harbor, not a swimming beach."),
        stay_area("The lagoon and the lava, as other trips", "The Retreat at Blue Lagoon is the splurge, far above a normal luxury night, and it is by the airport rather than in the city. Ion Adventure Hotel is a nature hotel near Þingvellir. Book Ion for moss and steam, not for an ocean view."),
    ],
    hotels=[
        hotel("The Reykjavik EDITION", "Harbor", "A luxury hotel on the harbor, a short walk from Harpa. This is the default ocean-adjacent room: you look at the port, and you walk to dinner.", "$450–900", "Reykjavik"),
        hotel("Tower Suites Reykjavik", "Harbor", "Suites on the harbor, more apartment than lobby scene, still on the water. A good fit if you want space and the same walk to Harpa.", "$400–850", "Reykjavik"),
        hotel("Canopy by Hilton Reykjavik Marina", "Marina", "The marina hotel of the three, slightly more relaxed and still on the water. Book a harbor-facing room if the view is the reason. A courtyard room misses the point.", "$320–650", "Reykjavik"),
    ],
    itinerary=[
        day(1, "Lagoon only if it is already booked, then the harbor", "The Blue Lagoon is between the airport and the city. It is a reservation, not a place you discover.", "If you booked a slot, go from Keflavík with the luggage handled the way the lagoon tells you. If you did not, drive to the hotel and book a departure-day slot or skip it. Do not appear at the door.", "Harbor walk: Harpa outside and in, then the sculpture shore toward the Sun Voyager. The wind is part of the architecture.", "Dinner near the harbor. You are not driving tonight.", "The Retreat is on the same water as the public lagoon and is a different hotel at a different price. Do not wander into it as a nightcap.", "Harpa (concert hall)"),
        day(2, "The Golden Circle, as a full day", "Þingvellir, the geyser field, and Gullfoss. About 230 kilometers round trip from the city. One day, done properly.", "Leave after breakfast. Þingvellir first: the rift and the assembly plain. Walk down into the fissure if the path is open. This is the landscape.", "Geysir, then Gullfoss. Both are crowded at midday. See them and leave. Do not add secret lagoons.", "Back to the harbor for a late dinner. The day is long enough.", "A bus tour is the right choice if you do not want to drive. Do not drive this and the south coast on the same date.", "Golden Circle (Iceland)"),
        day(3, "South coast to Vík, and not also the west", "Waterfalls, a black beach, and a turnaround. Snæfellsnes is the other direction and needs its own day.", "Early start. Seljalandsfoss or Skógafoss, not a requirement to photograph both from every angle. Pick one to walk behind or up to, and one to see from the path.", "Reynisfjara and the basalt, then Vík if you want a town. The sneaker waves at Reynisfjara kill people. Do not turn your back on the water, and do not climb the wet columns.", "Drive back to Reykjavík in the long light. Dinner late, near the hotel.", "This is a 2.5-hour drive each way before you stop. Starting at noon means you rush the beach.", ""),
        day(4, "Hallgrímskirkja, the harbor again, and the airport", "A city morning, then Keflavík. The lagoon only if today's slot is the one you booked.", "Hallgrímskirkja, inside and up the tower if the view matters. It is the city's height. It is not a mountain.", "A last harbor walk. If the Blue Lagoon is your departure booking, leave for it with the time they gave you, then the airport. If it is not, go straight to Keflavík.", "Eat before the terminal or at the lagoon's café if you are booked there. Do not invent a third excursion.", "Reykjanes eruptions have closed the lagoon before. Check the week you fly, even with a reservation.", "Hallgrímskirkja"),
    ],
    attractions=[
        sight("Harpa", "The concert hall on the harbor, all glass and geometry, and the easiest ocean-adjacent walk from these hotels.", "Go inside even without a ticket for a show. The lobby is the public part.", "Harpa (concert hall)"),
        sight("Hallgrímskirkja", "The concrete church on the hill above downtown. The tower is the city view.", "Walk up from the harbor so you feel the distance. The tower is a small fee.", "Hallgrímskirkja"),
        sight("Blue Lagoon", "Milky geothermal water near the airport. Excellent, and a timed ticket.", "Book it. The public lagoon is this trip. The Retreat is the splurge next door, not the default.", "Blue Lagoon (geothermal spa)"),
        sight("Golden Circle", "Þingvellir, Geysir, and Gullfoss in one loop from the city.", "One day. A tour if you would rather not drive. Do not bolt the south coast onto it.", "Golden Circle (Iceland)"),
        sight("Þingvellir", "The rift valley and the old parliament site. The part of the Circle that is a landscape, not a roadside stop.", "Walk the path between the plates. Give it more than a parking-lot photo.", "Þingvellir"),
        sight("Reynisfjara", "The black beach and basalt stacks near Vík. Beautiful and dangerous in ordinary surf.", "Stay back from the water. If a wave looks small, it can still reach the steps.", ""),
    ],
    scenic_routes=[
        route("Harbor walk", "From the marina hotels past Harpa and along the shore path toward the Sun Voyager. Wind, water, and the city behind you.", "About 3 km round trip"),
        route("Golden Circle by car", "Reykjavík to Þingvellir, Geysir, and Gullfoss, and back. Stops measured in hours, not minutes.", "About 230 km, a full day"),
        route("South coast to Vík", "Route 1 to a waterfall, Reynisfjara, and Vík, then the same road home. Not via Snæfellsnes.", "About 2.5 hours each way, plus stops"),
    ],
    transport="A rental car for the Golden Circle and the south coast, or a guided day for one of them if you want a single long drive. The harbor hotels do not need a car at night. Keflavík is about 45 minutes. The Blue Lagoon sits on that airport road and still requires a booking. Winter tires and a changed plan if you come outside the long-day months. Ion is inland, off this transfer.",
    food=[
        dish("Lamb soup", "Café Loki, by Hallgrímskirkja", "A bowl and bread after the tower. The right city lunch. It is not delicate."),
        dish("Pylsa", "Bæjarins Beztu, near the harbor", "The lamb hot dog. Eat one between the hotel and Harpa. Mustard, onion, and no improvement."),
        dish("Fish pan", "Messinn", "A skillet of fish, practical and local, for the dinner that is not a tasting menu."),
        dish("Skyr", "The hotel breakfast or a shop", "The daily yogurt. Buy a plain one. The flavored cups are a souvenir, not breakfast."),
    ],
    tips=[
        "Book the Blue Lagoon or skip it. It is not a spontaneous stop, and eruptions have closed it before.",
        "The Retreat is the splurge on the lagoon. A harbor suite is already the luxury trip.",
        "Ion Adventure Hotel is a nature hotel. It is the wrong booking if the search was ocean view.",
        "At Reynisfjara, never turn your back on the sea.",
    ],
    faqs=[
        faq("Is the harbor an ocean view?", "It is a working harbor on the North Atlantic, and from these three hotels you see water. It is not a white-sand beach, and it is not the open coast at Vík."),
        faq("Can I do the Golden Circle and Vík in one day?", "You can, and you will see both badly. This itinerary gives them separate days. Snæfellsnes would be a third and does not fit."),
        faq("Should I stay at the Retreat instead?", "Only if the lagoon is the whole trip and the rate is one you have already accepted. It is well above a normal luxury harbor night. It is not the default."),
        faq("What is Ion, if I keep seeing it?", "A luxury hotel in the lava near Þingvellir, with a spa. Go there for a nature stay. Do not book it expecting the ocean."),
    ],
    map_places=[
        stop("Harpa", "Reykjavik", "Iceland", "Harpa (concert hall)"),
        stop("Hallgrímskirkja", "Reykjavik", "Iceland", "Hallgrímskirkja"),
        stop("Þingvellir", "Þingvellir", "Iceland", "Þingvellir"),
        stop("Reynisfjara", "Vík", "Iceland", ""),
        stop("Blue Lagoon", "Grindavík", "Iceland", "Blue Lagoon (geothermal spa)"),
    ],
    budget_notes="A harbor luxury room is roughly $350–800, more at the EDITION on a weekend. The Retreat is a separate, much higher number and not assumed here. The car, fuel, and one good dinner per day matter as much as the room. The Blue Lagoon is a prepaid ticket. Golden Circle parking and the Hallgrímskirkja tower are small. Reynisfjara is free and unforgiving.",
))
