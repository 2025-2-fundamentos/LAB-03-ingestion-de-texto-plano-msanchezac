"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import re

def convertir_a_pd(head,columns):
    data_dict={}
    for i,column in enumerate(head):
        data_dict[column]=columns[i]
    df=pd.DataFrame(data_dict)
    return df

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

    filename='files/input/clusters_report.txt'
    head=[]
    clusters=[]
    cant_palabras=[]
    porcentaje_palabras=[]
    palabras_clave=[]

    with open(filename,mode="r") as data:
        
        for linea in data:
            if linea.startswith("--"):
                break
            if linea.strip()=="":
                continue
            linea_aux=re.sub(r"\s\s+", "-", linea)
            linea_aux=re.sub(" ", "_", linea_aux) 
            linea_aux=((linea_aux).lower()).split("-")
            

            if re.match(r"\s\s",linea):
                for i,palabra in enumerate(linea_aux):
                    head[i]=((head[i]+"_"+palabra).strip("_")).strip()    
            else:
                linea_aux.pop()
                head=linea_aux

        for linea in data:
            linea=linea.strip()
            if linea=="":
                continue
            if re.match(r"\d",linea):
                linea_aux=linea.split("%")
                linea_numeros=linea_aux[0].split()
                #agregar los números 
                clusters.append(int(linea_numeros[0]))
                cant_palabras.append(int(linea_numeros[1]))
                porcentaje_palabras.append(float(re.sub(",",".",linea_numeros[2])))

                #agregar las palabras clave
                linea_valores=linea_aux[1]
                linea_valores = re.sub(r"\s+", " ", linea_valores)
                palabras_clave.append(linea_valores)
              
            else:
                linea_aux=re.sub(r"\s+", " ", linea)
                palabras_clave[-1] += " " + linea_aux
                palabras_clave[-1] = (palabras_clave[-1].strip()).strip(".")
    
    return convertir_a_pd(head,[clusters,cant_palabras,porcentaje_palabras,palabras_clave])

pregunta_01()