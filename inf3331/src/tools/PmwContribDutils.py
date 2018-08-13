from PmwContribD.TreeExplorer import TreeExplorer
from PmwContribD.NavigableTree import NavigableFileTree, create_from_directory
from PmwContribD import TreeNavigator
from PmwContribD.TreeExplorer import TreeExplorer
import os, sys, string, re, Pmw, Tkinter

class NavigableDirTree(NavigableFileTree):
    """class for a directory tree with directory items only"""

    def children(self):
        child_names = []
        allfiles = os.listdir(self.full_path)
        for file in allfiles:
            f = os.path.join(self.full_path,file)
            if os.path.isdir(f):
                child_names.append(file)
        children = map(lambda x, s=self: create_from_directory(
            os.path.join(s.full_path, x), parent=s,
            directory_node_type=NavigableDirTree
            ),
                       child_names)
        return list(children)

       
class DirList(TreeExplorer):
    def __init__(self, parent=None, rootdir=os.curdir, dirsonly=0, **kw):
        optiondefs = (('width', 200, Pmw.INITOPT),)
        self.defineoptions(kw,optiondefs)
        if dirsonly:
            self.data = create_from_directory(rootdir,
                        directory_node_type=NavigableDirTree)
        else:
            self.data = create_from_directory(rootdir)

        TreeExplorer.__init__(self, parent, autoexpand=1, **kw)
        # we are forced to use configure to set treedata:
        self.component('navigator').configure(treedata=self.data)
        # the font is not nice; default Tkinter.Text font...
        self.component('navigator').component('tree').component('text').configure(font="Helvetica 10 bold")
        self.selected_dir = None
        self.top_dir = os.getcwd()

    def _createInterior(self):
        """
        Modify TreeExplorer._createInterior(); drop the pane
        """
        interior = Pmw.LabeledWidget.interior(self)
        
        self.panes = self.createcomponent(
            'panes',
            (), None,
            Pmw.PanedWidget,
            (interior,),
            orient='horizontal',
            hull_height=self['height'],
            hull_width=self['width'],
            )
        self.panes.add('navigatorpane', min=self['width'], size=200)
#        self.panes.add('datapane')# , min=.1)
        
        self.navigator = self.createcomponent('navigator', (), None,
                                        TreeNavigator.TreeNavigator,
                                        (self.panes.pane('navigatorpane'),),
                                        treedata=None,
                                        command=self.select_node,
                                        entercommand=self.enter_node,
                                        leavecommand=self.leave_node,
                                        )
        self.navigator.pack(side='top',
                            expand='yes',
                            fill='y',
                            )
                            
#        self.childsite = self.createcomponent('childsite', (), None,
#                                        Frame,
#                                        (self.panes.pane('datapane'),),
#                                        )
#        self.childsite.pack(side='top',
#                            expand='yes',
#                            fill='both',
#                            )
                            
        self.panes.pack(side='top',
                        expand='yes',
                        fill='both',
                        )
        return

    def select_node(self, node):
        if node:
            self.selected_dir = string.join(map(str,node.getpath()), os.sep)
        
    def get(self):
        return self.selected_dir

if __name__ == "__main__":
    root = Tkinter.Tk()
    gui = DirList(parent=root, dirsonly=1, width=150) #height=100)#, width=100)
    gui.pack()

    def printdir():
        print gui.get()
    
    Tkinter.Button(root, text="chosen dir", command=printdir).pack()
    root.mainloop()

        
