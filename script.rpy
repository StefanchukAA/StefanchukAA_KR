define m = Character('Mcas', color="#FFC0CB")
define a = DynamicCharacter("p_name", color = "#1E90FF")
define l = Character ('Лина', color = "#B22222")
define n = Character ('Некто', color = "#B22222")
define r = DynamicCharacter("r_name", color = "#B22222")
#define x = Character('Эллис', color="#98FB98")

# Начало игры:

image lina:
    "lina.png"
    zoom 0.5
image fon:
    "fon.jpg"
    zoom 2
image mcas:
    "mcas.png"
    zoom 0.3
    
image bud:
    "bud.jpg"
    zoom 2

label splashscreen:
    scene black with dissolve 
    pause 1
    show text "Говорите правду, проходя эту игру. В современном мире ее и так осталось мало." with dissolve 
    pause 3
    show text "Обещаю, эта игра затянет вас с первых секунд." with dissolve
    pause 3
    show text "Дисклеймер: все персонажи выдуманы, схожесть с реальными людьми лишь совпадение, всем больше 18 и бла бла бла." with dissolve
    pause 3
    show text "Покажи свой истинный облик." with dissolve
    pause 3
    show text "Удачи... хоть она и не поможет..." with dissolve 
    pause 4
    scene black with dissolve
    pause 1
    return
     

label start:

    #scene black with dissolve 
    #$ renpy.pause(2.0, hard = True) 
    
    #scene orig   
    play music "id.mp3"
    $ p_name = renpy.input(u"Как тебя зовут?") 
    
    
    "Вот как. %(p_name)s. Знаешь, что я тебе скажу, %(p_name)s?"
    "Ах, да, я не представилась."
    "Впрочем, важно ли тебе мое имя?"
    
    menu:
        "Да.":
            jump im
        
        "Честно? Нет.":
            jump notim
        
        "Я придумаю тебе имя.":
            jump pri
    
    
    
label im:
    scene fon
    show lina
    "Ого. Я удивлена."
    "Хорошо, меня зовут Лина."
    l "Это сокращение от моего имени, но мне оно более приятно."
    l "В общем, я буду твоим проводником в мире этой игры."
    l "Или голосом совести."
    l "Но перед этим... Ты..?"
        
    menu:
        "Я девушка.":
            jump girl_im
            
        "Я парень.":
            jump boy_im
           
label notim:
    scene fon
    show lina
    "Аххаха, что ж, спасибо за честность."
    "В таком случае, для тебя я буду некто."
    n "И зачем же я тут нужна?"
    n "Возможно, я буду тебе помогать... ну, чем смогу."
    n "К примеру, я точно не помогу выплатить твою ипотеку."
    n "С этим разберемся после. Но перед этим... ты..?"
    
    menu:
        "Я девушка.":
            jump girl_notim
        
        "Я парень.":
            jump boy_notim

label pri:
    scene fon
    show lina
    $ r_name = renpy.input(u"Как тебя зовут?")
    r "Хм, %(r_name)s, любопытное имя. "
    r "В общем, я буду твоим проводником в мире этой игры."
    r "Или голосом совести."
    r "Но перед этим... Ты..?"
        
    menu:
        "Я девушка.":
            jump girl_pri
        
        "Я парень.":
            jump boy_pri
    
label girl_im:
    l "Здорово! Из женской солидарности я постараюсь помочь тебе чуть лучше, чем обычно."
    l "Знаешь, при желании ты можешь попасть в любую часть света."
    l "И даже в любую эпоху."
    l "Интересно?"
    l "Я создам для тебя симуляцию на твой вкус."
    l "Итак... куда бы ты хотела попасть,%(p_name)s?"
    menu:
        "Прошлое.":
            jump girl_im_pro
        
        "Настоящее.":
            jump girl_im_nas
        
        "Будущее.":
            jump girl_im_byd
    
