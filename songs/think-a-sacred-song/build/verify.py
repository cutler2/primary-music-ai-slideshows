import json
from pathlib import Path
from PIL import Image
root=Path(__file__).resolve().parents[1]
a=json.loads((root/'build/raw-template.json').read_text(encoding='utf-8'))['structuredContent']
b=json.loads((root/'build/raw-output.json').read_text(encoding='utf-8'))['structuredContent']
ids=json.loads((root/'build/presentation-plan.json').read_text())['ids']
def scrub(v):
    if isinstance(v,dict):return {k:scrub(x) for k,x in v.items() if k!='contentUrl'}
    if isinstance(v,list):return [scrub(x) for x in v]
    return v
outside=[s for s in a['slides'] if s['objectId'] not in ids]
assert all(scrub(s)==scrub(next(x for x in b['slides'] if x['objectId']==s['objectId'])) for s in outside)
assert [s['objectId'] for s in outside]==[s['objectId'] for s in b['slides'] if s['objectId'] not in ids]
song=[s for s in b['slides'] if s['objectId'] in ids]
assert [s['objectId'] for s in song]==ids
geometry=[]
for i,s in enumerate(song):
    t=next(e for e in s['pageElements'] if e.get('shape',{}).get('text'))
    geometry.append((t['size'],t['transform']))
    runs=[x for x in t['shape']['text']['textElements'] if 'textRun' in x]
    assert all(x['textRun']['style']['fontSize']['magnitude']==38 and x['textRun']['style']['bold'] and x['textRun']['style']['fontFamily']=='Arial' for x in runs)
    src=a['slides'][[53,53,54,54,55,55,56,56][i]]
    original=next(e for e in src['pageElements'] if e.get('shape',{}).get('text'))
    text=lambda e:''.join(x.get('textRun',{}).get('content','') for x in e['shape']['text']['textElements'])
    assert text(t)==text(original)
    split=len('\n'.join(text(t).split('\n')[:2]))+1
    for run in runs:
        start=run.get('startIndex',0)
        if not run['textRun']['content'].strip():continue
        active=(start<split) if i%2==0 else (start>=split)
        c=run['textRun']['style']['foregroundColor']['opaqueColor']['rgbColor']
        expected={'red':64/255,'green':229/255,'blue':242/255} if active else {'red':1,'green':1,'blue':1}
        assert all(abs(c[k]-expected[k])<1e-6 for k in expected)
    img=next(e for e in s['pageElements'] if 'image' in e)
    assert img['transform']['scaleX']==img['transform']['scaleY']
    assert img['size']['width']['magnitude']*img['transform']['scaleX']>=9144000-1
    overlay=next(e for e in s['pageElements'] if 'sacred_overlay' in e['objectId'])
    assert abs(overlay['shape']['shapeProperties']['shapeBackgroundFill']['solidFill']['alpha']-.42)<1e-6
assert all(g==geometry[0] for g in geometry)
print('PASS: eight full blocks, exact lyrics and emphasis, 38pt Arial Bold, identical text geometry, equal image scaling, full overlay, title and all other song structures/order unchanged.')
sheet=Image.new('RGB',(960,540),'#202020')
for i,n in enumerate(range(53,62)):
    im=Image.open(root/f'previews/{n}.png').resize((320,180))
    sheet.paste(im,((i%3)*320,(i//3)*180))
sheet.save(root/'previews/room-view.png')
