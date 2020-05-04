import sys

# import time
from subprocess import getstatusoutput
from multiprocessing import Pool
from typing import Tuple, List, Any, Callable
from logging import debug, info

from random import shuffle

# from functools import reduce


# run_function	la fonction a executer
# cmds_exec	list des args de la fonction
# nbProcessus	Nombre de processus a utiliser
# stdout	"" -> sortie stdout | "data.log" fichier de sortie
# ret		False -> recupere pas les sorties de la fonction run_worker
def run_parallel(
    run_function: Callable[..., str],
    cmds_exec: List[Any],
    number_of_processes: int = 1,
    stdout: str = '',
    ret: bool = False,
) -> List[Any]:
    # def secondsToStr(t: float) -> str:
    #     return "%d:%02d:%02d.%03d" % reduce(
    #         lambda ll, b: divmod(ll[0], b) + ll[1:], [(t * 1000,), 1000, 60, 60]
    #     )

    if stdout != '':
        sys.stdout = open(stdout, 'a')

    # startTime = time.time()
    ret_info = []
    pool = Pool(processes=number_of_processes)

    shuffle(cmds_exec)

    debug('[+] Nomber of execution ' + str(len(cmds_exec)))
    debug('[+] ' + str(cmds_exec[0]))

    try:
        if ret:
            jobs = pool.map_async(run_function, cmds_exec)
            pool.close()
            # pool.join()
            ret_info = jobs.get()
        else:
            pool.map_async(run_function, cmds_exec)
            pool.close()
            # pool.join()
    except KeyboardInterrupt:
        info('parent received control-c')
        pool.terminate()

    # debug('[+] Execution time ' + secondsToStr(time.time() - startTime))
    if stdout != '':
        if ret_info != []:
            print(ret_info)
        sys.stdout = sys.__stdout__
    return ret_info


# function run_worker execute des prgrammes exterieurs avec des
# parametres command_line
def run_worker(command_line: str) -> Tuple[int, str]:
    try:
        return getstatusoutput(command_line)
    except KeyboardInterrupt:
        return (0, 'KeyboardException')
