# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
define rightCharacter = Position(xalign = 0.8, yalign = 0.0)
define leftCharacter = Position(xalign = 0.2, yalign = 0.0)

# 게임에서 사용할 캐릭터를 정의합니다.
#공략 캐릭터
define kunugi = Character('쿠누기 아키오미', color = "#ffffff")
define leo = Character('츠키나가 레오', color = "#ffffff")
define tsukasa = Character('스오우 츠카사', color = "#ffffff")
define kohaku = Character('오우카와 코하쿠', color = "#ffffff")
define HiMERU = Character('HiMERU',color = "#ffffff")

#별도 지정 휴먼
define f = Character('친구', color = "#ffffff")
define m = Character('???', color = "#ffffff")
define p = Character('OOO', color = "#ffffff")
define nn = Character('플레이어', color = "#ffffff")
define n = Character("[player_name]", color = "#ffffff")
define h = Character('회사동료', color = "#ffffff")
define b = Character('직원', color = "#ffffff")
define h = Character('간호사1', color = "#ffffff")
define hh = Character('간호사2', color = "#ffffff")
define k = Character('가게 직원', color = "#ffffff")

#배경 이미지
image background_es_in = "background/es_in.png"
image background_es_in1 = "background/es_in1.png"
image background_es_talking = "background/es.talking.png"
image background_es_company = "background/es.company.png"
image background_es_tree = "background/es_tree.png"
image background_walk = "background/walk.png"
image background_white = "background/white.png"
image background_hos = "background/hos.png"
image background_hos_b = "background/hos_b.png"
image background_hos_0 = "background/hos0.png"
image background_caffe = "background/caffe.png"
image background_after = "background/after.png"
image background_moring_walk = "background/moring_walk.png"
image background_night_walk = "background/night_walk.png"
image background_pos_night = "background/pos_night.png"
image background_ex = "background/ex.png" 
image background_caffe_lite = "background/caffe.lite.png"
image background_es_off = "background/es.off.png"
image background_music_room = "background/music_room.png"
image background_es_self = "background/es.self.png"
image background_park = "background/park.png"
image background_walk_caffe = "background/walk_caffe.png"
image background_home ="background/home.png"
image background_night_home = "background/home_night.png"
image background_night_home_walk = "background/night_home_walk.png"
image background_tur = "background/tur.png"
image background_walk_walk = "background/walk_walk.png"


#이벤트 배경 이미지
image background_matsuri = "background/matsuri.png"
image background_night_matsuri = "background/night_matsuri.png"
image background_night_000 = "background/night_000.png"
image background_sakura = "background/sakura.png"
image background_playroom = "background/playroom.png"
image background_merry_go_round = "background/merry_go_round.png"
image background_merry_go_round_night = "background/merry_go_round_night.png"
image background_gost = "background/gost.png"
image background_bus_in = "background/bus_in.png"
image background_night_beach = "background/night.beach.png"
image background_white_walk = "background/white.png"
image background_chrismas = "background/chrismas.png"
image background_movie = "background/movie.png"
image background_movie_box = "background/movie_box.png"
image background_eat = "background/eat.png"


#히든엔딩 배경 이미지
image background_hos_night_b = "background/hos_night_b.png"
image background_hos_night = "background/hos_night.png"


#중간 분기점 이미지
image background_tsukasa = "images/tsukasa.png"
image background_kohaku = "images/kohaku.png"
image background_kunugi = "images/kunugi.png"
image background_HiMERU = "images/HiMERU.png"
image background_leo = "images/leo.png"
image background_dream = "dream.png"

#츠카사 캐릭터 이미지
image tsukasa nomal = "characters/tsukasa nomal.png"
image tsukasa hmm = "characters/tsukasa hmm.png"
image tsukasa happy = "characters/tsukasa happy.png"
image tsukasa dessert = "characters/tsukasa dessert.png"
image tsukasa sad = "characters/tsukasa sad.png"
image tsukasa very happy = "characters/tsukasa very happy.png"
image tsukasa near = "characters/tsukasa n.png"
image tsukasa wow = "characters/tsukasa wow.png"

#코하쿠 캐릭터 이미지
image kohaku nomal = "characters/kohaku nomal.png"
image kohaku hmm = "characters/kohaku hmm.png"
image kohaku sad = "characters/kohaku sad.png"
image kohaku wow = "characters/kohaku wow.png"
image kohaku angry = "characters/kohaku angry.png"
image kohaku love = "characters/kohaku love.png"
image kohaku happy = "characters/kohaku happy.png"

#레오 캐릭터 이미지
image leo nomal = "characters/leo nomal.png"
image leo hmm = "characters/leo hmm.png"
image leo happy = "characters/leo happy.png"
image leo sad = "characters/leo sad.png"
image leo wow = "characters/leo wow.png"
image leo unhappy = "characters/leo unhappy.png"
image leo very happy = "characters/leo very happy.png"

#히메루 캐릭터 이미지
image HiMERU nomal = "characters/himeru nomal.png"
image HiMERU nomal1 = "characters/himeru nomal1.png"
image HiMERU hmm = "characters/himeru hmm.png"
image HiMERU sad = "characters/himeru sad/png"
image HiMERU sad1 = "characters/himeru sad1.png"
image HiMERU when = "characters/himeru whan.png"
image HiMERU happy = "characters/himeru happy.png"

#쿠누기 캐릭터 이미지
image kunugi nomal = "characters/kunugi nomal.png"
image kunugi sad = "characters/kunugi sad.png"
image kunugi no = "characters/kunugi no.png"
image kunugi hmm = "characters/kunugi hmm.png"
image kunugi angry = "characters/kunugi angry.png"

#CG이미지 갤러리
image 1:

    im.FactorScale ("1.png", 1)
    yalign 0.0

image 2:

    im.FactorScale ("2.png", 1)
    yalign 0.0

image 3:

    im.FactorScale ("3.png", 1)
    yalign 0.0

image 4:

    im.FactorScale ("4.png", 1)
    yalign 0.0

image 5:

    im.FactorScale ("5.png", 1)
    yalign 0.0

image 6:

    im.FactorScale ("6.png", 1)
    yalign 0.0

init python:

    g = Gallery()

    g.locked_button = "images/gal-locked.png"

    g.button("cg1")
    g.unlock_image("images/1.png")

    g.button("cg2")
    g.unlock_image("images/2.png")

    g.button("cg3")
    g.unlock_image("images/3.png")

    g.button("cg4")
    g.unlock_image("images/4.png")

    g.button("cg5")
    g.unlock_image("images/5.png")

    g.button("cg6")
    g.unlock_image("images/6.png")

    g.button("cg7")
    g.unlock_image("images/7.png")

    g.button("cg8")
    g.unlock_image("images/8.png")

    g.button("cg9")
    g.unlock_image("images/9.png")

    g.button("cg10")
    g.unlock_image("images/10.png")



    g.button("cg1")
    g.unlock_image("1")

    g.button("cg2")
    g.unlock_image("2")

    g.button("cg3")
    g.unlock_image("3")

    g.button("cg4")
    g.unlock_image("4")

    g.button("cg5")
    g.unlock_image("5")

    g.button("cg6")
    g.unlock_image("6")

    g.button("cg7")
    g.unlock_image("7")

    g.button("cg8")
    g.unlock_image("8")

    g.button("cg9")
    g.unlock_image("9")

    g.button("cg10")
    g.unlock_image("10")

    g.transition = dissolve

# 여기에서부터 게임이 시작합니다.
label start:
    scene background_es_talking with fade
    play music "main.mp3" loop 

    p "후우.....드디어 다 끝냈네....이제 슬슬 가야지."

    "회사일을 겨우 끝마치고 이제 집으로 갈까 싶어 자리에서 일어났다."
     
    play sound "down.mp3"
    scene background_es_talking with hpunch
    with Pause(2)
    
    "가방을 들고 집으로 향하려는데, 회사 복도 쪽에서 큰 소리가 났다."

    p "뭐지..?"
    
    play sound "walkfoot.mp3"
    "소리의 원인이 뭔지 파악하기 위해 서둘러 복도로 갔다."
    
    scene background_es_in with dissolve
    "복도로 나가보니 작지만 여러개의 상자들이 쓰러져 있었다."

    p "다 쓰러졌네!! 이거 중요한 물품들이라 망가지면 큰일나는데..!!" with hpunch

    p "으음....."

    "이걸 내버려두고 집에 갈지 아니면 옮겨두고 갈지 고민을 하다가 결국..."

    p "아무리 그래도 옮겨놓고 가야지...하하"

    "옮겨놓고 가기로 했다."

    p "일단, 계단 아래쪽에 놓아두면 될거 같은데.."

    p "잠깐만...진짜? 엘리베이터 점검..??"

    "하필이면 지금 엘리베이터 점검이라는 문구가 종이에 쓰여져 있었다."

    "어쩔 수 없이 계단으로 옮기기로 했다."

    scene background_walk with dissolve
    play sound "walkfoot.mp3"
    p "양이 은근 많네..."

    "분명 눈으로만 봤을때는 금방 옮길 줄 알았는데, 옮기다보니 양이 꽤 엄청났다."

    "게다가 요 며칠은 일이 계속 많았던터라 피로도 갑자기 몰려오는거 같다."
    
    stop music fadeout 1.0
    p "조금만 더 옮기면 되는데..."
    
    play music "waring.mp3" loop 
    p "으앗!!!!" with hpunch

    "결국 피로가 몰려와 그만 발을 헛딪여버렸다."

    m "ooo!!!!!!!!" with hpunch

    "누군가가 계단에서 내려오고 있었는지 넘어지려던 나를 부르며 잡기 위해 팔을 뻗었지만 간발의 차로 잡지 못했다."

    "누구인지라도 확인하려했지만 시야가 흐려 사람의 인영만 보일 뿐 누구인지 알 기 어려웠다."

    scene background_white with fade
    play sound "down.mp3"
    "그렇게 넘어져 의식을 잃었다"

    scene background_white
    stop music fadeout 2.0

    menu:
        
        "당신의 이름은 무엇인가요?":
         
            $player_name = renpy.input("(내 이름은...)")
            $player_name = player_name.strip()
            if player_name == "":
                $player_name = "플레이어"



label endtest:
if persistent.ending1 and persistent.ending2 and persistent.ending3 and persistent.ending4 and persistent.ending5:
    scene background_white with fade

    "당신은 모든 캐릭터와의 엔딩을 보셨습니다."

    "이제 이 이야기의 마지막을 보실 차례입니다."

    "일어나십시오.."

    scene background_dream with fade
    with Pause(1)
    
    
    scene background_hos_night_b with fade
    with Pause(1)

    scene background_hos_night with dissolve
    
    "머리가 아파 제대로 누워 있기 힘들어 겨우 눈을 떴다."

    "귀는 먹먹해서 주변 소리가 잘 들리지 않는다."
    
    "눈을 겨우 뜨자 어둡지만 흰색으로 추정되는 천장이 보인다."

    "분명 여기는 내 방은 아닐것이다."

    "주변을 둘러보니 여러개의 침대가 보였지만 이곳에는 나 혼자인거 같다."

    "코와 입이 무언가에 싸인듯이 답답했지만, 왠지 이게 없으면 숨을 쉬기 버겁다...."

    "문득, 팔에 위화감이 느껴져 몸이 무거워 움직이기 힘들었지만, 겨우 팔을 들었다."

    n "....뭐지...? 바늘?"

    "팔에는 주사바늘이 꽂혀있었다."

    "분명 이런건 영화나 드라마에서나 볼 법한 일인데, 왜 내가 이걸 하고 있는건지 잘 모르겠다."

    "정신을 차리려고 무겁지만 눈을 계속 깜빡거리며 있으니 먹먹했던 귀가 조금씩 돌아오기 시작했다."
    
    play music "heart.mp3"
    scene background_hos_night
    with Pause(2)

    "알 수 없는 기계음이 규칙적으로 들려온다."

    "도대체 이게 무슨 소리인가 싶어 고개를 왼쪽으로 돌려 위쪽을 향해 바라보니 링겔로 추정되는 것과, 같은 형태로 움직이는 기계..? 같은게 보였다."

    "그리고 그 기계들은 내 손과 연결되어있다."

    n "으윽....!" with hpunch
    
    stop music fadeout 2.0
    "갑자기 지끈거리던 머리가 이내 깨질듯이 아파오기 시작했다."

    "너무 아파 눈을 질끈 감고 있자, 이내 머리안에 영사기의 필름이 돌아가듯이 장면들이 하나하나 재생되었다."

    scene black with dissolve
    with Pause(2)

    "장면들속에는 내 모습이 있었다."

    "더러운 방 안에서 게임을 하는 모습, 무언가를 먹기 위해 서랍을 열던 모습, 먹을게 없어 대충 입고 나가던 모습..."

    "그리고.........."

    n "(트럭이 돌진해서.....)"
    
    play music "bibi.mp3"
    scene black
    with Pause(2)
    
    stop music fadeout 2.0
    scene background_hos_night with dissolve
    n "......"
    
    play music "hidden.mp3"
    n "(나는...밖에 나가지도 않고 게임만 하던...일명 히키코모리..였어..)"

    n "(집안에 먹을게 다 떨어져서 밖에 나가서 사오려고 가다가...트럭이...돌진해서...)"

    "그러다 문득, 무엇인가 생각나 협탁이 있을 것 같은 곳에 시선을 옮기자 내 핸드폰이 보였다."

    "핸드폰을 겨우 들어 버튼을 누르자....."

    "내가 지금까지 겪었던 일들의 주인공들이 핸드폰 화면에 있었다."

    n "(분명....이 사람들은.....)"

    "기억을 조금씩 더듬어 내가 게임을 하던 기억에 집중한다."

    n "(그때 나는 게임을 하고 있었어...그 게임에서...)"
    
    n "(.....)"

    n "(설마....?)"

    n "(내가 여태까지 겪었던 일들은...모두...게임캐릭터와의 꿈...이였던거야?)"

    "내가 여태까지 겪은 일들은 모두 내가 정말 좋아하는 게임의 캐릭터들과 함께한 망상, 꿈이였다."

    "그걸 알아채자 갑자기 텅 빈듯한 느낌을 받았다."

    "안그래도 차가웠던 손은 더더욱 차가워지고 이제는 덜덜 떨리기까지 한다."

    "눈에서는 눈물이 쉴새없이 나온다."

    n "내가...내가 지금까지 겪어왔던게 전부 꿈이였다고...?"

    "그동안 있었던 일들이 마치 신기루처럼 흩어진다."

    "부모도 없고, 있을곳도 마땅치 않고, 하루하루 그저 폐인같은 생활만 하다 겨우 내 자리를 찾은 듯한 기분이였다."

    n "내가 있을 곳을 겨우 찾았었는데...왜!!!!!!" with hpunch

    n "으아아아아아아!!!!!!!!!!!!!!!!!" with hpunch

    n "다시...다시 돌려보내줘!!!!! 더 이상 내가 있을 곳을 잃는건 싫어!!!!!!!!!" with hpunch

    "제발 부탁이니까 다시 그곳으로 돌아가고 싶다라는 생각만이 맴돈다."

    "병실 안에서 혼자 울부짖고 있자 밖에서 간호사들이 들어오는 소리가 들렸다."
    
    h "환자분!! 제발 정신차리세요 네??"

    hh "지금 OOO병동 환자가 흥분상태입니다. 진정제 투여가 필요할거 같습니다."

    "간호사들은 진정시키려 애를 썼지만, 상실감에 빠져버린 나는 그저 울부짖는거 밖에 할 수 없었다."

    "규칙적으로 뛰던 기계음이 빠르게 요동치기 시작한다."

    "조금 지나자 흥분한 나에게 누군가 다가온다. 아마 의사인거 같다."

    "의사가 나에게 무언가를 꽂는 감각이 느껴진다. 서서히 다시 눈이 감긴다."

    n "(이제...다시...만날...수...있..어...)"

    "나는 내가 염원했던 곳으로 다시 갈 수 있다는 생각으로 행복해졌다."

    "그렇게 나는 다시 눈을 감았다."

    scene black with dissolve
    with Pause(2)
    stop music fadeout 2.0

    "히든엔딩 - 진실"

    return    



label chpter1:
    
    scene background_dream with fade
    with Pause(1)

    scene background_hos_b with fade
    with Pause(1)

    scene background_hos with dissolve
    play music "main.mp3" loop
    "머리의 두통과 함께 눈을 겨우 뜨니 병원이였다."

    n "뭐지...? 나 아까까지만 해도 분명 회사 계단에 있었던거 같은데.."

    "주변을 둘러보니 누군가가 있다 간건지 흔적이 조금 남아있었다."

    "회사 계단에 있었던 날을 중심으로 기억을 더듬어 보지만, 누군가 억지로 지워놓은듯이 그 부분의 기억만 전혀 떠오르지 않았다."

    "그때 도와주려던 분은 누구였을까?"

    "찾으면 꼭 감사하다고 전하고 싶은데...."

    "그렇게 생각하던 중, 갑자기 쎄한 기분이 느껴진다."

    n "....잠깐, 오늘이 며칠이지?"

    "불안한 마음으로 핸드폰을 키자 이미 며칠이나 지나있었다."
    
    "그리고, 쿠누기 씨에게도 문자가 와 있었다."

    "쿠누기 씨는 내 상사이시자 내가 아직 일에 서툴렀을때 부터 옆에서 도와주신분이다."

    "평소에도 많은 신세를 지고 있어 늘상 죄송한 마음이라 평소에 실수하지 않도록 노력했는데, 아무래도 이번에도 신세를 져 버린것 같다."
 
    kunugi "(쿠누기 입니다. 일어나셨다면 답장 주세요.)"

    "그 문자에 최대한 빠르게 답장을 건네고 병원의 퇴원 허락과 함께 바로 퇴원을 했다."
    
    play sound "Phone.mp3"
    scene background_hos_0 with dissolve
    kunugi "(일어나셔서 다행입니다. 시간 괜찮으시다면 회사로 잠시 들러주세요.)"
    
    "문자를 보자마자 바로 회사로 향했다."

    "다행히 회사가 병원이랑 가까워서 빠르게 도착할 수 있을꺼 같다."

    scene background_es_off with dissolve
    n "겨우 도착했네..."

    "시간을 확인해보니 병원에서부터 그리 오랜 시간이 지나지 않은 시점에 도착했다."
        
    "회사랑 가까워서 정말 다행이라는 생각을 다시 하며 회사 문을 열었다."

    scene background_es_in1 with dissolve
    show kunugi no with dissolve
    kunugi "벌써 도착하셨군요. 좀 더 천천히 오셔도 괜찮았습니다만..."

    "문을 여니 쿠누기 씨가 안경을 고쳐쓰시고 계셨다."

    n "병원이랑 가까워서 빠르게 도착했어요."
    
    show kunugi sad with dissolve
    kunugi "몸은 좀 괜찮으신가요?"

    n "네! 지금 당장 일 해도 무리 없을정도로 건강합니다!"
    
    show kunugi nomal with dissolve
    kunugi "이상이 없다면 다행이지만, 그래도 오늘 퇴원하셨으니 가급적 조심하도록 하세요."

    kunugi "우선 이렇게 서서 이야기 하는것도 그러니 이동해서 마저 얘기나누록 하죠."

    scene background_es_in with dissolve
    with Pause(1)
    play sound "walkfoot.mp3"
    
    scene background_es_talking with dissolve 
    "쿠누기 씨를 따라 회사 회의실에 도착해 큰 테이블을 마주하고 앉았다."
    
    show kunugi no with dissolve
    kunugi "오늘은 퇴원하신지도 얼마 되지 않으셨으니 회사를 둘러보시거나 간단한 것 까지만 허용합니다."
    
    show kunugi angry with dissolve
    kunugi "이 이상은 혹시 몸이 다시 안좋아지실 수 있으니 절대 안됩니다. 무리하시는것도 안됩니다."

    n "네에..."
    
    show kunugi nomal with dissolve
    kunugi "혹시라도 몸이 안좋아지셨다면 언제든지 가셔도 좋습니다. 그러니 오늘은 휴식을 취하셨으면 합니다."
    
    kunugi "평소에도 무리하시는 경향이 있으시니 이번 기회에 한 숨 돌리시는것도 좋을꺼 같군요."

    menu:
        "잔업이라도 하면 안될까요...?":
            n "잔업이라도 하면 안될까요...?"
            jump want

        "명심하겠습니다..":
            "명심하겠습니다.."
            jump soso

