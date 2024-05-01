from antecedente import Antecedent
class Fuzzy():
    def __init__(self, pAnt = [], pCon = []):
        self.ant = pAnt
        self.con = pCon
        self.ez = Antecedent("eZ")
        self.dz = Antecedent("dZ")

    def solution(self, tExt, tInt, tObj):
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
        aper = (c * sc + m * sm + a * sa) / (c + m + a)
        aper /= 100
        tau = (86400 / (5 * (1 + 0.1 * aper)))
        dvt = (tExt - tInt) / (tau * (1 + 0.1 * aper))
        tInt = tInt + dvt * 3600
        return tInt