import os,sys,json,base64,urllib.request
key=os.environ['OPENROUTER_API_KEY']
def gen(name,prompt,model='google/gemini-3.1-flash-image',ar='4:3'):
    body={"model":model,"modalities":["image","text"],"image_config":{"aspect_ratio":ar},
          "messages":[{"role":"user","content":prompt+" Photograph only: absolutely no text, letters, logos, watermarks or UI."}]}
    req=urllib.request.Request("https://openrouter.ai/api/v1/chat/completions",json.dumps(body).encode(),
        {"Authorization":"Bearer "+key,"Content-Type":"application/json"})
    r=json.load(urllib.request.urlopen(req,timeout=240))
    imgs=r['choices'][0]['message'].get('images')
    if not imgs: print(name,'NO IMAGE',json.dumps(r)[:300]); return
    url=imgs[0]['image_url']['url']; data=base64.b64decode(url.split(',',1)[1])
    open(f'photos/{name}.png','wb').write(data); print(name,'ok',len(data))
if __name__=='__main__':
    gen(sys.argv[1],sys.argv[2],ar=sys.argv[3] if len(sys.argv)>3 else '4:3')
