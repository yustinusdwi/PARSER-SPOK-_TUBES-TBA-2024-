class FASubject:
    def __init__(self):
        self.state = "q0"

    def transition(self, char):
        if self.state == "q0":
            if char == 's':
                self.state = "q1"
            elif char == 'k':
                self.state = "q4_1"
            elif char == 'a':
                self.state = "q5_1"
            elif char == 'm':
                self.state = "q6_1"
            else:
                self.state = "q_reject"
        elif self.state == "q1":
            if char == 'a':
                self.state = "q2"
            else:
                self.state = "q_reject"
        elif self.state == "q2":
            if char == 'y':
                self.state = "q3"
            else:
                self.state = "q_reject"
        elif self.state == "q3":
            if char == 'a':
                self.state = "q_accept"
            else:
                self.state = "q_reject"
        elif self.state == "q4_1":
            if char == 'a':
                self.state = "q4_2"
            else:
                self.state = "q_reject"
        elif self.state == "q4_2":
            if char == 'm':
                self.state = "q4_3"
            else:
                self.state = "q_reject"
        elif self.state == "q4_3":
            if char == 'i':
                self.state = "q_accept"
            else:
                self.state = "q_reject"
        elif self.state == "q5_1":
            if char == 'n':
                self.state = "q5_2"
            else:
                self.state = "q_reject"
        elif self.state == "q5_2":
            if char == 'd':
                self.state = "q5_3"
            else:
                self.state = "q_reject"
        elif self.state == "q5_3":
            if char == 'i':
                self.state = "q_accept"
            else:
                self.state = "q_reject"
        elif self.state == "q6_1":
            if char == 'e':
                self.state = "q6_2"
            else:
                self.state = "q_reject"
        elif self.state == "q6_2":
            if char == 'r':
                self.state = "q6_3"
            else:
                self.state = "q_reject"
        elif self.state == "q6_3":
            if char == 'e':
                self.state = "q6_4"
            else:
                self.state = "q_reject"
        elif self.state == "q6_4":
            if char == 'k':
                self.state = "q6_5"
            else:
                self.state = "q_reject"
        elif self.state == "q6_5":
            if char == 'a':
                self.state = "q_accept"
            else:
                self.state = "q_reject"

    def is_accepting(self):
        return self.state == "q_accept"

    def reset(self):
        self.state = "q0"

    def recognize(self, word):
        self.reset()
        for char in word:
            self.transition(char)
            if self.state == "q_reject":
                return False
        return self.is_accepting()


