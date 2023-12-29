
from gettext import find


class DirNode(object):
        def __init__(self, name):
            self.name = name
            self.parent = None # ref to parent direction
            self.children = dict()  # dir_name -> reference
            self.file_list = []
            self.ls_dir_size = 0
            
        def add_child(self, obj):
            self.children[obj.name] = obj
            obj.parent = self
                      
            
            
class FileTree():
    
    def __init__(self) -> None:
        self.root = DirNode("/")
    
    def is_present(self, node_name):
        return self._find(self.root, node_name)


    def _find(self, node, node_name_to_find):  # not used
       # if node.name == node_name_to_find:
        #    return node
        print(f'{node.name} {node.ls_dir_size}')
        for child in node.children:
            result = self._find(child, node_name_to_find)
            if result is not None:
                return result
            
        return None
        
        
        
    
    
    
    