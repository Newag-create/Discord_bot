import random
import requests
def gen_pas(pass_length):
    elements = "@qwertyuiopasdfghjklzxcvbnm1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
def coin_toss():
    coin = ["Co wypadło: orzeł | What came out: eagle", "Co wypadło: reszka | What came out: tails"]
    toss = random.choice(coin)
    print(toss)
    return toss 
def emoi():
    e = "😀🍹🌜🙍🏻🎾☢️🙍🏽‍♀️🙍🏻‍♀️👧🏼⚗️🤵🏾‍♀️👦🏼🆗🏳️🧬🤵🏾‍♂️👦🏽®️🧑🏿🆕©️🧒🏿🏁🔭🆒⁉️🔣🔡🔢🔠✔️♻️💱™️🌡️❌🧻❗‼️🟰✖️❓⏸️➖⏮️▶️➗⚛️➕⬅️⏪⏩🔃☯️☦️✝️⬇️⬆️➡️🗝️🛒⚔️🧲🔒🏹🛁🛠️🌊☁️🎺🌎📏📋✂️💎☣️🔔⛈️🕶️🌠🌧️⛄🏔️🌩️🌠🚙🌕☔☄️🕒🛸🌘⏳🚉🎈🚦🏦🚊🌍🚂🚃🏡⛰️🚄🛝⛲🕌🏖️🌃🗻🪨⛩️🧭🏗️🎆♟️🥫🏝️🏕️⚽🏛️🎊🌋🏒🎯🧱🌏🪡⛳🥊🧶⛸️🎮🎁🥋🎳🎖️🏐🎯🎉🎃🥏🎄🏅🏆🏀☕🥎🍧😃🧊😄🍆🪀🍪🍮🍜🎲🎱🧩♠️🎫🀄🍡🍪🥞🍳🍾🫜🥫🍘🍨🌽🍚😁🫕🍣🥫🥪🪺🥑🍃🍌🥚😆🫠😇🥰😜😍🙃😋🌲🫥👨‍💻😶‍🌫️🤑🙂‍↔️👨‍🍳🥵🥶🤠😎🥳🧐😲🥱💀👻😻💗💌🌶️❤️💯👋🐣🌵🦐🐬🪼🦘🐍🤴🌹🍄🧖🦍🦙🐑🫂🧑‍🔬🍇🦹‍♂️👍🍋‍🟩🧑‍🚒👸🫛🍞🥐👊👮‍♂️🕷️🍒👏🌭🥞🐟🍣🧊🍲🌳🦞🐒🫶🧔🌯🙎‍♀️👧🦍👩‍🌾👴🧊🍠🦧🤺🌶️🦝🍚🦓🍕🚴🍿🦃🍂🙎🐺🧓🦏🦚👊✌️🐟👩‍🦱🦖"
    emoij = random.choice(e)
    print(emoij)
    return emoij
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
def random_fact():
    facts = ['Co to są zmiany klimatyczne: zmiany klimatyczne to długotrwałe przekształcenia klimatu Ziemi spowodowane głównie działalnością człowieka, a ich skutki są poważne i dotyczą również Polski, ponieważ wpływają na pogodę, zdrowie, gospodarkę i środowisko | What climate change is: climate change is the long-term alteration of Earth s climate mainly caused by human activity, and its effects are serious and also affect Poland, because they impact the weather, health, economy, and the environment','Co robić: oszczędzać energię i wodę | What to do: save energy and water','Co robić: wybierać transport niskoemisyjny | What to do: choose low-emission transport','Co robić: ograniczać marnowanie żywności | What to do: cut down on food waste','Co robić: wspierać odnawialne źródła energii | What to do: support renewable energy sources','Co robić: sadzić drzewa i chronić tereny zielone | What to do: plant trees and protect green areas','Co robić: edukować się i podejmować świadome wybory konsumenckie | What to do: educate yourself and make conscious consumer choices','Przyczyny: emisje gazów cieplarnianych pochodzące z działalności człowieka | Causes: greenhouse gas emissions from human activities','Przyczyny: spalanie paliw kopalnych (węgiel, ropa, gaz) – energetyka, transport, przemysł | Causes: burning fossil fuels (coal, oil, gas) – energy, transport, industry','Przyczyny: rolnictwo – emisje metanu z hodowli zwierząt, podtlenku azotu z nawozów | Causes: agriculture – methane emissions from livestock, nitrous oxide from fertilizers','Przyczyny: wylesianie – mniej drzew oznacza mniej pochłaniania CO₂ | Causes: deforestation – fewer trees means less CO₂ absorption','Przyczyny: przemysł – produkcja cementu, chemikaliów, tworzyw sztucznych | Causes: industry – production of cement, chemicals, plastics']
    fakt = random.choice(facts)
    print(fakt)
    return fakt
