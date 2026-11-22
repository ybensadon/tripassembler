"""Prague, Vienna, Lisbon, Budapest, Barcelona, and Athens."""
from _common import trip, hotel, stay_area, day, sight, route, dish, faq, stop

TRIPS = []


def add(record):
    TRIPS.append(record)


add(trip(
    slug="prague-city-center-walkable",
    title="Walkable Prague: Malá Strana and the Old Town on foot",
    location="Prague, Czechia",
    summary=(
        "Four nights between Malá Strana and the Old Town for people who want Charles Bridge, the lanes, and one castle morning, all on foot. "
        "Sleep off Wenceslas Square. The pastry spun over coals on Old Town Square is a tourist product; the meal to plan around is svíčková."
    ),
    who="A couple or two friends who like walking and would rather have one good Czech lunch than a checklist of museums.",
    best_time="Late April to June, or September to mid-October. Christmas week and Easter are packed and priced like a different city. August is hot on the unshaded lanes.",
    nights=4,
    hook="4 nights · Malá Strana and Old Town on foot · $150-400/night",
    constraints=["Walkable center", "No car", "One castle morning, not three museums"],
    lodging="$150-400",
    daily="$230-480",
    neighborhoods=[
        stay_area("Malá Strana", "The castle side of the river. Lanes, Kampa, and the bridge are the walk. The climb home is the tax if you sleep under the castle."),
        stay_area("Old Town (Staré Město)", "Flat streets to the square, the clock, and the bridge. Hotel Josef sits here. Leave the blocks off Wenceslas Square for someone else."),
    ],
    hotels=[
        hotel("Hotel Josef", "Old Town, Rybná", "Eva Jiřičná's design hotel, open since 2002, a short walk from the square and the bridge. Rooms are compact. The location is the point, and there is no pool to confuse the booking.", "$160-280", "Prague"),
        hotel("Alchymist Grand Hotel & Spa", "Malá Strana, Tržiště", "A baroque palace hotel on the quiet side of Malá Strana. You walk to Kampa and the bridge. The spa pool is shared with other guests.", "$220-420", "Prague"),
        hotel("Golden Well Hotel", "Malá Strana, under the castle", "U Zlaté studně, a small historic hotel with the terrace everyone photographs. The street home is steep and a taxi does not love it. Book it if the view is the evening, not if you want a flat walk with bags.", "$250-480", "Prague"),
    ],
    itinerary=[
        day(1, "Bridge first, then the lanes", "Arrive, drop bags, and cross before the day-trip crowds own the bridge.", "If you land early, walk the bridge west to east or the reverse while the statues are still a pleasure. If you land late, do it at dusk.", "Kampa and the Čertovka mill wheel, then Malostranské náměstí. The Lennon Wall is a five-minute stop on the way, not a destination.", "Dinner in Malá Strana. U Hrocha is a beer, not a feast. For food, walk to a real table rather than the first menu on Mostecká.", "Cobbles and a slight hill. Shoes you can walk in beat the nice pair.", "Charles Bridge"),
        day(2, "Castle at opening", "One ticketed circuit, then downhill. Do not climb back up after lunch.", "Prague Castle at opening. St. Vitus is the room that matters. Golden Lane is skippable if the line is a shuffle.", "Walk down Nerudova into Malá Strana and stay down. Lunch late. The afternoon is lanes, a church if you want one, and a sit by the river.", "Svíčková at Lokál if you are willing to cross back to the Old Town, or a slower dinner on the Malá Strana side. Skip the trdelník stands on the bridge stairs.", "Tram 22 to Pražský hrad if the climb is the problem. Walk down either way.", "Prague Castle"),
        day(3, "Old Town, with a plan", "The square, the clock, and the Jewish quarter if you hold a timed ticket. Then stop adding sights.", "Old Town Square before 9:00. Watch the astronomical clock once from the side, not from the middle of the tour groups. The Týn church front is the picture; the interior is optional.", "Josefov only with a booked slot for the cemetery. Without one, walk Pařížská to the river and stop. The cemetery line without a ticket is a bad use of the day.", "Dinner away from the square. Café Louvre does an honest Czech plate upstairs if you want a room that has been there for a century.", "The clock performs on the hour. Being early for a better view matters more than hearing the bells twice.", "Old Town Square"),
        day(4, "Petřín or a last loop, then out", "A last morning that is still a walk.", "Petřín gardens if your train is late enough. The funicular is optional; the hill and the view of the bridges are the point. Skip the tower if the queue eats the morning.", "A final pass through Malá Strana or a coffee and the walk to the station. Main station and Florenc are not pretty. Leave time.", "Eat before you go. Station food is a compromise, and a trdelník at the platform is still a trdelník.", "The Petřín funicular stops running in the evening. This is a morning plan, so that does not matter.", "Petřín"),
    ],
    attractions=[
        sight("Charles Bridge", "The walk between the two halves of this trip. Early or late, it is the city's main street.", "Go before 8:30 or after 8 at night. Midday is a corridor of easels and selfie sticks.", "Charles Bridge"),
        sight("Prague Castle", "The complex on the hill: St. Vitus, the old palace, a view back over the river.", "Timed circuit at opening. Walk down when you are done.", "Prague Castle"),
        sight("Old Town Square", "The stage set. Useful as a starting point, poor as a place to eat.", "Stand at the edge for the Týn towers. Eat two streets away.", "Old Town Square"),
        sight("Prague Astronomical Clock", "A 15th-century clock on the town hall. The hourly show is short.", "Watch it once. The rest of the hour is a better walk.", "Prague Astronomical Clock"),
        sight("St. Vitus Cathedral", "The Gothic interior inside the castle, which is the part of the ticket that earns the climb.", "Enter with the castle circuit. A separate wander in the free zone is the nave only.", "St. Vitus Cathedral"),
        sight("Petřín", "The wooded hill above Malá Strana. Gardens, orchards, and a view that does not require the tower.", "Walk down toward Újezd. The paths are steep and the funicular is a fair shortcut up.", "Petřín"),
    ],
    scenic_routes=[
        route("Bridge and Kampa", "From the Old Town bridge tower across Charles Bridge, left onto Kampa, around the mill wheel, and out to Malostranské náměstí.", "About 3 km, an hour with stops"),
        route("Castle downhill", "Tram 22 or a walk up to the castle, then Nerudova street all the way down to the river. Steep stone. Do it in that direction.", "About 2 km down, plus the ride up"),
        route("Old Town to the embankment", "Old Town Square, a loop past the clock, then west to the Vltava and south along the embankment until the bridge.", "About 3 km"),
    ],
    transport="Walk. These four days stay inside Malá Strana and the Old Town on purpose. Buy single tram tickets for the castle hill and for rain, not a three-day pass you will not use. Bolt and local taxis work for the airport; the 119 bus plus metro is the cheaper version and a nuisance with bags. Main station is a tram or a 20-minute walk from the Old Town.",
    food=[
        dish("Svíčková", "Lokál Dlouhá", "Marinated beef sirloin, cream sauce, dumplings, cranberries. This is the Czech plate to book a hunger around. The trdelník stands on the square are a tourist pastry, not an old Prague recipe."),
        dish("Pilsner", "U Hrocha, Malá Strana", "A tiny pub, poured beer, almost no room. Go for one beer. It is not where you order the svíčková."),
        dish("Duck", "U Modré kachničky, Malá Strana", "A long-running duck house. Book. It is a better evening than any table with a view of the astronomical clock."),
        dish("Cake and coffee", "Café Louvre", "Upstairs, off Národní, a real café rather than a square-side trap. Have this instead of a chimney cake."),
    ],
    tips=[
        "Book the castle circuit for opening. Afternoon entries are a shuffle through Golden Lane.",
        "Trdelník looks traditional and is not. Eat svíčková, a pub beer, or a slice of something in a café that has chairs.",
        "Mostecká and the streets feeding the bridge are the worst menus. Walk two minutes off them.",
        "Hotel stairs are steep and rooms run small. Read the square meters before you pay for a castle view.",
    ],
    faqs=[
        faq("Can I do this without the tram?", "Yes. The tram is for the castle hill and for rain. The rest is a walk if your hotel is in Malá Strana or the Old Town."),
        faq("Is the trdelník worth it once?", "No. It is batter on a spit for visitors. Spend the money on svíčková."),
        faq("How bad is the climb to the Golden Well?", "Real. The lane is steep, cobbled, and awkward with a suitcase. Take it if you want the terrace. Otherwise sleep at Josef or the Alchymist."),
        faq("What should I book before I fly?", "The castle time slot, and dinner if you care which table. The bridge does not take a reservation."),
    ],
    map_places=[
        stop("Charles Bridge", "Prague", "Czechia", "Charles Bridge"),
        stop("Prague Castle", "Prague", "Czechia", "Prague Castle"),
        stop("Old Town Square", "Prague", "Czechia", "Old Town Square"),
        stop("St. Vitus Cathedral", "Prague", "Czechia", "St. Vitus Cathedral"),
        stop("Petřín", "Prague", "Czechia", "Petřín"),
    ],
    budget_notes="Josef often lands $160-280. The Alchymist and the Golden Well jump on weekends. Food stays reasonable if you eat one proper Czech lunch and skip square-side dinners: $15-30 for svíčková, a few dollars for a beer. Castle tickets are the main prepaid cost. The walks are free.",
))


add(trip(
    slug="prague-2-bedroom-under-400night",
    title="Prague two-bedrooms under $400: kitchens in Malá Strana and the Old Town",
    location="Prague, Czechia",
    summary=(
        "Four nights in a two-bedroom with a kitchen, close enough to walk to the bridge. Outside Christmas and Easter, a real two-bedroom in Malá Strana routinely stays under $400; the terrace that looks at the bridge often does not. "
        "Hotel Bologna is the predictable family room. Charles Bridge Residence and Malostranská Residence are actual apartments, and you have to read the rate."
    ),
    who="Two couples, or a family, who want doors that close and one or two suppers cooked in.",
    best_time="May, June, September, and October, avoiding Easter and the Christmas markets. Those two weeks break the cap even in ordinary buildings. January and February are cheap and dark.",
    nights=4,
    hook="4 nights · Two bedrooms · Under $400 outside holidays",
    constraints=["Two bedrooms", "Kitchen or kitchenette", "Under $400 outside Christmas and Easter"],
    lodging="$140-380",
    daily="$210-460",
    neighborhoods=[
        stay_area("Malá Strana", "The two-bedrooms people mean when they say under $400 and central. Charles Bridge Residence and Malostranská Residence are here. Hills and cobbles, and a grocery you can walk to."),
        stay_area("Old Town, south of the square", "Hotel Bologna on Konviktská is the flatter option, a few minutes from the bridge and the National Theatre. Family rooms are the two-bedroom product."),
    ],
    hotels=[
        hotel("Hotel Bologna", "Old Town, Konviktská", "Also booked as Residence Bologna. Ask for a family room with two bedrooms. The kitchenette is basic, fine for breakfast and a simple supper, not a dinner party. This is the one most likely to stay under $400. Reception is 24 hours, which the apartment houses are not.", "$140-280", "Prague"),
        hotel("Charles Bridge Residence", "Malá Strana, U Lužického semináře", "Six apartments in one house beside the bridge, with real kitchens. Do not confuse it with Charles Bridge Premium Residence, a different operator with several Old Town addresses. The terrace suites that face the bridge often break $400. A plainer two-bedroom in the same streets often does not.", "$200-450", "Prague"),
        hotel("Malostranská Residence", "Malostranské náměstí", "Apartments on the Lesser Town square. The superior is two bedrooms and a full kitchen, some with a balcony toward St. Nicholas and the castle. Square-facing rates are the ones that climb past $400. Read the date before you assume the cap.", "$180-420", "Prague"),
    ],
    itinerary=[
        day(1, "Keys, groceries, the bridge at dusk", "The first job is the apartment, not a museum.", "Check in and learn the building: stairs, trash, which burner works. Hotel Bologna will hand you a key at a desk. The two residences need a confirmed arrival time.", "An Albert or a neighborhood potraviny. Buy bread, coffee, fruit, and something easy for the first night. Then walk the bridge once the bags are inside.", "Cook a simple supper if the kitchen is a real one. At Bologna, treat the kitchenette as breakfast equipment and eat a bowl of soup out.", "Confirm you have two rooms with doors, not a sofa listed as sleeps 4.", "Charles Bridge"),
        day(2, "Castle, then lunch at home", "The kitchen earns its keep on the day you are tired of restaurant queues.", "Castle at opening, St. Vitus, then down. Buy lunch ingredients on the way back if you are in a full kitchen, or sit down for svíčková if you are at Bologna.", "The afternoon is Malá Strana without a plan: Kampa, a coffee, a rest in the apartment. This is the point of not living out of a suitcase.", "One beer at U Hrocha or a short walk and an early night. You do not need a second attraction.", "The walk down from the castle is the right direction with tired legs.", "Prague Castle"),
        day(3, "Old Town, one proper meal out", "Use the saved lunch money on a real dinner.", "Old Town Square and the clock early. Keep it short.", "Cross to Josefov only if you already have cemetery tickets. Otherwise walk the river and come back.", "Svíčková at Lokál Dlouhá. Skip every trdelník between you and the door.", "Lokál is a modern hospoda, not a secret. It is still the right place to eat the dish.", "Old Town Square"),
        day(4, "Vyšehrad or Petřín, then the train", "A last walk that is not the bridge again.", "Vyšehrad if you want ramparts and fewer groups, or Petřín if you are already on the Malá Strana side. Both are free to enter the grounds.", "Back to the apartment, fridge emptied, keys returned the way the building asked.", "Eat the leftovers or a last pub lunch. Do not save the nicest meal for the station.", "Vyšehrad is a tram or a riverside walk from the Old Town. Do not try it with a noon checkout and a 2 p.m. train.", "Vyšehrad"),
    ],
    attractions=[
        sight("Charles Bridge", "You will cross it every day if you stay at either residence. That is the luxury, not a tour.", "Dawn and late evening are when it feels like a street again.", "Charles Bridge"),
        sight("Prague Castle", "Still the one prepaid sight. The apartment does not replace it.", "Opening slot, then downhill.", "Prague Castle"),
        sight("Malostranské náměstí", "The square in front of Malostranská Residence. St. Nicholas on one side, trams, and the road up to the castle.", "It is a place to live on, not a place to eat the first menu you see.", ""),
        sight("Kampa", "The island park under the bridge. A better afternoon than another museum when you have a kitchen to go back to.", "The Lennon Wall is on the edge. Look, then go into the park.", ""),
        sight("Old Town Square", "The set piece, ten minutes from Bologna and a bridge from Malá Strana.", "Do it early. Eat elsewhere.", "Old Town Square"),
        sight("Vyšehrad", "A fort above the river with graves of composers and a view back at the castle. Quieter than the bridge.", "Go on the last morning. The grounds are free.", "Vyšehrad"),
    ],
    scenic_routes=[
        route("Grocery loop", "Apartment to the nearest Albert, then the long way home across the bridge so the first evening is the walk.", "About 2 km"),
        route("Castle and back to the kitchen", "Up by tram 22, down on foot, stop at a shop on Újezd or in Malá Strana, cook.", "Half a day"),
        route("River to Vyšehrad", "The embankment south from the National Theatre to the Vyšehrad rock. Fewer postcard stops, a real walk.", "About 4 km"),
    ],
    transport="Walk, plus tram 22 for the castle and a tram or metro when you are carrying groceries in the rain. The apartments often have no lift. Bolt to the airport is simpler than the bus with two suitcases and leftover food. Confirm how you return the keys if your train is early.",
    food=[
        dish("Svíčková", "Lokál Dlouhá", "The one restaurant meal to plan. Trdelník on the square remains a tourist trap; do not bring it home as if it were a local specialty."),
        dish("Bakery breakfast", "A neighborhood pekárna", "Koláč or a roll and coffee from a bakery, eaten in the apartment. This is what the kitchen is for on a slow morning."),
        dish("Shop supper", "Albert or a potraviny", "Bread, cheese, pickles, a rotisserie chicken. Works in the residences. Bologna's kitchenette is too basic for anything ambitious."),
        dish("Beer and a small plate", "U Hrocha or a Malá Strana pivnice", "One night out that is not a tasting menu. Stand or sit, then go home."),
    ],
    tips=[
        "Read the floor plan. Sleeps 4 often means a sofa. This page is two bedrooms with doors.",
        "Christmas markets and Easter week break $400 even for ordinary flats. The bridge-view terraces break it on ordinary Saturdays too.",
        "Hotel Bologna is the easy under-$400 family room. The two residences are the real kitchens, at a less predictable rate.",
        "Buildings are old. Ask about stairs and a lift before you arrive with a stroller.",
    ],
    faqs=[
        faq("Is under $400 realistic?", "Yes for a normal two-bedroom in Malá Strana or at Hotel Bologna, outside Christmas and Easter. No for a terrace looking straight at Charles Bridge on a weekend."),
        faq("Can I cook at Hotel Bologna?", "A simple breakfast and a reheated supper. The hotel's own description of the kitchenette is modest. For a real stove, book Charles Bridge Residence or Malostranská Residence."),
        faq("Which Charles Bridge apartment is which?", "Charles Bridge Residence is one house on U Lužického semináře. Charles Bridge Premium Residence is a different business with more than one address. Book the name you meant."),
        faq("Do I still need castle tickets?", "Yes. The apartment saves restaurant money. It does not get you into St. Vitus."),
    ],
    map_places=[
        stop("Charles Bridge", "Prague", "Czechia", "Charles Bridge"),
        stop("Prague Castle", "Prague", "Czechia", "Prague Castle"),
        stop("Malostranské náměstí", "Prague", "Czechia", ""),
        stop("Old Town Square", "Prague", "Czechia", "Old Town Square"),
        stop("Vyšehrad", "Prague", "Czechia", "Vyšehrad"),
    ],
    budget_notes="Bologna family rooms are the rates that sit comfortably under $400. The residences swing from under the cap to well over it when the listing says terrace or castle view. Groceries for breakfast and one supper cut food spend to $40-70 a day plus one restaurant meal. Castle tickets are extra.",
))


