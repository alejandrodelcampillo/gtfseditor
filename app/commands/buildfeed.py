import os
from flask import current_app
from flask.ext.script import Command, Option
from flask.ext.script.commands import InvalidCommand
from celery.utils.log import get_task_logger

from app import db

logger = get_task_logger(__name__)


class BuildFeed(Command):
    """Builds a feed"""

    def get_options(self):
        return [
            Option('-v', '--validate', dest='validate', action="store_true", default=False),
            Option('-e', '--extract', dest='extract', action="store_true", default=False),
            Option('-u', '--upload', dest='upload', action="store_true", default=False)
        ]

    def run(self, validate=False, extract=False, upload=False):
        logger.info("build feed task started")

        from app.services.feed import Feed

        TMP_FOLDER = current_app.config['TMP_FOLDER']

        if not os.path.isdir(TMP_FOLDER):
            os.makedirs(TMP_FOLDER)

        feed = Feed(db=db.session)
        feedFile = feed.build()
        feed.saveTo(TMP_FOLDER)

        if extract:
            extractZip(TMP_FOLDER + feed.filename, TMP_FOLDER + 'extracted/')

        if validate:
            feed.validate()

        if upload:
            s3service = S3(current_app.config['AWS_S3_BUCKET_NAME'])
            s3service.config(current_app.config)
            s3service.uploadFileObj(feed.filename, feedFile)

        return 'success'
