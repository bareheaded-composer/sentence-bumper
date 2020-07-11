DOCS = """
Sentence Bumper - bump some sentence in your mind.

Usage: python3 sentence_bumeper [Options]

Options:
  -h, --help                print this help
  -v, --version             display version info of the program and sentence bundle
  --category <CATEGORY>     specify the category of sentence.
                            <CATEGORY> should be a single-character which stands for a valid category

Examples:
  python3 sentence_bumper   bumps a random sentence.
  python3 sentence_bumper --category a
                            bumps a random sentence from category "a" (ie, "Anime" Catogroy).
"""


from os import path
from datetime import datetime
import sys
import json
import random


VERBOSE = False
BUNDLE_PATH = path.join(path.dirname(__file__), '../data/hitokoto-osc-sentences-bundle')
CATAGORIES = dict()


def verbose(*args, **kwargs):
    if VERBOSE:
        print(args, kwargs)


def check_version():
    with open(BUNDLE_PATH + '/version.json') as version_file:
        versionInfo = json.loads(version_file.read())
        assert versionInfo["protocol_version"] == "1.0.0"

        verbose("语句库版本：", versionInfo["protocol_version"])
        updatedAt = datetime.fromtimestamp(versionInfo["updated_at"] / 1000)
        verbose("语句库更新时间：", updatedAt)


def get_category():
    global CATAGORIES

    with open(BUNDLE_PATH + '/categories.json') as categories_file:
        categories = json.loads(categories_file.read())
        verbose("分类数量：", len(categories))

        for category in categories:
            sentences = json.loads(open(BUNDLE_PATH + '/' + category["path"]).read())

            verbose("- 名称：%s" % category["name"])
            verbose("  编号：%s" % category["key"])
            verbose("  描述：%s" % category["desc"])
            verbose("  数量：%d" % len(sentences))
            verbose("  更新时间：%s" % category["updated_at"])

            CATAGORIES[category["key"]] = category["path"]


def get_random_sentence(category_key: str):
    if category_key not in CATAGORIES.keys():
        raise Exception("'%s' is not a valid catagory key!" % category_key)

    with open(BUNDLE_PATH + '/sentences/' + category_key + ".json") as sentences_file:
        sentences = json.loads(sentences_file.read())
        return random.choice(sentences)


def main():
    global VERBOSE

    argv = sys.argv[1:]

    if '-h' in argv or '--help' in argv:
        print(DOCS)
        sys.exit(0)

    if '-v' in argv or '--verbose' in argv:
        VERBOSE = True

    check_version()
    get_category()

    category = ''
    if '--category' in argv:
        try:
            category = argv[argv.index('--category') + 1]
        except IndexError:
            raise Exception("catagory argument is missing!")

    if category == "":
        category = random.choice(list(CATAGORIES.keys()))

    random_sentence = get_random_sentence(category)

    print(json.dumps(random_sentence, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
