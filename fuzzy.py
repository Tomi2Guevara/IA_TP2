from antecedente import Antecedent
class Fuzzy():
    def __init__(self, pAnt = [], pCon = [], pHs = [], pCon2 = []):
        self.ant = pAnt
        self.con = pCon
        self.pHs = pHs
        self.pCon2 = pCon2
        self.ez = Antecedent("eZ")
        self.dz = Antecedent("dZ")

    def solution(self, tExt, tInt, hr, pron):
        vh = []
        for i in self.pHs:
            vh.append(i.eval(hr))

        if vh[1] > vh[0] and vh[1] > vh[2]:
            tObj = 25*vh[1]

        elif pron > 25:
            val = max(vh[0], vh[2])
            tObj = 25 - 20 * vh[0]
        else:
            val = max(vh[0], vh[2])
            tObj = 45 - 20 * val

        ez1 = tInt - tObj
        dz1 = tExt - tInt
        ve = []
        vd = []


        for a in self.ant:
            ve.append(a.eval(ez1))
            vd.append(a.eval(dz1))
        self.ez.val = ve
        self.dz.val = vd




        c = max(min(self.ez.val[0], self.dz.val[0]), min(self.ez.val[0], self.dz.val[1]), min(self.ez.val[1], self.dz.val[0]), min(self.ez.val[1], self.dz.val[2]), min(self.ez.val[2], self.dz.val[1]), min(self.ez.val[2], self.dz.val[2]))
        a = max(min(self.ez.val[0], self.dz.val[2]), min(self.ez.val[2], self.dz.val[0]))
        m = min(self.ez.val[1], self.dz.val[1])

        sc = self.con[0].bisect_defuzzify(c)
        sm = self.con[1].bisect_defuzzify(m)
        sa = self.con[2].bisect_defuzzify(a)

        if (a+m+c) == 0:
            aper = 0
        else:
            aper = (c * sc + m * sm + a * sa) / (c + m + a)
        aper /= 100
        dvt = (tExt - tInt) / (17280 * (1 + 0.1 * aper))
        tInt = tInt + dvt * 3600
        return tInt, aper*10