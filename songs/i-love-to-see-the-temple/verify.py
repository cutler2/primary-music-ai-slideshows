import json
from pathlib import Path
from PIL import Image, ImageFont

root=Path(__file__).resolve().parent
workspace=root.parents[2]/'work'
a=json.loads((workspace/'raw-template.json').read_text(encoding='utf-8'))['structuredContent']
b=json.loads((workspace/'raw-output.json').read_text(encoding='utf-8'))['structuredContent']
old=a['slides'][62:66]
song=b['slides'][62:70]
assert len(a['slides'])==115 and len(b['slides'])==119
def scrub(v):
    if isinstance(v,dict): return {k:scrub(x) for k,x in v.items() if k!='contentUrl'}
    if isinstance(v,list): return [scrub(x) for x in v]
    return v
outside=a['slides'][:62]+a['slides'][66:]
outside_final=b['slides'][:62]+b['slides'][70:]
assert [s['objectId'] for s in outside]==[s['objectId'] for s in outside_final]
assert all(scrub(s)==scrub(t) for s,t in zip(outside,outside_final)), 'Outside song changed'
def text(e): return ''.join(t.get('textRun',{}).get('content','') for t in e['shape']['text']['textElements'])
geometries=[]
mapping=[]
for i,s in enumerate(song):
    assert len(s['pageElements'])==3
    img,overlay,t=s['pageElements']
    assert 'image' in img and overlay['shape']['shapeType']=='RECTANGLE'
    original=''.join(text(e) for e in old[i//2]['pageElements'] if e.get('shape',{}).get('text'))
    expected='\n'.join(original.splitlines()[1:])
    assert text(t).rstrip('\n')==expected
    geometries.append((t['size'],t['transform']))
    split=len('\n'.join(expected.splitlines()[:2]))+1
    for run in t['shape']['text']['textElements']:
        if 'textRun' not in run or not run['textRun']['content'].strip(): continue
        st=run['textRun']['style']
        assert st['fontSize']['magnitude']==35 and st['bold'] and st['fontFamily']=='Arial'
        active=run.get('startIndex',0)<split if i%2==0 else run.get('startIndex',0)>=split
        c=st['foregroundColor']['opaqueColor']['rgbColor']
        rgb=(64/255,229/255,242/255) if active else (1,1,1)
        assert all(abs(c.get(k,0)-v)<1e-6 for k,v in zip(('red','green','blue'),rgb))
    fill=overlay['shape']['shapeProperties']['shapeBackgroundFill']['solidFill']
    assert abs(fill['alpha']-.42)<1e-6
    tf=img['transform']; assert abs(tf['scaleX']-tf['scaleY'])<1e-6
    def pt(x): return x['magnitude']/(12700 if x['unit']=='EMU' else 1)
    iw,ih=pt(img['size']['width']),pt(img['size']['height'])
    scale=tf['scaleX']; assert iw*scale>=720-.01 and ih*scale>=405-.01
    im=Image.open(root/'images'/f'{i+1:02}.png')
    mapping.append({'position':63+i,'slide_id':s['objectId'],'art':f'images/{i+1:02}.png','pixels':im.size,'block':'ABCD'[i//2],'active_lines':[1,2] if i%2==0 else [3,4]})
assert all(g==geometries[0] for g in geometries)
font=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',350)
widths=[(font.getlength(line)/10,line) for s in old for e in s['pageElements'] if e.get('shape',{}).get('text') for line in text(e).splitlines() if not line.startswith('VERSE')]
report={'result':'passed','total_slides':119,'title_position':62,'lyric_positions':[63,70],'lyric_count':8,'blocks':4,'verses_complete':2,'outside_slides_unchanged':len(outside),'font_pt':35,'longest_line_pt':max(widths),'mapping':mapping}
(root/'slide-map.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
