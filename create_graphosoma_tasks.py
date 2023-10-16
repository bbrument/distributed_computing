#!/usr/bin/env python3

import itertools

def filename(comb_list):
    return '_'.join(map(str, comb_list)) + '_all.mat'

if __name__ == '__main__':
    
    categories = ["SIM_Light3-60-Ambiant", "SIM_Light3-90-Ambiant", "SIM_Light10-Ambiant"]
    subcategories = ["SIM_SDM"]

    modes = ["train_RnB_relu", "train_RnB_no_relu"]
    
    with open("scripts/tasks_list.sh", 'w') as f:
        for category in categories:
            for subcategory in subcategories:
                    for mode in modes:
                        if mode == "train_RnB_relu":
                            command = 'bash client_setup.sh "python exp_runner.py --mode {} \
                                --conf ./confs/wmask_rnb_relu_graphosoma.conf \
                                --case {}/{}"'.format(mode, category, subcategory)
                        elif mode == "train_RnB_no_relu":
                            command = 'bash client_setup.sh "python exp_runner.py --mode {} \
                                --conf ./confs/wmask_rnb_norelu_graphosoma.conf \
                                --case {}/{}"'.format(mode, category, subcategory)
                        f.write(command + '\n')
    
    with open("scripts/results_paths.txt", 'w') as f:
        for category in categories:
            for subcategory in subcategories:
                    for mode in modes:
                        if mode == "train_RnB_relu":
                            results_file = './exp/graphosoma_SIM_Ambiant_16bits/{}/{}/wmask_rnb_relu/meshes/00300000.ply'.format(category, subcategory)
                        elif mode == "train_RnB_no_relu":
                            results_file = './exp/graphosoma_SIM_Ambiant_16bits/{}/{}/wmask_rnb_norelu/meshes/00300000.ply'.format(category, subcategory)
                        f.write(results_file + '\n')
