import hydra


@hydra.main(config_path='config.yaml', strict=False)
def my_app(cfg):
    driver = cfg.db.driver
    user = cfg.db.user
    password = cfg.db.password
    cfg.db.port = 3306

    print(cfg.pretty())

if __name__ == "__main__":
    my_app()