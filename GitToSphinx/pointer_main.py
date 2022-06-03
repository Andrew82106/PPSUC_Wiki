import dirTools


class Pointer(object):
    def __init__(self, Route):  # 此处的Route一定要是目录根的绝对地址
        self.route = Route
        self.root = Route
        self.webRoute = 'https://github.com/ChrisWhite1024/PPSUC-NSLE/tree/22-01-02/'

    def jumpTo(self, subRoute: str):
        x = dirTools.ToolBags.ls(self.route)
        if subRoute not in x:
            print("INFO::路径{}下没有{}文件,拒绝跳转".format(self.route, subRoute))
        else:
            self.route += ('/' + subRoute)
            self.webRoute += ('/' + subRoute)
