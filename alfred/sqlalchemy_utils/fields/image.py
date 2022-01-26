from sqlalchemy import types

from alfred.aws import S3File, S3UploadFileException


class ImageType(types.TypeDecorator):
    impl = types.Unicode(128)

    def __init__(self, upload_to):
        super(ImageType, self).__init__()

        self.upload_to = upload_to

    def process_bind_param(self, value, dialect):
        success, file_name = S3File.upload_file(value, upload_to=self.upload_to)

        if not success:
            raise S3UploadFileException("Upload do arquivo não pode ser realizado")

        return file_name

    def process_result_value(self, value, dialect):
        url = S3File.get_presigned_url(value)

        return url
