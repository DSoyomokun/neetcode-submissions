class Solution:

    def encode(self, strs: List[str]) -> str:
        x = ""
        for s in strs:
            x = x + '?sdf' + s
        return x

        

    def decode(self, s: str) -> List[str]:
        s = s.split('?sdf')
        s.remove('')

        return (s)