class FAPredicate:
    def __init__(self):
        self.state = "q0"

    def transition(self, char):
        if self.state == "q0":
            if char == 'p':
                self.state = "q1"
            elif char == 'b':
                self.state = "q5"
            elif char == 'm':
                self.state = "q14"
            else:
                self.state = "q_reject"
        elif self.state == "q1":
            if char == 'e':
                self.state = "q2"
            else:
                self.state = "q_reject"
        elif self.state == "q2":
            if char == 'r':
                self.state = "q3"
            else:
                self.state = "q_reject"
        elif self.state == "q3":
            if char == 'g':
                self.state = "q4"
            else:
                self.state = "q_reject"
        elif self.state == "q4":
            if char == 'i':
                self.state = "q_accept"
            else:
                self.state = "q_reject"
        elif self.state == "q5":
            if char == 'e':
                self.state = "q6"
            else:
                self.state = "q_reject"
        elif self.state == "q6":
            if char == 'r':
                self.state = "q7"
            else:
                self.state = "q_reject"
        elif self.state == "q7":
            if char == 'b':
                self.state = "q8"
            else:
                self.state = "q_reject"
        elif self.state == "q8":
            if char == 'i':
                self.state = "q9"
            else:
                self.state = "q_reject"
        elif self.state == "q9":
            if char == 'n':
                self.state = "q10"
            else:
                self.state = "q_reject"
        elif self.state == "q10":
            if char == 'c':
                self.state = "q11"
            else:
                self.state = "q_reject"
        elif self.state == "q11":
            if char == 'a':
                self.state = "q12"
            else:
                self.state = "q_reject"
        elif self.state == "q12":
            if char == 'n':
                self.state = "q13"
            else:
                self.state = "q_reject"
        elif self.state == "q13":
            if char == 'g':
                self.state = "q_accept"
            else:
                self.state = "q_reject"
        elif self.state == "q14":
            if char == 'e':
                self.state = "q15"
            else:
                self.state = "q_reject"
        elif self.state == "q15":
            if char == 'r':
                self.state = "q16"
            else:
                self.state = "q_reject"
        elif self.state == "q16":
            if char == 'a':
                self.state = "q17"
            else:
                self.state = "q_reject"
        elif self.state == "q17":
            if char == 'n':
                self.state = "q18"
            else:
                self.state = "q_reject"
        elif self.state == "q18":
            if char == 'c':
                self.state = "q19"
            else:
                self.state = "q_reject"
        elif self.state == "q19":
            if char == 'a':
                self.state = "q20"
            else:
                self.state = "q_reject"
        elif self.state == "q20":
            if char == 'n':
                self.state = "q21"
            else:
                self.state = "q_reject"
        elif self.state == "q21":
            if char == 'g':
                self.state = "q_accept"
            else:
                self.state = "q_reject"

    def is_accepting(self):
        return self.state == "q_accept"

    def reset(self):
        self.state = "q0"

    def recognize(self, word):
        self.reset()
        for char in word:
            self.transition(char)
            if self.state == "q_reject":
                return False
        return self.is_accepting()


class FAObject:
    def __init__(self):
        self.state = "q0"

    def transition(self, char):
        if self.state == "q0":
            if char == 'p':
                self.state = "q1"
            elif char == 'b':
                self.state = "q10"
            elif char == 's':
                self.state = "q20"
            elif char == 'a':
                self.state = "q30"
            else:
                self.state = "q_reject"
        elif self.state == "q1":
            if char == 'e':
                self.state = "q2"
            else:
                self.state = "q_reject"
        elif self.state == "q2":
            if char == 's':
                self.state = "q3"
            else:
                self.state = "q_reject"
        elif self.state == "q3":
            if char == 'a':
                self.state = "q4"
            else:
                self.state = "q_reject"
        elif self.state == "q4":
            if char == 'w':
                self.state = "q5"
            else:
                self.state = "q_reject"
        elif self.state == "q5":
            if char == 'a':
                self.state = "q6"
            else:
                self.state = "q_reject"
        elif self.state == "q6":
            if char == 't':
                self.state = "q_accept"
            else:
                self.state = "q_reject"
        elif self.state == "q10":
            if char == 'u':
                self.state = "q11"
            else:
                self.state = "q_reject"
        elif self.state == "q11":
            if char == 'k':
                self.state = "q12"
            else:
                self.state = "q_reject"
        elif self.state == "q12":
            if char == 'u':
                self.state = "q_accept"
            else:
                self.state = "q_reject"
        elif self.state == "q20":
            if char == 't':
                self.state = "q21"
            else:
                self.state = "q_reject"
        elif self.state == "q21":
            if char == 'r':
                self.state = "q22"
            else:
                self.state = "q_reject"
        elif self.state == "q22":
            if char == 'a':
                self.state = "q23"
            else:
                self.state = "q_reject"
        elif self.state == "q23":
            if char == 't':
                self.state = "q24"
            else:
                self.state = "q_reject"
        elif self.state == "q24":
            if char == 'e':
                self.state = "q25"
            else:
                self.state = "q_reject"
        elif self.state == "q25":
            if char == 'g':
                self.state = "q26"
            else:
                self.state = "q_reject"
        elif self.state == "q26":
            if char == 'i':
                self.state = "q_accept"
            else:
                self.state = "q_reject"
        elif self.state == "q30":
            if char == 'a':
                self.state = "q31"
            else:
                self.state = "q_reject"
        elif self.state == "q31":
            if char == 'p':
                self.state = "q32"
            else:
                self.state = "q_reject"
        elif self.state == "q32":
            if char == 'l':
                self.state = "q33"
            else:
                self.state = "q_reject"
        elif self.state == "q33":
            if char == 'i':
                self.state = "q34"
            else:
                self.state = "q_reject"
        elif self.state == "q34":
            if char == 'k':
                self.state = "q35"
            else:
                self.state = "q_reject"
        elif self.state == "q35":
            if char == 'a':
                self.state = "q36"
            else:
                self.state = "q_reject"
        elif self.state == "q36":
            if char == 's':
                self.state = "q_accept"
            else:
                self.state = "q_reject"
        elif self.state == "q40":
            if char == 'u':
                self.state = "q41"
            else:
                self.state = "q_reject"
        elif self.state == "q41":
            if char == 'i':
                self.state = "q42"
            else:
                self.state = "q_reject"
        elif self.state == "q42":
            if char == 's':
                self.state = "q_accept"
            else:
                self.state = "q_reject"

    def is_accepting(self):
        return self.state == "q_accept"

    def reset(self):
        self.state = "q0"

    def recognize(self, word):
        self.reset()
        for char in word:
            self.transition(char)
            if self.state == "q_reject":
                return False
        return self.is_accepting()


