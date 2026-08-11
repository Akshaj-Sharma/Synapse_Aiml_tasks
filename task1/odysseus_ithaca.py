from collections import Counter

def earliest_ithaca_step(sequence):
    target = Counter("ITHACA")
    collected = Counter()

    for step, letter in enumerate(sequence, start=1):
        collected[letter.upper()] += 1

        if all(collected[ch] >= needed for ch, needed in target.items()):
            return step

    return -1

if __name__ == "__main__":
    letters = "T X I A H C B A".split()
    result = earliest_ithaca_step(letters)
    print("Output:", result)
