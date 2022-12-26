from advent.common import task_output, read_file_line_by_line
from tree import DirNode, FileTree
import numpy as np


def handle_change_dir(dir_name, current_node, file_system):
    if dir_name == "/":
        return file_system.root
    
    if dir_name == "..":
        return current_node.parent
    
    if dir_name not in current_node.children.keys(): # does not happen, but is possible theoretically
        new_node = DirNode(dir_name)
        current_node.add_child(new_node)
        return new_node
    else:
        for name, ref in current_node.children.items():
            if name == dir_name:
                return ref


def build_file_system_tree(file_system, input):
    current_node = file_system.root
    for line in input:
        comps = line.split(" ")
        if comps[0] == "$":
            if comps[1] == "cd":   # only handle cd command, ls has no effect -> ignore
                current_node = handle_change_dir(comps[2], current_node, file_system)
           
        else: # listing files from ls
            if comps[0] == "dir": #  potentially useless information, only add to tree if cd'ing
                dir_name = comps[1]
                if dir_name not in current_node.children.keys():
                    current_node.add_child(DirNode(dir_name))
                   
            else:
                file_size = comps[0]
                file_name = comps[1]
                if file_name not in current_node.file_list:
                    current_node.file_list.append(file_name)
                    current_node.ls_dir_size += int(file_size)
                    
              
def common() -> np.ndarray:
    '''
        Returns numpy array with all directory sizes (recursive sizes)
    '''
    input = read_file_line_by_line("advent/day07/input.txt")
    file_system = FileTree() # initiated  with / as root direction
    
    build_file_system_tree(file_system, input)
    
    dir_sizes = []
    
    def travers_tree(node):
        child_size = 0
        for n in node.children.values():
            child_size += travers_tree(n)
        
        total = child_size + node.ls_dir_size
        dir_sizes.append(total)
        return total
    
    travers_tree(file_system.root)
    
    return np.array(dir_sizes)
        
        
@task_output(challenge=1)
def task1():
    dir_sizes = common()
    return np.sum(dir_sizes[dir_sizes <= 100000])


@task_output(challenge=2)
def task2():
    dir_sizes = common()
    total_space_used = np.max(dir_sizes)
    
    total_file_system_size = 70000000
    required_space = 30000000
    
    min_free_size = required_space - (total_file_system_size - total_space_used)
    return np.min(dir_sizes[dir_sizes >= min_free_size])
   
   
if __name__ == "__main__":
    task1()
    task2()