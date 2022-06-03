import os


class ToolBags:

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


if __name__ == '__main__':
    a = ToolBags
    print(a.ls("/Users/andrewlee/Desktop/PPSUC_WIKI_WEB/GitToSphinx"))