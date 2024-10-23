from yacs.config import CfgNode as CN

def get_cfg():
    cfg = CN()
    cfg.merge_from_file("config.yaml")

