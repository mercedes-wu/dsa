class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = []
    def add_child(self, obj):
        self.children.append(obj)