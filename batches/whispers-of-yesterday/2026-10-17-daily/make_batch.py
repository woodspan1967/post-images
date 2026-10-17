import json, os
T1 = "A warm hand-painted Saturday Evening Post style illustration with visible brushstrokes and slightly stylized faces, clearly a painting, not a photograph, "
T1_END = " Norman Rockwell influence, warm amber and honey tones, nostalgic American setting. "
T3 = "A vintage 1960s educational illustration in flat retro style, warm cream background, "
T3_END = " Saturday Evening Post illustration style, warm muted palette, clean lines, nostalgic school textbook aesthetic, people drawn as flat stylized illustrations. "
END = "No other text, signs, logos, signatures, or watermarks anywhere in the image; keep the bottom corners plain. Vertical 4:5 portrait format."
D = "2026-10-17-daily"; IMG = f"images/whispers-of-yesterday/{D}/"

def t1(scene, quote, place="Bold white text with a thin dark outline across the top of the image, no bubble, reads exactly"):
    return T1 + scene + f" {place}: \"{quote}\"." + T1_END + END
def t2(scene, quote, pos="top"):
    return ("A realistic color photograph from the early 1960s, " + scene + " No people anywhere in the frame. Authentic period photograph style, warm faded color, fine grain. "
            f"Bold white uppercase text at the {pos} reads exactly: \"{quote}\". " + END)
def t3(scene, head, sub):
    return T3 + scene + f" Bold retro serif headline text at top reads exactly: \"{head}\". Smaller subtitle text below the headline reads exactly: \"{sub}\"." + T3_END + END

posts = []
def img(n, tmpl, theme, quote, caption, first, prompt, ai=False, story=False):
    pid = (f"wys-20261017-{n}" if story else f"wy-20261017-{n:02d}")
    d = {"id": pid, "kind": "story" if story else "image", "template": tmpl, "character": theme, "quote": quote,
         "caption": caption, "first": first, "prompt": prompt, "ai": ai,
         "image": IMG + ("stories/" if story else "") + pid + ".png"}
    return d

