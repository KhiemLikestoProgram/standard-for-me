"""
This library was made by [NGTKhiem]. If you have any suggestions or questions that are related to this program, report at https://github.com/KhiemLikestoProgram/standard-for-me/issues. 
All I want to say is:
 - There is no copyright. This library is for everyone.
 - All issues related to Copyright that are related to my program, please tell me, I don't want it to be taken down :(((
 - Also, like I said a bunch of times, farewell Technoblade, you're a legend, and a part of this generation grown up with your content. May you rest in peace. (1999-2022)
 - If you want to ask me unrelated questions, wait. You have to ask another question that is more related 😈😈 because I haven't find a place to ask yet. Maybe Twitter? or Discord? Here's my account and server:
 https://twitter.com/GiaKhiem_1009/
 https://discord.com/channels/897050868166295572/
"""
# DOCUMENT

from genericpath import isfile
from re import findall, finditer
from time import strftime
import sys, time, os, json, msvcrt, threading
os.system('cd '+os.path.dirname(__file__))
sysdo = os.system
# Imports that are preinstalled + move directory so easier to config and debug

with open('data\settings.jsonc','r') as js: cont = js.read()
SETTINGS = json.loads(cont)["settings"]

class tError_cpython(BaseException):
  pass
class tError_base:
  def __init__(self,error):
    self.error = error
class t_typeError(tError_base): pass
class t_valueError(tError_base): pass
class t_connectionError(tError_base): pass
class t_debugError(tError_base): pass
class standard:
  """
  standard:
  Use it for writing code faster or smt.
  """
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
  def i(*prompts,end=' ',sep=' ',slow=False,raw=False):
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
    std.log(f'Exit failed at {strftime(time_format)}.',0,std.dir); exit(1)
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
  def sum(expression,start=0,stop=10):
    s = 0
    if not (isinstance(start,int) and isinstance(start,int)):
      std.e(t_valueError('The start value or stop value is not a integer.'))
    if start > stop: std.e(t_valueError('The start value is larger than stop value.'))
    else:
      for i in range(start,stop+1):
        s += eval(expression.replace('i',str(i)))
      return s
  def open(self='',*files):
    for file in files:
      if isfile(file): sysdo('start'+file)
  def format(self='',*args,end='',sep=' '):
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
  def log(message: str,level,filename: str):
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
    if not isinstance(func,function): std.e(t_valueError('Invalid function to wrap.'))
    if level < max:
      time.sleep(sleep)
      func(args)
      std.recursionwrap(func,args[0],level=level+1,max=max,sleep=sleep)
    else: std.o(message)
  def split_i(prompt:str='> ',end='\n',sep=' ',slow=False,raw=False,lim=10):
    get = std.i(prompt,end=end,sep=sep,slow=slow,raw=raw).split()
    list = ['']*lim; get = get[:lim] if len(get) > 10 else get
    for i in range(len(get)):
      list[i] = get[i]
    return list
  def cmdl(prompt,commands): ...

class tools:
  def find(string: str,pattern,flags='rg'):
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
  def cls(line='all'):
    if line == 'all': sysdo('cls')
    elif isinstance(line,int): std.o(f'\0337\033[H\033[{line}B\033[2K \0338')
  def __version__():
    std.o('\033[1mtools v1.0.1 by Gia Khiem\033[0m')

# Variables
__filedir__ = os.path.dirname(__file__)
__filename__ = os.path.basename(__file__)
time_format = '%H:%M:%S %d/%m/%Y'
std = standard

# Imports that are may not be installed
try:
  from playsound import playsound
except:
  std.o('\033[38;5;178mDownload playsound because you do not install it yet...\033[0m')
  sysdo('pip install playsound')
try:
  import pyautogui as pyag
except:
  std.o('\033[38;5;178mDownload pyautogui because you do not install it yet...\033[0m')
  sysdo('pip install pyautogui')

if sys.version_info < (3,6):
  std.o('Sorry, but this library only works on version 3.6 or later.')
  exit(2)

# Seperate functions
def _loopSound():
  while 1: playsound(bg_dir,True)
def btw():
  std.o('Btw this is a secret function. But you have found it. OK. I will show you some facts about this library later.',slow=True)
def isint(*args):
  for arg in args:
    try:
      int(arg)
    except ValueError: return False
    except TypeError: return False
  return True
