class crc:
    def isRightData(self, data: "", generatorPolynomial: "", checkCode: ""):
        if checkCode == None:
            for i in generatorPolynomial.len():
                data += '0'
        else:
            data+=checkCode
        print("data:"%data)
