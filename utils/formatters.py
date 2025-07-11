import datetime

def format_ip(ip: str)-> str:
    # Remove caracteres não numéricos
    digits = "".join(filter(str.isdigit, ip))

    # Limita o tamanho a 12 dígitos
    digits = digits[:12]

    # Aplica a formatação do IP (XXX.XXX.XXX.XXX)
    formatted = ""

    if len(digits) > 9:
        formatted = f"{digits[:3]}.{digits[3:6]}.{digits[6:9]}.{digits[9:12]}"
    elif len(digits) > 9:
        formatted = f"{digits[:3]}.{digits[3:6]}.{digits[6:9]}-{digits[9:]}"
    elif len(digits) > 6:
        formatted = f"{digits[:3]}.{digits[3:6]}.{digits[6:]}"
    elif len(digits) > 3:
        formatted = f"{digits[:3]}.{digits[3:]}"
    else:
        formatted = digits

    return formatted

def format_port(port: str)-> str:
    # Remove caracteres não numéricos
    digits = "".join(filter(str.isdigit, port))

    # Limita o tamanho em 5 dígitos
    digits = digits[:5]

    # Aplica a formatação do NIP (XX.XXXX.XX)
    formatted = ""
    if len(digits) > 5:
        formatted = f"{digits[:2]}.{digits[2:5]}.{digits[5:]}"
    elif len(digits) > 2:
        formatted = f"{digits[:2]}.{digits[2:]}"
    else:
        formatted = digits
    return formatted

def format_date(date):
    """
    Formata o conteúdo de um campo de texto como uma data no formato DD/MM/AAAA, à medida que o usuário digita.

    :param date: Objeto de evento do Flet, contendo o campo (TextField) modificado.
    :return: None
    """
    # Remove caracteres não numéricos
    digits = "".join(filter(str.isdigit, date.control.value))

    # Limita o tamanho em 8 dígitos
    digits = digits[:8]

    # Aplica a formatação da DATA (XX/XX/XXXX)
    formatted = ""
    if len(digits) > 8:
        formatted = f"{digits[:2]}/{digits[2:4]}/{digits[4:8]}"
    elif len(digits) > 4:
        formatted = f"{digits[:2]}/{digits[2:4]}/{digits[4:]}"
    elif len(digits) > 2:
        formatted = f"{digits[:2]}/{digits[2:]}"
    else:
        formatted = digits

    # Critica data (se já tiver os 8 dígitos)
    if len(digits) == 8:
        try:
            dia = int(digits[:2])
            mes = int(digits[2:4])
            ano = int(digits[4:])

            # Regras Básicas
            if not (1 <= dia <= 31):
                raise ValueError("Dia Inválido")
            if not (1 <= mes <= 12):
                raise ValueError("Mês Inválido")
            if not (1900 <= ano <= 2100):
                raise ValueError("Ano inválido")

            # Verifica se é uma data real (ex: 31/02 falha)
            datetime(ano, mes, dia)

        except ValueError as e:
            date.control.error_text = f"Data Inválida"
        else:
            date.control.error_text = None  # Limpa o erro se tudo ok
    else:
        date.control.error_text = None  # Limpa o erro enquanto digita

    date.control.value = formatted
    date.control.update()