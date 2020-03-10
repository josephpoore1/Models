from hestia.crop_builder import FarmedCropBuilder
from hestia.data_client.file_writers.json_writer import JsonWriter
if __name__ == '__main__':
    writer = JsonWriter('D:\ProArch\hestia\objects')
    builder = FarmedCropBuilder()
    crop = builder.build_crop(1041)
    writer.write(crop, 'crop20')