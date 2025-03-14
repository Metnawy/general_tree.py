from functools import total_ordering
import copy
class general_tree:
    @total_ordering
    class tree_node:#there are still some methods need to complete after finishing the positon nested class 
        '''
        objectives:it's nested lass to generate objects represent the nodes of the tree ...with the same type ordered childern 
        '''
        def __init__(self,data,parent=None):
            self.parent=parent
            self.data=data
            self._childern=[] 
           
        #very critical point here related to the children of the node i shouldn't have direct access publicly to change it's value entirely which has very severe consequences on the form of the tree as it' recursive nature in the case of general tree 
        
        #write  a defenive code her to prevent any change in self.data could lead to inconsistancy of the childern of the parent 
        @property
        def data(self):#getter
            return self._data
        @data.setter#setter
        def data(self,data):
            if not self.parent:
                self._data=data
                return 
            elif not len(self.parent.childern()):
                self._data=data
                return 
          
            if isinstance(data,type(self.parent._childern[0].data)):
                self._data=data
                return
            else:
                raise TypeError
            
        @property 
        def parent(self):
            return self._parent 
        @parent.setter
        def parent(self,parent):
            
            if isinstance(parent,(type(None),general_tree.tree_node)):
                self._parent=parent
            else:
                raise TypeError
            
        
        ### operation on the node childern ###
        def search_childern_index(self,index):
            '''
            objectives:using index to get the node childern ...return the node object itself 
            '''
            if not isinstance(index,int):
                raise TypeError
            else:
                if not (0<=index<len(self._childern)):
                    raise IndexError
                else:
                    return self._childern[index]
                
        def search_childern_value(self,value):
            '''
            objectives:searching if the value exists in the childern of that parent return the node reprsents that value ...return none if it doesn't exist or it was empty

            '''
            if not self.size_childern():
                return  None
            if not isinstance(value,type(self._childern[0])):
                return None
            for i in self.childern:
                if value==i.data:
                    return i
            return None


        def _shift_forward(self,the_list,new_node,start_index):
            '''
            new_node:tree_node object
            start_index:the first index will assign the new _node to it then shift the rest of the list forward 
            '''
        
            the_list.append(None)
            x=len(the_list)-start_index
            
            for i in range(1,x):
                
                the_list[-i]=the_list[(-i)-1]
            the_list[start_index]=new_node
        
        def add_child(self,data):#setter 1
            def helper(the_list,new_node,start,end):
                       if start==end:
                           if start==0:
                               if new_node.data<=the_list[start].data:
                                
                                  self._shift_forward(self._childern,new_node,start)
                               else:
                                  
                                   self._shift_forward(self._childern,new_node,start+1)
                           else:
                               if new_node.data<=the_list[start].data:
                                  
                                   self._shift_forward(self._childern,new_node,start)
                               else:
                                
                                  self._childern.append(new_node)
                           
                       else:
                        mid=(start+end)//2
                        if new_node.data==the_list[mid].data:
                            self._shift_forward(self._childern,new_node,mid)
                            
                        elif  new_node.data<the_list[mid].data:
                            if the_list[mid] is the_list[0]:
                                self._shift_forward(self._childern,new_node,mid)
                                
                            else:
                            
                                   helper(the_list,new_node,0,mid)
                                   
                        elif  new_node.data>the_list[mid].data:
                            if the_list[mid] is the_list[-1]:
                               the_list.append(new_node)
                               
                            else:
                           
                                  helper(the_list,new_node,mid+1,end)
            
            if self.size_childern()==0:
                
                new_node=general_tree.tree_node(data,self)### may be this line acause of a problem 
                self._childern.append(new_node)
                return new_node
            else:
                new_node=general_tree.tree_node(data,self)
                if isinstance(new_node.data,type(self._childern[0].data)):
                        
                    helper(self._childern,new_node,0,len(self._childern)-1)     
                    return new_node
                else:
                    raise TypeError(f"as the consistancy of the sibilings' type:{type(self._childern[0])} and new data type:{type(data)} , the input is refused")


        def delete_child_index(self,index):#setter 2 
           '''
           objectives:delete a node from the childern of the parent and implicitly it's childern
           output:the value deleted node or none if it's not exist in the childern of parent 
           '''
           if not isinstance(index,int):
              raise TypeError("the index should be intger")
           else:
               if not (0<=index<=len(self._childern)):
                   raise IndexError("the index you want to delete the associated node doesn't exist")
               else:
                   x=self._childern[index].data
                   for i in range(index,len(self._childern)-1):
                       self._childern[i]=self._childern[i+1]
                   self._childern.pop()
                   return x
            
        def delete_child_value(self,value):#setter3
            '''
            objectives: delete specific node by searching of with it's data value
            output:return the node to be delete ... or none if it doesn't exist 
            note:it delete the first existance of that value
            '''
            if self.size_childern()==0:
            
                return None
            if not (type(value)==type(self._childern[0].data)):
                
                return None
            
            index=-1
            for i in self._childern:
                index+=1
                if value==i.data:
                    return self.delete_child_index(index)
                
            return None
            # need to discuss the recursive/deeper insertion or deletion 

    
        ### info about the node generally###

        def __repr__(self):
            
             return f"{self.data}"
        
        def childern(self):#getter
            return self._childern

        def size_childern(self):
            return len(self._childern)
        
        def the_data(self):
            return self.data

        def the_parent(self):
            return self.parent#return position object represents the parent of that node 
        
        
        def type_parent(self):
            return type(self.parent.node.data)

        def type_node(self):
            return type(self.data)
        
        def type_childern(self):
            return type(self._childern[0])
        
        #comparsion

        def __eq__(self,second):
            if isinstance(second,general_tree.tree_node):
                return self.data==second.data
            else:
                raise TypeError
        def __lt__(self,second):
            if isinstance(second,general_tree.tree_node):
                return self.data<second.data
            else:
                raise TypeError
 

    @total_ordering
    class _position:
        def __init__(self,node,container):
            self.node=node
            self.container=container

        def __repr__(self):
            return f"{self.node}"
        #comparsion 
        def __eq__(self,second):
            if not isinstance(second,general_tree._position):
                raise TypeError
            else:
                if self.node.data==second.node.data and self.node.parent==second.node.parent and self.node._childern==second.node._childern:
                    return True
                else:
                    return False
                
        def __lt__(self,second):
            if not isinstance(second,general_tree._position):
                raise TypeError
            if self.node.data<second.node.data and self.node.parent<second.node.parent and self.node._childern<second.node._childern:
                    return True
            else:
                    return False
    
    def __init__(self,root=None):
        self.root=root


    @property
    def root(self):
        return self._root
    @root.setter
    def root(self,r):
        if isinstance(r,(type(None),general_tree.tree_node)):
            self._root=r
        else:
            raise TypeError

    ### operation###
    #addition 
    def add_to_root_childern(self,data):
        '''
        objective :add a new node to the childern of the root if it is possible 
        '''
        if not self.root:

            new_node=self.tree_node(data)
            self.root=new_node
            return
        
        self.root.add_child(data)
        return 
    
    def add_to_child_no_depth_index(self,data,index):
        """
        objectives:choosing specific element of the root childern using index then if it's data consistancy accepts add new data to them if it will violate the consistancy of ...will raise error 
        """
        if not self.root or not self.root._childern:
            return "no new inseration this empty tree ,,may be there is no more than the root "
        if not isinstance(index,int):
            raise TypeError("the index should be intger")

        if not (0<=index<=len(self.root._childern)):
    
              raise IndexError('this index of element you want to insert on it doesnt exist')
        else:
            if not self.root._childern[index]._childern:
                new_node=general_tree.tree_node(data,self.root._childern[index])
                self.root._childern[index]._childern.append(new_node)
                return general_tree._position(new_node,self)
            if not isinstance(data,type(self.root._childern[index]._childern[0])):
                          
                raise TypeError("this data isn't consistant with the dominant data type in the childern of the node")
            else:
                new_node=self.root._childern[index].add_child(data)
                return general_tree._position(new_node,self)


    def add_to_child_with_depth_index(self,data,index):
        '''
        objectives:here the topic is  more complex we add the new child as the child of one of the root childs at that index 
        if we have a problem to insert here due to consistancy we iterate depthlly with all it's childern to get fist suitable place
        '''
        
        if not self.root or not self.root._childern:
            return "no new inseration this empty tree ,,may be there is no more than the root "

        if not isinstance(index,int):
            raise TypeError("the index should be intger")
        
        if not (0<=index<=len(self.root._childern)):
            raise IndexError("this index of element you want to insert on it doesnt exist")
        concerned=self.root._childern[index]
        if isinstance(data,type(concerned._childern[0])):
            new_node=concerned.add_child(data)
            return general_tree._position(new_node,self)
        else: 
        
            for i in range(len(concerned._childern)):
                x=helper(concerned._childern[i],data)
                if x:
                    return general_tree(x,self)


        def helper(start,data):
            if not start._childern:
                new_node=general_tree.tree_node(data,start)
                start._childern.append(new_node)
                return new_node
            else:
                if isinstance(data,type(start._childern[0])):
                    new_node=start.add_child(data)
                    return new_node
                else:
                    for i in range(len(start._childern)):
                        x=helper(start._childern[i],data)
                        if x:
                            return x
                    return False

    def add_child_first_available(self,data):
        if not  self.root:
            new_node=self.tree_node(data)
            self.root=new_node
            return general_tree._position(new_node,self)
        all_childern=[self.root]  

        while all_childern :

            x=all_childern.pop(0)
            if not x._childern:
                new_node=general_tree.tree_node(data,x)
                x._childern.append(new_node)
                return general_tree._position(new_node,self)
            else:
                if isinstance(data,type(x._childern[0])):
                    new_node=x.add_child(data)
                    return general_tree._position(new_node,self)
                else:
                    for i in x._childern:
                        all_childern.append(i)

    def add_child_using_positon_without_depth(self,data,position):
        '''
        objectives:here we use the utility of nested class position to access specific node on the tree without need to travrse from the root 
        here if there is no consistancy of the new data with the existed data the operation is being refused 
        paramaters:
        data :to add
        position:position object resembles the targeted node
        '''
        if not (isinstance(position,general_tree._position) and position.container==self):
           raise TypeError
        else:
            if not position.node._childern:
                new_node=general_tree.tree_node(data,position.node)
                position.node._childern.append(new_node)
                return general_tree.tree_node(new_node,self)
            elif not isinstance(data,position.node._childern[0]):
                raise TypeError
            else:
                new_node=position.node.add_child(data)
                return general_tree.tree_node(new_node,self)

    def add_child_using_positon_with_depth(self,data,position):
        '''
        objectives:here we use the utility of nested class position to access specific node on the tree without need to travrse from the root 
        here if there is no consistancy of the new data with the existed data ....we continue searching to get a suitable place to this new data in the tree 
        starting from position node
        paramaters:
        data :to be added 
        position:position object resembles the targeted node
        '''
        if not (isinstance(position,general_tree._position) and position.container==self):
           raise TypeError
        else:
            if not position.node._childern:
                new_node=general_tree.tree_node(data,position.node)
                position.node._childern.append(new_node)
                return general_tree._position(new_node,self)
            elif  isinstance(data,position.node._childern[0]):
                new_node=position.node.add_child(data)
                return general_tree._position(new_node,self)
            else:
                 
                 all_childern=[position.node]

                 while all_childern:
                     new=all_childern.pop(0)
                     if not new._childern:
                         new_node=general_tree.tree_node(data,new)
                         new._childern.append(new_node)
                         return general_tree._position(new_node,self)
                     if type(data)==type(new._childern[0]):
                         new_node=new.add_child(data)
                         return general_tree._position(new_node,self)
                     for i in new._childern:
                         all_childern.append(i)

    

    #deletion methods

    def delete_root_son_index(self,root,index):
        #deletion of one of roots sons reaching to it by the index
        if not self.root :
            return None
       
        if not (root is self.root):
            raise ValueError

        if not isinstance(index,int):
            raise TypeError("the index should be intger")
        
        if not (isinstance(index,int) and (0<=index<=len(self.root._childern)-1)):
            return TypeError
        concerned_node=self.root._childern[index]
        concerned=concerned_node.data
        for i in range(index,len(self.root._childern)-1):
            self.root._childern[i]=self.root._childern[i+1]
        
        self.root._childern.pop()
        concerned_node._parent=None
        concerned_node._data=None
        return concerned
    


    def delete_root_son_value(self,root,value):
        '''
        objectives:delete specif child of the root ..reaching to it by it's value 
        parameters :root node , the value to be searched
        '''

        if not root==self.root:
            raise ValueError("that's method is suitable to root element only ")
        if not self.root:
            return None 
        if not ( type(value)==type(self.root._childern[0].data)):
            
            return None
        
        index=-1
        for i in self.root._childern:
            index+=1
            if i.data==value:
                 
                 concerned_node=self.root._childern[index]
                 concerned=concerned_node.data
                 for x in range(index,len(self.root._childern)-1):
                     self.root._childern[x]=self.root._childern[x+1]

                 self.root._childern.pop()
                 concerned_node._parent=None
                 concerned_node._data=None
                 return concerned
        return None
    
    def delete_position(self,position):
        if not (isinstance(position,general_tree._position) and position.container==self):
            raise ValueError
        if not self.root:
            return None
        if position.node is self.root :
            
            value=self.root.data
            self.root=None
            return value
        parent=position.node.parent
        
     
        value=position.node.data
        index=-1

        for i in parent._childern:
            index+=1
            if i is position.node:
                
                for x in range(index,len(parent._childern)-1):
                    parent._childern[x]=parent._childern[x+1]
                parent._childern.pop()
                return value
        
    def delete_node_son_index(self,node,index):
        if not (isinstance(node,general_tree.tree_node)):
            return False

        if not self.root:
            return False

        if not self.root._childern:
            return False

        all_nodes=[self.root]

        while all_nodes:
            x=all_nodes.pop(0)

            if node is x:
                if not node._childern:
                    return None
                if (isinstance(index,int) and 0<=index<=len(node._childern)):
                     concerned_node=node._childern[index]
                     concerned=concerned_node.data
                     for i in range(index,len(node._childern)-1):
                        node._childern[i]=node._childern[i+1]
        
                     node._childern.pop()
                     concerned_node._parent=None
                     concerned_node._data=None
                     return concerned
                else:
                    raise IndexError

                
            for i in x._childern:
                all_nodes.append(i)
        return False
        
    
    def delete_node_son_value_with_breadth(self,node,value):
        '''
        objectives:deleting a son / grand son of a node in the tree 
        parameters:
        node:general_tree.tree_node object of the used tree(object of general_tree class)
        value:the value which will  the assoicated node be deleted ...where the search will start from the node argument ,,scanning in by breadth approach
        output :true ..the node was founded and deleted ; false ... we didn't find a node to be deleted or there is something wrong related
        to node (ins't accepted object) or already the tree is empty which means no deletion happened 
        '''
        if not (isinstance(node,general_tree.tree_node)):
            return False

        if not self.root:
            return False

        if not self.root._childern:
            return False

        all_nodes=[self.root]
        #
        while all_nodes:
            # to get the argument node ...and confirm it's part of the concerned tree (then start from it search on son the argument value to delete...
            # or return false as we didn't find that node here in the list )
            x=all_nodes.pop(0)
            #
            if node is x:
            # from here we start new session of the algorithm where finsihed the mission to confirm the belonging of node to that tree
            #search the son /grand son of that node to delete returning true or returning false if we didn't find any son/grand son with that value 
                if not node._childern:
                    return False
                 
                ##
                new_all=[]+node._childern

                while new_all:
                    n=new_all.pop(0)
                    
                    if n._childern:
                       

                       if  type(n._childern[0])==type(node):

                            index=-1
                    
                            for i in node._childern:
                                
                                index+=1
                                if i.data==value:
                            
                           
                                  for m in range(index,len(n._childern)-1):
                                      n._childern[m]=n._childern[m+1]

                                  n._childern.pop()
                                  i._data=None
                                  i._parent=None
                                  return True
                    for i in n._childern:
                                new_all.append(i)
                return False
        
                
                
            #
            for i in x._childern:
                all_nodes.append(i)
        #
        return False
        

    #value depth in deletion by value
       
        
    
    def view_sibilings_node_by_position(self,position):
        if not(isinstance(position,general_tree._position) and position.container==self):
            raise TypeError
        
        else:
            parent=position.node.parent
            return parent._childern



    ### information ###

    def belonging(self,node):
        #is it node belong to that tree 
        if not (isinstance(node,general_tree.tree_node)):
            return False

        if not self.root:
            return False


        all_nodes=[self.root]

        while all_nodes:
            x=all_nodes.pop(0)

            if node is x:
              if node.data==x.data and node.parent==x.parent and node._childern==x._childern:
                return True
            for i in x._childern:
                all_nodes.append(i)
        return False

    def the_tree(self,start,space=0,level=0):
        if not start:
            return
        if not start._childern:
            return

        print(" "*space,f"R:{start}")
        print(" "*space,f" level({level+1}):",start._childern)

        for i in start._childern:
              self.the_tree(i,space+5,level+1)


    def size(self):

        if not self.root:
            return 0
        if not self.root._childern:
            return 1

        all_nodes=[self.root]
        size=1

        while all_nodes:
            x=all_nodes.pop(0)
            size=size+len(x._childern)

            for i in x._childern:
                all_nodes.append(i)

        return size


    def height2(self,node):
        
        #is it node belong to that tree 
        if not (isinstance(node,general_tree.tree_node)):
            raise ValueError

        if not self.root:
           raise ValueError


        def helper(start):
            if not start._childern:
                return 0
            else:
                return 1+max(helper(i) for i in start._childern )
        

        all_nodes=[self.root]

        while all_nodes:
            x=all_nodes.pop(0)

            if node is x:
              if node.data==x.data and node.parent==x.parent and node._childern==x._childern:
                 return helper(node)
            for i in x._childern:
                all_nodes.append(i)
        raise ValueError("this node doesn't belong to this tree")
    
    
    def height(self):
        if not self.root:
        
            return None
        if not self.root._childern:
            return 0
        def helper(start):
            if not start._childern:
                return 0
            all=[]
            for i in start._childern:
                all.append(helper(i))
            return 1+max(all)
        return helper(self.root)

    def level(self,node):
        '''
        objectives: calculating the level/depth of specific node from the root of the tree
        inputs: concerned node 
        outputs: either the level/depth of the node OR  none if it doesn't node or deosn't belong to the tree 
        '''
        if not(isinstance(node,general_tree.tree_node)):
            raise TypeError("this isn't node to check the level of it in the tree ")

        #here we try to do two things simultinously check if that node belong to the concerned tree or not ,,,and if it is on return it's level/depth
        if not self.root:
     
            return None

        if not self.root._childern:
           
            return None

        if node is self.root:
            return 0
        
        def helper(root,node,level=0):
            if  not node.parent :
                
                return None
            if node.parent  is self.root:
               return 1+level
            return helper(root,node.parent,level+1)
        return helper(self.root,node)


    def breadth_first_search(self,node):
        if not (isinstance(node,general_tree.tree_node)):
            raise TypeError 

        if not self.root:
            return None

        if not self.root._childern:
            return None

        if not self.belonging(node):
            raise ValueError

        all_nodes=[node]
        all_elements=[node]

        while all_nodes:
            x=all_nodes.pop(0)
            if x._childern:
                for i in x._childern:
                    all_nodes.append(i)
                    all_elements.append(i)

        return all_elements

    def depth_first_search_pre_order(self,node):
        if not (isinstance(node,general_tree.tree_node)) :
            raise TypeError
        if not self.root:
            return None
        if not self.root._childern:
            return None
        if not self.belonging(node):
            raise ValueError("this node doesn't belong to the concerned tree")

        
        all_elements=[self.root]
        def helper(start,all_elements):
            if not start._childern:
                return 
            for i in start._childern:
                all_elements.append(i)
                helper(i,all_elements)
            return 
        helper(self.root,all_elements)

        return all_elements


    def depth_first_search_post_order(self,node):
        if not (isinstance(node,general_tree.tree_node)) :
            raise TypeError
        if not self.root:
            return None
        if not self.root._childern:
            return None
        if not self.belonging(node):
            raise ValueError("this node doesn't belong to the concerned tree")

        all_elements=[]
        def helper(start,all_elements):
            if not start._childern:
                return 
            for i in start._childern:
                
                helper(i,all_elements)
                all_elements.append(i)
            return 
        helper(self.root,all_elements)
        all_elements.append(self.root)

        return all_elements


    def __iter__(self,method="breadth"):

       if method=="breadth":
            x=self.breadth_first_search(self.root)

            for i in x:
                 yield i
       elif method=="depth_post":
           x=self.depth_first_search_post_order(self.root)
           for i in x:
               yield i

       elif method=="depth_pre":
            x=self.depth_first_search_pre_order(self.root)
            for i in x:
                yield i
       else:
            raise ValueError


    def search_by_value(self,value):
        '''
        objectives:searching the node with that value on the list 
        output:position object represents that node it's value equals the searched value OR none if it doesn't exist 
        '''

        if not self.root:
            return None

        if not self.root._childern:
            return  None

        all_nodes=[self.root]

        while all_nodes:
            concerned=all_nodes.pop(0)

            if value==concerned.data:
                return general_tree._position(concerned,self)

            for i in concerned._childern:
                all_nodes.append(i)
        return None
        
    def search_by_parent_predicate_zone(self,first,second):
        '''
        objectives:searching of numeric nodes within specific zone 
        inputs:two included edges of the zone
        outputs : a list of _position objects represents that all nodes with the condition or none if dont have any node like that
        '''
        if not(isinstance(first,(int,float))and isinstance(second,(int,float))):
            raise TypeError

        if not self.root:
            return None
        if not self.root._childern:
            return None

        if first <= second:
            first_edge=first
            second_edege=second
        else:
            first_edge=second
            second_edege=first

        all_nodes=[self.root]
        all_elements=[]

        while all_nodes:
            concerned=all_nodes.pop(0)
            if first_edge<=concerned.data<=second_edege:
                all_elements.append(general_tree._position(concerned,self))

            for i in concerned._childern:
                all_nodes.append(i)

        if not all_elements:
            return None
        else:
            return all_elements

    def search_by_childern_predicate_statistics(self,parent_value,case):
        '''
        objectives:get the statistical cases on the childern of the conderned node
         it returns none if the node doesn't exist in the tree 
        '''
        if not self.root:
            return None
        if not self.root._childern:
            return None
        
        if case=="sum":
            all_nodes=[self.root]
            all_elements=[]
            while all_nodes:
                concerned=all_nodes.pop(0)
                if concerned.data==parent_value:
                    if (not concerned._childern) or(not isinstance(concerned._childern[0].data,(int,float))):
                        all_elements.append([general_tree._position(concerned,self),None])
                    else:
                        l=[]
                        for i in concerned._childern:
                            l.append(i.data)
                        all_elements.append([general_tree._position(concerned,self),sum(l)])

                for i in concerned._childern:
                    all_nodes.append(i)

            return all_elements


        elif case=="mean":
            all_nodes=[self.root]
            all_elements=[]
            while all_nodes:
                concerned=all_nodes.pop(0)
                if concerned.data==parent_value:
                    if (not concerned._childern) or(not isinstance(concerned._childern[0].data,(int,float))):
                        all_elements.append([general_tree._position(concerned,self),None])
                    else:
                        l=[]
                        for i in concerned._childern:
                            l.append(i.data)
      
                        all_elements.append([general_tree._position(concerned,self),sum(l)/len(concerned._childern)])

                for i in concerned._childern:
                    all_nodes.append(i)

            return all_elements
        elif case=="median":
            all_nodes=[self.root]
            all_elements=[]
            while all_nodes:
                concerned=all_nodes.pop(0)
                if concerned.data==parent_value:
                    if (not concerned._childern) or(not isinstance(concerned._childern[0].data,(int,float))):
                        all_elements.append([general_tree._position(concerned,self),None])
                    else:
                      mid=len(concerned._childern)//2
                      all_elements.append([general_tree._position(concerned,self),concerned._childern[mid]])

                for i in concerned._childern:
                    all_nodes.append(i)

            return all_elements
            
        elif  case=="mood":
            all_nodes=[self.root]
            all_elements=[]
            while all_nodes:
                concerned=all_nodes.pop(0)
                if concerned.data==parent_value:
                    if (not concerned._childern) or (not isinstance(concerned._childern[0].data,(int,float))):
                        all_elements.append([general_tree._position(concerned,self),None])
                    else:
                       elements={}
                       for i in concerned._childern:
                           if i.data not in elements.keys():
                              elements[i.data]=1
                           else:
                            elements[i.data]=elements[i.data]+1
                  
                       
                        
                       last_one=[]
                       max_value=max(elements.values())
                      
                       if max_value==1:
                              all_elements.append([general_tree._position(concerned,self),None])
                       else:
                            for i in elements.keys():
                                if elements[i]==max_value:
                                    last_one.append(i)
                            
                            all_elements.append([general_tree._position(concerned,self),last_one])
    
                            

                for i in concerned._childern:
                    all_nodes.append(i)

            return all_elements
        else:
            raise ValueError(f"case should be one of those (sum,mean,mood,median)")
        
    def merge_without_change(self,second,mood,start):
        '''
        objectives:merging two general tree objects without  making changes on the the basic (calling) object... the merging will start specific point
        on the tree either by level or the first existance of a value 
        inputs:second is general tree object we need to merge version to the basic(calling )object general tree 
        mood : we have two options /states to start the merging (level,value)
        start: either intger or value according the mood ( start&mood should be consistancy )
        output : a new general tree object with is a merge of two copies of the basic & second
        '''
        if not (isinstance(second,(general_tree))):
            raise TypeError

        # the case of either or both lists are empty 
        if (not self.root) and (not second.root):
            raise ValueError("both of them is empty ...no meaning of merging ")
        if (not self.root) and (second.root):
            new_self=general_tree()
            new_copy=copy.deepcopy(second)
            new_copy.root.parent=None
            new_self.root=new_copy.root
            return new_self.the_tree(new_self.root)
        if (self.root) and (not second.root):
            new_self=copy.deepcopy(self)
            return new_self.the_tree(new_self.root)

        if mood=="value":
            def insert(the_list,second):
              while the_list:
                node=the_list.pop(0)
              
                if not node._childern:
                    
                    second.root.parent=node
                    node._childern.append(second.root)
                    return
                elif  type(second.root.data)==type(node._childern[0].data):
                    index=-1
                    for i in node._childern:
                        index+=1
                        if second.root.data<=i.data:
                            node._childern.append(None)
                            x=len(node._childern)-index
                            for n in range(1,x):
                                node._childern[-n]=node._childern[(-n)-1]
                            node._childern[index]=second.root
                            return
                    node._childern.append(second.root)
                    return

                else:
                    for i in node._childern:
                        the_list.append(i)
                            

            def helper(start_list,start_value,second):
                
                while start_list:
                      concerned=start_list.pop(0)
                      if concerned.data==start_value:
                        #starting the inseration stage of algorithm stop the iterating over the nodes in different levels 
                         new_copy=copy.deepcopy(second)
                         insert([concerned],new_copy)
                         return new_self.the_tree(new_self.root)
                         
                      else:
                        for i in concerned._childern:
                            start_list.append(i)
            new_self=copy.deepcopy(self)
            helper([new_self.root],1,second)
            return new_self.the_tree(new_self.root)
        

        elif mood=="level":
            
            if not (isinstance(start,int)):
                raise TypeError("the level should be numeric intger ")
            if not (0<=start<=self.height()):
                raise ValueError("the starting point you want us to start doesn't exist ")
            copyed_second=copy.deepcopy(second)
            def helper(start_list,current_level,start):
                if current_level==start:

                    while start_list:
                        concerned=start_list.pop(0)
                        if not concerned._childern:
                            copyed_second.root.parent=concerned
                            concerned._childern.append(copyed_second.root)
                            return
                        if type(copyed_second.root.data)==type(concerned._childern[0]):
                           index=-1
                           for i in concerned._childern:
                              index+=1
                              if i.data<=copyed_second.root.data:
                                
                                concerned._childern.append(None)
                                x=len(concerned._childern)-index
            
                                for n in range(1,x):  
                
                                    concerned._childern[-n]=concerned._childern[(-n)-1]
                                concerned._childern[index]=copyed_second.root
                                return
                           concerned._childern.append(copyed_second.root)
                           return
                        else:
                            for i in concerned._childern:
                                start_list.append(i)
                                         
                    
                else:
                    new_start=[]
                    while start_list:
                        concerned=start_list.pop(0)
                        if  concerned._childern:
                            for i in concerned._childern:
                                new_start.append(i)

                    helper(new_start,current_level+1,start)
            new_self=copy.deepcopy(self)
            helper([new_self.root],0,start)
            return new_self.the_tree(new_self.root)
         
        else:
            raise ValueError("the type of mergeing here either to search of start by it's value or by it's level")
        
    def merge_with_change(self,second,mood,start):
        '''
        objectives:merging two general tree objects with making changes on the the basic (calling) object... the merging will start specific point
        on the tree either by level or the first existance of a value 
        inputs:second is general tree object we need to merge version to the basic(calling )object general tree 
        mood : we have two options /states to start the merging (level,value)
        start: either intger or value according the mood ( start&mood should be consistancy )
        output : the self (basic) general tree with the new changes 
        '''
        if not (isinstance(second,(general_tree))):
            raise TypeError

        # the case of either or both lists are empty 
        if (not self.root) and (not second.root):
            raise ValueError("both of them is empty ...no meaning of merging ")
        if (not self.root) and (second.root):
            new_copy=copy.deepcopy(second)
            new_copy.root.parent=None
            self.root=new_copy.root
            return self.the_tree(self.root)
        if (self.root) and (not second.root):
            return self.the_tree(self.root)

        if mood=="value":
            def insert(the_list,second):
              while the_list:
                node=the_list.pop(0)
              
                if not node._childern:
                    
                    second.root.parent=node
                    node._childern.append(second.root)
                    return
                elif  type(second.root.data)==type(node._childern[0].data):
                    second.root.parent=node
                    index=-1
                    for i in node._childern:
                        index+=1
                        if second.root.data<=i.data:
                            node._childern.append(None)
                            x=len(node._childern)-index
                            for n in range(1,x):
                                node._childern[-n]=node._childern[(-n)-1]
                            node._childern[index]=second.root
                            return
                    node._childern.append(second.root)
                    return

                else:
                    for i in node._childern:
                        the_list.append(i)
                            

            def helper(start_list,start_value,second):
                
                while start_list:
                      concerned=start_list.pop(0)
                      if concerned.data==start_value:
                        #starting the inseration stage of algorithm stop the iterating over the nodes in different levels 
                         new_copy=copy.deepcopy(second)
                         insert([concerned],new_copy)
                         return self 
                         
                      else:
                        for i in concerned._childern:
                            start_list.append(i)

            helper([self.root],start,second)
            return self.the_tree(self.root)
        

        elif mood=="level":
            
            if not (isinstance(start,int)):
                raise TypeError("the level should be numeric intger ")
            if not (0<=start<=self.height()):
                raise ValueError("the starting point you want us to start doesn't exist ")
            copyed_second=copy.deepcopy(second)
            def helper(start_list,current_level,start):
                if current_level==start:

                    while start_list:
                        concerned=start_list.pop(0)
                        if not concerned._childern:
                            copyed_second.root.parent=concerned
                            concerned._childern.append(copyed_second.root)
                            return
                        if type(copyed_second.root.data)==type(concerned._childern[0]):
                           index=-1
                           for i in concerned._childern:
                              index+=1
                              if i.data<=copyed_second.root.data:
                                
                                concerned._childern.append(None)
                                x=len(concerned._childern)-index
            
                                for n in range(1,x):  
                
                                    concerned._childern[-n]=concerned._childern[(-n)-1]
                                concerned._childern[index]=copyed_second.root
                                return
                           concerned._childern.append(copyed_second.root)
                           return
                        else:
                            for i in concerned._childern:
                                start_list.append(i)
                                         
                    
                else:
                    new_start=[]
                    while start_list:
                        concerned=start_list.pop(0)
                        if  concerned._childern:
                            for i in concerned._childern:
                                new_start.append(i)

                    helper(new_start,current_level+1,start)

            helper([self.root],0,start)
            return self.the_tree(self.root)
         
        else:
            raise ValueError("the type of mergeing here either to search of start by it's value or by it's level")

    def extract_subtree_with_change_by_position(self,position):
        '''
        objectives:extracting/deleting a subtree of the concerned tree return it as the new general tree object 
        input:position object as reference to the starting point the concerned general tree we want to extract part of it 
        output:a new tree 
        '''
        if not(isinstance(position,general_tree._position)) or  not (position.container==self):
            raise TypeError
        if not self.root :
            raise ValueError
        
        if not self.belonging(position.node):
            raise ValueError
        self.delete_position(position)
        new_tree=general_tree()
        new_tree._root=position.node

        return new_tree
        

    def extract_subtree_with_change_by_value(self,value):
        '''
        objectives:extracting/deleting a subtree of the concerned tree return it as the new general tree object 
        input:value as reference to the starting point the concerned general tree we want to extract part of it 
        output:a new tree 
        '''
        if not (self.root):
            raise ValueError("the list is empty no value to extract ")
        if self.root.data==value:
            new_copy=copy.deepcopy(self.root)
            self.root=None
            new_tree=general_tree()
            new_tree.root=new_copy
            return new_tree
        
        the_list=[self.root]
        while the_list:
            concerned=the_list.pop(0)
            if concerned.data==value:
                parent_concerned=concerned.parent
                ind=-1
                for i in parent_concerned._childern:
                    ind+=1
                    if i is concerned:
                        
                        for x in range(ind,len(parent_concerned._childern)-1):
                            parent_concerned._childern[x]=parent_concerned._childern[x+1]
                        parent_concerned._childern.pop()

                concerned.parent=None
                new_tree=general_tree(concerned)
               
               
                return new_tree
            
            for i in concerned._childern:
                the_list.append(i)

        raise ValueError("the value you want to start the extracting from it doesn't exist ")

    def extract_subtree_without_change_by_position(self,position):
        '''
        objectives:extracting a copy of a subtree of the concerned tree return it as the new general tree object without any change of the basic tree
        input:position object as reference to the starting point the concerned general tree we want to etracting /copying part of it 
        output:a new tree 
        '''
         
        if not(isinstance(position,general_tree._position)) or not(position.container==self):
            raise TypeError
        if not self.root :
            raise ValueError
        
        if not self.belonging(position.node):
            raise ValueError
        new_copy=copy.deepcopy(position.node)
        new_copy.parent=None
        new_tree=general_tree()
        new_tree._root=new_copy

        return new_tree

    def extract_subtree_without_change_by_value(self,value):
        '''
        objectives: get a subtree of the concerned tree return it as the new general tree object  without any change in the basic tree 
        input:value as reference to the starting point the concerned general tree we want to copy part of it 
        output:a new tree 
        '''
        if not (self.root):
            raise ValueError("the list is empty no value to extract ")
        if self.root.data==value:
            new_copy=copy.deepcopy(self.root)
      
            new_tree=general_tree()
            new_tree.root=new_copy
            return new_tree
        
        the_list=[self.root]
        while the_list:
            concerned=the_list.pop(0)
            if concerned.data==value:
                new_copy=copy.deepcopy(concerned)
                new_copy.parent=None
                new_tree=general_tree()
                new_tree.root=new_copy

                return new_tree
            
            for i in concerned._childern:
                the_list.append(i)

        raise ValueError("the value you want to start the extracting from it doesn't exist " )


    def is_equivilant(self,second):
        '''
        objectives:determining the equivilance between two general tree objects
        inputs:second parameter is general tree object
        output:True/False 
        '''
        if not isinstance(second,general_tree):
            return TypeError
        if self.root and not(second.root):
            return False
        if not(self.root) and second.root:
            return False
        
        the_first=[self.root]
        the_second=[second.root]

        while the_first and the_second:
            f=the_first.pop(0)
            s=the_second.pop(0)
            if f.data==s.data:
                if len(f._childern)==len(s._childern):

                   for i in f._childern:
                       the_first.append(i)
                
                   for i in s._childern:
                       the_second.append(i)
                else:
                    return False
            else:
                return False 
            
        if not the_first and the_second:
            return False
        if the_first and not the_second:
            return False
        return True

    def is_superset(self,second):
        '''
        objectives:determining the superamcy of the basic general tree object over the second general tree object
        inputs:second parameter is general tree object
        output:True/False 
        note :we here mean by superset, the proper superset mathemitical concept not explicit superset because simply the problem of applying that meaning in the practical field where two identical trees one of them have superamcy ?!! which is not acceptable

        '''
        if not isinstance(second,general_tree):
            raise TypeError

        if not self.root:
            return None
        if not second.root:
            return None
        the_main_list=[self.root]
        while the_main_list:
            start_comparsion=the_main_list.pop(0)
            if start_comparsion.data==second.root.data:
                ### here we the process of determine the spermacy of the self tree of the second from that point on self tree
                ### it return true if the mission done or nothing to continue to search for another point could achieve the required 
                the_first=[start_comparsion]
                the_second=[second.root]
                flag=True

                while the_first and the_second:
                    f=the_first.pop(0)
                    s=the_second.pop(0)
                    if f.data==s.data:
                        if len(f._childern)==len(s._childern):

                           for i in f._childern:
                              the_first.append(i)
                
                           for i in s._childern:
                              the_second.append(i)
                        else:
                            for i in f._childern:
                              the_main_list.append(i)
                            flag=False
                            break
                            
                    else:
                       for i in f._childern:
                            the_main_list.append(i)
                       flag=False
                       break 
                if not the_first and not the_second and flag and start_comparsion is not self.root:
                    return True
            
                elif not the_first and the_second and start_comparsion is self.root:
                     return False
                elif not the_first and the_second and start_comparsion is not self.root:
                     pass
                elif  the_first and not the_second and flag:
                      return True
                elif  the_first and the_second :
                    pass
            else:
                for i in start_comparsion._childern:
                    the_main_list.append(i)

        return False
    def is_subset(self,another):
        '''
        objectives:determining if the basic general tree object is a subsetof  the second general tree object or not 
        inputs:second parameter is general tree object
        output:True/False 
        note :we here mean by subset, the proper subset mathemitical concept 
        '''
        if not isinstance(another,general_tree):
            raise TypeError

        if not self.root:
            return None
        if not another.root:
            return None
        the_main_list=[another.root]
        while the_main_list:
            start_comparsion=the_main_list.pop(0)
            if start_comparsion.data==self.root.data:
                ### here we the process of determine the spermacy of the self tree of the second from that point on self tree
                ### it return true if the mission done or nothing to continue to search for another point could achieve the required 
                the_first=[start_comparsion]
                the_second=[self.root]
                flag=True

                while the_first and the_second:
                    f=the_first.pop(0)
                    s=the_second.pop(0)
                    if f.data==s.data:
                        if len(f._childern)==len(s._childern):

                           for i in f._childern:
                              the_first.append(i)
                
                           for i in s._childern:
                              the_second.append(i)
                        else:
                            for i in f._childern:
                              the_main_list.append(i)
                            flag=False
                            break
                            
                    else:
                       for i in f._childern:
                            the_main_list.append(i)
                       flag=False
                       break 
                if not the_first and not the_second and flag and start_comparsion is not another.root:
                    return True
            
                elif not the_first and the_second and start_comparsion is another.root:
                     return False
                elif not the_first and the_second and start_comparsion is not another.root:
                     pass
                elif  the_first and not the_second and flag:
                      return True
                elif  the_first and the_second :
                    pass
            else:
                for i in start_comparsion._childern:
                    the_main_list.append(i)

        return False