label want:

    scene background_es_talking
    show kunugi angry with dissolve
    kunugi "안됩니다."
    
    show kunugi nomal with dissolve
    kunugi "...라고 제가 말씀드려도 분명 저 몰래 하실거 같으니.."

    kunugi "간단한 잔업정도까지 입니다. 이 이상은 허락할 수 없습니다."

    n "...!!!"

    n "네! 감사합니다!"
    
    scene background_es_talking with dissolve
    "다행히 잔업정도까지는 허락받았다!"
    
    show kunugi nomal with dissolve
    kunugi "정말이지...다른 사람들이라면 쉬라는 말에 화색이 돌았을텐데 당신은 오히려 기운이 없어보이시니..워커홀릭인 면이 있으셔서 좀 걱정되는군요."

    kunugi "평소에도 쉬엄쉬엄 해주세요. 그러다 몸이 다 상할지도 모릅니다."

    n "그게...하다보니 어느새 집중하게 되버려서..아하하.."
    
    kunugi "저는 집중을 길고 오래 하는 부분은 당신의 큰 장점이라고 생각합니다."

    kunugi "쉬워보일수 있지만 그건 절대 아무나 할 수 있는게 아니니깐요."

    "살짝 미소를 띄우며 쿠누기 씨가 말씀하셨다."
    
    scene background_es_talking with dissolve
    "쿠누기 씨와 얘기를 나누다보니 어느새 시간이 훌쩍 지나있었다."
    jump chapter1_1

label soso:

    scene background_es_talking
    "저 상태라면 아마 뜻을 절대 굽히지 않으실거 같아 어쩔 수 없이 순응했다."

    n "(아마 잔뜩 밀렸을텐데...어쩔 수 없지..)"
    
    show kunugi hmm with dissolve
    kunugi "네. 오늘은 절대 휴식입니다."
    
    show kunugi nomal with dissolve
    kunugi "그래도 평소라면 고집을 조금 피우셨을텐데 오늘은 알겠다고 순응해주셔서 다행이네요."

    kunugi "쉬어가는 것도 중요한 부분이니 컨디션 체크는 잊지말아주세요."

    n "하하 네에.."

    "쿠누기 씨와 얘기를 나누다 보니 어느새 시간이 훌쩍 지나있었다."
    jump chapter1_1


label chapter1_1:

    scene background_es_talking
    show kunugi no with dissolve
    kunugi "이런, 벌써 시간이..."
    
    show kunugi nomal with dissolve
    kunugi "전 선약이 있어 먼저 일어나겠습니다. 그럼...."

    n "네, 수고하세요!"

    scene background_es_in with dissolve
    with Pause(1)


    scene background_es_in with dissolve
    "쿠누기 씨와 헤어진 후 무리하지 말라는 말씀에 뭘 하면 좋을 지 고민이 된다."

    "말씀대로 회사를 둘러볼까 아니면 잔업이라도 하러 갈까?"
        
    menu:
        "회사를 둘러본다.":
            "회사를 둘러보며 시간을 보낸다."
            jump chapter1_walk
            play sound "walkfoot.mp3"

        "잔업을 하러간다.":
            "간단한 잔업이라도 처리하러 간다."
            jump chapter1_busy
            play sound "walkfoot.mp3"    

label chapter1_walk:
    scene background_es_in
    "오늘은 회사를 둘러볼까 하고 발걸음을 옮겼다."

    "여태까지 회사를 둘러볼 시간이 마땅치 않아 이번 기회에 자세히 둘러보고 싶었던 마음도 있었다."
        
    "방향도 목적지도 없이 그저 회사 내부를 걷고 있기만 했는데 왠지 모르게 마음이 편안해졌다."

    "그렇게 걷다보니 길이 두갈래로 갈렸다."

    "왼쪽은 탕비실, 오른쪽은 회사 정원으로 이어지는 계단이 있다."

    menu:
        "어느쪽으로 향할까요?"

        "휴게실":
            "휴게실로 향했다."
            jump chapter1_tsukasa
            play sound "walkfoot.mp3"

        "회사 정원":
            "회사 정원으로 향했다."
            jump chapter1_leo
            play sound "walkfoot.mp3"

label chapter1_tsukasa:
    scene background_es_self with dissolve
    "걷다보니 회사 휴게실에 도착했다."

    tsukasa "누님!"

    "뒤에서 누군가 부르는 소리가 들려 뒤를 돌아보니 붉은 머리카락을 가진 조금 앳되어보이는 남자가 서 있었다."
        
    show tsukasa nomal with dissolve
    n "아, 츠카사!"

    "츠카사는 학창시절부터 봐왔던 후배다. 지금은 가문의 당주이자 뉴디멘션이라는 회사의 소장을 맡고 있다."

    "나보다 어린데 벌써 능력도 인정받고..정말 여러모로 본받고 싶어진다."
        
    show tsukasa sad
    tsukasa "며칠간 company에 나오시지 않아 정말 걱정했습니다.. 혹시 몸이 많이 안좋으셨나요?"
        
    n "그게, 나도 설명을 해주고 싶은데.. 눈 떠보니까 병원이였어서...하하.."

    tsukasa "혹시 입원하셨던건가요??"

    tsukasa "정말 많이 아프셨나보군요... 말씀해주셨다면 병문안이라도 갔을텐데.."
        
    n "그렇게 걱정하지 않아도 돼! 오늘 퇴원하고 무리하시지 말라하셔서 지금 회사 돌아다니면서 시간 보내고 있어."
        
    show tsukasa nomal with dissolve
    tsukasa "그렇다면 다행입니다. 혹시 괜찮다면 저도 같이 다녀도 될까요?"

    "마침 혼자다니는게 슬슬 심심하다고 생각중이여서 츠카사의 제안은 정말 반가웠다."

    n "그래! 심심했는데 잘 됐다. 같이 돌아다니자."

    "츠카사와 얘기를 나누며 회사를 한참 돌아다녔다."
    scene background_white with dissolve
    with Pause(1)
    
    stop music fadeout 2.0
    jump chapter2_start
    
label chapter1_leo:
    scene background_es_tree with dissolve
    "이리저리 회사를 둘러보다가 중간층에 위치한 화단에 왔다."

    "예전에는 늘상 이곳에서 숨을 돌리고 갔는데, 최근에는 업무가 많아 그럴 시간조차 없이 바쁘게 돌아다녔다."

    "오랜만에 다시 오니 탁 틔인 공간이라 답답함도 사라지는 것만 같다."

    leo "인스피레이션!!!!!!!!!!" with hpunch

    "나무를 등대고 조금 앉아 쉴까 하던 중 나무 위에서 갑자기 큰 소리가 나더니 한 남자가 나무위에서 뛰어내렸다."

    "예쁜 주황색 머리카락에 살짝 날카로운 눈매를 가진 사람이였다."
        
    show leo wow with dissolve
    leo "어라? 지금 시간엔 나 말고 없을텐데?"
        
    show leo nomal with dissolve
    leo "어어어!!! 잘 보니까 [player_name](이)잖아!!!!"
        
    show leo happy
    leo "오랜만이야!!!! 귀국했는데 안보여서 쓸쓸했다구!!" with hpunch

    n "레...레오 씨..반가운건 알겠는데..어지럽..." with hpunch
        
    "지금 내 팔을 신나게 잡고 흔드는 사람은 레오 씨다. 학창시절때는 나보다 한 학년 선배이셨다."

    "어렸을때부터 작곡에 재능이 뛰어나셔서 학생이실때 이미 작곡으로는 유명하신분이였다."

    "졸업하시고서는 친구인 세나 씨와 함께 피렌체로 가셨는데, 얼마 전 잠시 귀국하신 모양이였다."

    n "레오 씨 나무에서는 뭐하시고 계셨던 건가요?"

    show leo nomal with dissolve
    leo "작곡하고 있었어! 이번에 들어온 의뢰가 '맑고 편안한 느낌의 곡' 이라 하늘을 보면서 작업하면 영감이 잘 떠오를 거 같아서!"

    n "하하...레오 씨는 여전하시네요"
        
    show leo sad with dissolve
    leo "그나저나 그동안 어디있었던거야!!! 많이 찾아다녔는데.."

    n "죄송해요..아마 그날 병원에 있던거 같아요."
        
    show leo wow with dissolve
    leo "병원은 왜??!!"
        
    scene background_es_tree with dissolve 
    "레오 씨에게 지금까지 있었던 일들을 정리하여 설명해주었다."

    show leo sad with dissolve 
    leo "많이 아팠던거구나.."

    leo "병문안이라도 갈껄....."

    n "앗 아니에요! 지금은 건강하니까 그렇게 걱정하시지 마세요."

    leo "그래도..."

    n "저 원래는 오늘 잔업하려고 생각할 정도로 건강에는 이상 없으니까 괜찮아요!"
        
    show leo nomal
    leo "그럼 다행이네!"

    leo "아! 맞다! 지금 시간 있다면 곡 쓴거 들을래??"

    n "그래도 괜찮나요? 좋아요!"

    scene background_white with dissolve
    "레오 씨가 쓴 노래들을 들으며 시간을 보냈다."
    stop music fadeout 2.0
    jump chapter2_start

label chapter1_busy:
    scene background_es_in
    play sound "walkfoot.mp3"
    "회사를 둘러볼까 하다가 며칠간 쌓였을거 같은 일들이 신경쓰여 잔업이라도 처리하기로 했다."

    "부서로 이동하던 중 길의 맞은편에서 누군가 부르는 소리가 들렸다."
    jump chapter1_HiMERU_kohaku
    return

label chapter1_HiMERU_kohaku:
    show kohaku nomal at rightCharacter with dissolve
    show HiMERU nomal1 at leftCharacter with dissolve
        
    "뒤를 돌아보니 물망초색의 머리를 가진 남자와, 분홍색의 머리를 가진 누가봐도 앳된 모습의 소년이 같이 서 있었다."

    n "아 HiMERU 씨랑 코하쿠구나!"

    "코하쿠는 뉴디멘션의 소장인 츠카사가 엄청 아끼는 분가 동생이다. 나이는 츠카사보다 더 어리지만 어딘가 좀 더 어른스러운 분위기가 물씬 난다."

    "그리고 옆에 코하쿠랑 같이 계시는 HiMERU 씨는 내가 이 회사에 온지 얼마 되지 않아 알게 된 사이다."

    "어른스럽고 특유의 사람을 편안하게 해주는 분위기가 있어 얘기하기 굉장히 편안한 느낌을 준다. 이 둘은 지금 코즈프로의 소속이다."

    kohaku "콧콧코, [player_name] 씨, 뭔가 오랜만에 본 것 같구려."

    HiMERU "HiMERU도 그렇게 생각합니다. 혹시 무슨 일이 있으셨나요?"

    scene background_es_in with dissolve 
    "두사람에게 여태까지 있었던 일들을 설명했다."

    show kohaku wow with dissolve
    kohaku "그게 정말인가?"

    show kohaku sad with dissolve
    kohaku "미리 알았더라면 좋았을텐데 미리 알지 못해 마안하구려."

    n "괜찮아! 지금은 멀쩡하고 코하쿠의 잘못도 없으니까 미안해하지 마."

    scene background_es_in with dissolve
    show HiMERU sad1 with dissolve
    HiMERU "[player_name] 씨의 말도 맞습니다만..HiMERU도 오우카와와 똑같이 생각하고 있습니다."

    n "난 정말 괜찮아! 오늘 퇴원할정도로 건강하니까 걱정하지 않아도 돼!"
        
    scene background_es_in
    show kohaku nomal with dissolve
    kohaku "그러고보니 [player_name] 씨는 어디가는 길인겐가?"

    n "잔업하러 가고 있었어! 며칠간 회사에 못갔으니까..아무래도 좀 걱정이 되서..두사람은?"

    kohaku "우리는 회의하러 가는 길에 잠시 시간이 좀 남아 가벼운 얘기라도 나누고 있던 참일세."
        
    show kohaku wow with dissolve
    kohaku "이런, 곧 있으면 회의 할 시간이구먼."
        
    scene background_es_in
    show kohaku nomal at rightCharacter with dissolve
    show HiMERU nomal1 at leftCharacter with dissolve
    kohaku "[player_name] 씨, 우리는 이만 회의하러 가보겠네. 잔업이라도 조금만 하고 들어가게."
        
    HiMERU "오우카와의 말에 동의합니다. [player_name] 씨는 평소에도 무리하시는 경향이 있으니 힘드시면 쉬엄쉬엄하세요."

    n "하하 고마워! 난 이만 가볼께!"
        
    scene background_es_in
    "두사람과 헤어진 후 마저 작업을 하러 갔다."

    scene background_white with dissolve
    with Pause(2)

    scene background_es_company with dissolve

    "잔업을 처리하다 시계를 보니 벌써 늦은시간이라 더 늦게 갔다간 설교를 한참 들을 꺼 같아 정리하고 집으로 갔다."
    stop music fadeout 1.0
    jump chapter2_start

label chapter2_start:
    scene background_dream with fade
    with Pause(1)

    scene background_es_talking with dissolve
    with Pause(1)
    play music "main.mp3" loop

    n "후우....."

    "퇴원한지도 벌써 몇주가 지나고, 난 평소처럼 일하고 있다."

    "오늘은 다행히 일이 많지 않아 순조롭게 처리 중이다."

    "사고 당일 날의 기억은 아직도 되찾지 못했다."

    "기억을 되찾으려고 기억을 더듬어 회사 계단으로 가도 별 소득이 없다.."
    
    n "(이 상태로 계속 누군지 모른다면 그건 그거대로 싫을지도..)"

    "머릿속에 집념이 계속 쌓여 일에 집중이 전혀 되지 않는다."

    "도저히 안 되겠다 싶어 잠시 나가서 한숨 좀 돌릴까 싶은 생각이 들었다."

    menu:
        "어디로 가시겠습니까?"

        "회사 정원":
            "회사 정원으로 한숨 돌리러 올라갔다."
            jump meet_himeru

        "계획없이 돌아다닌다":
            "계획없이 돌아다니는것도 좋을꺼 같아 복도로 나왔다."
            jump meet_leo

        "휴게실":
            "휴게실에 잠시 앉아있다가 오기로 했다."
            jump meet_kohaku

        "잠시 산책":
            "잠시 회사 근처를 좀 걷다 오기로 했다."
            jump meet_tsukasa

        "자리에서 잠시 한숨을 돌린다.":
            "어디로 가야할까 고민하다 그냥 나가지 않고 자리에서 한숨을 돌리기로 한다."
            jump meet_kunugi


label meet_himeru:
    
    stop music fadeout 2.0
    scene background_HiMERU with dissolve
    with Pause(1)
    
    play sound "walkfoot.mp3"
    scene background_es_tree with dissolve
    play music "main.mp3" loop
    n "으아....좀 살 거 같다."

    "회사 정원에 잠시 올라오니 좀 살거 같다."

    "이 상태면 집념도 좀 가실 수 있지 않을까 싶어 좀 느긋하게 있다 가기로 했다."

    "한 자리에 있는 것보단 돌아다니면서 몸을 좀 풀어주는게 더 좋을거 같아 조금 정원을 돌아다니기로 했다"

    scene background_es_tree
    with Pause(2)
    
    "어디선가 물 소리가 난다. 정원을 관리하시는 분이 주시고 계신건가 싶어 방해하지 않기 위해 다른곳으로 이동하려고 발을 돌렸다."

    HiMERU "후후, 오늘도 햇볕이 참 좋네요. 이 상태라면 분명 잘 자랄꺼 같습니다."

    "이 목소리는 분명 HiMERU 씨의 목소리다."

    "다른 곳으로 가려던 발을 다시 돌려 물을 주고 있는 HiMERU 씨에게로 향했다."

    n "HiMERU 씨?"
    
    show HiMERU nomal with dissolve
    HiMERU "음? 누구신가 했더니 [player_name] 씨군요."

    n "정원 식물들에게 늘 이렇게 물을 주고 계신 건가요?"
    
    HiMERU "네, 원래는 이곳을 관리해주는 분이 따로 계시지만, 그 분이 오늘 나오지 못하셔서 HiMERU가 대신 주고 있었습니다."

    HiMERU "[player_name] 씨께서는 휴식중에 오신 건가요?"

    n "네, 일에 집중이 안돼서 잠시 한 숨 돌리러 왔어요."

    n "여기는 올때마다 식물이 많아서 참 좋아요."
    
    show HiMERU happy with dissolve
    HiMERU "HiMERU도 그렇게 생각합니다. 이렇게나 종류가 많은데 관리를 하나하나 잘 해놓으셔서 늘 꽃들의 색깔이 좋습니다."

    scene background_es_tree with dissolve 
    "그 말에 둘러보니 정말 많은 종류의 꽃들이 있었다. 이 많은걸 다 관리하시다니 대단한 분이신거 같다."
    
    show HiMERU nomal with dissolve
    HiMERU "여기는 다 됐으니 이제 다른 구역에 물을 주러 가야겠군요."

    n "저 HiMERU 씨!"
    
    HiMERU "무슨 일이신가요?"

    n "물 주는거 도와드려도 될까요?"
    
    "정원에서 꽃을 보고 있으니 HiMERU 씨를 도와 같이 물을 주고 싶어졌다."
    
    show HiMERU happy with dissolve
    HiMERU "후후, 좋습니다. 이곳의 물 호스는 수압이 센 편이니 옷이 젖지 않게 조심하세요."

    scene background_white with fade
    "HiMERU 씨를 도와 물을 주다보니 꽃들에게 집중할 수 있어 자연스래 머릿속의 집념도 사라졌다."
    stop music fadeout 2.0                  
    jump HiMERU_date

label meet_leo:
    stop music fadeout 2.0
    scene background_leo with dissolve
    with Pause(1)
    
    play music "main.mp3" loop
    scene background_es_in
    n "으으으.....!!!"

    "복도로 나와 기지개를 한번 하니 몸이 좀 풀리는 거 같다."

    "우선 근처라도 좀 돌아다녀볼까 싶어 방향없이 그저 걸어다녔다."

    "회사를 둘러보며 돌아다니고 있는데 벽에 웬 낙서 같은게 있었다."

    n "(누가 회사벽에다 낙서를 해놨지?)"

    n "(어라, 이건....설마 악보?)"

    "자세히 들여다보니 낙서들은 악보인거 같았다."
    
    play sound "walkfoot.mp3"
    "회사에 이런짓을 할 사람은 딱 한사람밖에 없어서 한숨을 짧게 내쉰 후 낙서를 따라갔다."

    "낙서를 따라가자 역시나 그곳에는 레오 씨가 있었다."

    n "레오 씨!"
    
    show leo nomal with dissolve
    leo "오? [player_name] !!"
    
    n "회사 벽에다 악보를 쓰시면 어떡해요! 그런건 종이에다가 해주세요!"
    
    show leo sad with dissolve
    leo "그치마안....종이가 없는걸!!!"

    leo "모처럼 인스피레이션이 떠올랐는데 안 써놓는건 아깝잖아!"

    n "제가 종이 금방 구해다 드릴 테니까 잠시만 기다려주세요!!"

    scene background_es_talking with fade
    n "음....이정도면 충분하시려나?"

    "레오 씨에게 드릴 이면지를 급하게 모았다."

    "다행히 이면지를 깜빡하고 안버려둔게 있어서 꽤나 많은 양의 이면지들이 모였다."

    "모은 이면지들을 잘 정돈해 품에 안고 레오 씨에게 갔다."

    scene background_es_in with dissolve
    "레오 씨가 계신곳으로 가니 다행히 악보를 더 그리시진 않으신거 같다."

    n "레오 씨! 이면지이긴한데 이거라도 쓰세요."

    show leo nomal with dissolve
    "오! 꽤 종이가 많네!!"

    show leo happy with dissolve
    "고마워! 그럼 이제 여기에 적을께!"
    
    scene background_es_in with dissolve
    "그렇게 말씀하시더니 정말 바로 악보를 쓰신다."

    "몇분 안 지난거 같은데 벌써 한페이지의 악보를 완성했다."

    n "레오 씨는 정말 대단하시네요..몇분 안 지난거 같은데 벌써 악보를..."
     
    show leo happy with dissolve 
    leo "와하하! 머릿속에 인스피만 있으면 몇장이든 쓸 수 있어!"

    "그렇게 말씀하더니 어느새 노래 한곡 분량의 악보를 만들어냈다."
    
    show leo very happy with dissolve
    leo "완성됐다!!! 세기의 역작이!!!!" with hpunch

    leo "모차르트랑 베토벤도 부러워할꺼야!!"
    
    n "와아, 벌써 노래 한곡을...정말 대단하세요!"

    n "앗, 저는 이제 슬슬 가봐야 할 거 같아서...먼저 가볼께요."
    
    scene background_es_in with dissolve
    "레오 씨가 작곡하는걸 보다가 그만 예정했던 시간을 넘어버렸다."

    "인사를 드리고 다시 회사부서로 돌아가려고 하는데 레오 씨가 내 소매를 붙잡았다."
    
    show leo nomal with dissolve
    leo "저기, 가기전에 방금 만든 노래 듣고 가!"

    n "그게...일이.."
    
    show leo happy with dissolve
    leo "응?"
    
    n "....노래 한 곡 정도면 괜찮을꺼 같아요!"

    scene background_es_in with dissolve
    "일 때문에 거절하고 들어가보려 했는데 웃는 모습에 그만 노래를 듣고 가기로 했다."

    scene background_white with fade
    "레오 씨 옆에 앉아 레오 씨가 만든 곡을 들었다."

    "그 노래는 어딘가 애정이 느껴지는, 마치 짝사랑을 자각하지 못한것 같은 순수한 감정이 담겨있는 노래였다."
    stop music fadeout 2.0
    jump leo_date

