import string

ORIGIN = """
50m3b0dy 0nc3 70ld m3 7h3 w0rld 15 60nn4 r0ll m3
1 41n'7 7h3 5h4rp357 700l 1n 7h3 5h3d
5h3 w45 l00k1n6 k1nd 0f dumb w17h h3r f1n63r 4nd h3r 7humb
1n 7h3 5h4p3 0f 4n "l" 0n h3r f0r3h34d
w3ll 7h3 y34r5 574r7 c0m1n6 4nd 7h3y d0n'7 570p c0m1n6
f3d 70 7h3 rul35 4nd 1 h17 7h3 6r0und runn1n6
d1dn'7 m4k3 53n53 n07 70 l1v3 f0r fun
y0ur br41n 6375 5m4r7 bu7 y0ur h34d 6375 dumb
50 much 70 d0, 50 much 70 533
50 wh47'5 wr0n6 w17h 74k1n6 7h3 b4ck 57r3375?
y0u'll n3v3r kn0w 1f y0u d0n'7 60
y0u'll n3v3r 5h1n3 1f y0u d0n'7 6l0w
h3y n0w, y0u'r3 4n 4ll-574r, 637 y0ur 64m3 0n, 60 pl4y
h3y n0w, y0u'r3 4 r0ck 574r, 637 7h3 5h0w 0n, 637 p41d
4nd 4ll 7h47 6l1773r5 15 60ld
0nly 5h0071n6 574r5 br34k 7h3 m0ld
17'5 4 c00l pl4c3 4nd 7h3y 54y 17 6375 c0ld3r
y0u'r3 bundl3d up n0w, w417 71ll y0u 637 0ld3r
bu7 7h3 m3730r m3n b36 70 d1ff3r
jud61n6 by 7h3 h0l3 1n 7h3 5473ll173 p1c7ur3
7h3 1c3 w3 5k473 15 63771n6 pr377y 7h1n
7h3 w473r'5 63771n6 w4rm 50 y0u m16h7 45 w3ll 5w1m
my w0rld'5 0n f1r3, h0w 4b0u7 y0ur5?
7h47'5 7h3 w4y 1 l1k3 17 4nd 1 n3v3r 637 b0r3d
h3y n0w, y0u'r3 4n 4ll-574r, 637 y0ur 64m3 0n, 60 pl4y
h3y n0w, y0u'r3 4 r0ck 574r, 637 7h3 5h0w 0n, 637 p41d
4ll 7h47 6l1773r5 15 60ld
0nly 5h0071n6 574r5 br34k 7h3 m0ld
h3y n0w, y0u'r3 4n 4ll-574r, 637 y0ur 64m3 0n, 60 pl4y
h3y n0w, y0u'r3 4 r0ck 574r, 637 7h3 5h0w, 0n 637 p41d
4nd 4ll 7h47 6l1773r5 15 60ld
0nly 5h0071n6 574r5
50m3b0dy 0nc3 45k3d c0uld 1 5p4r3 50m3 ch4n63 f0r 645?
1 n33d 70 637 my53lf 4w4y fr0m 7h15 pl4c3
1 541d y3p wh47 4 c0nc3p7
1 c0uld u53 4 l177l3 fu3l my53lf
4nd w3 c0uld 4ll u53 4 l177l3 ch4n63
w3ll, 7h3 y34r5 574r7 c0m1n6 4nd 7h3y d0n'7 570p c0m1n6
f3d 70 7h3 rul35 4nd 1 h17 7h3 6r0und runn1n6
d1dn'7 m4k3 53n53 n07 70 l1v3 f0r fun
y0ur br41n 6375 5m4r7 bu7 y0ur h34d 6375 dumb
50 much 70 d0, 50 much 70 533
50 wh47'5 wr0n6 w17h 74k1n6 7h3 b4ck 57r3375?
y0u'll n3v3r kn0w 1f y0u d0n'7 60 (60!)
y0u'll n3v3r 5h1n3 1f y0u d0n'7 6l0w
h3y n0w, y0u'r3 4n 4ll-574r, 637 y0ur 64m3 0n, 60 pl4y
h3y n0w, y0u'r3 4 r0ck 574r, 637 7h3 5h0w 0n, 637 p41d
4nd 4ll 7h47 6l1773r5 15 60ld
0nly 5h0071n6 574r5 br34k 7h3 m0ld
4nd 4ll 7h47 6l1773r5 15 60ld
0nly 5h0071n6 574r5 br34k 7h3 m0ld
"""

if __name__ == "__main__":
    SOURCE = ("CTF{" + ORIGIN.translate(str.maketrans('', '', string.punctuation)).replace(" ", "_").replace("\n", '.') + "}")[::-1]

    with open("script.py", "w") as f:
        f.write('"' * 3)
        f.write("\nSOURCE : A string\n")
        f.write('"' * 3)
        f.write(f"""\nSOURCE = "{SOURCE}"\n""")


