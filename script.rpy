# The script of your game goes in this file.

# Redimensionnement propre des arrière-plans (1920x1080)
image bg_room = Transform("room", xysize=(1920, 1080))
image bg_ckitchen = Transform("ckitchen", xysize=(1920, 1080))
image bg_tri9 = Transform("tri9", xysize=(1920, 1080))
image bg_marcet = Transform("marcet", xysize=(1920, 1080))
image bg_rofofe = Transform("rofofe", xysize=(1920, 1080))
image bg_cachier = Transform("cachier", xysize=(1920, 1080))
image bg_babe = Transform("babe", xysize=(1920, 1080))

# Redimensionnement des personnages avec des noms uniques pour éviter l'erreur
image spr_billy = Transform("billy", zoom=1.5)
image spr_cashier = Transform("cashier", zoom=1.5)

# Déclaration des personnages
define e = Character("Eileen")
define c = Character("cashier")
define j = Character("joche")
define M = Character("[player_name]")
define b = Character("billy")

# Le jeu commence ici.

label start:

    # Demande le nom du joueur
    $ player_name = renpy.input("What is your name?", default="")
    $ player_name = player_name.strip()
    
    if player_name == "":
        $ player_name = "Meow"

    scene bg_room

    " ou chit way i wak up now"
    " i'm so fucking hangry" 
    "what is the time now"
    " ou it is 3pm "
    "thas bad "            
    "i thing i still have some noudles in the ckitchen"
    
    scene bg_ckitchen
    "oh no , i dont have any noudles here "
    " i need to go to the store to buy some noudles "
    
    menu:
        "go to bay some":
            jump baysome

        "go back to sleep":
            jump backsleep

# --- Option 1 : Aller au magasin ---
label baysome:
    scene bg_ckitchen
    "i will bay some and eat it sceven eleven not far at my house"
    
    scene bg_tri9
    "oh thas bad the store is closed now, i have to go to the far one "
    
    menu:
        "go to the far store":
            jump farstore

        "go back home to sleep":
            jump backsleep

label farstore:
    scene bg_tri9
    "just i will go to the far store"
    "oh it so darck "
    show spr_billy at center
    " oh thas billy why he here in this tame "
    
    menu:
        "talk to billy":
            jump talk

        "dont talk withe billy":  
            jump donttalk

label talk:   
    show spr_billy at center
    M " hi billy "
    b " oh [player_name] , hi "
    b "oh this is long time wen i see you "
    M "oh thas rihte "
    M "oh i need to go now "
    b "oh yes but be careful ,i heard there are disappearance cases and thieves in this area"
    M "oh thas bad , i will be careful"
    b "oh ok , take care and call me if you need help"
    M " ok , thank you billy"
    "afther i say thas i go fast to the store "
    jump store_inside

label donttalk: 
    "i will ignor it thas long time wen i see him "
    "hh or i see any one "
    "just i will ignor it and go fast to the store"
    jump store_inside

label store_inside:
    scene bg_marcet
    "oh thas good the market is open now"
    
    scene bg_rofofe
    "i will go to the noudles section"
    "oh thas good i found the noudles"
    
    scene bg_cachier
    M " hi , any one here?"
    M " any one here?"
    " why is no one here "
    
    menu:
        "wait for a while":
            jump wait_cashier

        "juste stole":
            jump stole_noudles

# --- Option : Attendre au caissier ---
label wait_cashier:
    "i will wait for a while"
    "afther a 3 minutes , a man come to the cashier"
    "i thing he is the cashier "
    
    scene bg_cachier
    show spr_cashier at right
    c " hi , how can i help you?"
    M " hi , can i buy that?"
    c " sure , that will be 5$"
    M " ok , here is 5$"
    c " thank you , come back soon"
    
    scene bg_tri9
    "i need to go fast to my home ,i'm so hungry, and the time is later"
    " how is thas persen and way he walk behand me"
    menu:
        "run away":
            jump runaway_lolo

        "keep walking":
            jump keepwalking_lolo

label runaway_lolo:
    "i will run away from him"
    " oh that bad why he is running after me"
    " i need to run fast to my home"
    " oh finelly the house"
    
    scene bg_room
    "oh thas good i'm safe now  "
    "[player_name] you are safe now , you dont need to be afraid "
    " i will cook the noudles now "
    
    scene bg_ckitchen
    "oh thas good "
    " i'm so fucking hungry "
    " oh this noudles is so good" 
    
    scene bg_room
    " oh i feel so good now "
    " but i feel so tired , i will go to sleep now"
    
    scene black
    "good end"
    " jiji [player_name] "
    return

label keepwalking_lolo:
    " i will keep walking and ignore him"
    "oh thas bad he is running after me"
    "oh thas bad he is so fast , i need to run fast to my home "
    "oh no , i fell down , and he is so close to me"
    
    scene black
    "oh you dead , the game is over , hhhh you are so fucking stupid , you need to be more careful next time  "
    return

# --- Option : Voler les nouilles ---
label stole_noudles:
    " i think i will just stole the noudles no one will see me"
    "and wen i turne my back and walke to the door" 
    c " hey , what are you doing , you stolen the noudles"
    
    menu:
        "run away from store":
            jump runaway_store

label runaway_store:
    scene bg_tri9
    "oh i dont know whay i did that , i have mony "
    c " hey , stop , stoler "
    " oh thas bad he is running after me"
    c " hey i know your face betch , i will call the police the next time i see you"
    " oh he go back to the market "
    " thas good i will eat the best noudles in my life"
    
    scene bg_babe
    " i need to run fast inside my house"

    scene bg_ckitchen
    "i will cook the noudles now"
    "oh this noudles is so good even if i stole it"
    
    scene bg_room
    "i will go to sleep now"
    
    scene black
    "stolen end"
    "you ate but you are a thief now [player_name]!"
    return

# --- Option 2 : Retourner dormir ---
label backsleep:
    scene bg_ckitchen
    "i will eat tomorow i will not day if i didn't eat "
    
    scene bg_room
    "just i come back to sleep, i will eat tomorrow "
    
    scene black
    "end of the game "
    "you fineche the game baby thank for playe it and why are you so boring chose something elese"
    return