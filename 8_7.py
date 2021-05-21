def make_album(name, tittle, songs=''):
    if songs:
        album ={name: tittle, 'Songs':songs}
    else:
        album ={name:tittle}
    return album

album1 = make_album('2020 Tour', 'Shakira')
album2 = make_album('California Girls', 'Katy Perry')
album3 = make_album('Hope', 'XXXTentacion')
album4 = make_album('Views', 'Drake', '24')

print(album1)
print(album2)
print(album3)
print(album4)