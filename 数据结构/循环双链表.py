class DoubleLinkedNode(object):

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoubleLinkedList(object):

    def __init__(self):
        self.head = DoubleLinkedNode(None)

    def CreateCircularDoubleLinkedList(self):

        print("请输入数据按回车确认，按#号退出")

        data = input("请输入元素：")
        cNode = self.head
        while data != "#":
            nNode = DoubleLinkedNode(int(data))
            cNode.next = nNode
            nNode.prev = cNode
            nNode.next = self.head
            self.head.prev = nNode
            cNode = cNode.next
            data = input("请输入元素：")

    def GetLength(self):
        cNode = self.head
        length = 0
        while cNode.next != self.head:
            length = length + 1
            cNode = cNode.next
        return length

    def IsEmpty(self):
        if self.head.next == None:
            return True
        else:
            return False

    def InsertElementInTail(self):
        Element = input("请输入待插入结点的值：")
        if Element == "#":
            return
        nNode = DoubleLinkedNode(int(Element))
        cNode = self.head
        while cNode.next != self.head:
            cNode = cNode.next
        cNode.next = nNode
        nNode.prev = cNode
        nNode.next = self.head
        self.head.prev = nNode

    def InsertElementInHead(self):
        Element = input("请输入待插入结点的值：")
        if Element == "#":
            return
        cNode = self.head.next
        pNode = self.head
        nNode = DoubleLinkedNode(int(Element))
        nNode.prev = pNode
        pNode.next = nNode
        nNode.next = cNode
        cNode.prev = nNode

    def DeleteElement(self):
        dElement = int(input('请输入待删除结点的值：'))
        cNode = self.head
        pNode = self.head
        if self.IsEmpty():
            print("当前双链表为空！")
            return
        while cNode.next != self.head and cNode.data != dElement:
            pNode = cNode
            cNode = cNode.next
        if cNode.data == dElement:
            qNode = cNode.next
            pNode.next = qNode
            qNode.prev = pNode
            del cNode
            print(f"成功删除含有元素{dElement}的结点")
        else:
            print(f"删除失败！双链表中不存在含有元素{dElement}的结点")

    def TraverseElement(self):
        if self.IsEmpty():
            return
        cNode = self.head.next
        print("按next域遍历带头结点双链表:")
        while cNode.next != self.head:
            print(cNode.data, "->", end="")
            cNode = cNode.next
        print(cNode.data)


if __name__ == "__main__":
    CDLL = CircularDoubleLinkedList()
    CDLL.CreateCircularDoubleLinkedList()
    CDLL.TraverseElement()
    CDLL.InsertElementInHead()
    CDLL.TraverseElement()
    CDLL.InsertElementInTail()
    CDLL.TraverseElement()
    CDLL.DeleteElement()
    CDLL.TraverseElement()
