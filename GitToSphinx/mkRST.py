import dirTools

"""
排版格式：
.. PPUSC_Wiki documentation master file, created by
   sphinx-quickstart on Thu Jun  2 09:32:21 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PPUSC_Wiki's documentation!
======================================

.. toctree::
   :maxdepth: 4
   :caption: 目录:

   about
   -->markdown文档
   dir1/index
   dir2/index
   -->文件夹


* 链接文本1 http://www.baidu.com/
* 链接文本2 http://www.baidu.com/
* 链接文本3 http://www.baidu.com/
-->非markdown文档
"""


class RST_MAKER(object):
    def __init__(self, Route: str):
        self.Route = Route

    def writeRST(self, markdown_list: list, folder_list: list, none_folder_dict: dict, headers: str):
        # markdown_list:markdown文档的名字，folder_list文件夹的名字，none_folder_dict：非文件夹文档的名字和链接
        f = open(self.Route + '/index.rst', 'w', encoding='utf-8')
        f.write("{}\n======================================\n\n".format(headers))
        f.write(".. toctree::\n   :maxdepth: 4\n   :caption: PPSUC_Wiki:\n\n")
        for i in markdown_list:  # 输出markdown文件
            f.write("   {}\n".format(i))
        for i in folder_list:  # 输出文件夹
            f.write("   {}/index\n".format(i))
        f.write("\n\n")
        #  rst链接格式：`Link text <http://www.baidu.com/>`_
        for i in none_folder_dict:  # 输出链接
            f.write("* `{} [gitHub Link] <{}>`_\n".format(i, none_folder_dict[i]))
        f.close()


if __name__ == '__main__':
    a = RST_MAKER("/Users/andrewlee/Desktop/PPSUC_WIKI_WEB/source/dir1")
    a.writeRST(['markdown_list0'], ['folder1'], {'non markdown': "www.baidu.com", 'non1 markdown': "www.baidu.com"})