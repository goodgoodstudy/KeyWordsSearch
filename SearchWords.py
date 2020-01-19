'''
遍历当前文件夹内所有文件找出对应字符所在的文件，并输出该行
autor wei.yu
version 1.0 自用
'''

# 代码准备工作
# 由于需要获得文件的路径，所以要加载 os和system库
import os
import sys

# 设定关键词keyword 和 注释 使用dict结构以便动态扩展 随便加随便改
# keyword_dict = {'UiCallManager: onTelecomCallAdded = number': '新电话回调',
#                 'TelecomCallListener onStateChanged': '电话状态改变回调',
#                 'UiCallManager: onTelecomCallRemoved = number': '挂断回调'}

# keyword_dict = {'downloadContacts: bluetoothDevice': '下载联系人',
#                 'refreshDownloadStates, type:': '联系人下载状态'}

keyword_dict = {'downloadContacts: bluetoothDevice': '下载联系人',
                'refreshDownloadStates, type:': '联系人下载状态'}



# 设定一个排除的exclude_word bb
exclude_word = ''

# 设定一组指定的文件名，使用list结构以便动态扩展
file_name_list = ['.txt', 'main.log']

# 设定不参与检索的文件名，也使用list结构
exclude_file_name_list = ['packet', '.gz ', 'pcap']

# 指定一个search_path路径，把字符串留空，只初始化，如果不指定路径，默认为当前py脚本路径
default_search_path = '/work/share/swim_bug/DCY11GKUI-4587/logger'


# 准备工作完毕
# 下面创建一个my_search函数，目的是为了实现递归查找子文件夹
# 如果只需要查找当前目录层次的文件，则可以不使用函数
# 传入参数为当前路径，为了实现递归查找子文件夹
def my_search(search_path):
    # 防错机制，判断当前路径是否存在
    if os.path.exists(search_path):

        # 获得路径下所有文件文件夹的名字，并for循环遍历
        for my_filename in os.listdir(search_path):

            # 把当前路径和文件名拼接成完整绝对路径
            full_filepath = os.path.join(search_path, my_filename)

            # 判断拼接出的完整路径是文件还是文件夹
            if os.path.isfile(full_filepath):
                # 如果是文件，则对file_name_list中期望的文件名进行遍历
                for my_extend in file_name_list:
                    # 判断.txt是文件结尾
                    if my_extend in my_filename:
                        flag = True
                        isRead = False
                        # 对exclude_file_name_list中不希望的文件名进行遍历
                        for my_exclude in exclude_file_name_list:
                            # 若文件名有.bak就剔除
                            if my_exclude in my_filename:
                                flag = False

                        if flag:  # 文件名匹配已经命中
                            i = 0  # i作为文件行号

                            # 逐行读取文件，碰到特大文件就不会卡死程序
                            try:
                                for line in open(full_filepath):
                                    i = i + 1  # 每次读一行，i+1

                                    # 判断关键字该行中
                                    for key, value in keyword_dict.items():
                                        if key in line:
                                            # 满足检索条件，打印文件完整路径，行号
                                            if not isRead:
                                                print(full_filepath, 'line', i, ':')
                                                isRead = True
                                            print('###### ' + value + '###### ' + line)
                            except Exception as e:
                                pass
                            continue

            # 当前完整路径不是文件，而是文件夹
            if os.path.isdir(full_filepath):
                # 执行函数递归，继续到下一层文件夹目录查找，直到底层文件
                my_search(full_filepath)

    else:  # 防错机制，当前路径不存在，则报错
        print(search_path, 'path not exist!')


def main():
    if default_search_path == '':
        my_search(os.getcwd())
    else:
        my_search(default_search_path)


main()
