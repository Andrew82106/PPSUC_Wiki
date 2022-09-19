import os
from re import S
import dirTools
import mkRST
header_all = "Welcome to PPSUC_Wiki!"


class Pointer(object):
    def __init__(self, workRoute, dirRoute):  # 此处的Route一定要是目录根的绝对地址
        self.dirRoute = dirRoute  # 将要转换的文件的根地址（以这个为主调动其他的指针转换）
        self.workRoute = workRoute  # 转换后的文件生成的目标地址的根地址
        self.workRoot = workRoute
        self.webRoute = 'https://github.com/Andrew82106/PPSUC-NSLES/tree/22-05-31'  # 网页地址的根地址

    def jumpTo(self, subRoute: str):  # 指针向下跳转
        x = dirTools.ToolBags.ls(self.dirRoute)
        if subRoute not in x:
            print("INFO::路径{}下没有{}文件,拒绝跳转".format(self.dirRoute, subRoute))
        else:
            self.dirRoute += ('/' + subRoute)
            self.webRoute += ('/' + subRoute)
            self.workRoute += ('/' + subRoute)

    def jumpBack(self):
        if '/' not in self.dirRoute:  # 指针向上跳转
            print("现在的文件路径为:{} 无法再返回".format(self.dirRoute))
        else:
            x = self.dirRoute.split('/')
            routeNew = ''
            for i in range(0, len(x)-1, 1):
                routeNew += x[i]
                if i < len(x)-2:
                    routeNew += '/'
            self.dirRoute = routeNew

            x = self.workRoute.split('/')
            routeNew = ''
            for i in range(0, len(x) - 1, 1):
                routeNew += x[i]
                if i < len(x) - 2:
                    routeNew += '/'
            self.workRoute = routeNew

            x = self.webRoute.split('/')
            routeNew = ''
            for i in range(0, len(x) - 1, 1):
                routeNew += x[i]
                if i < len(x) - 2:
                    routeNew += '/'
            self.webRoute = routeNew


def WorkDir(pointer: Pointer):  # 生成当前pointer指向文件夹对应的文件夹
    layer = 2
    if str(pointer.dirRoute).split('/')[-1] != 'PPSUC-NSLES':
        xx = str(pointer.dirRoute).split('/')[-1]
    else:
        xx = header_all
        layer = 1
    sonRoute = dirTools.ToolBags.ls(pointer.dirRoute)
    markdown_list = []
    folder_list = []
    none_folder_dict = {}
    for name in sonRoute:
        if name == '.git' or name == '.DS_Store' or name == '.gitattributes' or name == 'LICENSE':
            continue
        if dirTools.ToolBags.is_dir(pointer.dirRoute + '/' + name):
            folder_list.append(name)
            os.mkdir(str(pointer.workRoute + '/' + name))
            pointer.jumpTo(name)
            WorkDir(pointer)
            pointer.jumpBack()
            # dir
        elif name.split('.')[-1] == 'md':
            markdown_list.append(name[:name.index('.')])
            dirTools.ToolBags.copyfile(pointer.dirRoute + '/' + name, pointer.workRoute + '/')
            # markdown
        else:
            none_folder_dict[name] = pointer.webRoute + '/' + name
            none_folder_dict[name] = none_folder_dict[name].replace('tree', 'blob')  # 原来文件下载链接和层级的链接是不一样的。。。
            # others
    ENGINE = mkRST.RST_MAKER(pointer.workRoute)
    ENGINE.writeRST(markdown_list, folder_list, none_folder_dict, xx, layer)


def Work(workRoute, dirRoute):  # 生成指定文件夹的对应的文件夹 workRoute:资源文件夹  dirRoute:工作文件夹
    if os.path.exists(workRoute):
        dirTools.ToolBags.removedir(workRoute)
    os.mkdir(workRoute)
    WorkDir(Pointer(workRoute, dirRoute))


def copyTomake(srcRoute, MakeFileRoute):
    sonFileList=dirTools.ToolBags.ls(srcRoute)
    for i in sonFileList:
        dirTools.ToolBags.copyfile(srcRoute+"/"+i, MakeFileRoute)


def clean_source(sourcePath):
    whiteList = ['index.rst', '.DS_Store', '_templates', 'conf.py', '_static']
    sons = dirTools.ToolBags.ls(sourcePath)
    for i in sons:
        if i in whiteList:
            continue
        dirTools.ToolBags.removedir(sourcePath + "/" + i)


if __name__ == '__main__':
    path = '/Users/andrewlee/Desktop/PPSUC_WIKI_WEB/GitToSphinx/MakeFile'
    dirPath = '/Users/andrewlee/Desktop/PPSUC_Wiki/PPSUC-NSLES'
    sourcePath = '/Users/andrewlee/Desktop/PPSUC_WIKI_WEB/source'
    makeFileRoute = '//Users/andrewlee/Desktop/PPSUC_WIKI_WEB/GitToSphinx/MakeFile'
    # Work(path, dirPath)
    copyTomake(makeFileRoute, sourcePath)
    clean_source(sourcePath)
    copyTomake(makeFileRoute, sourcePath)