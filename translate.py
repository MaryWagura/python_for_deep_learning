from fpdf import FPDF
import textwrap


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, self.title_text, 0, 1, 'C')
        self.ln(5)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 6, body)
        self.ln()

    def chapter_body_bold(self, body):
        self.set_font('Arial', 'B', 11)
        self.multi_cell(0, 6, body)
        self.ln()

    def bullet_point(self, text):
        self.set_font('Arial', '', 11)
        self.cell(5)  # Indent
        self.multi_cell(0, 6, f"{chr(149)} {text}")
        self.ln(1)


def create_policy_pdf():
    pdf = PDF()
    pdf.title_text = "THE RED-BLACK WAY (Policy & Values)"
    pdf.add_page()

    # Page 1 Intro
    pdf.chapter_title("FOREWORD")
    pdf.chapter_body(
        "What you hold in your hand is a presentation of our association's core values, policy, and goals. The purpose is to give you insight into what we should all work towards, whether you are a practitioner, parent, or simply interested in our operations. 'The Red-Black Way' informs and inspires you about what our organization wants and stands for. This compendium is developed together with leaders, practitioners, and parents to create a stable foundation to stand on.")
    pdf.chapter_body(
        "Taekwondo with us is practiced from exercise level to elite level for both adults and children. We adhere to the association's values and policy. We warmly welcome you to our community and hope you will enjoy your time with us.")

    pdf.chapter_title("1. DEFINITION OF THE RED-BLACK WAY")
    pdf.chapter_body(
        "Our association's colors are red and black, and in our association, we believe that all people can make choices wherever they are in life.")
    pdf.chapter_body(
        "Taekwondo means 'The Way of the Foot and the Hand', and we believe that by learning how our feet, hands, and bodies function, we can better understand ourselves and other people. Therefore, we believe that our training makes us better equipped to choose paths that lead to the good intentions we express, among other things, in the Student's Oath.")
    pdf.chapter_body(
        "Since Taekwondo training is about understanding myself and my fellow human beings, it becomes natural to enter the Dojang [Training Hall] with a listening mind and a humble attitude. Taekwondo differs from many other sports precisely because we are aware that our training not only affects our physical ability but our whole being and our choices in life.")

    # Values
    pdf.chapter_title("CORE VALUES")
    pdf.chapter_body_bold("Values:")
    pdf.bullet_point("Everyone is different but of equal worth—regardless of characteristics or performance.")
    pdf.bullet_point("Everyone has the right to develop at their own pace.")
    pdf.bullet_point(
        "Consideration and respect are a matter of course. (Treat others as you yourself want to be treated).")
    pdf.bullet_point("We distance ourselves from all forms of harassment and coercive violence.")
    pdf.bullet_point("Sportsmanship = To be honest, fair, and a role model in all situations.")
    pdf.bullet_point("Within the limits of the rules, one does everything to win, but can also lose with honor intact.")

    pdf.add_page()
    pdf.chapter_title("2. POLICY FOR LEADERS IN KUMGANG")
    pdf.chapter_body(
        "By 'leader' we mean instructor, coach, board member, and others who have taken responsibility for members at events.")
    pdf.chapter_body_bold("Leaders in Kumgang shall:")
    pdf.bullet_point("Live up to and be well versed in the association's values and policy.")
    pdf.bullet_point(
        "Be a good example in their leadership based on the association's values inside and outside the Dojang [Training Hall].")
    pdf.bullet_point("Not abuse their position of power.")
    pdf.bullet_point("Create conditions for community.")
    pdf.bullet_point("Look to every individual's development before results.")
    pdf.bullet_point("Make everyone in the group visible.")
    pdf.bullet_point("Act professionally and be engaged.")
    pdf.bullet_point("Be willing to educate themselves and stay updated.")
    pdf.bullet_point("Reflect on their role as a leader.")
    pdf.bullet_point("Be a good representative for the club.")

    pdf.chapter_title("3. POLICY FOR PRACTITIONERS IN KUMGANG")
    pdf.chapter_body_bold("Practitioners in Kumgang shall:")
    pdf.bullet_point("Be well versed in the association's core values and policy.")
    pdf.bullet_point("Not abuse their techniques and skills; understand the right of self-defense.")
    pdf.bullet_point("Show consideration and respect towards leaders and other members.")
    pdf.bullet_point("Show the way for lower grades.")
    pdf.bullet_point("Show respect for higher grades and their knowledge.")
    pdf.bullet_point("Know the Student's Oath.")
    pdf.bullet_point("Pay their membership and training fees.")
    pdf.bullet_point("Wear a whole and clean Dobok [Uniform] to Taekwondo training.")
    pdf.bullet_point("On fight and morning training, wear a Dobok [Uniform] or club clothes.")

    pdf.chapter_body_bold("THE STUDENT'S OATH")
    pdf.bullet_point("I shall observe the rules of Taekwondo.")
    pdf.bullet_point("I shall respect the instructor and senior students.")
    pdf.bullet_point("I shall never misuse Taekwondo.")
    pdf.bullet_point("I shall be a champion of freedom and justice.")
    pdf.bullet_point("I shall build a more peaceful world.")

    pdf.add_page()
    pdf.chapter_title("4. POLICY FOR PARENTS & RELATIVES")
    pdf.chapter_body(
        "Kumgang is grateful for your voluntary effort which is needed to run the operations towards the association's goals and guidelines.")
    pdf.chapter_body_bold("Parents and relatives in Kumgang shall:")
    pdf.bullet_point("In all situations be a role model for the children.")
    pdf.bullet_point("Be versed in the association's values and policy.")
    pdf.bullet_point("Take responsibility and actively seek information concerning your child and the association.")
    pdf.bullet_point("Respect coaches, trainings, and Taekwondo's rules.")
    pdf.bullet_point("Know the rules that apply in the association's premises.")
    pdf.bullet_point("Encourage your child to training and personal development.")
    pdf.bullet_point("Not interrupt or talk to the child during training.")
    pdf.bullet_point("Encourage and cheer on all members during competition.")

    pdf.chapter_body_bold("SIMPLE DOJANG RULES FOR PARENTS & RELATIVES")
    pdf.bullet_point(
        "No parents or relatives in the Dojang [Training Hall] during training (exception by agreement with coach).")
    pdf.bullet_point("Bow when entering the Dojang [Training Hall].")
    pdf.bullet_point("Show respect for our Dojang, coaches, and everyone training.")

    pdf.chapter_title("5. TAEKWONDO FOR CHILDREN")
    pdf.chapter_body(
        "The overall goal for all children's groups is to inspire a lifelong interest in Taekwondo and exercise. Teaching children to take others and coaches into consideration, cooperate in groups, and the importance of fair play are important objectives.")
    pdf.chapter_body(
        "Since we practice martial arts, it is important for us to teach children how and when one may potentially use Taekwondo as self-defense. Taekwondo is above all fun and really good exercise.")

    pdf.chapter_body_bold("4-6 Years: 'This is what we want'")
    pdf.bullet_point("Gross motor training.")
    pdf.bullet_point("Try the basics of Taekwondo in a playful way.")
    pdf.bullet_point("Practice discipline and concentration.")
    pdf.chapter_body_bold("We reach this through:")
    pdf.bullet_point("Exercises involving technique, balance, jumping, throwing, catching, etc.")
    pdf.bullet_point("Basic positions, footwork, and the first kick and hand techniques.")
    pdf.bullet_point("Being quiet, listening to the coach, and lining up. Start talking about the Student's Oath.")

    pdf.chapter_body_bold("7-9 Years: 'This is what we want'")
    pdf.bullet_point("Motor training.")
    pdf.bullet_point("Learn the basics of Taekwondo in a playful way.")
    pdf.bullet_point("Learn discipline and concentration.")
    pdf.bullet_point("Stimulate interest and understanding for matches in Taekwondo's different branches.")
    pdf.chapter_body_bold("We reach this through:")
    pdf.bullet_point("Coordination exercises.")
    pdf.bullet_point("A lot of technique in varied forms. Accustom children to stretching and physical training.")
    pdf.bullet_point("Training with fixed and clear rules. Concentration during exercises. Teach the Student's Oath.")
    pdf.bullet_point("Match-like training in a fun and challenging way.")

    pdf.chapter_body_bold("10-13 Years: 'This is what we want'")
    pdf.bullet_point("Motor training.")
    pdf.bullet_point("Learn basics playfully; learn discipline and concentration.")
    pdf.bullet_point("Stimulate interest for matches.")
    pdf.bullet_point("Create understanding for how important diet, sleep, and training are.")
    pdf.chapter_body_bold("We reach this through:")
    pdf.bullet_point("Coordination exercises.")
    pdf.bullet_point("Varied technique, stretching, physical training.")
    pdf.bullet_point("Fixed rules, concentration, Student's Oath.")
    pdf.bullet_point("Match-like training.")
    pdf.bullet_point("Talk about the connection between diet, sleep, and training for good health.")

    pdf.add_page()
    pdf.chapter_title("6. TAEKWONDO FOR YOUTH (13-17 Years)")
    pdf.chapter_body(
        "Overall goal is to inspire a lifelong interest. Consideration, humility, honesty, and friendship are emphasized. We stimulate community through cooperation and self-confidence by accepting challenges. Since we practice martial arts, it is very important our youth learn the law regarding the right of self-defense. We want to make our youth participate and give them responsibility; our future leaders are among our youth.")
    pdf.chapter_body_bold("This is what we want:")
    pdf.bullet_point("Create conditions for personal development physically, mentally, and socially.")
    pdf.bullet_point("Give options for individual focus or serious investment.")
    pdf.bullet_point("Continue training regularly through puberty.")
    pdf.bullet_point("Create understanding for how thought affects feelings and behavior.")
    pdf.bullet_point("Create understanding for diet, sleep, and training.")
    pdf.chapter_body_bold("We reach this through:")
    pdf.bullet_point("Training containing strength, mobility, cardio, and coordination. Pepping, encouragement.")
    pdf.bullet_point("Time to get to know each other through cooperation exercises.")
    pdf.bullet_point("Look to the individual's needs, conditions, and interests.")
    pdf.bullet_point("Create awareness of why you train. Inspire own goal-setting.")
    pdf.bullet_point("Inform, discuss, offer lectures and education.")

    pdf.chapter_title("7. TAEKWONDO FOR ADULTS (18+)")
    pdf.chapter_body(
        "Overall goal: Lifelong interest. Values: Consideration, humility, honesty, friendship. It is very important adults learn the law of self-defense.")

    pdf.chapter_body_bold("18-29 Years & 30+ Years")
    pdf.bullet_point("Create conditions for personal development, physical and mental.")
    pdf.bullet_point("Give options for individualized/varied training or serious investment.")
    pdf.bullet_point("Greater understanding of training's impact.")
    pdf.bullet_point("Understanding how thought affects feelings/behavior.")
    pdf.bullet_point("Importance of diet/sleep/health.")

    pdf.chapter_title("8. TAEKWONDO COMPETITION")
    pdf.chapter_body(
        "Competition is for those interested from 7 years and up. It serves as education for rules, tactics, sportsmanship, etc. Kumgang has specific trainings for Poomsae [Patterns] and Kyorugi [Sparring/Fight]. Competition is voluntary.")
    pdf.chapter_body_bold("Goals:")
    pdf.bullet_point("Understand rules and tactics.")
    pdf.bullet_point("Sportsmanship.")
    pdf.bullet_point("Create a stimulating environment.")
    pdf.bullet_point("Give conditions to become an elite practitioner.")
    pdf.chapter_body_bold("We reach this through:")
    pdf.bullet_point("Review of rules/tactics (theoretical and practical).")
    pdf.bullet_point("Regular conversations about sportsmanship.")
    pdf.bullet_point("Safe atmosphere, support, 'Development before results'.")

    pdf.chapter_title("9. TAEKWONDO ELITE")
    pdf.chapter_body(
        "Refers to international or national top-level activity. If a practitioner wants to take a step further in their career, the association shall create these conditions.")
    pdf.chapter_body_bold("Goals:")
    pdf.bullet_point("Get practitioners from Swedish elite to World elite.")
    pdf.bullet_point("Championship medals.")
    pdf.bullet_point("Create best possible conditions for elite investment.")
    pdf.bullet_point("Network of physiotherapists, naprapaths, mental coaches, doctors, etc.")

    pdf.chapter_title("10. DRUG POLICY & INFO")
    pdf.chapter_body(
        "We support a sound, healthy, and drug-free lifestyle. We strongly distance ourselves from all drugs and doping.")
    pdf.chapter_body("For more info: Visit www.kumgang.se")

    pdf.output("Kumgang_Policy_RedBlackWay_Translated.pdf")


