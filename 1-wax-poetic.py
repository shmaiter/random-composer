import random

"""_summary_
Write a program that generates poetry using lists and the random module.
Whith the following structure inspired by Clifford Pickover:

{A/An} {adj1} {noun1}
{A/An} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
{adverb1}, the {noun1} {verb2}
the {noun2} {verb3} {prep2} a {adj3} {noun3}
"""

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]
vocals = "aeiou"


def make_poem():
    """Select the words and print the content with the correct syntax"""

    adj1, adj2, adj3 = random_picker(adjectives, 3)
    noun1, noun2, noun3 = random_picker(nouns, 3)
    verb1, verb2, verb3 = random_picker(verbs, 3)
    prep1, prep2 = random_picker(prepositions, 2)
    adv1 = random_picker(adverbs, 1)[0]
    article = "An" if adj1[0] in vocals else "A"

    print(
        f"""
        {article} {adj1} {noun1}
        {article} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
        {adv1}, the {noun1} {verb2}
        the {noun2} {verb3} {prep2} a {adj3} {noun3}
        """
    )


def random_picker(lst, num):
    """Return a list of unique words according to the amount passed on 'num'"""

    s1 = [random.choice(lst)]
    while len(s1) < num:
        temp = random.choice(lst)
        while temp in s1:
            temp = random.choice(lst)
        s1.append(temp)

    return s1


if __name__ == "__main__":
    make_poem()