label meet_kohaku:

    scene background_kohaku with dissolve
    with Pause(1)
     
    scene background_es_self with dissolve
    "커피머신에 커피를 내려 휴게실 내에 있는 소파에 앉았다."

    "따뜻한 커피를 마시며 있으니 몸이 노곤노곤해진다."

    show kohaku nomal with dissolve 
    kohaku "누가 있는거 같아보였네만 [player_name] 씨가 있었구려?"

    n "코하쿠!"

    n "여기 잠시 쉬러 온거야?"

    kohaku "그렇다네, 방금 전까지 바빴으니 잠시 머리도 식힐겸 온것일세. [player_name] 씨돈가?"

    n "응, 일에 집중이 좀 안되서...잠시 한 숨 돌리려고 왔어."

    kohaku "그렇구먼. 일이 안풀릴 때는 잠시 쉬는게 더 나은 법일세. 잘 선택했구려."
    
    kohaku "아, 마침 쉬는김에 같이 먹을까 싶어 다과를 챙겨왔는데, [player_name] 씨도 같이 들게나."

    n "그래도 괜찮아?"
    
    kohaku "물론, 아직 먹어보진 않았지만 특히나 이번껀 무척 맛있다고 도련님이 눈을 빛낼정도였으니...아마 맛은 보증일걸세."
    
    scene background_es_self with dissolve
    "그렇게 말하더니 코하쿠는 가져온 상자를 열었다."

    "상자를 열자 그 안에는 예쁜 모양의 한눈에 봐도 정말 맛있어보이는 과자들이 들어있었다."

    n "와아...엄청 예쁘다.."
    
    show kohaku nomal with dissolve
    kohaku "콧콧코, 도련님의 안목도 꽤나 나쁘진 않아보이는구려. 물론 중요한건 맛이네만."
    
    scene background_es_self with dissolve
    "상자에서 과자를 하나 꺼내었다."

    "외관이 너무 예뻐 먹기 아까웠지만, 맛있는 냄새가 나 참지 못하고 한입 베어물었다."


    n "!!!!!!!!"

    "과자의 맛은 정말 훌륭했다. 재료를 좋은걸 썼는지 버터랑 바닐라의 맛이 정말 고급스럽고, 무엇보다 딱 적절한 단맛이라 기분을 좋게 만들어줬다."

    n "이거 진짜 맛있다..."
    
    show kohaku happy with dissolve
    kohaku "도련님이 왜 그렇게 눈을 빛내며 말했는지 알거 같네. 꽤나 잘만든 과자구려."
    
    scene background_es_self with dissolve
    "그렇게 같이 다과를 즐기다 코하쿠가 말했다."
    
    show kohaku nomal with dissolve
    kohaku "그러보니 [player_name] 씨와 이렇게 단 둘이 즐기는건 처음인거같구려."

    n "음? 그런가?"

    kohaku "아마 그럴걸세. 만나도 HiMERU 항과 같이 만나거나 도련님과 같이 만났으니."

    kohaku "이렇게 둘이서 즐기는것도 좋구려."

    n "그러게, 코하쿠랑 단둘이 있으니까 뭔가 좀 진정되는 느낌인거 같아."

    n "다음부턴 코하쿠랑 종종 만날까봐. 오늘은 코하쿠가 다과를 가져왔으니까 다음엔 내가 들고오는걸로!"
    
    show kohaku happy with dissolve
    kohaku "그런것이라면 언제든지 환영일세. 다과, 기대하고 있겠네."

    scene background_white with fade
    "코하쿠랑 탕비실에서 느긋하게 있으며 도란도란 얘기를 나누다 들어갔다."

    "신기하게도 일하는동안 불필요한 집념들이 다시 생각나는 일 없이 무탈하게 서류를 처리했다."
    stop music fadeout 2.0
    jump kohaku_date


label meet_tsukasa:
    
    scene background_tsukasa with dissolve
    with Pause(1)
    
    scene background_es_off with dissolve
    "회사 밖을 나와 바람을 쐬니 기분이 좋아진다."

    "우선 근처 상점가라도 돌아다녀볼까 싶어 발걸음을 옮겼다."

    scene background_moring_walk with dissolve
    "상점가로 나오니 여러 가게들과 노점들도 보인다."

    "그러고보니 일이 바빠 상점가에 온 것도 꽤나 오랜만이였다."

    "예전하고 크게 달라진 모습은 없었지만, 못 보던 가게들이 눈에 보인다."

    "그러다 분위기가 꽤 좋아보이는 카페를 발견했다."

    n "(분위기 좋아보이는데 잠시 쉬었다 갈까?)"
    
    scene background_walk_caffe with dissolve
    "카페 안으로 들어가니 더 분위기가 좋았다."

    "카페 주인분이 꽃들을 좋아하시는지 주변에 꽃들이 굉장히 많아 싱그러운 분위기를 준다."

    "음료수를 주문하고 자리에 앉으려는데 근처에서 많이 익숙한 적색의 머리가 보였다."
    
    show tsukasa dessert with dissolve
    tsukasa "(여기의 Dessert는 언제 봐도 정말 맛있어보이는군요.)"
    
    show tsukasa nomal with dissolve
    tsukasa "(오늘은 평소와 조금 다른 Cake를 시켜보았습니다...이곳의 시그니처 메뉴라고 하는데..먹어보지 못한 맛이라 궁금하군요..)"
    
    show tsukasa happy
    tsukasa "(후후..그럼 한입-)" 

    n "츠카사?"
    
    show tsukasa wow
    tsukasa "누.....누님??!!" with hpunch

    "아무래도 쉬는데 방해를 해버린걸까 싶었다."

    n "미안....괜히 불렀나? 뒷모습이 보여서 그만..."

    tsukasa "아뇨! 괜찮습니다."
    
    show tsukasa nomal with dissolve
    tsukasa "괜찮으시다면 저도 혼자 왔는데 같이 합석하시겠습니까?"

    scene background_walk_caffe with dissolve 
    "츠카사랑 자리를 합석했다."

    "츠카사 앞에는 케이크랑 라떼가 있다."
 
    n "여기에는 잠시 쉬러 온거야?"
   
    show tsukasa nomal with dissolve
    tsukasa "네, 이곳에서만 파는 시그니처 Cake를 먹으러 왔습니다. 누님도 드시러 오신건가요?"

    n "아니, 난 잠시 돌아다니다가 분위기 좋아보여서 들어왔어."

    tsukasa "확실히 여기 카페 분위기는 쉬었다 가기엔 정말 좋은거 같습니다."

    tsukasa "꽃들과 식물이 많아 눈도 편하고요."

    n "그러게, 이런 좋은곳을 발견해서 기분이 좋은걸."

    "도란도란 가벼운 얘기를 나누며 음료를 즐기니 방금전까지 방해했던 집념들이 금방 정리된다."
    
    show tsukasa happy with dissolve
    tsukasa "으음!! 이 시그니처 Cake 정말 맛있습니다! 이곳의 시그니처인데는 이유가 있는 맛이군요!"

    "츠카사는 이곳의 시그니처 케이크가 맛있는지 내 앞에서 귀엽게 우물거리며 열심히 먹고 있다."

    "그 모습을 보니 예전 학창시절때의 츠카사가 떠올라 괜히 웃음이 나왔다."
    
    show tsukasa hmm with dissolve
    tsukasa "누님, 왜그러신가요? 제 얼굴에 뭔가 묻었나요?"

    n "후후 아니, 츠카사는 예전이나 지금이나 한결같은거 같아서"
    
    show tsukasa near
    tsukasa "아닙니다!" with hpunch
    
    tsukasa "저도 이제 어엿한 사회인입니다! 물론 외형은 달라지지 않았을지도 모르지만...나름 어른이라는 티가 날껍니다!"

    n "후후, 그래? 하지만 내 눈앞에서 열심히 케이크를 먹고 있는 츠카사는 예나 지금이나 똑같은걸?"
    
    show tsukasa sad
    tsukasa "누님...!!!" with hpunch
    
    scene background_walk_caffe with dissolve
    "츠카사와 장난치며 있으니 마치 예전의 학생시절로 돌아간 듯한 반가운 느낌이 들었다."

    scene background_white with fade
    "그렇게 즐겁게 얘기를 나눴던건 간만이라 다시 회사로 갔을때 남은 일들은 순조롭게 끝낼 수 있었다."
    stop music fadeout 2.0
    jump tsukasa_date



label meet_kunugi:
    
    scene background_kunugi with dissolve
    with Pause(1)

    scene background_es_talking with dissolve
    "가만히 앉아 잠시 멍때리고 있으니 뭔가 무기력해진 기분이 든다."

    "오히려 밖에 나가는게 더 나았을거 같다는 생각도 잠시 들었지만 몸이 피곤한건지 움직일 생각조차 들지 않았다."
    
    scene background_es_talking
    with Pause(2)

    "핸드폰에서 알림이 울렸다."

    "핸드폰을 들어 알림을 확인해보니 쿠누기 씨에게 문자가 와 있었다."

    kunugi "(쿠누기입니다. 잠시 시간 괜찮으시다면 같이 밖에 나갔다 오시지 않겠습니까?)"

    "무기력해져서 가만히 있는 것 보단 움직이는게 집념을 떨쳐내는데에도 도움이 되지 않을까..라는 생각이 들었다."

    n "(좋아요, 어디에서 만날까요?)"

    kunugi "(1층에서 뵈죠. 그럼 준비하시고 오세요.)"

    "신기하게도 방금전까지 움직일 생각을 하지 않던 몸이 다시 잘 움직여졌다."

    "잠시 나갔다 오는거니 가볍게 짐을 챙기고 1층으로 내려갔다."

    scene background_es_in1 with dissolve

    "1층으로 내려가니 쿠누기 씨께서 기다리고계셨다."

    n "쿠누기 씨!!"

    n "많이 기다리셨나요??"
    
    show kunugi nomal with dissolve
    kunugi "이 근처에서 일이 있었어서 먼저 기다리고 있었으니 얼마 기다리지 않았습니다. 가실까요?"
    
    scene background_es_in1
    "주변을 돌아다니기 전, 잠시 카페에 들렀다."
    
    scene background_caffe_lite with dissolve
    show kunugi nomal with dissolve
    kunugi "전 아메리카노 할 건데, [player_name] 씨는 뭘로 하시겠어요?"

    n "음...저는 초코라떼로요!"

    n "평소에 많이 신세를 졌으니까 음료는 제가 살께요!"

    kunugi "아닙니다. 오늘 저와 같이 동행해주시니 음료 정도는 제가 사겠습니다."

    "평소에 신세를 많이 지기도 해서 음료는 사고 싶었는데 쿠누기 씨께서 사주셨다."

    "다음에라도 기회가 있다면 꼭 내가 사드려야지.."

    scene background_park with dissolve
    "쿠누기 씨가 사주신 음료를 들고 가니 못본 곳에 예쁜 공원이 있었다."

    n "와아...공원이 엄청 예쁘네요..!"
    
    show kunugi nomal with dissolve
    kunugi "일하다가 발견한 곳입니다. 생긴지 얼마 안된 곳인지 깨끗하고 관리도 잘 되어있더군요."

    kunugi "여기를 좀 돌아다닙시다."
    
    scene background_park with dissolve
    "쿠누기 씨가 데려다 주신 공원은 둘러보면 둘러볼 수록 정말 잘 꾸며져 있었다."

    "나무들도 많고, 화단도 예쁘게 잘 가꾸어져 있었다."

    n "날씨가 정말 좋네요. 나오니까 숨도 틔이고 기분이 좋아지네요."

    n "아, 그런데 조금 무기력해질지도요."
    
    show kunugi no with dissolve
    kunugi "일기예보를 보니 앞으로 며칠간은 비 소식이 없다고 하더군요."
    
    show kunugi nomal with dissolve
    kunugi "확실히 이렇게나 날씨가 좋으니 저도 무기력해질꺼 같네요."

    "쿠누기 씨가 하신 말씀에 실례지만 정말 의외라고 생각했다. 늘 힘든 모습을 전혀 보이시지 않아서 문득 무기력 하실수도 있다는 생각을 차마 하지 못했던거 같다."
    
    kunugi "....무슨 생각하시는지 눈에 보입니다만, 아무리 저라도 무기력함은 느낍니다."

    n "늘상 피곤하다거나 힘드신 기색은 전혀 하시지 않으셔서 그만..."

    kunugi "겉으로는 내색하지 않으려고 하는 편입니다. 제가 힘든 얼굴을 보이면 다른 이들의 사기가 떨어질지도 모르니깐요."

    kunugi "그러니 다른사람이 그러더라도 저만은 그러지 않으려고 합니다."
    
    scene background_park with dissolve
    "그 말을 들으니 힘든 기색을 전혀 보이시지 않는 쿠누기 씨의 모습에 힘들어도 몇번이고 다시 힘내서 이겨냈었던 기억들이 떠올랐다."

    n "쿠누기 씨의 그 모습 덕분에 마음가짐을 탄탄히 해서 이겨낸적이 정말 많았거든요."

    n "아마 저 뿐만이 아니라 다른분들도 그러셨을꺼에요. 감사해요 쿠누기 씨."
    
    show kunugi nomal with dissolve
    kunugi "그렇게 말씀해주시니 저야말로 감사할 따름입니다."  
    
    scene background_white with fade
    "쿠누기 씨와 함께 얘기를 나누며 걸으니 불필요한 생각들이 모두 정리되어 머릿속이 가벼워졌다."
    stop music fadeout 2.0
    jump kunugi_date

label leo_date:
    scene background_leo with dissolve
    with Pause(1)
    
    scene background_home with dissolve
    with Pause(1)
    play music "main.mp3" loop
    play sound "Phone.mp3"

    n "으음....."

    n "이 시간에 누구.....? 레오 씨?"

    "아침부터 레오 씨가 전화를 거셨다."
    
    "혹시 급한 일이라 지금 전화하신건가 싶어 아직 잠이 덜 깨 잠긴 목소리를 겨우 풀고 전화를 걸었다."

    n "네에...[player_name] 입니다.."

    leo "[player_name]! 우리 놀러 가자!"

    "아침 일찍이라고는 믿기지 않을 정도로 활기찬 목소리로 말했다."

    leo "이번 주 일요일에 가을의 마지막으로 축제를 연대!!!!"

    n "축제...?"

    "달력에서 날짜를 확인해보니 오늘이였다."

    "오늘은 오후 3시쯤에 미팅이 잡혀 있어서 갈 수 있을지 고민을 하다가 축제 시간을 확인해보니 잘만 맞추면 촉박하게 갈 수 있을것 같다."

    n "시간 괜찮을 거 같아요."

    leo "정말??? 그럼 5시에 보자!!!"

    "볼일이 끝났는지 냅다 전화를 끊어버렸다."

    "지금이 몇 시인가 싶어 시계를 확인해보니 7시 10분이였다."

    n "(아무리 아침이여도 너무 이른 시간 아닌가....? 도대체 몇 시에 일어나시는 거지..)"

    "기지개를 피고 옆에서 먼저 일어나 야옹거리며 기다리고 있던 도도의 머리를 쓰다듬어 주며 자리에서 일어났다."

    "갑자기 정해진거지만, 여하튼 축제에 가기로 했으니 옷을 어쩌면 좋을지 고민했다."

    menu:
        "오늘 축제에 무슨 옷을 입고 갈까?"

        "축제의상":
            "축제의상"
            jump yukata

        "평범한 사복":
            "평범한 사복"
            return    
    