def create_grading_pdf():
    pdf = PDF()
    pdf.title_text = "KUMGANG GRADING COMPENDIUM (Rules & Requirements)"
    pdf.add_page()

    # Introduction
    pdf.chapter_title("GRADING CONDITIONS (Version 3.0, 2017)")
    pdf.chapter_body(
        "You must be prepared and know your techniques, Kyorugi [Sparring], Poomsae [Patterns], Hosinsul [Self-defense], and theory. You must also know everything from previous grades.")
    pdf.chapter_body(
        "The responsible coach decides if the student is ready for grading. Membership and training fees must be paid.")

    pdf.chapter_body_bold("Training Attendance")
    pdf.chapter_body(
        "70% attendance is required to grade. Exceptions can be made for good reasons or if the practitioner trained the previous term without grading.")
    pdf.chapter_body(
        "Training time between 5 and 4 Kup is usually 2 terms. Between 1 Kup and 1 Dan is usually 2 terms.")

    pdf.chapter_body_bold("Dan - Black Belt")
    pdf.chapter_body("90% attendance required. The head instructor may assign extra training.")

    pdf.chapter_title("INTRODUCTION TO TAEKWONDO")
    pdf.chapter_body("Taekwondo means 'The Way of the Foot and Hand'.")
    pdf.bullet_point("Tae: Foot")
    pdf.bullet_point("Kwon: Hand")
    pdf.bullet_point("Do: The Art, the development, and the mental strength's way.")
    pdf.chapter_body("Training improves concentration, discipline, respect, humility, and strengthens self-confidence.")

    pdf.chapter_body_bold("THE STUDENT'S OATH")
    pdf.bullet_point("I shall observe Taekwondo's rules.")
    pdf.bullet_point("I shall respect instructors and senior students.")
    pdf.bullet_point("I shall never misuse Taekwondo.")
    pdf.bullet_point("I shall be a champion of freedom and justice.")
    pdf.bullet_point("I shall help to create a more peaceful world.")

    # 9 Kup
    pdf.add_page()
    pdf.chapter_title("9 KUP - YELLOW BELT")
    pdf.chapter_body_bold("Poomsae [Patterns]")
    pdf.bullet_point("6 first movements in Taegeuk Il Jang.")

    pdf.chapter_body_bold("Seogi [Stances]")
    pdf.bullet_point("Kyurogi-seogi [Fighting stance]")
    pdf.bullet_point("Juchum-seogi [Riding stance]")
    pdf.bullet_point("Ap-seogi [Short front stance]")
    pdf.bullet_point("Ap-kubi-seogi [Long front stance]")

    pdf.chapter_body_bold("Makki [Blocks]")
    pdf.bullet_point("Arae-makki [Low block]")

    pdf.chapter_body_bold("Jireugi [Punches]")
    pdf.bullet_point("Arae-jireugi [Low punch]")
    pdf.bullet_point("Momtong-jireugi [Middle punch]")

    pdf.chapter_body_bold("Chagi [Kicks]")
    pdf.bullet_point("Ap-chaolligi [Rising/Stretch kick]")
    pdf.bullet_point("An-chagi [Inward kick]")
    pdf.bullet_point("Bakkat-chagi [Outward kick]")
    pdf.bullet_point("Ap-chagi [Front kick with ball of foot]")
    pdf.bullet_point("Ap-mireo-chagi [Front push kick]")
    pdf.bullet_point("Pich-chagi [Roundhouse kick to stomach]")

    pdf.chapter_body_bold("Kyurogi [Olympic Sparring]")
    pdf.bullet_point("Footwork: Skip, Shift, Step.")
    pdf.bullet_point("Hand techniques: Guard, Low block, Punch.")
    pdf.bullet_point("Sparring: 2 rounds light sparring (2 x 1.5 min).")

    pdf.chapter_body_bold("Hosinsul [Self-Defense]")
    pdf.bullet_point("Basic self-defense rights.")
    pdf.bullet_point("Handling threatening situations (Attacker approaches/pushes).")

    pdf.chapter_body_bold("Teori [Theory]")
    pdf.bullet_point(
        "Meanings: Charyot (Attention), Kyongle (Bow), Jumbi (Ready), Sijak (Start), Kalyjo (Break), Keuman (Stop), Tirodora (Turn around).")
    pdf.bullet_point("Titles: Chokyonim (Assistant 1 Kup), Kyosanim (Coach 1-3 Dan), Sabomnim (Instructor 4-6 Dan).")

    # 8 Kup
    pdf.add_page()
    pdf.chapter_title("8 KUP - GREEN BELT")
    pdf.chapter_body_bold("Poomsae")
    pdf.bullet_point("Taegeuk Il Jang (18 movements). Meaning: 'Keon' (Heaven/Light).")

    pdf.chapter_body_bold("Seogi")
    pdf.bullet_point("Moa-seogi [Feet together]")
    pdf.bullet_point("Naranhi-seogi [Parallel stance]")

    pdf.chapter_body_bold("Makki")
    pdf.bullet_point("Momtong an-makki [Inner middle block]")
    pdf.bullet_point("Olgul-makki [High block]")

    pdf.chapter_body_bold("Jireugi")
    pdf.bullet_point("Olgul-jireugi [High punch]")

    pdf.chapter_body_bold("Chagi")
    pdf.bullet_point("Ap-chagi [Front kick]")
    pdf.bullet_point("Yop-chagi [Side kick]")
    pdf.bullet_point("Yop-mireo-chagi [Side push kick]")
    pdf.bullet_point("Naeryo-chagi [Axe kick]")

    pdf.chapter_body_bold("Hosinsul")
    pdf.bullet_point("Defense against 'Haymaker' punch (Rallarsving).")
    pdf.bullet_point("Defense against 'Haymaker' kick (Rallarspark).")
    pdf.bullet_point("Wrist holds.")

    pdf.chapter_body_bold("Kyokpa [Breaking]")
    pdf.bullet_point("Ap-chagi [Front kick]")

    # 7 Kup
    pdf.add_page()
    pdf.chapter_title("7 KUP - GREEN BELT W/ BLUE STRIPE")
    pdf.chapter_body_bold("Poomsae")
    pdf.bullet_point("Taegeuk I Jang. Meaning: 'Tae' (Joy/Inner Strength).")

    pdf.chapter_body_bold("Chagi")
    pdf.bullet_point("Dollyo-chagi [Roundhouse kick high]")
    pdf.bullet_point("360 pich-chagi [Tornado kick]")
    pdf.bullet_point("Dwi-chagi [Back kick]")

    pdf.chapter_body_bold("Hosinsul")
    pdf.bullet_point("Clothes grab front/back.")

    pdf.chapter_body_bold("Kyokpa")
    pdf.bullet_point("Momtong-jireugi [Middle punch]")

    pdf.chapter_title("WHAT IS POOMSAE?")
    pdf.chapter_body("Poomsae is an imaginary fight where one is attacked from all directions. Important points:")
    pdf.bullet_point("1. Must end at the same spot it started.")
    pdf.bullet_point("2. Muscles tensed at the moment of impact.")
    pdf.bullet_point("3. Performed in a specific rhythm.")
    pdf.bullet_point("4. Understand all movements.")
    pdf.bullet_point("5. Realistic execution.")
    pdf.bullet_point("6. 'Sison' - Look before performing a technique.")

    # 6 Kup
    pdf.add_page()
    pdf.chapter_title("6 KUP - BLUE BELT")
    pdf.chapter_body_bold("Poomsae")
    pdf.bullet_point("Taegeuk Sam Jang. Meaning: 'Ri' (Fire/Sun).")

    pdf.chapter_body_bold("Seogi")
    pdf.bullet_point("Dwitkubi-seogi [Back stance]")

    pdf.chapter_body_bold("Makki")
    pdf.bullet_point("Hansonnal bakkat-makki [Single knife-hand outward block]")

    pdf.chapter_body_bold("Chigi [Strikes]")
    pdf.bullet_point("Sonnal olgul an-chigi [Knife-hand high inward strike]")

    pdf.chapter_body_bold("Chagi")
    pdf.bullet_point("Huryo-chagi [Hook kick]")
    pdf.bullet_point("Ban pandae-dollyo-chagi [Reverse roundhouse/Spinning hook 180]")

    pdf.chapter_body_bold("Hosinsul")
    pdf.bullet_point("Body hold from front (under/over arms).")

    pdf.chapter_body_bold("Kyokpa")
    pdf.bullet_point("Dollyo-chagi [Roundhouse kick]")

    # 5 Kup
    pdf.add_page()
    pdf.chapter_title("5 KUP - BLUE BELT W/ RED STRIPE")
    pdf.chapter_body_bold("Poomsae")
    pdf.bullet_point("Taegeuk Sam Jang (Refined).")

    pdf.chapter_body_bold("Chagi")
    pdf.bullet_point("Twio ap-chagi [Jumping front kick]")
    pdf.bullet_point("Twio dollyo-chagi [Jumping roundhouse kick]")
    pdf.bullet_point("Pandae-dollyo-chagi [Spinning hook kick 360]")

    pdf.chapter_body_bold("Hosinsul")
    pdf.bullet_point("Body hold from back. Choke hold from back.")

    pdf.chapter_title("THEORY: PALGWE - THE 8 TRIGRAMS")
    pdf.chapter_body(
        "Palgwe symbolizes the whole and basic concepts of the universe. The patterns (Taegeuk) are based on these.")
    pdf.bullet_point("Keon (Heaven) - Taegeuk 1")
    pdf.bullet_point("Tae (Joy) - Taegeuk 2")
    pdf.bullet_point("Ri (Fire) - Taegeuk 3")
    pdf.bullet_point("Jin (Thunder) - Taegeuk 4")
    pdf.bullet_point("Seon (Wind) - Taegeuk 5")
    pdf.bullet_point("Gam (Water) - Taegeuk 6")
    pdf.bullet_point("Gan (Mountain) - Taegeuk 7")
    pdf.bullet_point("Kon (Earth) - Taegeuk 8")

    # 4 Kup
    pdf.add_page()
    pdf.chapter_title("4 KUP - RED BELT")
    pdf.chapter_body_bold("Poomsae")
    pdf.bullet_point("Taegeuk Sah Jang. Meaning: 'Jin' (Thunder).")

    pdf.chapter_body_bold("Makki")
    pdf.bullet_point("Sonnal momtong-makki [Knife-hand middle block]")

    pdf.chapter_body_bold("Chigi")
    pdf.bullet_point("Jebi-poom mok-chigi [Swallow-form neck strike]")

    pdf.chapter_body_bold("Tzireugi [Thrust/Poke]")
    pdf.bullet_point("Pyonsonkeut sewo-tzireugi [Fingertip thrust, vertical]")

    pdf.chapter_body_bold("Chagi")
    pdf.bullet_point("Twio yop-chagi [Jumping side kick]")
    pdf.bullet_point("Twio pandae-dollyo-chagi [Jumping spinning hook]")

    pdf.chapter_body_bold("Hosinsul")
    pdf.bullet_point("Lapel grab, choke from back, push kick defense.")

    # 3 Kup
    pdf.add_page()
    pdf.chapter_title("3 KUP - RED BELT W/ BLACK STRIPE")
    pdf.chapter_body_bold("Poomsae")
    pdf.bullet_point("Taegeuk Oh Jang. Meaning: 'Seon' (Wind).")

    pdf.chapter_body_bold("Seogi")
    pdf.bullet_point("Wen-seogi [Left stance], Oreun-seogi [Right stance], Koa-seogi [Cross stance].")

    pdf.chapter_body_bold("Chigi")
    pdf.bullet_point("Deungjumeok ap-chigi [Backfist front strike]")
    pdf.bullet_point("Palkup momtong-chigi [Elbow strike]")
    pdf.bullet_point("Me-jumeok naeryo-chigi [Hammer-fist downward strike]")

    pdf.chapter_body_bold("Hosinsul")
    pdf.bullet_point("Ground defense against standing opponent.")

    # 2 Kup
    pdf.add_page()
    pdf.chapter_title("2 KUP - RED BELT W/ 2 BLACK STRIPES")
    pdf.chapter_body_bold("Poomsae")
    pdf.bullet_point("Taegeuk Yook Jang. Meaning: 'Gam' (Water).")

    pdf.chapter_body_bold("Makki")
    pdf.bullet_point("Arae hechyo-makki [Low scattering block]")
    pdf.bullet_point("Batangson an-makki [Palm inward block]")

    pdf.chapter_body_bold("Chagi")
    pdf.bullet_point("360 Naeryo-chagi [Tornado axe kick]")

    pdf.chapter_body_bold("Hosinsul")
    pdf.bullet_point("Apply grips 1-4 to situations.")

    # 1 Kup
    pdf.add_page()
    pdf.chapter_title("1 KUP - RED BELT W/ 3 BLACK STRIPES")
    pdf.chapter_body_bold("Poomsae")
    pdf.bullet_point("Taegeuk Chill Jang. Meaning: 'Gan' (Mountain).")

    pdf.chapter_body_bold("Seogi")
    pdf.bullet_point("Beom-seogi [Tiger stance]")

    pdf.chapter_body_bold("Makki")
    pdf.bullet_point("Kawi-makki [Scissor block]")

    pdf.chapter_body_bold("Chagi")
    pdf.bullet_point("Combinations without putting foot down.")

    pdf.chapter_body_bold("Hosinsul")
    pdf.bullet_point("Defense against 2 opponents.")

    # 1 Dan Prep (Page 19)
    pdf.add_page()
    pdf.chapter_title("TO 1 DAN (BLACK BELT)")
    pdf.chapter_body_bold("Poomsae")
    pdf.bullet_point("Taegeuk Pal Jang. Meaning: 'Kon' (Earth).")

    pdf.chapter_body_bold("Makki")
    pdf.bullet_point("Wesanteul-makki [Single mountain block]")

    pdf.chapter_body_bold("Chigi")
    pdf.bullet_point("Dangkyo teok-chigi [Pulling chin strike]")

    pdf.chapter_body_bold("Hosinsul")
    pdf.bullet_point("Defense against knife, sticks, and multiple opponents.")

    # Competition Rules
    pdf.add_page()
    pdf.chapter_title("COMPETITION RULES - KYORUGI (FIGHT)")
    pdf.chapter_body("Area: 8x8 meters. Goal: Score points on allowed areas.")
    pdf.chapter_body_bold("Points:")
    pdf.bullet_point("1 point: Punch to vest.")
    pdf.bullet_point("2 points: Kick to vest.")
    pdf.bullet_point("3 points: Head kick / Rotating kick to vest.")
    pdf.bullet_point("4 points: Rotating kick to head.")
    pdf.chapter_body_bold("Minus Points (Gam-jeom):")
    pdf.bullet_point("Falling, crossing boundary, grabbing, attacking below belt, hitting head with hand.")

    pdf.chapter_title("THEORY: SELF-DEFENSE LAW (NÖDVÄRNSRÄTT)")
    pdf.chapter_body("Based on Swedish Penal Code (Brottsbalken 24 § 1).")
    pdf.chapter_body("Right to self-defense exists against:")
    pdf.bullet_point("1. A begun or imminent criminal attack on person or property.")
    pdf.bullet_point("2. Anyone preventing the repossession of stolen property.")
    pdf.bullet_point("3. Unlawful intrusion into room/house.")
    pdf.chapter_body("The defense must not be 'manifestly unjustifiable' considering the nature of the attack.")

    pdf.output("Kumgang_Grading_Rules_Translated.pdf")


if __name__ == "__main__":
    create_policy_pdf()
    create_grading_pdf()