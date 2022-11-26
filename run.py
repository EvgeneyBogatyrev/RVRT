import os

with open("/model/run.sh", "w") as f:
    f.write("python /model/main_test_rvrt.py --task 001_RVRT_videosr_bi_REDS_30frames --folder_lq /dataset --results /results --tile 30 64 64 --tile_overlap 2 20 20 --num_workers 2 --save_result\n")

os.system("sh /model/run.sh")
