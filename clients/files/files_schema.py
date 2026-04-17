from pydantic import BaseModel, HttpUrl

class FileSchema(BaseModel):
    """ОТписание структуры файла"""
    id: str
    url: HttpUrl
    filename: str
    directory: str

class CreateFileRequestSchema(BaseModel):
    """Описане запроса создания файла"""
    filename: str
    directory: str
    upload_file: str

class CreateFileResponseSchema(BaseModel):
    """Описание структуры ответа создания файла"""
    file: FileSchema