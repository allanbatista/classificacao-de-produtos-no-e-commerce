import re
 
re_html = re.compile(r"<[^>]*>")
re_especial = re.compile(r'^[\-\.\,]+|\s[\-\.\,]+|[\-\.\,]+\s|[\-\.\,]+$')
re_chars = re.compile(r'[^a-z0-9àáâãçéêíóôõúü+\-\"\s\.\,]')
re_lines = re.compile(r'\n')
re_spaces = re.compile(r'\s+')
 
tokens_norm = dict(
   zip(
       'æ,œ,á,è,ì,ò,ù,ä,ë,ï,ö,ü,ÿ,â,ê,î,ô,û,å,ø,Ø,ñ'.split(","),
       'ae,oe,a,e,i,o,u,a,e,i,o,u,y,a,e,i,o,u,a,o,O,n'.split(",")
   )
)
 
def _accent2latin(text):
   result = []
 
   for char in text.lower():
       newchar = tokens_norm.get(char)
 
       if newchar:
           result.append(newchar)
       else:
           result.append(char)
 
   return "".join(result)
 
 
def clear(text):
   text = str(text).lower()
   text = _accent2latin(text)
   text = re_html.sub(' ', text)
   text = re_chars.sub(' ', text)
   text = re_lines.sub(' ', text)
   text = re_especial.sub(' ', text)
   text = re_spaces.sub(' ', text)
   return text.strip()