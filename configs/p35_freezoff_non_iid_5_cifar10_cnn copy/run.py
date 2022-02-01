from pathlib import Path
import time
from fltk.util.generate_docker_compose import run as generate_docker
import os
if __name__ == '__main__':
    EVENT_FILE="exp_events.txt"
    name = 'p11_freezoff'
    generate_docker(name)
    base_path = f'configs/{Path(__file__).parent.name}'
    exp_list = [
        'fedavg.yaml',
        # 'offload_strict.yaml',
        # 'fednova.yaml',
        # 'fedprox.yaml',
        # 'offload.yaml',
        # 'tifl_adaptive.yaml',
        # 'tifl_basic.yaml',
        # 'dyn_terminate_swyh.yaml',
        # 'dyn_terminate.yaml',
        ]
    exp_list = [f'{base_path}/exps/{x}' for x in exp_list]
    first_prefix = '--build'
    for exp_cfg_file in exp_list:
        cmd = f'export EXP_CONFIG_FILE="{exp_cfg_file}"; docker-compose --compatibility up {first_prefix};'
        os.system(f'echo "[$(date +"%T")] Starting {exp_cfg_file}" >> {EVENT_FILE}')
        start = time.time()


        print(f'Running cmd: "{cmd}"')
        os.system(cmd)
        first_prefix = ''
        elapsed = time.time() - start
        os.system(f'echo "[$(date +"%T")] Finished with {exp_cfg_file} in {elapsed} seconds" >> {EVENT_FILE}')

    print('Done')


