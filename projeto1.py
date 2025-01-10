from time import sleep
import random


wordslist = ["significado", "perspectiva", "resiliência", "dissimulado", "vicissitude", "complacente", "contundente", "peremptório", "compreensão", "comorbidade", "perspicácia", "expectativa", "pressuposto", "subterfúgio", "beneplácito", "experiência", "preconceito", "consonância", "indiferente", "pretensioso", "transcender", "imensurável", "contingente", "intensidade", "necessidade", "proeminente", "beligerante", "superficial", "concernente", "benignidade", "contencioso", "inenarrável", "animosidade", "intervenção", "incumbência", "vocabulário", "cumprimento", "antagonismo", "resistência", "compreender", "indiferença", "reivindicar", "subsequente", "supracitado", "integridade", "diversidade", "estereótipo", "ambiguidade", "indulgência", "deliberação", "especulação", "divergência", "elucubração", "proveniente", "austeridade", "indubitável", "importância", "prognóstico", "tergiversar", "heterogêneo", "negligência", "estabelecer", "identificar", "displicente", "benevolente", "oportunista", "consciência", "conveniente", "redundância", "discriminar", "excepcional", "congruência", "pragmatismo", "providência", "admoestação", "substantivo", "conferência", "comprimento", "sistemático", "facultativo", "compulsório", "intersecção", "verborragia", "desenvolver", "melancólico", "subordinado", "intelectual", "relativizar", "dificuldade", "contradição", "honestidade", "substancial", "generalizar", "retificação", "amabilidade", "competência", "emblemático", "procedência", "conservador", "autoritário", "dicionário", "intrínseco", "prescindir", "presunçoso", "diligência", "corroborar", "intempérie", "detrimento", "parcimônia", "maturidade", "referência", "inspiração", "inexorável", "pragmático", "prepotente", "incipiente", "disruptivo", "serenidade", "sororidade", "iniquidade", "auspicioso", "arbitrário", "indulgente", "pertinente", "sagacidade", "hipocrisia", "resignação", "preconizar", "vislumbrar", "precedente", "incidência", "lisonjeado", "suscetível", "entretanto", "disposição", "excêntrico", "fleumático", "tribulação", "preliminar", "subestimar", "depreender", "anacrônico", "escrutínio", "excelência", "equivocado", "indolência", "ingerência", "democracia", "retrógrado", "infortúnio", "compassivo", "contemplar", "importante", "pejorativo", "restringir", "proposição", "sintetizar", "primordial", "subjacente", "intrínseca", "signatário", "conjuntura", "itinerário", "alteridade", "dissolução", "coercitivo", "no entanto", "finalidade", "esplêndido", "constância", "pecuniária", "necessário", "designação", "espontâneo", "transeunte", "pusilânime", "sarcástico", "disciplina", "felicidade", "privilégio", "verossímil", "exacerbado", "pernóstico", "idoneidade", "relevância", "desprovido", "inferência", "reverberar", "satisfação", "divergente", "pernicioso", "disseminar", "esporádico", "meticuloso", "influência", "retumbante", "fornicação", "consolidar", "resiliente", "etimologia", "perspicaz", "recíproco", "concessão", "impressão", "escrúpulo", "supérfluo", "retificar", "paradigma", "propósito", "dicotomia", "presunção", "concepção", "ratificar", "hipócrita", "plenitude", "implícito", "essencial", "corolário", "hegemonia", "incidente", "esdrúxulo", "altruísmo", "vagabundo", "altruísta", "hermético", "esperança", "aleatório", "confiança", "promíscuo", "persuadir", "deliberar", "sapiência", "indelével", "diligente", "demasiado", "mesquinho", "descrição", "impetuoso", "inusitado", "regozijar", "resignado", "compaixão", "prudência", "eminência", "discrição", "pretensão", "percepção", "ordinário", "explícito", "analítico", "exequível", "autonomia", "subjetivo", "nostalgia", "companhia", "resolução", "autóctone", "fidedigno", "dissensão", "paciência", "outrossim", "expressão", "supressão", "desdenhar", "constante", "taciturno", "imparcial", "ignorante", "autêntico", "arrogante", "consoante", "desumilde", "execrável", "obstinado", "discorrer", "jactância", "arcabouço", "restrição", "eloquente", "cognitivo", "interesse", "submissão", "adjacente", "instância", "limítrofe", "iminência", "sintético", "relevante", "presságio", "empecilho", "liberdade", "humildade", "excelente", "irascível", "ludibriar", "insensato", "plausível", "convicção", "aquisição", "primícias", "inerente", "respeito", "peculiar", "denegrir", "genocida", "anuência", "equidade", "deferido", "prudente", "essência", "iminente", "pandemia", "desgraça", "misógino", "eminente", "invasivo", "premissa", "alienado", "abstrato", "extensão", "empírico", "rapariga", "conceito", "ardiloso", "talarico", "ascensão", "reiterar", "devaneio", "lascívia", "prodígio", "relativo", "passível", "conserto", "inefável", "gratidão", "analogia", "destarte", "inserção", "modéstia", "remissão", "fomentar", "apologia", "ativista", "despeito", "inóspito", "medíocre", "monótono", "retórica", "concerne", "respaldo", "alicerce", "história", "proceder", "sinônimo", "perfídia", "primazia", "portanto", "complexo", "metódico", "rechaçar", "demagogo", "espectro", "critério", "consiste", "paradoxo", "amálgama", "suscitar", "sucumbir", "distinto", "singular", "abnegado", "comunhão", "notívago", "escárnio", "desfecho", "contexto", "objetivo", "processo", "refletir", "vocábulo", "elegível", "problema", "impávido", "obstante", "incrível", "maestria", "redenção", "desígnio", "epifania", "solícito", "mediante", "endêmico", "jurídico", "instigar", "reflexão", "preceito", "imanente", "paralelo", "insípido", "genérico"]


def comp_print(text, skips):
    for a in str(text):
        print(a, end="")
        sleep(0.05)
    if skips > 0:
        for b in range(int(skips)):
            print()


comp_print("Bem-vindo ao jogo de Adivinhação de Palavras!", 1)
life = 6
lster = ["_"]
chosen = (random.choice(wordslist)).upper()
print(chosen)
for h in range(len(chosen)-1):
    lster.append("_")
comp_print(f"A palavra tem {len(chosen)} letras: ", 0)
for i in range(len(lster)):
    print(lster[i], end="")
print()

while True:
    comp_print("Adivinha uma letra: ", 0)
    guess = (input()).upper()
    print(guess)
    if len(guess) == 1:
        for j in chosen:
            if chosen == guess:
                idx = lster.index("_")
                print(idx)
                lster[idx] = guess
        print(lster)
