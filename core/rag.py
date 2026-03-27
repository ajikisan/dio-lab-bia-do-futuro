# 🧠 RAG — Retrieval Augmented Generation

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document


# 🏗️ 1 — Função para criar documentos
def criar_documentos(transacoes=None, historico=None, produtos=None, perfil=None):
    docs = []

    # 📊 Transações
    if transacoes is not None and not transacoes.empty:
        for row in transacoes.to_dict(orient="records"):
            docs.append(
                Document(
                    page_content=f"""
Tipo: {row.get('tipo')}
Categoria: {row.get('categoria')}
Valor: {row.get('valor')}
""".strip(),
                    metadata={"source": "transacoes"}
                )
            )

    # 📞 Histórico
    if historico is not None and not historico.empty:
        for row in historico.to_dict(orient="records"):
            docs.append(
                Document(
                    page_content=f"""
Atendimento em {row.get('data')} via {row.get('canal')}
Tema: {row.get('tema')}
Resumo: {row.get('resumo')}
Status: {"Resolvido" if str(row.get("resolvido")).lower() == "sim" else "Não resolvido"}
""".strip(),
                    metadata={"source": "historico"}
                )
            )

    # 💰 Produtos
    if produtos and isinstance(produtos, list):
        for p in produtos:
            docs.append(
                Document(
                    page_content=f"""
Produto: {p.get('nome')}
Categoria: {p.get('categoria')}
Risco: {p.get('risco')}
Rentabilidade: {p.get('rentabilidade')}
""".strip(),
                    metadata={"source": "produtos"}
                )
            )

    # 👤 Perfil
    if perfil and isinstance(perfil, dict):
        docs.append(
            Document(
                page_content=f"""
Perfil: {perfil.get('perfil_investidor', 'desconhecido')}
Renda: {perfil.get('renda_mensal', 0)}
Patrimônio: {perfil.get('patrimonio_total', 0)}
""".strip(),
                metadata={"source": "perfil"}
            )
        )

    return docs


# 🏗️ 2 — Criar base vetorial
def criar_vector_db(docs):
    if not docs:
        print("⚠️ Nenhum documento disponível para RAG")
        return None

    try:
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        vector_db = FAISS.from_documents(docs, embeddings)
        return vector_db

    except Exception as e:
        print("❌ Erro ao criar vector DB:", e)
        return None


# 🔎 3 — Busca semântica
def buscar_contexto(pergunta, vector_db, k=4):
    if vector_db is None:
        return ""

    try:
        resultados = vector_db.similarity_search(pergunta, k=k)

        if not resultados:
            return ""

        partes = []

        for r in resultados:
            fonte = r.metadata.get("source", "desconhecido")
            conteudo = (r.page_content or "")[:300].strip()

            partes.append(f"[{fonte}]\n{conteudo}")

        return "\n\n".join(partes)

    except Exception as e:
        print("❌ Erro na busca de contexto:", e)
        return ""