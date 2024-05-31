class Cipher:
    def __init__(self, keyword):
        self.keyword = keyword.upper()
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.cipher_alphabet = self._generate_cipher_alphabet()
        self.encode_map = self._create_mapping(self.alphabet, self.cipher_alphabet)
        self.decode_map = self._create_mapping(self.cipher_alphabet, self.alphabet)

    def _generate_cipher_alphabet(self):
        seen = set()
        keyword_unique = "".join([c for c in self.keyword if not (c in seen or seen.add(c))])
        remaining_letters = "".join([c for c in self.alphabet if c not in keyword_unique])
        return keyword_unique + remaining_letters

    def _create_mapping(self, from_alphabet, to_alphabet):
        return {from_alphabet[i]: to_alphabet[i] for i in range(len(from_alphabet))}

    def encode(self, plaintext):
        return self._transform(plaintext, self.encode_map)

    def decode(self, ciphertext):
        return self._transform(ciphertext, self.decode_map)

    def _transform(self, text, mapping):
        result = []
        for char in text:
            if char.upper() in mapping:
                new_char = mapping[char.upper()]
                result.append(new_char if char.isupper() else new_char.lower())
            else:
                result.append(char)
        return "".join(result)


cipher = Cipher("crypto")
encoded = cipher.encode("Hello world")
print(encoded)

decoded = cipher.decode("Fjedhc dn atidsn")
print(decoded)

                 

