from urllib.request import urlopen
import json

url = "https://raw.githubusercontent.com/pokemongo-dev-contrib/pokemongo-json-pokedex/master/output/pokemon.json"
response = urlopen(url)

final_data = []

json_data = json.loads(response.read())
for p in json_data:
    final_data.append({
        'dex': p['dex'],
        'name': p['name'],
        'height': p['height'],
        'weight': p['weight'],
        'kmBuddyDistance': p['kmBuddyDistance'],
        'maxCP': p['maxCP'],
        'cinematicMoves': [x['name'] for x in p['cinematicMoves']],
        'quickMoves': [x['name'].replace(' Fast','') for x in p['quickMoves']],
        'family': p['family']['name'],
        'stats': p['stats'],
        'types': [x['name'] for x in p['types']],
        'gender': p['encounter']['gender'] if 'gender' in p['encounter'] else '',
        'baseCaptureRate': p['encounter']['baseCaptureRate'] if 'baseCaptureRate' in p['encounter'] else '',
        'baseFleeRate': p['encounter']['baseFleeRate'] if 'baseFleeRate' in p['encounter'] else '',        
        'evolution': p['evolution'],
        'forms': [x['name'] for x in p['forms']],
    })

# print(json.dumps(final_data))

with open('pokedex.json', 'w') as f:
    json.dump(final_data, f, separators=(',', ':'))

with open("pokedex_pretty.json", "w") as f:
    json.dump(final_data, f, indent=2)