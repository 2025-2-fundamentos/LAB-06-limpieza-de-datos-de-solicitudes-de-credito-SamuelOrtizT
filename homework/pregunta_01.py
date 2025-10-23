"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import os
import pandas as pd

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    def limpiar_texto(df, col_name):
        """Limpia la columna col_name del dataframe"""

        df = df.copy()
        df[col_name] = df[col_name].str.lower().str.replace(r"[ .-]", "_", regex=True).str.strip()

        return df

    df = pd.read_csv("files/input/solicitudes_de_credito.csv", index_col=0, sep=";")
    df.dropna(axis=0, inplace=True)
    df["sexo"] = df["sexo"].str.lower()
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype("Int64")
    df["fecha_de_beneficio"] = pd.to_datetime(
        df["fecha_de_beneficio"], dayfirst=True, format="mixed"
    )
    df["monto_del_credito"] = (
        df["monto_del_credito"]
        .str.removeprefix("$ ")
        .str.replace(",", "")
        .astype("float64")
    )

    unificables = ["tipo_de_emprendimiento", "idea_negocio", "barrio", "línea_credito"]
    for col_name in unificables:
        df = limpiar_texto(df, col_name)

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
