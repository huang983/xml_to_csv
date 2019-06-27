import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for big_child in root:
            if (big_child.tag == 'image'):
                attributes = big_child.attrib # A dictionary of image's  attributes
                #print(attributes['name'])
                #print(attributes['width'])
                #print(attributes['height'])
                for child in big_child:
                 #   print(child.attrib)
                    child_attrib = child.attrib
                    value = (attributes['name'],
                             int(attributes['width']),
                             int(attributes['height']),
                             child_attrib['label'],
                             int(float(child_attrib['xtl'])),
                             int(float(child_attrib['ytl'])),
                             int(float(child_attrib['xbr'])),
                             int(float(child_attrib['ybr']))
                             )
                    xml_list.append(value)
                  #  print(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']

    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():

    folder = 'train'
    image_path = os.path.join(os.getcwd(), ('images/' + folder))
    xml_df = xml_to_csv(image_path)
    xml_df.to_csv(('images/' + folder + '_labels.csv'), index=None)
    print('Successfully converted xml to csv.')


main()