label yukata:
    scene background_home
    n "(축제니까....이거 입고 가야겠다.)"

    "옷을 잘 챙겨두고, 간단하게 토스트와 핫초코로 아침을 먹었다."

    "아침을 다 먹고 쇼파에 잠시 앉아 축제에서 뭘 하면 좋을지 생각을 했다."

    n "(잠깐...이거 완전 데이트잖아..!!)"

    "그렇게 생각하자 갑자기 얼굴이 붉어졌다."

    "다가와서 내 발 근처에서 야옹거리는 도도를 안아 올려 마치 레오인거 마냥 장난스럽게 말을 걸며 한 숨을 내쉬었다."

    scene background_home
    with Pause(1)

    scene background_moring_walk with dissolve
    with Pause(1)
    
    "3시간 후.."

    n "(흐아....성공적으로 미팅이 잘 끝나서 다행이야..!!)"

    n "(잘 끝났으니 기념으로 딸기 스무디라도 한 잔 마셔야지!)"

    scene background_caffe with dissolve
    play sound "bell.mp3"
    show tsukasa wow with dissolve
    tsukasa "누님?"

    n "츠카사!"
    
    show tsukasa nomal with dissolve
    tsukasa "여기에서 뵙다니...오늘은 여기로 오길 잘 한거 같군요."

    tsukasa "drink는 제가 사 드릴테니 먼저 가서 앉아계세요."

    n "그럴 필요까진 없는데..."

    tsukasa "제가 사드리고 싶어 그런거니 너무 부담가지신 말아주세요."
    
    n "고마워, 그럼 먼저 앉아있을께!"
    
    scene background_caffe with dissolve
    n "(축제까지 얼마나 남았지...올해 처음 가는 축제라 더 기대되네..)"
    
    show tsukasa nomal with dissolve
    tsukasa "누님, 오늘 무슨 좋은 일이라도 있으셨나요?"

    n "그게, 오늘 저녁에 하는 가을 마지막 축제에 레오 씨랑 같이 가게 되어서 기대 돼!"

    tsukasa "후후, 레오 씨와 데이트라니 상당히 재미있네요."

    n "데이트라니...! 그런거 아니야!!"
    
    show tsukasa sad with dissolve
    tsukasa "그런데 누님, 레오 씨한테 듣기로는 오후 5시에 뵙기로 하셨다는데...시간이 꽤 타이트 한거 같습니다만..."

    "츠카사의 말에 시계를 확인해보니 약속시간까지 10분도 채 남지 않았다."

    n "큰일났다...! 츠카사 나 가봐야할 거 같아, 먼저 가볼께!!"
    
    stop music fadeout 2.0
    show tsukasa happy with dissolve
    tsukasa "축제 잘 즐기고 오세요 누님!"

    scene background_matsuri with dissolve
    with Pause(1)
    play music "timess.mp3" loop

    "축제 입구에 도착하니 레오 씨가 먼저 도착하셨는지 기다리고 계셨다."

    n "레오 씨! 많이 기다리셨어요?"
    
    show leo sad with dissolve
    "레오의 얼굴을 보니 많이 삐진것 같은 얼굴이였다."

    "시간을 확인하니 늦지도 않았는데 왜 그러시는지 알 수가 없었다."
    
    leo "아까 왜 스오랑 같이 있었어!!"
    
    "갑자기 성큼 다가와 두 눈을 똑바로 바라보며 여쭤보셨다. 별 얘기 나누지 않았는데.."

    n "방금은 카페에서 우연히 만나 잠시 얘기 나눈거에요. 절대 사적인 일로 만난게 아니에요!"

    show leo hmm 
    leo "흐음.....그래?"
    
    show leo nomal with dissolve
    leo "그럼 됐어! 일단 급하니까 빨리 따라와줘!!"
    
    n "잠시만요 레오 씨! 저 잠시 옷만 좀 갈아입고 올께요!"
    
    scene background_matsuri with dissolve
    "주변을 둘러보니 따로 옷을 입을 수 있는 장소가 마련되어 있어 그곳에서 집에서 따로 가져온 축제 의상을 입었다. 간만의 축제니 머리도 올려봤다."

    n "다 입었어요!"
    
    show leo very happy with dissolve
    leo "좋아 빨리 가자!!!!!"

    "레오 씨는 아직 축제도 시작하지 않았는데 뭔가 급하신거 같았다."

    n "레오 씨!! 아직 축제도 시작하지도 않았는데 왜 그렇게 서두르시는 거에요??"

    leo "폭탄야끼!!!!!" with hpunch
    
    scene background_matsuri with dissolve
    "몇번 더 여쭤봐도 레오 씨는 그저 폭탄야끼만 외치실 뿐이였다."

    n "(그렇게 폭탄야끼가 드시고 싶으셨나...?)"

    "같이 따라 올라가자 레오 씨가 간 곳은 주인이 없어 보이는 노점이였다."
    
    scene 5 with fade
    leo "시작하자!!"

    "레오 씨한테 이게 무슨 상황인지 여쭤 볼 겨를도 없이 갑자기 시작하신다며 나에게 앞치마를 주시더니 일을 시작하신다."
    
    stop music fadeout 2.0
    n "(뭐야 우리가 만드는거였어??!!)"
    
    play music "zigul.mp3"
    "잠시 생각할 시간도 없이 바쁘게 일을 시작했다.."
    
    leo "축제 때 노점 내서 장사 해보는거 한번 쯤 해보고 싶었거든!! [player_name](이)(가) 같이 와줘서 정말 다행이야!! 같이 하는게 더 좋을거 같아서!!"
    stop music fadeout 2.0

    play music "woowoo.mp3"
    scene background_matsuri with dissolve
    "그렇게 얼렁뚱땅 노점을 시작해버린 우리는 가을 마지막 축제인 만큼 정말 많은 인파가 몰렸고, 바쁘게 장사를 했다."
    stop music fadeout 2.0

    "축제가 막바지로 접어들었을 때 즈음, 검은 밤하늘에 반짝거리는 빛들이 터지는 소리가 들렸다."

    n "우와! 불꽃놀이다!!"

    "축제 막바지에 불꽃놀이가 시작해, 예쁜 불꽃들을 레오 씨와 함께 바라봤다."
    
    "불꽃놀이를 마지막으로 축제도 점점 끝나가고 있어 좀 더 길었으면 하는 아쉬움이 남았다."

    "생각해보니, 모처럼의 축제에 폭탄야끼를 만드느라 축제를 제댜로 즐기지도 못했다."

    n "(그래도 데이트라고 생각해서 나름 준비했는데...일이나 시키고..)"

    "나름 잘 보이고 싶은 마음에 의상까지 꺼내입었는데, 한번 쯤은 예쁘다고 말해줄수도 있지 않나..라는 생각이 들었다."

    stop music fadeout 2.0 
    "노점을 다 정리하고, 사람이 빠져나간 길거리를 레오 씨와 둘이 조용히 걸으며 가고 있었다."
    
    scene background_night_matsuri with dissolve
    show leo very happy with dissolve
    play music "after.mp3" fadein 2.0 loop
    leo "와하핫!! 오늘 지인짜 재미있었어!!"

    "기대하고 나왔던 내 상상처럼 멋진 데이트는 아니였지만, 어린아이 같은 레오 씨의 신나보이는 미소를 보니 차마 불평을 내뱉을 순 없었다."

    n "저도 재미있었어요."
    
    show leo nomal with dissolve
    leo "오늘은 시간이 많이 늦었으니깐 내가 데려다줄께!"
    
    scene background_night_000 with dissolve
    "그렇게 레오 씨의 차를 얻어타고 어두운 밤 도로를 달리는 걸 그저 멍 때리며 가다보니 어느 새 집 근처까지 금방 도착했다."
    
    scene background_night_000
    with Pause(1)


    scene background_night_home_walk with dissolve
    n "오늘은 재밌었어요. 내일 회사에서 뵈요!"
    
    show leo hmm with dissolve
    leo "잠시만,"
    stop music fadeout 2.0
    
    scene background_night_home_walk with dissolve
    "차가 완전히 멈춘 후 내릴 준비를 하고 있는데 레오 씨가 불렀다."

    "그러더니 갑자기 내 위로 다가왔다."

    n "(.......??!!)"

    "당황한 나머지 눈을 질끈 감아버렸다."

    "의자가 뒤로 넘어갔다."

    n "으앗!! 뭐 하는 거에요 레오 씨!!"
    
    "레오 씨는 잠시 아무런 말 없이 그저 한참동안 쳐다보시다 말을 꺼내셨다."
    
    play music "main.mp3" loop
    show leo hmm with dissolve
    leo "...음"
    
    show leo happy with dissolve 
    leo "아! 실수야~ 잘못 눌렀나 봐!"

    "레오 씨의 눈에는 장난끼가 가득해 보였다."
    
    scene background_night_home_walk with dissolve

    "얼굴이 빨개지다 못해 터져버릴껏만 같았던 나는 그만 심통이 났다."

    "열심히 손 부채질을 하면서 고개를 돌린 후 얼른 나가려고 했다."

    n "???"
    
    stop music fadeout 2.0
    show leo hmm with dissolve
    leo "다음에는 장난 따위 없으니깐. 각오해 둬?"

    "갑자기 내 손을 붙잡은 레오 씨는 방금 전 까지 장난기 가득한 눈은 어디로 간 건지 진지한 표정으로 말씀하셨다."
    
    show leo very happy with dissolve
    leo "오늘 정~말 예뻤어 [player_name]! 내일 보자 잘 자!"
    
    scene background_night_home_walk with dissolve
    "인사를 건넨 후 그대로 가버렸다."

    n "참 빨리도 말씀해주시네요.."

    "하지만 오늘 꾸미고 만나러 가길 정말 잘했다는 생각이 들었다."
    stop music fadeout 2.0

    scene background_white
    "5번 갤러리가 해금되었습니다."
    jump happyending_leo      



label kohaku_date:
    scene background_kohaku with dissolve
    with Pause(1)
    
    play music "main.mp3" loop
    scene background_home with dissolve
    "주말 아침, 오늘은 일에 치이는 일 없이 휴일을 만끽하고 있는데 고등학교 친구에게 전화가 왔다."

    n "여보세요?"

    f "[player_name]! 조금 이따가 1시에 번화가에서 만나지 않을래? 줄 것도 있고 오랜만에 만나는거니까 밥 한끼 살께!!"

    "그렇게 얼떨결에 약속을 잡아버렸다."

    n "(오늘은 집에서 쉬고 싶었는데~ 그래도 오랜만에 만나는거니깐!)"

    "시계를 보니 2시간 정도 남아 서둘러 샤워를 했다."

    "준비를 얼추 끝내고 서둘러 만나기로 한 약속장소로 갔다."

    scene background_sakura with dissolve
    with Pause(1)
    
    f "[player_name]~!!"

    n "많이 기다렸어??"

    f "전혀! 나도 방금 왔어~"

    f "오늘 삼거리에 있는 카페에 새로운 음료가 나왔대! 벚꽃 음료라는데 먹으러 가자!!"

    n "와아, 좋아!"

    "친구를 따라 카페로 향했다."
    
    play sound "bell.mp3"
    scene background_caffe_lite with dissolve
    n "(요새 한창 벚꽃이 피는 시즌이라 그런가 벚꽃들이 유난히 많이 보이네)"

    "새로 나왔다는 음료를 시키고 자리에 앉아 바깥의 벚꽃들을 구경하고 있는데 벚꽃의 색을 머금은 머리카락을 가진 사람이 지나가는것이 보였다."
    
    scene background_sakura with dissolve
    show kohaku hmm with dissolve
    n "저건 코하쿠..?"

    scene background_caffe_lite with dissolve
    f "야~ 길거리가 벚꽃 천진데, 벚꽃도 돌아다니는거야?"

    "친구도 놀라며 같이 창밖을 바라보다 갑자기 의미심장한 미소를 지었다."

    f "나 갑자기 약속이 생겨서 가봐야 할 거 같아!"

    n "뭐라고?"
    
    scene background_sakura with dissolve
    "일이 생겼다고 갑자기 뛰어나간 친구는 지나가던 코하쿠를 붙잡고 내가 앉아 있는 자리를 가리켰다."

    n "...엣...나..???!!"

    "친구는 엄지 척하는 사인을 날리더니 유유히 사라졌다.."
    
    "놀라는 나를 보더니 바로 카페로 코하쿠가 들어왔다."
    
    scene background_caffe_lite with dissolve
    show kohaku wow with dissolve
    kohaku "그...[player_name] 안녕한가.."

    n "으..응! 음료라도 마실래?"
    
    show kohaku nomal with dissolve
    kohaku "음료는 마신지 얼마 되지 않았으니 거절하겠네."

    n "그럼 그..할 것도 없는데 어디 놀러가지 않을래?"

    "이 때가 기회라고 생각해 자연스럽게 데이트 신청을 건넸다."
    
    show kohaku happy with dissolve
    kohaku "콧콧코, 좋구려."
    
    scene background_sakura with dissolve
    "남은 음료를 서둘러 마시고 같이 카페에서 나왔다."

    n "코하쿠, 어디 가고 싶은 곳이라도 있어?"
    
    show kohaku nomal with dissolve
    kohaku "난 이런곳은 잘 모르는지라..[player_name]이 가고 싶은 곳이라면 다 좋다네."

    "그 말에 어디를 가야 코하쿠도 즐겁게 즐길 수 있을지 고민에 휩싸였다."

    "고민을 하던 도중 근처의 3층 높이의 오락실이 눈에 들어왔다."

    n "오락실 가자!"
    
    scene background_playroom with dissolve
    n "뭐 할까?"
    
    show kohaku hmm with dissolve
    kohaku "뭔가 여러가지로 많아서 고민되는구려.."
    
    scene background_playroom with dissolve
    with Pause(1)

    show kohaku love with dissolve
    kohaku "[player_name], 저걸 해보고 싶구려!"

    "코하쿠가 고른건 가장 흔한 뽑기 머신이였다."

    "반짝거리는 눈으로 권유하는 코하쿠가 너무 귀여워서 돈을 버릴 걸 알면서도 거절 할 수가 없었다."

    n "딱 두번만이야..!"

    "내 말에 코하쿠는 기뻐하며 인형을 뽑으러 갔다."
    
    show kohaku nomal with dissolve
    kohaku "이건 어디로 결제를 하는 것인가?"

    "오락실에 처음 와서 현금으로 하는 것을 몰랐던 모양이다."

    n "그건 현금으로 해야 돼."

    "그러자 놀란 표정으로 날 바라보더니 이내 실망한 듯 돌아서서 가려고 한다."

    n "코하쿠! 왜 그냥 가??"
    
    show kohaku sad with dissolve
    kohaku "카드는 있네만...현금으로 해야하는지 몰랐구먼...어쩔수 없제..."
    
    menu:
        "코하쿠에게 현금을 건네줄까?"

        "코하쿠에게 현금을 건네준다":
            "코하쿠에게 현금을 건네주었다."
            jump money

        "코하쿠에게 현금을 건네주지 않는다":
            "코하쿠에게 현금을 건네주지 않았다."
            return


label money:
    $ persistent.ending2 = True
    $ renpy.save_persistent()

    scene background_playroom with dissolve
    "잔뜩 실망한 코하쿠에게 현금을 건네주었다."

    "그 결과 단 두번만에 인형을 뽑아 나에게 건네주었다."

    n "...!!! 내가 받아도 돼?"
    
    show kohaku happy with dissolve
    kohaku "물론, 내는 이런것에 관심이 없는지라 [player_name]이 가지게."

    n "와아, 고마워!"

    "귀여운 핑크 색의 고양이 인형이였다."

    "순간, 코하쿠를 닮았다고 생각 해 인형의 이마에 살포시 입을 가져가 댔다."

    kohaku "콧콧코~ 그렇게 마음에 들었다니 다행이구려."

    scene background_playroom with dissolve
    "다시 돌아다니기 시작한 우리는 멀리 상품이 걸린 펀치기계에 관심을 가졌다."

    n "(저거 해보고 싶었는데...)"
    
    show kohaku hmm with dissolve
    kohaku "...."
    
    show kohaku nomal with dissolve
    kohaku "[player_name] 저거 하러 가봅세."
    
    scene background_playroom with dissolve
    "나의 티 나는 눈빛을 느낀건지 펀치기계를 하러 가자고 말해주었다."

    "기계에 붙어있는 종이가 보여 읽어보니 1000점수를 낸 사람에게 오락실에 있는 인형 중 가장 크고 비싼 인형을 증정한다고 쓰여있었다."

    "생각 해 보니 아까 입구에서 엄청나게 큰 인형을 본 것 같기도 하다.."
 
    "사실은 그 인형을 가지고 싶은것도 있었다."
    
    show kohaku nomal with dissolve
    kohaku "혹시 인형 가지고 싶은가?"

    n "응..."
    
    scene background_playroom with dissolve
    "괜찮다고 말하려는 본심과는 달리 입에서는 긍정의 목소리가 나와버리고 말았다."

    "손목을 돌리는 코하쿠에게 직원으로 보이는 사람이 다가왔다."

    b "저번 최고 기록이 990인데 한 번 도전해보시겠어요?"

    n "(990?? 와...진짜 아깝다..)"
    
    show kohaku nomal with dissolve
    kohaku "[player_name]은 인형 가지고 싶었던거 맞제?"

    n "어...? 응...."
    
    scene 3 with dissolve
    
    "갑작스러운 소란에 사람들이 조금씩 몰려 들었다. 코하쿠는 아무렇지도 않은 듯 조용히 자세를 잡았다."
    
    scene background_playroom with dissolve
    show kohaku hmm with dissolve
    "눈을 감았다 뜬 코하쿠에게 알 수 없는 위화감이 물씬 느껴졌다. 한껏 진지한 코하쿠가 순식간에 펀치 기계에다가 주먹을 날렸다."

    scene background_playroom
    
    play sound "Punch.mp3"
    scene background_playroom with hpunch
    with Pause(1)
    
    "순간적으로 무언가 터지는 소리와 함께 주변은 고요해졌다."

    "사람들은 무언가 터진 줄 알고 다들 쳐다보고 있었고 그 사이에 혼자 서 있는 코하쿠가 보였다."

    "큰 소리에 기계가 멀쩡한지 확인하기 위해 직원이 다가갔다."

    "그러자 직원이 의아해 하는 눈으로 기계를 바라보았다."
   
    show kohaku hmm with dissolve
    kohaku "....???"
    
    "다가가 직접 확인해보니 기계의 점수가 000 이였다."

    b "어라...? 아쉽네요...?"
    
    show kohaku nomal with dissolve
    kohaku "[player_name] 이만 갑세."

    "이상하다는 것을 눈치챘지만 그냥 가자고 코하쿠가 말했다."

    n "으응..그래.."

    scene background_playroom with dissolve
    b "어라...? 기계가...망가졌잖아!!! 이건 그만한 충격을 받아야 망가질 정도로 튼튼한데...설마..?"

    scene background_after with dissolve
    "밖으로 나오니 어느새 날이 저물고 있었다."
    
    play sound "foot.mp3"
    show kohaku sad with dissolve
    kohaku "저 큰 인형 가지고 싶었을 텐데 미안하구려.."

    n "괜찮아."

    "아까 코하쿠가 뽑아주었던 인형을 꺼내들었다."

    "코하쿠의 얼굴로 가져가 코에 톡 하고 가져다 댔다."
    
    show kohaku wow with dissolve
    kohaku "???"
    
    n "난 저 큰 인형보다도 이 인형이 가장 마음에 드는걸!"

    n "고마워 코하쿠!"
    
    show kohaku love with dissolve
    kohaku "콧콧코, 고맙구먼."

    "내 머리를 쓰다듬으며 말해주었다."
    
    scene background_after with dissolve
    "그렇게 아쉬운 마음을 뒤로 하고 아까 만났던 카페까지 같이 걸었다."
    
    show kohaku nomal with dissolve
    kohaku "집까지 데려다 주겠네." 

    n "으응? 아니야. 시간도 많이 안늦었으니까 혼자 갈 수 있는 걸?"

    scene background_after with dissolve
    "혼자 갈 수 있다고 몇번은 설득한 끝에야 겨우 집에 혼자 걸어올 수 있었다."

    scene background_white with dissolve
    "3번 갤러리가 해금되었습니다."
    
    stop music fadeout 2.0
    jump happyending_kohaku



label tsukasa_date:
    scene background_tsukasa with fade
    with Pause(1)
    
    play music "main.mp3" loop
    scene background_home with dissolve
    n "~~~"

    "콧노래를 부르며 놀러갈 준비를 하고 있다."

    "이러는 이유는 일주일 전, 심심풀이로 했던 이벤트 참여에서 당첨 돼 놀이공원 티켓 2매를 받았기 떄문이다!"

    "누구랑 갈지 고민하다 츠카사에게 같이 가자고 했다."

    "츠카사가 거절하면 어쩌나 했는데 다행히 같이 가자고 해줘서 같이 가게 되었다."

    "오랜만의 놀이공원이라 조금 멋을 내고 싶기도 하다."

    menu:
        "뭘 입고 가는게 좋을까?"

        "하늘하늘한 원피스":
            "하늘하늘한 원피스"
            jump skirt

        "터틀넥에 청바지":
            "터틀넥에 청바지"
            return