add(trip(
    slug="prague-quiet-romantic-getaway",
    title="Quiet Prague: Kampa, Petřín at dusk, and a dinner you booked",
    location="Prague, Czechia",
    summary=(
        "Three nights in Malá Strana for a quiet trip: Kampa in the evening, Petřín as the gardens empty, and a table you reserved. "
        "The stag-party streets off Wenceslas Square are a different city. Stay on the castle side of the river and you will barely hear them."
    ),
    who="A couple who want one good dinner and unhurried walks, not a bar crawl.",
    best_time="May, June, and September. December evenings are pretty and crowded. Midsummer weekends fill Kampa with picnics; it is still calmer than the New Town at midnight.",
    nights=3,
    hook="3 nights · Kampa and Petřín · Quiet hotels",
    constraints=["Quiet streets", "No stag-party neighborhood", "Evenings on foot"],
    lodging="$160-700",
    daily="$280-800",
    neighborhoods=[
        stay_area("Malá Strana", "Kampa, the lanes under the castle, and hotels that are quiet after dinner. This is the whole trip."),
        stay_area("St. Agnes corner of the Old Town", "Hotel Residence Agnes sits by the old convent, away from the clock. A longer walk to Kampa, and a peaceful night."),
    ],
    hotels=[
        hotel("Mandarin Oriental, Prague", "Malá Strana, Nebovidská", "A former monastery. Courtyards, thick walls, and a quiet that you are paying for. The spa pool is shared, and it is not why you are here. Most rooms do not face the river.", "$450-900", "Prague"),
        hotel("Aria Hotel Prague", "Malá Strana, Tržiště", "The music-themed hotel under the castle, with a rooftop toward the spires. The building is calm. Go up to the roof at opening or after the sunset rush.", "$220-450", "Prague"),
        hotel("Hotel Residence Agnes", "Old Town, near St. Agnes", "A smaller, quieter hotel by the convent, well away from Old Town Square at night. The least expensive of the three and the least theatrical. Walk to the river in a few minutes.", "$140-260", "Prague"),
    ],
    itinerary=[
        day(1, "Kampa after dark", "Check in on the quiet side and do not cross into the New Town.", "Drop bags. If you are at Agnes, walk to the river through the back of the Old Town, not down the main tourist chute.", "Kampa in the late afternoon. The park, the mill wheel, the swans. The Lennon Wall is busy; the island is the point.", "A booked dinner. U Modré kachničky for duck, or the Mandarin if you want to stay in the courtyard. Skip any restaurant that faces the astronomical clock.", "Reservations matter on Friday. The romantic tables are the ones that answer the phone.", ""),
        day(2, "Petřín as it closes", "A slow morning, then the hill late, when the day-trippers have gone down.", "Coffee in Malá Strana. Cukrkávalimonáda if you want a room that has been pouring coffee here for years. One church if you want one: St. Nicholas on Malostranské náměstí.", "Late afternoon on Petřín. Gardens and the view of the bridges. The tower is optional and often a queue; the hill at closing is the idea.", "Walk down toward Újezd before the paths are fully dark. Dinner early. The funicular does not run all night, so do not plan the return around it.", "Wear shoes you can walk downhill in. The paths are dirt and roots as well as steps.", "Petřín"),
        day(3, "Castle courtyards early, then leave", "A last quiet hour in the courtyards before the coaches, then the airport or the train.", "Castle grounds at opening if you want St. Vitus without a crowd. You do not need every building on the ticket. An hour can be enough.", "Back down to the hotel, checkout, a last walk on Kampa if the timing works.", "Leave from somewhere easy. Agnes is a simpler taxi pickup than a lane under the castle.", "If you only have the morning, choose the castle or Petřín, not both.", "Prague Castle"),
    ],
    attractions=[
        sight("Kampa", "The island under the bridge. Lawns, water, and a path that does not perform for anyone.", "Evening is better than noon. In summer you will share it with picnics, not with pub crawls.", ""),
        sight("Petřín", "The hill for the last light on the bridges. Go late.", "Skip the tower if the line is long. Walk down; do not wait on the funicular after dark.", "Petřín"),
        sight("Charles Bridge", "Beautiful at dawn on a morning you are already awake. Skip it at noon.", "Five minutes from Kampa. You do not need a plan.", "Charles Bridge"),
        sight("Prague Castle", "Worth one early hour. The courtyards before the groups are the romantic version.", "Opening time. Then leave.", "Prague Castle"),
        sight("St. Vitus Cathedral", "The interior, if you go up the hill at all.", "It is dark and cool. That is the right pause.", "St. Vitus Cathedral"),
        sight("Lennon Wall", "A colorful wall you will pass. It is repainted constantly and always crowded.", "Look once on the way to Kampa. Do not build the evening around it.", "Lennon Wall"),
    ],
    scenic_routes=[
        route("Kampa loop at dusk", "Na Kampě, around the park, past the mill wheel, back by the bridge stairs. Stay on the island.", "About 2 km"),
        route("Petřín down to Újezd", "Funicular up or a slow climb, gardens, then the paths down to Újezd as the funicular's last runs come and go.", "About 2 km, steep"),
        route("Agnes to the river", "From St. Agnes along the quiet end of the Old Town to the embankment, then the bridge only if you want it.", "About 2 km"),
    ],
    transport="Walk. Do not stay near Wenceslas Square and commute to the quiet. A taxi or Bolt for arrival if you have bags and a Mandarin or Golden-Well-style lane; Agnes is an easier pickup. The airport bus is fine on the way out if you are traveling light.",
    food=[
        dish("Duck", "U Modré kachničky", "The long-running Malá Strana duck restaurant. Book it and treat that as the dinner. It is a better plan than a view table on the square."),
        dish("Coffee", "Cukrkávalimonáda", "A Malá Strana café for the slow morning. Sit. You are not collecting cafés."),
        dish("Svíčková", "A proper table, not a bridge stall", "Have it once, at lunch, so the trip includes the real Czech plate. The trdelník stands are for visitors who did not ask."),
        dish("A last pastry", "A pekárna, not a grill on the square", "Koláč or a slice of something baked. Leave the spit pastries."),
    ],
    tips=[
        "Wenceslas Square at night is stag groups and clubs. You do not need to see it to have been to Prague.",
        "Book the dinner before you book a sunset slot. A romantic city with no reservation is a walk and a compromise menu.",
        "Petřín after 4 p.m. beats Petřín at noon. Bring a layer. The walk down is darker than the photos.",
        "Aria's roof is lovely and it fills at sunset. Go earlier or later if you want it quiet.",
    ],
    faqs=[
        faq("Which hotel is actually quiet?", "The Mandarin, because of the monastery walls. Residence Agnes, because of the street. Aria is calm inside and more social on the roof at sunset."),
        faq("Is Kampa romantic or just a park?", "A park, which is what you want. People live around it. It is not a show."),
        faq("Can we stay on Wenceslas Square and walk over?", "You can, and you will spend the evenings in the wrong neighborhood. Stay in Malá Strana or at Agnes."),
        faq("Do we need the castle?", "Only if you want one early morning in the courtyards. The trip works on Kampa and Petřín if you would rather not queue."),
    ],
    map_places=[
        stop("Kampa", "Prague", "Czechia", ""),
        stop("Petřín", "Prague", "Czechia", "Petřín"),
        stop("Charles Bridge", "Prague", "Czechia", "Charles Bridge"),
        stop("Prague Castle", "Prague", "Czechia", "Prague Castle"),
        stop("Lennon Wall", "Prague", "Czechia", "Lennon Wall"),
    ],
    budget_notes="Residence Agnes can be $140-260. Aria sits in the middle. The Mandarin is a different budget and the quietest building. One booked dinner is $70-140 for two. The walks cost nothing. Do not add a club district just because the hotel was cheaper there.",
))


add(trip(
    slug="prague-with-private-pool",
    title="Prague and the pool question: shared spas, not a private pool",
    location="Prague, Czechia",
    summary=(
        "Central Prague hotels do not have private pools. The Four Seasons riverside villa uses the hotel vitality pool, shared with other guests, not a pool in the room. "
        "Mandarin Oriental and the Alchymist have shared spa pools in old buildings. If a pool of your own is the point of the trip, this city is a poor fit. What follows is a short luxury stay that tells the truth about the water."
    ),
    who="Travelers who asked for a private pool and should hear a clear answer before they book a spa photo.",
    best_time="May, June, and September if you want the city as well as a swim. The shared pools are indoor or courtyard affairs and do not care about August. The lanes do.",
    nights=3,
    hook="3 nights · Shared spa pools · Private pool is a poor fit",
    constraints=["No private pool", "Shared hotel spas only", "Central hotels"],
    lodging="$250-900",
    daily="$360-1000",
    neighborhoods=[
        stay_area("Vltava bank, Old Town side", "Four Seasons Hotel Prague, including the riverside villa rooms. The vitality pool is in the hotel, shared."),
        stay_area("Malá Strana", "Mandarin Oriental and the Alchymist. Both have spas. Neither has a pool that belongs to one room."),
    ],
    hotels=[
        hotel("Four Seasons Hotel Prague", "Vltava, by Charles Bridge", "The riverside hotel, and the villa rooms attached to it, look at the Vltava. Guests use the hotel vitality pool. That pool is shared. It is not an in-room pool and it is not private.", "$500-1000", "Prague", "https://www.fourseasons.com/prague/"),
        hotel("Mandarin Oriental, Prague", "Malá Strana", "The monastery hotel. The spa has a pool for guests. You share it. The courtyards are the reason to stay; the pool is a lap or a soak, then you go walk.", "$450-900", "Prague"),
        hotel("Alchymist Grand Hotel & Spa", "Malá Strana, Tržiště", "A palace hotel with a spa pool. Shared, indoors, not a garden pool of your own. Useful if you want Malá Strana and one swim, and you have dropped the private-pool brief.", "$220-450", "Prague"),
    ],
    itinerary=[
        day(1, "One swim, then the bridge", "Use the shared pool once so you know what you booked. Then leave it.", "Check in. Swim if the pool is open. It will be other guests, lap lanes or a small spa basin, and hotel rules about towels and children. That is the whole pool story.", "Walk the embankment and Charles Bridge in the late afternoon.", "Dinner out. Do not spend the evening in the spa waiting for a private feeling that is not on the rate.", "Ask at the desk what time the pool is quiet. That is the best it gets.", "Charles Bridge"),
        day(2, "Castle, and the spa only if you liked it", "The city is the day. The pool is optional and still shared.", "Castle at opening. St. Vitus. Walk down to Malá Strana.", "A second swim only if the first one was worth it. Otherwise Kampa and a long lunch.", "Svíčková or duck. You are in a very good city for dinner and an ordinary city for private swimming.", "Do not move hotels mid-trip chasing a different pool. The next one is shared too.", "Prague Castle"),
        day(3, "Old Town morning", "A last walk and a checkout that does not depend on a cabana.", "Old Town Square and the clock early.", "Checkout. If you want a final swim, do it before reception gets busy, and expect company.", "Leave. Prague does not become a pool resort in the afternoon.", "The airport transfer takes longer on Friday evenings. Book it.", "Old Town Square"),
    ],
    attractions=[
        sight("Charles Bridge", "The walk outside the hotel, which is the actual amenity.", "Early or late.", "Charles Bridge"),
        sight("Prague Castle", "The morning that justifies the trip once the pool question is settled.", "Opening slot.", "Prague Castle"),
        sight("St. Vitus Cathedral", "The interior on that castle ticket.", "Go in. Then walk down.", "St. Vitus Cathedral"),
        sight("Old Town Square", "Ten minutes from the Four Seasons if you are on the Old Town bank.", "Eat somewhere else.", "Old Town Square"),
        sight("Kampa", "The park under the bridge. A better place to sit than a crowded spa lounger.", "Afternoon.", ""),
        sight("Petřín", "The hill, if you want a view and a walk on day two instead of a second swim.", "The tower is optional.", "Petřín"),
    ],
    scenic_routes=[
        route("Hotel embankment", "From the Four Seasons along the Vltava to the bridge and back. This is the water you actually have.", "About 1.5 km"),
        route("Malá Strana lanes", "From the Mandarin or the Alchymist through the lanes to Kampa. No sights required.", "About 2 km"),
        route("Down from the castle", "Nerudova to the river after the morning ticket.", "About 2 km, steep"),
    ],
    transport="Walk. All three hotels are central. A car is useless here and will not deliver a private pool. Airport by Bolt or a prebooked car.",
    food=[
        dish("Svíčková", "Lokál Dlouhá", "The Czech meal. Have it once. A hotel pool afternoon is not a reason to eat every meal in the hotel."),
        dish("Duck", "U Modré kachničky", "Book it on the Malá Strana night."),
        dish("Coffee", "Cukrkávalimonáda or Café Louvre", "A real café. The spa menu is not the food culture."),
        dish("Anything except trdelník", "Two streets off the square", "The spit pastry is a tourist product. Order food a kitchen cooked."),
    ],
    tips=[
        "Read the room description for the words private pool. You will not find them at these hotels. You will find spa, vitality pool, and wellness.",
        "The Four Seasons villa is still the hotel's pool. Pretty rooms, shared water.",
        "Children and lap hours differ by hotel. Ask. None of that turns the pool into yours.",
        "If a private pool is non-negotiable, choose a different trip. Prague will not grow one by summer.",
    ],
    faqs=[
        faq("Does the Four Seasons villa have its own pool?", "No. The riverside villa has access to the hotel vitality pool. Other guests use it too."),
        faq("Are the Mandarin and Alchymist pools private?", "No. They are hotel spa pools. You share them with whoever is staying."),
        faq("Is there a private-pool hotel in the center I missed?", "Not among the long-established luxury hotels. A shared spa is what Prague sells."),
        faq("Should I book an apartment with a pool instead?", "Not from a random listing. This page stays with three hotels whose pools can be described accurately."),
    ],
    map_places=[
        stop("Charles Bridge", "Prague", "Czechia", "Charles Bridge"),
        stop("Prague Castle", "Prague", "Czechia", "Prague Castle"),
        stop("Old Town Square", "Prague", "Czechia", "Old Town Square"),
        stop("Kampa", "Prague", "Czechia", ""),
        stop("Petřín", "Prague", "Czechia", "Petřín"),
    ],
    budget_notes="You are paying luxury rates for the building and the location. The pool is a shared extra, not a second property. Dinner out is $40-80 a person if you leave the hotel. Do not add a fake villa fee on top.",
))