class FAAdverb:
    def __init__(self):
        self.state = "q0"

    def transition(self, char):
        if self.state == "q0":
            if char == 'd':
                self.state = "q1"
            elif char == 'k':
                self.state = "q10"
            elif char == 'b':
                self.state = "q20"
            elif char == 's':
                self.state = "q30"
            else:
                self.state = "q_reject"
        elif self.state == "q1":
            if char == 'i':
                self.state = "q2"
            else:
                self.state = "q_reject"
        elif self.state == "q2":
            if char == ' ':
                self.state = "q3"
            else:
                self.state = "q_reject"
        elif self.state == "q3":
            if char == 'k':
                self.state = "q4"
            else:
                self.state = "q_reject"
        elif self.state == "q4":
            if char == 'a':
                self.state = "q5"
            else:
                self.state = "q_reject"
        elif self.state == "q5":
            if char == 'm':
                self.state = "q6"
            else:
                self.state = "q_reject"
        elif self.state == "q6":
            if char == 'p':
                self.state = "q7"
            else:
                self.state = "q_reject"
        elif self.state == "q7":
            if char == 'u':
                self.state = "q_accept"
            else:
                self.state = "q_reject"
        elif self.state == "q10":
            if char == 'e':
                self.state = "q11"
            else:
                self.state = "q_reject"
        elif self.state == "q11":
            if char == ' ':
                self.state = "q12"
            else:
                self.state = "q_reject"
        elif self.state == "q12":
            if char == 'k':
                self.state = "q13"
            else:
                self.state = "q_reject"
        elif self.state == "q13":
            if char == 'a':
                self.state = "q14"
            else:
                self.state = "q_reject"
        elif self.state == "q14":
            if char == 'n':
                self.state = "q15"
            else:
                self.state = "q_reject"
        elif self.state == "q15":
            if char == 't':
                self.state = "q16"
            else:
                self.state = "q_reject"
        elif self.state == "q16":
            if char == 'i':
                self.state = "q_accept"
            else:
                self.state = "q_reject"
        elif self.state == "q20":
            if char == 'e':
                self.state = "q21"
            else:
                self.state = "q_reject"
        elif self.state == "q21":
            if char == 'r':
                self.state = "q22"
            else:
                self.state = "q_reject"
        elif self.state == "q22":
            if char == 's':
                self.state = "q23"
            else:
                self.state = "q_reject"
        elif self.state == "q23":
            if char == 'a':
                self.state = "q24"
            else:
                self.state = "q_reject"
        elif self.state == "q24":
            if char == 'm':
                self.state = "q25"
            else:
                self.state = "q_reject"
        elif self.state == "q25":
            if char == 'a':
                self.state = "q26"
            else:
                self.state = "q_reject"
        elif self.state == "q26":
            if char == '-':
                self.state = "q27"
            else:
                self.state = "q_reject"
        elif self.state == "q27":
            if char == 's':
                self.state = "q28"
            else:
                self.state = "q_reject"
        elif self.state == "q28":
            if char == 'a':
                self.state = "q29"
            else:
                self.state = "q_reject"
        elif self.state == "q29":
            if char == 'm':
                self.state = "q30"
            else:
                self.state = "q_reject"
        elif self.state == "q30":
            if char == 'a':
                self.state = "q_accept"
            else:
                self.state = "q_reject"
        elif self.state == "q30":
            if char == 'e':
                self.state = "q31"
            else:
                self.state = "q_reject"
        elif self.state == "q31":
            if char == 'l':
                self.state = "q32"
            else:
                self.state = "q_reject"
        elif self.state == "q32":
            if char == 'a':
                self.state = "q33"
            else:
                self.state = "q_reject"
        elif self.state == "q33":
            if char == 'm':
                self.state = "q34"
            else:
                self.state = "q_reject"
        elif self.state == "q34":
            if char == 'a':
                self.state = "q35"
            else:
                self.state = "q_reject"
        elif self.state == "q35":
            if char == 'n':
                self.state = "q36"
            else:
                self.state = "q_reject"
        elif self.state == "q36":
            if char == 'y':
                self.state = "q37"
            else:
                self.state = "q_reject"
        elif self.state == "q37":
            if char == 'a':
                self.state = "q_accept"
            else:
                self.state = "q_reject"

    def is_accepting(self):
        return self.state == "q_accept"

    def reset(self):
        self.state = "q0"

    def recognize(self, word):
        self.reset()
        for char in word:
            self.transition(char)
            if self.state == "q_reject":
                return False
        return self.is_accepting()


    def is_accepting(self):
        return self.state == "q_accept"

    def reset(self):
        self.state = "q0"

    def recognize(self, word):
        self.reset()
        for char in word:
            self.transition(char)
            if self.state == "q_reject":
                return False
        return self.is_accepting()


