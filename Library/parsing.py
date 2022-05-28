from listbook import listbooks


class parsing:
    def parse(obj):
        array = []
        id = 1
        if type(obj) == dict:
            id = obj['num_ID']
            if 'Books' in obj:
                for x in obj['Books']:
                    array.append(listbooks(x['name'],x['author'],x['year'],x['number'],x['id']))
        pars = id, array
        return pars