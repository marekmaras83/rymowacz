#! /usr/bin/python3
import re

VOVELS = ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y']
CENTRALIZED_DIPHTHONGS = {
    'i': VOVELS,
    'j': ['e', 'a'],
}
TONES_WITH_EXCHANGEABLE_VOVELS = [
    ["u", "ó"],
    ["i", "j"],
]

BASIC_DICTIONARY = ['brukselka', 'wielka', 'taka', 'blada', 'takie', 'jej', 'to', 'wszyscy', 'kłótnie', 'oprze', 'feler', 'tu', 'drodzy', 'mój', 'cebula', 'nos', 'buraku', 'prędzej', 'zginiemy', 'brzuszku', 'trochu', 'dla', 'jakoś', 'wtorku', 'jaka', 'żyje', 'swary', 'przy', 'co', 'klepie', 'fasoli', 'naraz', 'głupie', 'bo', 'wasze', 'spać', 'pietruszka', 'zatyka', 'pani', 'rozsądzi', 'groch', 'lecz', 'rzepo', 'gorzej', 'żony', 'żonę', 'krzepka', 'szczypiorku', 'ja', 'tutaj', 'widzieliście', 'no', 'doń', 'od', 'zmyka', 'odpowiada', 'pan', 'krewka', 'po', 'jak', 'tylko', 'straganie', 'mnie', 'seler', 'płaczą', 'wnet', 'już', 'marchewka', 'więdnie', 'tak', 'dzień', 'leżę', 'lepiej', 'mieć', 'targowy', 'westchnął', 'stroni', 'czerwony', 'burak', 'może', 'się', 'koprze', 'nas', 'pusta', 'chuda', 'jest', 'kapusta', 'niech', 'cóż', 'słyszy', 'czybyś', 'bądź', 'na', 'cebuli', 'smutnie', 'coraz', 'spójrz', 'chcę', 'rzecze', 'rozmowy', 'zaperzyła', 'moi', 'takiej', 'tą', 'głowa', 'panie', 'zupie', 'słychać', 'kalarepka', 'grochu', 'tam', 'dziwić', 'buraczą', 'chciał', 'gramoli', 'gdzie', 'dzięki', 'głos', 'rzepę', 'czuli', 'ta', 'nie']
BASIC_DICTIONARY += ['nową', 'krakowskiéj', 'szpieg', 'swary', 'chołodziec', 'kulę', 'nowo', 'mocno', 'znam', 'dalsze', 'gościom', 'pyta', 'zasięgała', 'kuca', 'częściéj', 'jakie', 'barbarzyństwa', 'ryby', 'twardo', 'dosyć', 'ażeby', 'uparta', 'szły', 'napełniając', 'spójrzéć', 'różnica', 'tajnie', 'domów', 'krzyk', 'korelicze', 'swoje', 'plac', 'powód', 'wodę', 'drzew', 'mały', 'zaczerwienione', 'opis', 'wzroście', 'posiedzenie', 'myślami', 'roskrzyżował', 'granicznych', 'wespazjanus', 'żołniersczyzny', 'żołnierza', 'konikach', 'mami', 'morzu', 'uszczułem', 'zacność', 'zdala', 'biegu', 'ukryte', 'jest', 'rozejm', 'inne', 'spały', 'kogo', 'przestępując', 'myśl', 'rąk', 'gromi', 'ganku', 'dama', 'województwie', 'brano', 'buja', 'zniszczone', 'nadstawiając', 'podkomorzemu', 'pała', 'żali', 'izbie', 'ściągnęły', 'dozwolę', 'szyję', 'daczy', 'żył', 'staropolska', 'laty', 'twarz', 'progi', 'żydom', 'bezprzykładną', 'ryki', 'okien', 'ubrana', 'chcę', 'skroni', 'prawem', 'żywa', 'niesą', 'ręka', 'zwady', 'ubrać', 'sprawa', 'widzi', 'najpiękniejszéj', 'powiedział', 'czarował', 'izby', 'koniu', 'mało', 'kity', 'wojewoda', 'peruce', 'gospodarskiéj', 'kłusował', 'stole', 'męszczyźni', 'weń', 'okiem', 'szybko', 'tuż', 'znaki', 'serce', 'jakoby', 'najpiękniejszego', 'mamę', 'cichym', 'nieczynności', 'słowo', 'surowy', 'tył', 'scen', 'odgadnęła', 'izba', 'pędu', 'panów', 'duma', 'biała', 'pies', 'przechrzciłby', 'smyk', 'dworem', 'czasu', 'ręki', 'światłych', 'wyczha', 'rzuciła', 'przesądów', 'zastępstwie', 'żadna', 'zamku', 'ozoru', 'damom', 'niezwyczajnéj', 'gorszącéj', 'taką', 'stają', 'ganek', 'niźli', 'katona', 'gniew', 'nieodrodził', 'proces', 'damy', 'gałeczki', 'najwymowniejsza', 'ręku', 'wiek', 'rzeczypospolitéj', 'wiodł', 'jego', 'nagła', 'roju', 'siedział', 'chcą', 'strzeleckiemu', 'łzach', 'pływać', 'ucho', 'podkomorzynie', 'końca', 'rogi', 'nieodstąpił', 'zawrócił', 'dnie', 'przystojna', 'jakiś', 'tyłu', 'stryflastych', 'kroku', 'kościuszkowskie', 'oczyma', 'ciemnozieloném', 'białopiotrowiczem', 'beczek', 'rzeczpospolita', 'trzykroć', 'który', 'podkomorzanki', 'cichy', 'swoją', 'nudzi', 'taka', 'bitwie', 'żyje', 'probie', 'dzik', 'zimny', 'niesiołowski', 'pytaj', 'swoim', 'lubi', 'małpowanie', 'szanownych', 'spokojniejszych', 'lekka', 'gonił', 'bóg', 'trzej', 'dążył', 'bezładnością', 'powozu', 'gryka', 'upodobał', 'nauki', 'sama', 'kaczki', 'widzę', 'włos', 'liść', 'ubóstwiałbym', 'wiec', 'schwytać', 'niedostrzegł', 'niby', 'zwierciadła', 'skończono', 'mimowolnie', 'zaś', 'konary', 'pijem', 'pokrewieństwem', 'lata', 'świadectwo', 'przeznaczenie', 'murami', 'cudzy', 'przyjaźń', 'pole', 'chart', 'wrzasnął', 'też', 'łani', 'niewielkim', 'nosił', 'rzecze', 'jaskrawych', 'żyta', 'gwar', 'nauką', 'taż', 'gęste', 'kurz', 'wieka', 'ogary', 'dworu', 'nię', 'rany', 'grad', 'rospowiadał', 'godni', 'miał', 'sługi', 'jedna', 'nieuszanowanie', 'mię', 'modą', 'nowym', 'wesele', 'kula', 'siano', 'podniosłem', 'jaki', 'lancy', 'kota', 'drzewa', 'temu', 'twą', 'osoba', 'litwy', 'konia', 'ciskając', 'boru', 'kórki', 'rosną', 'kości', 'czem', 'płot', 'świecił', 'cicha', 'poda', 'prawować', 'koszt', 'czule', 'petersburku', 'skał', 'mamy', 'jedli', 'cara', 'łany', 'dwadzieścia', 'muzyce', 'jaja', 'rosciągnionych', 'jeżdżąc', 'trzy', 'przykopie', 'żywą', 'cały', 'susy', 'biegało', 'grom', 'nadzieje', 'jutrzenką', 'okoliczne', 'prapradziadów', 'człowiek', 'tamek', 'głośniejsza', 'zbyt', 'worończańskim', 'uszaki', 'młodzieży', 'choć', 'psami', 'puste', 'czuję', 'widoki', 'rano', 'zakryła', 'wiele', 'cienki', 'radzi', 'lecą', 'odmieniła', 'róży', 'dramatycznych', 'pili', 'strony', 'moskiewskie', 'szmer', 'wielki', 'ledwo', 'czyje', 'panie', 'niesiołowskiemu', 'wzrok', 'trybunałem', 'sine', 'zapach', 'kopę', 'dawno', 'bursztynowy', 'rogów', 'spraw', 'oknie', 'jadą', 'razy', 'tępy', 'wleką', 'cary', 'wznosi', 'jadł', 'godzinę', 'najwyższych', 'kołem', 'zowie', 'lekce', 'moim', 'bernardyńskie', 'trybunału', 'nami', 'smutek', 'lekki', 'drogo', 'góry', 'napój', 'szczęśliwsza', 'nieutrudza', 'witac', 'ogród', 'kilka', 'kamieniem', 'lisem', 'jéj', 'dojeżdżaczów', 'czemu', 'król', 'wieś', 'tyle', 'znać', 'czym', 'mniéj', 'dojeżdżaczy', 'szafie', 'pustki', 'stały', 'własnéj', 'postrzegali', 'pływa', 'mych', 'samym', 'niéj', 'tkany', 'kosy', 'wiosny', 'trzech', 'bryki', 'uroda', 'blasku', 'poglądał', 'uszakach', 'inni', 'jakby', 'zacnie', 'maja', 'pęk', 'pogłoski', 'byli', 'papier', 'dostatecznéj', 'kumpia', 'krążące', 'nadzwyczajnie', 'duszy', 'nowych', 'swą', 'niewyraźnie', 'wojska', 'skrzydełkami', 'jeden', 'szyją', 'proste', 'kopie', 'stogi', 'kilku', 'suchym', 'starożytnej', 'wozy', 'takim', 'winy', 'padnie', 'najpiękniejszym', 'hojnie', 'alpów', 'nuda', 'przyjechał', 'wodza', 'panny', 'ziarna', 'duszę', 'rana', 'moskal', 'złoty', 'randka', 'wola', 'zwierciadlanéj', 'obmoczyłem', 'dosiedzieć', 'mówcy', 'gotyckiéj', 'dobrze', 'gazet', 'nierostrzygniony', 'wróciłby', 'oddasz', 'przy', 'obok', 'majowéj', 'ludzi', 'toczy', 'dojeżdżaczowi', 'przegrał', 'bezprzytomnie', 'ślad', 'fajt', 'źwierzyny', 'krwią', 'szukała', 'lokaj', 'zboża', 'rozeszła', 'sztandarów', 'przejrzystość', 'łeb', 'kilkn', 'wnuki', 'nieba', 'znalazł', 'sporu', 'herb', 'ważny', 'nagłe', 'miasta', 'siadłbym', 'zajeżdżają', 'kart', 'mickiewiczów', 'kąty', 'drudzy', 'gada', 'powiem', 'niemyśl', 'kara', 'potrząsając', 'roskaz', 'bicia', 'tém', 'póki', 'pytań', 'baśni', 'palcem', 'marszałkowską', 'utrzymywał', 'zgody', 'przysiągłbyś', 'kichnął', 'zaród', 'gdzie', 'rojem', 'cierpi', 'wzroku', 'woła', 'jegermajster', 'każe', 'mnich', 'obiadach', 'niewzbrania', 'kaznodzieją', 'sień', 'syna', 'boku', 'polu', 'pozłocisty', 'niepowiedziała', 'tace', 'opoka', 'zagrabię', 'podniesionemi', 'może', 'trwał', 'powtarzał', 'charty', 'dziki', 'czas', 'jacyś', 'wytnie', 'dobył', 'cóż', 'bitwy', 'rączy', 'żydzi', 'czary', 'danie', 'siedli', 'domu', 'protazym', 'nosy', 'latem', 'wspaniałych', 'znowu', 'miesiąca', 'skończyło', 'było', 'czém', 'imał', 'nieogłodzą', 'książe', 'komplementy', 'zdziwił', 'szczególniéj', 'stoją', 'rosciągnionemi', 'imion', 'szlacheckich', 'takie', 'plecie', 'winem', 'niemieszał', 'białopiotrowiczowi', 'wykli', 'chude', 'jednej', 'przez', 'tego', 'owiec', 'mego', 'trwogi', 'motyl', 'owdzie', 'dotknieniem', 'kwita', 'mowę']
BASIC_DICTIONARY = list(set(BASIC_DICTIONARY))