feed = [
img(6, "T1 illustrated scene", "Childhood rules and rituals (carving pumpkins)",
 "DAD CARVED THE FACE, MOM SAVED THE SEEDS, AND THE KIDS GOT THE JOB NOBODY WANTED: SCOOPING OUT THE GUTS.",
 "Every October the newspapers came out and got spread across the kitchen table, and that was how you knew it was pumpkin night. Dad got the big knife and the final say on the face. Mom stood by with a bowl, because not one seed in that house was going to waste. That left the kids, sleeves rolled up past the elbow, reaching into a cold, slimy pumpkin and pulling out handfuls of strings. We complained the whole time. Then the candle went in, the lights went off, and every one of us forgot we ever did.",
 "My little sister refused to touch the inside of a pumpkin, so I did hers and mine every year. Mom roasted the seeds with salt on a cookie sheet and they were gone before they cooled. I can still smell that kitchen.\n\n#WhispersOfYesterday #ChildhoodMemories #RememberWhen #GrowingUpIn60s #FallMemories #GoodOldDays",
 t1("on an October evening in a 1960s kitchen, newspapers spread across a wooden table holding a big orange pumpkin with its top cut off. A father in a cardigan carefully carves a toothy grin with a kitchen knife, a mother in an apron holds a mixing bowl of pumpkin seeds, and two children of about eight and ten, sleeves rolled up, pull out stringy pumpkin insides with disgusted, laughing faces. A finished jack-o'-lantern glows on the windowsill.",
 "DAD CARVED THE FACE, MOM SAVED THE SEEDS, AND THE KIDS GOT THE JOB NOBODY WANTED: SCOOPING OUT THE GUTS.")),
img(7, "T2 vintage photo", "Real-photo nostalgia (diner jukebox)",
 "A QUARTER IN THE JUKEBOX BOUGHT YOU THREE SONGS, AND THE WHOLE DINER HAD TO LISTEN.",
 "Every diner worth its pie had one, glowing in the corner like a church window. You'd lean over the glass and flip through the cards one at a time, reading every title twice. Three songs for a quarter meant real decisions. Pick the wrong one and the whole counter would let you know it. Pick the right one and the cook would start humming along behind the window. It was the only place in town where a kid with a quarter controlled the room.",
 "There was a jukebox at a diner on Route 9 that had the same songs on it for about twelve years. My dad played the same one every single time we stopped. I knew every word by the time I was six.\n\n#WhispersOfYesterday #BoomerMemories #RetroLife #VintageLife #RememberWhen #AmericanNostalgia",
 t2("inside an empty 1950s roadside diner at night: a glowing chrome-and-glass jukebox with warm colored lights and arched bubble tubes stands at the end of a long chrome counter with red vinyl stools, a pie under a glass dome on the counter, checkered floor, neon-free windows showing a dark parking lot. The jukebox has no brand name and its song cards are blank or unreadable.",
 "A QUARTER IN THE JUKEBOX BOUGHT YOU THREE SONGS, AND THE WHOLE DINER HAD TO LISTEN."), ai=True),
img(8, "T1 illustrated scene", "Old-school parenting (pull this car over)",
 "\"DON'T MAKE ME PULL THIS CAR OVER.\" HE NEVER DID, AND WE NEVER FOUND OUT WHAT HAPPENED IF HE DID.",
 "It always started somewhere around the second hour. Somebody's elbow crossed the invisible line down the middle of the back seat, and somebody else made sure the whole car heard about it. Mom would turn around first, which was a warning. Then Dad's eyes would find you in the rearview mirror, and that was serious. When he finally said the words, the back seat went so quiet you could hear the tires. Nobody knew what happened on the side of the road, and nobody was ever brave enough to find out.",
 "Three of us in the back of a wood-paneled station wagon, no air conditioning, eight hours to Grandma's. Dad said those words at least once per state. He slowed down one time and I thought my brother was going to cry.\n\n#WhispersOfYesterday #OldSchool #BoomerMemories #GrowingUpIn70s #BackInTheDay #ChildhoodMemories",
 t1("inside a 1960s family station wagon on a summer highway, seen from the back seat: three squabbling children of about seven to eleven freeze mid-argument, one pointing at the other's elbow, while the father's stern eyes stare back at them in the rearview mirror and the mother turns around from the front bench seat with a warning finger raised. Fields and telephone poles roll by the windows.",
 "\"DON'T MAKE ME PULL THIS CAR OVER.\" HE NEVER DID, AND WE NEVER FOUND OUT WHAT HAPPENED IF HE DID.", "A white rounded speech bubble with a tail pointing toward the father's eyes in the mirror reads, in bold black text, exactly")),
{"id": "wy-20261017-t1", "kind": "tobi", "template": "TOBI (black)", "character": "Humor about today vs. then (the family dog)",
 "quote": "We didn't have a garbage disposal. We had a dog under the table and a mother who pretended not to see.",
 "caption": "",
 "first": "Our beagle Rusty knew exactly which chair the lima beans came from. He'd sit next to me and wait without making a sound. Mom knew the whole time and never said a word.\n\n#WhispersOfYesterday #RememberWhen #BoomerMemories #OldSchool #ChildhoodMemories #GoodOldDays"},
img(9, "T3 retro poster", "Lost school subjects (clapping erasers)",
 "CLAPPING ERASERS / STAYING AFTER SCHOOL TO BEAT THE CHALK OUT OF THEM WAS SOMEHOW AN HONOR",
 "At the end of the day the teacher would look out over the room and pick two names, and the two of you would try not to look too pleased about it. You'd carry an armload of felt erasers out the back door and bang them together against the brick wall. White clouds of chalk dust went everywhere: your hair, your sweater, your eyebrows. You came home looking like you'd been in a flour fight. Your mother asked what happened. You told her, proud as anything, that you'd been chosen.",
 "Mrs. Albright picked me for erasers about once a week in third grade, and I thought it meant I was her favorite. Years later I figured out she just picked whoever talked the most. There was a white spot on that brick wall the whole time I went there.\n\n#WhispersOfYesterday #SchoolDays #GrowingUpIn60s #RememberWhen #ChildhoodMemories #BackInTheDay",
 t3("outside the brick back wall of a 1960s elementary school on a sunny afternoon, two children of about nine, a boy in a sweater vest and a girl with pigtails, clap chalkboard erasers together, big puffs of white chalk dust billowing around them and dusting their hair, a stack of felt erasers on the steps beside them, a teacher smiling from the open doorway.",
 "CLAPPING ERASERS", "STAYING AFTER SCHOOL TO BEAT THE CHALK OUT OF THEM WAS SOMEHOW AN HONOR")),
img(10, "T1 illustrated scene", "Crafts and homemaking (gelatin salad)",
 "EVERY HOLIDAY TABLE HAD A WOBBLY GREEN SALAD WITH SOMETHING FLOATING IN IT THAT NOBODY COULD NAME.",
 "It came out of the refrigerator on Grandma's good glass plate, still shivering from the trip. It was green, it was shaped like a ring, and there was definitely something suspended inside it. Some years it was fruit cocktail. Some years it was shredded carrots. One year there was something that looked like celery and tasted like a mystery. Nobody ever asked for the recipe, and nobody ever dared skip it. It was on the table every Thanksgiving, and somehow it's the dish we miss the most.",
 "My Aunt Ruth made hers with cottage cheese and pineapple, and she was very proud of it. Every one of us took a spoonful to be polite. I'd give anything for one more polite spoonful.\n\n#WhispersOfYesterday #FamilyTraditions #BoomerMemories #RememberWhen #GrowingUpIn60s #AmericanNostalgia",
 t1("a 1960s Thanksgiving dinner table in a warmly lit dining room, a smiling grandmother in a floral dress and apron sets down a glass plate holding a tall wobbly green gelatin ring mold with bits of fruit and shredded carrot suspended inside it, while three family members around the table, an uncle, a teenage girl and a boy of about eight, eye it with polite, suspicious smiles. Roast turkey, mashed potatoes and candles fill the table.",
 "EVERY HOLIDAY TABLE HAD A WOBBLY GREEN SALAD WITH SOMETHING FLOATING IN IT THAT NOBODY COULD NAME.")),
img(11, "T2 vintage photo", "Cars and driving culture (tail fins)",
 "TAIL FINS AS TALL AS A FENCE POST, AND A BACK SEAT BIG ENOUGH TO RAISE A FAMILY IN.",
 "You could spot one from a block away, those chrome fins sweeping up off the back like the car was about to take off. They were longer than some driveways. The back seat was a sofa with doors, and on a long trip you could lay down across it with room to spare. Parking it took a team effort and a prayer. Nobody cared about the gas mileage. When one of those rolled down Main Street on a Saturday night, everybody on the sidewalk turned to watch it go by.",
 "Our neighbor Mr. Hadley had a pink one with fins so sharp my mother made us walk around them. He washed it every Saturday morning and wouldn't let anybody lean on it. When he finally sold it, I think he cried.\n\n#WhispersOfYesterday #ClassicCars #BoomerMemories #RetroLife #AmericanNostalgia #GrowingUpIn60s",
 t2("a long pastel pink late-1950s American sedan with towering chrome-trimmed tail fins and red bullet taillights, parked at the curb of a quiet small-town street at dusk, seen from a rear three-quarter angle, a white picket fence and elm trees behind it, warm street lamp glow. The car has no badges, emblems, readable license plate, or brand names.",
 "TAIL FINS AS TALL AS A FENCE POST, AND A BACK SEAT BIG ENOUGH TO RAISE A FAMILY IN."), ai=True),
img(12, "T1 illustrated scene", "Old jobs and skills (movie usher)",
 "THE USHER HAD A FLASHLIGHT AND A LOOK, AND HE KNEW EXACTLY WHICH ROW YOU WERE TALKING IN.",
 "He wore a red jacket with brass buttons and walked the aisle like he owned the place, which as far as we knew, he did. He'd walk you to your seat with that flashlight pointed at the floor, polite as a butler. But start whispering during the picture and that beam would land right on your face. He never said much. He didn't have to. One flash of light and the whole row sat up straight for the rest of the show.",
 "The usher at the Rialto was a tall, skinny fellow named Walt who must have been seventy. He caught my friend Danny with his feet on the seat in front of him and just stood there with the light on his shoes until Danny put them down. We behaved after that.\n\n#WhispersOfYesterday #OldSchool #BoomerMemories #RememberWhen #BackInTheDay #VintageLife",
 t1("inside a grand 1950s movie palace during a show, dim red velvet seats and gold trim lit by the glow of the screen. A stern older usher in a red jacket with brass buttons and a little cap stands in the aisle shining a flashlight beam right onto two whispering boys of about twelve, who freeze with wide guilty eyes while a woman nearby turns to look. Popcorn boxes in their laps are plain red and white with no writing.",
 "THE USHER HAD A FLASHLIGHT AND A LOOK, AND HE KNEW EXACTLY WHICH ROW YOU WERE TALKING IN.")),
img(13, "T3 retro poster", "Values and work ethic (passbook savings)",
 "THE PASSBOOK SAVINGS ACCOUNT / A QUARTER A WEEK, A STAMP IN THE LITTLE BOOK, AND A TELLER WHO MADE YOU FEEL LIKE A MILLIONAIRE",
 "Your first bank account came with a little book that fit in your back pocket, and you guarded it like a passport. Every Saturday you stood on your toes at the counter and slid your quarter across the marble. The teller wrote it in, stamped the date, and handed it back like you were a regular customer. Twice a year the interest showed up, a few cents you didn't do a thing to earn. You'd add it all up on the walk home. It wasn't much, but every penny of it was yours.",
 "I opened mine at the bank downtown with four dollars of birthday money. The teller was a lady with cat-eye glasses who always called me \"young man.\" I was nine and I stood an inch taller every time.\n\n#WhispersOfYesterday #OldSchool #GrowingUpIn60s #BoomerMemories #RememberWhen #GoodOldDays",
 t3("split into two panels: the left panel shows a boy of about nine on tiptoes at a tall marble bank counter sliding a coin to a smiling teller in cat-eye glasses behind a brass teller's window; the right panel shows a close-up of a small blue savings passbook lying open with neat handwritten columns of numbers and round date stamps beside a coin bank shaped like a pig.",
 "THE PASSBOOK SAVINGS ACCOUNT", "A QUARTER A WEEK, A STAMP IN THE LITTLE BOOK, AND A TELLER WHO MADE YOU FEEL LIKE A MILLIONAIRE")),
img(14, "T1 illustrated scene", "Values and manners (thank-you notes)",
 "BEFORE YOU PLAYED WITH ONE CHRISTMAS PRESENT, MOM HAD YOU WRITING THANK-YOU NOTES TO EVERY AUNT IN THE STATE.",
 "The paper was barely off the boxes before Mom showed up with a stack of note cards and a pen. You could look at your new things all you wanted. You could not touch them. Dear Aunt Helen, thank you for the socks. Dear Aunt Marge, thank you for the other socks. Every note had to be in your best handwriting and every one had to say something nice and true. It took all morning. And every aunt on the list wrote back to tell your mother what a fine young person you were.",
 "My mother kept a list taped inside the kitchen cabinet of who gave what, so you couldn't get out of a single one. I still write thank-you notes. My hand starts aching at the third one, just like it did then.\n\n#WhispersOfYesterday #OldSchool #ChildhoodMemories #RememberWhen #GrowingUpIn60s #BackInTheDay",
 t1("on Christmas morning in a cozy 1960s living room, a decorated tree with big colored bulbs and tinsel, torn wrapping paper everywhere. A boy and a girl of about eight and ten sit at a small table in pajamas and robes writing thank-you notes with pencils and long faces, while their unopened toys, a toy fire truck and a doll, sit just out of reach beside them. Their mother in a robe stands over them holding a stack of envelopes and a fond, firm smile.",
 "BEFORE YOU PLAYED WITH ONE CHRISTMAS PRESENT, MOM HAD YOU WRITING THANK-YOU NOTES TO EVERY AUNT IN THE STATE.")),
]
stories = [
img(1, "T1 illustrated scene", "Cars and driving culture (Dad's arm)",
 "EVERY TIME DAD HIT THE BRAKES, HIS RIGHT ARM SHOT ACROSS THE FRONT SEAT. THAT WAS OUR SEAT BELT.", "", "",
 t1("inside a 1960s car with a wide bench front seat, on a small-town street. The father driving in a short-sleeved shirt brakes hard at a stop sign and throws his right arm straight across the chest of a surprised boy of about eight sitting beside him, a paper sack of groceries tipping over on the seat, the boy's eyes wide, the father calm and steady.",
 "EVERY TIME DAD HIT THE BRAKES, HIS RIGHT ARM SHOT ACROSS THE FRONT SEAT. THAT WAS OUR SEAT BELT."), story=True),
img(2, "T2 vintage photo", "Real-photo nostalgia (chrome kitchen table)",
 "THE CHROME KITCHEN TABLE WAS WHERE THE HOMEWORK GOT DONE, THE BILLS GOT PAID, AND EVERY BIG DECISION GOT MADE.", "", "",
 t2("a 1950s kitchen in soft morning light: a chrome-legged dinette table with a red-and-white speckled laminate top and four matching vinyl chairs, a sugar bowl, a salt and pepper set, a pencil and an open school workbook with blank pages, a stack of plain envelopes, a percolator on the stove behind it, checked curtains at the window.",
 "THE CHROME KITCHEN TABLE WAS WHERE THE HOMEWORK GOT DONE, THE BILLS GOT PAID, AND EVERY BIG DECISION GOT MADE."), ai=True, story=True),
img(3, "T3 retro poster", "Childhood rules and rituals (bookmobile)",
 "THE BOOKMOBILE / EVERY OTHER TUESDAY THE LIBRARY ROLLED RIGHT UP TO THE END OF OUR STREET", "", "",
 t3("a rounded 1960s bookmobile van in two-tone cream and teal parked at a neighborhood corner, its side door open to shelves of colorful books, a friendly librarian on the step handing books to a line of excited children of about six to ten clutching library cards, houses and trees behind them. The van's side has no lettering.",
 "THE BOOKMOBILE", "EVERY OTHER TUESDAY THE LIBRARY ROLLED RIGHT UP TO THE END OF OUR STREET"), story=True),
]
b = {"title": "Whispers Of Yesterday Review · Oct 17", "subtitle": "", "bucket": "Whispers Of Yesterday",
     "story_bucket": "Whispers Of Yesterday Stories", "posts": feed, "stories": stories}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "batch.json")
json.dump(b, open(out, "w"), indent=1, ensure_ascii=False)
print(len(feed), len(stories))