t=general_tree()
print(t.root)
t.root=general_tree.tree_node(3.14)
first=t.tree_node(100)
print(first._childern,first.size_childern())
first.add_child(0)
print(first.parent,first,first._childern[0].parent,first._childern[0])

print(first._childern,first.size_childern(),"\n")
first.add_child(-10)
print(first._childern,first.size_childern(),"\n")
first.add_child(50)
print(first)

first.add_child(1000)
print(first._childern,first.size_childern(),"\n")

import random

for i in range(3):
    l=random.randint(-500,500)
    first.add_child(l)
    t.add_to_root_childern(l)
    print(first._childern,first.size_childern(),"\n")
    print(t.root._childern,t.root.size_childern(),"\n")

print(t.root.parent,t.root,t.root._childern,t.root._childern[0].parent)
print(first._childern,first.size_childern(),"\n")
first.add_child(28)
print(first._childern,first.size_childern(),"\n")
first.add_child(1000)
print(first._childern,first.size_childern(),"\n")
first.add_child(-10000)
print(first._childern,first.size_childern(),"\n")

first.add_child(24)
print(first._childern,first.size_childern(),"\n")
for i in range(2,50,2):
    first.add_child(i)

print(first.delete_child_value(1000))
print(first.delete_child_value(-10000))
print(first._childern)

