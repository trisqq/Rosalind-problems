# Словарь генетического кода
GENETIC_CODE: dict[str, str] = {
    "UUU": "F",
    "CUU": "L",
    "AUU": "I",
    "GUU": "V",
    "UUC": "F",
    "CUC": "L",
    "AUC": "I",
    "GUC": "V",
    "UUA": "L",
    "CUA": "L",
    "AUA": "I",
    "GUA": "V",
    "UUG": "L",
    "CUG": "L",
    "AUG": "M",
    "GUG": "V",
    "UCU": "S",
    "CCU": "P",
    "ACU": "T",
    "GCU": "A",
    "UCC": "S",
    "CCC": "P",
    "ACC": "T",
    "GCC": "A",
    "UCA": "S",
    "CCA": "P",
    "ACA": "T",
    "GCA": "A",
    "UCG": "S",
    "CCG": "P",
    "ACG": "T",
    "GCG": "A",
    "UAU": "Y",
    "CAU": "H",
    "AAU": "N",
    "GAU": "D",
    "UAC": "Y",
    "CAC": "H",
    "AAC": "N",
    "GAC": "D",
    "UAA": "Stop",
    "CAA": "Q",
    "AAA": "K",
    "GAA": "E",
    "UAG": "Stop",
    "CAG": "Q",
    "AAG": "K",
    "GAG": "E",
    "UGU": "C",
    "CGU": "R",
    "AGU": "S",
    "GGU": "G",
    "UGC": "C",
    "CGC": "R",
    "AGC": "S",
    "GGC": "G",
    "UGA": "Stop",
    "CGA": "R",
    "AGA": "R",
    "GGA": "G",
    "UGG": "W",
    "CGG": "R",
    "AGG": "R",
    "GGG": "G",
}


def translate_rna_to_protein(rna_seq: str) -> str:
    """Делит цепь РНК на триплеты и переводит их в аминокислоты.

    Args:
        rna_seq: строка РНК (символы A, C, G, U).

    Returns:
        Строка аминокислот. Трансляция останавливается на стоп-кодоне.
    """
    protein_letters: list[str] = []

    for i in range(0, len(rna_seq), 3):
        triplet = rna_seq[i : i + 3]
        amino = GENETIC_CODE.get(triplet, "")

        if amino == "Stop":
            break
        if amino:
            protein_letters.append(amino)

    return "".join(protein_letters)


def main() -> None:
    """Читает РНК из RNA.txt, транслирует и печатает белок.
    """
    with open("RNA.txt", "r") as f:
        rna = f.read().replace("\n", "").strip()

    peptide = translate_rna_to_protein(rna)
    print(peptide)


if __name__ == "__main__":
    main()
