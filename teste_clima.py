from src.services.open_meteo_clima import buscar_clima


resultado = buscar_clima(
    latitude=-5.1875,
    longitude=-37.3442
)

print(resultado)