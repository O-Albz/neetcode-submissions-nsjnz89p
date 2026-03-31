class Solution:



    def encode(self, strs: List[str]) -> str:
        encoded = ''

        for string in strs:
            length = str(len(string))
            encoded += length
            encoded += '#'
            encoded += string

        return encoded

    def decode(self, s: str) -> List[str]:

        result = []
        i = 0
        n = len(s)

        while i < n:
            length = 0

            while s[i] != '#':
                length = length * 10 + (ord(s[i]) - ord('0'))
                i += 1

            i += 1 # skip # character

            temp = s[i:i + length]
            result.append(temp)

            i += length

        return result