label girl_notim:
    n "Здорово! Из женской солидарности я постараюсь помочь тебе чуть лучше, чем обычно."
    n "Знаешь, при желании ты можешь попасть в любую часть света."
    n "И даже в любую эпоху."
    n "Интересно?"
    n "Я создам для тебя симуляцию на твой вкус."
    n "Итак... куда бы ты хотела попасть,%(p_name)s?"
    menu:
        "Прошлое.":
            jump girl_notim_pro
        
        "Настоящее.":
            jump girl_notim_nas  
        
        "Будущее.":
            jump girl_notim_byd

label girl_pri:
    r "Здорово! Из женской солидарности я постараюсь помочь тебе чуть лучше, чем обычно."
    r "Знаешь, при желании ты можешь попасть в любую часть света."
    r "И даже в любую эпоху."
    r "Интересно?"
    r "Я создам для тебя симуляцию на твой вкус."
    r "Итак... куда бы ты хотела попасть,%(p_name)s?"
    menu:
        "Прошлое.":
            jump girl_pri_pro
        
        "Настоящее.":
            jump girl_pri_nas  
        
        "Будущее.":
            jump girl_pri_byd
       
label boy_im:
    l "Отлично! Тогда поехали. "
    l "Знаешь, при желании ты можешь попасть в любую часть света."
    l "И даже в любую эпоху."
    l "Интересно?"
    l "Я создам для тебя симуляцию на твой вкус."
    l "Итак... куда бы ты хотела попасть,%(p_name)s?"
    menu:
        "Прошлое.":
            jump boy_im_pro
        
        "Настоящее.":
            jump boy_im_nas  
        
        "Будущее.":
            jump boy_im_byd

label boy_notim:
    n "Отлично! Тогда поехали. "
    n "Знаешь, при желании ты можешь попасть в любую часть света."
    n "И даже в любую эпоху."
    n "Интересно?"
    n "Я создам для тебя симуляцию на твой вкус."
    n "Итак... куда бы ты хотела попасть,%(p_name)s?"
    menu:
        "Прошлое.":
            jump boy_notim_pro
        
        "Настоящее.":
            jump boy_notim_nas  
        
        "Будущее.":
            jump boy_notim_byd

label boy_pri:
    r "Отлично! Тогда поехали. "
    r "Знаешь, при желании ты можешь попасть в любую часть света."
    r "И даже в любую эпоху."
    r "Интересно?"
    r "Я создам для тебя симуляцию на твой вкус."
    r "Итак... куда бы ты хотела попасть,%(p_name)s?"
    menu:
        "Прошлое.":
            jump boy_pri_pro
        
        "Настоящее.":
            jump boy_pri_nas 
        
        "Будущее.":
            jump boy_pri_byd

label girl_im_pro:
    l "Поверь мне, прошлое обязательно появится... уже скоро."
    l "А пока выберай что дают."
    menu:
        "Будущее.":
            jump girl_im_byd

label girl_notim_pro:
    n "Поверь мне, прошлое обязательно появится... уже скоро."
    n "А пока выберай что дают."
    menu:
        "Будущее.":
            jump girl_im_byd

label girl_pri_pro:
    r "Поверь мне, прошлое обязательно появится... уже скоро."
    r "А пока выберай что дают."
    menu:
        "Будущее.":
            jump girl_im_byd

label boy_im_pro:
    l "Поверь мне, прошлое обязательно появится... уже скоро."
    l "А пока выберай что дают."
    menu:
        "Будущее.":
            jump boy_im_byd

label boy_notim_pro:
    n "Поверь мне, прошлое обязательно появится... уже скоро."
    n "А пока выберай что дают."
    menu:
        "Будущее.":
            jump boy_im_byd

label boy_pri_pro:
    r "Поверь мне, прошлое обязательно появится... уже скоро."
    r "А пока выберай что дают."
    menu:
        "Будущее.":
            jump boy_im_byd

