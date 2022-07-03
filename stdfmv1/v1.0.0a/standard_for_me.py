"""
This library was made by [NGTKhiem]. If you have any suggestions or questions that are related to this program, report at https://github.com/KhiemLikestoProgram/standard-for-me/issues. 
All I want to say is:
 - There is no copyright. This library is for everyone.
 - All issues related to Copyright that are related to my program, please tell me, I don't want it to be taken down :(((
 - Also, like I said a bunch of times, farewell Technoblade, you're a legend, and a part of this generation grown up with your content. May you rest in peace. (1999-2022)
 - If you want to ask me unrelated questions, wait. If it is really useful / you really want to ask me, go to https://. Else, you have to ask another question that is more related 😈😈
"""

from genericpath import isfile
from re import findall, finditer
from time import strftime
import sys, time, os

time_format = '%H:%M:%S %d/%m/%Y'
def btw():
  std.o('Btw this is a secret function. But you have found it. OK. I will show you some facts about this library later.',slow=True)
def isint(*args):
  for arg in args:
    try:
      int(arg)
    except ValueError: return False
    except TypeError: return False
  return True
class tError_cpython(BaseException):
  pass
class tError_base:
  def __init__(self,error):
    self.error = error
class t_typeError(tError_base): pass
class t_valueError(tError_base): pass
class t_connectionError(tError_base): pass
class standard:
  dir = os.path.dirname(__file__)+'\log.txt'
  def __version__():
    std.o('\033[1mstandard v1.0.1 by Gia Khiem\033[0m')
  def o(*args,end='\n',sep=' ',slow=False):
    args = [str(i) if not isinstance(i,str) else i for i in args]
    if slow:
      for i in sep.join(args):
        sys.stdout.write(i); time.sleep(0.1); sys.stdout.flush()
      sys.stdout.write(end)
    else:
      sys.stdout.write(sep.join(args)+end)
  def i(*prompts,end='\n',sep=' ',slow=False,raw=False):
    if slow:
      for i in sep.join(prompts):
        sys.stdout.write(i)
        time.sleep(0.1)
        sys.stdout.flush()
      sys.stdout.write(end)
    else:
      sys.stdout.write(sep.join(prompts)+end)
    return input(r'') if raw else input()
  def e(errorType: tError_base):
    std.o(str(type(errorType).__name__)+':',errorType.error)
    std.log(std,f'Exit failed at {strftime(time_format)}.',0,std.dir); exit(1)
  def compare(*,x,y,mode):
    if mode in ['len','leng','length']:
      if len(x) < len(y): return '<'
      elif len(x) > len(y): return '>'
      else: return '='
    elif mode in ['num','number']:
      if not isinstance(x,int):
        if isint(x): x = int(x)
        else: return
      if not isinstance(y,int):
        if isint(y): y = int(y)
        else: return
      if x < y: return '<'
      elif x > y: return '>'
      else: return '='
    elif mode == 'array':
      if isinstance(x,(list,tuple,set)) and isinstance(y,(list,tuple,set)):
        for i in x+y:
          if not isinstance(i,int):
            if isint(i): i = int(i)
            else: return
        for i in zip(x,y):
          if i[0] > i[1]: return '>'
          elif i[0] < i[1]: return '<'
        return '='
      return
  def sum(self,start,stop,/,expression):
    s = 0
    if not (isinstance(start,int) and isinstance(start,int)):
      std.e(t_valueError('The start value or stop value is not a integer.'))
    if start > stop: std.e(t_valueError('The start value is larger than stop value.'))
    else:
      for i in range(start,stop+1):
        s += eval(expression.replace('i',str(i)))
      return s
  def open(*files):
    for file in files:
      if isfile(file): os.system('start'+file)
  def format(*args,end='',sep=' '):
    s = []; print(args)
    for k,v in args:
      if   v in ['bold:','b:']:
        s.append('\033[1m'+k)
      elif v in [':bold',':b']:
        s.append(k+'\033[22m')
      elif v in ['italic:','i:']:
        s.append('\033[3m'+k)
      elif v in [':italic',':i']:
        s.append(k+'\033[23m')
      elif v in ['underline:','u:']:
        s.append('\033[4m'+k)
      elif v in [':underline',':u']:
        s.append(k+'\033[24m')
      elif v in [':'+'0'*(3-len(hex(i)[2:]))+hex(i)[2:] for i in range(0,16**3)]: s.append(k+f'\033[38;2;{int(v[1],16)*16};{int(v[2],16)*16};{int(v[3],16)*16}m')
      elif v in ['0'*(3-len(hex(i)[2:]))+hex(i)[2:]+':' for i in range(0,16**3)]: s.append(f'\033[38;2;{int(v[0],16)*16};{int(v[1],16)*16};{int(v[2],16)*16}m'+k)
      elif v == '': s.append(k)
      elif v == 'reset:': s.append('\033[0m'+k)
      elif v == ':reset': s.append(k+'\033[0m')
      else: 
        std.e(t_valueError('The format value is not in the list right now. If you want to add it, please report it at the issues tab here: {insert github repo link here}'))
    return sep.join(s)+end+'\033[0m'
  def log(self,message: str,level,filename: str):
    with open(filename,'a') as f:
      match level:
        case 0 | 'status':
          f.write('[STATUS] '+message+'\n')
        case 1 | 'info':
          f.write('[INFO] '+message+'\n')
        case 2 | 'warning':
          f.write('[WARNING] '+message+'\n')
        case 3 | 'error':
          f.write('[ERROR] '+message+'\n')
        case 4 | 'critical':
          f.write('[CRITICAL] '+message+'\n')
  def recursionwrap(func,*args,level=0,max=11,sleep=0,message='\nRecursion...'):
    if level < max:
      time.sleep(sleep)
      func(args)
      std.recursionwrap(func,args[0],level=level+1,max=max,sleep=sleep)
    else: std.o(message)
  def split_i(prompt,end='\n',sep=' ',slow=False,raw=False,lim=10):
    get = std.i(prompt,end=end,sep=sep,slow=slow,raw=raw).split()
    list = ['']*lim; get = get[:lim] if len(get) > 10 else get
    for i in range(len(get)):
      list[i] = get[i]
    return list
  def cmdl(prompt,commands):
    pass
