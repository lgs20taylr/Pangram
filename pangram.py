import string

def main():
    sentence = input("Enter a sentence to check if it is a pangram.\n").lower()
    print("Sentence is a pangram." if check(sentence) else "Sentence is not a pangram.")

def check(sentence):
    alphabet = list(string.ascii_lowercase)
    for letter in alphabet:
        if letter not in sentence:
            return False
    return True

if __name__ == "__main__":
    main()