add(trip(
    slug="prague-luxury-with-ocean-view",
    title="Prague has no ocean: a luxury stay on the Vltava",
    location="Prague, Czechia",
    summary=(
        "Prague has no ocean. The water in front of the luxury hotel is the Vltava, a river, and the only rooms that truly face it are at the Four Seasons. "
        "Mandarin Oriental is the quiet Malá Strana palace, and Hotel Kings Court looks at the Municipal House and Republic Square. Book this if you want a fine city hotel. Do not book it for a sea view."
    ),
    who="Travelers who searched for an ocean view and need the geography before the rate.",
    best_time="May, June, and September for walking beside the river. Winter light on the Vltava is beautiful and cold. No season puts an ocean in Bohemia.",
    nights=3,
    hook="3 nights · No ocean · Vltava view at the Four Seasons",
    constraints=["No ocean", "River view only at the Four Seasons", "Luxury center"],
    lodging="$250-1000",
    daily="$360-1100",
    neighborhoods=[
        stay_area("Vltava embankment", "The Four Seasons is the river hotel, by the bridge. Ask for a Vltava-facing room if the water is the point. It is still a river."),
        stay_area("Malá Strana and the Powder Tower", "The Mandarin is inland among lanes. Kings Court is by the Municipal House, facing a square and a tower, not water."),
    ],
    hotels=[
        hotel("Four Seasons Hotel Prague", "Vltava, by Charles Bridge", "This is the water view: the Vltava and the bridge, from the Old Town bank. Ask for a river-facing room. There is no ocean to upgrade into. The vitality pool, if you use it, is the shared hotel pool.", "$500-1000", "Prague", "https://www.fourseasons.com/prague/"),
        hotel("Mandarin Oriental, Prague", "Malá Strana", "The luxury address in a former monastery. You are here for quiet courtyards and the walk to Kampa. Most rooms look at roofs and walls, not at water, and none of them look at a sea.", "$450-900", "Prague"),
        hotel("Hotel Kings Court", "Old Town, U Obecního domu", "Next to the Powder Tower and the Municipal House. Rooms look at the Municipal House or Republic Square. It is a comfortable luxury hotel and it is not on the river. Do not pay it for a water view it does not have.", "$220-480", "Prague"),
    ],
    itinerary=[
        day(1, "The river you actually have", "Learn the Vltava from the bank, not from a brochure that said ocean.", "If you are at the Four Seasons, walk the embankment and look at the room you booked so you know the view in daylight. If you are at the Mandarin or Kings Court, walk to the river. It is 10 to 20 minutes, not a view from the bed.", "Charles Bridge from water level, then Kampa.", "Dinner inland. A river-view restaurant is a markup. The water is free from the bank.", "The prettiest river light is late. The bridge is calmer then too.", "Charles Bridge"),
        day(2, "Castle above the river", "The view back down is rooftops and the Vltava bend. Still not a coast.", "Castle at opening. From the ramparts you see the river and the bridges. That panorama is the honest wide shot of Prague.", "Down through Malá Strana. If you are at the Mandarin, this is your neighborhood for the rest of the day.", "Svíčková or duck. Kings Court guests can walk home through the Old Town without a hill.", "Do not add a day trip to a sea. The Baltic is not a side trip from a Prague weekend.", "Prague Castle"),
        day(3, "Old Town, then leave", "A last morning in the lanes.", "The clock and the square early. Kings Court is the hotel that can do this before coffee cools.", "Checkout. A final look at the river if you are already on it.", "Go to the airport. There is no coastal road.", "Photographs of the Vltava at blue hour are the souvenir. They are not photos of an ocean.", "Old Town Square"),
    ],
    attractions=[
        sight("Vltava embankment", "The water. A working river with weirs, swans, and tour boats. This is the view the Four Seasons sells.", "Walk it. A river-facing room is the only hotel version, and only at that hotel.", ""),
        sight("Charles Bridge", "The crossing over that river. The picture is stone and water, not surf.", "Early.", "Charles Bridge"),
        sight("Prague Castle", "The hill that looks back at the bend in the Vltava.", "Opening, then down.", "Prague Castle"),
        sight("Old Town Square", "Inland. No water. Do it for the square, not for a view.", "Morning.", "Old Town Square"),
        sight("Petřín", "Another angle on the same river and the same bridges.", "The hill, not the tower, if time is short.", "Petřín"),
        sight("Dancing House", "The glass building on the river further south. A short walk if you want a second river scene.", "See it from the opposite bank or the embankment. You do not need the roof.", "Dancing House"),
    ],
    scenic_routes=[
        route("Vltava bank", "From the Four Seasons under the bridge and along the embankment. The entire ocean-view request, answered.", "About 2 km"),
        route("Letná overlook", "Cross the bridge, walk up to Letná, and look back at the bridges and the river in one bend.", "About 3 km, one climb"),
        route("Castle ramparts", "The morning view from the castle down to the Vltava, then Nerudova down.", "About 2 km down"),
    ],
    transport="Walk. The three hotels are in the center, and only one faces the river. Airport by taxi or Bolt, 30 to 45 minutes. A car will not get you to a beach.",
    food=[
        dish("Svíčková", "Lokál Dlouhá", "Eat this and retire the idea of a seafood coast. Trdelník on the square is a tourist pastry either way."),
        dish("Duck", "U Modré kachničky", "A Malá Strana dinner that does not pretend to be a marina."),
        dish("Coffee on the bank", "A café you pass, then a bench", "The view is public. You do not have to buy it inside a hotel restaurant."),
        dish("Cake", "Café Louvre", "A century-old café off Národní. Inland, and better than a view menu."),
    ],
    tips=[
        "Say Vltava when you ask for a water view. Say ocean and a honest hotel will tell you there isn't one.",
        "Only the Four Seasons is a river-view hotel. The Mandarin and Kings Court are luxury for other reasons.",
        "Tour boats on the river are optional and a bit silly in good walking weather. The bank is better.",
        "Winter fog on the river is a mood. It is still a river in Central Europe.",
    ],
    faqs=[
        faq("Can I see the ocean from Prague?", "No. Prague is inland. The water is the Vltava. The sea is a different country and a different trip."),
        faq("Which room actually faces the water?", "A river-facing room at the Four Seasons. Confirm it in the booking. A courtyard room there is not a view, and the other two hotels are not on the water."),
        faq("Does Hotel Kings Court have a river view?", "No. It faces the Municipal House and Republic Square, by the Powder Tower."),
        faq("Is the Mandarin on the river?", "No. It is in Malá Strana, in a former monastery, a walk from the water."),
    ],
    map_places=[
        stop("Charles Bridge", "Prague", "Czechia", "Charles Bridge"),
        stop("Prague Castle", "Prague", "Czechia", "Prague Castle"),
        stop("Dancing House", "Prague", "Czechia", "Dancing House"),
        stop("Old Town Square", "Prague", "Czechia", "Old Town Square"),
        stop("Petřín", "Prague", "Czechia", "Petřín"),
    ],
    budget_notes="A river-facing Four Seasons room is the expensive line, often $500 and up. Kings Court is the lower luxury rate and buys you the Powder Tower, not water. Food can stay at normal Prague prices if you leave the hotel: svíčková is not a marina markup.",
))

add(trip(
    slug="vienna-city-center-walkable",
    title="Walkable Vienna: the Innere Stadt on foot",
    location="Vienna, Austria",
    summary=(
        "Four nights inside the Ring for people who want St. Stephen's, the Hofburg, and the Naschmarkt without turning the trip into a palace marathon. "
        "Hotel Sacher is famous and the rooms are small. Kaiserin Elisabeth and Hollmann Beletage are the calmer doors in the same walk."
    ),
    who="A couple or a friend who likes cities on foot and one museum, not three.",
    best_time="April to June, and September to October. August is quieter in the kitchens and some Beisln close. Christmas markets fill the center and slow every walk.",
    nights=4,
    hook="4 nights · Innere Stadt on foot · $180-500/night",
    constraints=["Walkable Innere Stadt", "No car", "One museum morning"],
    lodging="$180-550",
    daily="$270-650",
    neighborhoods=[
        stay_area("Innere Stadt", "The old center inside the Ring. Stephansdom, the Graben, and the Hofburg are a walk from all three hotels."),
        stay_area("Opera edge", "Hotel Sacher faces the opera. You hear trams. You are still inside the walk, on the noisier side of it."),
    ],
    hotels=[
        hotel("Hotel Sacher Wien", "Philharmonikerstraße, by the opera", "The famous address. Rooms are small for the rate, and street-side windows hear the Ring. Stay here for the building, not for space. You can eat the cake without sleeping upstairs.", "$400-900", "Vienna"),
        hotel("Hotel Kaiserin Elisabeth", "Weihburggasse, Innere Stadt", "A 19th-century house a few lanes from the cathedral, named for the empress. Old-fashioned in the useful way: central, quieter than the opera corner, and not a design project.", "$180-360", "Vienna"),
        hotel("Hollmann Beletage", "Köllnerhofgasse, Innere Stadt", "A courtyard hotel near Stephansdom. Rooms are not huge. Breakfast is the meal people come back for, and the street is calm at night.", "$170-320", "Vienna"),
    ],
    itinerary=[
        day(1, "Cathedral, then the lanes", "Learn the Innere Stadt before you add a palace.", "Stephansdom. The roof pattern is the exterior; the interior is dark stone and a tomb you may or may not care about. Do not spend the whole day inside.", "Graben, Kohlmarkt, and the Hofburg courtyards. One courtyard is enough. The Spanish Riding School is a separate ticket and a separate trip.", "Dinner in a Beisl, not on the cathedral square. Figlmüller is the famous schnitzel and it is crowded. Go at opening or book, or eat the same dish somewhere that does not have a queue down the lane.", "The center is flat. You do not need the tram today.", "St. Stephen's Cathedral, Vienna"),
        day(2, "The Ring, one way", "A long walk around part of the ring, with one food market and one building.", "From the opera along the Ring toward the Stadtpark. The opera house is the exterior unless you already hold tickets.", "Naschmarkt for lunch. Eat standing or at a small stall. The market thins out after 3, and the flea market is Saturday.", "Karlskirche from the outside if your legs are still willing, then back. One museum only if you care: the Albertina or the Kunsthistorisches, not both.", "Figlmüller can be this dinner if you did not do it last night. Do not do it twice.", "Naschmarkt"),
        day(3, "Belvedere for the Klimt, or Schönbrunn", "Pick one palace. Doing both is how a walking trip becomes a commute.", "Belvedere if you want Klimt's Kiss and a garden you can walk back from. Schönbrunn if you want the imperial rooms and a park. Schönbrunn is a U4 ride, not a stroll from the cathedral.", "The gardens of whichever you chose. Skip the second palace.", "Café Sperl or Café Hawelka. Café Central is beautiful and it is a queue. Sperl is the one that still feels like a café.", "Book Belvedere timed entry in busy months. The upper palace is the Klimt.", "Belvedere, Vienna"),
        day(4, "A last lane and the station", "Leave with a short walk, not a dash through a market you already did.", "Coffee and one street you liked. Hollmann's courtyard is a fair goodbye if you stayed there. Sacher's café is a fair goodbye if you did not stay there and want the cake once.", "Train or the City Airport Train. The center hotels are a short taxi to Wien Mitte or a walk to a U-Bahn.", "Eat before the airport. The station version of a schnitzel is not the one to remember.", "If your flight is at noon, skip the palace day and keep day 3 as the buffer.", "Vienna State Opera"),
    ],
    attractions=[
        sight("St. Stephen's Cathedral, Vienna", "The center of the walk. The roof is the picture from the lanes.", "Go in once. The catacombs are optional and slow.", "St. Stephen's Cathedral, Vienna"),
        sight("Hofburg", "The imperial rooms and courtyards in the middle of the city. Easy to over-tour.", "Walk the squares. Buy a ticket only for the one wing you care about.", "Hofburg"),
        sight("Naschmarkt", "The market for lunch, not a sight with a turnstile.", "Weekday lunch. Saturday is the flea market and a crowd.", "Naschmarkt"),
        sight("Belvedere, Vienna", "Upper Belvedere holds the Klimt. The gardens are free and good.", "The Kiss, then out. Do not add Schönbrunn the same day.", "Belvedere, Vienna"),
        sight("Schönbrunn Palace", "The yellow palace and the gardens. A U-Bahn ride from the Innere Stadt.", "Gardens if you are tired of interiors. The palace rooms are a timed ticket.", "Schönbrunn Palace"),
        sight("Vienna State Opera", "The building on the Ring, across from Sacher.", "A tour or a ticket only if you want the inside. The walk past it is enough for this trip.", "Vienna State Opera"),
    ],
    scenic_routes=[
        route("Innere Stadt lanes", "Stephansdom, Graben, Kohlmarkt, Hofburg courtyards, back by the opera.", "About 4 km"),
        route("Ring to the Stadtpark", "From the opera along the Ring to the Stadtpark and back on a parallel street. Trams if you fade.", "About 4 km"),
        route("U4 to Schönbrunn gardens", "U4 to Schönbrunn, gardens and Gloriette hill, U4 back. One palace morning.", "20 minutes each way on the U-Bahn"),
    ],
    transport="Walk inside the Ring. Tram 1 or 2 if you want the Ring without walking all of it. U4 for Schönbrunn. A car is a handicap in the Innere Stadt. The City Airport Train runs from Wien Mitte; a taxi from these hotels is a short hop to that station or all the way out.",
    food=[
        dish("Wiener Schnitzel", "Figlmüller, Bäckerstraße", "The famous schnitzel, and the room is crowded. There is a second dining room nearby. Book or go when they open. A neighborhood Beisl cooks the same dish without the queue. Ask veal or pork if you care: the classic is veal."),
        dish("Sachertorte", "Hotel Sacher or Demel", "One slice, not a meal. Sacher is the hotel's cake and a wait. Demel is the old rival on Kohlmarkt. You do not need to stay at Sacher to eat it."),
        dish("Käsekrainer", "Bitzinger, behind the opera", "A cheese sausage at the stand behind the opera. This is the honest quick meal on the Ring."),
        dish("Market lunch", "Naschmarkt", "Pick a stall that is cooking, not a souvenir row. Urbanek is the cold-cut counter if you want something to carry."),
    ],
    tips=[
        "Sacher's reputation is the cake and the address. The rooms are small. Read the size before you pay the opera view.",
        "Figlmüller is worth one meal if you like a scene. It is a bad default every night.",
        "Café Central is a queue. Café Sperl and Café Hawelka are how you actually sit down.",
        "August closures are real. If a Beisl is shut, the market and the Würstelstand are not.",
    ],
    faqs=[
        faq("Can I walk Schönbrunn from the cathedral?", "You can, and you should not. It is a long trek. Take the U4 and save the walking for the gardens."),
        faq("Do I need to stay at Sacher to eat the cake?", "No. The café takes people who are sleeping somewhere else. The hotel is for the address, and the rooms are small."),
        faq("How many palaces in one day?", "One. Belvedere or Schönbrunn. The Innere Stadt is the rest of the trip."),
        faq("Is the center walkable in the rain?", "Yes. Distances are short. The arcades and cafés are the point of a wet afternoon."),
    ],
    map_places=[
        stop("St. Stephen's Cathedral", "Vienna", "Austria", "St. Stephen's Cathedral, Vienna"),
        stop("Naschmarkt", "Vienna", "Austria", "Naschmarkt"),
        stop("Belvedere", "Vienna", "Austria", "Belvedere, Vienna"),
        stop("Schönbrunn Palace", "Vienna", "Austria", "Schönbrunn Palace"),
        stop("Vienna State Opera", "Vienna", "Austria", "Vienna State Opera"),
    ],
    budget_notes="Kaiserin Elisabeth and Hollmann often land $180-320. Sacher is a different number and a smaller room than the price suggests. A schnitzel dinner is $25-40. The cake is a separate, smaller bill. Palace tickets are the prepaid piece. Walking the Ring is free.",
))


add(trip(
    slug="vienna-2-bedroom-under-400night",
    title="Vienna two-bedrooms under $400: read the floor plan",
    location="Vienna, Austria",
    summary=(
        "A two-bedroom with a kitchen under $400 is realistic in Vienna outside Christmas markets and the big conference weeks. The trap is the word suite. "
        "Aparthotel Adagio Vienna City has a full kitchen, and many of its units are studios, so ask for two bedrooms. The Starlight houses on Renngasse and Salzgries are central suite hotels; a suite is often one bedroom and a living room, with a microwave rather than a stove."
    ),
    who="Friends or a family who want space and a kitchen, and who will read the plan before they pay.",
    best_time="April to June and September to October. Christmas market weeks and large congress dates lift the center. August is calmer and some kitchens in town close, which makes the apartment more useful.",
    nights=4,
    hook="4 nights · Confirm two bedrooms · Under $400 most weeks",
    constraints=["Two bedrooms if the plan says so", "Kitchen or kitchenette", "Under $400 outside peak weeks"],
    lodging="$150-380",
    daily="$230-460",
    neighborhoods=[
        stay_area("Schwedenplatz and the Ring", "Adagio Vienna City on Uraniastraße. Full kitchens, the Danube Canal outside, Stephansdom a 10-minute walk. This is the aparthotel."),
        stay_area("Innere Stadt, Freyung and Salzgries", "Starlight Suiten on Renngasse and on Salzgries. You are in the old center. Confirm the suite is two rooms and that you have more than a kettle."),
    ],
    hotels=[
        hotel("Aparthotel Adagio Vienna City", "Uraniastraße, by Schwedenplatz", "The real aparthotel: a full kitchen with a hob, fridge, and dishwasher in the apartments. Many listings are studios or one-room units that sleep four on a sofa. Under $400 is normal. Book a plan that shows two bedrooms if that is the trip.", "$160-340", "Vienna"),
        hotel("Starlight Suiten Hotel Wien Renngasse", "Renngasse, Innere Stadt", "A long-running suite hotel by the Freyung. You are in the center. Ask whether the suite has two bedrooms and a hob. Some units are a bedroom plus a living room, with a microwave and a fridge.", "$150-320", "Vienna"),
        hotel("Starlight Suiten Hotel Wien Salzgries", "Salzgries, Innere Stadt", "The sister house near the canal, same idea: space, a central door, and a kitchenette you should confirm. A true two-bedroom under $400 exists in this part of town. It is not every listing with the word suite.", "$150-320", "Vienna"),
    ],
    itinerary=[
        day(1, "The apartment, then the Ring", "Settle the kitchen before you sightsee.", "Check in and open the cupboards. If there is no hob, change the dinner plan now.", "Billa, Spar, or the Naschmarkt for fruit and bread. Cook the first night or eat a Käsekrainer and call that the easy evening.", "A short Ring walk after dinner. The opera and the lights are enough.", "Photo the floor plan against the room you received.", "Vienna State Opera"),
        day(2, "Schönbrunn, picnic from the kitchen", "The palace day is when a kitchen saves you.", "U4 to Schönbrunn. Palace rooms if you booked them, gardens either way.", "Picnic from groceries on the lawn, or a Würstel. You do not need a palace restaurant.", "Home to cook, or Figlmüller if you want the famous schnitzel and you booked. It is crowded. One night of it is plenty.", "The U4 back at rush hour is busy and fine.", "Schönbrunn Palace"),
        day(3, "Innere Stadt on foot", "Use the central address.", "Stephansdom and the lanes. Keep it to a morning.", "Belvedere if you want one museum, Upper palace for the Klimt. Or skip it and sit in the Stadtpark.", "Dinner out that is not schnitzel again if you had it yesterday. Tafelspitz at Plachutta is the other famous plate, and it also needs a booking.", "Adagio to Belvedere is a walk or a short tram. Do not make it a third transit day.", "Belvedere, Vienna"),
        day(4, "Market and checkout", "Empty the fridge and go.", "Naschmarkt for a last snack, or breakfast from what you bought.", "Checkout. These are apartments: do the dishes enough that you are not arguing about a cleaning fee.", "Airport from Wien Mitte. Adagio is the closest of the three to that train.", "Do not leave cheese in the fridge.", "Naschmarkt"),
    ],
    attractions=[
        sight("Schönbrunn Palace", "The one big outing. Gardens even if you skip the rooms.", "U4, morning, picnic.", "Schönbrunn Palace"),
        sight("St. Stephen's Cathedral, Vienna", "The center, a short walk from all three stays.", "Exterior and a short visit.", "St. Stephen's Cathedral, Vienna"),
        sight("Naschmarkt", "Groceries and lunch in one place.", "Go hungry. Leave before you buy a third jar of anything.", "Naschmarkt"),
        sight("Belvedere, Vienna", "Klimt, if you want a museum.", "Upper palace. Book the slot.", "Belvedere, Vienna"),
        sight("Vienna State Opera", "The easy evening walk from the center.", "Outside is enough.", "Vienna State Opera"),
        sight("Stadtpark", "A green break inside the Ring, useful with a kitchen breakfast behind you.", "The Kursalon is the building. The lawn is the point.", ""),
    ],
    scenic_routes=[
        route("Canal to the cathedral", "From Adagio or Salzgries along the Danube Canal, then in to Stephansdom.", "About 2 km"),
        route("U4 and the Schönbrunn gardens", "The palace morning, with food you carried.", "20 minutes each way"),
        route("Ring after dinner", "Opera, a slice of the Ring, back to the apartment. No tickets.", "About 3 km"),
    ],
    transport="Walk in the center. U4 to Schönbrunn. U-Bahn and trams are easy with a weekly ticket if you will ride daily; single tickets if you will not. Airport: City Airport Train from Wien Mitte, or the slower rail. Adagio is the convenient one for that. The Starlight houses are a short hop on the U-Bahn.",
    food=[
        dish("Wiener Schnitzel", "Figlmüller", "Famous and crowded. Book or go early, once. If the apartment has a real kitchen, do not eat out every night just to say you did."),
        dish("Breakfast in", "Billa or Spar, then the apartment", "Coffee, rolls, yogurt. This is the budget win. A suite with only a kettle still manages breakfast."),
        dish("Käsekrainer", "Bitzinger, behind the opera", "The night you do not cook and do not want a reservation."),
        dish("Tafelspitz", "Plachutta", "Boiled beef, the other Viennese classic. Book. Skip it if you would rather cook and walk."),
    ],
    tips=[
        "Under $400 is realistic. Two bedrooms is a floor plan, not a vibe. Open the listing and count doors.",
        "Adagio is the kitchen. The Starlight houses are the central suites. They are not the same product.",
        "There is a Citadines in many cities. In Vienna the aparthotel to book is Adagio Vienna City.",
        "Conference weeks and Christmas markets move the rate. Check the date before you trust the cap.",
    ],
    faqs=[
        faq("Will I get two bedrooms under $400?", "Often, yes, outside Christmas and congress weeks. You have to book the two-bedroom plan. A suite that sleeps four on a sofa is a different room."),
        faq("Which one has a stove?", "Adagio. The Starlight suites often have a fridge and a microwave. Ask about a hob before you plan to cook dinner."),
        faq("Is Adagio central?", "Yes. Uraniastraße, by Schwedenplatz and the Ring, a 10-minute walk to the cathedral."),
        faq("Can we cook every night?", "At Adagio, yes. At the Starlight houses, plan on breakfast and one or two dinners out unless your suite confirms a kitchen."),
    ],
    map_places=[
        stop("St. Stephen's Cathedral", "Vienna", "Austria", "St. Stephen's Cathedral, Vienna"),
        stop("Schönbrunn Palace", "Vienna", "Austria", "Schönbrunn Palace"),
        stop("Naschmarkt", "Vienna", "Austria", "Naschmarkt"),
        stop("Belvedere", "Vienna", "Austria", "Belvedere, Vienna"),
        stop("Vienna State Opera", "Vienna", "Austria", "Vienna State Opera"),
    ],
    budget_notes="Adagio and the Starlight suites commonly sit between $150 and $340 outside holiday weeks. A two-bedroom at the top of that range still clears $400 less often than a Prague bridge terrace does. Groceries pull daily food down. Figlmüller and Plachutta are the splurges, not the baseline.",
))


