def py_variable(statements):
   
   statements = statements.split()
   statements.remove('var')
   print(' '.join(statements))
   
def py_let(statements):
   
   statements = statements.split()
   statements.remove('let')
   print(' '.join(statements))
   
def py_const(statements):
   
   statements = statements.split()
   statements.remove('const')
   print(' '.join(statements))

def py_print(statements):
   
    print(statements.replace('console.log','print'))
    
def py_if_condition(statements):
      statements = statements.split()
      if '{' in statements:
         statements.remove('{')
      statements.append(':')
      print(''.join(statements))
      

def py_else(statements):
   
    statements = statements.split()
    for keyword in statements:
       if '}else' in keyword.strip():
          statements[statements.index(keyword)] = keyword.strip()[1:]
          break
       elif '}' in keyword:
          statements.remove('}')
          
    print(''.join(statements).replace('{',':'))

def py_elif_condition(statements):
   
   statements = statements.split()
   if statements[0] == '}':
         statements.remove('}')
   for keyword in statements:
      if '}else' in keyword:
         statements.remove(keyword)
         statements.insert(0,'el')
      elif '{' in keyword:
         statements[statements.index(keyword)] = keyword.replace('{',':')
      elif 'else' in keyword:
         statements.remove(keyword)
         statements.insert(0,'el')
   print(''.join(statements))
   
def py_def(statements):
   
   statements = statements.split()
   statements.remove('function')
   statements.insert(0,'def ')
   print(''.join(statements).replace('{',':'))
   
def py_while(statements):
   print(statements.replace('{',':'))

def py_for(statements):
   pass

"""def convert(file):

    with open(file,"r") as js:

        for statements in js.readlines():
            if 'var' in statements:
                py_variable(statements)
            elif 'if else' in statements:
                py_elif_condition(statements)
            elif 'if(' in statements:
                py_if_condition(statements)
            elif 'else' in statements:
                py_else(statements)
            elif 'console.log' in statements:
                py_print(statements)
"""

def testing(js_pro):
   for statements in js_pro.readlines():
      if 'var' in statements:
            py_variable(statements)
      elif 'let' in statements:
            py_let(statements)
      elif 'const' in statements:
            py_const(statements)
      elif 'else if' in statements:
            py_elif_condition(statements)
      elif 'if' in statements:
            py_if_condition(statements)
      elif 'else' in statements:
            py_else(statements)
      elif 'console.log' in statements:
            py_print(statements)
      elif 'function' in statements:
            py_def(statements)
      elif 'while' in statements:
            py_while(statements)
      elif '{\n' in statements:
         pass
      elif '}\n' in statements:
         pass
      else:
         if '}' not in statements:
            print(statements)

if __name__ == '__main__':                
   testing(open('javas.js','r'))
