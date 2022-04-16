class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSingleLinkedList(object):
    def __init__(self):

        self.head = Node(None)

    def CreateCircularSingleLinkedList(self):
        print("请输入数据按回车确认，按#号结束")
        data = input("请输入结点的值：")
        cNode = self.head
        while data != "#":
            nNode = Node(int(data))
            cNode.next = nNode
            nNode.next = self.head
            cNode = cNode.next
            data = input("请输入结点的值：")

    def InsertElementInTail(self):
        Element = input("请输入待插入结点的值（尾插）：")
        if Element == "#":
            return
        cNode = self.head
        nNode = Node(int(Element))
        while cNode.next != self.head:
            cNode = cNode.next
        cNode.next = nNode
        nNode.next = self.head

    def InsertElementInHead(self):
        Element = input("请输入待插入结点的值（头插）：")
        if Element == "#":
            return
        cNode = self.head
        nNode = Node(int(Element))
        nNode.next = cNode.next
        cNode.next = nNode

    def GetLength(self):
        cNode = self.head
        if self.head is None:
            return
        length = 1
        while cNode.next is not self.head:
            cNode = cNode.next
            length = length + 1
        return length

    def IsEmpty(self):
        return self.head is None

    def DeleteElement(self):
        dElement = int(input("请输入待删除结点的值："))
        cNode = self.head
        pNode = self.head
        if self.IsEmpty():
            print("当前循环单链表的为空！")
            return
        while cNode.next != self.head and cNode.data != dElement:
            pNode = cNode
            cNode = cNode.next
        if cNode.data == dElement:
            pNode.next = cNode.next
            del cNode
            print(f"成功删除含有元素{dElement}的结点")
        else:
            print(f"删除失败！循环双链表不存在含有元素{dElement}的结点")

    def FindElement(self):
        Posi = 0
        cNode = self.head
        key = int(input("请输入想查找的元素值："))
        if self.IsEmpty():
            print("当前链表为空，不存在该元素")
            return
        while cNode.next != self.head:
            if cNode.data == key:
                return True
            else:
                cNode = cNode.next
                Posi = Posi + 1
        if cNode.data == key:
            print(f"查找成功！元素值为{key}的结点位于该单链表的第{Posi}位")
        else:
            print(f"查找失败！当前单链表中不存在{key}元素")

    def TraverseElement(self):
        if self.IsEmpty():
            return
        cNode = self.head
        while cNode.next != self.head:
            print(f"当前结点为：{cNode.data}")
            cNode = cNode.next
        print(f"当前结点为：{cNode.data}")


LinkList = CircularSingleLinkedList()
LinkList.CreateCircularSingleLinkedList()
LinkList.TraverseElement()
LinkList.InsertElementInTail()
LinkList.TraverseElement()
LinkList.InsertElementInHead()
LinkList.TraverseElement()
LinkList.FindElement()
LinkList.DeleteElement()
LinkList.TraverseElement()