add(trip(
    slug="vienna-family-friendly-with-kitchen",
    title="Vienna with kids: a kitchen, the Stadtpark, and the Prater",
    location="Vienna, Austria",
    summary=(
        "Four nights with children, a stove when you can get one, and a park that is not a slogan. HiLight Suites sits opposite the Stadtpark, and its family kitchenette is a sink and a microwave, so say so before you promise them pasta. "
        "Abieshomes at Messe Prater is the two-bedroom with a real kitchen, a walk from the Prater. Living Hotel Kaiser Franz Joseph has kitchens too, in green Döbling, a tram ride from both parks."
    ),
    who="Parents who need breakfast at 7:30 in their own kitchen and a park before any palace.",
    best_time="May, June, and September. The Prater is better in daylight you can stay out in. August is possible and some city restaurants close. Winter is Christmas-market season, which is pretty and a poor fit for a stroller plus a Ferris wheel queue.",
    nights=4,
    hook="4 nights · Stadtpark or Prater · Kitchen if you book the right building",
    constraints=["Family", "Kitchen or an honest kitchenette", "A park in the plan"],
    lodging="$160-380",
    daily="$250-480",
    neighborhoods=[
        stay_area("Stadtpark", "HiLight Suites, the former Starlight house on Salesianergasse, is across from the park. Lawns and a playground-scale morning without a metro."),
        stay_area("Prater and Döbling", "Abieshomes by Messe Prater puts the big park at the end of a walk. Living Hotel Kaiser Franz Joseph is in Döbling: vineyards and tram 38, not the Stadtpark outside the door."),
    ],
    hotels=[
        hotel("HiLight Suites Hotel", "Salesianergasse, opposite the Stadtpark", "The suite hotel on the park, formerly the Starlight Suiten at Heumarkt. Family suites sleep four with sofa beds and a kitchenette that is a sink and a microwave, not a stove. Stay here for the park. Cook the real dinners at the Prater apartment, or eat out.", "$180-340", "Vienna"),
        hotel("Abieshomes Messe Prater", "Leopoldstadt, by the Prater", "Serviced apartments with two bedrooms and a full kitchen, a walk from the Prater and the wheel. This is the family product that matches the brief. It is not a grand hotel. U2 Messe-Prater is the stop. Fair and congress weeks can lift the rate.", "$170-360", "Vienna"),
        hotel("Living Hotel Kaiser Franz Joseph", "Sieveringer Straße, Döbling", "Apartments with kitchenettes in the 19th district. Many units are one room; the maisonette separates living and sleeping and is still not always two bedrooms. Tram 38 reaches the center in about 20 minutes. The neighborhood is green. Stadtpark and the Prater are outings, not the backyard.", "$150-300", "Vienna"),
    ],
    itinerary=[
        day(1, "Park first", "Get the wiggles out before any museum.", "Check in, find the kitchen, buy milk and bread at a Billa.", "Stadtpark if you are at HiLight: lawns, the Kursalon outside, a playground rhythm. If you are at the Prater apartment, the green Prater is the bigger version and it is free. The rides are a separate, paid corner.", "Early dinner. Cook if you have a stove. A Würstelstand if you have a microwave and tired children.", "The amusement park is optional. The trees are the point on day one.", "Prater"),
        day(2, "Schönbrunn gardens and the zoo", "One paid animal day. The palace interior is optional with small children.", "U4 to Schönbrunn. Tiergarten Schönbrunn, the zoo in the palace grounds, is the morning that works. Book it.", "Palace gardens, maze if the line is human, Gloriette only if everyone still walks. Skip the state rooms if the group is under 8 and melting down.", "Home. Cook. The kitchen is why you are not hunting a kids' menu at 6 p.m.", "The zoo is big. Leave before everyone is furious.", "Tiergarten Schönbrunn"),
        day(3, "Prater properly, or the park you missed", "The green Prater is huge. The Wurstelprater is the ride corner with the old wheel.", "If you stayed at HiLight, take the U-Bahn to Praterstern and do the park today. If you stayed at Abieshomes, you are already there: meadows first, the Riesenrad only if the children actually want the wheel.", "A playground break and ice cream. Do not stack the zoo and the rides.", "Back before late. Döbling guests should not try to do the Prater and a Heuriger the same evening with small kids. Pick one.", "The Ferris wheel has a queue and a price. The park does not.", "Prater"),
        day(4, "Slow breakfast, Naschmarkt fruit, airport", "A last easy morning.", "Breakfast in, or bakery rolls. A short return to whichever park worked.", "Checkout and a taxi. If you have time, Naschmarkt for fruit to carry, not a full shop.", "Airport with a margin. Apartments want a key handover.", "Do not promise Schönbrunn on the way to the flight.", "Naschmarkt"),
    ],
    attractions=[
        sight("Stadtpark", "The lawn outside HiLight. The right first morning.", "Let them run. The statue tour can wait.", ""),
        sight("Prater", "The large park in Leopoldstadt. Free to walk. The rides are the noisy corner.", "Meadows first. The wheel is a choice.", "Prater"),
        sight("Tiergarten Schönbrunn", "The zoo in the Schönbrunn grounds. This is the kids' ticket.", "Morning, booked. It is larger than it looks.", "Tiergarten Schönbrunn"),
        sight("Schönbrunn Palace", "Gardens and the hill. The interior is a long shuffle with a stroller.", "Gardens if the zoo already happened. Rooms only with older kids who voted for it.", "Schönbrunn Palace"),
        sight("Naschmarkt", "Fruit, bread, and a snack. Overwhelming if everyone is hungry and short.", "One stall, then leave.", "Naschmarkt"),
        sight("St. Stephen's Cathedral, Vienna", "One look at the cathedral so the trip is still Vienna.", "Ten minutes. Skip the tower with small children.", "St. Stephen's Cathedral, Vienna"),
    ],
    scenic_routes=[
        route("Into the green Prater", "From Praterstern or from the Messe-Prater apartment into the park, away from the rides, and back.", "An hour of wandering"),
        route("U4 to the zoo", "The Schönbrunn day. Stroller on the U-Bahn is normal and crowded at 9.", "20 minutes each way"),
        route("Tram 38 from Döbling", "If you stayed at the Living Hotel: tram 38 to the Ring, then decide between Stadtpark and the U-Bahn to the Prater.", "About 20 minutes to the center"),
    ],
    transport="U-Bahn with a stroller is the system. U4 to Schönbrunn, U1 or U2 toward the Prater. HiLight is on U4 Stadtpark. Abieshomes is on U2 Messe-Prater. Living Hotel is tram 38, which is easy and not a metro. Taxis for the airport with car seats: ask when you book the car. The parks themselves need no tickets.",
    food=[
        dish("Breakfast in the apartment", "Billa or Spar", "Rolls, butter, jam, fruit, yogurt. This is the reason for a kitchen with children. HiLight's microwave kitchenette manages less of it."),
        dish("Würstel", "A stand near the Prater or the opera", "The meal when nobody will sit through schnitzel. Käsekrainer for the adults, a plain sausage for the cautious."),
        dish("Wiener Schnitzel", "A Beisl, not only Figlmüller", "Figlmüller is famous and crowded, a poor room for tired children. Eat schnitzel somewhere that can seat you when you arrive."),
        dish("Kaiserschmarrn", "A café after the park", "Torn pancake, plum sauce. One order for the table. It is dessert, not dinner."),
    ],
    tips=[
        "HiLight is the park. Abieshomes is the stove and the second bedroom. Living Hotel is the quiet green district. Pick on purpose.",
        "The green Prater is free. The Wurstelprater rides are not. You can do the trip and never buy a wristband.",
        "Zoo in the morning, naps after. Do not add the palace rooms on the same day with children under 8.",
        "Congress weeks near Messe Prater move Abieshomes rates. Check the calendar.",
    ],
    faqs=[
        faq("Which stay can actually cook dinner?", "Abieshomes, with a full kitchen and two bedrooms. Living Hotel has kitchenettes and you must confirm a second bedroom. HiLight's family kitchenette is a sink and a microwave."),
        faq("Is the Prater an amusement park?", "Part of it. The large park is lawns and paths and free. The rides and the old wheel sit in one corner."),
        faq("Do we need the palace interior?", "No. The gardens and the zoo carry the Schönbrunn day with children."),
        faq("Where is the Living Hotel relative to the park?", "Döbling, on tram 38, about 20 minutes from the Ring. It is green. It is not across the street from the Stadtpark or the Prater."),
    ],
    map_places=[
        stop("Prater", "Vienna", "Austria", "Prater"),
        stop("Schönbrunn Palace", "Vienna", "Austria", "Schönbrunn Palace"),
        stop("Tiergarten Schönbrunn", "Vienna", "Austria", "Tiergarten Schönbrunn"),
        stop("Naschmarkt", "Vienna", "Austria", "Naschmarkt"),
        stop("St. Stephen's Cathedral", "Vienna", "Austria", "St. Stephen's Cathedral, Vienna"),
    ],
    budget_notes="These three usually sit under $400, and a two-bedroom at Abieshomes is the one to price carefully in fair weeks. The zoo ticket is the big prepaid cost. Groceries and one sausage dinner keep food sane. The Prater lawns are free; the rides are how the day gets expensive.",
))

add(trip(
    slug="lisbon-budget-under-200night",
    title="Lisbon under $200: Baixa first, Alfama when you are ready to climb",
    location="Lisbon, Portugal",
    summary=(
        "Three nights in Lisbon on a cap that holds most of the year and breaks in August, during the June street festivals, and when Web Summit fills the city in November. "
        "Sleep in flat Baixa or at a simple Saldanha ibis, and treat Alfama as a morning walk. The hills are steep, cobbled, and a bad surprise with a suitcase."
    ),
    who="Travelers who want the center without a design-hotel rate, and who will walk.",
    best_time="March to early June, and late September to November outside Web Summit week. August is hot and the $200 cap is a rumor. June's Santos Populares fill the streets and the prices.",
    nights=3,
    hook="3 nights · Under $200 most weeks · Alfama is a climb",
    constraints=["Under $200 outside August and event weeks", "No car", "Hills called out in advance"],
    lodging="$70-190",
    daily="$140-260",
    neighborhoods=[
        stay_area("Baixa", "The flat grid by the river. Yes! Lisbon Hostel is on Rua de São Julião. Rossio and the metro are an easy walk. This is the budget geography that does not punish your knees."),
        stay_area("Saldanha and Príncipe Real", "ibis Lisboa Centro Saldanha is a plain chain room on the flatter business grid. Independente Príncipe Real is a mansion hostel up the hill, with a rooftop locals actually use."),
    ],
    hotels=[
        hotel("ibis Lisboa Centro Saldanha", "Saldanha", "A plain Accor room that can sit under $200 outside August and congress weeks. You are not in Alfama. You are on a flat street with a metro, which is the practical version of a budget Lisbon base.", "$90-180", "Lisbon"),
        hotel("Yes! Lisbon Hostel", "Baixa, Rua de São Julião", "Private rooms, not a dorm, if this page is the plan. Some rooms share a bathroom, so read that line. There is a communal kitchen, not a kitchen in the room. The lounge is social at night. The street is flat, by Praça do Comércio.", "$80-170", "Lisbon"),
        hotel("Independente Príncipe Real", "Príncipe Real", "Private rooms and suites in the old mansion on São Pedro de Alcântara. A simple private room can land near or under $200; a balcony suite often does not. The rooftop bar is popular with locals, so ask for a quiet room. The hill is real.", "$110-220", "Lisbon"),
    ],
    itinerary=[
        day(1, "Baixa and Chiado, on the flat", "Arrive and stay low before you climb.", "Praça do Comércio and Rua Augusta. The arch is free. Santa Justa is a lift with a queue; skip it if the line wraps the block and use a miradouro later.", "Chiado on foot. Manteigaria for a warm pastel de nata. One is the right number. Time Out Market is convenient and not a bargain; a bifana at a counter is the budget lunch.", "A quiet evening if you are at Yes!. The lounge stays lively. Eat early nearby and do not plan a 6 a.m. alarm.", "Tram 28 looks cheap and costs you an hour in line plus a pickpocket lesson. Walk.", "Praça do Comércio"),
        day(2, "Alfama in the cool morning", "Climb while the stones are cooler. Do not drag luggage on this walk.", "Up through Alfama to a miradouro. São Jorge Castle is the paid version; the view from the nearby lookouts is free and, on a clear day, enough.", "Back down before the afternoon heat. Laundry-steep lanes, laundry overhead, trams squeezing past. This is the neighborhood. It is a poor place to be lost with a bad knee.", "Dinner in Baixa or at a tasca, not a tourist menu on the castle steps. Ginjinha at A Ginjinha is one small glass, not a bar crawl.", "Wear shoes with grip. The cobbles are polished and slick after rain.", "Alfama"),
        day(3, "Belém if the flight is late", "The monastery is the one ticket. The tower is the picture outside.", "Tram 15 or the train from Cais do Sodré to Belém. Jerónimos if you will pay for one building. The cloisters are the room.", "Belém Tower from the river path. Pasteis de Belém, the 1837 shop, because you are already here. Eat them warm in the tiled rooms. The line moves.", "Back with enough time for a hill-free pickup. Baixa and Saldanha are easier taxi streets than a lane in Alfama.", "Do not attempt Belém and the castle on the morning of a flight.", "Jerónimos Monastery"),
    ],
    attractions=[
        sight("Praça do Comércio", "The river square. The right first hour, and it is free.", "The yellow arch, then into the grid. The terrace cafés are priced for the view.", "Praça do Comércio"),
        sight("Alfama", "The old lanes under the castle. Steep, beautiful, and tiring.", "Morning. A miradouro is enough if you skip the castle ticket.", "Alfama"),
        sight("São Jorge Castle", "The paid view over the roofs. Worth it once, not required for the view.", "Go early. The free lookouts nearby are the backup.", "São Jorge Castle"),
        sight("Jerónimos Monastery", "The one monument to pay for in Belém. The cloisters carry it.", "Morning ticket. Combine with the pastry shop, not with a second museum.", "Jerónimos Monastery"),
        sight("Belém Tower", "The riverside fort. A photo and a short visit.", "If the inside queue is long, the outside and the river path are the budget version.", "Belém Tower"),
        sight("LX Factory", "Old industrial halls under the bridge. Free to walk, useful if you have a spare afternoon and no more ticket budget.", "Go for the graphic murals and a coffee. The shops are not cheap.", "LX Factory"),
    ],
    scenic_routes=[
        route("Baixa to Chiado", "From Praça do Comércio up through Rua do Ouro or Rua Augusta into Chiado. A hill at the end, not a cliff.", "About 2 km"),
        route("Alfama without luggage", "From the cathedral up to a miradouro and back down a different lane. Stop when you are tired. The way down is slippery.", "About 2 km, steep"),
        route("Train or tram 15 to Belém", "Cais do Sodré to Belém. Monastery, tower, pasteis, back the same way.", "About 20-30 minutes each way"),
    ],
    transport="Walk in Baixa. Metro from Saldanha or Baixa-Chiado when you are done climbing. Tram 15 to Belém is the useful tram; tram 28 is the crowded one. Bolt and Uber beat tuk-tuks, which are a tourist ride. The airport metro is the cheap exit from Saldanha and Baixa. From a Príncipe Real lane, budget a car to the airport if you have bags.",
    food=[
        dish("Pastel de nata", "Manteigaria in Chiado, and Pastéis de Belém when you are in Belém", "Eat them warm. Manteigaria is the one you can reach without a Belém trip. The Belém shop is the old factory room and it belongs to the morning you are already there."),
        dish("Bifana", "A tasca counter in Baixa", "A pork sandwich and a beer. This is the lunch that keeps the day under budget. Time Out Market is busier and pricier for the same hunger."),
        dish("Bacalhau à Brás", "A simple tiled room, not a view terrace", "Salt cod, eggs, potatoes, olives. Order it once so the trip tastes like Lisbon."),
        dish("Ginjinha", "A Ginjinha, Largo de São Domingos", "A small glass of cherry liqueur, drunk standing up. One. Then go."),
    ],
    tips=[
        "August, June's festivals, and Web Summit break $200. The rest of the year the cap is real at these three.",
        "Alfama is a walk, not a luggage route. Sleep lower if you can.",
        "Yes! private rooms are not all en suite. Independente's rooftop is noisy on weekends. The ibis is the predictable quiet room.",
        "Tram 28 is a pickpocket line with a long wait. Walk or take a less famous bus.",
    ],
    faqs=[
        faq("Will I stay under $200?", "Most weeks, yes, for an ibis room or a hostel private room. Not in August, not during Web Summit, and not always for an Independente suite with a view."),
        faq("Are the hills that bad?", "In Alfama, yes. Polished cobbles, stairs, and no metro. Baixa is the flat grid. Do the climb in the morning with empty hands."),
        faq("Is Time Out Market the cheap meal?", "It is a useful food hall and it is not the budget lunch. A bifana costs less and tastes like the city."),
        faq("Which pastry shop?", "Manteigaria when you are in Chiado. Pastéis de Belém when the monastery is the morning. Both, if you are that kind of person. They should be warm."),
    ],
    map_places=[
        stop("Praça do Comércio", "Lisbon", "Portugal", "Praça do Comércio"),
        stop("Alfama", "Lisbon", "Portugal", "Alfama"),
        stop("Jerónimos Monastery", "Lisbon", "Portugal", "Jerónimos Monastery"),
        stop("Belém Tower", "Lisbon", "Portugal", "Belém Tower"),
        stop("LX Factory", "Lisbon", "Portugal", "LX Factory"),
    ],
    budget_notes="Rooms $70-190 outside the spike weeks. A bifana lunch is a few euros. Natas are cheap even when you buy two. The monastery ticket is the main sight cost. Tuk-tuks and tram 28 souvenirs are how the budget leaks. Airport metro is a few euros.",
))


