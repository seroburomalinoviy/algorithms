"""
Учёные нашли остатки сообщений от древней цивилизации финикийцев — создателей одного из первых
 алфавитов, который использовали для торгов, дипломатии, в религиозных текстах. Финикийцы были
  морской цивилизацией, активно торговавшей по всему Средиземноморью. Для передачи сообщений
   между кораблями или поселениями они использовали систему из девяти барабанов, где количество
    ударов по конкретному барабану определяло букву сообщения, — похожая система добралась до
     наших дней в кнопочных телефонах с режимом ввода Т9.
Например, чтобы набрать U, финикийцы дважды ударяли по барабану номер 8, а чтобы набрать Z,
 они четырежды били по барабану с номером 9. Сообщение HELLOWORLD от них выглядит так:
  443355555566696667775553.

Известно, что финикийцы используют только слова из словаря. Словом является последовательность\
 буквенных символов без пробелов и иных знаков. Сообщение, которое нашли учёные, как раз связано с
  ритмами барабанов. Ваша задача — при помощи словаря расшифровать сообщение, переданное финикийцами.


Используя заглавные буквы латинского алфавита и пробелы, выведите расшифрованное сообщение.
 Гарантируется, что существует хотя бы один способ расшифровать сообщение с использованием
  слов из словаря. В случае если существует несколько способов расшифровать сообщение,
   выведите любой из них.

443355555566696667775553
3
WORLD
QUANTUM
HELLO

HELLO WORLD


7788266888674499977774442227777
5
PHYSICS
QUANTUM
WORLD
HELLO
PHYS

QUANTUM PHYSICS

Провальный тест на:
46663633338
3
GOOD
GREAT
MEET


"""


def main():
    """
    O(n) = nk (n*phinik_words)
    :return:
    """
    s = input()
    n = int(input())
    phinik_words = set()  # используем множество для быстрого поиска
    for _ in range(n):
        phinik_words.add(input())

    words = {
        "1": ["-"],
        "2": list("ABC"),
        "3": list("DEF"),
        "4": list("GHI"),
        "5": list("JKL"),
        "6": list("MNO"),
        "7": list("PQRS"),
        "8": list("TUV"),
        "9": list("WXYZ"),
    }

    """
    Увеличим длину исходной последовательности на одну "нечитаемую" цифру, для
    корректной работы алгоритма по сравниванию текущий и предыдущей цифры, чтобы
    избежать потерю поиска последней буквы
    """

    s += "0"

    """
    кандидаты
    при вычислении новой буквы, опросить словарь, если есть хотя
     бы один кандидат, то сохранить его
    """

    prev_char = s[0]
    letter = [s[0]]  # список из последовательности одинаковых цифр, который переводиться в букву
    letters_sequence = []  # список переведенных букв
    answer = []  # вычлененные слова
    candidate = ''  # кандидат в распознанное слово
    prev_candidate = ''  # предыдущий кандидат в распознанное слово
    next_index = 0  # индекс буквы с которой начинается поиск кандидата
    word_of_current_letters = ''  # все распознанные буквы на данной итерации
    for i in range(1, len(s)):
        if s[i] != prev_char or len(letter) == len(words[prev_char]):
            letters_sequence.append(words[prev_char][len(letter)-1])

            for word in phinik_words:
                word_of_current_letters = "".join(letters_sequence[next_index:])
                if word.startswith(word_of_current_letters):
                    # если зашли хотя бы один раз, то текущая последовательность букв
                    # есть в финикийском словаре, иначе проверяем предыдущего кандидата
                    candidate = word
            if not candidate:
                if prev_candidate:  # если кандидат не найден, проверим предыдущего
                    if prev_candidate in phinik_words:  # если предыдущий существует, поищем его в финикийском словаре
                        answer.append(prev_candidate)
                        next_index = len(word_of_current_letters) - 1  # следующий поиск кандидата начнется с последней переведенной буквы
                        prev_candidate = None
                    else:
                        next_index += 1
                else:
                    next_index += 1
            else:
                prev_candidate = candidate  # сохраняем кандидата, если он был найден
            candidate = None

            letter = [s[i]]
            prev_char = s[i]
        else:
            letter.append(s[i])

    answer.append(prev_candidate)
    print(answer)

    return " ".join(answer)


print(main())
