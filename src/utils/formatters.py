WEATHER_CODES = {
    0: "Céu limpo",

    1: "Principalmente limpo",
    2: "Parcialmente nublado",
    3: "Nublado",

    45: "Neblina",
    48: "Neblina com geada",

    51: "Garoa leve",
    53: "Garoa moderada",
    55: "Garoa intensa",

    56: "Garoa congelante leve",
    57: "Garoa congelante intensa",

    61: "Chuva leve",
    63: "Chuva moderada",
    65: "Chuva intensa",

    66: "Chuva congelante leve",
    67: "Chuva congelante intensa",

    71: "Neve leve",
    73: "Neve moderada",
    75: "Neve intensa",
    77: "Grãos de neve",

    80: "Pancadas de chuva leves",
    81: "Pancadas de chuva moderadas",
    82: "Pancadas de chuva violentas",

    85: "Pancadas de neve leves",
    86: "Pancadas de neve intensas",

    95: "Tempestade",

    96: "Tempestade com granizo leve",
    99: "Tempestade com granizo forte"
}


def traduzir_weather_code(code: int) -> str:
    return WEATHER_CODES.get(
    code,
    f"Condição desconhecida (code: {code})"
)