add(trip(
    slug="lisbon-family-friendly-with-kitchen",
    title="Lisbon with kids: Chiado and Príncipe Real apartments with kitchens",
    location="Lisbon, Portugal",
    summary=(
        "Four nights in an apartment with a kitchen in Chiado, Bairro Alto, or Príncipe Real. This is the family trip, not the $200 trip. Martinhal Lisbon Chiado has two-bedrooms, a full kitchen, and a kids' club, and it can cost more than a simple flat. "
        "The Lumiares and Lisbon Serviced Apartments do the same job on steeper streets. Belém is the easy day with children. Alfama is the steep one."
    ),
    who="Parents who want breakfast in the apartment and one monument morning, not a hostel lounge.",
    best_time="April to June and September. August is hot on the hills and busy at Belém. Winter is mild, often wet, and fine if the beach is not the plan.",
    nights=4,
    hook="4 nights · Family apartments · Kitchens in Chiado",
    constraints=["Kitchen", "Family", "Not the $200 budget page"],
    lodging="$180-550",
    daily="$280-680",
    neighborhoods=[
        stay_area("Chiado", "Martinhal on Rua das Flores. Cafés, a flatter approach from Baixa, and the kitchen upstairs. Cobbles remain. A stroller is work, not impossible."),
        stay_area("Bairro Alto and Príncipe Real", "The Lumiares on Rua do Diário de Notícias, and Lisbon Serviced Apartments on Rua das Taipas. Hills, viewpoints, and a garden at Príncipe Real. Ask for the two-bedroom, not the studio."),
    ],
    hotels=[
        hotel("Martinhal Lisbon Chiado", "Rua das Flores, Chiado", "Serviced apartments from studios to two-bedrooms, each with a stove, dishwasher, and washer. There is a kids' club. This is the family hotel. It often prices above a tight budget, which is fine: this page is not the $200 page. Book the two-bedroom if you need two doors.", "$250-550", "Lisbon"),
        hotel("The Lumiares", "Rua do Diário de Notícias, Bairro Alto", "Apartment-style rooms in an old palace, all with kitchens. The Glória Suite and the penthouses are the two-bedrooms, and they cost more than a studio. You are at the top of the Glória funicular. The hill with a stroller is the catch. The rooftop is the reward after bedtime, if you still have a sitter.", "$220-600", "Lisbon"),
        hotel("Lisbon Serviced Apartments", "Príncipe Real, Rua das Taipas", "A local apartment house with a real kitchen. The T2 is the two-bedroom, about 90 square meters, for a family. Daily cleaning does not include the dishes. Code entry, not a big lobby. The São Pedro de Alcântara viewpoint is at the end of the street. The street is steep.", "$160-380", "Lisbon"),
    ],
    itinerary=[
        day(1, "The apartment and the garden", "Get groceries in before you sightsee uphill.", "Check in, learn the stairs, and shop at a Pingo Doce or Continente. Martinhal can feel like a hotel. The other two feel like a flat with housekeeping.", "Príncipe Real garden, the one with the elevated cedar, if you are up the hill. Chiado and a slow pastry at Manteigaria if you are at Martinhal. One nata each, eaten warm.", "Cook. Early night. The hills will still be there tomorrow.", "Ask which floor you are on. A walk-up with a stroller is the mistake.", ""),
        day(2, "Belém with children", "The monastery cloisters, the tower outside if the line is long, and lawn by the river.", "Tram 15 or the train from Cais do Sodré. Jerónimos. The cloisters read clearly even to children who do not want a lecture.", "Pasteis de Belém, then the river path and the tower's exterior. There is grass. Use it.", "Home to cook, or a simple soup out. Do not add the castle today.", "Belém is flatter than Alfama. This is the right monument day.", "Jerónimos Monastery"),
        day(3, "Alfama only if everyone can climb", "Otherwise LX Factory, which a stroller can do on the main lanes.", "If the children are steady on their feet, Alfama in the morning to a miradouro, not a forced castle tour. If not, tram or rideshare to LX Factory and let them look at the murals.", "Back to the apartment for lunch you bought. This is the kitchen's best hour.", "A quiet dinner in. Príncipe Real's streets are calmer at night than Bairro Alto's bar lanes. If you are at the Lumiares, the bar noise is below you on the weekends.", "Do not push Alfama in the hot afternoon.", "Alfama"),
        day(4, "A short morning and a flat pickup", "Checkout from a building that is hard for a driver.", "Breakfast in. A last walk to the Príncipe Real garden or down to the river if energy remains.", "Meet a car on a wider street. Ask the apartment where drivers actually stop.", "Airport. Leave time for the hill.", "Baixa is the easy backup meeting point if your lane is blocked.", "Praça do Comércio"),
    ],
    attractions=[
        sight("Jerónimos Monastery", "The Belém morning. Cloisters first.", "Book a time. Combine with the pastry shop, then stop.", "Jerónimos Monastery"),
        sight("Belém Tower", "The fort by the river. The outside is enough if the line is long.", "The lawns nearby matter more than the interior with children.", "Belém Tower"),
        sight("LX Factory", "Warehouses, murals, space to wander. Easier with a stroller than Alfama.", "Stay on the main lanes. Some shops are tight.", "LX Factory"),
        sight("Alfama", "The old quarter. Beautiful and steep.", "Only with children who can climb. Morning.", "Alfama"),
        sight("Praça do Comércio", "The flat river square for the first or last day.", "The arcades are the stroller route.", "Praça do Comércio"),
        sight("Time Out Market", "A food hall when you cannot cook and everyone wants something different.", "Loud and busy. One plate each and a seat if you can find one. Not a nightly plan.", "Time Out Market"),
    ],
    scenic_routes=[
        route("Down to the river", "From Chiado or Príncipe Real downhill to Praça do Comércio. Down is the kind direction. A tram or a car back up.", "About 2 km down"),
        route("Cais do Sodré to Belém", "Train or tram 15, monastery, pastry, tower, grass.", "20-30 minutes each way"),
        route("Príncipe Real garden loop", "The garden, the viewpoint at São Pedro de Alcântara, and back to the apartment without a museum.", "About 1.5 km, hilly"),
    ],
    transport="Walk downhill, ride up. Tram 15 or the Cascais line to Belém. The metro misses these apartments; the nearest stations are a descent away. Bolt for the airport and for the Alfama decision. Strollers and cobbles are a known fight. A baby carrier beats a cheap stroller on Rua das Flores and in Alfama.",
    food=[
        dish("Pastel de nata", "Manteigaria, and Pastéis de Belém on the Belém day", "Warm. Children will eat several. Adults should too, and then stop pretending it is breakfast."),
        dish("Pasta or chicken at home", "Pingo Doce", "The kitchen night. Roast chicken from the shop is a fair version of cooking."),
        dish("Bacalhau à Brás", "A neighborhood room in Chiado", "The one Portuguese plate to share. Mild enough for cautious eaters, salty enough to be the real thing."),
        dish("Bifana", "A counter, not a ceremony", "Lunch on the move. Cheaper and faster than the market with hungry children."),
    ],
    tips=[
        "Martinhal is the family hotel and it can cost like one. The Lumiares two-bedrooms are a splurge. Lisbon Serviced Apartments is the plainer two-bedroom with a stove.",
        "Belém before Alfama. Flatter, and the pastry shop is the reward.",
        "Housekeeping that skips the kitchen means you wash up. Budget five minutes.",
        "Bairro Alto is loud on weekend nights. Ask for a room off the bar street.",
    ],
    faqs=[
        faq("Is this the cheap Lisbon page?", "No. The under-$200 page is hostels and an ibis. These are apartments with kitchens, and Martinhal in particular can sit well above that cap."),
        faq("Which unit is actually two bedrooms?", "Martinhal's two-bedroom, the Lumiares Glória Suite or a penthouse, and the T2 at Lisbon Serviced Apartments in Príncipe Real. A studio with a sofa is not the same."),
        faq("Can we do Alfama with a stroller?", "Poorly. The lanes are stairs and polished stone. Use a carrier, or spend that day in Belém and LX Factory."),
        faq("Is there a park?", "Jardim do Príncipe Real. It is small and it works. Belém's river lawn is the larger run-around."),
    ],
    map_places=[
        stop("Jerónimos Monastery", "Lisbon", "Portugal", "Jerónimos Monastery"),
        stop("Belém Tower", "Lisbon", "Portugal", "Belém Tower"),
        stop("LX Factory", "Lisbon", "Portugal", "LX Factory"),
        stop("Alfama", "Lisbon", "Portugal", "Alfama"),
        stop("Praça do Comércio", "Lisbon", "Portugal", "Praça do Comércio"),
    ],
    budget_notes="Expect $180-400 for a straightforward two-bedroom and more at Martinhal or a Lumiares penthouse in peak weeks. Groceries cut the food bill. Belém tickets are the sight cost. The Príncipe Real garden is free. This page does not pretend to be the $200 cap.",
))


add(trip(
    slug="lisbon-with-private-pool",
    title="Lisbon pools: one shared rooftop, and two hotels with none",
    location="Lisbon, Portugal",
    summary=(
        "A private pool in Alfama is the wrong request. Memmo Alfama has a small shared rooftop pool for guests, and the hotel is 16 and older. Santiago de Alfama has no pool, only a terrace over the river. Palácio Ludovice has no pool either; it is a wine hotel with a spa. "
        "If the pool has to be yours alone, rent a house in Cascais or Estoril. The train from Cais do Sodré takes about 40 minutes, and you can still spend a day in Lisbon."
    ),
    who="Travelers who asked for a private pool and should see what the central hotels actually have.",
    best_time="May, June, and September if you want to swim at all. The Memmo pool is a small shared basin, pleasant in warm weather and beside the point in January. Cascais swimming weather is the same Atlantic season.",
    nights=3,
    hook="3 nights · Shared rooftop at best · Private pool means Cascais",
    constraints=["No private pool in these hotels", "Alfama hills", "Cascais train is the honest alternative"],
    lodging="$220-650",
    daily="$340-780",
    neighborhoods=[
        stay_area("Alfama", "Memmo and Santiago. Steep lanes, river light, and almost no swimming. Memmo's rooftop is the exception, and you share it."),
        stay_area("São Pedro de Alcântara", "Palácio Ludovice, by the viewpoint and the Glória funicular. Chiado and Bairro Alto on foot. No pool. Weekend street noise is the trade."),
    ],
    hotels=[
        hotel("Memmo Alfama", "Travessa das Merceeiras, Alfama", "A design hotel with a small shared rooftop pool looking over Alfama to the Tagus. Guests only. It is not a private pool and it is not in the room. The hotel welcomes guests 16 and older, so it is the wrong booking with children. The hill with luggage is real.", "$220-480", "Lisbon"),
        hotel("Santiago de Alfama", "Rua de Santiago, Alfama", "A 15th-century palace under the castle, 19 rooms, a terrace toward the river. The hotel does not have a swimming pool. Book it for the building and the quiet, not for a swim.", "$250-550", "Lisbon"),
        hotel("Palácio Ludovice", "São Pedro de Alcântara", "The wine hotel in the 18th-century palace by the viewpoint. There is a spa and a serious wine list. There is no pool. Street-facing rooms hear Bairro Alto on weekends.", "$230-500", "Lisbon"),
    ],
    itinerary=[
        day(1, "The pool, accurately", "If you are at Memmo, swim once and notice that other guests are there. If you are at the other two, walk to a viewpoint instead.", "Check in. Memmo guests can use the rooftop pool when they like; it is still shared. Santiago guests have the terrace. Ludovice guests have the viewpoint across the street.", "Alfama lanes or the Chiado side, depending on the hotel. Do not spend the day searching for a private cabana.", "Dinner. Audrey's at Santiago if you stayed there. A Chiado table if you are at Ludovice. The pool will not become private after dark.", "Luggage and Alfama stairs do not mix. Ask about a transfer to the door.", "Alfama"),
        day(2, "Belém, not a second swim", "The monastery is the day. The pool is yesterday's fact.", "Jerónimos in the morning. Cloisters.", "Belém Tower and pasteis. Back by tram 15 or the train.", "A last look at the river from a miradouro. Santa Luzia if you are in Alfama. São Pedro de Alcântara if you are at Ludovice.", "One monument day is enough. The castle can wait unless you are already under it.", "Jerónimos Monastery"),
        day(3, "Cascais by train, or home", "The water day, if you still want water that is not a shared basin.", "Train from Cais do Sodré toward Cascais, about 40 minutes. The bay is calmer than Guincho, which is wind and a rough Atlantic a further taxi away.", "Walk the Cascais waterfront. This is the sea. It is not attached to your Lisbon hotel.", "Back for a flight, or stay on if you rented the house with its own pool. That house is a different booking from these three hotels.", "Do not try Guincho with a short afternoon and small children. The bay in Cascais is the easy swim.", ""),
    ],
    attractions=[
        sight("Alfama", "The neighborhood these hotels sit in, or a short ride from Ludovice. Steep and worth one wander.", "Morning, without bags.", "Alfama"),
        sight("Tagus viewpoint", "The view from Memmo's roof, Santiago's terrace, or Santa Luzia. River, not a pool.", "Sunset is busy and still the right hour.", ""),
        sight("Jerónimos Monastery", "The Belém ticket.", "Morning, then the pastry shop.", "Jerónimos Monastery"),
        sight("Belém Tower", "The fort on the river.", "Outside if the line is long.", "Belém Tower"),
        sight("São Jorge Castle", "The castle above Santiago. A morning walk up, not a swim.", "Go early.", "São Jorge Castle"),
        sight("Praça do Comércio", "The flat square on the way to the Cascais train at Cais do Sodré.", "Use it as the easy part of the city.", "Praça do Comércio"),
    ],
    scenic_routes=[
        route("Alfama lanes", "From the hotel to a miradouro and back by a different stair.", "About 2 km, steep"),
        route("Cais do Sodré to Belém", "Tram 15 or the train. Monastery and tower.", "20-30 minutes"),
        route("Cais do Sodré to Cascais", "The Cascais line, about 40 minutes, bay at the end. This is the water if the hotel pool was the question.", "About 40 minutes each way"),
    ],
    transport="Walk the hills or take the Glória funicular near Ludovice. Trains to Belém and Cascais both leave the riverfront at Cais do Sodré. Tuk-tuks are a poor way to move luggage in Alfama. A prebooked transfer to the hotel door is worth it. The airport is a taxi or the metro plus a climb.",
    food=[
        dish("Pastel de nata", "Manteigaria or Pastéis de Belém", "Warm. The Belém shop pairs with the monastery. Manteigaria pairs with a Chiado walk from Ludovice."),
        dish("Grilled fish", "A Cascais taverna on the water day", "The honest use of the train. Agree the price if it is sold by the kilo."),
        dish("Bacalhau à Brás", "A room in Alfama or Chiado", "One proper Portuguese plate on the night you are not chasing a pool."),
        dish("Wine at the hotel", "Palácio Ludovice", "This hotel's point is the wine, not a swim. Taste there if you stayed there. Do not invent a pool bar."),
    ],
    tips=[
        "Memmo's pool is shared, small, and for guests 16 and older. Santiago and Ludovice do not have pools.",
        "A private pool means a house in Cascais or Estoril, then the train. Do not rename a rooftop and call it private.",
        "Alfama luggage is the practical problem. Pay for the transfer.",
        "Guincho is a serious surf beach. Cascais bay is the swim that matches a short afternoon.",
    ],
    faqs=[
        faq("Which of these has a private pool?", "None. Memmo has a shared rooftop pool. Santiago de Alfama and Palácio Ludovice have no pool at all."),
        faq("Can I bring children to Memmo for the pool?", "The hotel is 16 and older. Book somewhere else with children."),
        faq("How do I get a pool of my own?", "Rent a house in Cascais or Estoril that states the pool is private to the house. The train from Cais do Sodré is about 40 minutes. This page does not invent a villa name."),
        faq("Is the Tagus a beach?", "No. It is the river. The Atlantic swim on this itinerary is Cascais, on the train."),
    ],
    map_places=[
        stop("Alfama", "Lisbon", "Portugal", "Alfama"),
        stop("Jerónimos Monastery", "Lisbon", "Portugal", "Jerónimos Monastery"),
        stop("Belém Tower", "Lisbon", "Portugal", "Belém Tower"),
        stop("São Jorge Castle", "Lisbon", "Portugal", "São Jorge Castle"),
        stop("Praça do Comércio", "Lisbon", "Portugal", "Praça do Comércio"),
    ],
    budget_notes="These are $220-550 hotels. You are paying for the building and the neighborhood, not for a private pool. The Cascais train is a few euros. A house with its own pool is a separate rate and usually higher, which is the honest price of the thing you asked for.",
))