class tools:
  def find(self,string: str,pattern,flags='rg'):
    regex_, global_, normal_, first_ = 0,0,0,0
    if 'r' in flags and not regex_:
      if 'n' in flags: std.e(t_valueError('Invalid flag.'))
      regex_ = 1
    else: std.e(t_valueError('Invalid flag.'))
    if 'g' in flags and not global_:
      if 'f' in flags: std.e(t_valueError('Invalid flag.'))
      global_ = 1
    else: std.e(t_valueError('Invalid flag.'))
    if 'n' in flags and not normal_:
      if regex_: std.e(t_valueError('Invalid flag.'))
      normal_ = 1
    else: std.e(t_valueError('Invalid flag.'))
    if 'f' in flags and not first_:
      if global_: std.e(t_valueError('Invalid flag.'))
      first_ = 1
    else: std.e(t_valueError('Invalid flag.'))
    if not any([regex_,global_,normal_,first_]): std.e(t_valueError('Invalid flag.'))
    
    if normal_: 
      if first_: 
        if string.find(pattern) == -1:
          std.e(ValueError('Cannot find any matches.'))
        return string.find(pattern)
      if global_:
        pattern = ''.join([i if i not in ['+','*','?','^','$','(', ')','[',']','{','}','|','\\'] else '\\'+i for i in pattern])
        return [m.start() for m in finditer(pattern,string)]
    
    if regex_: 
      if first_: return findall(pattern,string)[0]
      if global_:
        return [m.start() for m in finditer(pattern,string)]
  def cls(self,line='all'):
    if line == 'all': os.system('cls')
    elif isinstance(line,int): std.o('\033[2K')
  def __version__():
    std.o('\033[1mtools v1.0.1 by Gia Khiem\033[0m')

std = standard
if strftime('%d') == '01':
  with open(os.path.dirname(__file__)+'\log.txt','r+') as f: f.truncate(0)
if __name__ == '__main__':
  std.log(std,'Successfully run standard-for-me at '+strftime(time_format),1,std.dir)
  std.o(tools.find(std,'pythonpython','py','rg'))