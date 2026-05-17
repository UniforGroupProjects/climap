UFS_VALIDAS = {
    "AC", "AL", "AP", "AM", "BA", "CE", "DF",
    "ES", "GO", "MA", "MT", "MS", "MG", "PA",
    "PB", "PR", "PE", "PI", "RJ", "RN", "RS",
    "RO", "RR", "SC", "SP", "SE", "TO"
}

def validar_uf(uf: str) -> bool:
    uf = uf.upper()

    return (
        len(uf) == 2
        and uf.isalpha()
        and uf in UFS_VALIDAS
    )