add(trip(
    slug="budapest-pet-friendly",
    title="Budapest with a dog: parks, the river, and no thermal baths",
    location="Budapest, Hungary",
    summary=(
        "Four nights with a dog in the center. Aria Hotel Budapest is the sure one: a VIP pet package, a bed, bowls, and a room cleared for the animal if you write ahead. "
        "InterContinental Budapest and Kempinski Hotel Corvinus publish pet fees too. The days are Margaret Island and City Park. Dogs are not allowed in Széchenyi or the other baths."
    ),
    who="People who travel with one calm dog and would rather walk a park than stand in a ruin bar.",
    best_time="April to June and September. July and August cook the pavement; walk at the edges of the day and carry water. Winter is doable and gray, and the baths are still closed to dogs.",
    nights=4,
    hook="4 nights · Dog on the parks · Not in the baths",
    constraints=["Dog welcome at the hotel", "No thermal baths", "Walks, not ruin bars"],
    lodging="$180-450",
    daily="$260-520",
    neighborhoods=[
        stay_area("District V, around the basilica", "Aria is on Hercegprímás utca. You can walk to the river and, in about 20 minutes, to Margaret Bridge and the island."),
        stay_area("The Danube and Erzsébet tér", "The InterContinental is on the river by the Chain Bridge. Kempinski faces Erzsébet Square, which is the small central lawn for a first sniff."),
    ],
    hotels=[
        hotel("Aria Hotel Budapest", "Hercegprímás utca, District V", "The hotel that expects a dog. Book a pet-approved room in advance and buy the VIP package, about €80 for the stay, with a bed, bowls, a treat, and a toy. The Harmony Spa has a pool for people. Leave the dog out of the spa.", "$180-400", "Budapest", "https://www.ariahotelbudapest.com/"),
        hotel("InterContinental Budapest", "Apáczai Csere János utca, by the Chain Bridge", "The large Danube hotel still listed by IHG as pet-friendly: dogs and cats, about €25 a night, one pet, tell them before you arrive. Fees move. Confirm the number when you book. The river walk starts at the door. The indoor pool is not a dog pool.", "$200-450", "Budapest"),
        hotel("Kempinski Hotel Corvinus Budapest", "Erzsébet tér", "A published pet policy: one dog up to 25 kg, about €40 a day, leash in public areas, not allowed in the spa. Erzsébet Square is across the street for the first walk. The concierge can book a sitter if you give them half a day of notice.", "$220-480", "Budapest"),
    ],
    itinerary=[
        day(1, "River bank, short loops", "A city dog needs a short first day and water.", "Check in, fill the bowl, and walk Erzsébet Square or the basilica block. Do not start with a hill.", "The Danube promenade on a leash. Chain Bridge from the Pest side. Cross if the dog is steady with crowds; turn back if not.", "Dinner on a terrace that allows dogs. Call ahead. Many dining rooms say no and the terrace says yes.", "Pack a bowl and bags. Do not assume the café has water.", "Széchenyi Chain Bridge"),
        day(2, "Margaret Island", "The best dog morning in the city. Cars are mostly kept off. You walk.", "From Margaret Bridge onto the island. Meadows, shade, a long loop. Keep the leash on. The Palatinus baths on the island are not for dogs.", "Stay on the island until you are both tired. A second small loop beats a castle climb.", "Back by the bridge. Terrace dinner again. Skip the ruin bars; they are crowded, loud, and rarely the right room for a dog.", "Carry water. The island has fountains and long stretches between them.", "Margaret Island"),
        day(3, "City Park, outside the bath", "See Széchenyi from the path. Do not try to bring the dog in.", "City Park, Városliget. Lawns, the lake, Heroes' Square from the outside if the dog is fine with pavement.", "Walk the park. The zoo is a separate ticket and a separate policy; do not assume the dog can enter. The bath is a clear no.", "Dinner near the park or back in District V. Andrássy Avenue is a handsome walk and hard on paws in the heat. Use the park instead.", "If the pavement is hot, go early and skip the avenue.", ""),
        day(4, "Repeat the walk that worked", "The last morning is the island or the park again, then the airport.", "The favorite loop, shorter.", "Checkout. Aria will have the routine. The big hotels need the pet fee settled on the bill.", "A pet taxi to the airport. Public transport wants a muzzle and a ticket and a calm dog in a crowd. Walking is the city plan; the airport is a car.", "Do not add the castle hill on departure day.", "Margaret Island"),
    ],
    attractions=[
        sight("Margaret Island", "The car-light island. This is the dog's main sight.", "Leash, water, a long loop. Skip the baths on the island.", "Margaret Island"),
        sight("City Park", "The Pest park, with the bath building on the edge.", "Walk the lawns. The dog stays out of Széchenyi.", ""),
        sight("Széchenyi thermal bath", "The yellow bath in the park. People go in. Dogs do not.", "Look at the building from outside. Plan a bath trip for a visit without the dog.", "Széchenyi thermal bath"),
        sight("Széchenyi Chain Bridge", "The walk between Pest and Buda. Fine if your dog handles crowds and grates.", "Turn around if the bridge is a crush.", "Széchenyi Chain Bridge"),
        sight("Hungarian Parliament Building", "The riverfront building. The exterior is the version that works with a dog.", "The interior tour is not a dog activity. See it from the square.", "Hungarian Parliament Building"),
        sight("Gellért Hill", "A Buda walk with trees, steep. Better than a ruin bar, harder than the island.", "Only if the dog likes a climb. Skip the baths at the bottom.", "Gellért Hill"),
    ],
    scenic_routes=[
        route("Margaret Island loop", "Onto the island from Margaret Bridge, a circuit on the paths, back the same bridge.", "3 to 5 km, as long as you like"),
        route("Danube promenade", "From the InterContinental or the Parliament down the Pest bank. Leash, crowds, a view.", "About 3 km"),
        route("City Park without the bath", "Heroes' Square edge, into the park, past the bath on the outside, back.", "About 4 km"),
    ],
    transport="Walk. That is the plan, and it is why the hotel has to be central. Margaret Island from Aria is a real but fair walk. Taxis for the airport: say there is a dog when you book. Public transport allows dogs with rules and a muzzle; this itinerary does not depend on it. The castle bus and the funicular are a crowd you can skip.",
    food=[
        dish("Gulyás", "A terrace that takes dogs", "Hungarian goulash is a soup, not a stew. Order it outside, with the dog under the table if the house allows. Call first."),
        dish("Paprikás csirke", "The same kind of terrace", "Chicken paprikash with nokedli. A proper plate on the night you do not want soup."),
        dish("Lángos", "A stand at the market edge or a park kiosk", "Fried dough, sour cream, cheese. Eat it outside. The Great Market Hall is a poor bet with a dog; do not plan to browse inside."),
        dish("Dobos torte", "A slice to take away", "The layered cake. Gerbeaud on Vörösmarty tér is famous and crowded and may not want a dog indoors. Buy the slice and eat it on a bench."),
    ],
    tips=[
        "Aria is the hotel built around the dog. The InterContinental and the Kempinski publish fees and limits. Confirm the current number before you pay.",
        "Dogs are not allowed in Széchenyi, Gellért, Rudas, or the island baths. Do not try.",
        "Terraces yes, dining rooms often no. Ask before you sit.",
        "Summer pavement burns paws. Walk early, use the parks, carry water.",
    ],
    faqs=[
        faq("Can my dog come into the baths?", "No. Széchenyi and the other thermal baths do not allow dogs. See the building from the park and book a bath on a trip without the dog."),
        faq("Which hotel is the sure one?", "Aria. You register the dog ahead and pay the VIP package. The InterContinental and Kempinski also publish pet rules; reconfirm the fee, the weight limit, and the breed notes."),
        faq("Are ruin bars a dog plan?", "No. They are crowded and indoor. This trip is parks, the river, and terraces."),
        faq("How do we get to the airport?", "A taxi or transfer that knows about the dog. Do not improvise the metro on the way to a flight."),
    ],
    map_places=[
        stop("Margaret Island", "Budapest", "Hungary", "Margaret Island"),
        stop("Hungarian Parliament Building", "Budapest", "Hungary", "Hungarian Parliament Building"),
        stop("Széchenyi thermal bath", "Budapest", "Hungary", "Széchenyi thermal bath"),
        stop("Gellért Hill", "Budapest", "Hungary", "Gellért Hill"),
        stop("Széchenyi Chain Bridge", "Budapest", "Hungary", "Széchenyi Chain Bridge"),
    ],
    budget_notes="Rooms $180-450, plus the pet fee: about €80 for the stay at Aria, about €25 a night at the InterContinental, about €40 a day at the Kempinski. Confirm those numbers. Food on terraces is normal Budapest pricing. The parks are free. The bath you are not entering would have been the ticket you do not buy.",
))


add(trip(
    slug="budapest-with-private-pool",
    title="Budapest pools are shared: Gresham, Aria, and the Kempinski",
    location="Budapest, Hungary",
    summary=(
        "A private pool in central Budapest is a poor fit. Four Seasons Gresham Palace, Aria, and Kempinski Corvinus all have hotel pools, and you share them with other guests. "
        "A pool of your own means a house in the Buda hills, in District II or XII, with the pool on the property. This page does not invent a villa brand. It books a city hotel and tells the truth about the water."
    ),
    who="Travelers who searched for a private pool and should hear what the famous hotels actually offer.",
    best_time="Any time you want the city. The pools are indoor and heated. They do not turn Budapest into a resort, in August or in January.",
    nights=3,
    hook="3 nights · Shared hotel pools · Private pool is a house in the hills",
    constraints=["No private pool", "Shared hotel pools", "Central Pest"],
    lodging="$200-900",
    daily="$300-1000",
    neighborhoods=[
        stay_area("District V, the Danube", "Four Seasons in the Gresham Palace and Aria near the basilica. The pools are downstairs or in the spa, not on a private terrace."),
        stay_area("Erzsébet tér", "Kempinski Corvinus. A small indoor pool over the square. Shared, heated, and not yours alone."),
    ],
    hotels=[
        hotel("Four Seasons Hotel Gresham Palace", "Széchenyi István tér, on the Danube", "The grand palace hotel by the Chain Bridge. The pool is the hotel's, indoors, shared with other guests. You are paying for the building and the river outside, not for a private swim.", "$450-950", "Budapest", "https://www.fourseasons.com/budapest/"),
        hotel("Aria Hotel Budapest", "Hercegprímás utca", "The music hotel. Harmony Spa includes a pool for guests. Shared. If you also have a dog, the pet package is a different conversation and the dog still does not go in the pool.", "$180-420", "Budapest", "https://www.ariahotelbudapest.com/"),
        hotel("Kempinski Hotel Corvinus Budapest", "Erzsébet tér", "A heated indoor pool about 7 by 5 meters, shared, with a view toward the square and the wheel. Day-spa hours exist for non-guests too, which tells you how private it is not. Dogs are barred from the spa.", "$220-480", "Budapest"),
    ],
    itinerary=[
        day(1, "One shared swim, then the river", "Use the pool once so the photo and the reality match.", "Check in and swim if the spa is open. Other people will be there. That is the product.", "Walk to the Danube and the Chain Bridge. The Four Seasons is already on the square.", "Dinner out. Ruin bars are irrelevant to a pool question. Eat gulyás, which is a soup, and go to bed.", "Ask when the pool is quiet. Morning is the usual answer.", "Széchenyi Chain Bridge"),
        day(2, "Castle hill without a cabana", "The city day. The pool does not get a second chapter unless you liked the first.", "Fisherman's Bastion and Matthias Church in the morning, before the cruise groups.", "The Parliament from the river, outside. A bath is optional and public: Széchenyi is a famous shared thermal bath, which is yet another way the water in this city is not private.", "Dinner in the center. You do not need a pool bar.", "The castle hill is a climb or the funicular. Neither is a swim.", "Fisherman's Bastion"),
        day(3, "A last lap or a last walk", "Checkout. The Buda hills are where a private pool would be, and they are not these hotels.", "A morning swim if you want one more shared hour.", "Walk the river or the basilica square.", "Leave. If you rebook a house in the hills for a later trip, confirm the pool is on that property and heated if you are out of summer.", "Do not transfer across town mid-morning hunting a different hotel pool. It will also be shared.", "Hungarian Parliament Building"),
    ],
    attractions=[
        sight("Széchenyi Chain Bridge", "The walk outside the Gresham. Better than another hour in a small pool.", "Sunset is busy and still the right time.", "Széchenyi Chain Bridge"),
        sight("Fisherman's Bastion", "The white terraces in the castle district.", "Morning. The interior bits are skippable.", "Fisherman's Bastion"),
        sight("Matthias Church", "The church beside the bastion.", "A short visit, then the view.", "Matthias Church"),
        sight("Hungarian Parliament Building", "The riverfront set piece.", "Outside, from the Pest bank, is the clear view.", "Hungarian Parliament Building"),
        sight("Széchenyi thermal bath", "The city's famous shared bath. Public, not private, and not a hotel pool.", "Go only if you want a bathhouse. It does not answer a private-pool request.", "Széchenyi thermal bath"),
        sight("Buda Castle", "The palace grounds on the hill.", "Walk the terraces. One museum is enough if you add one.", "Buda Castle"),
    ],
    scenic_routes=[
        route("Danube bank", "From the Chain Bridge along the Pest promenade to the Parliament and back.", "About 3 km"),
        route("Castle hill loop", "Funicular or a climb, bastion, church, down toward the river.", "About 3 km"),
        route("Erzsébet tér to the basilica", "A short city walk between the Kempinski and Aria. Squares, not water.", "About 1 km"),
    ],
    transport="Walk. All three hotels are in central Pest. The castle is a funicular, a bus, or a taxi up and a walk down. Airport by taxi. A car does not help you find a private pool in District V.",
    food=[
        dish("Gulyás", "A Pest csárda or a serious casual room", "It is a beef soup. Order it once so the trip tastes like Hungary. The stew is pörkölt, a different bowl."),
        dish("Paprikás csirke", "The same kind of restaurant", "Chicken in paprika sauce, with nokedli. Share it."),
        dish("Lángos", "Great Market Hall or a stand", "Fried dough with sour cream and cheese. The hall is upstairs for the food and busy. Eat it and leave."),
        dish("Dobos torte", "Gerbeaud or a smaller cukrászda", "The layered sponge and chocolate. One slice. Kürtőskalács, the chimney cake, is fair food, not the local cake to plan on."),
    ],
    tips=[
        "Shared means shared. Gresham, Aria, and the Kempinski all fall in that category.",
        "A Buda hills house is the private-pool product. Book it only when the listing shows the pool on that property. Do not trust a brand name invented for the search.",
        "Széchenyi is a public bath. It is wonderful and it is the opposite of private.",
        "Ruin bars have nothing to do with this request.",
    ],
    faqs=[
        faq("Is the Four Seasons pool private?", "No. It is the hotel pool in the Gresham Palace, shared with guests."),
        faq("Does Aria have a private pool?", "No. Harmony Spa has a pool for hotel guests. You share it."),
        faq("What about the Kempinski?", "A heated indoor pool, about 7 by 5 meters, shared. Non-guests can even buy a day-spa slot. Bring a suit, not a fantasy of a locked garden."),
        faq("Where is the private pool, then?", "A house in the Buda hills, District II or XII, if the pool is on that house. This page names three real hotels and does not invent a villa chain."),
    ],
    map_places=[
        stop("Széchenyi Chain Bridge", "Budapest", "Hungary", "Széchenyi Chain Bridge"),
        stop("Fisherman's Bastion", "Budapest", "Hungary", "Fisherman's Bastion"),
        stop("Hungarian Parliament Building", "Budapest", "Hungary", "Hungarian Parliament Building"),
        stop("Széchenyi thermal bath", "Budapest", "Hungary", "Széchenyi thermal bath"),
        stop("Buda Castle", "Budapest", "Hungary", "Buda Castle"),
    ],
    budget_notes="Gresham is the luxury rate. Aria and the Kempinski are less, and still city-hotel prices. The pool is included or a spa-hour question, not a second villa. A hills house with a real pool is usually a different budget and a different neighborhood. Dinner out is ordinary Budapest money if you leave the hotel.",
))

