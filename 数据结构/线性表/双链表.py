# 带头结点的双链表
class DoubleLinkedNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList(object):
    def __init__(self):
        self.head = DoubleLinkedNode(None)

    def CreateDoubleLinkedList(self):
        print("输入数据按回车确认，按#号结束")
        data = input("请输入元素：")
        cNode = self.head
        while data != "#":
            nNode = DoubleLinkedNode(int(data))
            cNode.next = nNode
            nNode.prev = cNode
            cNode = cNode.next
            data = input("请输入元素：")

    def GetLength(self):
        cNode = self.head.next
        length = 0
        while cNode != None:
            length = length + 1
            cNode = cNode.next
        return length

    def IsEmpty(self):
        if self.head.next == None:
            return True
        else:
            return False

    def InsertElementInTail(self):
        Element = input("请输入待插入结点的值（尾插）：")
        if Element == "#":
            return
        nNode = DoubleLinkedNode(int(Element))
        cNode = self.head
        while cNode.next != None:
            cNode = cNode.next
        cNode.next = nNode
        nNode.prev = cNode

    def InsertElementInHead(self):
        Element = input("请输入待插入结点的值（头插）：")
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
        dElement = int(input("请输入待删除结点的值："))
        cNode = self.head
        pNode = self.head
        if self.IsEmpty():
            print("当前双链表为空：")
            return
        while cNode.next != None and cNode.data != dElement:
            pNode = cNode
            cNode = cNode.next
        if cNode.data == dElement:
            if cNode.next == None:
                pNode.next = None
                del cNode
                print(f"成功删除数据值为{dElement}的结点")
            else:
                qNode = cNode.next
                pNode.next = qNode
                qNode, prev = pNode
                del cNode
                print(f"成功删除数据值为{dElement}的结点")
        else:
            print(f"删除失败！当前双链表中不含有值为{dElement}的结点")

    def TraverseElement(self):
        cNode = self.head
        print("按照next域遍历带头结点的双链表：")
        if self.IsEmpty():
            print("当前双链表为空！")
            return
        while cNode.next != None:
            cNode = cNode.next
            print(cNode.data, "->", end="")
        print("None")


if __name__ == '__main__':
    DLL = DoubleLinkedList()
    DLL.CreateDoubleLinkedList()
    DLL.TraverseElement()
    DLL.InsertElementInHead()
    DLL.TraverseElement()
    DLL.InsertElementInTail()
    DLL.TraverseElement()
    DLL.DeleteElement()
    DLL.TraverseElement()
