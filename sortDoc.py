import os


def get_file_list(file_path):
    dir_list = os.listdir(file_path)
    if not dir_list:
        return
    else:
        # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
        # os.path.getmtime() 函数是获取文件最后修改时间
        # os.path.getctime() 函数是获取文件最后创建时间
        dir_list = sorted(dir_list, key=lambda x: os.path.getctime(os.path.join(file_path, x)))
        print(dir_list)
        return dir_list


get_file_list('/work/share/swim_bug/108331/IhuLog20200116153638/LOG_FILES/data/logger')