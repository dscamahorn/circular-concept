import config


def load_rag_context() -> str:
    cpr = config.load_file(config.CPR_RAG)
    fwu = config.load_file(config.FWU_RAG)
    return (
        f"[Consumer Packaging Reuse]\n{cpr}\n\n"
        f"[Food Waste and Upcycling]\n{fwu}"
    )