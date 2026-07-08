class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        ans = []
        for s in strs:
            ans.append("256")
            lenstr = str(len(s))
            if len(lenstr) >= 3:
                ans.append(lenstr)
            elif len(lenstr) >= 2:
                ans.append("0" + lenstr)
            else:
                ans.append("00" + lenstr)
            for c in s:
                numstr = str(ord(c))
                if len(numstr) >= 3:
                    ans.append(numstr)
                elif len(numstr) >= 2:
                    ans.append("0" + numstr)
                else:
                    ans.append("00" + numstr)
        
        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        ans = []
        decoder = [s[i:i+3] for i in range(0, len(s), 3)]
        for x in range(0, len(decoder)):
            if decoder[x] == "256":
                ansstr = []
                for y in range(1, int(decoder[x+1])+ 1):
                    ansstr.append(chr(int(decoder[x+1 + y])))
                ans.append("".join(ansstr))
        return ans

                        
