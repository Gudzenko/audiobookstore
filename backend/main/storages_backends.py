import os
import logging
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.storage import Storage
from b2sdk.v2 import InMemoryAccountInfo, B2Api
import mimetypes


class B2Storage(Storage):
    def __init__(self, *args, **kwargs):
        logging.basicConfig(level=logging.DEBUG)

        self.info = InMemoryAccountInfo()
        self.b2_api = B2Api(self.info)
        self.application_key_id = os.environ.get('B2_APP_KEY_ID')
        self.application_key = os.environ.get('B2_APP_KEY')
        self.bucket_name = os.environ.get('B2_BUCKET_NAME')
        try:
            self.b2_api.authorize_account("production", self.application_key_id, self.application_key)
            logging.info("Authorization successful")
        except Exception as e:
            logging.error(f"Authorization failed: {e}")
            raise

        try:
            self.bucket = self.b2_api.get_bucket_by_name(self.bucket_name)
            logging.info(f"Bucket retrieval successful: {self.bucket_name}")
        except Exception as e:
            logging.error(f"Bucket retrieval failed: {e}")
            raise

        super().__init__(*args, **kwargs)

    def _open(self, name, mode='rb'):
        try:
            downloaded_file = self.bucket.download_file_by_name(name)
            with BytesIO() as byte_stream:
                downloaded_file.save(byte_stream)
                byte_stream.seek(0)
                return ContentFile(byte_stream.read())
        except Exception as e:
            logging.error(f"File open failed: {e}")
            raise

    def _save(self, name, content):
        try:
            content_type, _ = mimetypes.guess_type(name)
            self.bucket.upload_bytes(content.read(), name, content_type=content_type)
            logging.info(f"File saved successfully: {name}")
            return name
        except Exception as e:
            logging.error(f"File save failed: {e}")
            raise

    def exists(self, name):
        try:
            self.bucket.get_file_info_by_name(name)
            return True
        except:
            return False

    def url(self, name):
        try:
            token = self.bucket.get_download_authorization(name, 60 * 60)
            return f"{self.bucket.get_download_url(name)}?Authorization={token}"
        except Exception as e:
            logging.error(f"URL generation failed: {e}")
            raise

    def delete(self, name):
        try:
            file_version = self.bucket.get_file_info_by_name(name)
            self.bucket.delete_file_version(file_version.id_, file_version.file_name)
            logging.info(f"File deleted successfully: {name}")
        except Exception as e:
            logging.error(f"File deletion failed: {e}")
            raise
