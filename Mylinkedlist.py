######################################################################################################################
#####                                      Implementation of Singly Linked List in Python                     ########
##### Created By: Thomas                                                                                      ########
######################################################################################################################
##### Functions Used in Linked list:                                                                          ########
##### 1) displist       - to display the linked list                                                          ########
##### 2) listsize       - to check the size of linked list                                                    ########   
##### 3) adddata_end    - to add data to end of linked list                                                   ########
##### 4) adddata_begin  - to add data to beginning of linked list                                             ########
##### 5) adddata_pos    - to add data at any postion in the linked list                                       ########
##### 6) deldata_end    - to delete data at end of linked list                                                ########
##### 7) deldata_begin  - to delete data at beginning of linked list                                          ########
##### 8) deldata_pos    - to delete data at any postion in the linked list                                    ########
##### 9) deldata_val    - to delete data by value that is present within the linked list                      ########
##### 10) sortdata      - to sort the linked list in ascending or descending order                            ########
##### 11) finddata      - to find a particular data in the linked list                                        ########
######################################################################################################################

class mynode:

    def __init__(self,data=None):
        self.data = data
        self.nextptr = None

class MyLinkList:

    def __init__(self):
        self.first = mynode()

    def displist(self):
        listall = []
        curr_node = self.first
        if curr_node.data == None:
            return print(listall)
        while curr_node:
            listall.append(curr_node.data)
            curr_node = curr_node.nextptr
        print (listall)

    def listsize(self):
        total = 0
        curr_node = self.first
        if curr_node.data == None:
            return total
        while curr_node.nextptr !=None:
            total = total +1
            curr_node = curr_node.nextptr
        return (total +1)

    def adddata_end(self,data):
        if self.first.data == None:
            self.first = mynode(data)
            curr_node = self.first
            new_node = curr_node.nextptr
        else:
            new_node = mynode(data)
            curr_node = self.first
        while curr_node.nextptr!= None:
            curr_node = curr_node.nextptr
        curr_node.nextptr = new_node

    def adddata_begin(self,data):
        if self.first.data == None:
            self.first = mynode(data)
            curr_node = self.first
            new_node = curr_node.nextptr
        else:
            new_node = mynode(data)
            curr_node = self.first
            prev_node = new_node
            prev_node.nextptr = curr_node
            self.first = new_node

    def adddata_pos(self,data,pos):
        if pos > (self.listsize() + 1):
            return (print("Could not add data at position {}".format(pos)))
        if self.first.data == None:
            self.first = mynode(data)
            curr_node = self.first
            new_node = curr_node.nextptr
        else:
            curr_pos = 1
            prev_node = self.first
            curr_node = self.first
            while True:
                if pos == curr_pos:
                    if pos == 1:
                        #curr_node = prev_node.nextptr
                        new_node = mynode(data)
                        self.first = new_node
                        new_node.nextptr = curr_node
                        return (print("Data added successfully at pos {}".format(pos)))
                    new_node = mynode(data)
                    prev_node.nextptr = new_node
                    new_node.nextptr = curr_node
                    return (print("Data added successfully at pos {}".format(pos)))
                prev_node = curr_node
                curr_node = curr_node.nextptr
                curr_pos = curr_pos + 1

    def deldata_end(self):
        curr_node = self.first
        if curr_node.data == None:
            return print(("List already empty, nothing deleted"))
        if curr_node.nextptr == None:
            self.first = mynode()
            return print("Data deleted at end")
        prev_node = self.first
        while curr_node.nextptr != None :
            prev_node = curr_node
            curr_node = curr_node.nextptr
        prev_node.nextptr = curr_node.nextptr

    def deldata_begin(self):
        if self.first.data == None:
            return print ("List already empty, nothing deleted")
        if self.listsize()==1:
            self.first = mynode()
            return (print("Data deleted at beginning"))
        else:
            prev_node = self.first
            curr_node = prev_node.nextptr
            self.first = curr_node

    def deldata_pos(self, pos):
        if pos > self.listsize():
            return (print("Cannot perform deletion at position {} as it does't exit".format(pos)))
        if pos <= 0:
            return (print("{} is Not a valid postion to delete data from".format(pos)))
        else:
            curr_pos = 1
            prev_node = self.first
            curr_node = self.first
            while True:
                if pos == curr_pos:
                    if pos == 1 and self.listsize() == 1:
                        self.first = mynode()
                        return
                    else:
                        prev_node.nextptr = curr_node.nextptr
                        return (print("Data removed successfully at pos {}".format(pos)))
                prev_node = curr_node
                curr_node = prev_node.nextptr
                curr_pos = curr_pos + 1
                
    def deldata_val(self,val):
        size = self.listsize()
        curr_node = self.first
        prev_node = self.first
        if curr_node.data == None:
            return (print("Linked list already empty. Cannot perform delete"))

        if size == 1:
            if curr_node.data == val:
                self.first = mynode()
                return (print("Removed 1 Item. Now Linked List has no data"))
            else:
                return (print("Data {} to be removed not found in list".format(val)))

        while True:
            if curr_node.data == val:
                prev_node.nextptr = curr_node.nextptr
                return (print("{} removed successfully".format(val)))
            prev_node = curr_node
            curr_node = curr_node.nextptr
            if curr_node.nextptr == None:
                return (print("Data {} to be removed not found in list".format(val)))

    def sortdata(self,choice):
        prev_node = self.first
        curr_node = self.first
        max = prev_node.data
        min = prev_node.data
        if curr_node.data == None:
            return (print("Linked list already empty. Cannot perform sort"))
        curr_node = prev_node.nextptr
        if self.listsize() == 1:
            return (print("Only one entry. Sort not required"))
        if choice == 'D':
            while True:
                if curr_node.data > max:
                    prev_node.data = curr_node.data
                    curr_node.data = max
                    max = prev_node.data
                if curr_node.nextptr == None:
                    prev_node = prev_node.nextptr
                    max = prev_node.data
                    curr_node = prev_node
                if prev_node.nextptr == None:
                    return (print("Linked list sorted in Descending order complete"))
                curr_node = curr_node.nextptr
        if choice == 'A':
            while True:
                if curr_node.data < min:
                    prev_node.data = curr_node.data
                    curr_node.data = min
                    min = prev_node.data
                if curr_node.nextptr == None:
                    prev_node = prev_node.nextptr
                    min = prev_node.data
                    curr_node = prev_node
                if prev_node.nextptr == None:
                    return (print("Linked list sorted in Ascending order complete"))
                curr_node = curr_node.nextptr
        else:
            return (print("Choose valid Input A or D"))

    def finddata(self,val):
        curr_node = self.first
        if curr_node.data == None:
            return (print("Linked list already empty. Cannot perform find"))
        if self.listsize() == 1:
            if curr_node.data == val:
                return (print("Found {}".format(val)))
            else:
                return (print("{} not found".format(val)))
        while True:
            if curr_node.data == val:
                return (print("Found {}".format(val)))
            curr_node = curr_node.nextptr
            if curr_node.nextptr == None:
                return (print("{} not found".format(val)))



myllist = MyLinkList()
myllist.adddata_end(5)
myllist.adddata_end(4)
myllist.adddata_end(6)
myllist.displist()
myllist.adddata_begin(3)
myllist.adddata_begin(2)
myllist.displist()
myllist.adddata_pos(1,4)
myllist.displist()
myllist.deldata_end()
myllist.displist()
myllist.deldata_begin()
myllist.displist()
myllist.deldata_pos(1)
myllist.displist()
myllist.sortdata('D')
myllist.displist()
myllist.finddata(3)