label skirt:
    scene background_home
    with Pause(1)

    n "이걸 입어볼까..?"

    "나갈 채비를 모두 마치고 약속했던 장소로 갔다."

    scene background_moring_walk with dissolve
    "약속했던 장소로 가자 저 멀리 츠카사가 기다리고 있었다."
    
    play sound "foot.mp3"
    show tsukasa nomal with dissolve
    n "츠카사!"
    
    n "후우...미안, 혹시 기다렸어?"

    tsukasa "아닙니다. 저도 온지 얼마 안되었습니다. 갈까요?"

    scene background_white with dissolve
    with Pause(1)

    "1시간 후...."
    
    play sound "woowoo2.mp3"
    scene background_merry_go_round with dissolve
    with Pause(1)

    "놀이공원에 도착하자 사람이 굉장히 많아 해메다가 겨우 입구에 도착했다."
    
    show tsukasa nomal with dissolve
    tsukasa "놀이공원 ticket은 이미 누님께서 준비해주셨으니..저는 더 fast 하게 탈 수 있게 ticket들을 upgrade 할게요."

    n "그래도 괜찮아??"
    
    show tsukasa happy with dissolve
    tsukasa "물론이죠. 모처럼 놀러왔는데 제대로 즐기지 못하면 아쉽잖아요?"

    scene background_merry_go_round with dissolve
    "그렇게 안으로 들어오자 가장 먼저 무엇을 타면 좋을지 고민이 되었다."
    
    show tsukasa hmm with dissolve
    tsukasa "뭘 탈까요..."
    
    show tsukasa nomal with dissolve
    tsukasa "혹시 타고 싶은 거 있나요?"

    n "음...."

    n "아! 여기 바이킹이 되게 유명하대! 바이킹 타러 가자!"

    scene background_merry_go_round with dissolve
    "바이킹 쪽으로 향하자 역시 인기가 많아서 그런지 사람이 길게 줄을 서 있었다."
    
    n "와아! 줄 서지 않고 들어갈 수 있겠다!"

    "츠카사가 프리패스 티켓으로 업그레이드 해준 덕분에 줄을 서지 않고 들어갈 수 있었다."
    
    show tsukasa nomal with dissolve
    "좋아하는 날 보며 츠카사는 만족스러운 듯이 웃고 있었다."
    
    scene background_merry_go_round with dissolve
    with Pause(1)

    "바이킹을 타고 나오자 아침에 별로 먹지 못한 것이 떠올라 출출해졌다."
    
    show tsukasa sad with dissolve
    tsukasa "출출하네요..."
    
    show tsukasa nomal with dissolve
    tsukasa "churros 드시겠습니까? 제가 사오겠습니다."

    scene background_merry_go_round with dissolve
    with Pause(1)
    
    play sound "foot.mp3"
    scene background_merry_go_round
    show tsukasa very happy with dissolve
    tsukasa "누님~~~~~!"
    
    scene 1 with dissolve

    "분명 츄로스만 사온다고 했는데 츠카사는 누가봐도 정말 많아 보이는 양의 간식들을 한가득 들고 왔다."
    
    tsukasa "여러가지 맛있는게 보여서 사오는게 좀 늦었네요!"

    n "츠카사, 이거 다 먹을 수 있겠어?"
    
    tsukasa "후후, 당연하죠 누님."

    scene background_merry_go_round with dissolve
    "그렇게 츠카사는 내 걱정이 무색하게 그 많은 간식들을 전부 먹어치웠다.."

    "저번의 카페에서도 느낀 거지만 디저트를 내 생각보다도 더 좋아하는 모양이다."
    
    show tsukasa nomal with dissolve
    tsukasa "다음은 뭐 타실래요 누님?"

    scene background_merry_go_round with dissolve
    "우리는 이리저리 돌아다니며 여러종류의 놀이기구를 다 타러 다녔다."
    
    "츠카사가 재미있어 하는 모습을 보니 같이 오길 정말 잘했다는 생각이 들었다."

    "여러 종류의 놀이기구를 다 타다보니 이제 탈 것도 거의 남아있지 않았다."

    n "(흠....뭐타지...)"

    n "(...귀신의 집?)"

    n "츠카사, 귀신의 집 가볼래?"
    
    show tsukasa hmm with dissolve
    tsukasa "그러고보니 아직 안가본 곳인거 같네요."
    
    show tsukasa nomal with dissolve
    tsukasa "좋습니다. 누님이 가고 싶으시다면 갑시다."

    scene background_merry_go_round with dissolve
    n "보통 이런 귀신의 집 하면 이벤트가 있던데..여기는 무슨 이벤트가 있으려나?"

    scene background_merry_go_round
    with Pause(1)
    
    n "츠카사, 이것봐봐! 안에서 발목을 잡아당기나 봐!"
    
    show tsukasa hmm with dissolve
    tsukasa "그렇군요.."

    "그 말과 함께 날 바라보던 츠카사는 자신의 외투를 나에게 걸쳐주었다."

    n "음? 왜?"
    
    tsukasa "발목을 잡아당기려면 밑에서 봐야합니다."
    
    show tsukasa nomal with dissolve
    tsukasa "누님은 지금 원피스를 입으셨으니 혹시 모르니까 꼭 하시고 계세요."

    scene background_merry_go_round with dissolve
    "귀신의 집은 따로 돈을 지불해야해서 줄을 서 기다렸다."

    scene background_merry_go_round
    with Pause(1)

    scene background_merry_go_round
    "그렇게 얼마나 기다렸을까 드디어 우리 차례가 왔다."

    scene background_gost with dissolve
    with Pause(1)

    scene background_gost
    "좁은 길을 따라 천천히 나가야 해서 양 옆이 아니라 앞 뒤로 서서 나아가야 했다."

    "자신있게 앞으로 왔지만, 막상 오니 무서워졌다.."
    
    show tsukasa nomal with dissolve
    tsukasa "제가 먼저 앞으로 가겠습니다. 저를 잘 따라오세요."
    
    scene background_gost with dissolve
    "입장 후 아무것도 보이지 않는 정말 깜깜한 공간에서 츠카사의 동글동글한 뒷모습만 보였다."

    scene background_gost
    with Pause(1)

    "한참을 걸어도 귀신이나 놀라게 하는 것들은 전혀 나오지 않아 조금 안심이 되었다."

    n "후우...이제 조금 익숙해 진 거 같아!"

    "츠카사랑 조금 떨어져 걷기 시작했다."

    "그 순간, 뒤에서 갑자기 유령 인형이 튀어나왔다."

    "놀란 나머지 앞으로 뛰어가 츠카사의 등을 꼭 껴안았다."

    show tsukasa wow with dissolve
    tsukasa "!!!" with hpunch

    scene background_gost with dissolve
    "그 순간 멈칫한 츠카사가 자신을 감싸 안은 손을 양 손으로 포개어 잡더니 다시 앞으로 움직였다."

    "공포스러운 분위기는 순식간에 사라져 이 공간에 츠카사와 나, 단 둘이 남은것만 같았다."

    "츠카사를 뒤에서 두르고 있던 손에서 작은 고동이 느껴졌다."

    "왜인지 점점 빨라지는 느낌에 츠카사를 살짝 올려다봤다."

    show tsukasa n with dissolve
    tsukasa "....."

    "츠카사의 귀는 어째서인지 붉어진 것 같은 느낌이였다."

    scene background_merry_go_round with dissolve
    with Pause(1)
    
    "그렇게 아무 말 없이 귀신의 집을 빠져나온 우리는 한동안 계속 말이 없었다."

    n "그...시간도 늦었는데 밥 먹으러 갈까?"

    "츠카사는 빨개진 귀를 숨기려는 듯 황급히 뒤 돌아 식당가로 가버렸다."

    n "엇, 츠카사??!!"

    "츠카사를 불러보았지만 손짓만 할 뿐 뒤를 돌아주지 않았다."

    scene background_merry_go_round_night with dissolve
    "식사 후, 마감 퍼레이드까지 본 우리는 막차가 끊기가 전에 서둘러 지하철을 타러 갔다."
    
    scene background_tur with dissolve
    "시계를 보니 지하철이 아직 올 시간이 아니여서 의자에 잠시 앉아 기다리기로 했다."

    n "(으음...뭔가 좀 불편한데...아!!)"

    n "외투!! 빌려줘서 고마워!"
    
    show tsukasa nomal with dissolve
    tsukasa "오늘 원피스 입으셨잖아요. 저녁은 쌀쌀하니 조금이라도 따뜻하게 있으세요 누님."
    
    "그러더니 작게 웃어주며 받은 외투를 다시 어깨에 걸쳐주었다."

    "그리고 또 한마디를 덧붙여주었다."
    
    show tsukasa happy with dissolve
    tsukasa "누님, 오늘 무척이나 예쁘십니다.."
    
    tsukasa "다음에 기회가 된다면 한번 더 같이 놀러오고 싶습니다."

    scene background_tur with dissolve
    "이때, 지하철이 들어오는 소리가 들린다."

    "우리는 서로를 바라보다가 조용히 지하철을 타고 집으로 갔다."

    "내려야 하는 역에 다 와가 내리려고 준비를 하고 있다."
    
    show tsukasa nomal with dissolve
    tsukasa "늦은 밤이니 제가 데려다드리겠습니다."

    n "으응, 집이 이 근처니까 괜찮아!"
    
    show tsukasa happy with dissolve
    tsukasa "후후, 다음에는 집 앞까지 데려다 드릴껍니다."

    tsukasa "오늘 즐거웠습니다 누님, 안녕히 들어가세요."

    n "나도! 잘가 츠카사~"

    scene background_white with dissolve
    "1번 갤러리가 해금되었습니다."
    
    stop music fadeout 2.0
    jump happyending_tsukasa
    


label HiMERU_date:
    scene background_HiMERU with dissolve
    with Pause(1)
    play music "main.mp3" loop
    
    scene background_es_off with dissolve
    "오늘은 금요일."

    "회사가 여느때보다도 빨리 끝나 일찍 집으로 갈 수 있을거 같아 신난 마음으로 회사 근처 정거장에서 버스를 기다리고 있었다."

    "정거장엔 아무도 없이 나 혼자라 핸드폰을 보며 버스가 오기를 기다리고 있는데, 누군가 내 옆에 바짝 붙어 앉았다."

    n "(뭐지?)"

    "누군가 하고 돌아보니 HiMERU 씨가 앉아있으셨다."

    n "HiMERU 씨! 안녕하세요, HiMERU 씨도 이제 집에 가는 길이신가요?"
    
    show HiMERU nomal with dissolve
    HiMERU "안녕하세요, [player_name] 씨, HiMERU도 이제 버스를 타려던 참이였습니다."

    HiMERU "그나저나 [player_name] 씨, 혹시 이 후 시간 있으신가요?"

    menu:
        "네, 시간 괜찮아요!":
            "네, 시간 괜찮아요!"
            jump time_yes

        "아니요, 오늘은 예정이 있어서...":
            "아니요, 오늘은 예정이 있어서..."
            jump time_no   



label time_no:
    scene background_es_off
    n "죄송해요...저 오늘은 많이 피곤해서 집에 가야 할 거 같아요."
    
    show HiMERU hmm with dissolve
    HiMERU "그렇군요...그럼 어쩔 수 없죠."
    
    show HiMERU nomal with dissolve
    HiMERU "그럼 가보겠습니다."

    "HiMERu 씨가 자리에서 일어나 유유히 떠났다."

    return



label time_yes:
    show HiMERU happy with dissolve
    HiMERU "그런가요!"

    "평소의 HiMERU 씨 와는 다르게 정말 기쁜 듯한 얼굴이라 조금 당황했다."
    
    HiMERU "그럼 HiMERU와 바다 어떠신가요?"
    
    n "네, 좋아요!"

    "이 쌀쌀한 날씨에 바다라니...사실은 정말 가기 싫었지만, HiMERU 씨의 티 나진 않지만 은근 기대하는 모습에 그만 알겠다고 해버렸다."

    scene background_es_off with dissolve
    
    scene background_bus_in with dissolve
    with Pause(1)
    "경로를 바꿔 바다로 가는 버스에 탑승했다."

    "바다로 가는 버스라 그런지 사람이 많진 않았다."

    "맨 뒷자리 창가자리에 앉은 우리는 그저 창 밖을 바라보며 말 없이 가고 있었다."

    "한참을 가던 중, 버스의 따뜻한 히터에 졸음이 쏟아져 내렸다."

    "안 자려고 눈을 크게 떠봐도 소용이 없었고, 점점 눈이 잠겼다."

    n "........"
    
    show HiMERU hmm with dissolve
    HiMERU "[player_name] 씨?"

    n "......색색..."
    
    "HiMERU는 버스 창가쪽으로 머리를 숙이고 자는 [player_name]의 얼굴을 깨지 않게 조심히 돌려 자신의 어깨에 기대도록 했다."

    "어깨에 기대어 새근새근 자는 [player_name]의 모습을 보니 묘한 두근거림을 느꼈다."

    scene background_bus_in with dissolve
    with Pause(1)

    n "으음...?"

    "얼마나 지났을까 버스 벨 소리에 잠이 깨버렸다."

    HiMERU "드디어 일어나셨나요?"

    "무언가 이상하다 싶어 봤더니 HiMERU 씨의 어깨에 기댄 상태로 자고 있었다는걸 깨달았다."

    n "죄....죄송해요 HiMERU 씨!!!! 많이 힘드셨죠...??"
    
    show HiMERU happy with dissolve
    HiMERU "HiMERU가 기대게 한 거니 괜찮습니다. 굉장히 곤히 주무시길래 오히려 깨우기도 죄송해 주무시도록 두었습니다."

    HiMERU "이제 슬슬 도착해갑니다. 내릴 준비하세요."    

    "그렇게 말씀하시고 먼저 나가시는 HiMERU 씨를 따라 같이 따라 나갔다."
    
    scene background_night_beach with dissolve
    "바닷가까지는 조금 더 걸어야 했지만 주변 풍경을 둘러보며 걸으니 금새 바다에 도착했다."

    n "역시 늦은 시간이라 그런지 사람이 많이 없네.."

    "바닷가라 그런지 더 쌀쌀한 바람에 추위를 느끼고 있었다."
    
    show HiMERU nomal with dissolve
    HiMERU "[player_name] 씨, 추우시면 HiMERU의 외투라도 입으세요."

    n "HiMERU 씨도 추우실테니 괜찮아요."
   
    HiMERU "괜찮습니다. HiMERU에겐 이정도는 시원합니다."
    
    play sound "fado.mp3"
    scene background_night_beach with dissolve
    "그러다 갑자기 차가운 바람이 강하게 불어왔다."

    n "(역시 늦은 시간이라 그런건가...조금 춥다..)"
    
    scene 7 with fade
    with Pause(1)
    
    "HiMERU 씨를 돌아봤더니 HiMERU 씨도 추운듯 주머니에 양손을 넣고 움츠려 있었다."

    n "후후, 역시 추우신가 보네요."

    "아기 고양이같이 추워서 움츠리는 HiMERU 씨가 너무 귀엽다."
    
    scene background_night_beach with dissolve
    show HiMERU nomal with dissolve
    HiMERU "근처 카페라도 들어갑시다."

    "우리는 바다에서 2분 정도 거리에 있는 카페로 들어갔다."
    play sound "bell.mp3"
    
    scene background_caffe with dissolve
    n "(음...난 간단하게 아이스 아메리카노 마실까?)"

    n "저는 아이스 아메리카노 마실껀데 HiMERU 씨는 뭐 마실래요?"
    
    show HiMERU nomal with dissolve
    HiMERU "HiMERU는 따뜻한 아메리카노로 하겠습니다."

    scene background_caffe with dissolve
    "아메리카노라 금방 나와 우리는 쿠션이 있는 구석진 자리에 앉았다."
    
    show HiMERU hmm with dissolve
    HiMERU "이런 추운 날씨에 아이스 아메리카노라니...안 추우신가요?"
    
    scene background_caffe with dissolve
    n "후후, 원래 이런 날씨에는 아이스 아메리카노죠!"

    n "자요! HiMERU 씨도 한입 하세요!"

    "솔직히 거절할 줄 알고 반은 장난으로 한거였는데, HiMERU 씨는 정말 한모금 마셨다."

    "심지어 내가 마시던 빨대로 드셨다..."
    
    show HiMERU happy with dissolve
    HiMERU "추운날에 아이스 아메리카노도 나쁘지 않네요."

    scene background_caffe with dissolve
    "HiMERU 씨는 아무렇지도 않은 듯이 보였다. 아마 나만 의식한거 같았다.."

    scene background_night_beach with dissolve
    "다 마시고 밖으로 나오자 날이 더 저물어서 방금 전 보다 더 추웠다."

    scene background_night_beach
    with Pause(1)

    "해변을 따라 걷다가 손이 너무 시려워서 두 손을 계속 비볐다."
    
    show HiMERU nomal with dissolve
    HiMERU "혹시 손 시려우신가요? 손이 시려우시다면 HiMERU의 손을 잡아도 됩니다."
    
    scene background_night_beach with dissolve
    "손을 잡는것 까진 너무 부끄러워 거절하려 했지만 손이 너무 시려워 그만 HiMERU 씨의 손을 잡았다."

    "그렇게 우리는 손을 잡고 버스 정류장까지 걸어갔다."
    
    scene background_white with dissolve
    "버스가 오고 집에 가는 길에도 HiMERU 씨는 내 손을 놓지 않으셨다."

    "내가 놓으려하면 놓치지 않으시겠다는듯이 내 손을 더 꽉 잡고 계셨다."

    scene background_night_home_walk
    "그렇게 집까지 HiMERU 씨가 데려다 주셨다."

    n "오늘은 고마웠어요 HiMERU 씨."

    "손을 살짝 놓으며 이야기하자 HiMERU 씨는 놓은 손을 조금 아쉬운듯이 바라보셨다."
    
    show HiMERU happy with dissolve
    HiMERU "HiMERU 야말로 오늘 함께해주셔서 감사합니다. 안녕히 주무세요."

    scene background_white with dissolve
    with Pause(1)

    "왜인지 오늘 밤은 굉장히 좋은 꿈을 꿀것만 같은 기분이 들었다."
    
    stop music fadeout 2.0
    jump happyending_HiMERU


label kunugi_date:
    scene kunugi with dissolve
    with Pause(1)

    scene background_home with dissolve
    "금요일 아침, 회사에 출근을 하기 위해 평소처럼 옷을 갈아입고 나갈 준비를 한다."

    "오늘은 평소보다 준비를 빨리 해 나름 여유를 가지고 거실에서 티비를 틀자 크리스마스 특집 방송을 하고 있었다."

    n "아, 오늘 크리스마스구나..."

    "금요일이라 모처럼 신경써서 메이크업을 했기도 하고, 크리스마스인 오늘을 그냥 포기핳 수 없어 밖에 나가서 구경이라도 할 생각으로 신발장으로 갔다."

    "모처럼이니 힐을 신을지, 아니면 편하게 스니커즈를 신을지 고민이 된다."

    menu:
        "크리마스 날, 신발은 어떤걸로 신으시겠습니까?"

        "오랜만에 힐을 신는다":
            "오랜만에 힐을 신는다."
            jump top

        "그냥 평소처럼 스니커즈를 신는다":
            "평소처럼 스니커즈를 신는다"
            return    


label top:
    
    scene background_walk_walk with dissolve
    "신발을 신고 나오자 찬 공기가 얼굴을 스친다."

    n "엄청 춥네..."

    "지금 이 시간이라면 출근하는 사람이 많아 북적거렸을 길이 한가하다."

    "지하철을 타고 시내로 나가기로 했다."

    scene background_tur with dissolve
    with Pause(1)

    "지하철역에 도착해 주위를 둘러보니 역시 커플들이 많이 보인다."

    n "(그러고보니...이번 크리스마스도 솔로네..하하)"

    n "(뭐 그동안 바빠서 누구를 만날 여유도 없었으니 그럴만도..)"

    scene background_white with dissolve
    "___이번 정거장은 OO..OO 내려가시는 문은 오른쪽입니다____"

    "드디어 시내에 도착했다."
    
    play sound "woowoo2.mp3"

    scene background_tur with dissolve
    "역에서 내려 위로 올라가자 크리스마스 분위기로 한껏 꾸민 가게들이 보인다."
    
    play music "main.mp3" loop
    scene background_moring_walk with dissolve
    "광장 중앙에는 큰 트리가 있고, 백화점도 크리스마스 분위기를 한껏 풍기고 있었고, 빨간 모금함도 보이고.."

    "그리고...쿠누기 씨."

    n "(잠깐...쿠누기 씨?)"

    "주위를 둘러보자 쿠누기 씨가 보였다. 혼자 광장 가운데 벤치에 앉아 책을 읽고 계사는 듯이 보였다."

    n "아침 일찍 시내에서 혼자 뭐하세요...?"

    "쿠누기 씨에게 조심스럽게 다가가 말을 걸었다."

    show kunugi no with dissolve
    kunugi "그러는 [player_name] 씨야 말로 아침 일찍 여기서 뭐 하시는건가요?"

    n "어...그게,"

    scene background_moring_walk with dissolve
    with Pause(1)
    "주절주절...아침에 있었던 일들을 쿠누기 씨에게 설명했다."
    
    show kunugi nomal with dissolve
    kunugi "[player_name] 씨는 성실하다고 해야 할꺼 같군요."

    n "하하..."

    n "혹시 누구 기다리시고 계신 건가요?"
    
    kunugi "네, 아는 분과 약속이 있어 기다리고 있었습니다."

    scene background_moring_walk with dissolve
    "내심 예정이 없으시길 바랬지만...있으시다는 말에 씁쓸한 건 어쩔 수 없었다."
    
    show kunugi no with dissolve
    kunugi "....."

    show kunugi hmm with dissolve

    scene background_moring_walk with dissolve
    "쿠누기 씨는 누군가에게 문자를 보내시는 것 같다."

    show kunugi nomal with dissolve
    kunugi "이제 약속이 없어졌습니다."

    n "...네?"

    kunugi "이제 약속이 없어 할 것도 없는데, 같이 시내 구경이나 할까요?"

    scene background_moring_walk with dissolve
    "갑자기 약속이 없으시다고 하셔서 의구심이 들었지만, 크리스마스 날 혼자 있지 않아도 된다는 안도감이 들어 기쁘게 수락했다."

    "그렇게 같이 시내를 돌아다녔다."

    "가게 이곳 저곳에서는 크리스마스 이벤트를 하느라 바쁘다."

    scene background_moring_walk with dissolve
    with Pause(1)

    k "거기 커플분~ 저희 매장에서 커플끼리 오면 할인 해주는 이벤트를 하고 있는데, 괜찮으시다면 들렀다 가세요~"

    "우리 둘을 향해 가게 직원분이 말을 걸었다."
    
    "커플...이라니..조금 부끄럽다."

    n "하하하, 커플이라니..정말 말도 안되네요~"
    
    "혹시나 싫어하실 수도 있을거 같아 커플이라는 소리를 부정했다."
    
    show kunugi nomal with dissolve
    kunugi "아뇨, 말도 안되는건 아니죠."
    
    scene background_moring_walk with dissolve

    "그 말씀에 괜히 얼굴이 달아오른 나는 시선을 돌리며 말했다."

    n "그...이제 할 것도 없는데 영화 보실래요?"
    
    scene background_moring_walk with dissolve
    with Pause(1)

    "그렇게 우리는 영화를 보기로 했다."

    "근처 백화점 윗층에 영화관이 있어 그곳으로 갔다."

    scene background_movie_box with dissolve
    with Pause(1)
    
    show kunugi nomal with dissolve
    kunugi "무슨 영화로 하실껀가요?"

    scene background_movie_box with dissolve
    "이번 상영중인 영화 목록들을 보니 볼게 많아보여 조금 고민이 된다.."

    scene background_movie_box
    "티켓을 얘매하고 팝콘과 콜라를 사서 극장 안으로 들어갔다."
    
    scene background_movie with dissolve
    "안으로 들어가자 상영 전 광고가 재생되고 있었다."

    "그냥 광고만 보면서 있기에는 어색해 무언가 말을 걸어보려고 했지만...무슨 주제로 말을 꺼내야 할지 고민하다가 시간이 다 가버렸다.."

    menu:
        "어떤 영화로 할까요?"

        "스릴러":
            "스릴러"
            jump exid

        "로맨스":
            "로맨스"
            jump lomance


