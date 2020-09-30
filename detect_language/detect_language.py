import langdetect
from multiprocessing import Pool


def detector(sentence):
    if not sentence:
        return
    lang = langdetect.detect(sentence)
    return tuple([sentence, lang])


class LanguageChecker(object):
    def __init__(self):
        super(LanguageChecker, self).__init__()

    @staticmethod
    def detect_language_of_sentences(sentences: list, cores: int = 1,
                                       use_multiprocessing: bool = False):
        if use_multiprocessing and cores > 1:
            # language = [lang for lang in [language] for x in range(len(sentences))]
            with Pool(cores) as p:
                output = p.map(detector, sentences)
            return output
        #     pool = Pool(cores)
        #     output = pool.starmap(detector, sentences)
        #     pool.close()
        #     pool.join()
        #     return output
        # else:
        #     return list(map(detector, sentences))

# if __name__ == '__main__':
#     c = LanguageChecker()
#     s = []
#     out = c.detect_language_of_sentences(sentences=s, cores=1, use_multiprocessing=True)
#     print(2)
