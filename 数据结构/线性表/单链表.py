# 循环单链表：表中的最后一个结点的指针域不为空，而是指向表中的第一个结点。
# 若循环单链表中存在头结点，则第一个结点为头结点，否则第一个结点为循环单链表第一个元素所在的结点。
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList(object):

    def __init__(self):
        self.head = Node(None)

    def CreateSingleLinkedList(self):
        print("请输入数据后按回车确认，按#号结束")
        cNode = self.head
        Element = input("请输入当前结点的值：")
        while Element != '#':
            nNode = Node(int(Element))
            cNode.next = nNode
            cNode = cNode.next
            Element = input("请输入当前结点的值：")

    def InsertElementInTail(self):
        Element = input("请输入要插入结点的值（尾插）")
        if Element == "#":
            return
        cNode = self.head
        nNode = Node(int(Element))
        while cNode.next != None:
            cNode = cNode.next
        cNode.next = nNode

    def InsertElementInHead(self):
        Element = input("请输入要插入结点的值（头插）：")
        if Element == "#":
            return
        cNode = self.head
        nNode = Node(int(Element))
        nNode.next = cNode.next
        cNode.next = nNode

    def GetLength(self):
        cNode = self.head
        length = 0
        while cNode.next != None:
            length = length + 1
            cNode = cNode.next
        return length

    def IsEmpty(self):
        if self.GetLength() == 0:
            return True
        else:
            return False

    def FindElement(self):
        Posi = 0
        cNode = self.head
        key = int(input("请输入想查找的元素值："))
        if self.IsEmpty():
            print("当前链表为空，不存在该元素")
            return
        while cNode.next != None and cNode.data != key:
            cNode = cNode.next
            Posi = Posi + 1
        if cNode.data == key:
            print(f"查找成功！元素值为{key}的结点位于该单链表的第{Posi}位")
        else:
            print(f"查找失败！当前单链表中不存在{key}元素")

    def DeleteElement(self):
        dElement = int(input("请输入要删除结点的值："))
        cNode = self.head
        pNode = self.head
        if self.IsEmpty():
            print("当前链表为空！")
            return
        while cNode.next != Node and cNode.data != dElement:
            pNode = cNode
            cNode = cNode.next
        if cNode.data == dElement:
            pNode.next = cNode.next
            del cNode
            print(f"成功删除值为{dElement}的结点")
        else:
            print(f"删除失败！当前单链表中不含有值{dElement}的结点")

    def VisitElement(self, tNode):
        if tNode != None:
            print(tNode.data, "->", end="")
        else:
            print("None")

    def TraverseElement(self):
        cNode = self.head
        if cNode.next == None:
            print("当前单链表为空！")
            return
        print("您当前的单链表为：")
        while cNode != None:
            cNode = cNode.next
            self.VisitElement(cNode)


if __name__ == '__main__':
    LinkList = SingleLinkedList()
    LinkList.CreateSingleLinkedList()
    LinkList.TraverseElement()
    LinkList.InsertElementInTail()
    LinkList.TraverseElement()
    LinkList.InsertElementInHead()
    LinkList.TraverseElement()
    LinkList.FindElement()
    LinkList.DeleteElement()
    LinkList.TraverseElement()