label exid:
    scene background_movie
    with Pause(2)
    stop music fadeout 2.0

    "영화가 시작되었다."

    "평점 4.3의 스릴러 영화인데..4.3점이라는 평가가 무색하게도 재미가 없어 그만 잠에 들어버리고 말았다..."

    "그렇게 영화가 끝나버렸다.."
    
    jump dinner
    
    
label lomance:
    scene background_movie
    with Pause(2)
    stop music fadeout 2.0

    "영화가 시작되었다."

    "평소에 로맨스를 즐겨봤던 나는 금세 빠져들었다."

    "옆에서 한창 집중해서 보던 쿠누기 씨는 영화가 너무 진부했는지 꿈뻑 꿈뻑 조시는 거 같다."

    scene background_movie
    with Pause(1)

    "잠시후, 내 어깨에 무언가 닿았다."

    "쿠누기 씨가 잠드셨다.."

    "갑작스러운 상황에 설렘과 두근거림으로 마음을 어떻게 할 수가 없다.."

    "심장이 크게 두근거리는게 느껴진다."

    scene background_movie
    with Pause(1)

    "그렇게 잠이 든 쿠누기 씨를 어깨에 기대게 하고 세상에서 가장 설레는 영화를 봤다."
    jump dinner


label dinner:

    scene background_movie_box with fade
    with Pause(1)
    play music "main.mp3" loop

    scene background_night_000 with dissolve
    "영화가 끝나고 우리는 저녁을 먹기 위해 주변 식당에서 밥을 먹으려 했다."

    "그런데 크리스마스라 사람이 너무 많은 탓에 가게마다 사람이 꽉 차 보였다."

    n "(사람이 진짜 많네...여기서 먹기는 힘들것 같아..)"
    
    show kunugi nomal with dissolve
    kunugi "[player_name] 씨, 여기로 오세요."

    n "네...?? 자리 있나요??"

    kunugi "제가 미리 예약해놨었습니다."
    
    play sound "bell.mp3"
    scene background_eat with dissolve
    "쿠누기 씨가 미리 식당을 예약해주신 덕분에 저녁을 먹고 갈 수 있게 되었다."

    "우리는 창가 자리에 앉아 메뉴를 골랐다."
    
    show kunugi nomal with dissolve
    kunugi "저는 봉골레 비앙코로 하겠습니다. [player_name] 씨는요?"

    n "음....저는 토마토 파스타로요!"

    scene background_eat with dissolve
    with Pause(1)
    "조금 기다리자 주문한 파스타가 나왔다."

    n "....!!"

    "파스타의 맛은 내가 여태껏 먹어본 곳 중에 가장 맛있는것 같았다.."

    "그렇게 파스타를 먹던 도중, 창 밖에 흰색의 무언가가 톡 하고 떨어진다."

    "창 밖을 보자 눈이 내린다."

    image snow = SnowBlossom("snow.png", count=100, yspeed=(50, 150), fast=True)

    n "눈이다...."

    "펑펑 예쁘게 눈이 내린다."

    "파스타를 먹던 우리는 예쁘게 내리는 눈에 창문 밖을 한참 바라보았다."

    n "너무 예뻐요...계속 바라볼 수 있을것만 같아.."

    n "(올해도 솔로를 마지막으로 끝내는구나..)"

    scene background_eat with dissolve
    with Pause(1)
    
    show kunugi nomal with dissolve
    kunugi "계속 구경하다간 모처럼의 파스타가 식어버리니 얼른 드세요."

    "그렇게 우리는 함박눈을 보며 파스타를 먹었다."

    scene background_night_000 with dissolve
    "식사를 마치고 눈이 내려 더 운치있어진 광장을 우산을 쓰고 천천히 걸었다."

    scene background_night_000 with dissolve
    with Pause(1)

    "한참을 걸으니 다리가 슬슬 저려오기 시작했다."

    "엎친데 격친격으로 날이 추워서 건조해진 피부에 힐의 뒤꿈치가 쓸려 그만 까져버렸다."
    
    scene 9 with fade
    kunugi "어디 불편한 곳 있으신가요?"
    
    "내가 다리를 조금씩 절뚝거리는걸 눈치채신 모양인지 물어보셨다."

    n "그 별건 아니고..뒤꿈치가 살짝 까진 거라서 괜찮아요!"

    "내 말에 쿠누기 씨는 내 발을 잠시 바라보셨다."
    
    kunugi "잠시만 기다려주세요."

    "그 말과 함께 우산을 쓰고 어디론가 달려가신다.."

    scene background_night_000 with dissolve
    with Pause(1)

    "잠시후.."

    "저 멀리 눈을 맞으며 뛰어오는 쿠누기 씨가 보인다."

    "점점 가까워지면서 그의 손에 무언가 들려있는게  보인다."

    n "그게 뭐에요?"
    
    show kunugi hmm with dissolve
    kunugi "반창고입니다."

    n "...!! 눈도 오는데 괜히 춥게 왜 다녀오셨어요..!!"
    
    show kunugi nomal with dissolve
    kunugi "아픈 사람을 치료하는건 당연합니다."

    kunugi "그리고 빨리 치료하지 않으면 덧날수도 있으니깐요."

    scene background_night_000 with dissolve
    "그렇게 말씀하시더니 내 앞에 쭈그려 앉으셨다."
    
    show kunugi nomal with dissolve
    kunugi "제 어깨에 손을 짚고 다리를 살짝 올려주세요."

    scene background_night_000 with dissolve
    "힐을 벗기고, 반창고를 뜯어 내 뒷꿈치에 붙여주시려고 하는데..."

    "자세히 보니...반창고 디자인..."

    "귀여운 공룡이 그려져 있다."

    n "후후, 왜 이걸로 사오신거에요?"

    show kunugi hmm with dissolve
    kunugi "그...이것만 있었습니다.."

    "그렇게 나에게 반창고를 꼼꼼하게 붙여주셨다."
    
    show kunugi no with dissolve
    kunugi "이 상태로 역까지 가는건 무리이니 역앞까지만 제가 업어드리겠습니다."

    n "네...???!! 아니에요!! 괜찮아요..!!"

    scene background_night_000 with dissolve
    "업어주신다는 말씀에 최대한 거절하려고 했지만..완고한 쿠누기 씨를 막을수는 없었다.."

    scene background_night_000 with dissolve
    with Pause(1)

    "그렇게 나는 쿠누기 씨에게 업힌채로 역으로 돌아갔다."
    
    scene background_tur with dissolve
    "처음처럼 지하철을 기다리고 있지만, 내 옆에는 쿠누기 씨가 함께 있으신다."

    "쿠누기 씨가 같이 계셔서 정말 다행이라는 생각이 들었다."

    scene background_white with dissolve
    "지하철이 도착하고, 우리는 함께 지하철을 타고 집으로 돌아간다."
    
    show kunugi nomal with dissolve
    kunugi "집까지 데려다드리겠습니다."

    n "피곤하실텐데..집까지 데려다주시지 않으셔도 괜찮아요."

    kunugi "시간도 늦었고, 혼자서는 위험하니 그럴 수는 없습니다."
    
    scene background_ex with dissolve
    "밖에 나가니 눈은 어느새 그친건지 더 내리지 않았다."

    "눈이 그쳐버려 내심 아쉬웠지만, 쿠누기 씨가 곁에 있다는것이 그 무엇보다도 기뻤다."

    scene background_night_home_walk with dissolve
    with Pause(1)
    play sound "foot.mp3"
     
    "어두운 골목길, 가로등만이 비춰주는 길을 따라 그저 걷다보니 우리는 어느새 집 앞에 도착했다."

    n "오늘은 정말 감사했습니다..! 조심히 들어가세요 쿠누기 씨!"
    
    show kunugi nomal with dissolve
    kunugi "아닙니다. 다음주 회사에서 봅시다."

    scene background_white with dissolve
    "서로 작별인사를 하며 우리는 헤어졌다."
    
    scene background_white
    with Pause(1)
    "9번 갤러리가 해금되었습니다."
    stop music fadeout 2.0
    
    jump happyending_kunugi




#해피엔딩 츠카사
label happyending_tsukasa:
    $ persistent.ending1 = True
    $ renpy.save_persistent()
    
    scene background_tsukasa with fade
    with Pause(1)
    
    play music "main.mp3" loop

    scene background_es_talking with dissolve
    "츠카사와 놀이공원에서 놀았던 날을 기점으로 우리는 좀 더 자주 만나게 되었다."

    "점심을 같이 먹거나, 간단한 티타임이라던가, 휴일에도 만나서 놀 정도로 우리는 전보다 더 친해졌다."

    scene background_white with dissolve
    "그리고...나는 내 사고 당일날의 기억도 되찾았다."

    scene background_walk with dissolve
    "그때, 계단에서 날 도와주려고 급하게 내려오던 사람은 츠카사였다."

    "비록 나는 계단에서 넘어졌지만, 츠카사가 그 때 도와주려하지 않았다면 어떻게 되었을지 벌써 아찔하다."
     
    scene background_es_talking with dissolve 
    "그렇게 여러가지가 합쳐져...나는 츠카사를 좋아하게 되었고, 하나의 문제도 발생했다."

    "그건 회사사람들이 우리가 사귄다고 알고 있기 때문이다.."

    "아무리 아니라고 말해도 오히려 믿지 않아 곤란했다."

    n "(친해지는건 정말 좋지만, 츠카사는 그런 마음도 없을텐데 이런 오해를 받게 해버려서 미안하네..)" with hpunch

    "그 결과, 우리는 사귀지도 않는데 사귄다고 오해를 받아버린 것이였다."

    "츠카사는 이 사실을 모르는것 같았지만..."

    "아무리 아니라고 해도 믿지 않는통에 괜히 츠카사에게 미안해졌다."

    "그래서, 요 근래는 츠카사를 조금 피해다녔다."

    "그리고, 피한다면 좋아하는 마음이 조금은 사라지지 않을까 하는 내 개인적인 마음도 있었다."

    scene background_white with dissolve

    scene background_es_in with dissolve
    show tsukasa happy with dissolve
    tsukasa "누님! 어디가시는 길이신가요?"

    n "어....그게..아, 아무것도 아니야!!"
    
    show tsukasa wow
    tsukasa "누님!!???" with hpunch

    scene background_white with dissolve
    with Pause(1)

    scene background_es_self with dissolve
    show tsukasa very happy with dissolve
    tsukasa "누님! 잠시 쉬시는거면 저도 같이 있어도 될까요?"

    n "아 미안...나 이제..일 가봐야해서!!!!"
    
    show tsukasa wow
    tsukasa "누님!!?????" with hpunch
    stop music fadeout 2.0
    
    scene background_white with dissolve
    with Pause(1)
    
    play music "sad.mp3" fadein 2.0 loop
    scene background_es_talking with dissolve
    n "(아무리 그래도 언제까지 이럴수는 없는데..)"

    "우리는 친하기 이전에 회사 동료이다. 이렇게 계속 피해다닌다면 일에도 지장이 생길게 분명했다."

    n "(회사인 만큼 공과 사는 확실히 해야 하는데...)"

    n "(어떻게 하면 좋으려나...)"

    "그렇게 고민하고 있었을 때, 츠카사에게 문자가 왔다."

    tsukasa "(누님, Talking 하고 싶은게 있습니다. 오늘 회사 끝나고 회사 앞에서 잠시 기다려주세요.)"

    n "....."

    n "(츠카사도 내가 요 근래 피해다녀서 많이 당황스러웠겠지..?)"

    "오늘 우리 오해에 대해 확실히 말하는게 낫겠다 생각하며 마저 남은 일들을 처리했다."

    scene background_pos_night with dissolve
    "일을 다 끝내고 회사 앞에서 기다리고 있자 츠카사가 왔다."
                  
    show tsukasa nomal with dissolve             
    tsukasa "다행히 기다리고 계셨군요. 누님, 같이 가시죠."

    scene background_night_000 with dissolve
    tsukasa "......"

    n "......"
    
    play sound "foot.mp3"
    "우리는 그저 말없이 계속 걸었다."

    "츠카사는 어떻게 말을 꺼내면 좋을지 고민하는것만 같았다."

    "나도 무슨 말을 꺼내야할지 감이 오지 않아 말을 딱히 꺼내진 않았다."

    scene background_night_matsuri with dissolve
    "얼마나 걸었을까 우리는 아직 가을 축제의 흔적이 생생하게 남아있는 신사에 도착했다."

    "저녁시간이라 그런지 주변에 사람은 아무도 없었다."
    
    show tsukasa sad with dissolve
    tsukasa "누님...혹시 이 츠카사가 뭔가 잘못이라도 한 건가요..?"

    "조금 울먹거리는 목소리로 츠카사가 말했다."

    tsukasa "만나도 자꾸 피해버리시고, 휴일에도 바쁘시다 하시고....츠카사가 무슨 잘못이라도 했으면 말씀해주십시오.."

    n "그게 사실은..."

    "내가 말을 꺼내자 츠카사는 흔들림 없이 똑바로 날 쳐다보고 있었다."

    n "그.....우리 오해 때문이야..!"
    
    show tsukasa wow with dissolve
    tsukasa "네..? 오해라뇨...?"

    n "그....우리 요 근래 계속 만났잖아..그거 때문에 우리가 사귀는 사이라고 오해를 받아버려서.."

    n "우리 사귀지도 않는데 이런 오해를 받아버리니까 미안해져서.."
    
    show tsukasa near with dissolve
    tsukasa "....오해 받으면 안되나요?"

    n "츠카사는 그런 마음도 아닌데..좀 그렇잖아.."

    tsukasa "그럼, 누님은요?"

    "갑자기 츠카사가 가까이 다가왔다."

    tsukasa "누님의 마음은 어떠신가요?"
    
    scene background_night_matsuri with dissolve
    "갑자기 머릿속이 새하얘졌다. 마치 생각을 읽힌것만 같은 예리한 질문이였다."

    "그 물음에 아무런 말도 못꺼내고 있었다."
    
    stop music fadeout 2.0
    show tsukasa sad with dissolve
    tsukasa "저는....누님을 좋아합니다."

    tsukasa "예전부터 좋아했습니다..하지만 누님께서는 저를 이성이 아닌, 후배이자 귀여운 남동생으로 밖에 보시지 않으시는거 같아 걱정했습니다."

    tsukasa "그런데, 누님이 같이 놀이공원에 가자고 한 그날, 저는 정말 기뻤습니다."

    tsukasa "다른 누구와도 아닌, 누님과 단 둘이 가는 Date..였으니깐요."

    tsukasa "놀이공원에 같이 간 그날 이후로, 저는 드디어 사이가 더 발전할 수 있을거 같아 열심히 Appeal 해왔습니다만..."

    tsukasa "어째선지....갑자기 누님이 피해버리셔서..요 며칠간...많이 슬펐습니다.."
    
    show tsukasa near with dissolve
    tsukasa "오늘은, 지금만큼은 저를 그저 남동생이나 후배로 보지 말아주세요.."

    tsukasa "좋아합니다...제 마음..받아주시겠습니까?"
    
    play music "Noblesse.mp3" loop
    scene background_night_matsuri with dissolve
    with Pause(1)
    
    "츠카사의 말을 듣고 지금 꿈을 꾸고 있는것만 같았다."

    "물론, 처음에는 후배이자 챙겨주고 싶은 남동생의 이미지였던 것은 맞다."

    "하지만, 지내오면서 점점 후배가 아닌 이성으로써 보게 되고..그렇게 좋아하게 되었다."

    "츠카사는 나와는 다른 마음으로 대한것 같아 일부터 피해다녔는데...진작 마음을 전해볼껄 그랬나보다.."
    
    show tsukasa wow with dissolve
    tsukasa "누님..? 무슨 일 있으신가요?"
     
    scene background_night_matsuri with dissolve
    "내가 한동안 말이 없자 츠카사는 무슨 일이 있나 싶어 초초한 눈으로 날 바라보았다."

    n "...아해.."
    
    show tsukasa wow with dissolve
    tsukasa "네?"

    n "나도...츠카사가 좋아.."
    
    scene background_night_matsuri with dissolve
    n "나도 맨 처음에는 츠카사가 생각한 대로 그저 후배로써 본 건 맞아."

    n "하지만 같이 지내오면서 점점 좋아하게 되어서.. 사실 놀이공원 전부터 좋아하고 있었어.."

    n "그래서 놀이공원에 같이 가줬을 때, 많이 설레고 기뻤어...그리고.."

    n "내가 사고가 났던 날, 그 때 날 도와주려했던 사람은 츠카사였지?"
     
    show tsukasa wow with dissolve 
    tsukasa "...!!"

    "내 말에 츠카사는 놀란 듯이 날 바라보았다."
    
    scene background_night_matsuri with dissolve
    n "넘어진 이후에는 누가 도와주려 해줬는지 몰랐어..나중에 기억을 더듬어도 아무것도 기억나지 않았으니까.." 

    n "그 때 츠카사가 도와주려하지 않았다면 더 큰일이 났을꺼야..도와주려해줘서 고마워 츠카사."

    n "그리고...또.."

    "이 뒤에 말을 더 어떻게 하면 좋을지 말문이 막히자 츠카사가 내 손을 잡았다."
    
    show tsukasa sad with dissolve
    tsukasa "누님의 말씀대로 그 때 도와드리러 간건 제가 맞습니다."

    tsukasa "사실은 그 때...제 마음을 전하고 싶어 누님이 아직 계시다는 소식을 듣고 누님에게 가던 길 이였습니다."

    tsukasa "그 때 잡아주었더라면..누님이 그런 일은 겪으시지 않으셨을텐데...하는 생각으로 입원해계신 동안 저를 책망했습니다."

    tsukasa "누님이 일어나시고, 사고 당일의 기억이 나지 않으신다는 말씀에 말씀드리려 했지만...그 때 잡아주지 못한 저를 원망하실지도 모른다는 생각에 말씀을 드리진 않았습니다."
    
    show tsukasa happy with dissolve
    tsukasa "오히려 감사드려야 하는것은 츠카사입니다. 감사합니다 누님."

    tsukasa "그리고...저와 같은 마음이라니....정말 믿을수 없을 정도로 행복합니다."

    tsukasa "저를...츠카사를 받아주셔서 감사합니다.."

    tsukasa "누님을 늘 Happy 하게 웃는 얼굴로 있으실 수 있도록 해드리겠습니다."

    "츠카사가 그 말을 마치자 신사 주변의 등에 불이 들어와 밝게 빛났다."

    scene 2 with fade

    "등불이 빛나는걸 보고 있자 츠카사가 잡은 손을 더욱 강하게 잡았다."

    tsukasa "빛나는게 정말 예쁘군요. 조금 둘러보다가 갑시다!"
    
    "내 손을 잡으며 말하는 츠카사의 모습은 정말 그 무엇보다도 예뻤다."

    n "응, 좋아!"

    scene background_white with dissolve
    with Pause(1)
    
    "2번 갤러리가 해금 되었습니다."

    "츠카사_해피엔딩"
    stop music fadeout 2.0
    
    scene black with dissolve
    with Pause(2)
    play sound "heart.mp3"
    
    scene black
    with Pause(7)
    
    
                      
return


