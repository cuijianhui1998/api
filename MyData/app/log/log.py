
if __name__ == '__main__':

    import os,csv
    path = os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.dirname("__file__"),
                                                                     os.path.pardir)),os.path.pardir))
    data = [['ip地址','访问方法','访问路径','参数','到达时间']]

    with open('{}/log.csv'.format(path),'w+',encoding='utf-8-sig') as f:
        w = csv.writer(f)
        w.writerows(data)
