def parse(response_type, response):
    def json(_response):
        return "Parsing json: {}".format(_response)

    def xml(_response):
        return "Parsing xml: {}".format(_response)

    if response_type == 'json':
        return json(response)
    else:
        return xml(response)


if __name__ == '__main__':
    resp = '{"name": "Emily", "age": 35}'
    parsed = parse('json', resp)
    print(parsed)