#해피엔딩 코하쿠
label happyending_kohaku:
    $ persistent.ending2 = True
    $ renpy.save_persistent()
     
    scene background_kohaku with fade
    with Pause(1)
    
    play music "main.mp3" loop
    scene background_es_talking with dissolve
    "오락실에서의 날을 기점으로 우리는 주말에도 종종 만나서 놀 정도로 더욱 가까워졌다."

    "자주 만나 놀면서 코하쿠의 평소 못 보던 모습을 보면서 신선하다는 생각도 하고, 이야깃거리가 점점 더 늘어나게 되고, 같이 웃고.."

    "그러다보니 한가지의 의문이 들었다."

    n "(지금 코하쿠랑 나는 무슨 사이일까?)"

    "친구라기에는 묘하게 더 가까운 느낌이고, 애인이라 하기에는 또 아닌것 같다.."

    "그리고, 나는 며칠 전 사고 당일날의 기억을 되찾았다."

    scene background_walk with fade
    "계단에서 날 도와주려 했던 사람은 코하쿠였다."

    "그 때 코하쿠는 지금까지 한번도 본 적 없는 얼굴로 다급하게 날 부르고 있었다."

    scene background_es_talking with dissolve

    "처음에는 코하쿠를 그저 츠카사의 동생이자, 귀여운 후배 정도로 생각했다."

    "하지만 시간이 지나면서, 같이 지내는 날이 늘어나자 자연스럽게 코하쿠를 이성으로 제대로 마주하게 되었다."

    "예전에 있었던 일을 생각하면 늘상 코하쿠랑 같이 있었던 날들이 생각이 났고, 아무리 다른 주제로 돌려봐도 그 끝에는 늘 코하쿠 생각 뿐이였다."

    "그렇게 하루하루 보내다 보니....어느새 나는 코하쿠를 좋아하게 되어버린걸지도 모른다."

    scene background_es_talking
    with Pause(1)

    kohaku "[player_name] 씨, 들어가도 되나?"

    "마침 코하쿠에 대한 생각을 하고 있었는데, 아니나다를까 본인이 왔다.."

    n "응, 들어와 코하쿠~"
    
    play sound "door.mp3"
    show kohaku nomal with dissolve
    kohaku "실례하겠네, 후우..이제 바깥도 제법 추워졌구려."
    
    kohaku "자, 녹차일세. 방금 막 가져와 제법 따뜻할걸세."

    n "와아, 고마워!"
    
    "잠시 코하쿠랑 녹차를 마시며 얘기를 나누고 있자, 방금전의 생각이 정리되기는 커녕 오히려 머릿속에서 마구 뒤엉키는 느낌이 들었다."

    "내가 잠시 말이 없자 코하쿠가 날 걱정스럽게 보며 물었다."
    
    show kohaku wow with dissolve
    kohaku "[player_name] 씨? 괜찮은가? 어디 아픈건 아니겐가?"

    n "아니, 아픈건 아닌데...있지, 코하쿠.."
    
    show kohaku nomal with dissolve
    kohaku "아프지 않다면 다행이네만...무슨일인겐가?"

    n "그...있지..우리는 무슨 사이야?"

    "그러다 문득, 그만 생각하던게 입 밖으로 나와버렸다."

    "내 말에 코하쿠는 잠시 멈칫하더니 이내 웃는 얼굴로 말한다."

    kohaku "무슨 소리인겐가, 우리는 친한 친구같은 사이지 않나."

    "코하쿠의 말을 듣자 의문이 들어 생각해왔던 말들이 입 밖으로 계속 나왔다."

    n "정말...?"

    n "정말 그냥 친구사이라고 생각하는거야?"
    stop music fadeout 2.0

    "내 말에 어딘가 정곡을 찔린건지 당황하며 코하쿠는 아무런 말을 하지 못했다."

    n "나 사실은..사고 당일날의 기억이 누가 일부러 지운것 마냥 전혀 기억이 나지 않았어."

    n "그런데 며칠전, 기억이 되돌아왔었어. 그때 너는 지금까지 본 적없는 얼굴로 날 부르고 있었어."
    
    show kohaku hmm with dissolve
    kohaku "........."
    
    scene background_es_talking with dissolve
    n "말해줘 코하쿠, 정말 날 그냥 친한 친구사이라 생각하고 있는거야?"

    n "그리고...왜 사고 당일날 도와주려했다는 사람이 너라는걸 말 해주지 않았던거야? 난...계속 찾고 있었는데.."

    "나의 물음에 아무 말 없이 날 그저 바라보던 코하쿠는 말을 꺼내기 시작했다."

    scene background_es_talking
    with Pause(1)
    
    
    show kohaku hmm with dissolve
    kohaku "우선, 사고 당일 도와주려 했던 사람은 나 맞네."

    kohaku "말하지 않았던 이유는...."
    
    show kohaku sad
    kohaku "....그 때 잡아주지 못했기 때문일세."
    
    show kohaku hmm
    kohaku "난, 어렸을 때부터 오우카와 가의 남자로 태어났기 때문에 강해져야만 했네."

    kohaku "그러다보니 다양한 무술이라던가, 기술들을 어렸을 때부터 접해 일반인보다 힘이 더욱 세졌네."
    
    show kohaku sad with dissolve
    kohaku "그렇기에 나는, 누군가를 지킬 정도의 힘은 충분히 된다고 줄곧 생각하고 있었네만, 그 때..... 당신이 계단에서 넘어진 그날...난 그때 느꼈네.."

    kohaku "좋아하는 사람도 제대로 지키지 못하는 주제에...나 하나도 지키기 벅찰지도 모른다는 생각이 들어 이제까지 느껴본 적 없는 감정이 들었네.."

    n ".....!!!!!!"
    
    show kohaku love
    kohaku "...좋아하네 [player_name]."

    kohaku "아니라고 날 부정해도 언제나 시선 끝에는 당신이 있었다네."

    kohaku "오락실에서의 일도...사실은 잘 보이고 싶어서 그런것도 있었네."
    
    scene background_es_talking with dissolve
    "코하쿠의 말에 시간이 멈춘것만 같았다."

    "조곤조곤 진중하게 전해져 오는 고백에 얼굴이 달아오르는것이 느껴졌다."
    
    show kohaku nomal with dissolve
    kohaku "...내가 말하고 싶은건 다 말했네. 이제 당신 대답을 들려줬으면 좋겠구먼."
    
    scene background_es_talking with dissolve
    "코하쿠는 날 똑바로 응시하며 대답을 기다리고 있었다."
    
    n "나도...좋아해."

    n "방금 취조하는듯이 물어서 미안해.. 하지만 이래야 내 마음을 제대로 알 수 있을거 같아서 그랬던거야.. 악의는 없었어.."

    n "계단에서의 일은..난 코하쿠에게 정말 감사하고 있어. 그때 도와주지 않으려 했다면 더 큰일이 났을지도 모르는 거니까....고마워."

    n "그리고 방금 얘기를 듣고 확실하게 깨달았어..나는...코하쿠가 좋아.."

    n "아마도...오락실 가기 전부터 좋아했던거 같아.."

    "내 말이 끝나자 내 손을 잡아 슬며시 깍지를 꼈다."
    
    play music "Noblesse.mp3" loop
    scene 4 with fade
    kohaku "콧콧코..우리가 같은 마음이라니.."

    kohaku "앞으로는 내가 무슨일이 있어도 꼭 지키겠네."

    kohaku "그러니 그저 웃어주었길 바랄 뿐일세. 그것이 내 바램이네."

    n "응, 잘 부탁해 코하쿠."

    scene background_white with dissolve
    "우리는 깍지를 끼고 언제 그랬냐는듯 서로 바라보며 웃었다."
    
    "4번 갤러리가 해금되었습니다."

    "코하쿠_해피엔딩"
    
    stop music fadeout 2.0

    scene black with dissolve
    with Pause(2)
    play sound "heart.mp3"
    
    scene black
    with Pause(7)

return

#해피엔딩 레오

label happyending_leo:
    $ persistent.ending3 = True
    $ renpy.save_persistent()
    
    scene background_leo with fade
    with Pause(1)
    
    play music "main.mp3" loop
    scene background_es_talking with dissolve
    "레오 씨와의 특별했던 축제를 기점으로 우리 사이엔 아무런 진전이 없었지만 그래도 예전보다는 조금 더 가까워진 것 같다."

    "레오 씨는 요근래 나에게 작곡하신 음악을 들려주시는것을 즐기는 모양이신지 자주 찾아와 음악을 들려주신다."

    "음악을 듣다보면 잘 안풀리는 일들도 술술 풀어넘길 수 있을거 같은 느낌을 한 가득 받게 된다."

    "레오 씨의 음악으로 힐링을 하는게 좋아서 같은 회사인 츠카사에게도 레오 씨와의 일들을 말해주었다."

    scene background_es_self with dissolve
    show tsukasa wow with dissolve
    tsukasa "네? 레오 씨가 music을요?"

    n "응...?? 왜??"
    
    show tsukasa nomal with dissolve
    tsukasa "레오 씨는 정말 친밀한 사이가 아니라면 music을 들려주시는 분이 아니십니다."

    tsukasa "설령, 친밀하다 해도 직접 찾아가면서까지 들려주지는 않죠."
    
    show tsukasa happy with dissolve
    tsukasa "후후, 아마도 누님을 특별하다고 생각하시는 모양이군요."

    scene background_es_talking with fade
    "츠카사에게 들었을땐 놀랐던건 사실이다."

    "왜냐하면, 나는 레오 씨를 좋아하기 때문이다."

    "그런데, 레오 씨는 그런 마음은 아니신거 같아 씁쓸한건 어쩔수 없는거 같다."

    scene background_es_talking
    with Pause(2)
    play sound "Phone.mp3"
    

    "지금쯤이라면 레오 씨가 찾아오실 시간인데 시간이 지나도 오질 않으셔서 의문을 품던 도중, 레오 씨한테서 문자가 왔다."

    scene background_es_talking
    with Pause(1)

    leo "(와하핫! 오늘 정말 세기의 음악이 작곡됐어! 그런데 오늘은 거기까지 가는건 힘들어서 직접 와줘!)"

    "마침 쉬려고 생각하고 있던 찰나라 레오 씨를 만나러 가기 위해 가볍게 외투만 걸치고 레오 씨가 알려주신 장소로 발을 옮겼다."
    
    scene background_es_in with dissolve
    with Pause(1)
    play sound "walkfoot.mp3"
    
    n "(음...? 여기는 회사에서 본 적 없는 곳인데...내가 안가봤나?)"

    "레오 씨가 보내준 장소는 아직 나도 회사에서 가보지 못한 것 같은 곳이였다."

    "장소를 보아하니 여기는 사람이 잘 지나가지 않는 장소에다가 조금 구석진 곳에 있어서 나도 몰랐던 것 같다."

    scene background_es_in
    with Pause(1)

    "알려주신 장소에 도착하니 평소 신경쓰지 않았던 곳에 문이 하나 있었다."

    play sound "door.mp3"
    "혹시 여기인가 싶어 문을 열자 악보들이 바닥에 널부러져 있었다."

    scene background_music_room with dissolve
    "조금 더 들어가자 피아노를 막 치려는 참인지 준비하고 있던 레오 씨가 보였다."

    n "레오 씨!"
    
    show leo nomal with dissolve
    leo "오오 드디어 왔구나 [player_name]!!"

    n "우와...여기는 처음오는거 같은데...늘상 여기에서 작업하시는거에요?"
    
    show leo happy with dissolve
    leo "응! 여기는 원래 창고같은 방이였는데 내가 싹 개조했어!!"
    
    show leo very happy with dissolve
    leo "그건 그렇고 문자로 봐서 알겠지만 이번 노래는 엄청 역작이야!! 자자 빨리 앉아~!"
    
    "레오 씨는 내 팔을 끌어당겨 피아노 의자에 앉게한 후, 본인도 바로 옆자리에 앉았다."

    "그러고보니 여기에 있는 악보만 단정하게 놓여져 있었다."

    n "레오 씨, 왜 이 악보들만 단정하게 놓여져 있는 건가요?"
    
    show leo nomal
    leo "이게 그 역작이니까! 소중하게 대해줘야해!"
     
    stop music fadeout 2.0
    scene background_music_room with dissolve
    "그렇게 말씀하시면서 웃으시는 레오 씨는 그 어떤 사람보다도 훨씬 예쁘게 웃고 있었다."
    
    play music "For.mp3" loop
    scene background_music_room
    with Pause(2)
    
    "레오 씨의 피아노 연주가 시작되었다."

    "여태까지 들려주셨던 노래는 힘이 되는 느낌이였다면 이번 노래는 사랑하는 사람을 위한 애정이 담겨있는, 그런 느낌의 곡이였다."

    "문득, 피아노를 치는 레오 씨의 모습은 어떠실까 싶어 곁눈질로 살짝 보니 아까까지 해맑게 웃던 모습은 사라지고 어딘가 긴장하는 모습으로 피아노를 연주하시고 계셨다."
    
    stop music fadeout 2.0
    show leo hmm with dissolve
    leo "저기, 아까부터 계속 쳐다보는데....내 얼굴에 뭐라도 묻었어?"

    n "앗, 그..그게.... 계속 보려던건 아니고.."

    "갑자기 물어보신 탓에 머릿속에서 생각이 정리되지 않아 말을 계속 얼버무렸다."
    
    show leo happy with dissolve
    leo "와하핫! 지금 [player_name]의 모습 완전 웃겨!"

    "그 말에 그만 부끄러워져 잔뜩 빨개져버린 얼굴을 오른손으로 가리며 고개를 돌렸다."
    
    show leo hmm
    leo "....."
    
    play music "Noblesse.mp3" loop
    scene background_music_room
    "한참동안 나를 바라보던 레오 씨는 피아노 의자에 기대 있던 나의 손 위에 자신의 손을 포개어 올리셨다."

    n "...레, 레오씨??!!" with hpunch

    "아마 지금쯤 귀까지 빨개졌을것이 분명하다.."
    
    show leo nomal with dissolve
    leo "사실...이 노래는 널 위해서 쓴거야."

    "갑자기 귓속말로 속삭이시자 깜짝 놀라 그만 고개를 돌려 뭐라도 대꾸해야겠다고 생각한 순간, 레오 씨와 눈이 딱 마주쳐버렸다."

    scene background_music_room with dissolve
    with Pause(1)

    "그렇게 한참을 쳐다보던 중, 사고날의 기억들이 마치 아이디어가 떠오르는 듯이 서서히 돌아오기 시작했다."

    n "아.."
    
    "기억이 서서히 돌아오는것을 느끼자 그만 이상한 목소리가 나왔다."
    
    show leo hmm with dissolve
    leo "왜 그래?"

    n "저 사실...사고 났을때의 기억이 전혀 떠오르지 않았거든요."
    
    show leo wow
    leo "....!!"

    n "그런데 방금 그때 기억이 모두 기억났어요..그 때 저를 도와주시려 하셨던 분이 레오 씨였나요?"
    
    show leo happy
    leo "나 맞아!!" with hpunch
    
    scene background_music_room with dissolve
    n "그런데, 왜 처음부터 저한테 말씀해주시지 않으셨던 거에요?"

    n "저는 절 도와주려하신 분이 누구이신지 계속 찾고 있었는데.."

    "나의 물음에 레오 씨는 잠시 아무런 말씀도 하시지 않으시다 이내 천천히 말씀하셨다."

    scene background_music_room
    show leo sad with dissolve
    leo "왜냐하면....그때 나는 널 잡아주지 못했으니까.."

    n "네??"

    leo "난 그날일을 계속 후회하고 있었어..."

    leo "그날, 네가 계단에서 넘어져 구급차에 실려가고, 입원실에 누워있는 모습을 보고 난 큰 무력감을 느꼈어.."

    leo "'왜 그때 더 나서서 잡아주지 못했을까' '조금만 더 팔을 뻗었더라면 이런 일은 없었을텐데..' 라며 일 때문에 잠시 귀국하게 되었을때에도 비행기 안에서 계속 생각했어."

    leo "사실은, 일이 다 끝나고 회사로 돌아왔을 때, 혹시 만난다면 말해줘야겠다고 계속 생각하고 있었어."

    leo "하지만, 네가 웃으며 말하는 모습을 보니까 말해주는게 두려워졌어.."

    leo "혹시 사고날 일 때문에 나를 싫어하게 되면 어쩌지 라는 생각이 계속 머릿속을 꽉 차게 해서..결국 나는 말을 하지 않기로 결정한거야."
    
    scene background_music_room
    "레오 씨의 말씀에 마음 한 구석이 따끔따끔 거렸다."

    n "아니에요 레오 씨, 레오 씨가 그때 도와주시려 해주셔서 얼마나 다행이라고 생각했는지 몰라요...정말 감사해요 레오 씨."

    "그리고 하나의 의문이 들었다. 나는 레오 씨를 좋아하지만, 레오 씨는 나를 좋아하시지 않으시는데 이렇게 까지 잘해줄 필요가 있나라는 생각이 들었다."

    n "그런데 레오 씨, 왜 이렇게 저한테 잘해주시는건가요..?"
    
    show leo unhappy with dissolve
    leo "그거야...나는 너를 좋아하니깐.."

    leo "좋아하니까 그런거야. 다른 사람들한테는..스오한테도 이렇게까지 해주지 않아."

    leo "너라서...그런거야."
    
    scene background_music_room with dissolve
    "갑자기 들은 레오 씨의 고백에 순간 아무런 생각도 들지 않았지만, 이내 짝사랑이 아니였다는것에 그 어느순간보다도 기뻤다."

    n "저도..! 저도 사실은..레오 씨를 좋아하고 있었어요.."

    n "가을 축제에 갔을 때에는 제가 기대한 그런건 아니였지만, 정말 설렜었고..모처럼 꾸몄을 때 레오 씨가 예쁘다고 말씀해주셨으니깐요.."

    "머리가 새햐얘진 상태에서 말을 하려니 제대로 말이 정리되지 않아 두서없이 나왔다."

    "부끄러워하는 내 모습을 레오 씨가 똑바로 쳐다보는게 느껴진다."

    leo "고개 숙이지 말고 나를 봐줘, [player_name]."

    "레오 씨의 말씀에 부끄럽지만 고개를 똑바로 들어 레오 씨를 쳐다보자 레오 씨는 그 누구보다도 행복한 듯한 미소를 보이고 계셨다."

    scene 6 with fade
    leo "네가 나랑 같은 마음이라 정말 기뻐.."

    leo "나는 네가 웃는 모습이 좋아. 그 웃는 얼굴을 꼭 잃지 않게 해줄께."

    "시선이 엇갈리지 않고 똑바로 이어진다. 우리는 서로의 웃는 모습을 그저 한동안 바라보았다."

    scene background_white with fade
    "6번 갤러리가 해금되었습니다."

    "레오_해피엔딩"
    stop music fadeout 2.0

    scene black with dissolve
    with Pause(2)
    play sound "heart.mp3"
    
    scene black
    with Pause(7)

return



#해피엔딩 히메루