def fileviewer(dir='C:\Program Files (x86)',c=False):
  if os.path.isdir(dir):
    items = os.listdir(dir)
  else:
    std.o(dir)
    std.e(t_valueError('Invalid directory.'))
  highl = lambda str: f'\033[48;5;236m{str:100s}\033[49m'; pos = 0
  os.system('cls')
  if not c:
    while 1:
      std.o('\033[?25l'+dir); dir = os.path.normpath(dir)
      if len(items) > 15:
        for i in items[pos-5:pos+5]:
          if items[-1] != i:
            std.o('|---'+highl(i) if items[pos] == i else '|---'+i)
          else: std.o("'---"+highl(i) if items[pos] == i else "'---"+i)
      else:
        for i in items:
          if items[-1] != i:
            std.o('|---'+highl(i) if items[pos] == i else '|---'+i)
          else: std.o("'---"+highl(i) if items[pos] == i else "'---"+i)
      w = msvcrt.getwch()
      if w == "à": w1 = msvcrt.getwch()
      match w:
        case '\r':
          std.o(dir)
          try:
            if isfile(items[pos]) or ( os.path.isdir(dir+'\\'+items[pos]) and len(os.listdir(dir+'\\'+items[pos])) == 0 ): sysdo('explorer '+dir+'\\'+items[pos])
            else: fileviewer(dir+'\\'+items[pos]); std.o(f'\033[?25h'); break
          except PermissionError:
            std.e(t_debugError('Not enough permission.'))
        case '\b':
          os.system('cls')
          dir = os.path.normpath(dir)
          if dir != 'D:':
            fileviewer('\\'.join(dir.split(os.sep)[:-1]),False)
          else: fileviewer(dir+'\\',True)
        case 'à':
          if w1 == 'P':
            if pos < len(items)-1: pos += 1
          elif w1 == 'H': pos -= 1 if pos > 0 else pos
        case 'q': break
        case '\x03': std.o(f'\033[?25h',end=''); exit()
      os.system('cls')

# Driver code + clear log (change this in config.json if you don't want)
if strftime('%d') == '01' and SETTINGS['clear_log_file']:
  with open(os.path.dirname(__file__)+'\log.txt','r+') as f: f.truncate(0)
if __name__ == '__main__':
  match SETTINGS["Theme"]:
    case 'light':
      theme = json.load(open(__filedir__+'\\themes\light.json','r'))
      bg_dir = __filedir__+'\sounds\life.mp3'
    case 'dark':
      theme = json.load(open(__filedir__+'\\themes\dark.json','r'))
      bg_dir = __filedir__+'\sounds\life.mp3'
    case _:
      theme = json.load(open(__filedir__+'\\themes\default.json','r'))
      bg_dir = __filedir__+'\sounds\default.mp3'
  match SETTINGS["BackgroundMusic"]:
    case 'normal': bg_dir = __filedir__+'\sounds\life-could-be-dream.mp3'
    case None: pass
    case 'default' | _: bg_dir = __filedir__+'\sounds\default.mp3'

  if bg_dir is not None:
    loopThr = threading.Thread(target=_loopSound,name='BackgroundMusicThr')
    loopThr.daemon = True
    loopThr.start() # Thread for background music (im kinda stupid if compare with experts man im super bad)

  std.log('Successfully run standard-for-me at '+strftime(time_format),1,std.dir)
  while 1:
    bg = theme["Background"]; fg = theme["Foreground"]
    try:
      prompt=f'\033[48;2;{bg[0]};{bg[1]};{bg[2]}m\033[38;2;{fg[0]};{fg[1]};{fg[2]}m {__filename__} \033[49m\033[38;2;{bg[0]};{bg[1]};{bg[2]}m\033[39m';g=[]
      std.o(prompt,end=' ')
      g = [i for i in std.i('\033[38;5;62m',end='')]
      g = ''.join(g).split()+['']*(10-len(''.join(g).split()))
      std.o('\033[0m',end='')
      if   g[0] in ['exit','quit',':q']: break
      elif g[0] in ['cls','clear']: tools.cls()
      elif g[0] in ['fvw','fileviewer','fv']: 
        if not os.path.isdir(g[1]): fileviewer()
        else: fileviewer(g[1])
      elif g[0] in ['echo','std.o']:
        std.o(' '.join(g[1:]))
      elif g[0] in ['entry','std.i']:
        std.i('>')
      elif g[0] in ['multiline','mln','ml']:
        r = sys.stdin.readlines()
        exec('from standard_for_me import *\n%s' % (''.join(r)) )
      else:
        exec('from standard_for_me import *\n%s' % (' '.join(g)) )
    except KeyboardInterrupt: std.o('\033[F\033[0m')
    except:
      std.o('Oh no! something has gone wrong! Report it at https://github.com/KhiemLikesToProgram/standard-for-me/issues')
    