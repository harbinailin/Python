class SequenceList(object):
    def __init__(self):
        # 初始化顺序表
        self.SeqList = []

    def CreateSequenceList(self):
        print("请输入顺序表元素按回车确认，输入#号结束")
        Element = input("请输入元素：")
        while Element != '#':
            self.SeqList.append(int(Element))
            Element = input("请输入元素：")

    def FindElement(self):
        key = int(input("请输入需要查找的元素值："))
        if key in self.SeqList:
            ind = self.SeqList.index(key)
            print(f"查找成功！元素下标为:{ind} 元素值为{self.SeqList[ind]}")
        else:
            print(f"查找失败！当前顺序表中不存在值为{key}的元素")

    def InsertElemnt(self):
        ind = int(input("请输入待插入元素的下标："))
        Element = int(input("请输入待插入元素的值："))
        self.SeqList.insert(ind, Element)
        print(f"插入当前元素后的顺序表：{self.SeqList}")

    def DeleteElementById(self):
        ind = int(input("请输入要删除元素的下标："))
        print(f"正在删除下标为{ind}的元素")
        self.SeqList.remove(self.SeqList[ind])
        print("删除后的顺序表为：", self.SeqList)

    def DeleteElementByKey(self):
        key = int(input("请输入要删除元素的值："))
        print(f"正在删除值为{key}的元素")
        if key in self.SeqList:
            ind = self.SeqList.index(key)
            print(f"删除成功！已成功删除元素值为{self.SeqList[ind]}的元素")
            print("删除后的顺序表为：", self.SeqList)
        else:
            print(f"删除失败！当前顺序表中不存在值为{key}的元素")

    def TraverseElement(self):
        SeqListLen = len(self.SeqList)
        for i in range(0, SeqListLen):
            print(f"下标为{i}的元素的值为{self.SeqList[i]}")

    def IsEmpty(self):
        if len(SeqList) == 0:
            return True
        else:
            return False


SeqList = SequenceList()
SeqList.CreateSequenceList()
SeqList.TraverseElement()
SeqList.FindElement()
SeqList.InsertElemnt()
SeqList.DeleteElementById()
SeqList.DeleteElementByKey()
