#Hi! Welcome to the code- this game was made by programmer French Toast,
#And is written in Python!
#You'll need a console that can run python to play this game right!
#Please enjoy! (Completed February 16th, 2021)
#Update (Feb 17 2021): I made one (1) mistake in an elif, oops. Fixed now! "Listen" should now work.

#The game intro is here! This is just the entry writing, there will be a lot of this in the code.
print("""You sigh, putting the last of the clutter away. You'd just finished cleaning the house, by now, 
and it was somewhat late- Barely past sunset.

Now that you're finished, of course, you can CHOOSE to do something. 
There are GAMES you haven't played yet, a handful of BOOKS that haven't been read. 
Maybe you just want to SIT and do nothing, or listen to MUSIC.""")

FirstList = ["GAMES", "BOOKS", "SIT", "MUSIC"]
OneOption = False
activity = str.upper(input("what will you do?\n"))

#This while loop is to teach the user they have to input specifically the capitalized words in the story
while OneOption == False:

     
     if activity in FirstList:
            OneOption = True
            print(f"""[{activity}]
            
You decide what to do with a smile! Finally you'll be able to relax...
            """)

    #Choose is a somewhat different written result, is all.
     elif activity == "CHOOSE":
         
         OneOption = True
         Choose = True
         print("""[CHOOSE]

You exercise your freedom.
""")

     else:
            activity = str.upper(input("That is not an option. Please CHOOSE again.\n " ))

print("""
It's nice to have a CHOICE, but sometimes things happen without any influence from you. Just a moment later, 
in fact, there's a KNOCK at the door, interrupting you entierly. You weren't expecting anyone, and it's a bit late for any kind of 
door to door salesman...
""")

#User input variables are designated as such: They will start with the choice path (Choose, Sense, etc), 
#step number (1, 2, etc), with an additional letter (A, B, etc) in case of repeats.


First0 = str.upper(input("Will you OPEN the door, or IGNORE the knock?\n"))

#While loops from here on out will be to prevent the player from having to play the whole game over again if,
#for example, they misspell a word or select an invalid option.
#Variables will be "Flag" and a number based on the loop. There are going to be a lot of these, they'll be marked for each choice.

#Game course: 0 - tutorial. 1 - First knock. 2 - Second knock. 3 - Break-in. 4 - Neighborpass. Other timings irrelevant 
Flag1 = False