add(trip(
    slug="barcelona-city-center-walkable",
    title="Walkable Barcelona: Gothic Quarter and El Born, one Gaudí morning",
    location="Barcelona, Spain",
    summary=(
        "Four nights on foot in the Gothic Quarter and El Born, with one Gaudí morning and no second and third. "
        "Hotel Neri, Ohla, and Banys Orientals put you in the lanes. The practical problem is pickpockets, on La Rambla, on the metro, and at the Sagrada steps, not a shortage of churches."
    ),
    who="Travelers who want the old streets and one planned ticket, and who will keep their phone off the table.",
    best_time="April to June, and late September to October. August is humid, local kitchens close, and the crowds peak. Winter is a walking season and a poor beach season.",
    nights=4,
    hook="4 nights · Gothic and Born on foot · One Gaudí morning",
    constraints=["Walkable old center", "One Gaudí visit", "Pickpockets assumed"],
    lodging="$150-450",
    daily="$240-560",
    neighborhoods=[
        stay_area("Gothic Quarter", "Hotel Neri, on a small square a step from Sant Felip Neri. You walk out into the medieval grid. The Rambla is the edge to treat as a transit street, not a promenade."),
        stay_area("El Born and Via Laietana", "Ohla sits on Via Laietana, between the Gothic lanes and the Born. Banys Orientals is in the Born itself, small rooms, the neighborhood at the door."),
    ],
    hotels=[
        hotel("Hotel Neri", "Gothic Quarter", "A small palace hotel on a quiet square. You are in the middle of the walk. Rooms vary in size. The square is calm at night compared with the Rambla.", "$250-480", "Barcelona"),
        hotel("Ohla Barcelona", "Via Laietana", "A design hotel between the Gothic Quarter and El Born, with a rooftop. Useful if you want both neighborhoods without committing to a tiny Born room. The street is a real road, not a lane.", "$200-420", "Barcelona"),
        hotel("Banys Orientals", "Carrer de l'Argenteria, El Born", "A small hotel in a former bathhouse building. Rooms are compact. You step out into the Born, which is the point. Book it for the door, not for a large room.", "$140-280", "Barcelona"),
    ],
    itinerary=[
        day(1, "Gothic lanes, not the Rambla", "Arrive and learn the old grid before you add Gaudí.", "From the hotel into the Gothic Quarter. The cathedral, then smaller squares. Plaça de Sant Felip Neri is quiet and has a hard history. Do not turn the walk into La Rambla.", "Palau de la Música Catalana if you booked a tour. Otherwise stay in the lanes and end in El Born.", "Dinner in the Born, not on the Rambla. Pa amb tomàquet is bread, tomato, oil, and salt, and it is the start of the meal.", "Bag in front. Phone in a pocket you can feel. The first evening is when people get robbed.", "Gothic Quarter, Barcelona"),
        day(2, "El Born", "Santa Maria del Mar and the streets around it. One museum if you already have the ticket.", "Santa Maria del Mar when it opens. The Born streets after, before the shops fully perform.", "Picasso Museum only with a timed ticket. Without one, walk to the Ciutadella edge and stop adding museums.", "El Xampanyet, near the museum, for a glass of cava and a tin of seafood. It is crowded and cash is wise. Go early or accept the wait.", "The Born at night is busy and still a neighborhood. The Rambla at night is a pickpocket shift.", ""),
        day(3, "One Gaudí morning", "Sagrada Família, timed, then back to the old city. Do not add Park Güell the same day.", "Metro to Sagrada Família for your slot. The interior is the visit. The towers are a separate climb you can skip.", "Back to the center. A walk to Barceloneta and a swim if the weather is warm. One person watches the bags. The beach is a city beach.", "Dinner in the Born again or a simple place in the Gothic side streets. You do not need a second landmark.", "Book the basilica before you fly. Same-day tickets are a gamble.", "Sagrada Família"),
        day(4, "Boqueria early, then leave", "The market is useful at opening and grim by noon.", "La Boqueria when it opens. Fruit and a coffee. Then out. The front stalls are for visitors; the back is closer to a market.", "A last Gothic lane and checkout.", "Train or taxi. Do not walk La Rambla with your hands full of luggage and a phone out for the map.", "The airport bus and the metro both work. The bus is simpler with bags.", "La Boqueria"),
    ],
    attractions=[
        sight("Gothic Quarter, Barcelona", "The walk itself. Squares, the cathedral, and streets that do not need a ticket.", "Stay off the Rambla except to cross it.", "Gothic Quarter, Barcelona"),
        sight("Barcelona Cathedral", "The Gothic cathedral in the quarter, cloister and geese included.", "Morning. The roof is optional.", "Barcelona Cathedral"),
        sight("Sagrada Família", "The one Gaudí ticket. The interior columns are the reason.", "Timed entry. Do not add Casa Batlló and Park Güell to the same day.", "Sagrada Família"),
        sight("La Boqueria", "The market on the Rambla. Go early or skip it.", "Opening time. Watch your bag at the entrance.", "La Boqueria"),
        sight("Palau de la Música Catalana", "The concert hall with the skylight. A tour if you want one building that is not Gaudí.", "Book the tour. The street outside is easy to miss.", "Palau de la Música Catalana"),
        sight("Park Güell", "The other Gaudí park. It is a half day on a hill and it needs a ticket for the monumental zone.", "Leave it for another trip, or a different morning. Not the Sagrada day.", "Park Güell"),
    ],
    scenic_routes=[
        route("Gothic loop", "Cathedral, Sant Felip Neri, down to Plaça Reial only to look, back into the lanes. Cross the Rambla, do not stroll it.", "About 3 km"),
        route("Into El Born", "Via Laietana or the Gothic edge to Santa Maria del Mar and the streets behind it.", "About 2 km"),
        route("Metro to Sagrada and back", "The one transit morning. L2 or L5 depending on your stop. Then you are back on foot.", "About 15-20 minutes each way"),
    ],
    transport="Walk the old center. Metro for Sagrada Família only. A car is a liability. Airport: Aerobús or metro. Taxis are worth it late with bags. Do not follow a stranger to a different taxi queue.",
    food=[
        dish("Pa amb tomàquet", "A Born bar, or bread and tomato from a bakery", "Rubbed tomato, oil, salt. It is the base of lunch, not a cute starter to skip."),
        dish("Bombas", "La Cova Fumada, Barceloneta", "The potato-and-meat croquettes this bar is known for. No reservations, go early, often cash. Worth the walk on the beach afternoon."),
        dish("Cava and a tin", "El Xampanyet, El Born", "A standing glass and seafood from a tin. Crowded, old, and better than a Rambla paella."),
        dish("Churros", "Granja Dulcinea, Carrer Petritxol", "Chocolate and churros on a Gothic side street. Afternoon, not breakfast every day."),
    ],
    tips=[
        "Phone in a front pocket. Bag on your chest or in your lap, never on a chair back. La Rambla, the metro doors, and the Sagrada steps are the usual spots.",
        "Do not sign a petition. The clipboard teams are a theft routine.",
        "One Gaudí ticket. Sagrada in the morning. Park Güell is a different day if you are desperate to go.",
        "Paella on the Rambla is a bad lunch. If you want rice, eat it somewhere that cooks rice, on purpose, another day.",
    ],
    faqs=[
        faq("Can I walk Sagrada Família from the Gothic Quarter?", "You can, in half an hour or more. The metro is the right call before a timed entry so you are not late and sweaty."),
        faq("Is Park Güell on this trip?", "Only if you already have tickets and a free morning. The plan is one Gaudí visit."),
        faq("How bad are pickpockets?", "Bad enough to change how you carry a phone. Violent robbery is rarer. Theft from a loose bag is ordinary."),
        faq("Are the hotel rooms big?", "Neri and Ohla vary. Banys Orientals is small on purpose. You are booking the door."),
    ],
    map_places=[
        stop("Gothic Quarter", "Barcelona", "Spain", "Gothic Quarter, Barcelona"),
        stop("Barcelona Cathedral", "Barcelona", "Spain", "Barcelona Cathedral"),
        stop("Sagrada Família", "Barcelona", "Spain", "Sagrada Família"),
        stop("La Boqueria", "Barcelona", "Spain", "La Boqueria"),
        stop("Palau de la Música Catalana", "Barcelona", "Spain", "Palau de la Música Catalana"),
    ],
    budget_notes="Banys Orientals can sit near $150-250. Neri and Ohla cost more and you are paying for the square or the design. Sagrada tickets are the prepaid hit. Food stays reasonable if you eat pa amb tomàquet, one tapa bar, and not a Rambla terrace. The walks are free and the theft is not, so carry less.",
))


add(trip(
    slug="barcelona-family-friendly-with-kitchen",
    title="Barcelona with kids: Eixample kitchens, one beach morning, timed Sagrada",
    location="Barcelona, Spain",
    summary=(
        "Four nights in an apartment with a kitchen, aimed at the Eixample rather than a Rambla hotel. Eric Vökel's Sagrada Família and Gràcia buildings have two-bedroom apartments and real stoves. "
        "Citadines Ramblas is a one-bedroom apart-hotel on the pickpocket street, useful only if you accept that. Sagrada needs timed tickets. The beach is a morning, and the superblock streets are the playground."
    ),
    who="Parents who will cook breakfast, book the basilica, and leave the beach before the afternoon crush.",
    best_time="May, June, and September for a beach morning that is warm and not August. April and October can still be beach walks. August is hot, crowded, and a harder cap on patience.",
    nights=4,
    hook="4 nights · Eixample kitchens · Beach morning and a timed basilica",
    constraints=["Kitchen", "Family", "Timed Sagrada tickets"],
    lodging="$160-420",
    daily="$260-520",
    neighborhoods=[
        stay_area("Sagrada Família and Gràcia edge", "Eric Vökel Sagrada Familia Suites on Carrer de la Indústria, and Eric Vökel BCN Suites on Carrer d'en Grassot. Two-bedroom apartments with kitchens, a walk to the basilica, ordinary local shops."),
        stay_area("La Rambla", "Citadines Ramblas, at number 122. A real kitchen in the studio and the one-bedroom, and the city's least relaxing family street. Book it only if the Eixample apartments are gone."),
    ],
    hotels=[
        hotel("Eric Vökel Sagrada Familia Suites", "Carrer de la Indústria, Eixample", "Apartments about 700 meters from the basilica. Book the two-bedroom with a kitchen, not the one-bedroom attic. Washer, dishwasher, a normal stove. This is the family base. You are in a residential grid, not on the beach.", "$170-380", "Barcelona"),
        hotel("Eric Vökel BCN Suites", "Carrer d'en Grassot, Gràcia side", "The sister building between Sagrada Família and Gràcia, also with two-bedroom apartments and full kitchens. Same operator, slightly different walk. Pick it if you want Gràcia squares in the evening.", "$170-380", "Barcelona"),
        hotel("Citadines Ramblas Barcelona", "La Rambla 122", "An aparthotel. The studio and the one-bedroom have kitchens; the classic room does not. The largest apartment is one bedroom that sleeps four, not two bedrooms. The Rambla is noisy and it is where bags get opened. Use it as the central backup, not the first choice with children.", "$180-360", "Barcelona"),
    ],
    itinerary=[
        day(1, "Groceries and a superblock", "The kitchen and a place to run, before any ticket.", "Check in. Mercadona, Bonpreu, or a bakery. Tomatoes, bread, and oil so breakfast is pa amb tomàquet at the table.", "Walk to the Consell de Cent green axis, the pedestrian superblock streets in the Eixample, and let them use the play areas. If you are at the Rambla, go anyway. The apartment is not the park.", "Cook. Early night. The Rambla, if you are on it, gets worse after dark.", "Confirm the two-bedroom if you booked Eric Vökel. A sofa is not a second room.", ""),
        day(2, "Sagrada Família, timed", "The basilica in the morning. Skip the towers with small children.", "Your ticket slot. The floor, the columns, the light. The tower stairs are narrow and slow. Do not add them for a six-year-old.", "Back toward the apartment. A playground on the way, or Ciutadella if you want a classic park and can face the metro.", "Dinner in. You already did the hard ticket.", "Book the family slot before you book the flights. Same-day entry is how the morning collapses.", "Sagrada Família"),
        day(3, "Beach morning", "Barceloneta early, home for lunch, bags never left alone.", "Metro or bus to the beach. Go when it opens in spirit, not at 1 p.m. The water is a city Mediterranean, fine for a swim, not a brochure bay.", "One adult watches everything while the others swim. Leave before the afternoon wind and the theft hour. Lunch is in the apartment, which is why you have a kitchen. Beach restaurants are slow and expensive with hungry children.", "A quiet evening. Gràcia squares if you are at BCN Suites. Do not do Park Güell unless you already hold tickets and everyone voted yes.", "Sun cream, water, and a bag that stays on a person.", ""),
        day(4, "Short Gothic walk or straight to the airport", "One old-city hour if the flight allows.", "Breakfast in. A short metro to the cathedral quarter if you have the morning. Keep the loop small.", "Checkout and the Aerobús or a taxi. The Rambla with luggage is a bad last walk.", "Eat before the airport.", "If the flight is early, the Gothic Quarter can wait for another trip.", "Gothic Quarter, Barcelona"),
    ],
    attractions=[
        sight("Sagrada Família", "The one prepaid family sight. It works because the room looks like a forest.", "Timed tickets. Towers optional and a poor idea for small children.", "Sagrada Família"),
        sight("Consell de Cent superblock", "Pedestrian Eixample streets with play space. The local playground, not a theme park.", "Walk there from the Eric Vökel buildings. Let them stay a while.", ""),
        sight("Parc de la Ciutadella", "The big park with shade, a lake, and room to run.", "A metro hop from the apartments. Bring water.", "Parc de la Ciutadella"),
        sight("Barceloneta beach", "The city beach. A morning, then leave.", "Never leave a bag on the sand. The water is fine and the promenade is where phones disappear.", ""),
        sight("Gothic Quarter, Barcelona", "A short last-morning walk if you have the time.", "One loop. Do not add the Rambla as the route.", "Gothic Quarter, Barcelona"),
        sight("Park Güell", "Only with tickets already in hand and older children who want the hill.", "It is a half day. It does not fit beside the beach and the basilica.", "Park Güell"),
    ],
    scenic_routes=[
        route("To the superblock", "From the Indústria or Grassot apartments across the Eixample grid to the pedestrian stretch of Consell de Cent.", "About 20 minutes"),
        route("Metro to Barceloneta", "A beach morning and a ride home before lunch in the apartment.", "About 25-35 minutes each way"),
        route("Walk to the basilica", "From either Eric Vökel building to the Sagrada entrance. Do it on the ticket morning so you are not late.", "About 10 minutes"),
    ],
    transport="Metro for the beach and for Ciutadella. Walk to Sagrada from these apartments. The Rambla apart-hotel is the one you do not want to stroll from at night. Aerobús for the airport with a stroller; a taxi if the car seat matters. Pickpockets ride the metro at the doors. Hold the bag in front when the doors open.",
    food=[
        dish("Pa amb tomàquet", "The apartment", "Bakery bread, ripe tomatoes, oil, salt. Children will eat this every morning. That is the kitchen working."),
        dish("Bombas", "La Cova Fumada, on the beach morning", "Go early, before or after the swim, not at the hungry peak. No reservations. A small, famous room."),
        dish("Roast chicken", "A rostisseria near the apartment", "The night you do not cook from scratch. Better than a beach restaurant with a meltdown."),
        dish("Churros", "Granja Dulcinea, if you do the Gothic morning", "One shared order. Then back. It is not dinner."),
    ],
    tips=[
        "Book the two-bedroom at Eric Vökel. Citadines tops out at a one-bedroom and sits on La Rambla.",
        "Sagrada towers are a separate timed climb. Skip them with small children.",
        "Beach bags stay on a person. One adult does not swim.",
        "The superblock is the playground you can walk to. You do not need an amusement park.",
    ],
    faqs=[
        faq("Do we have to book Sagrada Família?", "Yes. Timed tickets. The interior is what children can enjoy. The towers are optional and cramped."),
        faq("Is Citadines a two-bedroom?", "No. One-bedroom apartments sleep four with a sofa, and the classic rooms have no kitchen. The Rambla is the other problem."),
        faq("Can we swim all day?", "You can, and you will watch the bags and the sun. A morning and lunch at home is the version that works."),
        faq("Where is the playground?", "On the pedestrian superblock streets, especially Consell de Cent in the Eixample, a walk from the Eric Vökel buildings. Ciutadella is the larger park by metro."),
    ],
    map_places=[
        stop("Sagrada Família", "Barcelona", "Spain", "Sagrada Família"),
        stop("Parc de la Ciutadella", "Barcelona", "Spain", "Parc de la Ciutadella"),
        stop("Gothic Quarter", "Barcelona", "Spain", "Gothic Quarter, Barcelona"),
        stop("Park Güell", "Barcelona", "Spain", "Park Güell"),
        stop("La Boqueria", "Barcelona", "Spain", "La Boqueria"),
    ],
    budget_notes="Eric Vökel two-bedrooms often sit in a family range under or around $400 outside peak weeks. Citadines is similar money for less peace. Groceries are the saving. Sagrada tickets for a family are the shock. The beach and the superblock are free, and a careless hour on the sand is how a phone gets expensive.",
))


