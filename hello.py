

if __name__ == "__main__":
    with open('random text.txt') as reader:
        counts = dict()
        for line in reader:
            words = line.split()
            for word in words:
                counts[word] = counts.get(word, 0) + 1
                
    # Get the max value based on the key's value
    most_used = max(counts, key=lambda key: counts[key])
    print(f"The most used word is '{most_used}' appearing {counts[most_used]} times.")