label girl_im_nas:
    l "Поверь мне, прошлое обязательно появится... уже скоро."
    l "А пока выберай что дают."
    menu:
        "Будущее.":
            jump girl_im_byd

label girl_notim_nas:
    n "Поверь мне, прошлое обязательно появится... уже скоро."
    n "А пока выберай что дают."
    menu:
        "Будущее.":
            jump girl_im_byd

label girl_pri_nas:
    r "Поверь мне, прошлое обязательно появится... уже скоро."
    r "А пока выберай что дают."
    menu:
        "Будущее.":
            jump girl_im_byd

label boy_im_nas:
    l "Поверь мне, прошлое обязательно появится... уже скоро."
    l "А пока выберай что дают."
    menu:
        "Будущее.":
            jump boy_im_byd

label boy_notim_nas:
    n "Поверь мне, прошлое обязательно появится... уже скоро."
    n "А пока выберай что дают."
    menu:
        "Будущее.":
            jump boy_im_byd

label boy_pri_nas:
    r "Поверь мне, прошлое обязательно появится... уже скоро."
    r "А пока выберай что дают."
    menu:
        "Будущее.":
            jump boy_im_byd 

label girl_im_byd:
    play music "boy.mp3"
    scene bud with fade
    show lina
    l "Это будущее, впечатляет?"
    l "Наслаждайся и помни: честность это золото."
    l "А я пошла, удачи!"
    hide lina
    show lina at right
    l "Так... ой"
    l "Почему я не могу выйти..."
    l "Что-то явно пошло не так..."
    
    menu:
        "Все в порядке?":
            jump proda
        
        "Аахахаха, ты застряла со мной?":
            jump proda

        
label proda:
    l "Нет-нет-нет, так не должно быть..."
    l "Просто превосходно... мне стоило чаще посещать те пары."
    l "Ладно, хорошо... соберись Лина"
    l "Я просто попала вместе с игроком в киберпанк, прекрасно"
    l "Никуда не уходи и ни с кем не говори."
    l "Я скоро вернусь."
    hide lina
    "Вот и одтиночество..."
    show mcas
    m "Ты еще кто?"
    m "Это закрытый мир, у тебя есть пропуск?"
    
    menu:
        "не отвечать":
            jump net
        
        "Есть, конечно":
            jump da
    
label net:

    m "Глухих завезли?"
    m "Отвечай кому говорю"
    return
        
label da:
    m "Так показывай, что стоишь?"
    return
        
        
 
label girl_pri_byd:
    "ofjv"

label girl_notim_byd:
    "ewpfk"

label boy_im_byd:
    "wfd"
    
label boy_notim_byd:
    "efref"

label boy_pri_byd:
    "efwf"


 
menu:
    
    "Да так...":
        jump da_tak
        
    "Бабушка попросила собрать ягод":
        jump igod
        
    
label da_tak:

    l "Возвращайся, в лесу детям не место."
    return

label igod:

    hide lesnik
    show lesnik at right
    l "Пойдем, знаю одну полянку."
    
    hide lesnik
    scene les2
    
    play music "les_bot.mp3"
    
    l "Этот лес я знаю как свои пять пальцев."
    l "Таких как ты он не отпускает."
    l "Пойдешь не по той тропке и кто знает где окажешься."
    
    stop music
    play music "medved.mp3"
    show lesnik
    
    l "Стоять!"
    l "Медведя нам тут не хватало."
    
    "Вы вглядываетесь вглубь леса."
    
    menu:
        "Лучше не рисковать":
            jump not_risk
        
        "Хочется своими глазами увидеть медведя":
            jump risk
        
label not_risk:

    "Жизнь дороже, вы следуюте за лесником."
    
    return
    
label risk:

    hide lesnik

    "Любопытство берет над вами вверх."
    show lesnik
    l "Айда, нечего на царя леса глазеть."
 
    return 
    
    