print(first._childern)
print(t.root._childern)
for i in range(1,2):
    k=random.randint(-100000,15000000)
    t.add_to_root_childern(k)
print(t.root._childern)
l=general_tree._position(t.root._childern[1],t)
print(l)
print(l.node.parent)
print(t.view_sibilings_node_by_position(l))
print(t.delete_root_son_index(t.root,7))
print(t.root._childern)

print(t.delete_root_son_value(t.root,31))
print(t.root._childern)
ps=general_tree._position(t.root._childern[0],t)
print(t.delete_position(ps))
print(t.root._childern)
print(t.belonging(t.root))


#############################3
g=general_tree()
g.add_to_root_childern(500)

print(g.root,g.root.parent,g.root._childern)
print(t.belonging(g.root))


print(g.root,t.root)
print(type(g.root),type(t.root))
print(type(g.root)==type(t.root))

x=[1,2,3,4]
y=[]+x

print("\n")
print(t.root._childern)
for child in t.root._childern:
  for _ in range(2):
    l=random.randint(1,1000)
    child.add_child(l)
  
    for grand_child in child._childern:
      for _ in range(2):
        l=random.randint(1,1000)
        grand_child.add_child(l)
 

(t.the_tree(t.root))
print("\n")

gl=general_tree(general_tree.tree_node(1))
(gl.the_tree(gl.root))
print(gl.root.parent)

