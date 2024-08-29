

import json




try:

   with open ('Climas.json','r') as file:
       data=json.load(file)
    
   print(data)    
   
   print("\n")

   print(f"El id del clima es:  {data['id']}")
   print(f"La descripcion es: {data['clima'][0].get('descripcion')}")
   print(f"La temperatura maxima es: {data['principal']['temp_max']}")
   print(f"La temperatura minima es: {data['principal']['temp_min']}")
   print(f"La sensacion es: {data['principal']['sensacion']}")

except Exception as e:
  print(f'El error es: {e}')
