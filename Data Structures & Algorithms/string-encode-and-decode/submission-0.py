class Solution:

    def encode(self, strs: List[str]) -> str:
        x = ""
        for s in strs:
            x = x + '?' + s
        return x

        

    def decode(self, s: str) -> List[str]:
        s = s.split('?')
        s.remove('')

        return (s)