class TokenRecognizer:
    def __init__(self):
        self.fa_subject = FASubject()
        self.fa_predicate = FAPredicate()
        self.fa_object = FAObject()
        self.fa_adverb = FAAdverb()

    def recognize_token(self, word):
        if self.fa_subject.recognize(word):
            return "S"
        elif self.fa_predicate.recognize(word):
            return "P"
        elif self.fa_object.recognize(word):
            return "O"
        elif self.fa_adverb.recognize(word):
            return "K"
        else:
            return "INVALID"


class Parser:
    def __init__(self):
        self.token_recognizer = TokenRecognizer()
        self.stack = []

    def parse(self, sentence):
        words = sentence.lower().split()
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

print("Parser Kalimat Aktif")
print("Anggota Kelompok : ")
print("-------------------")
print("1. Dwi Yustinus Adyra")
print("2. Rishad Tjandiaman")
print("3. Rafi Ainulfitrah T")
print("--------------------")
# Menambahkan tampilan pilihan kata yang tersedia
print("--------------------")
print("Silahkan masukkan pilihan S-P-O-K yang tersedia !")
print("Subjek :", "andi,saya,kamu,kami,mereka")
print("Predikat :", "pergi,berbincang,merancang,menyetir,menulis")
print("Objek :", "pesawat,buku,strategi,aplikasi,puisi")
print("Keterangan :", "di kampus,ke kantin,bersama-sama,kemarin,selamanya")
print("--------------------")

# Main loop to get user input
parser = Parser()
while True:
    sentence = input("Masukkan kalimat: ")
    if sentence.lower() == "exit":
        break
    result = parser.parse(sentence)
    print(result)