label happyending_HiMERU:

    $ persistent.ending4 = True
    $ renpy.save_persistent()

    scene background_HiMERU with fade
    with Pause(1)
    play music "main.mp3" loop
    
    scene background_es_talking with dissolve
    "HiMERU 씨와 바다 데이트(?)를 다녀오고 우리 사이에는 아무것도 변하지 않았다."

    "...사실은, 아무것도 안변한건 아니고..HiMERU 씨가 최근에 나랑 같이 계시는 횟수가 늘었다."
    
    "어떻냐고 하면..."

    scene background_es_in with fade
    n "으으....꽤 무겁네..."

    scene background_es_in
    with Pause(1)

    n ".....??"

    n "HiMERU 씨..??"

    show HiMERU nomal with dissolve
    "이건 HiMERU가 들테니 [player_name] 씨는 잠시 쉬세요."

    "내가 힘들일을 하고 있으면 어느샌가 오셔서 도와주신다거나.."
  
    scene background_es_talking with fade
    n "오늘따라...일이 더 많은거 같은데...."

    scene background_es_talking
    with Pause(1)

    n "(누구지...?)"

    n "네, 들어오세요."
    
    show HiMERU happy with dissolve
    HiMERU "실례하겠습니다. 오늘 지나가다가 맛있어 보여 사왔습니다. 시간 되신다면 HiMERU와 같이 드시지 않으시겠나요?"
    
    "힘든걸 귀신같이 아시고 간식같은 달달한걸 사오신다던가...같은..."

    scene background_es_talking with fade
    with Pause(1)

    "물론 평소에도 가끔씩 이러셨지만, 왠지 그날을 기점으로 빈도가 좀 더 늘어난것 같다."

    "싫다는것은 절대 아닌데, 우리가 사귀는 사이도 아니고...이러시니 조금은 기대하게 되어버린다.."

    "마침 오늘 HiMERU 씨와 회의가 있으니 회의가 끝나면 말씀드려보는게 좋을거 같다.."

    scene background_white with fade
    with Pause(1)

    scene background_es_talking with dissolve
    show HiMERU nomal with dissolve
    HiMERU "...해서 정리하면 될거 같네요."

    n "네, 그럼 잘 부탁드릴께요 HiMERU 씨."
    
    show HiMERU happy with dissolve
    HiMERU "HiMERU 에게 맡겨주세요."

    "드디어 회의가 다 끝나고 이제 말씀을 드려야 할 거 같아 타이밍을 본다.."
    
    show HiMERU nomal with dissolve
    HiMERU "[player_name] 씨, 혹시 시간 되시나요?"

    "이때가 타이밍인거 같아 말을 꺼내려 했는데, HiMERU 씨가 먼저 말씀을 건네셨다.."

    n "네?"
    
    show HiMERU happy with dissolve
    HiMERU "오늘 HiMERU와 같이 어디 좀 같이 가주셨으면 합니다."

    n "앗, 네에..."

    "얼떨결에 승낙을 해버렸지만..돌아가는 길에 말씀을 꼭 드리자고 다짐 아닌 다짐을 했다."

    n "(그래, 돌아가는 길에 말씀드리자..!)"

    scene background_white with dissolve
    with Pause(1)

    scene background_pos_night with dissolve
    play sound "walkfoot.mp3"
    "드디어 회사 업무를 모두 마치고, 회사 밖으로 나오자 HiMERU 씨가 기다리고 계셨다."

    n "HiMERU 씨..!"
   
    show HiMERU nomal with dissolve
    HiMERU "아, 오셨군요 [player_name] 씨."

    n "업무가 이제 끝나서...혹시 많이 기다리셨나요?"
    
    show HiMERU happy with dissolve
    HiMERU "아닙니다. HiMERU 도 방금 나왔습니다."
    
    show HiMERU nomal with dissolve
    HiMERU "그럼 가실까요?"
    
    scene background_pos_night with dissolve
    scene background_ex with dissolve

    "무슨 이유인지도 모르고 HiMERU 씨를 따라 그저 걸었다."

    "어디로 가는건지를 여쭤봐도 대답해주시지 않아 그냥 따라가기로 했다."
    play sound "walkfoot.mp3"

    scene background_night_home_walk with dissolve
    show HiMERU nomal with dissolve
    HiMERU "여기입니다."

    "HiMERU 씨를 따라 도착한 곳은 누군가의 집 앞이였다."

    n "저...HiMERU 씨..여기는 누구 집인가요?"
    
    scene background_night_home_walk
    show HiMERU hmm
    HiMERU "그거야 당연히 HiMERU의 집이죠?"

    "갑자기 HiMERU 씨의 집에 도착한 나는 당황스러웠다..나를 왜?"
    
    show HiMERU happy with dissolve
    HiMERU "자, 우선 들어가실까요?"
    
    play sound "door.mp3"
    scene background_home with dissolve
    with Pause(1)
    "집으로 들어가자 깔끔하고 정돈된 가구들이 보였다."
    
    show HiMERU nomal with dissolve
    HiMERU "아무데나 앉아계세요. HiMERU는 옷을 좀 갈아입고 오겠습니다."
   
    scene background_home with dissolve
    "나는 아직까지 상황을 이해못하고 있는데, HiMERU 씨는 나와 다르게 이 모든 상황이 그저 익숙한 듯 아무렇지도 않게 행동하신다."

    "이런 상상하긴 정말 싫지만...온갖 별의 별 생각이 다 든다.."

    n "(이런 상황에서 기대를 하는 내가 참 싫다...)"
    
    stop music fadeout 2.0
    HiMERU "저, [player_name] 씨? 지금 조금 곤란한 상황입니다만...조금 도와주실 수 있으실까요?"

    n "앗, 네!"

    "무슨 상황이기실래 그러시는건지 의아해하며 HiMERU 씨가 계신 방 문을 노크했다."

    scene background_home with dissolve
    with Pause(1)

    n "...!!"
    
    play sound "door.mp3"
    "방 문이 열리더니 갑자기 HiMERU 씨가 팔을 잡아당겼다."

    "갑작스럽게 일어난 일이라 속수무책으로 끌려 들어가버려 순식간에 벽에 밀착되었다."

    "뭔가 지금이 타이밍이라고 내 머릿속에서 말하는 듯 해 상황이 좀 그렇지만...말하기로 했다."

    n "저....HiMERU 씨...? 갑자기 왜 이러시는 건가요?"
    
    show HiMERU nomal with dissolve
    HiMERU "그거야...이런 시간에 집에 애인을 초대하는건....이유가 있으니까 그런거 아닐까요?"

    "HiMERU 씨의 말씀에 머릿속에 물음표가 한가득 나타난것 같다."

    n "네...? 애인이라뇨..? 제가요?"
    
    show HiMERU hmm with dissolve
    HiMERU "?? HiMERU의 애인은 [player_name] 씨잖아요?"

    n "네..?????"

    HiMERU "네??"

    scene background_home with dissolve
    with Pause(1)

    "....우선 우리는 이게 어떻게 된 상황인지 같이 침대에 걸터앉아 정리부터 하기로 했다."

    n "그러니까...바다에 같이 간 그날 이후에 저희가 사귀는 사이라고 생각하셨던건가요?"
    
    show HiMERU hmm with dissolve
    HiMERU "네, 그때 어필을 충분히 했다고 HiMERU는 생각합니다만.."
    
    scene background_home with dissolve
    n "...그런데 사귀자고 말씀 안하셨잖아요..?"

    "내가 말하자 HiMERU 씨가 곰곰히 생각하시더니 아차하는 표정이다."

    n "그럼 바닷가에 간 이후로 저를 만나러 오시거나 더 자주 같이 있었던 이유도 설마..?"
    
    show HiMERU hmm with dissolve
    HiMERU ".....네..같이 있고 싶어서.."
    
    scene background_home with dissolve
    "조금 작게 중얼거리시는 그 모습이 분명 나보다 덩치가 훨씬 큰데, 지금만큼은 굉장히 작아보여 귀여웠다."
    
    show himeru sad
    HiMERU "HiMERU가 이런 실수를 하다니....면목없습니다.."
    
    show HiMERU nomal with dissolve
    HiMERU "하지만, 이렇게 된 이상. 다시 제대로 말씀드리겠습니다."
    
    play music "Noblesse.mp3" loop
    HiMERU "HiMERU는, 저는 [player_name] 씨를 좋아합니다. HiMERU와 사귀어주세요."
    
    scene background_home with dissolve
    "방금전의 모습은 어디가고 조금 진중한 얼굴로 날 바라보며 말씀하신다."

    n "후후, 네 좋아요. 저도 HiMERU 씨를 좋아해요!"

    "내 말이 끝나자마자 바로 침대에 날 끌어당겼다."

    "나란히 침대에 누워버린 탓에 뭔가 묘한 분위기가 생겼다."

    "분위기에 휩쓸려 서서히 다가가 입을 맞췄다."
    
    show HiMERU nomal with dissolve
    HiMERU "이런,나이가 훨씬 많은 어른이 이러다니...HiMERU는 나쁜 어른이네요."

    n "후후, 그럼 제가 잡아가도 괜찮나요?"
    
    "HiMERU 씨가 빤히 날 쳐다보신다."

    scene 8 with fade

    HiMERU "후후, 원래는 [player_name] 씨가 저를 좋아하게 하려 했는데, 제가 좋아하게 되어버렸군요."

    n "하핫, 저도요!"

    scene background_white with dissolve
    "우리는 그렇게 한동안 침대에 누워 서로를 한참동안 마주보며 웃었다."

    "8번 갤러리가 해금되었습니다."

    "HiMERU_해피엔딩"
    stop music fadeout 2.0

    scene black with dissolve
    with Pause(2)
    play sound "heart.mp3"
    
    scene black
    with Pause(7)

return

#해피엔딩 쿠누기

label happyending_kunugi:
    $ persistent.ending5 = True
    $ renpy.save_persistent()
     
    scene background_kunugi with dissolve
    with Pause(1)

    scene background_white with dissolve
    with Pause(1)

    play music "main.mp3" loop

    "크리스마스날의 일을 기점으로 우리는 한동안 바빠서 서로 얼굴을 볼 시간도 없었다."

    "연말에는 안그래도 상당했던 일이 더 늘어나 눈코뜰새 없이 그저 바쁘게 업무를 처리하는 나날의 연속이였다."

    "쿠누기 씨도 마찬가지 이신지 원래 계시던 부서에서 어느 때보다 바쁘게 일하시는 것 같았다."

    "그렇게 우리는 다음 년도 봄, 여름, 가을이 다 지나도록 서로 바빠 만나면 가볍게 인사를 하거나 커피를 같이 마신다던가 하는 일 외에는 만날 기회가 현저히 줄어들게 되었다."

    "그리고 시간은 흘러....벌써 내일이면 또다시 크리스마스가 된다."
    
    scene background_home with dissolve
    n "(올해는 저번년도와는 다르게 회사 규모가 더 커지면서 일이 어쩔수없이 늘어나서..누굴 만나려고 해도 저번보다 더 만날 일이 없었네..)"

    n "(그래도 우리회사는 이브날에도 쉬는날로 해줘서 참 다행이야....내일은 혼자 집에서 뭐하는게 좋으려나...)"

    "근처에서 그루밍을 하던 도도를 보며 생각을 했다."

    scene background_home
    with Pause(1)
    play sound "Phone.mp3"
 
    n "누구지..?"
    
    "지금은 조금 늦은 저녁시간이라 딱히 연락올 사람이 없을텐데, 핸드폰이 울렸다."

    "문자를 보낸 사람은 다름아닌 쿠누기 씨였다."

    kunugi "(쿠누기 입니다. 혹시 내일 예정 있으신가요?)"

    n "(아니요, 예정은 없는데 무슨일이세요?)"

    kunugi "(내일은 크리스마스 이브인데, 저랑 같이 시내에 가시지 않으시겠습니까?)"

    "쿠누기 씨의 문자를 보자 작년, 크리스마스때의 일이 떠올랐다."

    "그때는 광장에서 만나서 갑자기 같이 다니게 되었지만, 지금은 약속을 잡고 만나는 거라 기대가 되기 시작한다."

    n "(네, 좋아요! 어디에서 뵐까요?)"
    
    "서둘러 긍정의 답을 보내고 약속을 잡았다."
     
    scene black with dissolve
    with Pause(1)
    
    scene background_home with dissolve
    "아침이 되고, 나는 서둘러 나갈 준비를 했다."

    "저번에는 조금 높은 힐을 신었지만, 오늘은 조금 낮은 구두를 신고, 도도를 쓰다듬어 준 뒤 밖으로 나왔다."

    scene background_white with dissolve
    with Pause(1)
    
    scene background_walk_walk with dissolve
    "밖으로 나오자 차가운 공기가 훅 들어온다.."

    "오늘은 크리스마스 이브 이다보니 거리에는 출근하시는 분들이 몇분 보였다."
    
    scene background_tur with dissolve
    "작년과 똑같이 지하철을 타고 시내로 나가기로 한다."
    
    scene background_white with dissolve
    with Pause(1)
    
    play sound "woowoo2.mp3"
    scene background_moring_walk with dissolve
    with Pause(1)
    
    "만나기로 한 역에서 내려 위로 올라가 보니 크리스마스라 한껏 꾸민 백화점, 빨간 모금함, 북적거리는 사람들...."

    "작년과 별 다를것 없는 풍경이였지만 올해는 뭔가 다른느낌이 들었다."

    "아마, 작년은 혼자 아무 일 없이 시내에 왔지만, 올해는 약속 때문에 시내에 와서 그런건가 싶은 생각도 있었다."

    "주변을 둘러보며 쿠누기 씨를 찾았다."

    n "(아, 저기 계신다!)"

    "쿠누기 씨는 광장 벤치에 앉아 책을 읽고 계셨다."

    "그 모습마저 작년의 크리스마스를 떠올리게 해 웃음이 나왔다."
    
    play sound "foot.mp3"
    n "쿠누기 씨!"
    
    show kunugi nomal with dissolve
    kunugi "아, 오셨군요. 오늘 날씨가 꽤 춥네요."

    n "네...작년보다 더 추운것 같아요..하하"

    kunugi "추우니까, 빨리 실내에 들어갑시다. 어디로 갈까요?"
    
    scene background_moring_walk with dissolve
    "잠시 고민하다, 평소에 정말 가보고 싶었던 카페에 가자고 했다."
     
    play sound "bell.mp3"
    scene background_caffe with dissolve
    with Pause(1)
    
    "카페는 역시 사람이 많았지만, 그래도 군데군데 자리가 남아있어서 다행이였다."

    n "오늘 크리스마스라 한정 메뉴가 있나봐요...!! 저는 이걸로 할건데, 쿠누기 씨는 뭘로 하실래요?"
    
    show kunugi nomal with dissolve
    kunugi "저는 따뜻한 아메리카노로 하겠습니다."
    
    scene background_caffe with dissolve
    "음료를 받은 후, 우리는 운좋게 창가자리에 자리를 잡았다."
    
    show kunugi nomal with dissolve
    kunugi "요새 회사 일은 어떤가요?"

    n "일이 많기는 한데...그래도 어떻게든 해내려고 하고 있어요.."
    
    kunugi "최근, 일 처리하는 속도가 아주 빠르다고 주변에서 칭찬이 자자합니다."

    kunugi "다만, 예전에 늘 말씀했던거지만, 몸 건강이 제일 중요하니 아무리 바빠도 쉬는건 잊지 말아주세요."

    n "나름 잘 쉬려고 하고 있는데 그게 잘 안되네요..하하"
    
    scene background_caffe with dissolve
    with Pause(1)
    
    "오랜만에 이렇게 음료를 마시며 쿠누기 씨와 가벼운 담소를 나누고 있으니 시간이 느리게 흘러가길 바라게 된다."
     
    scene background_moring_walk with dissolve
    with Pause(1)
    play sound "foot.mp3"

    "음료를 다 마시고, 카페를 나온 우리는 주변 상가를 구경하기로 했다."
    
    "그 사이 새로 생긴 가게들도 있고, 신상품이라면서 새로운 물건들을 구경하는 것이 즐거워 시간 가는줄 모르고 구경했다."
    
    scene background_white with dissolve
    with Pause(1)

    scene background_night_000 with dissolve
    "저녁은 이번에도 쿠누기 씨가 미리 예약을 해 놓아주셔서 기다리는 일 없이 저녁을 먹을 수 있었다.."

    "이 시간이 계속 되길 바라지만..애속하게도 시계를 확인해보니 벌써 집에 갈 시간이 다 되어간다.."
    
    show kunugi hmm with dissolve
    "아쉽지만 티를 내지 않으려고 쿠누기 씨를 슬쩍 보자 쿠누기 씨도 뭔가 아쉬운 듯한 표정으로 시계를 보고 계셨다."
    
    show kunugi no with dissolve
    kunugi "그....."

    n "네?"
    
    stop music fadeout 2.0
    show kunugi nomal with dissolve
    kunugi "시간은 벌써 조금 있으면 늦은 시간입니다만....조금만 더, 같이 있어주시겠습니까?"
    
    scene background_night_000 with dissolve
    "물어보는 쿠누기 씨의 얼굴은 평소와 다르게 어딘가 긴장된 듯한 얼굴이였다."
    
    scene background_ex with dissolve
    with Pause(1)
    play sound "foot.mp3"
    play music "after.mp3" fadein 2.0 loop
    
    "쿠누기 씨의 제안을 승낙하고 우리는 사람이 거의 없는, 한적한 길거리를 그저 걸었다."

    "밤이 되니 공기는 더 차가워졌지만 묘하게 더 상쾌한 것도 있어 그 공기를 즐기고 있자 쿠누기 씨가 천천히 말씀을 꺼내신다."
    
    stop music fadeout 2.0
    show kunugi nomal with dissolve
    kunugi "저는 지금 회사에 들어가기 전에는 하고 싶은것도 많고, 꿈도 많았던. 여느 학생과 다르지 않는 평범한, 그런 학생이였습니다."
    
    show kunugi nomal with dissolve
    kunugi "하지만, 어른이 된 후. 하고 싶은 것도 꿈을 꿀 새도 없이, 주변을 살필만한 여유도 없이..그저 앞만을 향해 달려오자 문득 뒤를 돌아보니 사회적이나 비즈니스적으로는 그래도 어느정도는 익숙해졌지만, 누군가와 개인적으로 연을 쌓는 것에 많이 미숙한 어른이 되어있었습니다."

    kunugi "저는 아마 살면서 평생 누군가와 함께 하지는 못할 것 같다고 생각하며 지내왔을 때."
    
    show kunugi nomal with dissolve
    kunugi "당신이, 지금 회사에 오고 나서부터 제 생각이 조금씩 달라지기 시작했습니다."

    kunugi "주변을 제대로 살필 줄 알고, 모두를 평등하게 대하고, 맡은 일에는 늘 최선을 다해 성실하게 임하는 당신을..아마 누가 좋아하지 않을 수 있을까요."

    kunugi "맨 처음에는 그저 회사 선배로써, 곤란한 일이 있을때는 도와주고, 혼나거나 힘든 일이 있을때는 위로해주는, 그런 선배로써 옆에 있으려 했습니다."

    kunugi "하지만, 시간이 지나면서 저의 마음은 제가 당신의 옆에 있고 싶던 모습과 조금씩 달라지고 있었습니다."

    kunugi "제가 학창시절 이후로, 다시는 느끼지 못할거라 스스로 예상했던 감정들을 말이죠."

    kunugi "처음에는 한 순간의 감정일게 분명하다, 나보다 몇살이나 어린 사람에게 무슨 감정을 품는 것이아며 저 스스로를 매도하고 다그쳤지만..."

    kunugi "그럼에도 어쩔 수 없이 저는 당신을 사랑하게 되었습니다."

    kunugi "저는...당신을 좋아합니다."
    
    scene background_ex with dissolve
    "잔잔하게 흘러들어온 고백에 마음이 간질간질 해지며 이내 심장이 두근거리기 시작한다."

    "얼굴이 달아오르는게 느껴진다.."
    
    show kunugi nomal with dissolve
    kunugi "저는 어느 쪽을 택하든 당신의 행복을 최우선으로 생각합니다."

    kunugi "그저 당신에게 제 마음을 전하고 싶었을 뿐, 받아주지 않아도 괜찮습니다."
    
    scene background_ex
    n "저도..저도..! 좋아해요.." with hpunch
    
    scene background_ex
    play music "Noblesse.mp3" loop
    "쿠누기 씨의 말이 끝나기도 전에 서둘러 말했다.."

    n "사실, 작년 크리스마스 때 부터 호감은 있었는데...저랑은 다른 감정이신거 같아...그냥 말 하지 않으려고 생각하고 있었어요.."

    "꾹 눌러왔던 말들을 하나하나 전하자 쿠누기 씨가 작게 웃으며 가까이 다가오신다."

    "코트 자락을 쥐던 내 손을 조심스럽게 잡아 깍지를 낀다."
    
    scene 10 with fade

    kunugi "당신이 같은 마음이라고는 생각하지 못해서...지금 어떤 감정으로도 정의할 수 없을 정도로 행복합니다."

    kunugi "저를...좋아해주셔서 감사합니다. 앞으로 잘 부탁드립니다."

    n "저야말로...잘 부탁드려요..!"

    scene background_white with dissolve
    "10번 갤러리가 해금되었습니다."

    "쿠누기_해피엔딩"

    stop music fadeout 2.0

    scene black with dissolve
    with Pause(2)
    play sound "heart.mp3"
    
    scene black
    with Pause(7)

return

#게임 시작 전 로고 이미지    
image splash = "splash.png"
label splashscreen:
    scene black
    with Pause(2)
        
    show splash with dissolve
    with Pause(3)

    scene black with dissolve
    with Pause(2)

    return
        
        
            
        

        









                

             


    