for first in range(0,3):
    l=random.randint(1,10)
    gl.add_to_root_childern(l)

for i in gl.root._childern:
  for _ in range(0,3):
    l=random.randint(1,10)
    i.add_child(l)
  for x in i._childern :
    for _ in range(0,3):
      l=random.randint(1,10)
      x.add_child(l)
    for c in x._childern:
        for _ in range(0,3):
           l=random.randint(1,10)
           c.add_child(l)

(gl.the_tree(gl.root))

print(gl.root.parent,gl.root,gl.root._childern[0],gl.root._childern[0].parent)
print(gl.height())
print(gl.level(gl.root))
print(gl.level(gl.root._childern[0]._childern[0]._childern[0]._childern[0]))
print((gl.root._childern[0]._childern[0]._childern[0]._childern[0]))
x=gl.root._childern[0]
print(x.parent is gl.root)
print(not gl.root.parent)
print(gl.root.parent)
print(gl.root._childern[0]._childern[0]._childern[0]._childern[0],gl.level(gl.root._childern[0]._childern[0]._childern[0]._childern[0]))
print(gl.level(t.root._childern[0]))
print(gl.breadth_first_search(gl.root))
print(gl.depth_first_search_pre_order(gl.root))




print("yess")
g=general_tree(general_tree.tree_node(1))
(g.the_tree(g.root))
print(g.size())

