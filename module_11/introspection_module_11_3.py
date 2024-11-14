def introspection_info(obj):
    info = {}
    info['type'] = str(type(obj)).split('\'')[1]
    info['methods'] = dir(obj)
    info['module'] = __name__
    return info


number_info = introspection_info(42)
print(number_info)
