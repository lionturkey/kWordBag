from pathlib import Path
from konlpy.tag import Mecab
import collections

def process_text(text, mecab, known_words, known_particles):
    parsed_words = mecab.pos(text, flatten=False)
    word_bag = collections.defaultdict(lambda: 0)
    particle_bag = collections.defaultdict(lambda: 0)

    htmlAnnotated = ""
    
    for cluster in parsed_words:
        for index, part in enumerate(cluster):
            morpheme = part[0]
            if index == 0 and morpheme != '(' and morpheme != ')':
                word_bag[morpheme] += 1
                style_class = get_morpheme_state(morpheme, known_words)
                htmlAnnotated += "<span class='" + style_class + "'>"
                htmlAnnotated += morpheme + "</span>"
            else:
                particle_bag[morpheme] += 1
                style_class = get_morpheme_state(morpheme, known_particles)
                htmlAnnotated += "<span class='particle " + style_class + "'>"
                htmlAnnotated += morpheme + "</span>"
        htmlAnnotated += " "

    for word in word_bag:
        known_words[word] += word_bag[word]

    for particle in particle_bag:
        known_particles[particle] += particle_bag[particle]


    stats = {}
    stats["word_count"] = len(parsed_words)
    stats["unique_count"] = len(word_bag)
    # stats["new_count"] = stats["unique_count"]
    # stats["seen_count"] = 0
    # stats["known_count"] = 0
    # stats["parse_words"] = parsed_words
    # print(parsed_words)
    stats["particle_count"] = len(particle_bag)
    stats["html"] = htmlAnnotated

    return (stats, known_words, known_particles)


def get_morpheme_state(morpheme, morpheme_bag):
    frequency = morpheme_bag[morpheme]
    if frequency == 0:
        return "new"
    elif frequency < 20:
        return "fuzzy"
    elif frequency < 50:
        return "learning"
    else:
        return "known"



def get_stats(text):
    mecab = Mecab()

    known_words = collections.defaultdict(lambda: 0)
    known_particles = collections.defaultdict(lambda: 0)
    known_words['있'] += 70
    known_words['수'] += 40
    known_particles['는'] += 70

    stats, known_words, known_particles = process_text(text, mecab, known_words, known_particles)

    print(known_words)

    return stats


# def get_bags(username):
#     known_words =
#     word_filename = Path(username + "/words.json")
#     if word_filename.is_file():

    

# text = "형태소는 언어학에서 일정한 의미가 있는 가장 작은 말의 단위로 발화체 내에서 따로 떼어낼 수 있는 것을 말합니다. 즉, 더 분석하면 뜻이 없어지는 말의 단위입니다. 형태소분석기는 단어를 보고 형태소 단위로 분리해내는 소프트웨어를 말합니다. 이러한 형태소분석은 자연어 처리의 가장 기초적인 절차로 이후 구문 분석이나 의미 분석으로 나아가기 위해 가장 먼저 이루어져야 하는 과정으로 볼 수 있습니다. (한국어 위키피디아에서 인용)"
# mecab = Mecab()
# print(process_text(text, mecab))
