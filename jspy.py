"""
MIT LICENSE

Copyright 2021 (c) JSPY.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, 
modify, merge, publish,distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

#AUTHOR_NAME = HARISH M

__all__,version = ('convert'),'0.3.0'
   
def __py_variable(statements,lineno):
      
   """returns a valid python assignment statement"""
   
   return statements[:statements.find('var')]+statements.replace('var','').strip()+'\n'
   
def __py_let(statements,lineno):
      
   """returns a valid python assignment statement"""
   
   return statements[:statements.find('let')]+statements.replace('let','').strip()+'\n'

def __py_const(statements,lineno):
      
   """returns a valid python assignment statement"""
   
   return statements[:statements.find('const')]+statements.replace('const').strip()+'\n'

def __py_print(statements,lineno):
      
   """returns a valid python print statement"""
   
   return statements.replace('console.log','print')
    
def __py_if_condition(statements,lineno):
      
      """returns a valid python if statement"""
      
      if_condition = statements[statements.find('(')+1:statements.find(')')]
      return statements[:statements.find('if')]\
             +f"if {if_condition}:\n".replace('&&',' and ').replace('||',' or ').replace('!',' not ').replace('===','==').replace('{','').replace('/','//')
   
def __py_elif_condition(statements,lineno):
      
   """returns a valid python elif statement"""
   
   elif_condition = statements[statements.find('(')+1:statements.find(')')]
   return statements[:statements.find('else')]\
          +f'elif {elif_condition}:\n'.replace('&&',' and ').replace('||',' or ').replace('!',' not ').replace('===','==').replace('{','').replace('/','//')

def __py_def(statements,lineno):
      
   """returns a valid python function."""
   
   function_name = statements.split()[1]
   function_name = function_name[:function_name.find('(')]
   function_parameters = statements[statements.find('(')+1:statements.find(')')]
   py_function = statements[:statements.find('function')]+'def {}:\n'
   if function_parameters:
      return py_function.format(f'{function_name}({function_parameters})')
   else:
      return py_function.format(f'{function_name}()')

def __py_while(statements,lineno):
      
   """returns a valid python while statement"""
   
   py_while = statements[statements.find('(')+1:statements.find(')')]
   return statements[:statements.find('while')]+\
          f'while {py_while}:\n'.replace('&&',' and ').replace('||',' or ').replace('!',' not ').replace('===','==').replace('{','').replace('/','//')

def __py_for(statements,lineno):
      
   """returns a valid python for statement"""
   
   init_con_incre = statements[statements.find('(')+1:statements.find(')')].replace('/','//').split(';')
   itervar = init_con_incre[0][:init_con_incre[0].find('=')].split()[1]
   py_init,py_con,py_incre = '',[],[]

   for statement in init_con_incre:
      if 'var' in statement:
         py_init = statement[statement.find('=')+1:].strip()
      elif 'let' in statement:
         py_init = statement[statement.find('=')+1:].strip()
      elif '>=' in statement:
         py_con.append('>=')
         py_con.append(statement[statement.find('>=')+2:].strip())
      elif '<=' in statement:
         py_con.append('<=')
         py_con.append(statement[statement.find('<=')+2:].strip())
      elif '>' in statement:
         py_con.append('>')
         py_con.append(statement[statement.find('>')+1:].strip())
      elif '<' in statement:
         py_con.append('<')
         py_con.append(statement[statement.find('<')+1:].strip())
      elif '==' in statement:
         py_con.append('==')
         py_con.append(statement[statement.find('==')+2:].strip())
      elif '!=' in statement:
         py_con.append('!=')
         py_con.append(statement[statement.find('!=')+2:].strip())
      elif '+=' in statement:
         py_incre.append('+=')
         py_incre.append(statement[statement.find('+=')+2:].strip())
      elif '-=' in statement:
         py_incre.append('-=')
         py_incre.append(statement[statement.find('-=')+2:].strip())
      elif '*=' in statement:
         py_incre.append('*=')
         py_incre.append(statement[statement.find('*=')+2:].strip())
      elif '/=' in statement:
         py_incre.append('/=')
         py_incre.append(statement[statement.find('/=')+2:].strip())

   return generate_for_loop(itervar,py_init,py_con,py_incre,lineno,statements)

def  generate_for_loop(var,init,con,incre,lineno,statements):
   
   "return a formatted for loop to the __py_for()"
   
   for_loop = statements[:statements.find('for')]+'for {} in range({},{}):\n'
   if incre:
      match incre[0]:
         case '+=':
            if con[0] == '<':
               return for_loop.format(var,init,f"{con[1]},{incre[1]}")
            elif con[0] == '<=':
               return for_loop.format(var,init,f"{int(con[1])+1},{incre[1]}")
            else:
               raise Exception(f'Invalid statement at lineno {lineno}.')
         
         case '-=':
            if con[0] == '>':
               return for_loop.format(var,init,f"{con[1]},-{incre[1]}")
            elif con[0] == '>=':
               return for_loop.format(var,init,f"{int(con[1])-1},-{incre[1]}")
            else:
               raise Exception(f'Invalid statement at lineno {lineno}.')
         case '/=':
            if con[0] == '<':
               return for_loop.format(var,init,f"{con[1]},{incre[1]}")
            elif con[0] == '<=':
               return for_loop.format(var,init,f"{int(con[1])+1},{incre[1]}")
            elif con[0] == '>':
               return for_loop.format(var,init,f"{con[1]},-{incre[1]}")
            elif con[0] == '>=':
               return for_loop.format(var,init,f"{int(con[1])-1},-{incre[1]}")
            else:
               raise Exception(f'Invalid statement at lineno {lineno}.')
         case '*=':
            if con[0] == '<':
               return for_loop.format(var,init,f"{con[1]},-{incre[1]}")
            elif con[0] == '<=':
               return for_loop.format(var,init,f"{int(con[1])+1},-{incre[1]}")
            elif con[0] == '>':
               return for_loop.format(var,init,f"{con[1]},-{incre[1]}")
            elif con[0] == '>=':
               return for_loop.format(var,init,f"{int(con[1])-1},-{incre[1]}")
            else:
               raise Exception(f'Invalid statement at lineno {lineno}.')
   else:
      match con[0]:
         case '<':
            return for_loop.format(var,init,con[1])
         case '<=':
            return for_loop.format(var,init,int(con[1])+1)
         case '>':
            return for_loop.format(var,init,f"{con[1]},-1")
         case '>=':
            return for_loop.format(var,init,f"{int(con[1])-1},-1")

def __py_match(statements,lineno):
      
      """returns a valid python match statement"""
      
      if 'default' in statements:
            return statements.replace('default','case __').replace('{',':')
      return statements.replace('switch','match').replace('{',':')

def __py_length(statements,lineno):

   """ Returns the valid python length statement"""
   
   if 'for' in statements:
      
      py_for_loop = __py_for(statements,lineno)
      length_property = py_for_loop[py_for_loop.find(',')+1:py_for_loop.find('.length')].strip()
      
      return py_for_loop.replace(length_property+'.length','len('+length_property+')')
   
   elif 'var' in statements:
      print(statements)
   elif '=' in statements:
      print(statements)

def __runner(code):
      
      with open('converted_file.py','w') as file: file.write(code)
         
def convert(file,display = False):
   
   "Converts the javascript to python"
   
   source_code = ""
   lineno = 0
   with open(file) as js_pro:
      for statements in js_pro.readlines():
         lineno +=1
         if '.length' in statements:      __py_length(statements,lineno)
         elif 'for' in statements:        source_code +=__py_for(statements,lineno)
         elif 'var' in statements:        source_code +=__py_variable(statements,lineno)
         elif 'let' in statements:        source_code +=__py_let(statements,lineno)
         elif 'const' in statements:      source_code +=__py_const(statements)
         elif 'else if' in statements:    source_code +=__py_elif_condition(statements,lineno)
         elif 'if' in statements:         source_code +=__py_if_condition(statements,lineno)
         elif 'else' in statements:       source_code += statements[:statements.find('else')]+'else:\n'
         elif 'console.log' in statements:source_code +=__py_print(statements,lineno)
         elif 'function' in statements:   source_code +=__py_def(statements,lineno)
         elif 'while' in statements:      source_code +=__py_while(statements,lineno)
         elif 'switch' in statements:     source_code +=__py_match(statements,lineno)
         elif 'default' in statements:    source_code +=__py_match(statements,lineno)
         elif '}' not in statements:      source_code +=statements
         

   if display: print(source_code)
   else:       __runner(source_code)
   
if __name__ == '__main__':                
   convert(r'testing.js')
