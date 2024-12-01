import pyttsx3
import re
import readline  # Importing readline module for input history

# Initialize TTS engine
tts_engine = pyttsx3.init()
tts_engine.setProperty("rate", 150)  # Speed of speech
tts_engine.setProperty("volume", 1.0)  # Volume (0.0 to 1.0)

# Expanded Cibit phonetic mappings with updated symbols replacing slashes
CIBIT_PHONETICS = {
    "⊳": "zetter",  # Replacing "/\\"
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
    "⊳ + ƃ": "zetter plus boo",  # Replacing "/\\ + ƃ"
    "λ + ⟿": "eye and zigzag arrow",
    "⊳ + ⧫": "slash and double slash",  # Replacing "/\\ + //"
    "⊔ + λ": "open box and lambda",
    "○ + ʘ": "circle and theta",
    "⊳ + ╎╎": "zetter and parallel lines",
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
    "⊳ + ~": "zetter and tilde",
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
    # Clean up the input
    cibit_sequence = cibit_sequence.strip().replace(" +", "+")  # Clean up spacing around '+'
    phonetics = []
    
    # Debugging print to check the input format
    print(f"Normalized Input: {cibit_sequence}")

    # Split by the "+" symbol
    symbols = cibit_sequence.split("+")
    for symbol in symbols:
        symbol = symbol.strip()  # Remove extra spaces
        
        # Debugging print to show what is being looked up
        print(f"Looking up symbol: {symbol}")

        # Directly use the symbol from Cibit dictionary without extra escaping
        phonetic = CIBIT_PHONETICS.get(symbol, f"unknown symbol: {symbol}")
        phonetics.append(phonetic)
    
    phonetic_sentence = " ".join(phonetics)
    print(f"Speaking: {phonetic_sentence}")  # Debugging print

    # Speak each phonetic word one by one for better clarity
    for word in phonetics:
        print(f"Speaking word: {word}")  # Debugging print
        tts_engine.say("fuck off")
        tts_engine.runAndWait()

# Function to generate Python code based on Cibit symbols
def generate_python_code(cibit_sequence):
    """Generate Python code from a Cibit sequence."""
    
    # Handle basic loops and actions
    if cibit_sequence == "⊳ + ƃ":  # Represents a basic loop
        return "for i in range(limit):\n    pass  # Single loop"
    
    if cibit_sequence == "⊳ + ⧫":  # Represents nested loops
        return "for i in range(outer_limit):\n    for j in range(inner_limit):\n        pass  # Nested loop example"
    
    # Handle recursive functions
    if cibit_sequence == "λ + ⟿":  # Recursive function
        return "def recursive_function(n):\n    if n <= 0:\n        return 1\n    return n * recursive_function(n - 1)  # Recursion example"
    
    # Handle class definitions
    if cibit_sequence == "⊔ + λ":  # Class definition
        return "class Box:\n    def __init__(self, value):\n        self.value = value  # Encapsulation example"
    
    # Handle other combinations for Python constructs (like conditionals, etc.)
    if cibit_sequence == "⊳ + ╎╎":  # Parallel or simultaneous actions
        return "for i in range(limit):\n    # Parallel actions can be written here"
    
    # Handle dynamic code generation
    if "⊳" in cibit_sequence and "ƃ" in cibit_sequence:
        return "for i in range(limit):\n    # Your code here"

    if "λ" in cibit_sequence and "⟿" in cibit_sequence:
        return "def function_name(n):\n    if n <= 0:\n        return 1\n    return n * function_name(n - 1)  # Recursive function"

    # Handle unknown Cibit sequences
    return "# Unknown Cibit sequence or unimplemented symbol"

# Main interpreter loop
def cibit_interpreter():
    print("Cibit Interpreter - Enter Cibit symbols (type 'help' for instructions):")
    while True:
        user_input = input("> ").strip().lower()

        # Exit condition
        if user_input == "exit":
            break
        elif user_input == "help":
            print("Available Cibit symbols and their Python code:")
            for symbol in CIBIT_PHONETICS.keys():
                print(f"  {symbol}: {generate_python_code(symbol)}")
            continue
        
        # Generate Python code based on the Cibit input
        python_code = generate_python_code(user_input)
        print(f"Generated Python Code:\n{python_code}")
        
        # Speak the phonetics of the Cibit sequence
        speak_cibit_phonetics(user_input)

if __name__ == "__main__":
    cibit_interpreter()

