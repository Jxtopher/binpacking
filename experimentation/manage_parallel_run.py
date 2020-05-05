import sys
import os
import time
from subprocess import getstatusoutput
from multiprocessing import Pool
from typing import Tuple, List, Any, Callable, Optional
from random import shuffle
from datetime import timedelta
from logging import getLogger

log = getLogger(__name__)


class ManageParallelRun:

    # run_function	the function to be performed
    # cmds_exec	list of function arguments
    # number_of_processes Number of processes to use
    # stdout	"" ->  stdout | "data.log" output file
    # ret		False -> not retrieve the outputs of the run_worker function
    @staticmethod
    def run_parallel(
        run_function: Callable[..., Any],
        cmds_exec: List[Any],
        number_of_processes: Optional[int] = None,
        stdout: str = '',
        ret: bool = False,
    ) -> Any:
        if stdout != '':
            sys.stdout = open(stdout, 'a')

        if number_of_processes is None:
            number_of_processes = os.cpu_count()

        startTime = time.time()
        ret_info = Any
        pool = Pool(processes=number_of_processes)

        shuffle(cmds_exec)

        log.debug('[+] Nomber of execution ' + str(len(cmds_exec)))
        log.debug('[+] ' + str(cmds_exec[0]))

        try:
            if ret:
                jobs = pool.map_async(run_function, cmds_exec)
                pool.close()
                ret_info = jobs.get()

            else:
                pool.map_async(run_function, cmds_exec)
                pool.close()
        except KeyboardInterrupt:
            log.info('parent received control-c')
            pool.terminate()

        log.debug('[+] Execution time ' + str(timedelta(seconds=(time.time() - startTime))))
        if stdout != '':
            if ret_info != []:
                print(ret_info)
            sys.stdout = sys.__stdout__
        return ret_info

    # function run_worker execute des prgrammes exterieurs avec des
    # parametres command_line
    @staticmethod
    def run_worker(command_line: str) -> Tuple[int, str]:
        try:
            return getstatusoutput(command_line)
        except KeyboardInterrupt:
            return (0, 'Cancelled execution')