while Flag1 == False:

     if First0 == "OPEN":
          Flag1 = True
          print("""[Open]

You open the door, and smile at the sight. Oh! It's a friend- 
they've got a plate of some kind of baked good, and gave a 
happy hello right when you answered.

You invite them in for a while and spend some time together- it's absolutely 
been too long, and you're happy to be in their company again.

Eventually you part ways, and try one of the treats they made.... 
it's delicious! And a wonderful way to end your night.

[END; EMPTY]""")

     elif First0 == "IGNORE":
          Flag1 = True

          print("""[IGNORE]

You ignore the knocking and continue with your activity. 
The knocking gets more aggressive, however, enough so to rattle the door in its frame.\n""")
          Flag2 = False
          Ignore1 = str.upper(input("Will you continue to IGNORE it? or will you actually ANSWER?\n"))

          while Flag2 == False:

               if Ignore1 == "ANSWER":
                    Flag2 = True

                    print("""[ANSWER]

You sigh, and go to answer the door. It's a stranger you don't 
recognize, and they're standing very close to the door. A gun is visible on their person, 
in a way discreet enough not to be seen from the street, but a clear threat to you. "Where is it.\"\n""")
                    Flag3 = False
                    Answer2 = str.upper(input("Are you going to tell the TRUTH, or a LIE?\n"))

                    while Flag3 == False:

                         if Answer2 == "TRUTH":
                              Flag3 = True
                              print("""[TRUTH]

"I don't know what you're talking about, there's nothing here."

"Let me see for myself."

The stranger forces their way in with or without your permission, 
looking through your house as you lag somewhat behind them. They don't
 search deeply, but they open almost door, looking for something...

After the last few doors leave them standing in annoyed silence, you speak up. 
"Like I said- there's nothing here. It's just a normal house."

They glare back at you for a moment, before sighing in annoyance, 
and walking out towards the door to leave.

"Not now. But when I come back later, there will be."

And with that, they're gone... you scoff, and lock the door. Weirdo.

[END; BLIND]""")

                         elif Answer2 == "LIE":
                              Flag3 = True
                              print("""[LIE]

"I don't know what you're talking about, there's nothing here."

"Let me see for myself."

The stranger tries to force their way in but you block them, 
and they instead glare down at you. "Move."

"I promise, there's nothing interesting here- please just go."

They look you in the eyes for a long moment. The desperation in your gaze. 
The slight edge to your voice... and they sigh, looking away.

"When I come back, it'll be different. Be ready for me next time."

You look away guiltily as they leave. You can't choose differently. 
Not knowing what it could lead to.

[END; GUILTY]""")

                         else:
                              Answer2 = str.upper(input("Try again.\n"))

               elif Ignore1 == "IGNORE":
                    Flag2 = True

                    print("""[IGNORE] 

You continue ignoring it. Whoever was knocking before has successfully broken in 
by now, and they glance around- seeing you just casually there throws them off 
a bit, though. They're surprised.\n""")
                    Flag3 = False
                    Ignore2 = str.upper(input("Are you going to keep on IGNORING them? Or strike up a FRIENDLY conversation?\n"))

                    while Flag3 == False:

                         if Ignore2 == "FRIENDLY":
                              Flag3 = True

                              print("""[FRIENDLY]

"Welcome!"

They look at you in confusion at your greeting, and the light smile you offer them. 
"That was a rude entrance, but I can't blame you- I've no idea where everyone's gone, 
but I never answer the door..."

"What do you mean-?\"\n""")
                              Flag4 = False
                              Friendly3 = str.upper(input("What do you mean? Are you just that RICH? Or are you POWERFUL?\n"))

                              while Flag4 == False:

                                   if Friendly3 == "RICH":
                                        Flag4 = True
                                        print("""[RICH]

"I mean, typically my attendant would answer, but they must be busy..." 

You shake your head in disappointment, and turn back to the stranger. 
"So, how much do you want?"

"How much?"

"Money, yes, how much? I don't need you rooting around for it, I can 
just pay you now." 

"I'm not here for money."

You raise your eyebrows at the stranger in curiosity. "Oh...? Then what 
are you here for..?"

"...There's something here. I'm trying to find it."

"Oh, that, unfortunately I can't show you myself."

The stranger tilts their head in confusion, and the silent question of why 
passes between the both of you. You decide to answer so they don't have to ask.

"If you want to be with it, you have to be willing to make choices... 
something I won't do. So you can't find it through me. Maybe if you try 
again another night..?"

The stranger shakes their head in puzzlement, before moving to leave. 
"Fine... I'll be back again later."

You wave goodbye and sigh in relief. Now you can finally relax!

[END; UNSUCCESSFUL]""")

                                   elif Friendly3 == "POWERFUL":
                                        Flag4 = True
                                        print("""[POWERFUL]

"Well, normally there are guards stationed throughout this area... Either you're 
the luckiest sneak thief ever, or the worst assassin that's ever been sent."

You watch them to gauge their reaction, but it doesn't reveal much. Not more than 
a sense of confusion, at least, and a guarded personality. "I'm not here for 
any kind of person, or to get involved in anything..."

"Oh, I don't doubt it. But by choosing me you've become involved... so, you have 
two options, don't you? You can leave now... and we can forget this little instance 
of trespassing... or you can leave later, and find yourself in even hotter water."

They hesitate a few moments longer before leaving, and you nod in approval. Good... 
This does mean you'll have to increase security, though, and be sure tonights guards 
have learned their lesson.  What a disgraceful display, letting that stranger through...

[END; DISAPPOINTED]""")

                                   else:
                                        Friendly3 = str.upper(input("Try again.\n"))

                         elif Ignore2 == "IGNORING":
                              Flag3 = True

                              print("""[IGNORING]

You continue not paying attention to them...

They watch you for a few moments, before continuing into the house. Awkwardly, 
perhaps, but continuing with their own BUSINESS- whatever they'd come here to do...

""")
                              Flag4 = False
                              Ignoring3 = str.upper(input("...Eventually, they finish, and pause at the door to look back at you again. \nAre you still going to IGNORE them?\n"))

                              while Flag4 == False:

                                   if Ignoring3 == "BUSINESS":
                                        Flag4 = True
                                        print("""[BUSINESS]

"Going so soon?"

The stranger jumps as you speak, suddenly a lot more uncomfortable than they were 
when you were ignoring them. "Yes?"

"But you can't be done here, can you? That quickly?"

They shuffle nervously, glancing back at where they'd been. "What do you mean?"

"You didn't find it, did you..."

You stand up, and the stranger pulls their gun on you, watching you with 
rapt attention. Good. You deserve it.

"Well... it's alright. Come back again and we can work out a deal. I will help you find it."

"I- don't know what you're talking about-"

"Of course you do! I know. It's my business to, even."

You grin at them, and they lower their gun with trembling hands. Not because they're 
any less afraid, but because they've realized they don't want to shoot you. Especially 
faced with the potential consequences of it.

"...Run along now. You're busy tonight."

They leave much faster than they came.

[END; WATCHER]""")

                                   elif Ignoring3 == "IGNORE":
                                        Flag4 = True
                                        print("""[IGNORE]

They leave. You continue to sit there... nothing happened, but are you really fulfilled? 
Are you ok with them having been able to do whatever they wanted?

[END; DISAPPOINTING]""")

                                   else:
                                        Ignoring3 = str.upper(input("Try again.\n"))

                         else:
                              Ignore2 = str.upper(input("try again.\n"))


               else:
                    Ignore1 = str.upper(input("try again.\n"))

     elif First0 == "KNOCK":
          Flag1 = True
          print("""[KNOCK]

You walk to the door, and knock back.

There's a moment of quiet, and then you get another knock in return- 
and after that, it almost becomes a game. Knocking back and forth through the door...

They do leave after a while of this, though. You smile to yourself and leave 
it be after that. That was fun- maybe they'll be back again..?

[END; LIGHT]""")

     elif First0 == "CHOICE":
          Flag1 = True
          
          print("\n[CHOICE]\n\nYou decide to prepare, so you can CHOOSE again. \nYou walk to the kitchen for a moment, retrieving a knife that you keep in your hand.")
          Flag2 = False
          Choice1 = str.upper(input("\nThey knock again, hard enough to rattle the DOOR in it's frame. \nyou can OPEN it, IGNORE it... You could also try to HIDE.\n"))


          while Flag2 == False:

               if Choice1 == "DOOR":
                    Flag2 = True
                    print("""[DOOR]

You grin, and leave for a moment. You just have to grab something.

The stranger eventually forces their way in, and the both of you make eye contact. 
They're shocked. "wh. Wha-"

You hit them with a door and send them sprawling across the porch, winded. 
You toss the door out on top of them for good measure, before closing and re-locking 
the front door. Hah. That'll show em.

[END; JOKE]""")

               elif Choice1 == "OPEN":
                    Flag2 = True
                    print("""[OPEN]

You open the door, and see a glimpse of the strangers face before getting 
pushed to the ground, backwards into your house, leaving you winded. The door is 
closed behind the stranger as they step in, staring down at you.

"Knew you'd still be here- you have no idea how long I've been waiting for this."

You scramble backwards away from them, crying out in alarm- but, unfortunately, 
they just pull a gun and shoot you where you lay.

Maybe opening the door just then was not such a good idea.

[END; MURDERED]""")

               elif Choice1 == "IGNORE":
                    Flag2 = True

                    print("""[IGNORE]

You remain in the kitchen and wait. The stranger gets past your door, 
and you hear them walking around before seeing them from your place in 
the kitchen. And they see you, of course.\n""")
                    Flag3 = False
                    Ignore2 = str.upper(input("....there's a moment of silence stretching between you. \nYou could GREET them and break the silence, or just... STARE, if you want to. It's your CHOICE.\n"))

                    while Flag3 == False:

                         if Ignore2 == "GREET":
                              Flag3 = True
                              print("""[GREET]

"Heya."

You offer the stranger a wave, and they glance between your face and 
your hand, baffled. "What..?"

"Did you need something?"

They look at you for a moment, before gesturing behind themselves, pointing 
at where the door would be. "You. Why didn't you answer the door?"

You shrug. "Why did you break in when I didn't?"

They open their mouth to reply, then close it, unprepared to answer. 
There's another brief moment of silence between you.

"...Did you want some water, or..?"

"Uh.... no, that... that's ok, I'll just... I'll just go, now..."

You wave goodbye and they do the same, leaving much more awkwardly than they came.

...Well, that was nice..?

[END; CONFUSED]""")

                         elif Ignore2 == "STARE":
                              Flag3 = True
                              print("""[STARE]

You look directly at them and wait. The moment stretches for a long time, until 
eventually, the stranger slowly backs out of the room. Once they're out of sight, 
you continue about your own business, shrugging off whatever else you hear as the 
night continues. You just... don't really care, huh?

[END; APATHETIC]""")

                         elif Ignore2 == "CHOICE":
                              Flag3 = True

                              print("""[CHOICE]

You make a decision.

"Are you here to see it? Or were you here for me?" 

Your question leaves the stranger stunned for a moment, but they collect themselves. 
"What are you..? What do you mean?\"\n""")
                              Flag4 = False
                              Choice3A = str.upper(input("Are they here for YOU, or for IT?\n"))

                              while Flag4 == False:

                                   if Choice3A == "YOU":
                                        Flag4 = True

                                        print("""[YOU]

You leave the knife on the counter as you move. The stranger pulls a gun on you, 
but you raise your hands in surrender, offering a nervous smile. "Hey- I'm not 
trying to attack you! I don't have much of anything valuable- so you must be here 
looking for me, right..? Not to kill me, I hope..."

Clearly, they weren't here to kill you, or you would be dead... They lower their 
gun somewhat as you continue to approach, looking at them without any trace of fear or doubt.

"See? Nothing to be afraid of." You're standing in front of them, and while they're 
tense and uncomfortable, they don't know what else to do besides look at you. \n""")
                                        Flag5 = False
                                        You4 = str.upper(input("FOOD, HOST.\n"))

                                        while Flag5 == False:

                                             if You4 == "FOOD":
                                                  Flag5 = True
                                                  print("""[FOOD]

You look at them a moment longer, before laughing slightly, shaking your head. 
"Well, if you weren't here for me before, you are now... A shame that the gun 
wouldn't have worked on me."

They take half a step away and you leap forward, tackling them to the ground. 
They're trying very hard to push you off, but they can't get a good grip before you 
bite them, teeth sinking into their neck.

They continue to struggle, as they always do- but you're experienced enough to know 
they won't break free. Not alone, with you drawing their life out of them so directly... 

Hopefully the screaming didn't alert the neighbors.

[END; VAMPIRE]""")

                                             elif You4 == "HOST":
                                                  Flag5 = True
                                                  print("""[HOST]

You inch closer and closer, until you have a hand on their shoulder. Waiting 
until you feel them relax, just slightly...

One hand moves to grab ahold of the front of their clothes, and the other to 
the back of their head, dragging them forward towards you by force. They try to 
push you away, crying out in shock at the action, but can't escape the attack. 
Nor can they escape what leaves you, throwing itself from your body into theirs, 
and leaving you to fall exhausted to the ground.

The stranger lets out a somewhat strangled cry, clawing at their chest and shuddered 
heavily... before very suddenly stopping, and standing up with a slight stretch.

"Ah, good- I thought I'd have to find someone new tomorrow, but this was much more convenient."

They turn back to look at you, grinning lightly. "Now then- I just have to get
rid of you, right? I'm sure you remember."

You do. And you aren't looking forward to your future.

[END; PARASITE]""")

                                             else:
                                                  You4 = str.upper(input("Try again.\n"))

                                   elif Choice3A == "IT":
                                        Flag4 = True
                                        print("""[IT]

You smile gently, and leave the knife on the counter as you move. The stranger 
pulls a gun on you, but you raise your hands in surrender. "I'm not going to hurt 
you! If you're here to see it, I can show you where it is."

They hesitate, but slowly lover their gun. Allowing you to walk around them and 
down the hall, watching you closely for anything suspicious.

You lead them to a door that goes down into a basement, and they look at you dubiously. 
You, of course, roll your eyes, turning on the light and continuing down, waiting for them to follow.

They're standing at the bottom when you turn off the lights again, surprised. Then, shouting 
in alarm when the door slams at the top of the stairs, much further than either of you could reach.

Now that its dark you can see something else. So can the stranger, and they scream and shoot 
at it to no avail. Hissing and grinding and growls fill the air, until eventually the screaming 
stops, replaced by a wet dripping sound...

"I hope that was alright for you... They were confident enough to try breaking in, so it couldn't have been all bad!"

Whispers of approval echo around you, and you smile.

[END; CARETAKER]""")

                                   else:
                                        Choice3A = str.upper(input("Try Again.\n"))

                         else:
                              Ignore2 = str.upper(input("try again.\n"))

               elif Choice1 == "HIDE":
                    Flag2 = True

                    print("[HIDE]\n\nWhere?\n")
                    Flag3 = False
                    Hide2 = str.upper(input("CABINETS, TABLE, BEDROOM, CLOSET\n"))

                    while Flag3 == False:

                         if Hide2 == "TABLE":
                              Flag3 = True
                              print("""[TABLE]

You run to hide under the table and the door is thrown up, a stranger breaking their 
way into the house soon after. They look around a moment, and... see you under there....... 

right there.....

...

Unfortunately, much to your surprise, they just end up shooting you.

[END; MURDERED]""")

                         elif Hide2 == "CLOSET":
                              Flag3 = True

                              print("""[CLOSET]

You run to the closet and close the door, right as the door is 
thrown open to your house. Putting a hand over your own mouth, trying to 
stifle the sound of your voice...

You can hear them walking through your house, and eventually past where you're hiding. 
Moving so deliberately, they have to be looking for you. Surely they know someone's here...\n""")
                              Flag4 = False
                              Closet3 = str.upper(input("Will you WAIT? Or try to RUN?\n"))

                              while Flag4 == False:

                                   if Closet3 == "WAIT":
                                        Flag4 = True
                                        print("""[WAIT]

You try to settle into place, letting tears fall silently. When the stranger walks by 
you go as still as a statue, and you're sure you're going to be found, this was a stupid place to hide...

But, eventually, the front door slams closed, and you hear nothing. The silence lasts... 
so long. You can't leave, for a long time, and when you do... it's followed by the feeling that 
the place you call home is not safe anymore.

[END; DISTURBED]""")

                                   elif Closet3 == "RUN":
                                        Flag4 = True
                                        print("""[RUN] 

You can't stay here. They're going to find you no matter what happens, you have to go now.

You throw the closet door open when you feel like the moment is best and start running. 
You hear footsteps behind you, and a shout- but you don't stop, and scream as a shot goes 
off behind you, even though it doesn't meet its mark.

You run into a neighbor on the street, panicked and crying. It's hard to tell them what's 
going on in a way they can understand, panicked as you are... But, they take you in for the 
night, a bit awkwardly perhaps... but, it's safer, right? 

Right?

[END; TERRIFIED]""")

                                   else:
                                        Closet3 = str.upper(input("Try again.\n"))

                         elif Hide2 == "BEDROOM":
                              Flag3 = True

                              print("""[BEDROOM]

You start running to the bedroom, and the door opens before you can make it all the way. 
You hear a shout behind you as you close the door, and lock it, looking around the room. 
There's nowhere for you to go from here...\n""")
                              Flag4 = False
                              Bedroom3 = str.upper(input("Maybe you can hide in the CLOSET? Or try and prepare to ATTACK?\n"))

                              while Flag4 == False:

                                   if Bedroom3 == "CLOSET":
                                        Flag4 = True
                                        print("""[CLOSET]

You run to the closet and close the door, waiting. The stranger is pounding 
on the door. Over, and over, until something snaps and you know they're in the room. 
Footsteps heavy, because they aren't trying to hide.

They make their way through the room almost methodically. Moving things. 
Searching for you. They know you're here somewhere. They don't care about making a mess.

When the noise pauses, the silence is crushing... and it's broken by three shots. 
One misses. One hits you in the arm. One hits you in a more vital place.

You cough, clutching the wound, falling forward and hitting the door with your head. 
Then the door opens, and you fall somewhat out onto the ground, the stranger 
looking down at you mercilessly.

They shoot one last time, and it's over you.

[END; MURDERED]""")

                                   elif Bedroom3 == "ATTACK":
                                        Flag4 = True
                                        print("""[ATTACK]

You turn towards the door and brace yourself, breath shakey. The door is hit, 
over and over again, until it's thrown open.

You move to attach them, but you weren't as prepared as you thought- and they
 were more armed than you expected. Stars flash through your vision as you're 
 hit with their gun, knocked to the ground with the knife out of your grip. Trying to 
 focus on the strangers face as they level the gun at your head.

"It's over."

And then it is.

[END; MURDERED]""")

                                   else:
                                        Bedroom3 = str.upper(input("try again.\n"))

                         elif Hide2 == "CABINETS":
                              Flag3 = True

                              print("""[CABINETS]

You open one of the kitchen cabinets and squeeze inside, pushing whatever's inside aside to 
try and give yourself space. You hear the front door forced open and try to close the cabinet door...

It's a bit louder than you realized, unfortunately.

You hold your breath and wait, trying to listen to the sounds outside. Soon enough 
you hear heavy footsteps walking through the kitchen. What do you do?\n""")
                              Flag4 = False
                              Cabinets3 = str.upper(input("Try and WAIT quietly? Or try to catch them off guard and ATTACK?\n"))

                              while Flag4 == False:

                                   if Cabinets3 == "ATTACK":
                                        Flag4 = True
                                        print("""[ATTACK]

You grab ahold of your weapon and try to dive out of your hiding place 
when you hear them in the right spot. It's... not really a good angle of attack, though...

And it's much easier for the stranger to just shoot down at you from so close.

[END; MURDERED]""")

                                   elif Cabinets3 == "WAIT":
                                        Flag4 = True

                                        print("""[WAIT]

You hold your breath and wait, listening as they walk past. They don't find you, 
and you eventually can't hear them close anymore.\n""")
                                        Flag5 = False
                                        Wait4 = str.upper(input("Will you LEAVE now? Or continue to WAIT?\n"))

                                        while Flag5 == False:

                                             if Wait4 == "WAIT":
                                                  Flag5 = True
                                                  print("""[WAIT]

You wait longer, as long as you possibly can... Maybe longer than you really had to, 
but you had to make sure.

When you do leave your hiding place, it's a bit noisy, but nothing beyond that. 
The house is unsettlingly silent now... and there is the extremely distinct sense 
that it's been damaged. Not literally- but the sense of safety this house gave you is shattered now...

You call a friend, and ask if you can stay at their place... maybe for a while.

[END; DISTURBED]""")

                                             elif Wait4 == "LEAVE":
                                                  Flag5 = True
                                                  print("""[LEAVE]

You try to leave quietly, but you're in a small space that had a lot of kitchenware 
in it. Leaving is somewhat clumsy, and the noise is definitely not going to escape their notice...

Sure enough, you're standing up and you hear a gun click. All you can do is 
raise your hands, hoping they won't decide to kill you...

[END; DISCOVERED]""")

                                             else:
                                                  Wait4 = str.upper(input("try again.\n"))

                                   else:
                                        Cabinets3 = str.upper(input("try again.\n"))

                         else:
                              Hide2 = str.upper(input("Try Again.\n"))

               elif Choice1 == "CHOOSE":
                    Flag2 = True

                    print("""[CHOOSE]

You move to stand in a place near the door, where it would be hard for 
someone to see you if they were walking inside. You'll be able to make another CHOICE from there.

There are a few loud clicks from the lock, and the door opens, letting someone 
walk through. Taller than you, but not by much, and unarmed as far as you can tell. They don't know you're there.\n""")
                    Flag3 = False
                    Choose2 = str.upper(input("You could KILL them. You can try to RUN, or maybe you can just WAIT...\n"))

                    while Flag3 == False:

                         if Choose2 == "KILL":
                              Flag3 = True

                              print("""[KILL]

They're a few steps into the house when you attack them. Striking from behind, 
stabbing them with your knife where you think you'll do the most damage- and you 
pull it off, for the most part, even if the stranger does struggle.

They don't win.

You have them on the ground, their blood on your hands, when you notice movement outside. 
On the sidewalk, one of your neighbors was walking by... 
and they've seen the scene that's just within your front door.\n""")
                              Flag4 = False
                              Kill3 = str.upper(input("The panic is clear in their expression. Are you going to EXPLAIN yourself? Or ELIMINATE any witness.\n"))

                              while Flag4 == False:

                                   if Kill3 == "EXPLAIN":
                                        Flag4 = True
                                        print("""[EXPLAIN]

"Wait- it's not what it-!"

Unfortunately, they're already running, and you can't get up and out to them 
fast enough to explain- not that going out there looking like you do is a good idea anyways...

You sigh, and as you expected, the police are soon at your door. Not asking 
very many questions, considering you were caught red handed with the body and 
the murder weapon. Hopefully they'll listen when you say it was self defense.

[END; KILLER]""")

                                   elif Kill3 == "ELIMINATE":
                                        Flag4 = True
                                        print("""[ELIMINATE]

You sprint out the door towards your neighbor, knife firmly in hand. 
They scream and stumble somewhat, trying to run. They aren't faster 
than you though, and it's not hard to kill them either...

Unfortunately, now that means you have two dead bodies... luckily, 
you can take care of that. Picking your neighbor's body up off the street 
and carrying it inside, closing the door behind you. Clean up can happen 
in a bit, a good clean up.

The bodies of your neighbor and the stranger are both placed in the basement,
and you're sure to close the door as you leave. Waiting until you hear a 
hiss and whispers of approval from beyond the door before moving on.

That will keep it fed for a week or two. A shame that these kills had to be so messy... 
normally you're much more composed. 

[END: KILLER]""")

                                   else:
                                        Kill3 = str.upper(input("try again.\n"))

                         elif Choose2 == "RUN":
                              Flag3 = True
                              print("""[RUN]

You wait for them to pass, then run through the still open door out into the night. 
If they noticed, they don't seem to follow you, although you run into a neighbor on the 
street... You insist that you're fine, trying to explain away the knife as best you can, 
and... it's not the most convincing of lies...

Your neighbor decides to continue along down the road a bit faster than before, and you 
go on your own way. You aren't sure how long to stay out before going home... eventually 
you call a friend, and they agree to let you sleep over for the night. You can resolve everything tomorrow.

[END: COWARD]""")

                         elif Choose2 == "WAIT":
                              Flag3 = True

                              print("""[WAIT]

You wait in silence as they move further into the house, carefully closing the door behind themselves. 
They're looking around at the house, ignoring most of what they see and continuing further down the hall.\n""")
                              Flag4 = False 
                              Wait3 = str.upper(input("They're somewhat far now. Are you going to RUN, or FOLLOW? maybe you can just IGNORE them..?\n"))

                              while Flag4 == False:

                                   if Wait3 == "RUN":
                                        Flag4 = True
                                        print("""[RUN]

You sneak out the door and run, ignoring the house entirely. You don't want to be anywhere near it for a while.

It's hard to say how long you're out for. Long enough for the night to grow dark and for you to be alone in 
the silence of it. It should have been long enough by now, right..? It should be safe to go back...

You return to your house, silent and untouched. Everything is how you left it, besides the stranger being 
gone. That's a good thing- it's good, you tell yourself... You don't need to worry about where they went... 
you don't need to worry about what happened while you were gone.

[END; IGNORANCE]""")

                                   elif Wait3 == "FOLLOW":
                                        Flag4 = True

                                        print("""[FOLLOW]

You creep quietly along behind them, watching as they move further into your house and staying out of sight. 
They're uninterested in most rooms, up until they get to a door you know leads to the basement.\n""")
                                        Flag5 = False
                                        Follow4 = str.upper(input("They go down into the basement. Will you FOLLOW, or CLOSE the door behind them?\n"))

                                        while Flag5 == False:

                                             if Follow4 == "FOLLOW": 
                                                  Flag5 = True
                                                  print("""[FOLLOW]

You follow the stranger down the stairs, and after a few steps the door slams behind you. 
They cry out in surprise and run into you, the room too dark for them to realize 
you're there, initially. "What's going on-!?"

You start to reply, but you're interrupted by a growl, and a hissing sound that 
echoes through your skull. The room isn't lit up, but you can see it clearly, approaching 
the both of you. The stranger screams in fear and scrambles to their feet, trying to 
fumble their way up the stairs.

The door doesn't open. You stare as voices reach out to surround you, reassuring you that 
you are a guest in its place, and a very wonderful keeper. Of course you can watch. It adores your company.

The stranger is not a guest.

They don't stop screaming until it's done pulling them apart, and turning the stranger
into another part of it, twisting their fear into yet another extension of their form.

You don't even try to wipe the blood off when you stand to leave, opening the door 
instantly when you reach it. For another night, you can be grateful that you are welcome in this home.

[END; WITNESS]""")

                                             elif Follow4 == "CLOSE":
                                                  Flag5 = True

                                                  print("""[CLOSE]

You close the door behind them, and hear them cry out in surprise behind the door. 
You also hear what could almost be a hiss of steam, although very loud... Alongside a low growl.

A few moments later you hear the stranger scream, and start slamming against the door 
full force. "OPEN THE DOOR- PLEASE, I'LL GO, OPEN IT, LET ME OUT-!\"\n""")
                                                  Flag6 = False
                                                  Close5 = str.upper(input("OPEN? or LISTEN?\n"))

                                                  while Flag6 == False:

                                                       if Close5 == "OPEN":
                                                            Flag6 = True
                                                            print("""[OPEN]

A wave of dread comes over you at your choice, and you twist the knob to open it. 
The door doesn't budge, however, no matter how you pull.

You struggle uselessly until you hear them scream in pain and jolt, banging on 
the door yourself to try and get it to budge. This wasn't what you thought would happen, 
and you try to say your sorry. You shout it through the door hoping they'll hear it.

When silence falls you have tears in your eyes. You don't want to believe what's happened. 
You cry and ask through the door for answers that will never come.

[END; REGRET]""")

                                                       elif Close5 == "LISTEN":
                                                       
                                                            Flag6 = True
                                                            print("""[LISTEN]

You step back as they continue to pound on the door, begging you to open it for them. 
You hear them scream in pain and the sound of the stairs creaking under a heavy weight.

There are multiple loud snaps. Eventually the screaming does stop. The house is 
mostly silent, beyond an occasional thump from downstairs.

You have better things to do than listen to it down there.

[END; CONDEMN]""")

                                                       else: 
                                                            Close5 = str.upper(input("Try again.\n"))

                                             else:
                                                  Follow4 = str.upper(input("try again.\n"))


                                   elif Wait3 == "IGNORE":
                                        Flag4 = True
                                        print("""[IGNORE]

You sigh quietly in relief, and move to sit on the couch. You get comfortable, even- you don't do any kind of activity, of course not, you want to stay alert at the moment...

....A few minutes pass, and you can feel a slight shudder as a door slams shut. You nod and listen as there is a distant hiss from somewhere else, and a muffled scream soon after. Pounding footsteps and frantic banging on a door.

The door will not open, even if you were there to try, of course. Soon the screaming stops. They won't bother you anymore, and you don't have to worry about finding someone to... well...

Anyways, maybe you should go to sleep.

[END; INACTION]""")

                                   else: 
                                        Wait3 = str.upper(input("Try again.\n"))

                         elif Choose2 == "CHOICE":
                              Flag3 = True

                              print("""[CHOICE]

You quietly step closer to the stranger, careful not to disturb anything as you move. 
The door is silent as you close it, up until you shut it firmly, causing 
the stranger to turn around to face you. "What the-!?\"\n""")
                              Flag4 = False
                              Choice3B = str.upper(input("What will you CHOOSE now? Will you ATTACK? Try to TALK?\n"))

                              while Flag4 == False:

                                   if Choice3B == "ATTACK":
                                        Flag4 = True
                                        print("END")

                                   elif Choice3B == "TALK":
                                        Flag4 = True

                                        print("""[TALK]

"What are you doing in my house?" 

You raise the knife and the stranger takes a step back, hands up. "I- I didn't realize someone was home-"

"You shouldn't have broken in regardless."

The stranger seems to want to respond, but doesn't have anything to say.""")
                                        Flag5 = False 
                                        Talk4 = str.upper(input("What are you going to do with them? REPORT them? or let them go with a WARNING?\n"))

                                        while Flag5 == False:

                                             if Talk4 == "REPORT":
                                                  Flag5 = True
                                                  print("""[REPORT]

"Sit down." You gesture to the couch and they sit, uncomfortable but quiet. 
Once you've watched them for a few seconds, you use your phone and call emergency 
services- fully intent on reporting the stranger to the authorities, of course.

You don't get very far into the call before the table is turned. Now that there's 
some distance between you, the stranger is able to pull a gun faster than 
you can stop them. A bang is the last thing you hear.

[END; DEAD]""")

                                             elif Talk4 == "WARNING":
                                                  Flag5 = True
                                                  print("""[WARNING]

"Get out of my house. Now."

You step closer as they step back, staring harshly into their eyes. They 
skirt around you towards the door, hands still raised in careful surrender, 
and under your gaze leave the house.

You lock the door when they're out, and sigh in relief. Putting the knife 
away and trying to calm down a bit. There, it's handled... Now you don't 
have to worry about someone finding it.

[END; REPELLED]""")

                                             else:
                                                  Talk4 = str.upper(input("Try again.\n"))

                                   elif Choice3B == "CHOOSE":
                                        Flag4 = True

                                        print("""[CHOOSE]

You choose them.

You reach forward and grab them by the shirt, pulling them down until your faces are level. 
They pull back in surprise and you tug harder, forcing them to fall to one knee.\n""")
                                        Flag5 = False
                                        Choose4 = str.upper(input("POSSESS them.\n"))

                                        while Flag5 == False:

                                             if Choose4 == "POSSESS":
                                                  Flag5 = True
                                                  print("""[POSSESS]

You lean forward to kiss them. Something horrible escapes you, leaving a horrible taste in your 
mouth and allowing you to fall away from the stranger. 

They stand up and laugh at you, stepping forward and taking the knife from your hand. 
"Thanks- we both knew you were reaching the end of your use. This body should last a good few months..."

You look up to a cruel smile you once wore. It's a familiar scene to you- even if the 
last time it happened, you'd been the recently possessed. The knife is put to your throat.

"Seeya later!"

[END; PARASITE]""")

                                             elif Choose4 == "CHOOSE":
                                                  Flag5 = True
                                                  
                                                  Flag6 = False
                                                  count = 0
                                                  while count <= 6:
                                                       count = count + 1
                                                       print("POSSESS them")
                                                       
                                                  Choose5 = str.upper(input())

                                                  while Flag6 == False:

                                                       if Choose5 == "POSSESS":
                                                            Flag6 = True
                                                            print("""[POSSESS]

You lean forward to kiss them. Something horrible escapes you, leaving a horrible taste in your mouth and allowing you to fall away from the stranger. 

They stand up and laugh at you, stepping forward and taking the knife from your hand. "Thanks- we both knew you were reaching the end of your use. This body should last a good few months..."

You look up to a cruel smile you once wore. It's a familiar scene to you- even if the last time it happened, you'd been the recently possessed. The knife is put to your throat.

"Seeya later!"

[END; PARASITE]""")

                                                       elif Choose5 == "CHOOSE":
                                                            Flag6 = True
                                                            print("""[CHOOSE]

You exercise your free will.

You scream for the stranger to run, tears in your eyes. Letting go of them and stumbling back.

They run.

When "you" stand up they are as far as they can get, out of sight, out of your reach. "You" hiss in frustration, throwing the knife aside. 

"You won't be able to stop me forever. I'll move to someone else eventually."

[END]""")

                                                       else:
                                                            Choose5 = str.upper(input("POSSESS them.\n"))

                                             else:
                                                  Choose4 = str.upper(input("POSSESS them.\n"))

                                   else:
                                        Choice3B = str.upper(input("Invalid choice, please try again.\n"))

                         else:
                              Choose2 = str.upper(input("Invalid choice, please try again.\n"))

               else: 
                    Choice1 = str.upper(input("Invalid choice, please try again.\n"))

     else: 
          First0 = str.upper(input("That is not an option, please try again.\n"))




#Template:
#
#(Writing of situation)
#Flag -> False
#user variable = str.upper(Input(What u do user?))

#While Flag is False:

#If (user variable) = thing:
#      Flag -> True
#      (template here for reply)

#elif (user variable) = other thing:
#      Flag -> True
#      (template here too)

#Else: str.upper(input(Invalid answer, try again))