def get_rhymes(raw_harmony: str, word_dictionary: [str]) -> [str]:
    def create_harmony_regex_pattern(harmony):
        pattern = ""
        for letter in raw_harmony:
            exchangeable_vovels = [
                tone_vovels for tone_vovels in TONES_WITH_EXCHANGEABLE_VOVELS if letter in tone_vovels
            ]
            if exchangeable_vovels:
                pattern += f"{exchangeable_vovels[0]}"
            else:
                pattern += letter
        return pattern + "$"

    harmony_regex = create_harmony_regex_pattern(raw_harmony)
    return [i for i in word_dictionary if re.search(re.compile(harmony_regex), i)]


def is_centralized_diphthong(word_to_check: str, letter_index: int):
    for prefix, possible_suffixes in CENTRALIZED_DIPHTHONGS.items():
        if word_to_check[letter_index] == prefix and word_to_check[letter_index + 1] in possible_suffixes:
            return True
    return False


def get_single_tone_rhyme_harmony(word: str) -> (str, int):
    reverse_enumerated_word = [(i, letter) for i, letter in enumerate(word)]
    reverse_enumerated_word.reverse()

    for letter_index, letter in reverse_enumerated_word:
        if letter in VOVELS:
            if letter_index != 0 and is_centralized_diphthong(word, letter_index - 1):
                return word[letter_index-1:], letter_index-1
            else:
                return word[letter_index:], letter_index
    return '', len(word)


def get_rhyme_harmony(word: str) -> str:
    harmony = ''
    previous_harmony_letter_index = len(word)

    for harmony_id in range(2):
        single_harmony, harmony_index = get_single_tone_rhyme_harmony(word[:previous_harmony_letter_index])
        harmony = single_harmony + harmony
        previous_harmony_letter_index = harmony_index

    return harmony


if __name__ == "__main__":
    while True:
        user_word = input("Enter user_word to rhyme: ")
        rhyme_harmony = get_rhyme_harmony(user_word)
        print(f"rhyme harmony for user_word '{user_word}' is '{rhyme_harmony}'")
        print(f"available rhymes: {get_rhymes(user_word)}")
