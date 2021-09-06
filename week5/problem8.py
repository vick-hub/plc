import os
import sys
import string

"""
Notes:
- Hard to follow!
- Work on naming variable to make it easy to read; it's easier to understand what 'sentence' is
compared to 's'
"""

def main():
    d1 = dict()
    # todo: you can also get punctuation from the string library (import string; string.punctuation)
    #   however, the punctuation may not be exhaustive
#    puncts = '''!()-[]{};:'"/,<>.\?@#$%^&*_~`'''
    puncts = string.punctuation
    text = "When Princess Mary came down, Prince Vasíli and his son were already in the drawing room, talking to the little princess and Mademoiselle Bourienne. When she entered with her heavy step, treading on her heels, the gentlemen and Mademoiselle Bourienne rose and the little princess, indicating her to the gentlemen, said: “Voilà Marie!” Princess Mary saw them all and saw them in detail. She saw Prince Vasíli’s face, serious for an instant at the sight of her, but immediately smiling again, and the little princess curiously noting the impression “Marie” produced on the visitors. And she saw Mademoiselle Bourienne, with her ribbon and pretty face, and her unusually animated look which was fixed on him, but him she could not see, she only saw something large, brilliant, and handsome moving toward her as she entered the room. Prince Vasíli approached first, and she kissed the bold forehead that bent over her hand and answered his question by saying that, on the contrary, she remembered him quite well. Then Anatole came up to her. She still could not see him. She only felt a soft hand taking hers firmly, and she touched with her lips a white forehead, over which was beautiful light-brown hair smelling of pomade. When she looked up at him she was struck by his beauty. Anatole stood with his right thumb under a button of his uniform, his chest expanded and his back drawn in, slightly swinging one foot, and, with his head a little bent, looked with beaming face at the princess without speaking and evidently not thinking about her at all. Anatole was not quick-witted, nor ready or eloquent in conversation, but he had the faculty, so invaluable in society, of composure and imperturbable self-possession. If a man lacking in self-confidence remains dumb on a first introduction and betrays a consciousness of the impropriety of such silence and an anxiety to find something to say, the effect is bad. But Anatole was dumb, swung his foot, and smilingly examined the princess’ hair. It was evident that he could be silent in this way for a very long time. “If anyone finds this silence inconvenient, let him talk, but I don’t want to,” he seemed to say. Besides this, in his behavior to women Anatole had a manner which particularly inspires in them curiosity, awe, and even love—a supercilious consciousness of his own superiority. It was as if he said to them: “I know you, I know you, but why should I bother about you? You’d be only too glad, of course.” Perhaps he did not really think this when he met women—even probably he did not, for in general he thought very little—but his looks and manner gave that impression. The princess felt this, and as if wishing to show him that she did not even dare expect to interest him, she turned to his father. The conversation was general and animated, thanks to Princess Lise’s voice and little downy lip that lifted over her white teeth. She met Prince Vasíli with that playful manner often employed by lively chatty people, and consisting in the assumption that between the person they so address and themselves there are some semi-private, long-established jokes and amusing reminiscences, though no such reminiscences really exist—just as none existed in this case. Prince Vasíli readily adopted her tone and the little princess also drew Anatole, whom she hardly knew, into these amusing recollections of things that had never occurred. Mademoiselle Bourienne also shared them and even Princess Mary felt herself pleasantly made to share in these merry reminiscences."
    # print(text)
    no_punct = ""
    # todo: is there a string method that can speed this up?
    for ch in text:
        if ch not in puncts:
            no_punct = no_punct + ch
    t1 = no_punct.split(" ")
    print(t1)
    for i in t1:
        if i not in d1:
            d1[i] = 1
        else:
            d1[i] = d1[i] + 1
    print(d1)
    # fixme: you can running three loops; do you need three loops? can you do the same work
    #   in one loop? loops are expensive and should be optimised!
    for keys in d1:
        if len(keys) == 3:
            print(keys, d1[keys])
    print("=" * 100)
    for keys in d1:
        if len(keys) == 4:
            print(keys, d1[keys])
    print("=" * 100)
    for keys in d1:
        if len(keys) == 5:
            print(keys, d1[keys])
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
