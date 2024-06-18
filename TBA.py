class TokenRecognizer:
    def __init__(self):
        self.subjects = {"saya", "kami", "andi", "mereka", "kamu"}
        self.predicates = {"pergi", "berbincang", "merancang", "menyetir", "menulis"}
        self.objects = {"pesawat", "buku", "puisi", "strategi", "aplikasi"}
        self.adverbs = {"di kampus", "ke kantin", "bersama-sama", "kemarin", "selamanya"}

    def recognize_token(self, word):
        if word in self.subjects:
            return "S"
        elif word in self.predicates:
            return "P"
        elif word in self.objects:
            return "O"
        elif word in self.adverbs:
            return "K"
        else:
            return "INVALID"

class Parser:
    def __init__(self):
        self.token_recognizer = TokenRecognizer()
        self.stack = []

    def parse(self, sentence):
        words = sentence.split()
        tokens = []
        i = 0

        while i < len(words):
            if i < len(words) - 1 and " ".join(words[i:i+2]) in self.token_recognizer.adverbs:
                tokens.append(self.token_recognizer.recognize_token(" ".join(words[i:i+2])))
                i += 2
            else:
                tokens.append(self.token_recognizer.recognize_token(words[i]))
                i += 1

        if "INVALID" in tokens:
            return "Tidak valid"

        # State machine implementation using a stack
        state = "START"
        self.stack = ["$"]  # Reset stack with initial state symbol

        for token in tokens:
            if state == "START":
                if token == "S":
                    self.stack.append("S")
                    state = "S"
                else:
                    return "Tidak valid"
            elif state == "S":
                if token == "P":
                    self.stack.append("P")
                    state = "P"
                else:
                    return "Tidak valid"
            elif state == "P":
                if token == "O":
                    self.stack.append("O")
                    state = "O"
                elif token == "K":
                    self.stack.append("K")
                    state = "K"
                else:
                    return "Tidak valid"
            elif state == "O":
                if token == "K":
                    self.stack.append("K")
                    state = "K"
                else:
                    return "Tidak valid"
            else:
                return "Tidak valid"

        # Valid final states
        final_states = [
            ["$", "S", "P", "O", "K"],
            ["$", "S", "P", "K"],
            ["$", "S", "P", "O"],
            ["$", "S", "P"]
        ]

        # Check if the stack is in one of the valid final structures
        if self.stack in final_states:
            return "Valid"
        else:
            return "Tidak valid"

print("parser kalimat logis")
print("Anggota Kelompok : ")
print("-------------------")
print("1. Yustinus Dwi Adyra")
print("2. Rishad Tjandiaman")
print("3. Rafi Ainulfitrah T")
print("--------------------")
print("Silahkan masukkan pilihan S-P-O-K yang tersedia !")
print("Subjek :", TokenRecognizer().subjects)
print("Predikat :", TokenRecognizer().predicates)
print("Objek :", TokenRecognizer().objects)
print("Keterangan :", TokenRecognizer().adverbs)
print("--------------------")

# Main loop to get user input
parser = Parser()
while True:
    sentence = input("Masukkan kalimat: ")
    if sentence.lower() == "exit":
        break
    result = parser.parse(sentence)
    print(result)
