from __future__ import print_function
from argparse import ArgumentParser

from entity import generate_entity

flags = ['entity', 'model', 'controller', 'repository', 'service', 'properties', 'types']

def get_cmd_line_args():
    parser = ArgumentParser()
    parser.add_argument('-e', '--entity', dest='entity', help='Enter the name of desired entity', type=str)
    parser.add_argument('-m', '--model', dest='model', help='Enter the name of desired model', type=str)
    parser.add_argument('-c', '--controller', dest='controller', help='Enter the name of desired controller', type=str)
    parser.add_argument('-r', '--repository', dest='repository', help='Enter the name of desired repository', type=str)
    parser.add_argument('-s', '--service', dest='service', help='Enter the name of desired service', type=str)
    parser.add_argument('-p', '--properties', nargs='*', dest='properties', help='Enter the name of desired properties', type=str)
    parser.add_argument('-t', '--types', nargs='*', dest='types', help='Enter the types of desired properties')
    args = parser.parse_args()
    return arguments_to_dict(args)


def arguments_to_dict(args):
    temp = dict()
    for flag in flags:
        temp[flag] = getattr(args, flag)
    return temp


def process_data(data):
    if not validate_class(data):
        return None
    elif validate_properties(data):
        return None
    elif data['entity'] is not None:
        return create_entity(data)
    elif data['model'] is not None:
        return create_model(data)
    elif data['controller'] is not None:
        return create_controller(data)
    elif data['repository'] is not None:
        return create_repository(data)
    elif data['service'] is not None:
        return create_service(data)


def validate_class(dict):
    count = 0
    if dict['entity'] is not None:
        count += 1
    if dict['model'] is not None:
        count += 1
    if dict['controller'] is not None:
        count += 1
    if dict['repository'] is not None:
        count += 1
    if dict['service'] is not None:
        count += 1

    if count is 1:
        return True
    print('Must enter one class to be created')
    return False


def validate_properties(dict):
    if dict['properties'] is None or dict['types'] is None:
        print('Properties or Types field is empty')
        return False
    elif len(data['properties']) != len(data['types']):
        print('Number of Properties do not match number of Types')
        return False
    return True


def create_entity(data):
    filename = data['entity'] + '.java'
    entity_file = open(filename, 'w+')
    entity_file.write("Testing")
    entity_file.close()
    return True


def create_model(data):
    return True

def create_controller(data):
    return True

def create_repository(data):
    return True

def create_service(data):
    return True


if __name__ == '__main__':
    data = get_cmd_line_args()
    process_data(data)
