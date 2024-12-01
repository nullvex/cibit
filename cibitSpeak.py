import pyttsx3

# Initialize TTS engine
tts_engine = pyttsx3.init()
tts_engine.setProperty("rate", 150)  # Speed of speech
tts_engine.setProperty("volume", 1.0)  # Volume (0.0 to 1.0)

# Expanded Cibit phonetic mappings with "zetter" included
CIBIT_PHONETICS = {
    "/\\": "zetter",
    "ƃ": "boo",
    "(": "koh",
    "⊂": "soo",
    "∈": "in",
    "┐": "ree",
    "C-": "kay",
    "╎╎": "pi",
    "λ": "eye",
    "⊔": "ell",
    "○": "ka",
    "⟿": "dah",
    "×": "shoo",
    "~": "uh",
    "/\\ + ƃ": "zetter plus boo",
    "λ + ⟿": "eye and zigzag arrow",
    "/\\ + //": "slash and double slash",
    "⊔ + λ": "open box and lambda",
    "○ + ʘ": "circle and theta",
    "/\\ + ╎╎": "zetter and parallel lines",
    "C- + ┘": "see dash and right angle",
    "λ + ∈": "lambda and element of",
    "~ + ×": "tilde and cross",
    "// + C-": "double slash and see dash",
    "○ + |<": "circle and angle",
    "~ + ⟿": "tilde and zigzag arrow",
    "┘ + |": "right angle and pipe",
    "⊂ + ~": "subset and tilde",
    "∈ + ⊂": "element of and subset",
    "λ + ╎╎": "lambda and parallel lines",
    "⊔ + ⊂": "open box and subset",
    "⊿": "tilde and backwards",
    "/\\ + ~": "zetter and tilde",
    "⅂ + ⊂": "hook and subset",
    "╎╎ + λ": "parallel lines and lambda",
    "× + ×": "cross and cross",
    "λ + ⊂": "lambda and subset",
    "⟿ + ⊂": "zigzag arrow and subset",
    "○ + |<": "circle and angle",
    "λ + ⟿": "lambda and zigzag arrow",
}

# Function to speak the Cibit phonetic sounds
def speak_cibit_phonetics(cibit_sequence):
    """Speak the phonetics of a given Cibit sequence."""
    # Normalize and split input by "+"
    cibit_sequence = cibit_sequence.strip().replace(" +", "+")  # Clean up spacing around '+'
    print(f"Normalized Input: {cibit_sequence}")  # Debugging print
    phonetics = []
    
    # Split by the "+" symbol
    for symbol in cibit_sequence.split("+"):
        symbol = symbol.strip()  # Strip spaces from the symbols
        phonetic = CIBIT_PHONETICS.get(symbol, f"unknown symbol: {symbol}")
        phonetics.append(phonetic)
    
    phonetic_sentence = " ".join(phonetics)
    print(f"Speaking: {phonetic_sentence}")  # Debugging print

    # Check if the TTS engine is working by speaking a test message
    tts_engine.say(f"Testing TTS: {phonetic_sentence}")
    tts_engine.runAndWait()

    # Speak each phonetic word one by one
    for word in phonetics:
        print(f"Speaking word: {word}")  # Debugging print
        tts_engine.say(word)
        tts_engine.runAndWait()

# Example functions to simulate Cibit interpreter input
def cibit_interpreter():
    print("Cibit Interpreter - Enter Cibit symbols (type 'help' for instructions):")
    while True:
        user_input = input("> ").strip().lower()
        if user_input == "exit":
            break
        elif user_input == "help":
            print("Available commands:")
            for symbol in CIBIT_PHONETICS.keys():
                print(f"  {symbol}")
            continue
        
        # Speak the phonetics of the Cibit input
        speak_cibit_phonetics(user_input)

if __name__ == "__main__":
    cibit_interpreter()

