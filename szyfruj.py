d1 = {"g":"a","d":"e","r":"y","p":"o","l":"u","k":"i"}
d2 = {"p":"o","l":"i","t":"y","k":"a","r":"e","n":"u"}

def split(word):
    return [char for char in word]

def szyfruj(text):
    tekst = text.lower()
    nowy = ""
    szyfr = input("Jeśli chcesz szyfrować za pomocą szyfru GA-DE-RY-PO-LU-KI, naciśnij G."
                  "Jeśli chcesz szyfrować za pomocą szyfru PO-LI-TY-KA-RE-NU, naciśnij P."
                  "Jeśli chcesz szyfrować za pomocą własnego szyfru, naciśnij S.")
    if szyfr == "g":
        for i in tekst:
            if i in d1.keys():
                nowy += d1.get(i)
            elif i in d1.values():
                nowy += str(list(d1.keys())[list(d1.values()).index(i)])
            else:
                nowy += str(i)
        return nowy
    if szyfr == "p":
        for i in tekst:
            if i in d2.keys():
                nowy += d2.get(i)
            elif i in d2.values():
                nowy += str(list(d2.keys())[list(d2.values()).index(i)])
            else:
                nowy += str(i)
        return nowy
    if szyfr == "s":
        swoj = str(input("Podaj szyfr, rozdzielając każdą parę liter za pomocą '-'."))
        swoj = swoj.lower()
        assert len(swoj) == 17 and [(swoj[i] >= 'a' or swoj[i] <= 'z') and [swoj[i] <'0' or swoj[i] > '9'] for i in [0, 1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16]], "Podaj prawidłowy szyfr."
        assert [swoj[i] == '-' for i in [2, 5, 8, 11, 14]], "Podaj prawidłowy szyfr"
        swoj = swoj.split('-')
        swoj = [split(i) for i in swoj]
        s = set()
        for i in swoj:
            for j in i:
                s.add(j)
        print(s)
        assert len(s) == 12, "Podaj prawidłowy szyfr"
        ds = dict(swoj)
        for j in tekst:
            if j in ds.keys():
                nowy += ds.get(j)
            elif j in ds.values():
                nowy += str(list(ds.keys())[list(ds.values()).index(j)])
            else:
                nowy += j
        return nowy
    else:
        print("Niepoprawnie wybrana metoda szyfrowania.")
    return nowy

print(szyfruj("ala ma kota"))

