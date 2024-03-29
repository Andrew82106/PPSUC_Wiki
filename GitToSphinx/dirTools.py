import os
import shutil


class ToolBags:
    @staticmethod
    def removedir(path: str):  # 删除文件夹及其子文件夹
        shutil.rmtree(path)

    @staticmethod
    def addRst(Path: str, FileName: str):  # 新建一个rst文件
        isExists = os.path.exists(Path)
        if not isExists:
            File = open('{}/{}'.format(Path, FileName), 'w', encoding='utf-8')
            print("INFO::" + Path + ' 创建{}成功'.format(Path+FileName))
            return File
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print("INFO::" + Path + ' {}文件已存在'.format(Path+FileName))
            return False

    @staticmethod
    def addFolder(path: str):  # 新建一个文件夹
        isExists = os.path.exists(path)
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            print("INFO::" + path + ' 创建{}成功'.format(path))
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print("INFO::" + path + ' {}目录已存在'.format(path))
            return False

    @staticmethod
    def ls(path: str):  # 获得文件夹下的子文件和文件夹的名字的列表
        x = os.listdir(path)
        return x

    @staticmethod
    def is_dir(Route):
        return os.path.isdir(Route)

    @staticmethod
    def copyfile(srcfile, dstpath):  # 复制函数 srcfile源文件(必须是文件) dstpath目标目录
        # srcfile 需要复制、移动的文件
        # dstpath 目的地址
        if not (os.path.isdir(srcfile) or os.path.isfile(srcfile)):
            print("%s not exist!" % (srcfile))
        else:
            fpath, fname = os.path.split(srcfile)  # 分离文件名和路径
            if not os.path.exists(dstpath):
                os.makedirs(dstpath)  # 创建路径
            shutil.copy(srcfile, dstpath + "/" + fname)  # 复制文件
            print("copy %s -> %s" % (srcfile, dstpath + "/" + fname)) 


if __name__ == '__main__':
    a = ToolBags
    # a.removedir("/Users/andrewlee/Desktop/PPSUC_WIKI_WEB/GitToSphinx/MakeFile")
    # print(a.ls("/Users/andrewlee/Desktop/PPSUC_WIKI_WEB/GitToSphinx"))
    # print(a.is_dir("/Users/andrewlee/Desktop/PPSUC_WIKI_WEB/GitToSphinx/mkRST.py"))
    a.copyfile("/Users/andrewlee/Desktop/PPSUC_WIKI_WEB/.gitignore","/Users/andrewlee/Desktop/PPSUC_WIKI_WEB/GitToSphinx/MakeFile")