import csv
from pprint import pprint
import time
import pstats
import cProfile

def speed_tester(func):
    """
    実行速度計測用のデコレータ
    """
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print("実行時間" + str(run_time) + "秒")
    return wrapper

def speed_tester_advance(func):
    """
    実行速度計測用のデコレータ
    """
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        # 実行処理の計測
        pr.runcall(func, *args, **kwargs)

        stats = pstats.Stats(pr)
        stats.print_stats()
    return wrapper


deleted_count = 0

@speed_tester
def main():
    dlv_candidates = {}
    with open('./data/sample.csv', 'r') as csv_file, open('./data/dlved.csv', 'r') as dlved_csv_file:
        # list検索はO(n)だがsetであればO(1)なためsetに変換している
        # setに変換するタイミングでコストがかかるが、対象setに対して一定回数以上の検索を実行する場合は圧倒的に処理が早くなる
        # 今後、複数の列を持たせたい場合はcsv読み込みのタイミングでdictにする必要がある(この時の検索はO(1)でsetと同速)
        reader = csv.reader(csv_file, skipinitialspace=True)
        dlv_candidates = set([row[0].strip() for row in reader])

        dlved_list = [line.strip() for line in dlved_csv_file.readlines()]

        unique_list = array_unique_diff(dlv_candidates, dlved_list)
        print(len(unique_list))

    with open('./data/dlv_candidates.csv', 'w') as f:
        f.write('\n'.join(unique_list))

def array_unique_diff(source, ignore):
    unique_list = []
    for row in ignore:
        if row not in source:
            unique_list.append(row)
    return unique_list


main()


#def test():
#    source = {'100000000', '100000001', '100000002', '100000003'}
#    ignore = ['100000001', '100000003', '10000004']
#    expected = ['100000001', '100000003']
#    actual = array_unique_diff(source, ignore)
#    if actual != expected:
#        print('error')
#        print(actual)
#    else:
#        print('success')
#        print(actual)
#
#test()
