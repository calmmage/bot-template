# run the app
from bot_base.data_model.mongo_utils import connect_to_db
from bot_base.utils.logging_utils import setup_logger
from bot_template.core.app import TemplateApp

if __name__ == "__main__":
    # cli kwarg data_dir:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=str, default="app_data")
    # connect to db
    connect_to_db()

    # setup logger
    setup_logger()
    args = parser.parse_args()
    app = TemplateApp(data_dir=args.data_dir)
    app.run()
