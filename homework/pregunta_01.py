"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import os
import string
import pandas as pd

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    df = pd.read_csv("files/input/solicitudes_de_credito.csv", index_col=0, sep=";")
    original = df["fecha_de_beneficio"].copy()
    df["fecha_de_beneficio"] = pd.to_datetime(
        original, errors="coerce", dayfirst=True
    )
    mask = df["fecha_de_beneficio"].isna()
    df.loc[mask, "fecha_de_beneficio"] = pd.to_datetime(
        original[mask], format="%Y/%m/%d", errors="coerce"
    )
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype("Int64")
    columnas = df.columns
    #idea_negocio y barrio no termina de limpiarse
    for columna in columnas:
        if df[columna].dtype == object:
            print(sorted(df[columna].value_counts().index.tolist()))
            df[columna] = (
                df[columna]
                .str.lower()
                .str.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))
                .str.replace("  ", " ", regex=False)
                .str.strip()
            )
            print(sorted(df[columna].value_counts().index.tolist()))
    df['línea_credito'] = df['línea_credito'].replace({
        "soli diaria": "solidaria"
    })
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(" ", "").astype("Int64")
    df.drop_duplicates(inplace=True)

    output_dir = "files/output/"
    output_data_path = "files/output/solicitudes_de_credito.csv"
    if os.path.exists(output_dir):
        os.remove(output_data_path)
    else:
        os.makedirs(output_dir)
    df.to_csv(output_data_path, sep=";", header=True, index=False)

if __name__ == "__main__":
    pregunta_01()