for first in range(0,3):
    l=random.randint(1,10)
    g.add_to_root_childern(l)

print(g.root.parent,g.root,g.root._childern[0],g.root._childern[0].parent)
for i in g.root._childern:
  for _ in range(0,3):
    l=random.randint(1,10)
    i.add_child(l)
  for x in i._childern :
    for _ in range(0,3):
      l=random.randint(1,10)
      x.add_child(l)

g.the_tree(g.root)
print(g.breadth_first_search(g.root))
print(g.depth_first_search_pre_order(g.root))
print(g.depth_first_search_post_order(g.root))



print(g.search_by_value(100))
x=g.search_by_value(1)

if x:
    print(x.node,x.container,x.node.parent)

x=g.search_by_parent_predicate_zone(0,100)
print(x)
for i in x:
    (i,type(i),i.node,i.container,i.node.data,i.node.parent)

print("\n")
print(g.search_by_childern_predicate_statistics(1,"sum"))
print(g.search_by_childern_predicate_statistics(1,"mean"))
print(g.search_by_childern_predicate_statistics(1,"median"))
print("\n")
print(g.search_by_childern_predicate_statistics(5,"mood"))
print(g.search_by_childern_predicate_statistics(1,"mood"))





gl.the_tree(gl.root)
g.the_tree(g.root)


(g.merge_with_change(gl,"value",1))


po=g._position(g.root._childern[0],g)
print(g.root._childern[0],g.root._childern[0].parent)
print(po,po.node.parent)




x=g.extract_subtree_with_change_by_position(po)
x.the_tree(x.root)

g.the_tree(g.root)
yo=g._position(g.root._childern[0],g)

y=g.extract_subtree_without_change_by_position(yo)
y.the_tree(y.root)
g.the_tree(g.root)

m=g.extract_subtree_without_change_by_value(3)
m.the_tree(m.root)
print("sfsdfsfsd")
g.the_tree(g.root)
gg=copy.deepcopy(g)
gg.the_tree(gg.root)
print(g.is_equivilant(m),g.is_superset(m))
print(g.is_equivilant(m),g.is_subset(m))
print(m.is_equivilant(g),m.is_subset(g))
print(g.height(),g.height2(g.root))
gg.the_tree(gg.root)
print(gg.root._childern[0]._childern[0]._childern[0],gg.height2(gg.root._childern[0]._childern[0]._childern[0]))