add(trip(
    slug="athens-2-bedroom-under-400night",
    title="Athens two-bedrooms under $400, except in August",
    location="Athens, Greece",
    summary=(
        "Four nights near the Acropolis in a two-bedroom with a kitchen. Outside August, under $400 is a normal rate in Koukaki and Thissio. August is the month that rate jumps. "
        "Athens Studios and Hercules Residence have real two-bedroom apartments. Marble House is the long-running Koukaki pension, and its apartment is one bedroom plus sofa beds, so count the doors."
    ),
    who="A family or two couples who want to walk to the Acropolis and cook one or two dinners.",
    best_time="April to early June, and late September through October. August is hot and the pleasant two-bedrooms can pass $400. July is already warm enough to do the Acropolis at opening.",
    nights=4,
    hook="4 nights · Koukaki or Thissio · Under $400 except August",
    constraints=["Two bedrooms where the plan says so", "Kitchen", "Under $400 outside August"],
    lodging="$90-360",
    daily="$160-450",
    neighborhoods=[
        stay_area("Koukaki and Makrigianni", "Athens Studios on Veikou, a few minutes from the Acropolis Museum. Marble House is on a dead-end residential street. You walk to the rock."),
        stay_area("Thissio", "Hercules Residence, toward Kerameikos. Two-bedroom apartments with kitchens, a walk to the Ancient Agora and the Acropolis paths."),
    ],
    hotels=[
        hotel("Athens Studios", "Veikou, Makrigianni", "Studios and apartments with kitchens, beside the Acropolis Museum. Book the apartment that has two bedrooms. A studio that sleeps four is the cheaper listing and the wrong one. Self check-in is normal. Under $400 is the usual story outside August.", "$120-320", "Athens"),
        hotel("Marble House Pension", "Zinni, Koukaki", "A family-run pension on a quiet dead-end, long established. The separate apartment has a real kitchen and a veranda, and it is one bedroom plus sofa beds, not two closed bedrooms. The rate is far under $400. Use it if you can live with the sofa, or choose Athens Studios for the second door.", "$80-180", "Athens"),
        hotel("Hercules Residence", "Thissio", "Two-bedroom apartments with kitchens, a walk to the Agora and the Acropolis. This is the Thissio version of the brief. Confirm the August rate. The rest of the year it belongs under the cap.", "$130-340", "Athens"),
    ],
    itinerary=[
        day(1, "Keys, bread, the rock at dusk from below", "Do not climb the Acropolis on arrival unless your ticket says so.", "Check in, learn the kitchen, buy bread and fruit at a bakery and a Sklavenitis or a small market.", "Walk the streets under the Acropolis. The museum neighborhood in the late light is enough. Souvlaki for dinner if you do not cook.", "An early night. Tomorrow starts at opening.", "Count bedrooms before you unpack.", "Acropolis of Athens"),
        day(2, "Acropolis at opening, Agora after", "The rock in the morning, the market square of ancient Athens when it is hotter and you want shade and trees.", "Timed Acropolis entry. The Parthenon, then down. Carry water. There is little shade.", "Ancient Agora. The Temple of Hephaestus is the building in the trees, and it is the calm part of the day.", "Cook, or souvlaki from a shop. Kostas, near Agia Irini, is the classic small queue if you want one named souvlaki and will walk to Psyrri.", "Hats. The marble throws the heat back at you.", "Acropolis of Athens"),
        day(3, "Plaka early, one museum if you still want one", "Plaka before the shops are fully open. Then either the National Archaeological Museum or a quiet afternoon.", "Plaka lanes and Anafiotika, the island-style houses on the slope. Leave before it turns into a menu corridor.", "National Archaeological Museum if everyone still has a museum in them. It is the best one and it is not next to the rock; take the metro. If not, stay in Koukaki and cook.", "Dinner at a taverna without a photo menu. Diporto, by the central market, is the basement room with no sign, cash, and a short list. Closed some days. Otherwise a Koukaki taverna a neighbor would use.", "Plaka tavernas with pictured fish are the ones to walk past.", "Plaka"),
        day(4, "A last souvlaki and the airport", "Empty the fridge. The metro reaches the airport.",
         "Breakfast from the bakery. A last walk under the walls if the flight is late.", "Checkout. These are apartments: do not leave the kitchen filthy.", "Metro to the airport from Akropoli or Kerameikos, with a change. Leave a margin.", "August taxis to the airport in the heat are fine if the metro with bags sounds miserable. Price it before you get in.", "Ancient Agora of Athens"),
    ],
    attractions=[
        sight("Acropolis of Athens", "The morning ticket. The Parthenon is the reason the neighborhood costs what it costs.", "Opening slot. Water. Then leave.", "Acropolis of Athens"),
        sight("Acropolis Museum", "The finds, in air conditioning, next to Athens Studios. A fair afternoon if you do not want another climb.", "The top floor for the Parthenon sculptures.", "Acropolis Museum"),
        sight("Ancient Agora of Athens", "The civic center below the rock. Trees and the Hephaestus temple.", "After the Acropolis, not before, so you are not late for the timed entry.", "Ancient Agora of Athens"),
        sight("Plaka", "The old lanes on the north slope. Lovely early, commercial later.", "Morning. Eat somewhere else.", "Plaka"),
        sight("Temple of Olympian Zeus", "The tall columns by the arch. A short stop, not a half day.", "On the way to or from the stadium side if you are already walking.", "Temple of Olympian Zeus"),
        sight("National Archaeological Museum, Athens", "The museum for the serious objects, in Exarchia, not on the Acropolis path.", "A separate metro ride. Two hours. Skip it if the group is done.", "National Archaeological Museum, Athens"),
    ],
    scenic_routes=[
        route("Under the walls", "From Koukaki along the pedestrian streets south of the Acropolis, toward Plaka or back.", "About 2 km"),
        route("Acropolis then the Agora", "The ticket morning, down the south or west slope, into the Agora.", "A full morning"),
        route("Thissio to the Agora", "From Hercules Residence through Thissio to the temple of Hephaestus. The easy version of day two's second half.", "About 1.5 km"),
    ],
    transport="Walk to the Acropolis from all three stays. Metro line 2 at Akropoli for the museum neighborhood and for connections. The airport metro is direct enough with one change and a long ride. August heat makes a taxi to the rock a waste: you still have to walk the top. Buy the Acropolis time before you arrive.",
    food=[
        dish("Souvlaki", "Kostas, near Agia Irini, or a Koukaki corner shop", "Pita, meat, onion, tomato, a fry or not. This is the meal. A Plaka taverna with a photo menu is how you pay more for less."),
        dish("Tyropita", "A bakery on the way to the rock", "Cheese pie for breakfast. Buy it where the locals are queued, not in the hotel."),
        dish("Horiatiki", "A taverna in Koukaki or Thissio", "Tomato salad. Worth it when the tomatoes are in season, late spring through summer. In winter, eat something else."),
        dish("A market lunch", "Diporto, near the central market", "No sign, cash, a few dishes, barrel wine. Go for lunch, not for a romantic dinner. It is the opposite of a Plaka terrace."),
    ],
    tips=[
        "Under $400 holds outside August. In August, ask for the rate before you assume the cap.",
        "Athens Studios and Hercules Residence are the two-bedroom kitchens. Marble House's apartment is one bedroom and sofas, at a much lower price.",
        "Acropolis tickets are timed. Book the first slot you can stand.",
        "Freddo espresso is the cold coffee. Drink it. The August version of sightseeing depends on it.",
    ],
    faqs=[
        faq("Is a two-bedroom under $400 realistic?", "Yes, except in August, when a pleasant Koukaki two-bedroom can cross the cap. Marble House stays under it and is not a strict two-bedroom."),
        faq("How far is the Acropolis?", "A short walk from Makrigianni and from Thissio. The climb and the sun are the issue, not the distance."),
        faq("Do we need a car?", "No. A car in this neighborhood is a place to get it scratched. The metro goes to the airport."),
        faq("Can we cook?", "Yes at Athens Studios and Hercules Residence. Marble House's apartment has a stove too. The pension rooms are a different, simpler product."),
    ],
    map_places=[
        stop("Acropolis of Athens", "Athens", "Greece", "Acropolis of Athens"),
        stop("Acropolis Museum", "Athens", "Greece", "Acropolis Museum"),
        stop("Ancient Agora of Athens", "Athens", "Greece", "Ancient Agora of Athens"),
        stop("Plaka", "Athens", "Greece", "Plaka"),
        stop("National Archaeological Museum", "Athens", "Greece", "National Archaeological Museum, Athens"),
    ],
    budget_notes="Outside August, $90-320 covers these apartments, with Marble House at the bottom and a two-bedroom at Athens Studios or Hercules in the middle. August can break $400 for the nicer two-bedrooms. Souvlaki keeps food cheap. The Acropolis ticket is the main extra. Groceries in Koukaki are normal city prices, not island prices.",
))


add(trip(
    slug="athens-near-the-beach-under-300",
    title="Athens beach under $300: Glyfada, Vouliagmeni, and the Saronic Gulf",
    location="Athens, Greece",
    summary=(
        "Four nights on the Athens coast, where the water is the Saronic Gulf, a real city beach and not a Caribbean bay. Palmyra Beach Hotel in Glyfada is the one that usually stays under $300, with the tram a few minutes away and a shared hotel pool that is not the sea. "
        "Amarilia and the Divani Apollon in Vouliagmeni are the beach hotels. The Divani, open since 1958, often breaks $300 in July and August. The Acropolis is a half day by tram and metro, not a quick errand."
    ),
    who="People who want to swim and still see the Acropolis once, without pretending they are on an island.",
    best_time="Late May, June, and September. The sea is warm enough and the $300 cap still shows up. July and August are hot, the beaches are busy, and the Vouliagmeni palace rates usually jump the cap. April is often too cold to swim.",
    nights=4,
    hook="4 nights · Saronic Gulf · Under $300 outside peak weeks",
    constraints=["City beach", "Under $300 in shoulder season", "Acropolis is a half day"],
    lodging="$90-320",
    daily="$160-420",
    neighborhoods=[
        stay_area("Glyfada", "Palmyra Beach Hotel on Poseidonos Avenue, about 50 meters from the beach and a short walk to the tram. A suburb with shops, traffic, and a swimmable gulf."),
        stay_area("Vouliagmeni", "Amarilia, by Kavouri beach, and the Divani Apollon, with a hotel beach and shared pools. Quieter water, a bit farther from the tram, clearer and less city than Glyfada."),
    ],
    hotels=[
        hotel("Palmyra Beach Hotel", "Poseidonos Avenue, Glyfada", "A 4-star beach hotel that often lands well under $300. The beach is a short walk. The tram stop is about 200 meters, which is how you do the Acropolis. The outdoor pool is the hotel's, shared, and it is not a substitute for the gulf.", "$90-220", "Glyfada"),
        hotel("Amarilia Hotel", "Vouliagmeni, near Kavouri", "A long-running 4-star on the Vouliagmeni coast, with a shared outdoor pool and the Saronic Gulf in front. Shoulder-season rates can fit under $300. August often does not. You are a bus or taxi beyond the easy Glyfada tram stop.", "$140-320", "Vouliagmeni"),
        hotel("Divani Apollon Palace & Thalasso", "Vouliagmeni", "The coast hotel open since 1958. Shared pools, a thalasso spa, and a beach reserved for guests. That beach is not a private pool. The room rate often sits over $300 from late June through August. May, early June, and September are when this page's cap and this hotel can meet.", "$180-450", "Vouliagmeni"),
    ],
    itinerary=[
        day(1, "Swim first", "You came for the gulf. Get in it before you plan a monument.", "Check in, then the beach. Glyfada is a city shore: a road, cafés, umbrellas for rent, water that is swimmable and not turquoise advertising. Vouliagmeni is quieter and usually clearer.", "A long afternoon in the water or under an umbrella you paid for. The hotel pool, where there is one, is shared and secondary.", "Dinner at a fish taverna. Point at the fish, ask the price per kilo, then sit down. Souvlaki is the cheap alternative and it is still the right food.", "The organized beaches charge for sunbeds. A towel on the free stretch is the budget version.", ""),
        day(2, "Another swim, no monuments", "One full beach day so the Acropolis day does not feel like the whole trip.", "Morning swim. The light is better and the sand is emptier.", "Lunch of salad and something grilled, or groceries if you have a kitchenette. Most of these rooms do not. Eat simply.", "A walk on the promenade. Glyfada's evening is cafés, not a Mykonos scene. Vouliagmeni Lake is a separate mineral lake a short hop from Amarilia if you want a different swim.", "Do not book a sunset cruise. The beach you have is the point.", ""),
        day(3, "Acropolis, then back to the water", "A half day. First ticket you can stand, then the tram or a taxi back.", "From Glyfada, the tram toward the center and a metro connection. Allow about an hour to the Acropolis slopes. From Vouliagmeni, a taxi is often the sane version and can take 30 to 50 minutes depending on traffic. Book the earliest Acropolis slot you will actually catch.", "The Parthenon, water, shade, and down. Do not add the Acropolis Museum on the same half day.", "Back to the hotel and into the gulf. That contrast is the trip.", "Hats and a timed ticket. A missed slot wastes the only monument morning.", "Acropolis of Athens"),
        day(4, "Last swim and the airport", "The airport is closer to this coast than people think, and traffic still exists.", "A morning swim.", "Checkout. If you are at the Divani or Amarilia and have an hour, Vouliagmeni Lake or Kavouri, not a dash back to Plaka.", "Taxi to the airport. From Glyfada or Vouliagmeni it is often under 40 minutes without traffic.", "Do not plan the Acropolis on departure day.", ""),
    ],
    attractions=[
        sight("Glyfada beach", "The city beach on the Saronic Gulf. Umbrellas, a promenade, and a real swim.", "Morning. It is a suburb, not a private island.", ""),
        sight("Vouliagmeni coast", "Quieter water around Kavouri and the hotel beaches. Clearer, less snack-bar.", "Go if you stayed here, or as a taxi from Glyfada for one afternoon.", ""),
        sight("Saronic Gulf", "The water itself. Part of the Aegean, in a gulf next to a city. Honest swimming, not a Caribbean color grade.", "Swim where the beach is organized or obviously used. Ask before you pick a random rock.", "Saronic Gulf"),
        sight("Acropolis of Athens", "The half-day ticket. Worth it once from the coast.", "First slot, then leave. The museum is a different day you do not have.", "Acropolis of Athens"),
        sight("Plaka", "You will see it only if you walk down from the Acropolis and still have time.", "A short loop or skip it. The beach afternoon is the priority.", "Plaka"),
        sight("Temple of Olympian Zeus", "The columns you can see if the ride back passes that way and you are not late for the sea.", "Skip it if the group wants the water. It will still be there.", "Temple of Olympian Zeus"),
    ],
    scenic_routes=[
        route("Glyfada tram toward the center", "From the stop near Palmyra, tram and metro to the Acropolis. About an hour. This is a half day, including the visit and the ride back.", "About an hour each way"),
        route("Vouliagmeni to the rock by taxi", "A car from Amarilia or the Divani. Fast when the avenue is clear, slow when it is not. Book the Acropolis with a margin.", "30-50 minutes"),
        route("The promenade", "A walk along the Glyfada or Vouliagmeni shore at the end of the day. No ticket.", "As long as you like"),
    ],
    transport="The Glyfada tram is the tool for Palmyra guests. Allow an hour to the Acropolis with the metro connection, not a tram that drops you at the Propylaea. Vouliagmeni is a taxi or a bus plus the tram. Airport taxis from this coast are straightforward. A rental car is useful only if you want several coves; parking at the Acropolis end is not a gift. Do not rent one for a single half day.",
    food=[
        dish("Fish by the kilo", "A taverna on the Glyfada or Vouliagmeni shore", "Choose from the display and ask the price per kilo before it is grilled. This is the coast meal. It can blow a food budget if you do not ask."),
        dish("Souvlaki", "A Glyfada shop, not a hotel club sandwich", "The cheap honest lunch. Pita, meat, tomato, onion. Eat it in your wet clothes."),
        dish("Horiatiki", "The same taverna", "When the tomatoes are ripe. It is a salad, not a meal by itself unless you add the fish or the souvlaki."),
        dish("Freddo espresso", "Any normal café on the avenue", "The cold coffee that makes August possible. Order it after the swim."),
    ],
    tips=[
        "The water is the Saronic Gulf. It is a good swim and a city shore. Do not expect an island poster.",
        "Palmyra is the under-$300 default. The Divani often costs more in July and August. Amarilia sits between them and can break the cap in peak weeks.",
        "Hotel pools here are shared. The sea is the swim you came for.",
        "The Acropolis is a half day from Glyfada. Do it once, early, and get back in the water.",
    ],
    faqs=[
        faq("Is this a beach holiday or a city holiday?", "A beach holiday with one city morning. Stay on the coast. Commuting up to Plaka every day wastes the gulf."),
        faq("Will $300 hold?", "At Palmyra, usually. At Amarilia, in the shoulder season. At the Divani Apollon, more often in May, early June, and September than in July or August."),
        faq("How do we get to the Acropolis?", "From Glyfada, tram and metro, about an hour. From Vouliagmeni, a taxi is the practical version. Book the first Acropolis slot you can reliably reach."),
        faq("Is the sea clean?", "Swimmable, and cleaner toward Vouliagmeni than on the busiest Glyfada stretch. It is a gulf beside a city, not a deserted cove."),
    ],
    map_places=[
        stop("Glyfada", "Glyfada", "Greece", "Glyfada"),
        stop("Vouliagmeni", "Vouliagmeni", "Greece", "Vouliagmeni"),
        stop("Acropolis of Athens", "Athens", "Greece", "Acropolis of Athens"),
        stop("Saronic Gulf", "Glyfada", "Greece", "Saronic Gulf"),
        stop("Plaka", "Athens", "Greece", "Plaka"),
    ],
    budget_notes="Palmyra often lands $90-200. Amarilia and the Divani need a shoulder-season date to respect $300, and the Divani in August usually does not. Sunbeds are a daily extra. Fish by the kilo is the splurge; souvlaki is the control. One taxi to the Acropolis from Vouliagmeni is still cheaper than moving the whole stay into the center.",
))
