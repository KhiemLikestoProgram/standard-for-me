from genericpath import isfile
from time import strftime
import sys, time, os

time_format = '%H:%M:%S %d/%m/%Y'
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

class std:
  def __init__(self):
    std.o('\033[1m\033[3m\033[4mNote\033[24m:\033[0m This is the standard (for me) library of Python 3.10. I\'m not related to Python or something. It\'s just a tool for me to program faster.')
  def o(*args,end='\n',sep=' ',slow=False):
    args = [str(i) if not isinstance(i,str) else i for i in args]
    if slow:  
      for i in sep.join(args):
        sys.stdout.write(i)
        time.sleep(0.1)
        sys.stdout.flush()
      sys.stdout.write(end)
    else:
      sys.stdout.write(sep.join(args)+end)
  def i(*prompts,end='\n',sep=' ',slow=False):
    if slow:
      for i in sep.join(prompts):
        sys.stdout.write(i)
        time.sleep(0.1)
        sys.stdout.flush()
      sys.stdout.write(end)
    else:
      sys.stdout.write(sep.join(prompts)+end)
    return input()
  def e(errorType: tError_base):
    std.o(str(type(errorType).__name__)+':',errorType.error)
    std.log('.\python\log.txt',f'Exit failed at {strftime(time_format)}.',0); exit()
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
  def sum(start,stop,/,expression):
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
      elif v == '': s.append(k)
      elif v == 'reset:': s.append('\033[0m'+k)
      elif v == ':reset': s.append(k+'\033[0m')
      else: std.e(t_valueError('The format value is not in the list right now. If you want to add it, please report it at the issues tab here: {insert github repo link here}'))
    return sep.join(s)+end+'\033[0m'
  def log(filename: str,message: str,level):
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
  def _(level=0):
    if level < 11:
      std._(level=level+1)
    else: std.o('\nRecursion...')